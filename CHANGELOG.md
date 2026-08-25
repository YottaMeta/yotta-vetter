# 更新日志

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
