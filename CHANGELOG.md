# 更新日志

## v0.1.3 (2026-08-28)

中英双语 README 对齐 + 版本统一（老张拍板「英文门面 + 中文全档」）：

- **README.md 改为英文**：作为 GitHub / npm / ClawHub 首页的英文门面（翻译 + 精简，覆盖定位 / 核心价值 / 四阶段协议 / 结论判定 / 使用示例 / 安装 / 升级卸载 / 常见问题 / 相关技能 / 边界 / 开发校验全流程）。
- **新增 README.zh-CN.md**：原中文完整主文档整体平移，顶部加语言切换链接。
- **移除 npx --agent codex 安装行**：README 安装方式一不再出现 `npx -y @yottameta/... --agent <name>`（固定智能体名，违反安装规范；npx 用 -g 或 --dir，--agent 仅 install.sh 用）。
- **版本统一 0.1.3**：此前 package.json=0.1.2、CHANGELOG 顶部=0.1.1、引擎 VERSION=0.1.0 不一致；本版统一为 0.1.3（package.json / SKILL frontmatter / 引擎 VERSION / CHANGELOG / 测试断言全对齐）。
- **package.json**：description 改英文；files 加 README.zh-CN.md。
- 边界（B 方案）：references / CHANGELOG / 测试注释不翻译；SKILL 触发描述保持中文。

## v0.1.1 (2026-08-26)

README 按标准补全：新增「这是什么 / 核心价值 / 核心优势 / 四阶段协议 / 结论判定 / 常见问题 / 相关技能 / 升级卸载」等章节，与 YottaMeta 技能矩阵 README 标准对齐；无功能变更。


## v0.1.0 (2026-08-26)

YottaMeta 自有实现首版（重写自第三方技术包 skill-vetter v2.0.0，已完全重写，无上游代码）：

- check：四阶段初审（来源/代码/权限/风险）+ 危险模式规则扫描 + SKILL VETTING REPORT 报告。
- 危险模式规则与 yotta-security-audit（元安）共用（vetter_rules.py 为 audit_rules.py 的同步副本）。
- 联动元安（V3）：初审发现 high 及以上，输出深度扫描引导命令。
- source（V4）：GitHub 仓库来源半自动化检查（stars/更新时间/许可证），本地缓存，无网络自动降级。
- 输出：文本 / --json / --report report.md（SKILL VETTING REPORT 模板，含结论/决策记录/时间戳/审查者）。
- 零依赖（Python 3.8+ 标准库），Windows + Linux 通用，UTF-8 加固（GBK 控制台不崩）。
- exit code 语义与元安一致：0=干净/仅 low，1=medium，2=high，3=critical，4=错误。
- 版权：YottaMeta 纯自有 MIT + NOTICE 品牌声明；README 一行上游致谢。
