#!/usr/bin/env python3
"""dsh-cover · 把封面 HTML 渲染成成品 PNG。

用法:
    python render.py <html路径> <输出png路径> [宽] [高] [缩放]

默认: 1086 x 1448 @2x  ->  2172 x 2896 的 3:4 竖版封面。

依赖:
    pip install playwright
    **无需** `playwright install` —— 本脚本直接调用系统已装的 Chrome / Edge。

为什么不用 AI 生图:
    AI 生图模型无法可靠渲染中文字形。本脚本用真实浏览器排版 + 截图，
    中文由系统字体渲染，正确率 100%。
"""
import sys
import os
import pathlib

from playwright.sync_api import sync_playwright

# 按优先级探测本机浏览器
CHROME_CANDIDATES = [
    # Windows
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    # macOS
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    # Linux
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/usr/bin/microsoft-edge",
]


def find_browser():
    """返回本机浏览器的可执行路径；找不到返回 None（退回 Playwright 自带 Chromium）。"""
    for p in CHROME_CANDIDATES:
        if os.path.exists(p):
            return p
    return None


def render(html_path, out_path, width, height, scale):
    html_path = pathlib.Path(html_path).resolve()
    out_path = pathlib.Path(out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not html_path.exists():
        raise SystemExit(f"HTML 不存在: {html_path}")

    with sync_playwright() as p:
        launch_args = {
            # 关掉字体 hinting，让笔画更干净（更接近印刷感）
            "args": ["--font-render-hinting=none", "--disable-lcd-text"],
        }
        exe = find_browser()
        if exe:
            launch_args["executable_path"] = exe
            print(f"浏览器: {exe}")
        else:
            print("浏览器: Playwright 自带 Chromium（未找到系统 Chrome/Edge）")

        browser = p.chromium.launch(**launch_args)
        page = browser.new_page(
            viewport={"width": width, "height": height},
            device_scale_factor=scale,
        )
        page.goto(html_path.as_uri(), wait_until="load")
        page.wait_for_timeout(300)

        # 等字体与图片都就绪，否则会截到 fallback 字形
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(700)

        target = page.query_selector("#cover") or page
        target.screenshot(path=str(out_path))
        browser.close()

    print(f"OK -> {out_path}  ({width * scale} x {height * scale})")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        raise SystemExit(1)
    html = a[0]
    out = a[1] if len(a) > 1 else "cover.png"
    w = int(a[2]) if len(a) > 2 else 1086
    h = int(a[3]) if len(a) > 3 else 1448
    s = int(a[4]) if len(a) > 4 else 2
    render(html, out, w, h, s)
