# SKILL VETTING REPORT 模板

check --report 生成的报告遵循本结构；人工审查也可直接套用。

```markdown
# SKILL VETTING REPORT

- 技能: <名称>
- 路径: <目录>
- 来源: <平台 / github:owner/repo>
- 审查时间: <ISO 8601>
- 审查者: <人名/角色>
- 文件数: <N>

## 结论

- 风险等级: <LOW / MEDIUM / HIGH / CRITICAL>
- 结论: <SAFE TO INSTALL / REVIEW REQUIRED / INSTALL WITH CAUTION / DO NOT INSTALL>
- 决策记录: <一句决策理由>

## 汇总

| 级别 | 数量 |
|---|---|
| CRITICAL | N |
| HIGH | N |
| MEDIUM | N |
| LOW | N |
| INFO | N |

## 发现

逐条：级别 · 规则 · 位置 · 描述

## 决策记录

- [ ] 已人工复核发现项
- [ ] 已确认来源可信度
- [ ] 已确认权限范围最小化
- [ ] 审查结论与理由已记录（时间戳/审查者）
```
