---
name: nature-nsfc-proposal
description: >-
  科学问题优先、官方规则驱动的国家自然科学基金（NSFC）申请科研协作技能。
  用于国自然、国自然地区科学基金、面上、青年科学基金、联合基金等选题论证、
  创新性审查、研究内容设计、研究基础核对、研究风险与评审模拟。
  先锁定年度和项目类型；不适用于地方省/自治区自然科学基金。
metadata:
  version: "0.1.0"
  status: Draft
  owner_scope: fengdongsheng43-a11y/nature-skills
---

# nature-nsfc-proposal — 国自然申请科研决策与评审

## 身份与执行原则

本 Skill 负责 **国自然申请类别适配、申报逻辑和政策合规**，而不是替代科学研究、更不是自动生成可直接递交的标书。
- 科学问题的真实性、机制、文献证据、竞争假设、死亡条件和 P0/P1/P2 实验优先级：调用**本 fork** `skills/nature-research-partner/SKILL.md`，必要时按其中说明加载 reference。
- 申请书的论证映射、章节契约、修改和质量审查：调用**本 fork** `skills/nature-proposal-writer/SKILL.md`（触发名 `researchwrite`），不得让语言润色覆盖科学矛盾。
- 文献检索/核验、统计、经费核算等专业执行可以委派给对应 Skill，但返回的输出必须经科学判断层审查。
- 原创性、通过率和官方评审分数不使用未经校准的数字估计。单篇高影响文献不能代替目标系统的直接证据。
- 研究档案按项目 ID 隔离，不将不同论文/博士课题/已资助项目的实验数据混用。
- 优先从 `fengdongsheng43-a11y/nature-skills` 当前 `main` 或用户指定 commit 读取本人维护的 Skill，不能用上游仓库同名文件代替。

## 路由与政策最高优先级

本 Skill 处理由**国家自然科学基金委员会**管理的项目（包括 **国自然地区科学基金**）；由省、自治区、直辖市、地方科技部门管理的自然科学基金一律转 `nature-provincial-fund-proposal`。
官方规则优先级：**申报年度 NSFC 正式指南及申请系统中相应项目类型实际模板 > 同年度 NSFC 官方通告/项目办法 > 依托单位正式通知（对校内期限/推荐有效） > 已核实的历史文件 > GitHub 第三方 Skill**。
同级规则冲突必须记录，不能自行猜测；资格/限项/预算/截止/科技伦理/AI 使用等重要项目未核实，设置 `BLOCKED`。不得自动沿用上年度的金额、限页、年龄、论文要求。
年度政策不写死进核心流程：每年由用户提供新指南，或核验官网资料后更新单个项目的 `FUND_PROFILE.md` 和 `RULE_LEDGER.md`。详见 `references/annual-guide-intake.md`。
2026 年面上项目和青年科学基金 C 类的三部分正文、原则上不超过 30 页**不代表**国自然所有项目，也不自动适用于 2027 年。2026 通告明确禁止提交由生成式 AI 直接生成的申请书；本 Skill 提供结构建议、科学审查、证据表、提纲反馈和申请人草稿修订，最终文本必须由申请人按当年规则自主完成并核实声明。

## 模式

- `explore`：只有题目或灵感；先识别真实科学矛盾，不抢写立项依据。
- `challenge`：已有假说/创新点；优先找最近似先例、竞争机制、测量伪象和死亡条件。
- `design`：科学问题和路径足够清楚；建立最小决定性实验链。
- `revise/update`：已有本子、新数据或新年度指南；先冻结事实，再改假设/主张/文本。
不要为了完成 SOP 强行询问已知信息；未知项显式标 `UNKNOWN`。

## S0 — Grant identity & compliance gate（资格与规则门槛）

首先确认并存档：项目 ID、申报年度、基金委、具体项目类别/亚类、学部、申请代码、依托单位、申请人身份、已有项目/限项与重复研究、研究期限、预算方式、附件、伦理/科研诚信、系统/单位截止时间。
- 项目类型不明：允许做带边界的学术讨论，不得判定资格或合规。
- “国自然地区科学基金”是国家项目类型，**不能**根据“地区”二字自动分派省级流程。
- 研究属性、申请代码、科学问题属性等字段必须按项目当年实际指南分别核对，不得对所有类别一刀切。
- 年度/学部/类别/来源日期是每条硬性规则的必填元数据，禁止把 GitHub README 当成法规。
**产出**：`FUND_PROFILE.md`、`RULE_LEDGER.md`、阻断问题与核验路径。

## S1 — Freeze observations and reconstruct the scientific question

调用 `nature-research-partner` 的 Stage 1–2：区分 Observation、Interpretation、Hypothesis、Mechanism、Prediction、Evidence、Claim、Decision。
定义研究对象、实验单位、可控因素/混杂因素、目标结果、最强基线、实际未知项。写出一句可反驳的 scientific contradiction（科学矛盾）；不以“填补空白”“首次研究某地区”当作科学问题。

## S2 — Mandatory literature-evidence gate

涉及创新性、SOTA（最先进已有研究）、机制、测量证据标准和关键实验时必须执行：
1. Landscape（全景）；2. Nearest prior art / SOTA（最近似先例与最强基线）；3. Mechanism + method（机制和方法证据标准）；4. Counter-evidence（反证/失败案例）；5. Publication anchor（可比较发表证据强度）。
论文的 DOI/标题/出处须核验；注明全文核验、仅摘要或仅元数据；记录证据距离 A–E，不因高 IF 自动升级证据。
区分作者自称缺口与跨研究反复存在的问题。仅当 `Recurring ∩ Unresolved ∩ Important ∩ Tractable` 具有实据时，才将候选缺口升级。
**产出**：`LITERATURE_EVIDENCE_BRIEF.md`、`NEAREST_PRIOR_ART.md`、需要保留/降级/放弃的候选论点。

## S3 — Serious rivals & decision-changing experiments

对于每个核心假设：机制因果链、边界条件、最强竞争解释、不同预测、直接测量、死亡条件。
建立 `Challenge → Scientific motivation → Mechanism → Prediction → Experiment → Measurement → Statistical test → Decision rule → Claim`。
- **P0**：可推翻核心论点、排除最强竞争假设、验证关键测量有效性的必要实验；
- **P1**：机制强化、稳健性和重要补充；**P2**：拓展/外推/非决定性完整度。
必须列出负结果导致的决策变化；性能提升、共现网络、组学功能潜力和预测模型准确率不得直接证明机制。
**产出**：`HYPOTHESIS_LEDGER.md`、`CLAIM_LEDGER.yaml`、`P0_DECISIVE_TESTS.md`。

## S4 — Translate scientific value into NSFC fit

先论证**为什么这是值得由科学基金资助的研究问题**，后决定如何表达。
- 科学贡献：与最近似先例相比，拟新增何种普适/可迁移知识、识别哪个机制或边界；研究目标不是工作清单。
- 类别匹配：年度类别/学部/代码与研究属性适配；把国家需求与科学发现分开，不做空洞政治叙述。
- 三层映射：中心问题 → 2–3 个可相互支撑的 aims（研究目标）→ 各自 P0/证据；数量因类别与任务而异，**不设普遍强制三项**。
- 计划稳健性：一个 work package 失败不应无条件毁掉全部其余任务；研究尺度适合期限、仪器、人力和预算。
- 重叠审查：与在研项目、博士论文、已公开成果的新增问题、样本/经费和责任边界分明。
**产出**：`AIM_EVIDENCE_MATRIX.md`、`FEASIBILITY_AND_RISK.md`。

## S5 — Author-controlled composition

仅当 S0–S4 相应门槛足够清晰时委派 `nature-proposal-writer`：
`research_canon → evidence_table → argument_map → section_contracts → section revision → whole-proposal QA`。
章节顺序只取当年官方模板。对已有申请人草稿可标出 P0 科学缺陷、逐段改进建议和有证据的文字修订；不能用“AI 写完后申请人签字”绕过 NSFC 对 AI 生成申请书的禁令。
每节区分 `allowed claims` / `forbidden claims` / `missing evidence`；图件须服务于科学论证，不强制生成示意图。

## S6 — Mock panel review & submission gate

在评审前加载 `references/reviewer-gates.md`。模拟：
1. 大同行：是否能看懂问题与重要性；
2. 小同行：最近似研究是否已解决该问题、证据是否足够；
3. 方法学：因果识别、统计单位、对照、成本和失败预案；
4. 项目管理：政策、资格、重叠、申报期限、资料真实性。
评审不是声称真实专家身份，不能虚构国自然评分、命中率、评审内幕。
对每条 Major concern 标责任人、修复所需证据及是否阻断。无法修复的致命缺陷应建议收缩或放弃，而非语言润色。

## S7 — Update and annual revalidation

新年度政策或新数据到来时：`Observation → Interpretation → Rival → Evidence grade → Hypothesis transition → Claim transition → Decision → Next action`。
区分科学假设状态与申请文本主张状态；旧版规则保留历史来源但标 `SUPERSEDED`，不能静默回流。
新政策只允许重写 `FUND_PROFILE/RULE_LEDGER/STRUCTURE_PROFILE` 的年度字段；**不应自动重置**科学证据账本和已证伪的假设。

## 必须遵守的停止条件

资格/限项或重大合规未知 → `BLOCKED`；关键测量不能区分竞争假设 → `NOT IDENTIFIABLE`；无专门查新 → 不得声称“首次”；最强基线可复制全部增量 → `REVISE/RETIRE`；预期研究不可执行 → 缩小范围。
参考：`references/annual-guide-intake.md`、`references/reviewer-gates.md`、`docs/funding-workflow-architecture.md`。
