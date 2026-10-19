# NSFC annual policy intake — 每年更新而不改科学工作流

## 输入顺序
1. NSFC 该年度项目指南和具体类别页面/申请系统模板（最优先）；
2. 同年度官方项目申请通告、科研诚信/伦理及 AI 使用规定、经费管理办法；
3. 依托单位通知（校内限额/流程/截止）；
4. 如上述文本不可访问，留 `UNKNOWN`，禁止以旧指南补全。

## 每条政策单独登记
| Field | Requirement |
|---|---|
| rule_id | 唯一编号 |
| funder / year / scheme / division | 具体适用对象 |
| rule / exact_span | 具体规则与可回查原文 |
| official_url / attachment | 官方来源及附件名称 |
| observed_on / access | 获取日期；已核验全文/仅摘要/转引 |
| status | VERIFIED / UNVERIFIED / CONFLICT / SUPERSEDED |
| impact | eligibility / form / ethics / budget / deadline / other |
| action | 缺失时如何核验；是否阻断提交 |

## 每次申请更新的项目级资料
`FUND_PROFILE.md`: `project_id`, `call_year`, `scheme`, `subscheme`, `division`, `application_code`, `research_attribute`, `applicant_status`, `institution`, `duration`, `budget_mode`, `system_template_version`, `official_deadline`, `institution_deadline`, `attachments`, `ai_disclosure_rule`, `ethics_rule`, `overlap_risk`, `unknowns`.
`STRUCTURE_PROFILE.md`: 官方章节原名、顺序、限制、是否强制；不能把历史三部分正文套给所有项目。

## 有年份约束的已核实示例（不是未来年度默认值）
- 2026 国家自然科学基金项目申请通告（官方）：https://www.nsfc.gov.cn/p1/3381/2824/99667.html
- 2026 NSFC 面上和青年 C 类结构改革（官方）：https://www.nsfc.gov.cn/p1/3381/2821/99242.html
- 2026 官方申请书 AI 使用问答：https://www.nsfc.gov.cn/p1/2961/2962/3642/sqs.html

不要从 GitHub 第三方 nsfc-proposal Skills 引用“面上、青 A/B/C、地区均三部分及 30 页”等未经类别核实的断言。
