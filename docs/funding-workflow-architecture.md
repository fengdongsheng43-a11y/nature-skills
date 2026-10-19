# 双基金研究—申报工作流：设计决策、边界与为何如此

**2026-10-19，Draft v0.1**。本文件是设计依据，不是任何年度的官方申报指南，也不是未经实验验证就声称“热门 Skill 最优”的结果。

## 1. 总体决定：共用科学内核，分开基金政策适配

```text
Project ID + Applicant facts + Funding authority + Year + Scheme
       ↓ [Route: NSFC incl. NSFC Regional / provincial-authority fund]
Official policy & system template (annual profile, rule ledger)
       ↓ [eligibility unknown -> BLOCK only compliance claims]
Scientific Discovery Partner (freeze observations and contradictions)
       ↓
Five-pass Literature Evidence Gate (incl. closest art & counterevidence)
       ↓
Serious Rival Hypotheses + Discriminating Predictions + Death Conditions
       ↓
Claim-to-Evidence Architecture + P0 Decisive Experiments
       ↓
Funding-fit adaptor [NSFC / local call] + overlap + budget/time/skills
       ↓
researchwrite [research_canon -> evidence_table -> argument_map
               -> section_contracts -> applicant-controlled revision]
       ↓
Multi-lens review + policy/claim QA + human submission gate
       ↓
Annual guide diff / new data -> update policy or science ledger separately
```

为什么不能把两套工作流直接合并？科学真伪判断可共享，但资助机关、资格、类别/学部、区域适配、经费/周期、校内推荐机制与系统模板是不同规则；同一个“标准国家基金模板”会在地方申报时制造合规风险。

为什么也不能完全独立？两个基金都属于自然科学资助，科学问题真实性、创新性、文献证据、竞争假设、可证伪性和核心实验设计不能因经费多少而放松。

## 2. 权限层次（防误用）

| Layer | Owner | Can determine | Cannot determine |
|---|---|---|---|
| Official annual guide | 国家 NSFC / 相应地方主管机关 | 资格、经费类别、实际模板、截止、限制 | 某机制科学上成立 |
| nature-research-partner | 本 fork 本人维护 | 未解问题、严重竞争假设、证据等级、P0 | 官方政策或中标概率 |
| nature-nsfc-proposal | 本仓库 | 国自然项目类型匹配、学部/代码/研究属性的核验任务、国内项目评审审计 | 任意地方申报的政策 |
| nature-provincial-fund-proposal | 本仓库 | 地方省级类别、区域科学边界、校内名额/期限/预算检查 | 国自然地区科学基金的类别规则 |
| nature-proposal-writer | 本仓库 | 章节论证映射、证据表、作者原稿的针对性反馈 | 用修辞将弱假设升级为强结论 |
| Applicant/institution | 申请人/依托单位 | 研究承诺、资料真实性、署名、提交与伦理责任 | 跳过公开官方要求 |

## 3. 国自然：先科学增量，再类别/学部适配

1. **冻结真实观察与系统**：为了避免先起宏大题目再寻找科学故事。没有观察时也可从有证据的文献冲突起步。
2. **五轮文献证据门槛**：为了避免“别人没在某个温度/材料做过”即被误判成创新。最近似研究、强基线和反证必须出现。
3. **机制竞争/死亡条件**：为了让研究成为可反驳的问题；不能只设计成功时好看的表征。
4. **P0实验优先**：在做成本高的组学、模型和复杂仪器前，先核查核心效应真实性与识别能力。
5. **匹配NSFC申报类别、学部和代码**：因为科学上好的方向仍可能申请错类型；而不同年度申请书结构可能改革。
6. **论证写作和评审**：只将已成立的科研证据组织给评委看。创新点不等于“使用新设备”，目标不等于方法清单。
7. **合规与提交**：正式稿由申请人按官方 AI 规定自主撰写并负责，不能让第三方 Skill 的自动写稿能力覆盖监管规定。

**与地方基金最大的差别**：国自然的导向要依各项目类别决定；不应在没有指南要求时强制添加地方产业落地、企业合作、当地样品验证作为创新点。

## 4. 省/区自然：资格/推荐与地方边界前置，科学标准不降

1. **先看具体主管机关、年度、类别和学校推荐**：地方人才项目可能有名额限制，不能花大量时间完成后才发现资格不符。
2. **拆开地区条件和科学问题**：地方需求必须是真实、可测、和已知基线构成新矛盾的条件；仅“内蒙古冬季冷”本身不证明创新。
3. **仍进行同等级的五轮文献检索/竞争假设**：避免把小经费项目理解为低标准研究。
4. **建立科学与地方两张适配表**：科学价值（Scientific）与区域/类别匹配（Regional/Scheme）独立审核；不是每个项目都需要产业应用指标。
5. **按经费期限缩小承诺**：地方博士研究生类与省级重点类规模截然不同，必须优先选择最小充分 P0，不照搬整套博士论文。
6. **项目重叠、前期基础、阶段里程碑**：尤其防止多基金重复申报同一研究任务或虚报已完成实验。
7. **当地模板与单位/系统双时点检查**：以当年的地方正式指南/附件为准，学校内部截止不同于科技厅截止。

**与国自然最大的差别**：地方适配是“依具体指南判断的项目匹配要素”，不是独立于科学问题的装饰性段落，更不能把区自然简单做成国自然的缩减字数版本。

## 5. 哪些部分可来自已检索 GitHub Skills；哪些不能照搬

| Source | Audited component to adopt | Rejected / qualified behavior |
|---|---|---|
| fork `nature-research-partner` | fail-closed claims; five evidence passes; rivals, death tests, P0 | 不允许后续写作组件推翻主张状态 |
| fork `nature-proposal-writer` | evidence table, argument map, section contracts, stage QA | 任一评估阈值仅内部启发，不是资助概率 |
| `LeonChaoX/qinyan-academic-skills` NSFC | NSFC-specific intake, proposal sections & compliance reminders | 不采纳其所有类别统一限制等未经官方核对的表述 |
| `pkgunboat/ScholarWriting` | section-by-section consistency, risk & feasibility checklists | 不采纳未经外部校准的自动评分作为真实专家分数 |
| `lyndonkl/claude` grant-proposal-assistant | reviewer mindset, fundable hypothesis, realistic aims, failure contingencies | 不移植 NIH/US NSF 的申报格式与评审标准 |
| `huangwb8/ChineseResearchLaTeX` research-foundation writer | prior-work to work-package evidence mapping and resource conditions | 不要求安装其 LaTeX/脚本或复制省份模板 |
| `davila7/claude-code-templates` research-grants | budget justification and milestone thinking | 不接受“所有申请必须 AI 生成示意图”的强制要求 |
| `wsxwj123/opencode-skills-backup` nsfc-proposal | claim-to-aim consistency, year/scheme-scoped format source, blind-review caution | 不照搬多轮强制问答、硬编码 MCP/脚本门槛和“自动签字” |
| `Wesley-Yin77/nsfc_medicine_all` | specialized hypothesis/innovation review architecture | 医学部样本的“中标规律”不视为环境学科的证据 |

只借鉴可明确描述的工作流思想；不复制第三方长篇原文、虚构同行验证或宣称各 Skill 已通过科学实证比较。

## 6. 每年新指南送入后的标准更新（两套通用）

```text
User uploads new guide / official link
  -> identify year, issuer, scheme, source authenticity
  -> extract each actionable rule into RULE_LEDGER
  -> compare prior year: added / changed / removed / unverified
  -> update FUND_PROFILE + STRUCTURE_PROFILE + timetable + budget + restrictions
  -> rerun only affected compliance + funding-fit + claims review gates
  -> preserve scientific evidence/history; update it only if scientific inputs change
  -> hand applicant checklist of unresolved hard rules
```

推荐项目文件：`FUND_PROFILE.md`、`RULE_LEDGER.md`、`POLICY_DIFF.md`、`LITERATURE_EVIDENCE_BRIEF.md`、`HYPOTHESIS_LEDGER.md`、`CLAIM_LEDGER.yaml`、`AIM_EVIDENCE_MATRIX.md`、`BUDGET_AND_MILESTONES.md`、`REVIEW_LOG.md`。
上述均为**单个申请项目工作目录**的建议产物，不能混入 skill 仓库作为“对所有项目有效”的数据。

## 7. Policy fact check（2026核实；只为说明为何必须逐年、逐类别处理）

- 国家自然科学基金委员会2026官方通告：https://www.nsfc.gov.cn/p1/3381/2824/99667.html ，明确2026面上+青年 C 改版，申报和生成式 AI 使用规范。
- 国家自然科学基金委员会 2025-12-30 的改革说明：https://www.nsfc.gov.cn/p1/3381/2821/99242.html ，三部分、原则上30页适用“面上与青年 C”，而非全部类型。
- 2027 内蒙古自治区科学技术厅 2026-10-16 通知原始路径：https://kjt.nmg.gov.cn/kjdt/tzgg/202610/t20261016_2965565.html （本次打开原始 URL 失败；待用户提供官方附件核实细项）。
- 2027 内蒙古某高校转发：https://www.jnnu.edu.cn/kyc/info/1115/8970.htm ，提供项目类别实例，但学校内部截止不是统一适用的内蒙古大学规则。

当前文件从不将政策快照作为新年度默认值。

## 8. Definition of done（完成标准）

- 路由正确且不会把国自然地区基金误判成省自然；
- 政策不跨年/跨类别/跨省默认套用，年份变更不清空科学历史；
- SOTA、机制与创新性结论过对应文献门槛；
- 认真列竞争解释、死亡条件、P0/负结果与决策；
- 所有中心目标均映射可执行的实验和可以支持的 claim；
- 研究基础与预算/时间/项目边界一致，无虚构；
- 国自然有独立 AI/诚信检查，地方政策独立核验；
- 先科研、后组织论证、最后评审，不让编排语言代替科学发现。
