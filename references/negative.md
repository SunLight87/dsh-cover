# 负面提示（每次必带）

## 中文版

```
文字, 水印, 签名, 乱码汉字, 错别字, 模糊, 低分辨率, 锯齿, JPEG 压缩伪影, 噪点,
渐变文字, 描边字, 立体字, 投影字, 发光字, 霓虹, 赛博朋克, 紫青色调, 马卡龙色,
手绘, 素描, 水彩, 动漫, 卡通吉祥物, 二次元, 插画感, 镜头光晕, 景深虚化, 散景,
衬线字体, 书法体, 艺术字, 烫金, 大理石纹理, 背景杂乱, 元素堆砌, 拼贴, 彩虹配色,
布局凌乱, 间距不均, 元素出血, 居中排版, 暗黑氛围, 低对比, 过度装饰
```

## English

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

## 出无文字底图时的加强版

走「无文字底图」流程时，负面提示里的文字项要从"避免出现"升级为**硬性禁止**：

**Midjourney**
```
--no text,letters,numbers,glyphs,placeholder,watermark,gradient
```

**SD / Flux**：把 negative 里 `text`、`garbled Chinese characters`、`placeholder glyphs` 的权重提到 **1.3–1.5**。

如果模型仍在留白区画了灰条或假字，追加：`caption bar, fake text blocks, lorem ipsum, typographic placeholder`。

## 常见失控与对策

| 症状 | 对策 |
|------|------|
| 留白区被填满 | 正向加 `generous negative space in upper half, keep the headline zone blank`；负面加 `cluttered, filled background` |
| 出现乱码汉字 | 负面权重提高；并确认正向已写 `ABSOLUTELY NO TEXT` |
| 图标被加上立体 / 渐变 | 正向 `flat two-tone vector icons, no gradients, no shadows`；负面 `3D icon, glossy icon, gradient icon` |
| 配色跑偏（出现紫 / 青 / 粉） | 负面加 `purple, teal, magenta, pastel`；正向重复三色十六进制值 |
| 标题居中 | 负面 `centered typography`；正向 `left-aligned, flush left` |
| 画面过暗 | 正向 `pure white paper background, bright even lighting`；负面 `dark moody lighting, low contrast` |
