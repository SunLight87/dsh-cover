# 构图骨架 · 九段横带

> 对 `D:\skills\封面参考` 样本做逐行墨量分析后得到的稳定结构。百分比 = 占全图高度。

## 实测版式表（1086 × 1448 基准）

| # | 区域 | 位置（%） | 像素 | 内容 |
|---|------|-----------|------|------|
| 1 | **刊头栏** | 0.6 – 6.2 | 8–90 | 左：深蓝实心方块 + 栏目名；右：超大期号 `01 / 02` |
| 2 | **藏蓝粗分隔线** | 6.8 – 7.3 | 99–106 | 通栏深藏蓝实线，粗约 7px |
| 3 | **日期行** | 7.7 – 9.5 | 112–138 | 右对齐小字 `新闻日期 ｜ 2026年8月30日` |
| 4 | **主标题区** | 10.0 – 50.3 | 145–728 | 3–5 行超粗标题，行高约 130–140px，占全图 **40% 高度** |
| 5 | **导语行** | 51.7 – 54.1 | 748–783 | 单行黑体，含红色数字，句末常带句号 |
| 6 | **红色细分隔线** | 54.6 – 55.5 | 791–803 | 通栏细红线，约 3px |
| 7 | **三栏信息面板** | 56.4 – 83.8 | 816–1214 | `01 / 02 / 03` 等宽三栏，占 **27% 高度** |
| 8 | **红色警示条** | 84.6 – 96.1 | 1225–1391 | 左侧 "!" 圆标 + 2 行结论，红框白底 |
| 9 | **页脚** | 96.2 – 98.5 | 1393–1426 | 细线 + 灰色免责声明 + 品牌水印 |

**安全边距**：左右各约 20 px（**1.8%**），内容宽度占画布 **96.3%** —— 近乎满版，这是"报纸感"的关键。

## 构图骨架块（英文，直接复制进提示词）

```
vertical 3:4 canvas, 20px safe margin, near full-bleed content width 96%,
Band 1 (0–6%):   masthead strip — navy solid square at left + column title, oversized issue number top-right
Band 2 (7%):     full-width deep navy horizontal rule
Band 3 (8–9.5%): right-aligned small date line
Band 4 (10–50%): HEADLINE ZONE — 3 to 5 lines of ultra-bold type, left-aligned, line-height 0.95,
                 one line in red, one key term in royal blue; KEEP THE RIGHT 35% OF ROWS 1–2 EMPTY
                 for the image inset
Band 5 (52–54%): single-line deck in regular weight, contains one red number
Band 6 (55%):    full-width thin red rule
Band 7 (56–84%): three equal columns, each with a solid header bar (red / navy / red),
                 numbered 01 02 03, one flat two-tone icon, one oversized red statistic, 2–3 lines body copy
Band 8 (85–96%): red-outlined alert bar, white exclamation mark in red circle at left, two-line takeaway
Band 9 (96–99%): hairline rule + small grey disclaimer line
```

## 留白 / 文字位置预留规则（必须显式声明，否则模型会把画面填满）

```
leave the upper-right quadrant of the headline zone completely empty as a clean white
negative-space block sized 35% width x 22% height, reserved for a cutout graphic;
leave a 20px clean margin on all four sides; do not let any element bleed off canvas
```

## 构图逻辑四条法则

1. **上留白、下密排** —— 上半 50% 只有大字，下半 50% 塞满信息。
2. **Z 字形动线** —— 刊头 → 大标题 → 导语 → 三栏 → 底部红条，每段之间用分隔线"关闸"。
3. **三段式叙事** —— `01 核心数据 → 02 关键变化 → 03 直接影响`，这个结构在所有样本中高度稳定。
4. **斜对角平衡** —— 左上大标题、右下配图、右上期号、左下第一栏，四角占满，画面不偏。

## 配图块的两种形态

| 形态 | 尺寸与位置 | 示例 |
|------|-----------|------|
| **抠图式** | 右下角，约 32% 宽 × 22% 高，主体带白/透明底 | 印 `AI` 的芯片 + 红箭头、金币堆、算力地球 |
| **宽幅场景式** | 标题区右侧，约 40% 宽 × 24% 高，矩形满边 | `IPO` 石碑 + `STOP` 路牌、NASDAQ 大屏 |

另外，**三栏面板内部可以放实拍照片**（样本中：产品界面截图 / 数据中心机房 / 办公场景），
此时照片占面板上半部，下半部仍是超大红色数字 + 短正文。
