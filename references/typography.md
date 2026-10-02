# 字体系统

> 代码生成方案下，字体是**真实字体**，不是 AI 画出来的形状 —— 这是中文不乱码的根本原因。

## 一、字体栈与 @font-face

```css
@font-face{
  font-family:'NotoSansSC';
  src:url('file:///C:/Windows/Fonts/NotoSansSC-VF.ttf') format('truetype');
  font-weight:100 900;      /* 可变字体，直接取 900 = Black */
  font-display:block;
}
```

**跨平台路径**

| 系统 | 路径 |
|------|------|
| Windows | `C:/Windows/Fonts/NotoSansSC-VF.ttf`（兜底 `msyhbd.ttc` 微软雅黑粗体） |
| macOS | `/System/Library/Fonts/PingFang.ttc` |
| Linux | `/usr/share/fonts/opentype/noto/NotoSansCJK-Black.otf` |

**字体栈**

```css
font-family:'NotoSansSC','PingFang SC','Microsoft YaHei',sans-serif;
```

> `file://` 路径必须写三个斜杠（`file:///C:/...`），且不能有未转义的空格。
> `render.py` 会在截图前 `await document.fonts.ready`，否则会截到 fallback 字形。

## 二、三级字重（全图只用 3 级）

| 层级 | 用途 | font-size | font-weight | letter-spacing |
|------|------|-----------|-------------|----------------|
| **L1 超粗** | 主标题、面板大数字、警示条结论 | 88 / 82 / 44px | **900** | -0.02em ~ -0.03em |
| **L2 中粗** | 刊头项目名、面板小标题、导语 | 60 / 30 / 32px | **900 / 500** | 0 |
| **L3 常规** | 面板正文、页脚 | 24 / 21px | **500** | 0 |

数字额外加 `font-variant-numeric: tabular-nums;`，让三栏的 `4412 / 23 / 1` 对齐干净。

## 三、完整字号表（1086 × 1448 基准）

| 元素 | 选择器 | font-size | weight | 颜色 |
|------|--------|-----------|--------|------|
| 刊头项目名 | `.masthead .name` | 60px | 900 | `--ink` + `--navy` 强调 |
| 主标题 | `.hl` | 88px | 900 | `--ink` / `--red` / `--blue` |
| 导语 | `.deck` | 32px | 500 | `--ink`，数字 `--red` |
| 面板序号 / 小标题 | `.panel-head .no` / `.label` | 30px | 900 | `#FFFFFF` |
| 面板大数字 | `.panel-body .big` | 82px | 900 | `--red`（02 栏 `--navy`） |
| 面板正文 | `.panel-body .txt` | 24px | 500 | `--ink`，`line-height:1.42` |
| 警示条结论 | `.alert-text .l1` | 44px | 900 | `--ink`，关键词 `--red` |
| 惊叹号 | `.alert-circle .bang` | 82px | 900 | `--red` |
| 页脚 | `.footer` | 21px | 500 | `--grey` |

## 四、排版规则

1. **标题左对齐顶格**，绝不用 `text-align:center`（居中会立刻失去报纸感）。
2. 标题行高 `line-height:1.0`，字距 `-0.02em` —— 超粗字必须收紧，否则字与字会打架。
3. 面板小标题里 `01` 与标签之间用一条 **1px 白色细竖线**分隔（`.panel-head .div`）。
4. 标点用全角，句末句号 / 感叹号加重语气。
5. 文字**不加 `text-shadow`**（深色变体除外，用极淡的暗色 lift）。
6. 面板正文**每栏不超过 3 行**，超出就删字，不要缩字号。
7. **字数少的标题行必须加宽** —— 见 `layout-spec.md` 的「标题行宽度归一」。
