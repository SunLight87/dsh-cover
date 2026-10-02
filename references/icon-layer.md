# 图标层 · 素材获取与内联规范

> 图标层是三层结构里的第二层，负责 logo、功能图标、装饰图形、主视觉插图。
> **核心原则：能下载真实素材就不要手画。**

## 一、素材优先级（必须按顺序尝试）

### 1️⃣ 项目自己的仓库（最优）
真实、可信、与内容一致。优先从这里取：

| 目标 | 取法 |
|------|------|
| 组织 / 项目头像 | `https://github.com/<org>.png` |
| 仓库内的 logo / 图标 | `https://raw.githubusercontent.com/<org>/<repo>/main/<path>` |
| README 里的截图 | 打开 README 找图片链接，直接下载 |
| 官网 favicon / og:image | `https://<site>/favicon.ico`、`<meta property="og:image">` |

```bash
curl -L -o assets/logo.png https://github.com/deepseek-ai.png
```

### 2️⃣ 成熟图标库仓库（次优）
- **Octicons**（GitHub 官方）：`https://raw.githubusercontent.com/primer/octicons/main/icons/<name>-16.svg`
  常用名：`plug` `tag` `terminal` `package` `stack` `cpu` `repo` `zap` `shield` `graph`
- **Simple Icons**（品牌 logo）：`https://cdn.simpleicons.org/<brand>/<hexcolor>`

### 3️⃣ SVG 手绘（兜底）
用 `<svg>` 直接画：电路板、箭头、柱状图、环形图、进度条、网格。

### 4️⃣ CSS 绘制（最后手段）
纯 CSS 做几何图形：圆点、色块、边框、条纹。

> ⚠️ **下载失败不要卡住。** 直接降级到 3 或 4，并在交付说明里提一句。
> 不要为了等一个图标把整张封面停下来。

## 二、必须内联，不要用 `<img>`

`<img src="x.svg">` 无法用 CSS 改颜色，会出现**黑色图标**（默认 fill）——这是最常见的翻车点。

**错误** ❌
```html
<div class="icon"><img src="assets/icon-terminal.svg" alt=""></div>
```

**正确** ✅ —— 把 SVG 的 `<path>` 内联进来，用 CSS 控制颜色
```html
<div class="icon">
  <svg viewBox="0 0 16 16"><path d="M0 2.75C0 1.784..."/></svg>
</div>
```
```css
.panel-body .icon svg{width:100%;height:100%;display:block;fill:var(--red);}
.panel.p2 .panel-body .icon svg{fill:var(--navy);}
```

> 位图（PNG/JPG，如项目 logo）**才**用 `<img>` —— 它们本来就带颜色。

## 三、配色纪律

| 位置 | 颜色 |
|------|------|
| 01 / 03 面板图标 | `var(--red)` |
| 02 面板图标 | `var(--navy)` |
| 主视觉插图底色 | `var(--navy)` 系渐变 `#0E2F63 → #061733` |
| 主视觉强调元素（箭头等） | `var(--red)` 系渐变 `#E23B33 → #B0180F` |
| 电路走线 | `#2E5FA8`，`opacity:.55` |
| 模块本体 / 发光核心 | `#16386F` / `#8FC3FF` |

**绝对不允许出现黑色图标或彩色（多色）图标。**

## 四、主视觉（`.hero-art`）的画法

右上角主视觉用一块 `372 × 330` 的 SVG 画布，四层结构：

1. **底** —— 深蓝线性渐变矩形
2. **电路走线** —— `<path>` 折线 + `<circle>` 焊点
3. **模块阵列** —— 用 JS 循环生成 `<rect>`（不要手写几百个）
4. **强调元素** —— 红色箭头，叠在最上层

```js
const tiles = document.getElementById('tiles');
const NS = 'http://www.w3.org/2000/svg';
const COLS = 6, ROWS = 5, S = 34, GAP = 14, X0 = 26, Y0 = 26;
for (let r = 0; r < ROWS; r++) {
  for (let c = 0; c < COLS; c++) {
    const x = X0 + c * (S + GAP), y = Y0 + r * (S + GAP);
    const g = document.createElementNS(NS, 'g');
    // 模块本体 + 发光核心，两次 createElementNS('rect')
    tiles.appendChild(g);
  }
}
```

## 五、图标尺寸

| 位置 | 尺寸 |
|------|------|
| 刊头项目 logo | `82 × 82`，`border-radius:14px` |
| 面板图标 | `68 × 68` |
| 警示条感叹号 | 白圈 `106 × 106`，字号 `82px` |

图标与相邻文字之间留 **≥ 12px** 呼吸位。
