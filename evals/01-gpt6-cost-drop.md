# Eval 01 · 「OpenAI 发布 GPT-6，推理成本再降 80%」

一条完整走通的样例，用来校准输出格式与质量。**新会话先读这一篇。**

---

## 输入

> 标题：OpenAI 发布 GPT-6，推理成本再降 80%
> 文案：GPT-6 在多模态推理上大幅提升，API 价格降至每百万 token 0.4 美元。行业竞争从拼参数转向拼成本，中小开发者迎来窗口期。

---

## 【意象提取】

| 槽位 | 取值 |
|------|------|
| `{{SUBJECT}}` | 一块刻着 `AI` 的芯片，边缘正在被"削价"削掉一角 |
| `{{NUMBER}}` | `-80%`（最大红色数字） |
| `{{POLARITY}}` | 中性偏利好 → 红蓝对撞 |
| `{{INDUSTRY}}` | 芯片、API 接口、服务器、价格标签 |
| `{{METAPHOR}}` | 价格断崖式下坠（红色下折线） |
| `{{SECTIONS}}` | 核心数据 / 价格变化 / 直接影响 |
| `{{TAKEAWAY}}` | 拼参数的时代结束了，拼成本的时代刚开始。 |

---

## 【底图提示词 · 英文】（MJ / Flux）

```
Chinese financial-news infographic cover TEMPLATE PLATE, 3:4 vertical, pure white paper background,
newspaper front-page grid, ABSOLUTELY NO TEXT of any kind - no letters, no numbers, no Chinese
characters, no placeholder glyphs, no lorem ipsum, every text area left as clean empty white space,
ultra-bold heavy black sans-serif Chinese typography reserved as blank areas (Source Han Sans Heavy
weight, uniform strokes, flat terminals, tight tracking, line-height 0.95) for later typesetting,
geometric extra-bold grotesque numerals reserved as blank areas (Archivo Black style),
strict 3-color system: China red #C41E1B, deep navy #0B2A5B, royal blue #12368F, plus ink black #111111,
flat two-tone vector icons (red and navy only, no gradients, no shadows), hairline dividers,
light pink panel #FDEDED and light blue panel #EAF1FA, full-width navy rule,
red-outlined warning bar with exclamation-mark circle,
layout: masthead strip 0-6% with a navy solid square at left and blank space at right,
full-width deep navy rule at 7%, blank date-line band at 8-9.5%,
headline zone 10-50% kept entirely blank white for 3-5 stacked left-aligned headline lines,
upper-right 35% x 22% of that zone holding a 3D render cutout of a single semiconductor chip
engraved with the letters "AI", one corner chipped away, with a bold red downward arrow and a jagged
price-drop polyline overlaying it, blank deck band at 52-54%, thin red rule at 55%,
three equal columns 56-84% each with a solid header bar alternating red / navy / red and left blank
inside, below it a flat two-tone red-and-navy vector icon of a chip, an API bracket symbol, a server
rack and a price tag, a blank block for an oversized red statistic, and blank space for 2-3 short body
lines, a simple red bar chart and a navy donut chart inside two of the panels,
red-outlined alert bar 85-96% with a white exclamation mark in a red circle at left and blank space
at right, hairline rule at 96-99%,
Swiss grid, 20px safe margins, near full-bleed content width 96%, generous negative space above,
vector-crisp print-ready edges, no gradient text, no outlined text, no 3D bevel text, no drop shadows
--ar 3:4 --style raw --stylize 100
```

## 【底图提示词 · 中文】（即梦 / Seedream）

取 `assets/prompt-baseplate.md` 中文版，替换：

- `【项目logo+项目名称】` → `项目 logo + 栏目名`
- `【核心主体】` → `一块刻着 "AI" 的芯片，边缘被削掉一角`
- `【行业符号】` → `芯片、API 接口、服务器、价格标签`
- `【关键数字】` → 留空（数字由压字阶段填）

## 【负面提示】

```
text, watermark, signature, garbled Chinese characters, misspelled letters, blurry,
low-res, jagged edges, jpeg artifacts, noise, gradient text, outlined text, 3D beveled text,
drop shadow text, glowing text, neon, cyberpunk, purple-teal color cast, pastel palette,
hand-drawn, sketch, watercolor, anime, cartoon mascot, illustration style, lens flare,
bokeh, depth of field, serif fonts, calligraphy, decorative script, gold foil, marble texture,
cluttered background, cluttered collage, rainbow palette, messy layout, uneven spacing,
element bleeding off canvas, centered typography, dark moody lighting, low contrast,
over-decorated, stock-photo watermark
```

MJ 追加：`--no text,letters,numbers,glyphs,placeholder,watermark`

---

## 【压字坐标表】（1086 × 1448）

| 区域 | y | 字号 | 字重 / 颜色 | 内容 |
|------|---|------|-------------|------|
| 刊头栏目名 | 20–78 | 48 px | Heavy / `#111111` | 栏目名 |
| 期号 | 10–70 | 66 px | Archivo Black / `#0B2A5B` | `01 / 02` |
| 日期行 | 112–138 | 23 px | Regular / `#111111` | 新闻日期 |
| 主标题 L1 | 145–280 | 128 px | Heavy / `#111111` | OpenAI 发布 GPT-6 |
| 主标题 L2 | 285–420 | 128 px | Heavy / `#111111` + 数字 `#C41E1B` | 推理成本**再降 80%** |
| 主标题 L3 | 425–560 | 128 px | Heavy / `#12368F` | 拼参数时代结束 |
| 主标题 L4 | 565–700 | 128 px | Heavy / `#111111` | 拼成本时代开始 |
| 导语 | 748–783 | 31 px | Medium，数字红 | API 价格降至每百万 token **0.4** 美元，中小开发者迎来窗口期。 |
| 三栏小标题 | 色条内 | 36 px | Bold / 白 | `01 核心数据` ｜ `02 价格变化` ｜ `03 直接影响` |
| 面板数字 | 面板中部 | 96 px | Archivo Black / `#C41E1B` | `-80%` ｜ `0.4 USD` ｜ `窗口期` |
| 面板正文 | 数字下方 | 27 px | Regular / `#111111`，行距 1.4 | 各 2 行 |
| 底部结论 | 警示条内 | 42 px | Heavy，关键词红 | 拼参数的时代结束了，拼成本的时代刚开始。 |
| 页脚 | 1393–1426 | 21 px | Regular / `#999999` | 免责声明 |

**自检 5 条**：① 缩到 20% 标题仍可读 ✓ ② 无文字压到配图块 ✓ ③ 红色只出现在 `-80%`、`0.4`、警示条、01/03 面板头 ✓ ④ 字重层级 = 3 ✓ ⑤ 四边留白 ≥ 20px ✓

---

## 交付物预期

1. **AI 产出**：1086 × 1448 白底**无文字**底图 —— 右上留白、右下芯片 + 红色下坠箭头、下半部三栏面板 + 底部红框结论条，所有文字位为纯白空带。
2. **压字后**：思源黑体 Heavy + Archivo Black 把四行标题（黑 / 红 / 蓝 / 黑）、导语、三栏、结论依次排入，导出 PNG 2x。
