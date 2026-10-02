# dsh-cover

[![dsh-plugin](https://img.shields.io/badge/topic-dsh--plugin-blue)](https://github.com/topics/dsh-plugin)
[![DeepSeek Harness](https://img.shields.io/badge/DeepSeek%20Harness-skill-4B6BFB)](https://github.com/deepseek-ai/deepseek-harness)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111111)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![no AI image model](https://img.shields.io/badge/AI%20image%20model-not%20used-critical)](#why-code-instead-of-ai-image-generation)

**Cover generator for Chinese finance / AI-news infographics — code, not AI image generation.** An Agent Skill for DeepSeek Harness, Claude Code, Codex and Cursor.

Give it a **headline** or a **short article**. It writes **HTML/CSS/JavaScript**, renders it in a **real browser**, and screenshots the result into a finished PNG cover.

```
headline → ① extract imagery → ② write HTML/CSS/JS → ③ render in browser → ④ screenshot
```

[中文说明 →](README.zh-CN.md)

## Why code instead of AI image generation

AI image models cannot render Chinese characters. They produce shape statistics that look like Chinese but are not — every headline comes out garbled. This is a property of how the models work, not a prompt problem. This skill sidesteps it entirely:

| | AI image generation | This skill (code) |
|---|---|---|
| Chinese accuracy | ~0% (always garbled) | **100%** |
| Change one word | re-roll the dice | edit one line of HTML |
| Layout precision | luck | pixel-exact |
| Dependencies | image API + credits | just a browser |

**No AI image model is ever called.**

## Three-layer structure

Every cover is built from exactly three layers:

1. **Text layer** — title, subtitle, key data. Real fonts, proper hierarchy, 900/500 weights only.
2. **Icon layer** — assets are fetched **from the project's own repo first** (org avatar, `raw.githubusercontent.com` assets, README screenshots), then from established icon repos (Octicons, Simple Icons), and only then drawn as SVG or CSS.
3. **Content boxes** — bordered / filled / elevated containers holding the main text and data (three-column panel row, red alert bar).

## Style anchor

Extracted at pixel level from 19 real covers:

| Dimension | Spec |
|-----------|------|
| Canvas | 3:4 vertical, 1086 × 1448 logical px, screenshot @2x |
| Background | Pure white `#FFFFFF`, newspaper front page |
| Headline | Ultra-bold 900 weight, tracking -0.02em, line-height 1.0 |
| China red | `#C41E1B` — key numbers, key verbs, alert bar, panels 01/03 |
| Deep navy | `#0B2A5B` — masthead, full-width rule, panel 02 |
| Royal blue | `#12368F` — the emphasized *word* in the headline |
| Panel fills | Light pink `#FDEDED` / light blue `#EAF1FA` |
| Layout | Nine horizontal bands, 20px safe margins, 1046px content width |

Three structural rules that never change:

- **Masthead holds only the project logo + project name**, set large.
- **Short headline lines are widened** via flex `space-between` so every line ends up the same width.
- **The bottom alert bar is a red square + white circle + bold exclamation mark.**

## Layout

```
dsh-cover/
├── SKILL.md                      main workflow
├── templates/
│   └── cover-3x4.html            the 3:4 template (three layers, ready to fill)
├── scripts/
│   └── render.py                 Playwright render + screenshot
├── references/
│   ├── style-anchor.md           the immutable style spec
│   ├── layout-spec.md            nine-band CSS dimensions + line-width normalization
│   ├── palette.md                CSS variables + red/blue/black semantics
│   ├── typography.md             font stack, @font-face, size table
│   ├── icon-layer.md             asset sourcing order + SVG inlining rules
│   └── anti-patterns.md          12-point post-render checklist
├── assets/
│   └── extraction-table.md       the extraction table template
├── examples/
│   ├── cover-awesome-dsh-plugin.html
│   ├── cover-awesome-dsh-plugin.png
│   └── assets/                   real logos + Octicons downloaded from repos
└── evals/
    └── 01-gpt6-cost-drop.md      a fully worked example
```

## Install

See [INSTALL.md](INSTALL.md). Fastest path:

```powershell
# DeepSeek Harness (per-user skill directory)
Copy-Item -Recurse -Force . "$env:USERPROFILE\.dsh\skills\dsh-cover"
```

Runtime dependency: **Playwright** (`pip install playwright`). No browser download needed — the script drives your installed Chrome or Edge.

## Usage

```bash
# 1. fill templates/cover-3x4.html
# 2. render
python scripts/render.py templates/cover-3x4.html out/cover.png 1086 1448 2
```

Or just ask the agent:

> 做封面：DSH 插件生态已收录 4412 个插件

## Triggers

做封面, 生成封面, 封面图, 信息图封面, 封面提示词, 公众号封面, 小红书封面, 财经封面, 资讯封面, cover prompt, dsh-cover

## Not for

Video / animation, in-article illustrations, avatars, retouching or re-lettering an existing image.

## License

MIT
