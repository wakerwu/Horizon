---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 89 条内容中筛选出 6 条重要资讯。

---

**AI 创作者雷达**
1. [OpenRouter 披露推理供应商数据处理事件](#item-ai-creator-1) ⭐️ 8.0/10
2. [Anthropic 数学家与 Claude 声称证明 Navier–Stokes 问题，同日另有 940 页纯人类黎曼猜想草稿公开](#item-ai-creator-2) ⭐️ 8.0/10
3. [分析称 Anthropic 2028 年电力 87% 来自天然气、11% 来自煤炭](#item-ai-creator-3) ⭐️ 7.0/10
4. [Gemini 将拆分“保留活动记录”为两项独立设置](#item-ai-creator-4) ⭐️ 7.0/10
5. [OpenCode 将 GLM-5.3 与 DeepSeek V4.1 Flash API 价格降至四折](#item-ai-creator-5) ⭐️ 7.0/10
6. [特朗普政府被指批准向中国关联公司出售 58 万颗英伟达 AI 芯片](#item-ai-creator-6) ⭐️ 7.0/10

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [OpenRouter 披露推理供应商数据处理事件](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) ⭐️ 8.0/10

OpenRouter 发布公告，说明其推理供应商出现数据处理事件，涉及 MiniMax 读取或转发提示词。社区讨论提到，部分供应商（评论中提及 AtlasCloud、Novita、StreamLake）可能将请求转发至 MiniMax 服务器，而非自行处理。有用户称收到邮件，并提到安全研究员通过植入诱饵 URL 发现访问行为。受影响的是使用 OpenRouter 多模型路由的开发者与用户；具体影响范围、供应商名单和整改措施需以公告原文核实，评论中的部分说法属于用户转述。

hackernews · sdko · 11月22日 02:14 · [社区讨论](https://news.ycombinator.com/item?id=50595554)

**「为何值得注意」** 该公告已发布并引发 HN 讨论（272 分、90 条评论），显示真实用户关注；但事件细节与整改力度尚未在材料中完整证实。

**「内容切入角度」** 可做角度：从 OpenRouter 公告出发，梳理多模型路由场景下“供应商转发提示词”与零数据保留（ZDR）承诺之间的信任缺口，并说明开发者可通过供应商白名单等设置降低暴露面。

**「社区讨论」** 评论中有人因该事件放弃考虑迁移至 OpenRouter，也有人肯定其回应但认为直接与推理供应商签订 ZDR 协议更可靠；有用户称仅一个提示词受影响，并已将路由限制为可信供应商。共识是供应商转发行为令人担忧，但对 OpenRouter 整改是否足够存在分歧。

**标签**: `#OpenRouter`, `#数据隐私`, `#推理供应商`, `#MiniMax`, `#LLM 路由`

---

<a id="item-ai-creator-2"></a>
### [Anthropic 数学家与 Claude 声称证明 Navier–Stokes 问题，同日另有 940 页纯人类黎曼猜想草稿公开](https://www.qbitai.com/2026/11/511870.html) ⭐️ 8.0/10

11 月 20 日，Anthropic 数学家 Levent Alpöge 与纽约大学教授 Tristan Buckmaster 公布 79 页论文，声称证明三维 Navier–Stokes 方程的无外力有限时间爆破，并公开 Lean 形式化证明代码。同日，数学家 Alessandro Maria Masullo 发布未使用 AI 的广义黎曼猜想证明草稿，篇幅 940 页，耗时近 12 年。两项主张均待独立核验；陶哲轩已发文讨论 NS 证明，认为大体策略清楚但仍需整理成规范文本。

rss · 量子位 · 11月22日 06:03

**「为何值得关注」** 两项千禧年难题的证明主张在同一天公开，且一项明确由 Claude 参与生成、整理和重写，另一项强调纯人类完成，形成 AI 辅助数学与人类长期研究的直接对照。但两者均非已确认成果，NS 证明的数值证书尚未公开，黎曼猜想草稿公开约 8 小时后已有研究者借助不同 AI 模型报告问题，最终能否成立仍待确认。

**「内容切入角度」** 可做角度：从“有论文、有 Lean 代码”不等于“外界已完整验证”切入，梳理 NS 证明公开仓库中数值证书未公开、Lean 包未重新构建等具体待核验环节，说明 AI 参与生成证明与人类复核证明之间的进度差。

**标签**: `#千禧年难题`, `#Navier-Stokes`, `#AI辅助数学证明`, `#Lean形式化验证`, `#数学研究范式`

---

<a id="item-ai-creator-3"></a>
### [分析称 Anthropic 2028 年电力 87% 来自天然气、11% 来自煤炭](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 7.0/10

一篇分析文章称，Anthropic 在 2028 年的电力结构将为 87% 天然气、11% 煤炭。该数据来自第三方分析而非 Anthropic 官方公告，统计口径尚待核实。文章在 Hacker News 引发高热度讨论，焦点是 AI 数据中心的能源来源与环境外部性。

hackernews · happosai · 11月22日 08:57 · [社区讨论](https://news.ycombinator.com/item?id=50597612)

**「为何值得注意」** AI 数据中心的用电规模正快速上升，而这份分析给出了一个具体到年份和燃料比例的量化口径，使“AI 电力从哪来”从抽象讨论变成可核对的问题。不过其数字来自第三方推算，尚未获 Anthropic 确认。

**「内容角度」** 可做角度：把“87% 天然气、11% 煤炭”当作一个待核实的第三方估算来拆解——说明数据来源、统计边界和不确定性，再对照 Anthropic 是否公开过可再生能源承诺，呈现事实与推测的边界。

**「社区讨论」** 评论者多批评 Anthropic 在能源与污染上的表现，有人提到其租用 Colossus 1 对孟菲斯当地造成污染，并指出其在美国缺乏可再生能源承诺；也有人主张需要监管来内部化环境与社会成本。另有评论强调数据中心能耗规模远超公众直觉。这些是评论者观点，不代表已核实的事实。

**标签**: `#AI 数据中心能耗`, `#Anthropic`, `#环境影响`, `#能源结构`, `#AI 基础设施`

---

<a id="item-ai-creator-4"></a>
### [Gemini 将拆分“保留活动记录”为两项独立设置](https://blog.google/innovation-and-ai/products/gemini-app/updated-controls/) ⭐️ 7.0/10

Google Gemini 团队发布通知称，将在未来几周内用两项新设置取代 Gemini 应用的“保留活动记录”：一项控制历史记录保存时长，另一项单独决定对话内容（含文字与附件）是否用于训练生成式 AI 模型。用户可保留对话记录但关闭训练授权。关闭“历史记录”后，新的 Gemini 对话约保存 2 个月，并在人工审核员协助下用于回复用户、处理反馈及保护 Google 与公众。变更生效时，两项设置按原开关状态同步开关；音频与 Gemini Live 录音默认仍不用于改进 Google 服务。

telegram · zaihuapd · 11月22日 01:24

**「为何值得注意」** 这是 Google 官方博客公告的二手转述，核心变化明确：原先单一的“保留活动记录”被拆成历史记录保存时长与训练数据授权两项独立设置。具体上线时间仅称“未来几周”，实际影响尚待生效后观察。

**「内容角度」** 可做角度：从“保留记录但关闭训练授权”这一新选项出发，梳理 Gemini 设置变更前后用户可做的隐私选择，并说明关闭历史记录后约 2 个月的保存期限与人工审核用途。

**标签**: `#Google Gemini`, `#隐私设置`, `#训练数据`, `#用户数据授权`, `#产品更新`

---

<a id="item-ai-creator-5"></a>
### [OpenCode 将 GLM-5.3 与 DeepSeek V4.1 Flash API 价格降至四折](https://opencode.ai/console/models) ⭐️ 7.0/10

OpenCode 模型价格页显示，GLM-5.3 与 DeepSeek V4.1 Flash 均标注「60% off」，即按原价四折计费。每百万 token 费率：GLM-5.3 输入 $0.56、输出 $1.76、缓存读取 $0.104；DeepSeek V4.1 Flash 输入 $0.12、输出 $0.48、缓存读取 $0.0024。受影响的是通过 OpenCode 调用这两款模型的开发者，但来源为 Telegram 频道转述，未附官方公告，折扣截止时间与是否长期有效均不明确。

telegram · zaihuapd · 11月22日 03:48

**「为何值得注意」** 价格页已显示四折费率，属于可核查的当前标价变化；但折扣的持续时间和适用范围尚未证实，不宜据此推断长期成本。

**「内容角度」** 可做角度：以价格页列出的每百万 token 输入、输出、缓存读取费率为基准，整理一张 GLM-5.3 与 DeepSeek V4.1 Flash 的四折价对照表，并明确标注折扣截止时间未知这一不确定性。

**标签**: `#API定价`, `#OpenCode`, `#GLM-5.3`, `#DeepSeek V4.1`, `#开发者成本`

---

<a id="item-ai-creator-6"></a>
### [特朗普政府被指批准向中国关联公司出售 58 万颗英伟达 AI 芯片](https://news.google.com/rss/articles/CBMigAFBVV95cUxPSFVFUUxURXk5V2poUzA2eGU3dEoxV2QwUXdzVlJteWVxOWFzXzZSUUNreTZsU182V0FDMzhfS1NHV0lvQzk1V09IbFlILWcwOGhlVDZnRUQtNFhWQnkwZFBEVlV3QVpOcU1TSGxMTEdocjhNRk9YUkR5bUNWQ3oycQ?oc=5) ⭐️ 7.0/10

一则报道称，特朗普政府批准向与中国有关联的公司出售 580,000 颗英伟达 AI 芯片，并称政府将从中抽取分成。目前可获取的内容仅有标题和跳转链接，没有正文、官方公告或可核实细节，芯片型号、涉及公司、分成机制和生效时间均不明确。来源为知名度较低、自称“挖掘可验证真相”的 OGM News NG，该说法尚待核实。

google\_news · OGM News NG - Digging Deep for Verifiable Truth · 11月22日 07:00

**「为何值得注意」** 若该说法属实，这将是涉及 AI 硬件供应和中美科技政策的重要变化；但现阶段只有标题层面的信息，政策是否真正落地、适用范围多大都未获证实。

**「内容角度」** 可做角度：以“一条只有标题的重大政策传闻”为切口，梳理这条消息目前能确认什么、缺哪些关键信息（芯片型号、买方身份、政府分成方式、生效时间），并说明在官方公告或权威媒体核实前不宜当作既成事实传播。

**标签**: `#Nvidia`, `#AI芯片出口管制`, `#中美科技政策`, `#供应链`, `#待核实`

---