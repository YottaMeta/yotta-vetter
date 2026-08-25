<p align="center">
  <img src="assets/banner.png" alt="yotta-vetter banner" width="100%" />
</p>

# yotta-vetter（元审）

安装任何技能前的「安全审查协议」：四阶段 checklist（来源→代码→权限→风险）+ 轻量 checker，与元安（yotta-security-audit）联动深度扫描。

- **check**：四阶段初审 + SKILL VETTING REPORT（含结论/决策记录/时间戳/审查者）。
- **source**：GitHub 仓库来源半自动化检查，本地缓存，无网络自动降级。
- **规则共用**：危险模式规则与元安同源（vetter_rules.py 为 audit_rules.py 的同步副本）。
- **零依赖**：Python 3.8+ 标准库，Windows + Linux 通用。

## 安装

本技能为「技能包」：先装到你的智能体技能目录，再由智能体按需调用其中的脚本。

### 方式一：npm（推荐，Windows / Linux / macOS）

```bash
npx -y @yottameta/yotta-vetter --agent codex      # 装到 Codex
npx -y @yottameta/yotta-vetter --agent claude    # 装到 Claude Code
npx -y @yottameta/yotta-vetter --agent cursor    # 装到 Cursor
npx -y @yottameta/yotta-vetter -g                # 装到全部已知智能体
npx -y @yottameta/yotta-vetter --list            # 查看智能体 → 默认目录
```

### 方式二：install.sh（Linux / macOS）

```bash
git clone https://github.com/YottaMeta/yotta-vetter.git
cd yotta-vetter
bash install.sh --agent codex        # 或 --agent claude / --dir <路径> / -g
```

### 方式三：手动复制

把本仓库内容复制到你的智能体技能目录（Claude Code ~/.claude/skills/、Cursor ~/.cursor/skills/、Codex ~/.codex/skills/ 或 $CODEX_HOME/skills、通用 ~/.agents/skills/）。

## 快速使用

```bash
python3 scripts/yotta_vetter.py check ./some-skill
python3 scripts/yotta_vetter.py check ./some-skill --json --report report.md
python3 scripts/yotta_vetter.py source github:YottaMeta/yotta-memory
```

## 与元安的关系

- 元审负责「安装前初审 + 来源检查 + 结构化报告」；
- 元安负责「技能深度扫描（13 类检测器）+ 系统安全基线」；
- 元审发现 high 及以上会输出命令引导跑元安。

## 测试

```bash
python3 scripts/test_yotta_vetter.py
```

## 许可证与品牌

- MIT License（Copyright © 2026 YottaMeta），详见 LICENSE。
- 品牌声明见 NOTICE：YottaMeta / 元忆 / 元审 / yotta-* 为 YottaMeta 品牌，派生作品须改名并声明无关联。
- 上游来源致谢：审查协议参考开源社区 skill-vetter 类技能思路，实现为 YottaMeta 自有。
