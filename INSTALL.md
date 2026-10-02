# dsh-cover 安装指南

一个「文案 / 标题 → 信息图封面 PNG」的 Agent Skill，兼容 **DeepSeek Harness (DSH)**、**Claude Code**、**OpenAI Codex** 与 **Cursor**。

**用代码生成封面，不使用任何 AI 生图模型。**

## 目录结构

```
dsh-cover/
├── SKILL.md                      技能主文档（触发词 + 三步流程）
├── README.md / README.zh-CN.md   中英双语入口
├── INSTALL.md                    本文件
├── AGENTS.md                     维护约束（仅开发者需要）
├── package.json                  npm 元数据
├── LICENSE                       MIT
├── templates/cover-3x4.html      3:4 封面模板
├── scripts/render.py             渲染 + 截图脚本
├── references/                   六份规范文档，按需加载
├── assets/extraction-table.md    意象提取表模板
├── examples/                     一张真实成品（HTML + PNG + 素材）
└── evals/                        完整走通的样例
```

---

## 一、安装到 DeepSeek Harness（推荐）

DSH 的个人技能目录是 `~/.dsh/skills/`（Windows 即 `C:\Users\<用户名>\.dsh\skills\`）。

```powershell
# Windows
Copy-Item -Recurse -Force . "$env:USERPROFILE\.dsh\skills\dsh-cover"
```

```bash
# macOS / Linux
cp -R . ~/.dsh/skills/dsh-cover
```

最终路径为 `.../.dsh/skills/dsh-cover/SKILL.md`。重启 DSH 或重新加载技能后即可触发。

## 二、安装到 Claude Code

```bash
cp -R . ~/.claude/skills/dsh-cover          # 个人级
cp -R . <项目>/.claude/skills/dsh-cover     # 项目级
```

`SKILL.md` 的 frontmatter（`name` + `description`）与 Claude Code Agent Skill 规范兼容，无需改动。

## 三、安装到 OpenAI Codex

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\dsh-cover"
```

## 四、安装到 Cursor

放进项目或全局的 skills 目录，或直接把 `SKILL.md` 内容作为规则文件引入。

---

## 五、运行依赖

| 依赖 | 用途 | 安装 | 必需 |
|------|------|------|------|
| **Python 3.9+** | 跑渲染脚本 | 系统自带 | ✅ |
| **Playwright** | 驱动浏览器 | `pip install playwright` | ✅ |
| **Chrome 或 Edge** | 真实渲染引擎 | 系统通常已有 | ✅ |
| **Noto Sans SC / 思源黑体** | 中文超粗字 | Windows 10+ 自带 `NotoSansSC-VF.ttf` | ✅ |

### 关键：**不需要** `playwright install`

本技能的 `scripts/render.py` 直接调用**系统已安装的 Chrome / Edge**，
不需要下载 Playwright 自带的 Chromium（省 150MB + 几分钟）。

脚本按下列顺序自动探测：

```
Windows : C:\Program Files\Google\Chrome\Application\chrome.exe
          C:\Program Files\Microsoft\Edge\Application\msedge.exe
macOS   : /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
Linux   : /usr/bin/google-chrome  /usr/bin/chromium
```

全部找不到时，才会退回 Playwright 自带 Chromium（此时需要 `playwright install chromium`）。

### 字体检查

```powershell
Test-Path C:\Windows\Fonts\NotoSansSC-VF.ttf
```

若为 `False`，去 Google Fonts 下载 **Noto Sans SC**，或改用系统已有的微软雅黑粗体
（把模板里 `@font-face` 的 `src` 换成 `file:///C:/Windows/Fonts/msyhbd.ttc`）。

---

## 六、快速自检

```bash
python scripts/render.py examples/cover-awesome-dsh-plugin.html out/test.png 1086 1448 2
```

输出 `2172 × 2896` 的 PNG，内容与 `examples/cover-awesome-dsh-plugin.png` 一致，即安装成功。

**打开图看一眼**，逐条对照 `references/anti-patterns.md` 的 12 项检查。

---

## 七、卸载

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.dsh\skills\dsh-cover"
```

不写入任何其他位置，删除目录即完全卸载。
