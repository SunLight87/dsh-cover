# 构图骨架 · 九段横带（CSS 尺寸表）

> 从 19 张真实封面样本的逐行墨量分析得到。逻辑画布 **1086 × 1448**，截图 @2x → **2172 × 2896**。

## 尺寸表

| # | 区域 | CSS 类 | 高度 | 说明 |
|---|------|--------|------|------|
| 1 | 刊头栏 | `.masthead` | `96px` | 左：项目 logo `82×82` + 项目名称 `60px/900` |
| 2 | 藏蓝粗线 | `.rule-navy` | `8px` | `background: var(--navy)` |
| 3 | 主标题区 | `.headline-zone` | `flex:1 1 auto` | 标题 4 行 + 右上角图标层 |
| 4 | 导语 | `.deck` | auto | `32px/500`，含一个红色数字 |
| 5 | 红色细线 | `.rule-red` | `4px` | `background: var(--red)` |
| 6 | 三栏内容框 | `.panels` | `372px` | `grid-template-columns: 1fr 1fr 1fr` |
| 7 | 底部警示条 | `.alert` | `158px` | 红方块 + 白圈 + 加粗惊叹号 |
| 8 | 页脚 | `.footer` | `46px` | `21px` 灰色 + 1px 顶边线 |

安全边距：`.cover { padding: 20px }`，内容宽度 `1046px`（96.3%）。

## 主标题区内部

```css
.headline-zone{
  flex:1 1 auto;
  display:flex; gap:18px;
  align-items:center;      /* 垂直居中 —— 消除标题下方大片留白 */
  padding-top:26px;
}
.headline{flex:1 1 auto; display:flex; flex-direction:column; justify-content:center;}
.hero-art{flex:0 0 372px; width:372px; height:330px;}
```

## ⭐ 标题行宽度归一（本风格最关键的排版技巧）

需求：**字数少的标题行要加宽，让各行总宽一致**。
用 flex 两端对齐实现，**不要**用 `text-align: justify`（对最后一行无效）。

```css
.hl{
  display:flex; justify-content:space-between; align-items:baseline;
  width:100%; line-height:1.0;
  font-size:88px; font-weight:900; letter-spacing:-.02em;
  margin-bottom:18px;
}
.hl:last-child{margin-bottom:0;}
.hl span{display:inline-block;}
```

```js
// 把每行拆成单字 span；数字/英文连成一个 token，中文逐字
h.dataset.lines.split('|').forEach(function (line) {
  const row = document.createElement('div');
  row.className = 'hl';
  (line.match(/[0-9A-Za-z.]+|\s+|./gu) || []).forEach(function (t) {
    const s = document.createElement('span');
    s.textContent = t;
    if (t.trim() === '') s.style.flex = '0 0 auto';   // 空格不参与撑开
    row.appendChild(s);
  });
  h.appendChild(row);
});
```

**字号上限公式**：`font-size ≤ 可用宽度 ÷ 最长一行的 token 数`

> 例：可用宽度 `1046 − 372 − 18 = 656px`，最长一行 7 个字 → `656 ÷ 7 ≈ 93px`，取 **88px** 留余量。

## 构图逻辑四条法则

1. **上留白、下密排** —— 上半只有大字，下半塞满信息。
2. **Z 字形动线** —— 刊头 → 大标题 → 导语 → 三栏 → 底部红条，每段用分隔线"关闸"。
3. **三段式叙事** —— `01 数据 → 02 变化 → 03 影响`。
4. **斜对角平衡** —— 左上大标题、右上图标层、左下第一栏，三角撑住画面。

## 三种变体

| 变体 | 触发条件 | 关键差异 |
|------|----------|----------|
| **A 完整信息图** | 内容含 ≥ 3 组数据 | 九段横带全开（默认，即模板） |
| **B 极简大字** | 单一爆点、标题即全部 | 删掉 `.panels` 与 `.hero-art`，`.hl` 字号提到 `120px`，底部只留细线 + 3 个参数 |
| **C 深色冲击** | 危机、暴跌、黑天鹅 | `.cover` 底色换 `#06080E`，标题白 + 红，警示条保持红框白底 |
