# 速用版 · 一段话通用提示词

> 用户给一段文案或标题时，把下面整段（含末尾粘贴位）一次性交给支持出图的大模型，
> 它会自己完成「意象提取 → 版式排布 → 出图」。只替换最后一行。

## 中文版

```
你是一位AI资讯封面设计师。我会给你一段【标题】或【文案】，请先自行提取：核心主体（一个能被画出来的具体物件）、最狠的数字锚点、情绪极性（下跌或风险→以红为主，增长或利好→红蓝对撞，中性→以蓝为主）、2–4 个行业符号、一个把新闻翻译成动作的隐喻，以及按「数据→变化→影响」归纳的三栏小标题和一句不超过 28 字的结论。

然后生成一张 3:4 竖版、完全不含任何文字的封面底图，所有文字位置一律留空，只输出排版骨架与视觉元素：纯白纸底，报纸头版式分区——顶部 0–6% 为刊头栏，左侧一个深蓝实心方块，右侧留出空白位给期号；6.8–7.3% 一条通栏藏蓝粗分隔线；7.7–9.5% 右侧留出日期行的空白带；上半部 10–50% 为主标题区，整块保持纯白空白，预留 3–5 行超粗黑体大字的位置，只在右上角 35%×22% 放置核心主体的 3D 渲染抠图，叠加一支粗红色向下箭头或锯齿状下跌折线；51.7–54.1% 留出一行导语的空白带；54.6–55.5% 一条通栏细红线；56.4–83.8% 为等宽三栏，每栏顶部是一条实心色条（按红 / 藏蓝 / 红交替，色条内保持纯色、不写字），色条下方依次放一枚扁平双色红蓝矢量图标、一块留白给超大红色数字、再留 2–3 行短正文的空白；面板底色为浅红 #FDEDED 与浅蓝 #EAF1FA；84.6–96.1% 为红框白底警示条，左侧红色圆形内白色感叹号，右侧留出两行结论的空白带；最底部一条发丝线配灰色小字位。严格三色系统：正红 #C41E1B、深藏蓝 #0B2A5B、宝蓝 #12368F 加墨黑，纯白底；扁平双色矢量图标，无渐变无阴影；发丝分隔线；瑞士网格纪律；四边 20px 安全边距、内容宽度接近满版；上留白下密排；矢量锐利印刷级边缘；绝不出现渐变字、描边字、立体字、投影或白底纹理，也不出现水印、模糊、噪点、衬线字体、书法体、手绘、动漫、赛博朋克、紫青色调。

画面中不得出现任何文字、字母、数字、汉字、乱码或文字占位符线条，所有文字位置一律留空为纯白。

我的文案是：【在此粘贴标题或文案】
```

## English

```
You are a Chinese financial-news cover designer. I will give you a headline or a short article;
first extract the core subject (one concrete drawable object), the single sharpest number,
the emotional polarity (fall or risk -> red-dominant; growth -> red-blue clash; neutral -> blue-dominant),
2-4 industry symbols, one metaphor that turns the news into an action, three column subtitles following
data -> change -> impact, and a closing line under 28 Chinese characters; then render one 3:4 vertical
cover BASE PLATE containing ABSOLUTELY NO TEXT: pure white paper background, newspaper front-page
layout - top masthead strip with a navy solid square at left and blank space at right, a full-width
deep navy rule, a right-aligned blank date-line band; the upper 40% is the headline zone kept entirely
blank white (reserved for 3-5 stacked left-aligned headline lines), while the upper-right 35% x 22%
holds a 3D-rendered cutout of the core subject with a bold red downward arrow or jagged drop polyline;
below it a blank one-line deck band, then a thin full-width red rule; from 56% to 84% three equal
columns, each with a solid header bar alternating red / navy / red left blank inside, below it a flat
two-tone red-and-navy vector icon, a blank block for an oversized red statistic and blank space for
2-3 short body lines, on light pink #FDEDED and light blue #EAF1FA panel fills; then a red-outlined
alert bar with a white exclamation mark in a red circle at left and blank space at right; finally a
hairline rule with a small grey disclaimer slot. Strict three-color system: China red #C41E1B,
deep navy #0B2A5B, royal blue #12368F plus ink black on pure white; flat two-tone vector icons with
no gradients or shadows; hairline dividers; Swiss grid discipline; 20px safe margins, near full-bleed
content width; generous negative space above and dense information below; vector-crisp print-ready
edges; never any gradient text, outlined text, 3D beveled text, drop shadows or texture on the white
background, and no watermark, garbled Chinese characters, blur, noise, serif fonts, calligraphy,
hand-drawn, anime, cyberpunk or purple-teal color cast. No letters, no numbers, no Chinese characters,
no placeholder glyphs anywhere. --ar 3:4 --style raw --stylize 100

My headline / copy is: 【PASTE HERE】
```

## 标准工作流 = 两段式

1. **第一段 · 出底图**：把上面整段丢给出图模型，产出一张**完全不含任何文字的 3:4 竖版底图**。
2. **第二段 · 压字**：在 **Figma / PPT / HyperFrames** 里用 **思源黑体 Heavy + Archivo Black** 把文字排进留白区。

为什么必须两段式：AI 画版式骨架很强，写中文字几乎必糊（乱码、缺笔画、字形错误）。
把「排版骨架」交给 AI、「文字渲染」交给字体，成品率从 ~20% 提到 ~95%。
