# dsh-cover 安装指南

一个「文案 / 标题 → 信息图封面提示词」的 Agent Skill，兼容 **DeepSeek Harness (DSH)**、**Claude Code**、**OpenAI Codex** 与 **Cursor**。

**零运行依赖** —— 纯提示词与规范文档，不需要 Python、Node 或任何 CLI。

## 目录结构

```
dsh-cover/
├── SKILL.md                      技能主文档（触发词 + 三步流程 + 输出格式）
├── README.md                     English entry
├── README.zh-CN.md               中文入口
├── INSTALL.md                    本文件
├── AGENTS.md                     维护约束（仅开发者需要）
├── package.json                  npm 元数据（可选发布）
├── LICENSE                       MIT
├── references/                   六份规范文档，按需加载
├── assets/                       三份可直接复制的提示词模板
└── evals/                        一条完整走通的样例
```

---

## 一、安装到 DeepSeek Harness（推荐）

DSH 的个人技能目录是 `~/.dsh/skills/`（Windows 即 `C:\Users\<用户名>\.dsh\skills\`）。

```powershell
# Windows
Copy-Item -Recurse -Force . "$env:USERPROFILE\.dsh\skills\dsh-cover"
```

```bash
# macOS / Linux
cp -R . ~/.dsh/skills/dsh-cover
```

最终路径为 `.../.dsh/skills/dsh-cover/SKILL.md`。重启 DSH 或重新加载技能后即可触发。

**验证**：新开一个会话，说「做封面：<任意标题>」，或输入 `/dsh-cover`，
若技能出现在技能列表里即安装成功。

## 二、安装到 Claude Code

```bash
cp -R . ~/.claude/skills/dsh-cover          # 个人级
cp -R . <项目>/.claude/skills/dsh-cover     # 项目级
```

`SKILL.md` 的 frontmatter（`name` + `description`）与 Claude Code Agent Skill 规范兼容，无需改动。

## 三、安装到 OpenAI Codex

```powershell
# Windows
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\dsh-cover"
```

```bash
# macOS / Linux
cp -R . ~/.codex/skills/dsh-cover
```

## 四、安装到 Cursor

放进项目或全局的 skills 目录，或直接把 `SKILL.md` 的内容作为规则文件引入。

---

## 五、运行依赖

**无。** 本技能只产出文本（提示词 + 坐标表）。

真正出图与压字需要你自备：

| 环节 | 工具 | 说明 |
|------|------|------|
| 出底图 | 即梦 / Seedream / GPT-Image / Midjourney / Flux / SDXL | 任选一个支持 3:4 的模型 |
| 压字排版 | Figma / PowerPoint / HyperFrames / Photoshop | 任选一个 |
| 字体 | **思源黑体 Source Han Sans SC Heavy** + **Archivo Black** | 必须先装好，否则字号表对不上 |
| 字体（可选） | 阿里巴巴普惠体 Heavy | 思源黑体 Heavy 的替代 |

### 字体获取

- 思源黑体：Google Fonts 搜 `Noto Sans SC`（即思源黑体的 Google 版），取 **Black (900)** 字重
- Archivo Black：Google Fonts 直接下载

---

## 六、快速自检

安装后跑一遍 `evals/01-gpt6-cost-drop.md` 里的输入，对比输出：

- [ ] 意象提取表 7 行齐全
- [ ] 底图提示词中/英各一条，且都含 `完全不含任何文字` / `ABSOLUTELY NO TEXT`
- [ ] 负面提示齐全
- [ ] 压字坐标表 13 行 + 自检 5 条

四项都对，说明技能加载正常。

---

## 七、卸载

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.dsh\skills\dsh-cover"
```

不写入任何其他位置，删除目录即完全卸载。
