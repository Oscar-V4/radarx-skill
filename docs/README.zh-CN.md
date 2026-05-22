# 📡 RadarX

<p align="center">
  <a href="../README.md">한국어</a> |
  <a href="README.en.md">English</a> |
  <b>简体中文</b>
</p>

**RadarX 是一个雷达型 Agent Skill，用来发现最新的 AI、开源、社交和社区信号。**  
它会扫描 Threads、X、Reddit、Hacker News、GitHub、YouTube、Hugging Face、arXiv、Product Hunt 和网页等 live sources，同时过滤弱 hype，只报告有价值、有证据的候选。

- 寻找最新 AI 工具、开源项目、agentic workflow、best practice 和项目 idea 信号。
- 如果有本地 Threads archive，会先建立连接，并把 archive context 与 live evidence 分开标注。
- 分层使用 GitHub、官方文档、Reddit/HN、YouTube、arXiv、Hugging Face、Product Hunt 和网页搜索。
- 按相关性、证据、freshness、新颖性、采用信号和安全性给候选打分。
- 对只有社交热度、缺少独立证据的候选降级。
- 对项目 idea 研究，会扩展到现有替代方案、MVP 路径、评估计划和风险门槛。

## 快速安装

把下面这段提示词复制给 Codex、Claude Code、Antigravity 或其他编码 Agent，它就可以按当前环境安装并说明如何使用。

```text
请查看这个 GitHub 仓库并安装 RadarX agent skill:
https://github.com/Oscar-V4/radarx-skill

请检测你当前运行的 agent 环境。
- 如果是 Codex，请安装到 ~/.codex/skills/radarx。
- 如果是 Claude Code，请安装到 ~/.claude/skills/radarx。
- 如果是其他 agent，请确认它是否支持基于 SKILL.md 的 skill 文件夹，并安装到最接近的用户级 skill 目录。
- 如果有内置 skill installer，请优先使用；否则 clone 这个 repo，并把 skills/radarx 复制到用户 skill 目录。

安装后，请阅读 skills/radarx/SKILL.md 和 README.md，然后告诉我：
1. 什么时候应该使用 $radarx
2. 应该怎样描述请求
3. 三个适合第一次测试的提示词
```

Codex 直接安装：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Oscar-V4/radarx-skill \
  --path skills/radarx
```

安装后重启你的 agent 应用，然后用 `$radarx` 调用。

## 什么时候使用

| 场景 | 可以这样说 |
|---|---|
| 想看最新 AI/开源趋势 | `$radarx 找一下最近适合实时 AI 语音 Agent 的开源工具。` |
| 想验证社交媒体 hype | `$radarx 检查这个在 X/Threads 上火的工具是否真的有用，请给证据。` |
| 正在研究比赛或 hackathon idea | `$radarx 调研这个 AI 比赛 idea 需要的信息、现有替代方案和 MVP 路径。` |
| 想结合个人 archive | `$radarx 连接我的 Threads archive，找相似但更新的 AI workflow 案例。` |
| 不想要链接堆砌 | `$radarx 只给我最多三个强候选，并说明被淘汰的弱信号。` |
| live social coverage 很重要 | `$radarx 用 social-heavy 模式优先搜索 X、Threads、Reddit 和 Hacker News。` |

## 输出形式

RadarX 通常会返回：

- **Intent**：问题和好候选的标准
- **Attention Mode**：quick、balanced、deep、social-heavy 或 archive-first
- **Archive Connections**：相关 archive context
- **Strong Finds**：有来源支撑的候选和 URL
- **Volatile Social Signals**：仍需验证的 live/social 信号
- **Rejected Or Weak Signals**：被忽略的内容和原因
- **Next Searches**：下一步要搜索的 query、社区、文档或作者

对于项目 idea 和 MVP planning，它会扩展到 baseline reality、build path、evaluation plan 和 privacy/safety risk gates。

## 兼容性

这个仓库按 `SKILL.md` agent skill 结构打包。Codex 和 Claude Code 这类支持用户 skill 目录的 agent 可以直接安装；其他 agent 也可以通过读取 `skills/radarx/SKILL.md` 使用同一套指令，但自动发现规则会因产品而异。

## 使用条件

RadarX 的正常使用不需要 X/Threads 登录、Playwright、browser-use、Chrome 自动化或付费 scraping API。它会优先使用公开证据，并把登录、付费、浏览器依赖来源当作可选 adapter。

不要为了使用 RadarX 导出 cookie 或 token。如果某个来源不可用，skill 应说明限制，并继续使用公开 fallback evidence。
