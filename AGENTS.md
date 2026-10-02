# AGENTS.md · 维护约束

> 仅维护者需要读。使用者看 `SKILL.md` 和 `README.md`。

## 这个技能是什么

一个**代码生成型** Skill：AI 写 HTML/CSS/JS → 浏览器渲染 → 截图出封面。

## 硬性约束

1. **绝对不许引入 AI 生图。**
   不要加回 Midjourney / Flux / SD / 即梦 / Seedream / Agnes / Gemini Image 的任何调用、
   提示词模板或"底图 + 压字"流程。中文乱码正是本技能要解决的问题，
   改回生图等于把技能存在的理由删掉。

2. **风格锚点不可漂移。**
   `references/palette.md` 里的色值来自 19 张真实样本的像素级采样。
   改任何一个十六进制值都必须重新采样验证，不能凭感觉调。

3. **三条结构约束不可删**：
   - 刊头栏只放项目 logo + 项目名称（`60px/900`）
   - 标题字数少的行必须加宽（flex `space-between`）
   - 底部警示条 = 红色正方形底 + 白色圆圈 + 加粗惊叹号

4. **图标必须内联 SVG。**
   用 `<img src="x.svg">` 会渲染成黑色图标 —— 这是本项目最高频的翻车点。
   位图（PNG/JPG）才用 `<img>`。

5. **`{{NUMBER}}` 不得编造。** 数字只能来自用户给的文案。

6. **保持双语。** `README.md` 英文、`README.zh-CN.md` 中文，两边都要维护。

## 修改流程

1. 改 `references/` 下的规范文档。
2. 同步更新 `SKILL.md` 里对应的摘要。
3. 跑一遍：
   ```bash
   python scripts/render.py examples/cover-awesome-dsh-plugin.html out/test.png 1086 1448 2
   ```
   **必须打开图看**，逐条对照 `references/anti-patterns.md` 的 12 项。
4. 若改了模板，同步更新 `examples/` 里的 HTML 与 PNG。
5. 若新增了槽位，同步更新 `assets/extraction-table.md` 和 `SKILL.md` 第 0 步表。

## 目录约定

- `SKILL.md` —— 只放**流程与决策**，不放细节。细节下沉到 `references/`。
- `templates/` —— 可直接复制使用的成品 HTML。保持可运行、无外部 CDN 依赖。
- `scripts/` —— 可执行脚本。必须能独立运行，参数从命令行传入。
- `references/` —— 规范事实。可以长，但要能被单独读懂。
- `examples/` —— 一张真实成品（HTML + PNG + 素材），作为视觉基线。
- `evals/` —— 每加一种新封面类型（如深色冲击变体）就加一个 eval。

## 已知的取舍

- **不用 CDN 字体**：走本地 `file://` 路径，避免离线环境渲染成 fallback 字形。
- **不做自动出图**：技能只产出 HTML + PNG，不接任何图像 API。
- **不做图像编辑**：对已有成图修图改字是另一件事。
- **字号表是 1086 × 1448 基准**：换画幅时按比例缩放，不要重算。
