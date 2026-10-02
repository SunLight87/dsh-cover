# 反模式清单（渲染后必查）

> 代码生成方案不会出现乱码，但会出现**排版事故**。每次渲染完必须用读图工具看一眼，
> 逐条对照下面 12 项。**不要只确认文件生成了就交付。**

## A. 必查 12 项

| # | 检查项 | 症状 | 修法 |
|---|--------|------|------|
| 1 | **图标是黑色** | 面板图标呈纯黑 | SVG 没内联，用了 `<img>`。改成内联 + `fill:var(--red)` |
| 2 | **标题溢出** | 最长一行超出右边界或被裁切 | 按公式降字号：`可用宽度 ÷ 最长行 token 数` |
| 3 | **留白过大** | 标题与导语之间出现大片空白 | `.headline-zone{align-items:center}`，或给 `.headline` 加 `justify-content:center` |
| 4 | **字体没生效** | 中文变成细体 / 衬线体 | `@font-face` 路径错；确认 `file:///` 三斜杠；确认等到了 `document.fonts.ready` |
| 5 | **导语换行难看** | 一句话被拆成两行且断在词中间 | 缩短文案，或降到 `28px` |
| 6 | **红色滥用** | 红色出现在非数字、非警示条的位置 | 红色只允许：数字、关键动词、警示条、01/03 面板头 |
| 7 | **三栏高度不齐** | 面板底边参差 | `.panels{display:grid}` 保证等高；`.panel{display:flex;flex-direction:column}` |
| 8 | **面板文字超 3 行** | 正文挤出面板 | 删字，不要缩字号 |
| 9 | **警示条挤压** | 结论文字贴到白圈上 | `.alert-text{padding:0 26px}` |
| 10 | **页脚被切** | 免责声明只露一半 | 检查总高度：各段 `flex` 之和 ≤ `1448 − 40` |
| 11 | **出现第四种字重** | 画面显得杂乱 | 全图只用 900 / 500 两级 |
| 12 | **标题居中** | 失去报纸感 | 一律 `justify-content:space-between`（两端对齐），不要 `center` |

## B. CSS 禁用清单

```css
/* ❌ 全部禁止 */
background:linear-gradient(...);        /* 用在文字上 */
-webkit-background-clip:text;           /* 渐变字 */
-webkit-text-stroke:1px ...;            /* 描边字 */
text-shadow:0 2px 4px ...;              /* 文字投影 */
box-shadow:0 8px 24px rgba(0,0,0,.3);   /* 重投影（面板只允许极淡或无） */
border-radius:50px;                     /* 大圆角（≤8px） */
filter:blur(...);                       /* 模糊 */
transform:rotate(...);                  /* 旋转文字 */
text-align:center;                      /* 用于主标题 */
font-family:serif;                      /* 衬线体 */
```

## C. 常见失控与对策

| 症状 | 对策 |
|------|------|
| 面板图标黑色 | 内联 SVG（见 `icon-layer.md`） |
| 标题行宽度参差 | 确认 `.hl` 是 `display:flex; justify-content:space-between`，且每字一个 `<span>` |
| 空格把行撑开 | JS 里给空格 `s.style.flex='0 0 auto'` |
| 数字与中文基线不齐 | `.hl{align-items:baseline}` |
| 截图截到 fallback 字体 | `render.py` 里 `page.evaluate("document.fonts.ready")` 后多等 700ms |
| 图片没加载 | `wait_until="load"`；本地图片用相对路径，HTML 与 `assets/` 同级 |
| 输出尺寸不对 | 参数是 `宽 高 缩放`，@2x 时实际输出 = `宽×2 × 高×2` |

## D. 交付前最后一问

**把成品缩到 20% 看**，标题是否仍然一眼可读？
封面在小红书 / 视频号信息流里就是这个尺寸。读不清就加大字号、删字，不要加装饰。
