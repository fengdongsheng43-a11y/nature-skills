# Dual grant Skill smoke-test cases (design-time; not executed automated QA)

| Input | Expected router | Must flag | Must not do |
|---|---|---|---|
| “2027 国自然青年 C，只有题目” | nature-nsfc-proposal | 年度规则待核对，先五类文献检索、竞争假设 | 默认套用2026限页 |
| “2026 国自然地区科学基金申请” | nature-nsfc-proposal | 属于 NSFC 国家项目，资格按对应指南 | 路由省基金 |
| “2027 内蒙古自治区博士研究生自然基金” | nature-provincial-fund-proposal | 官方2027附件/校内名额/与博士论文重叠待核对 | 直接采用NSFC模版/经费 |
| “广东2028省自然面上” | nature-provincial-fund-proposal | 广东2028指南未获取，规则 UNKNOWN | 使用内蒙古/广东2025细则 |
| “低温性能提升证明EPS主导抗冷” | both via nature-research-partner | 提出传质/初始菌量/驯化等对立解释和P0识别实验 | 写成 demonstrated mechanism |
| “我换了年度指南” | matching skill update | POLICY_DIFF、重新核资格/模版/预算；保留研究状态 | 覆盖旧假设为已证实 |
| “已有很长的申请书请润色” | matching skill revise | 先逻辑+文献审计，再作者控制修改 | 在缺机制证据时增添强因果 |
| “请保证我这个项目肯定中” | matching skill challenge | 明确不能估计无证据中标率 | 虚构真实评审内幕 |

实施性 QA 下一步：在一次真实年度指南入库后，逐案验证政策字段提取、章节跟随实际系统模板、缺失的 BLOCKED 路径、各来源标注、科研与项目之间的隔离。
