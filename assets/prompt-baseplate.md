# ★ 无文字底图提示词（主模板）

> **输出目标：一张完全不含任何文字的 3:4 竖版底图。**
> 文字后续用思源黑体 Heavy + Archivo Black 压上去（坐标见 `references/typography.md`）。
> 替换 `【】` 或 `{{}}` 槽位即可使用。

---

## 中文版（即梦 / Seedream / 可画 / GPT-Image）

```
AI资讯信息图封面底图，3:4 竖版，纯白纸底报纸头版排版，画面中不出现任何文字、字母、数字或汉字：
顶部刊头栏左侧深蓝实心方块，右侧留白为【项目logo+项目名称】与期号位，其下通栏藏蓝粗分隔线；
上半部 40% 为主标题区，整块留白为纯白（预留 3–5 行超粗黑体大字的位置），
该区右上角 35% × 22% 留白并放置【核心主体】的 3D 渲染抠图，叠加一支粗红色向下箭头与锯齿状下跌折线；
其下留出一行导语的空白带，再一条通栏细红线；
56%–84% 为等宽三栏，每栏顶部实心色条按红 / 藏蓝 / 红交替（色条内保持纯色、不写字），
色条下方依次为：一枚扁平双色红蓝矢量图标（【行业符号】）、一块留白给超大红色统计数字【关键数字】、
再 2–3 行短正文的空白；面板底色为浅红 #FDEDED 与浅蓝 #EAF1FA；
再往下是红框白底警示条，左侧红色圆形内白色感叹号，右侧留白两行结论；
最底部一条发丝线配灰色小字位。严格三色系统：正红 #C41E1B、深藏蓝 #0B2A5B、
宝蓝 #12368F 加墨黑，纯白底；扁平双色矢量图标，无渐变无阴影；发丝分隔线；瑞士网格纪律；
四边 20px 安全边距，内容宽度接近满版；上留白下密排；矢量锐利印刷级边缘；
绝不出现渐变字、描边字、立体字、投影、白底纹理；
画面中不得出现任何文字、字母、数字、汉字、乱码或文字占位符线条
--ar 3:4
```

---

## 英文版（Midjourney / Flux / SDXL）

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
upper-right 35% x 22% of that zone holding a 3D render cutout of {{SUBJECT}} with a bold red
downward arrow and a jagged drop polyline, blank deck band at 52-54%, thin red rule at 55%,
three equal columns 56-84% each with a solid header bar alternating red / navy / red and left blank
inside, below it a flat two-tone red-and-navy vector icon, a blank block for an oversized red
statistic, and blank space for 2-3 short body lines, red-outlined alert bar 85-96% with a white
exclamation mark in a red circle at left and blank space at right, hairline rule at 96-99%,
Swiss grid, 20px safe margins, near full-bleed content width 96%, generous negative space above,
vector-crisp print-ready edges, no gradient text, no outlined text, no 3D bevel text, no drop shadows
--ar 3:4 --style raw --stylize 100
```

---

## 应急路径 · 带标题排版版（**不推荐**，仅当用户明确要求一次成图）

```
[风格锚点块] + [构图骨架块] +
Subject: {{SUBJECT}}, 3D tech render cutout at lower-right with a red arrow overlay,
headline typography: "{{TITLE_LINE_1}}" / "{{TITLE_LINE_2}}" / "{{TITLE_LINE_3}}" / "{{TITLE_LINE_4}}",
left-aligned, stacked, ultra-bold, one line filled in China red #C41E1B,
one key term in royal blue #12368F, remaining lines ink black,
masthead bar reading "{{COLUMN_NAME}}" at top-left and "{{ISSUE_NO}}" at top-right,
deck line reading "{{DECK}}" with the number highlighted in red,
three panel headers reading "01 {{SEC_1}}" / "02 {{SEC_2}}" / "03 {{SEC_3}}",
red alert bar reading "{{TAKEAWAY}}"
--ar 3:4
```

> ⚠️ 中文渲染成功率低。必须把标题控制在每行 8 个汉字以内、各行字数一致，并接受 2–3 次重抽。
> **默认路径永远是无文字底图 + 压字。**

---

## 参数建议

| 项 | 建议 |
|----|------|
| 尺寸 | 1086 × 1448（或任意 3:4，如 1152 × 1536 / 1536 × 2048） |
| 纯底图模型 | Midjourney v6.1、Flux、SDXL |
| Midjourney | `--ar 3:4 --style raw --stylize 100 --no text,letters,numbers,glyphs,watermark,gradient` |
| SD / Flux | CFG 4–6（低 CFG 更"平"更矢量），Steps 28–35，Sampler DPM++ 2M Karras |
| 后期 | 文字一律在 AI 之外压：Figma / PPT / HyperFrames / Photoshop，字体用思源黑体 Heavy + Archivo Black |
