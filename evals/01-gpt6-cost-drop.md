# Eval 01 · 「OpenAI 发布 GPT-6，推理成本再降 80%」

一条完整走通的样例，用来校准输出格式与质量。**新会话先读这一篇。**

> 版本说明：v2.0 起改为**代码生成**方案。本 eval 描述的是「写 HTML → 渲染 → 截图」的流程，
> 不再涉及任何 AI 生图提示词。

---

## 输入

> 标题：OpenAI 发布 GPT-6，推理成本再降 80%
> 文案：GPT-6 在多模态推理上大幅提升，API 价格降至每百万 token 0.4 美元。行业竞争从拼参数转向拼成本，中小开发者迎来窗口期。

---

## 第 0 步 · 意象提取

| 槽位 | 取值 |
|------|------|
| `{{SUBJECT}}` | 一块被削掉一角的芯片（价格被削） |
| `{{NUMBER}}` | `-80%`（最大红色数字） |
| `{{POLARITY}}` | 中性偏利好 → 红蓝对撞 |
| `{{INDUSTRY}}` | 芯片、API 接口、服务器、价格标签 |
| `{{METAPHOR}}` | 价格断崖式下坠（红色折线） |
| `{{SECTIONS}}` | 核心数据 / 价格变化 / 直接影响 |
| `{{TAKEAWAY}}` | 拼参数的时代结束了，拼成本的时代刚开始。 |

---

## 第 1 步 · HTML 关键片段

### ① 文字层 · 刊头（只放 logo + 项目名）

```html
<header class="masthead">
  <img class="logo" src="assets/logo-openai.png" alt="">
  <div class="name">OpenAI <em>GPT-6</em></div>
</header>
<div class="rule-navy"></div>
```

### ① 文字层 · 标题行（宽度归一）

```html
<h1 class="headline" id="headline"
    data-lines="OpenAI发布GPT-6|推理成本|再降 80%|拼成本时代开始"></h1>
```

```js
const RED  = new Set(['80%']);
const BLUE = new Set(['拼成本时代开始']);
// 其余同模板：拆成单字 span + flex space-between
```

> 字号核算：可用宽度 `1046 − 372 − 18 = 656px`，最长行 `OpenAI发布GPT-6`
> 约合 6 个中文当量 → `656 ÷ 6 ≈ 109px`。取 **88px** 留余量。

### ② 图标层

| 元素 | 来源 | 说明 |
|------|------|------|
| 项目 logo | `https://github.com/openai.png` | 项目仓库头像，真实素材 |
| 芯片图标 | Octicons `cpu-16.svg` | 成熟图标库仓库 |
| 价格标签 | Octicons `tag-16.svg` | 同上 |
| 服务器 | Octicons `server-16.svg` | 同上 |
| 主视觉 | SVG 手绘 | 深蓝主板 + 芯片阵列 + 红色下坠折线 |

全部**内联**进 HTML，`fill` 由 CSS 控制为 `var(--red)` / `var(--navy)`。

### ③ 内容框

```html
<section class="panels">
  <div class="panel p1">
    <div class="panel-head"><span class="no">01</span><span class="div"></span><span class="label">核心数据</span></div>
    <div class="panel-body">
      <div class="icon"><svg viewBox="0 0 16 16">…cpu…</svg></div>
      <div class="big">-80%</div>
      <div class="txt">推理成本大幅下探<br>降价幅度创纪录</div>
    </div>
  </div>
  <div class="panel p2">
    <div class="panel-head"><span class="no">02</span><span class="div"></span><span class="label">价格变化</span></div>
    <div class="panel-body">
      <div class="icon"><svg viewBox="0 0 16 16">…tag…</svg></div>
      <div class="big">0.4</div>
      <div class="txt">每百万 token 美元<br>中小开发者可负担</div>
    </div>
  </div>
  <div class="panel p3">
    <div class="panel-head"><span class="no">03</span><span class="div"></span><span class="label">直接影响</span></div>
    <div class="panel-body">
      <div class="icon"><svg viewBox="0 0 16 16">…server…</svg></div>
      <div class="big">窗口期</div>
      <div class="txt">竞争从拼参数<br>转向拼成本</div>
    </div>
  </div>
</section>
```

### ③ 内容框 · 底部警示条（红方块 + 白圈 + 加粗惊叹号）

```html
<section class="alert">
  <div class="alert-badge">
    <div class="alert-circle"><span class="bang">!</span></div>
  </div>
  <div class="alert-text">
    <div class="l1">拼参数的时代结束了，<em>拼成本</em>的时代刚开始。</div>
  </div>
</section>
```

---

## 第 2 步 · 渲染

```bash
python scripts/render.py cover.html out/cover.png 1086 1448 2
# OK -> out/cover.png  (2172 x 2896)
```

---

## 第 3 步 · 渲染后自检（对照 `references/anti-patterns.md`）

| # | 检查项 | 结果 |
|---|--------|------|
| 1 | 图标是红/蓝，不是黑色 | ✅ 内联 SVG + `fill:var(--red)` |
| 2 | 标题无溢出 | ✅ 最长行 6 当量 @88px = 528px < 656px |
| 3 | 无大片留白 | ✅ `.headline-zone{align-items:center}` |
| 4 | 中文字体生效 | ✅ Noto Sans SC 900，笔画清晰 |
| 5 | 导语单行 | ✅ 24 字 @32px ≈ 768px < 1046px |
| 6 | 红色未滥用 | ✅ 仅 `-80%` / `0.4` / 警示条 / 01·03 面板头 |
| 7 | 三栏等高 | ✅ grid 保证 |
| 8 | 面板正文 ≤ 3 行 | ✅ 各 2 行 |
| 9 | 警示条不挤压 | ✅ `padding:0 26px` |
| 10 | 页脚完整 | ✅ 各段 flex 之和 1408 < 1448 |
| 11 | 字重层级 = 3 | ✅ 900 / 500 |
| 12 | 标题未居中 | ✅ 两端对齐 |

**最后一步**：缩到 20% 看，标题仍一眼可读 ✅

---

## 交付物

1. `cover.html` —— 可继续编辑的源文件
2. `out/cover.png` —— 2172 × 2896 成品封面
3. 一句话设计取舍：把「价格下坠」做成主视觉里的红色折线，数字 `-80%` 占最大红色权重。

---

## 参考：一张真实成品

见 `examples/cover-awesome-dsh-plugin.html` 与 `.png` ——
用同一套模板为「DSH 插件生态 4412 个插件」生成的封面，中文零乱码。
