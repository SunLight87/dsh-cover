# dsh-cover

[![dsh-plugin](https://img.shields.io/badge/topic-dsh--plugin-blue)](https://github.com/topics/dsh-plugin)
[![DeepSeek Harness](https://img.shields.io/badge/DeepSeek%20Harness-skill-4B6BFB)](https://github.com/deepseek-ai/deepseek-harness)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111111)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)](INSTALL.md)

**Cover-prompt generator for Chinese finance / AI-news infographic covers** — an Agent Skill for DeepSeek Harness, Claude Code, Codex and Cursor.

Give it a **headline** or a **short article**, and it returns:

1. **Image-idea extraction table** — subject / number / emotional polarity / industry symbols / metaphor / three column subtitles / closing line
2. **A text-free base-plate prompt** (Chinese + English, paste-ready)
3. **A typesetting coordinate table** — per-zone y position and font size (Source Han Sans Heavy + Archivo Black)

```
headline / copy  →  ① extraction table  →  ② text-free base-plate prompt  →  ③ typesetting table
```

[中文说明 →](README.zh-CN.md)

## Why two stages: base plate, then typeset

Image models lay out a page skeleton very well, but they cannot render Chinese text (garbled glyphs, missing strokes, wrong shapes). So this skill **never asks the model to write the headline**. The model produces a clean, completely text-free 3:4 base plate; the type is set afterwards in Figma / PPT / HyperFrames. Hit rate goes from roughly 20% to roughly 95%.

## Style anchor

Extracted at pixel level from 19 real cover samples:

| Dimension | Spec |
|-----------|------|
| Canvas | 3:4 vertical, 1086 × 1448 baseline |
| Background | Pure white `#FFFFFF`, newspaper front page |
| Headline type | Ultra-bold heavy black sans (Source Han Sans Heavy), uniform strokes, flat terminals, tracking -2% to -4%, line-height 0.95 |
| Numeral type | Geometric extra-bold grotesque (Archivo Black style), 1.2–1.6× the Chinese size |
| Three colors | China red `#C41E1B` ｜ deep navy `#0B2A5B` ｜ royal blue `#12368F`, with ink black `#111111` |
| Panel fills | Light pink `#FDEDED` / light blue `#EAF1FA` |
| Lighting | Flat everywhere except inside the cutout block, which gets realistic studio light |
| Layout | Nine horizontal bands on a Swiss grid, 20px safe margins, 96% content width |

## Layout

```
dsh-cover/
├── SKILL.md                      main workflow (triggers + three steps + output format)
├── references/
│   ├── style-anchor.md           the fixed style block (zh / en)
│   ├── layout-spec.md            nine-band grid + negative-space rules
│   ├── palette.md                color system + red/blue/black semantics
│   ├── typography.md             type system + typesetting coordinate table
│   ├── imagery.md                element library (subject, cutouts, icons, lighting)
│   └── negative.md               negative prompts + failure-mode fixes
├── assets/
│   ├── prompt-baseplate.md       ★ the text-free base-plate template
│   ├── prompt-oneline.md         one-paragraph quick version
│   └── extraction-table.md       extraction table template
└── evals/
    └── 01-gpt6-cost-drop.md      a fully worked example (quality bar)
```

## Install

See [INSTALL.md](INSTALL.md). Fastest path:

```powershell
# DeepSeek Harness (per-user skill directory)
Copy-Item -Recurse -Force . "$env:USERPROFILE\.dsh\skills\dsh-cover"
```

## Usage

After installing, just say:

> 做封面：OpenAI 发布 GPT-6，推理成本再降 80%

Or invoke `/dsh-cover` explicitly.

## Triggers

做封面, 生成封面, 封面图, 信息图封面, 封面提示词, 公众号封面, 小红书封面, 财经封面, 资讯封面, cover prompt, dsh-cover

## Not for

Video / animation, in-article illustrations, avatars, purely typographic posters that need no image generation, and retouching or re-lettering an existing image.

## License

MIT
