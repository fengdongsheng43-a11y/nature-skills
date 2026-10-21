# 第二轮：WR × ES&T 全刊数据抓取执行与验收记录

- 记录日期：2026-10-21
- 研究对象：Water Research（ISSN-L 0043-1354，OpenAlex S52566953）；Environmental Science & Technology（ISSN-L 0013-936X，OpenAlex S13479253）
- 研究窗口：2024-01-01 至 2026-10-21；2026 年使用同日历截点同比
- 排除：Nature Water；AFM 不纳入全刊分母，仅后续定向参照
- 分母：OpenAlex 按 primary_location.source.id 索引的 work 记录；研究论文主口径采用 article_proxy，未宣称完成出版社逐篇类型校对
- 方法：逐刊、逐年、逐页抓取；每组 API meta.count 严格匹配；源期刊与发表日期校验；DOI/ID 去重；14+ 研究主题多标签标题摘要规则和 OpenAlex 当前主题模型分别计数；绝对篇数、刊内份额、百分点变化；2026 同期截点
- 原始文献记录：仅 GitHub Actions artifact 备存，未写入长期仓库
- 待校验：2026 索引滞后、摘要缺失、类型误分、话题规则漏检误检、特殊专题偏倚、出版社在线日期差异
- 模型变更：OpenAlex 于 2026-10-06 更新话题模型；2026-07 更新文献类型分类。不要拼接新旧快照或将 article_proxy 表述为官方原创论文清单。
- 数据库连接情况：ChatGPT 本地容器不能解析 api.openalex.org；基于 GitHub Actions 联网执行的工作流已经提交至 feature/nature-journal-trends。
- Workflow：.github/workflows/wr-est-openalex-census.yml
- Script：skills/nature-journal-trends/scripts/run_census.py
- 完成的唯一有效证据：data/latest/COMPLETE.json 与同期 corpus_audit.csv、REPORT.md **真实出现**，且有可信 counts、完整性标记、检索时间和 hash。
- 本次检查状态：上述结果文件**尚未出现**。因此本轮仅完成联网执行路径搭建，不声明全刊抓取完成或已有新热点排行榜。
- 若 GitHub fork 的 Actions 被禁用：在仓库 Actions 页面按 GitHub 提示启用；若 API 拒绝分页或出现频率限制，在 GitHub 仓库设置增加 OPENALEX_API_KEY secret 后手动触发。
- 结论升级门槛：下载完整逐篇索引；每刊×每年源期刊/DOI/时间/类型审计；筛选文章形式；主题抽样人工验证（跨年份、刊别、类别）；稳定性分析；再输出真正的 2024→2025 与 2025→2026 同期份额变化及近似竞争基线。
