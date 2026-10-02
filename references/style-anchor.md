# 风格锚点块（固定不变，直接复制）

> 从 `D:\skills\封面参考` 19 张样本实测提取。**任何一条提示词都必须带这块**，不要改写。

## 中文版

```
AI资讯信息图封面，报纸头版排版，3:4 竖版，纯白纸底 #FFFFFF，
超粗黑体大字报标题（思源黑体 Heavy 字重，笔画等宽、笔端平切、字距收紧），
几何特粗无衬线数字（Archivo Black 风格），
严格三色系统：正红 #C41E1B、藏蓝 #0B2A5B、宝蓝 #12368F，配墨黑 #111111，
扁平双色矢量图标（仅红蓝两色，无渐变无阴影），细发丝分隔线，
浅红面板底 #FDEDED 与浅蓝面板底 #EAF1FA，
通栏藏蓝粗分隔线，红框白底警示条配感叹号圆标，
右下角嵌入 3D 渲染 / 实拍抠图（科技金融题材），
瑞士网格排版，上半部大留白，印刷级锐利边缘，矢量清晰，
零渐变、零描边字、零立体字、零投影
```

## English

```
Chinese financial-news infographic cover, editorial newspaper front-page layout, 3:4 vertical,
clean white paper background #FFFFFF, print-ready,
ultra-bold heavy black sans-serif Chinese headline typography (Source Han Sans Heavy weight,
uniform strokes, flat terminals, tight tracking), geometric extra-bold grotesque numerals
(Archivo Black style), strict 3-color system: China red #C41E1B, deep navy #0B2A5B,
royal blue #12368F, plus ink black #111111,
flat two-tone vector icons (red and navy only, no gradients, no shadows),
hairline dividers, light pink panel #FDEDED and light blue panel #EAF1FA,
full-width navy rule, red-outlined warning bar with exclamation-mark circle,
3D render / photo cutout inset at lower-right (tech-finance subject),
Swiss grid, generous negative space in upper half, vector-crisp edges,
no gradient text, no outlined text, no 3D bevel text, no drop shadows
```

## 为什么是这几个词

| 关键词 | 作用 |
|--------|------|
| `editorial newspaper front-page layout` | 一句话锁定"报纸头版"这个版式母题 |
| `uniform strokes, flat terminals, tight tracking` | 把字体从"普通黑体"推到"超粗黑大字报" |
| `flat two-tone vector icons ... no gradients, no shadows` | 防止模型给图标加立体和渐变 |
| `generous negative space in upper half` | 防止模型把标题区填满 |
| `no gradient text, no outlined text, no 3D bevel text, no drop shadows` | 四条否决式约束，比正向描述有效 |

## 三种变体（按内容气质切换）

| 变体 | 触发条件 | 关键差异 |
|------|----------|----------|
| **A 完整信息图** | 内容含 ≥ 3 组数据 | 九段横带全开（默认） |
| **B 极简大字** | 单一爆点、标题即全部 | 删掉三栏与配图块，标题放大到占 70% 高度，底部只留一条细线 + 3 个参数 |
| **C 深色冲击** | 危机、暴跌、黑天鹅 | 底色换 `#06080E` 近黑，标题白 + 红，配图区加极淡暗色 lift，警示条保持红框白底 |
