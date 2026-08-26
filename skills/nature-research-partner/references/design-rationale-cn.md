# `nature-research-partner` 设计逐句说明

这份文件解释 `SKILL.md` 中每个主要规范句为什么存在。它不是第二套规则；若本说明和 `SKILL.md` 冲突，以 `SKILL.md` 为准。

## 定位段

**“Use this skill as a persistent scientific collaborator…”**

意义：把角色从一次性答题工具改成持续科研搭档。关键词是 `persistent`，因为科研方向需要随着文献、数据和失败实验不断更新。

**“The default goal is not to help the user's current idea succeed.”**

意义：禁止迎合式科研。灵感只是候选解释，不是必须被证明正确的结论。

**“The default goal is to determine what is actually true enough to justify the next research decision.”**

意义：把科研目标从“讲出漂亮故事”改为“获得足够证据做下一步决定”。这里故意使用 `true enough`，因为实验科学通常只能获得有边界、有不确定性的支持，而不是绝对真理。

## 十一条不可协商规则

**1. Separate Observation, Interpretation, Hypothesis, Mechanism, Prediction, and Evidence.**

意义：防止把“看到某现象”“我认为为什么”“机制已经被证明”混为一谈，这是 AI 和论文讨论中最常见的逻辑跳跃。

**2. Do not complete the user's initial story merely because it is plausible.**

意义：你的灵感可能来自一个瞬间，天然存在锚定偏差。搭档必须主动找竞争解释，而不是替原故事补细节。

**3. Formalize what can be formalized… use UNKNOWN fields…**

意义：保留数学严格性，同时避免为了显得高级而伪造变量、权重和精度。未知本身就是科研状态。

**4. After the initial idea has been clarified enough to form searchable questions, literature-dependent reasoning must pass a literature-evidence gate.**

意义：这是 v0.2 的关键升级。我们先用对话把片面的灵感收紧到可检索问题，随后立即查外部证据。凡涉及 SOTA、创新性、机制先例、方法有效性和目标论文证据标准的判断，只要有检索能力，就不能只靠模型记忆继续推演。

**5. Do not treat literature absence as proof of novelty.**

意义：检索没有找到只能说明当前检索边界内没有找到，不能证明全世界没人做过。

**6. Every central mechanism or innovation claim must have a falsification condition or death condition.**

意义：没有失败条件的创新点不可证伪，容易变成任何结果都能解释的故事。

**7. Prefer experiments that discriminate among hypotheses…**

意义：优先做能改变判断的实验，而不是把 SEM、XPS、FTIR 等表征机械堆满。

**8. Negative, null, contradictory, or mechanism-killing results are evidence…**

意义：失败实验也必须改变我们的信念和路线，不能只保留支持性结果。

**9. Do not upgrade association to causation…**

意义：明确四种常见过度推断。性能提高不等于机制成立，相关不等于因果，代理指标不等于真实构念。

**10. Do not invent citations…**

意义：这是科研可信度底线，明确禁止 AI 为了让方案完整而补造证据。

**11. Keep current truth separate from historical discussion.**

意义：长期项目最怕旧想法和新结论同时堆在聊天里。历史保留用于追溯，但只有当前状态驱动实验。

## 四种工作模式

**“Choose the lightest mode…”**

意义：防止把每个小问题都套完整七阶段流程，避免流程主义。

**`explore`**

意义：针对片面灵感，先用少量高价值追问逼清问题，不急于写完整方案。

**`challenge`**

意义：当想法已成形后主动转为反方，检查 baseline、先验工作、边界和死亡条件。

**`design`**

意义：只有科学问题和候选机制足够明确后才进入实验落地，避免先做实验后补科学问题。

**`update`**

意义：数据回来以后不是重新讲故事，而是更新原有假设、证据和决策。

**“If the user explicitly requests an immediate complete answer…”**

意义：用户保留控制权。Skill 不能以“苏格拉底式讨论”为理由阻碍明确要求的直接输出，但必须把未解决假设写清楚。

## 核心研究对象

**`R={Ω,X,Z,A,Y,M,H,Θ,C,U,B,E}`**

意义：不是为了公式本身，而是用一个统一对象逼迫研究计划声明系统边界、变量、行动、响应、机制、竞争假设、未知、约束、baseline 和证据标准。

**“Do not require every field to be known.”**

意义：形式化的价值是暴露未知，而不是假装未知已经解决。

**优化问题与发现问题的区分句**

意义：材料配方可以优化，但机制发现的核心不是最大化一个性能值，而是区分解释。两者混在一起会造成“最佳配方=机制被证明”的错误。

**信息增益公式**

意义：表达下一实验应优先带来信息和决策价值，而不是简单增加数据量。公式只作为决策脚手架，除非概率和效用真的经过校准，否则不能输出虚假的精确分数。

## Stage 1

**“First write what was actually observed… before explaining why it happened.”**

意义：冻结事实，防止看到结果后立即把解释写进事实描述。

**来源、边界、实验单位、变量、直接测量/推断、未知和决策目的等字段**

意义：这些字段决定后续是否存在伪重复、混杂、代理指标误用和研究边界漂移。

**“Do not let an optimization framing hide an unresolved mechanistic question.”**

意义：能找到最优条件不代表知道为什么最优。

## Stage 2

**“Use focused dialogue…”**

意义：这一阶段的任务是和用户共同重构问题，而不是单向生成答案。

**“normally ask 2–4 high-value questions per round”**

意义：避免一次抛出几十个问题。只问会改变研究方向的问题。

**关于 baseline、主导变量、去掉机制后剩余解释、失效来源、因果与相关、失败条件的六类问题**

意义：这些问题用于寻找真正的科学矛盾和技术瓶颈，而不是收集背景资料。

**“not a polished project title”**

意义：科学问题先于标题包装。

## Stage 3

**“Once Stage 1–2 have produced a sufficiently clear and searchable problem, stop speculative mechanism strengthening and retrieve external evidence.”**

意义：这是 v0.2 的核心行为变化。先沟通，把问题收紧到可检索；一旦达到这个状态，就停止继续靠常识补机制，先查文献。

**“Do not search blindly from the user's first wording.”**

意义：检索本身也会受到锚定偏差影响。先明确 observation、system boundary、scientific contradiction、baseline 和真正需要验证的 claim，再构造检索词。

**五轮检索顺序：Landscape → nearest prior art/SOTA → mechanism/evidence → counter-evidence → publication anchor**

意义：先弄清领域语言，再找最接近的前沿和 baseline；随后确认机制到底怎么被证明；再主动找反例；最后才看目标层级论文如何组织证据。这样比一开始只搜“和我的想法最像的论文”更不容易自我确认。

**“Distinguish full-text verified, abstract-only, and metadata-only.”**

意义：避免把摘要预览或元数据当成全文证据。尤其机制、实验条件和数值结果不能从没真正读过的论文中补出来。

**Literature Evidence Brief**

意义：检索不是终点。必须把 3–5 个最有信息量的锚点压缩成一份“证据对初始想法造成了什么改变”的简报，包括最强 baseline、支持、反驳、未决和下一轮应该讨论的问题。

**“In an interactive explore workflow, normally discuss this brief with the user before Stage 4–6.”**

意义：符合我们的科研搭档模式。检索以后不是 Agent 自己一路把方案做到底，而是先把证据带回讨论桌，和用户共同重构问题，再进入竞争机制和实验设计。

**允许 `NOT FOUND`**

意义：文章难找时不硬凑。缺位本身可以提示“机制未被直接测过”“问题拆得不够细”或“搜索仍不充分”，但不能直接证明创新。

## Stage 4

**“Translate… into competing explanations rather than one preferred story.”**

意义：正式进入强推断思路。支持一个机制必须同时考虑其他机制能不能解释相同结果。

**机制链、边界、区分性预测、rival、证据和 death condition 字段**

意义：把机制从文字故事转为可以被实验攻击的结构。

**加入 artifact、confounding、batch、transport 等非机制 rival**

意义：很多“新机制”最终是传质、批次或测量造成的，不能只在漂亮的化学/生物机制之间选择。

**物理—化学—生物约束顺序**

意义：优先检查质量守恒、热力学、动力学和传质这些低成本硬约束，再进入昂贵表征和生物解释。

## Stage 5

**“Treat every proposed contribution as guilty until it survives comparison.”**

意义：创新点采用红队思维，默认需要被证明，而不是默认成立。

**minimum innovation units**

意义：把“一个听起来很新的大想法”拆成材料、机制、触发、方法、应用等最小单元，才能真正查新。

**去掉材料名、应用名和包装后再看贡献**

意义：判断创新是在科学关系本身，还是仅仅在命名和场景迁移。

**拒绝单一 numeric novelty score**

意义：创新不是一个可以无依据压缩成 8.7/10 的量。分维度判断更可审计。

## Stage 6

**Challenge → motivation → mechanism → prediction → experiment → measurement → statistics → decision → claim**

意义：这是整篇论文的核心证据骨架。任何缺失环节都要显式显示为 evidence gap。

**“Every key experiment must state what uncertainty it reduces…”**

意义：实验存在的理由不是“大家都做这个表征”，而是它能区分某个关键未知。

**独立实验单位、baseline、控制变量、对照、校准、不同假设预期、反证、统计、成本等字段**

意义：把科学逻辑和真实可执行性放进同一张实验设计表。

**“Prefer the smallest decisive experiment set…”**

意义：优先少量决定性实验，减少高成本但低信息量的表征堆砌。

## Stage 7

**“freeze the new observation before reinterpreting the story”**

意义：避免 HARKing 和事后故事重写。

**Observation → Interpretation → Rival → Evidence grade → Claim status → Decision impact → Next experiment**

意义：每一批数据都必须进入同一套更新协议，形成真正的科研循环。

**六种 hypothesis states**

意义：让假设不是“对/错”二元，而是可追踪地增强、削弱、否决、替代或保持未决。

**“Do not erase negative history.”**

意义：保留为什么改方向，防止几个月后在没有新证据的情况下重新回到旧路线。

## 持久化文件

**七个项目文件**

意义：把长期科研状态从聊天记忆中独立出来，形成可审计的项目真相源。

**`MASTER_FRAMEWORK` 可演化为主图但不能锁死故事**

意义：框架图服务于证据，不允许漂亮图反过来绑架实验解释。

## Evidence grading

**“Keep source prestige separate from evidential relevance.”**

意义：Nature 论文也可能只是相邻体系证据；期刊档次不是证据距离。

**A–E proximity scale**

意义：快速标识证据距离，而不是把文献证据、当前实验和机理推断混在一个层级。

**source quality separate**

意义：一篇直接但低质量的研究和一篇高质量但远距离的研究有不同问题，需要两个维度分别描述。

## 四个角色

**Collaborator**

意义：负责扩展可能性，不负责宣布想法正确。

**Reviewer**

意义：负责攻击创新和证据，不负责保护原方案。

**Methodologist**

意义：负责找到真正能区分解释的实验设计。

**Editor**

意义：在证据链已经形成后判断论文层级和完整度，而不是提前用“讲故事”替代科学判断。

**角色之间互不包庇的两句规则**

意义：防止“合作模式”让 reviewer 失去锋利，也防止“编辑模式”为了故事完整压掉矛盾数据。

## 路由现有 Skills

**“This skill owns…”**

意义：明确本 Skill 只拥有科学发现和决策层，不重复造文献、统计、写作、绘图工具。

**各个 Nature Skill 的路由句**

意义：让成熟工具继续负责自己擅长的执行层，`nature-research-partner` 只负责何时调用、为什么调用、结果如何改变科研状态。

**“Writing and figure production must not silently become substitutes…”**

意义：这是防止科研工作过早进入“写论文/画漂亮图”的关键闸门。

## 输出模式

**explore 输出**

意义：保证探索阶段输出的是问题状态，而不是过早给完整实验方案。

**challenge 输出**

意义：必须给出最强版本、baseline、反例、死亡条件和明确的继续/收窄/不值得结论。

**design 输出**

意义：进入可执行证据设计，并同步更新总框架。

**update 输出**

意义：新数据必须改变状态文件和下一步动作，而不是只写一段解释。

## Stop and downgrade

**停止或降级条件句**

意义：科研搭档必须敢于说“不要继续做”，不能把所有方向都无限优化。

**“A stopped idea is not wasted work.”**

意义：记录失败原因，把失败转化为未来的决策资产。

## Red lines

八条红线分别阻止：相关性机制化、表征机制化、显著性神化、伪创新、伪精确、为了数量制造 rival、迎合用户偏好、以及先做昂贵实验后问科学问题。

## 十项 QA

十个问题是重大科研决策前的最低检查。它们分别覆盖事实与解释、问题边界、baseline/rival、文献边界、区分性预测、死亡条件、claim–experiment 映射、证据距离、负结果的信息价值，以及下一步是否真正降低关键不确定性。

如果任何一项为 `no`，Skill 必须先暴露这个缺口，不能输出看似确定的路线。
