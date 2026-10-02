# dsh-cover

[![dsh-plugin](https://img.shields.io/badge/topic-dsh--plugin-blue)](https://github.com/topics/dsh-plugin)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111111)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![no AI image model](https://img.shields.io/badge/AI%20%E7%94%9F%E5%9B%BE-%E4%B8%8D%E4%BD%BF%E7%94%A8-critical)](#为什么用代码而不是-ai-生图)

**中文财经 / AI 资讯「信息图封面」生成器 —— 用代码画，不用 AI 生图。**
给 DeepSeek Harness、Claude Code、Codex、Cursor 用的 Agent Skill。

给它一段**标题**或**文案**，它编写 **HTML/CSS/JavaScript**，在**真实浏览器**里渲染，截图产出成品 PNG。

```
文案/标题 → ① 意象提取 → ② 写 HTML/CSS/JS → ③ 浏览器渲染 → ④ 截图出图
```

[English →](README.md)

## 为什么用代码而不是 AI 生图

AI 生图模型**画不出中文字**。它输出的是"看起来像中文"的形状统计，不是真的字 —— 每张封面标题必糊。
这是模型原理决定的，不是提示词能解决的。本技能直接绕开：

| | AI 生图 | 本技能（代码生成） |
|---|---|---|
| 中文正确率 | ~0%（必糊） | **100%** |
| 改一个字 | 重新抽卡 | 改一行 HTML |
| 布局精度 | 靠运气 | 像素级可控 |
| 依赖 | 生图 API + 额度 | 只需一个浏览器 |

**任何时候都不调用 AI 生图模型。**

## 三层结构

每张封面固定由三层构成：

1. **文字层** —— 标题、副标题、关键数据。真实字体，只用 900 / 500 两级字重。
2. **图标层** —— 素材**优先从项目自己的仓库下载**（组织头像、`raw.githubusercontent.com` 里的资产、README 截图），
   其次用成熟图标库仓库（Octicons、Simple Icons），最后才用 SVG 或 CSS 手绘。
3. **内容框** —— 带边框 / 背景 / 阴影的容器，承载主要文本与数据（三栏面板、红框警示条）。

## 风格锚点

来自 19 张真实封面样本的像素级分析：

| 维度 | 规格 |
|------|------|
| 画幅 | 3:4 竖版，1086 × 1448 逻辑像素，截图 @2x |
| 底色 | 纯白 `#FFFFFF`，报纸头版 |
| 标题字 | 超粗黑体 900 字重，字距 -0.02em，行高 1.0 |
| 正红 | `#C41E1B` — 关键数字、关键动词、警示条、01/03 面板头 |
| 深藏蓝 | `#0B2A5B` — 刊头、通栏分隔线、02 面板头 |
| 宝蓝 | `#12368F` — 标题里被强调的**词** |
| 面板底 | 浅红 `#FDEDED` / 浅蓝 `#EAF1FA` |
| 版式 | 九段横带，四边 20px 安全边距，内容宽度 1046px |

三条永不改动的结构约束：

- **刊头栏只放项目 logo + 项目名称**，字号要大。
- **标题字数少的行必须加宽**，用 flex `space-between` 让各行总宽一致。
- **底部警示条 = 红色正方形底 + 白色圆圈 + 加粗惊叹号**，三者缺一不可。

## 目录结构

```
dsh-cover/
├── SKILL.md                      主流程
├── templates/
│   └── cover-3x4.html            3:4 模板（三层结构，填内容即用）
├── scripts/
│   └── render.py                 Playwright 渲染 + 截图
├── references/
│   ├── style-anchor.md           不可变的风格规格
│   ├── layout-spec.md            九段横带 CSS 尺寸 + 标题行宽度归一
│   ├── palette.md                CSS 变量 + 红蓝黑语义
│   ├── typography.md             字体栈、@font-face、字号表
│   ├── icon-layer.md             图标层素材优先级 + SVG 内联规范
│   └── anti-patterns.md          渲染后 12 项必查清单
├── assets/
│   └── extraction-table.md       意象提取表模板
├── examples/
│   ├── cover-awesome-dsh-plugin.html
│   ├── cover-awesome-dsh-plugin.png
│   └── assets/                   从仓库下载的真实 logo 与 Octicons
└── evals/
    └── 01-gpt6-cost-drop.md      完整走通的样例
```

## 安装

见 [INSTALL.md](INSTALL.md)。最快的方式：

```powershell
# DeepSeek Harness（本机技能目录）
Copy-Item -Recurse -Force . "$env:USERPROFILE\.dsh\skills\dsh-cover"
```

运行时依赖：**Playwright**（`pip install playwright`）。**不需要下载浏览器** —— 脚本直接驱动你已装的 Chrome 或 Edge。

## 用法

```bash
# 1. 填 templates/cover-3x4.html
# 2. 渲染
python scripts/render.py templates/cover-3x4.html out/cover.png 1086 1448 2
```

或者直接对 Agent 说：

> 做封面：DSH 插件生态已收录 4412 个插件

## 触发词

做封面、生成封面、封面图、信息图封面、封面提示词、公众号封面、小红书封面、财经封面、资讯封面、cover prompt、dsh-cover

## 不适用

视频 / 动画、正文配图、头像、对已有成图修图改字。

## License

MIT
