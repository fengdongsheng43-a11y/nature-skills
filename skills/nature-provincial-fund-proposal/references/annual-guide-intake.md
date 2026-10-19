# Provincial / autonomous-region funding: annual-guide intake

## 主管机关与项目识别
`funder_level`: provincial / autonomous_region / municipality；
`region`, `ministry_or_department`, `year`, `scheme`, `subscheme`, `guide_title`, `official_guide_url`, `guide_attachment_hash`, `verified_on`, `institution`, `status`。
不要把国家自然科学基金“地区科学基金”放到地方基金里。

## 原始政策与项目级账本（每年建新版本）
| Rule group | Questions |
|---|---|
| 资格 | 在读博士/职称/年龄/导师同意/限项/在研项目/学位要求？ |
| 项目定位 | 面上、人才、博士、重点、联合或专项；指南支持什么？ |
| 立项与地方相关性 | 是否列出重点领域/区域问题？是否强制对接某产业/单位？ |
| 内部推荐 | 是否名额限制、学院排序、校内提前截止？ |
| 研究内容 | 类别要求、项目期限、里程碑、成果形式、交叉/协作要求？ |
| 财务 | 资助额度、预算结构、经费拨付、间接费/劳务费、支出限制？ |
| 申请书 | 模板、页数/字符数、附件、系统提交与单位审核步骤？ |
| 合规 | 数据共享、伦理、诚信、重复申报、AI辅助说明？ |

政策行：`id | exact_rule | jurisdiction | call_year | scheme | source_url | attachment/page | checked_at | access_status | verification_status | consequence`。
VERIFIED 仅限能回指官方文字/附件；转发学校通知与转载必须注明证据级别。任何缺失规则不得使用“通常规定”填空。
用户上传的新年度指南可替代旧年配置，不改变科研决策 Skill 内核。

## 内蒙古 2027 示例（仅历史快照；不能推断 2028）
- 自治区科技厅 2026-10-16 通知原始路径：https://kjt.nmg.gov.cn/kjdt/tzgg/202610/t20261016_2965565.html （本轮网页直接访问未成功，未完成主站全文核验）
- 2026-10-16 某高校的通知转述含当年项目分类（包括博士研究生项目），但属依托单位通知，不是所有高校的内部时间表：https://www.jnnu.edu.cn/kyc/info/1115/8970.htm
- 待用户提交：官方《2027年度自治区自然科学基金项目申请指南》原件及内蒙古大学当年校内通知；未提供前不锁定名额、系统截止、博士项目专属经费/评审细则。

## 新指南送入后的差异更新
按 `policy_id` 对比 `old_text / new_text / scope / impact / project_action`，标新增、变更、删除、不明；立即重审资格/内部推荐/预算/模板/项目规模，科学论点除非受项目边界影响不自动改变。
