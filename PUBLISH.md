# 发布指南 · 把 dsh-cover 推到 GitHub 的 `dsh-plugin` 生态

> 目标：让仓库出现在 [github.com/topics/dsh-plugin](https://github.com/topics/dsh-plugin)，
> 并具备提交到 [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) 的条件。

## 一、收录标准（来自 awesome-dsh-plugin 的说明）

该列表收录的插件需要满足：

1. 能用 `dsh plugin add` 安装 —— **每个插件必须声明 `dsh.bundle` 清单**；
2. 行为与其一行描述一致；
3. 归入正确的分类（本项目属于 **Skills**）；
4. 处于维护状态。

> ⚠️ **本项目的形态说明**
> `dsh-cover` 是**纯提示词 / 规范型 Skill**，零运行时代码。它已经能作为 Skill 被 DSH 直接加载
> （放进 `~/.dsh/skills/` 即可），但**若要走 `dsh plugin add` 安装，还需要补一层 `dsh.bundle` 清单**
> —— 见下方「四、补插件清单（可选）」。
>
> 只打 `dsh-plugin` **topic** 不需要清单，任何仓库都能打。清单只影响能否进 awesome 列表。

## 二、发布到 GitHub（三步）

```powershell
cd D:\skills\dsh-cover

# 1) 初始化并首次提交
git init -b main
git add -A
git commit -m "feat: dsh-cover — 中文财经/AI资讯信息图封面提示词生成器"

# 2) 创建公开仓库并推送
gh repo create dsh-cover --public --source=. --remote=origin --push `
  --description "Cover-prompt generator for Chinese finance / AI-news infographic covers — an Agent Skill that turns a headline into a text-free 3:4 base-plate prompt plus a typesetting table."

# 3) 打上 topic（这一步决定它能否出现在 topics/dsh-plugin 页）
gh repo edit --add-topic dsh-plugin,deepseek-harness,dsh,agent-skill,skill,cover-image,infographic,prompt-template,midjourney,typography
```

## 三、验证

```powershell
gh repo view --web                       # 打开仓库
gh api repos/{owner}/dsh-cover/topics    # 确认 topic 已生效
```

浏览器打开 <https://github.com/topics/dsh-plugin> 搜 `dsh-cover`，出现即成功。

## 四、补插件清单（可选 · 想进 awesome 列表再做）

在 `package.json` 里已预留 `dsh` 字段，若要走 `dsh plugin add`，需要补一个 `dsh.bundle` 清单文件，
并确认 DSH 的清单 schema（以官方文档为准，勿凭猜测写）。

**这一步建议先读官方插件协议再动手**，因为清单格式随 DSH 版本变化。
在此之前，`~/.dsh/skills/dsh-cover/` 的手动安装路径始终可用。

## 五、提交到 awesome-dsh-plugin

仓库稳定运行一两周后：

1. Fork `awesome-dsh-plugin/awesome-dsh-plugin`
2. 在 `README.md` 的 `### Skills` 分类下按字母序插入一行：

```markdown
- [SunLight87/dsh-cover](https://github.com/SunLight87/dsh-cover) - 中文财经/AI资讯信息图封面提示词生成器：给一段标题或文案，产出无文字 3:4 底图提示词（中/英）+ 逐区压字坐标表。零依赖。
```

3. 同时更新 `README.zh.md`
4. 提 PR。评审会按 `contributing.md` 的清单逐条核对描述是否属实。

## 六、后续维护清单

- [ ] 补 `evals/02-dark-impact.md`（深色冲击变体）与 `evals/03-minimal-headline.md`（极简大字变体）
- [ ] 加一张示例封面图到 `docs/` 并在 README 里引用（列表页有图的项目点击率明显更高）
- [ ] 打 tag 并发 Release：`git tag v1.0.0 && git push --tags`
- [ ] 若 DSH 的 `dsh.bundle` schema 稳定，补清单并尝试 `dsh plugin add`
