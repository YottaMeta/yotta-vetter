<p align="center"><b>Language</b>: <a href="./README.md">English</a> · 中文</p>

<p align="center">
  <img src="assets/banner.png" alt="yotta-vetter banner" width="100%" />
</p>

<h1 align="center">yotta-vetter · 元审</h1>

<p align="center">安装任何技能前的「安全审查协议」：<b>四阶段 checklist（来源 → 代码 → 权限 → 风险）+ 轻量 checker</b>，与元安联动深度扫描。适用于从技能市场、GitHub 或任何来源获取技能、安装前的审查场景。</p>
<p align="center">检测到安装/评估任何技能前、从市场或 GitHub 获取技能、审查他人分享的技能、任何「要装未知代码」的场景，或用户说 审查 / 审查技能 / vetting / 技能安全审查 / 检查技能 时自动激活——<b>不靠关键词碰运气，按是否要装未知代码判定</b>。</p>
<p align="center">Python 3.8+ 标准库实现，零依赖；Windows + Linux 通用；只做审查与报告，结论需人工确认。</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue" /></a>
  <a href="https://agentskills.io/"><img alt="Standard: agentskills.io" src="https://img.shields.io/badge/standard-agentskills.io-orange" /></a>
  <a href="https://www.npmjs.com/package/@yottameta/yotta-vetter"><img alt="npm package" src="https://img.shields.io/npm/v/@yottameta/yotta-vetter" /></a>
  <a href="https://github.com/YottaMeta/yotta-vetter"><img alt="GitHub stars" src="https://img.shields.io/github/stars/YottaMeta/yotta-vetter" /></a>
  <a href="https://github.com/YottaMeta/yotta-vetter/commits/main"><img alt="last commit" src="https://img.shields.io/github/last-commit/YottaMeta/yotta-vetter" /></a>
  <a href="https://github.com/YottaMeta/yotta-vetter"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen" /></a>
</p>

## 这是什么

「要不要装这个技能」应该有一个结构化、可回溯的决策依据，而不是凭感觉。元审把安装前审查固化成四阶段 checklist（来源 → 代码 → 权限 → 风险），并用轻量 checker 自动扫描危险模式、输出 SKILL VETTING REPORT。它不是某个平台的专属功能，而是一份与智能体无关的审查协议：装进任何支持 Agent Skills 的智能体即可按需调用，只做初审与报告，绝不代替最终决策。

## 核心价值

- **check**：四阶段初审（来源/代码/权限/风险），输出 SKILL VETTING REPORT（结论/决策记录/时间戳/审查者）。
- **source**：GitHub 仓库来源半自动化检查（stars/更新时间/许可证），本地缓存，无网络自动降级。
- **规则共用**：危险模式规则与元安同源（scripts/vetter_rules.py 为 audit_rules.py 的同步副本）。
- **联动元安**：初审发现 high 及以上，输出一条命令引导跑元安深度扫描。
- **结论分级**：critical=DO NOT INSTALL；high=INSTALL WITH CAUTION；medium=REVIEW REQUIRED；low/info=SAFE TO INSTALL。

## 核心优势

| 优势 | 说明 |
|---|---|
| **四阶段结构化** | 来源→代码→权限→风险，逐环核对，缺一不可 |
| **结论可回溯** | 报告含结论/决策记录/时间戳/审查者，留痕可追责 |
| **规则与元安同源** | vetter_rules.py 为 audit_rules.py 同步副本，口径一致 |
| **来源半自动** | source 命令查 stars/更新时间/许可证，本地缓存、无网络自动降级 |
| **联动深度扫描** | high 及以上自动引导跑 yotta-security-audit |
| **零依赖** | Python 3.8+ 标准库，无 daemon / 无数据库；Windows + Linux 通用 |
| **生态分发** | GitHub + npm 双源同步发布；npx / install.sh / 手动复制三种安装方式 |

## 功能体系 / 四阶段审查协议

| 阶段 | 检查点 | 对应命令/参考 |
|---|---|---|
| 1. 来源 | 来源平台、作者信誉、stars/更新时间、许可证 | source github:owner/repo；references/checklist.md |
| 2. 代码 | SKILL.md 完整性、脚本清单、危险模式规则扫描 | check <path> |
| 3. 权限 | 可执行位、全局可写、符号链接、需读取/写入/联网的范围 | check <path> |
| 4. 风险 | 风险等级判定 + 结论 + 决策记录 | 报告中的 结论/决策记录 段 |

## 结论判定

| 风险等级 | 结论 | 动作 |
|---|---|---|
| critical | DO NOT INSTALL | 拒绝安装并人工复核 |
| high | INSTALL WITH CAUTION | 人工复核后决定 |
| medium | REVIEW REQUIRED | 复核后安装 |
| low/info | SAFE TO INSTALL | 仍建议按协议完整审查 |

## 使用示例

```bash
# 初审一个技能目录
python3 scripts/yotta_vetter.py check ./some-skill

# 输出 JSON + 生成报告文件
python3 scripts/yotta_vetter.py check ./some-skill --json --report report.md

# 只报告 high 及以上
python3 scripts/yotta_vetter.py check ./some-skill --severity high

# 来源半自动化检查（本地缓存，无网络自动降级）
python3 scripts/yotta_vetter.py source github:YottaMeta/yotta-memory
```

**exit code 语义**：0 = 干净 / 仅 low；1 = medium；2 = high；3 = critical；4 = 错误。

## 与元安的分工

- **元审** = 初审：快、轻，四阶段 checklist + 规则扫描 + 来源检查。
- **元安** = 深度扫描：13 类检测器 + 系统安全基线。
- 元审发现 high 及以上 → 输出命令引导跑元安深度扫描。

## 安装

三种方式任选其一，技能文件统一从 **npm** 获取（GitHub 无代理时较慢，npm 可配国内镜像加速）。

### 方式一：npm（推荐，一行安装）
```bash
# 国内加速（可选）：npm config set registry https://registry.npmmirror.com
npx -y @yottameta/yotta-vetter -g
npx -y @yottameta/yotta-vetter --dir <你的技能目录>   # 任意智能体：指定目录安装
```
> 智能体不在预置列表里？用 `--dir` 指定它的 skills 目录，或手动复制（方式三）。`--list` 可查看各智能体对应的默认目录。想手动拿文件也可 `npm pack @yottameta/yotta-vetter` 解包后按方式二/三安装。

### 方式二：install.sh 一键安装
```bash
bash install.sh -g    # 用户级；bash install.sh --list 查看全部目录
bash install.sh --agent codex   # 指定智能体（--list 可查看可用项）
bash install.sh       # 项目级：自动检测已存在的 .claude/.cursor/.codex 等 skills 目录
bash install.sh --dir /path/to/skills
```
> 覆盖 17 类智能体，含国内 Trae / Qwen / Comate / CodeBuddy / Kimi。Windows 用户：装有 Git Bash 即可用；否则用方式三手动复制。

### 方式三：手动复制
把整个 `yotta-vetter` 文件夹复制到目标智能体的 skills 目录。常见位置（用户级；Windows 用 `%USERPROFILE%`，Linux/macOS 用 `~`）：

| 智能体 | 用户级目录 | 项目级目录 |
|---|---|---|
| Codex | `%USERPROFILE%\.codex\skills\yotta-vetter\` | `.codex\skills\` |
| Claude Code | `%USERPROFILE%\.claude\skills\yotta-vetter\` | `.claude\skills\` |
| Cursor | `%USERPROFILE%\.cursor\skills\yotta-vetter\` | `.cursor\skills\` |
| Windsurf | `%USERPROFILE%\.codeium\windsurf\skills\yotta-vetter\` | `.windsurf\skills\` |
| opencode | `%USERPROFILE%\.config\opencode\skills\yotta-vetter\` | `.opencode\skills\` |
| Gemini | `%USERPROFILE%\.gemini\skills\yotta-vetter\` | `.gemini\skills\` |
| Goose | `%USERPROFILE%\.config\goose\skills\yotta-vetter\` | `.goose\skills\` |
| Amp | `%USERPROFILE%\.config\agents\skills\yotta-vetter\` | `.agents\skills\` |
| Kiro | `%USERPROFILE%\.kiro\skills\yotta-vetter\` | `.kiro\skills\` |
| WorkBuddy | `%USERPROFILE%\.workbuddy\skills\yotta-vetter\` | `.workbuddy\skills\` |
| Trae Code CLI | `%USERPROFILE%\.traecli\skills\yotta-vetter\` | `.traecli\skills\` |
| Trae IDE（国内） | `%USERPROFILE%\.trae-cn\skills\yotta-vetter\` | `.trae\skills\` |
| Qwen Code | `%USERPROFILE%\.qwen\skills\yotta-vetter\` | `.qwen\skills\` |
| Comate | `%USERPROFILE%\.comate\skills\yotta-vetter\` | `.comate\skills\` |
| CodeBuddy | `%USERPROFILE%\.codebuddy\skills\yotta-vetter\` | `.codebuddy\skills\` |
| Kimi | `%USERPROFILE%\.kimi\skills\yotta-vetter\` | `.kimi\skills\` |
| 通用 AGENTS.md | `%USERPROFILE%\.agents\skills\yotta-vetter\` | `.agents\skills\` |

> Codex 默认目录若设置了环境变量 `CODEX_HOME`，以该变量为准；opencode 若设置 `XDG_CONFIG_HOME` 同理。`.agents\skills` 并非通用目录，仅 OpenCode / Cursor / Cline / Amp / Kimi / Gemini CLI / GitHub Copilot 等会读取，**Claude Code 与 Codex 默认不读**。不确定时用 `--dir` 指定，或让该智能体自行安装。

## 升级 / 卸载

- **升级**：重新安装最新版覆盖即可——`npx -y @yottameta/yotta-vetter -g` 或重跑 `bash install.sh -g`。技能目录内的旧文件会被覆盖；不影响项目中已有的其他文件。
- **卸载**：删除目标智能体 skills 目录下的 `yotta-vetter` 文件夹（各智能体目录见上表）即可。卸载后本技能不再生效。

## 常见问题

- **元审能直接替我做决定吗？** 不能。checker 只做初审与报告，最终结论必须由人类确认。
- **发现 high 风险怎么办？** 报告会输出一条引导命令跑元安（yotta-security-audit）深度扫描；建议先隔离或停止使用该技能，再人工复核。
- **离线能用吗？** 能。source 里 GitHub API 检查在无网络时自动降级；check 完全本地运行。
- **我自己扫自己会误报吗？** 元审自身含 source 检查，用标准库 urllib 访问 GitHub API，自扫会命中网络调用提示（medium），属预期行为，非风险。

## 相关技能

同属 YottaMeta 技能矩阵（安全家族）：[yotta-security-audit](https://github.com/YottaMeta/yotta-security-audit)（元安，13 类检测器 + 系统安全基线）负责深度扫描，元审负责安装前初审——元审发现 high 及以上会引导跑元安；[yotta-memory](https://github.com/YottaMeta/yotta-memory)（元忆）负责跨会话长期记忆。

## 开发与校验

本项目内运行：`python tools/validate-skill.py yotta-vetter`。

## 许可证

MIT © YottaMeta —— 详见 [LICENSE](./LICENSE)。品牌声明见 [NOTICE](./NOTICE)。上游来源致谢：审查协议参考开源社区 skill-vetter 类技能思路，实现为 YottaMeta 自有。
