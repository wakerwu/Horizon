---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 76 条内容中筛选出 5 条重要资讯。

---

**AI 创作者雷达**
1. [OpenRouter 披露推理供应商数据处理事故](#item-ai-creator-1) ⭐️ 8.0/10
2. [OpenAI 发文将困惑度作为基础模型预训练进展的简单基准](#item-ai-creator-2) ⭐️ 7.0/10
3. [Anthropic 数学家称用 Claude 辅助证明三维 Navier–Stokes 爆破，Lean 代码已公开但待核验](#item-ai-creator-3) ⭐️ 7.0/10
4. [OpenCode 页面显示 GLM-5.3 与 DeepSeek V4.1 Flash API 价格四折](#item-ai-creator-4) ⭐️ 7.0/10
5. [待核实：美方被指放行英伟达对华出售约 87.9 万颗 AI 芯片](#item-ai-creator-5) ⭐️ 7.0/10

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [OpenRouter 披露推理供应商数据处理事故](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) ⭐️ 8.0/10

OpenRouter 发布公告，披露其推理供应商存在数据处理事故。据评论转述，部分供应商（评论提及 AtlasCloud、Novita、StreamLake）将请求转发至上游 MiniMax，而非自行处理；有安全研究者通过植入诱饵 URL 发现请求被访问。评论还提到 OpenRouter 的零数据保留（ZDR）承诺在此次事件中失效。受影响的是使用 OpenRouter 路由、依赖其隐私承诺的开发者；具体受影响范围、供应商完整名单与整改措施仍需以公告原文核实。

hackernews · sdko · 11月22日 02:14 · [社区讨论](https://news.ycombinator.com/item?id=50595554)

**「为何值得注意」** 这是平台层面首次公开承认推理供应商存在数据处理问题，直接触及开发者对提示词隐私与供应商路由的信任。已发生的是公告披露与用户收到邮件通知；对 OpenRouter 供应商审核机制的实际影响尚未证实。

**「内容角度」** 可做角度：梳理 OpenRouter 公告中承认的供应商转发行为与 ZDR 承诺之间的落差，说明开发者如何通过限制可选供应商来降低提示词外流风险，并标注哪些细节仍待官方原文确认。

**「社区讨论」** 评论分歧明显：有人因该事件放弃迁移到 OpenRouter，认为其缺乏供应商审核；也有人肯定 OpenRouter 的回应，但指出最可靠的 ZDR 仍是与推理供应商直接签约。有用户称仅一条提示词受影响、影响不大，但已手动限制可选供应商；另有评论提醒不应默认任何供应商会遵守公开的数据保留承诺。

**标签**: `#OpenRouter`, `#数据隐私`, `#推理供应商`, `#零数据保留`, `#AI 安全`

---

<a id="item-ai-creator-2"></a>
### [OpenAI 发文将困惑度作为基础模型预训练进展的简单基准](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

OpenAI 发布文章，将困惑度（perplexity）定位为追踪基础模型预训练进展的简单基准，但文章本身未给出困惑度的定义。Hacker News 上该帖获得 482 分、334 条评论，讨论集中在困惑度与智能的关系以及这一指标是否仍然重要。评论中有人引用 Mustafa Suleyman 的推文，称微软 MAI-2 Base 在同一评测集上的对数困惑度为 0.819，与 GPT-5.6 Sol 基础模型处于同一量级；该数字来自第三方推文而非 OpenAI 原文，尚未独立验证。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「为何值得注意」** 在评测基准日益复杂、RL 训练占比上升的背景下，OpenAI 提出用一个简单的留出集困惑度来观察预训练进展，引发了对“交叉熵损失是否仍重要”的讨论。微软方面声称加入同一评测集，但目前只有推文层面的说法，缺乏可复核的细节。

**「内容角度」** 可做角度：梳理“困惑度作为预训练进展基准”这一提法的具体主张与边界——它衡量的是什么、文章没有定义什么、以及微软 MAI 数字目前仅来自推文这一证据层级，帮助读者区分已发布主张与未验证说法。

**「社区讨论」** 评论者对困惑度趋势的清晰度感到意外，认为在 RL 广泛使用后交叉熵损失仍具指示性；也有人肯定这种简单基准优于日益复杂的评测。另有评论补充了困惑度的定义，并引用 2008 年关于预测率与压缩的论文来支持这一对应关系。

**标签**: `#perplexity`, `#base-models`, `#pre-training`, `#evaluation-benchmarks`, `#OpenAI`

---

<a id="item-ai-creator-3"></a>
### [Anthropic 数学家称用 Claude 辅助证明三维 Navier–Stokes 爆破，Lean 代码已公开但待核验](https://www.qbitai.com/2026/11/511870.html) ⭐️ 7.0/10

Anthropic 数学家 Levent Alpöge 与纽约大学教授 Tristan Buckmaster 于 11 月 20 日发布 79 页论文，声称证明了三维 Navier–Stokes 方程在无外力条件下的有限时间爆破，并公开了 Lean 形式化证明代码。陶哲轩发文称该证明的大体策略已清楚，但仍需整理成规范证明文本并等待独立核验。作者公开的仓库显示，支撑证明构造的数值证书尚未公开，发布当天打过补丁的 Lean 包在组装仓库时也尚未重新构建，因此外界尚不能完整复核。同日，数学家 Alessandro Maria Masullo 发布了一份耗时近 12 年、约 940 页的广义黎曼猜想证明草稿，该草稿未使用 AI，公开约 8 小时后已有研究者借助不同 AI 模型报告其中存在问题。

rss · 量子位 · 11月22日 06:03

**「为何值得关注」** 这是 AI 辅助数学证明进入千禧难题级别问题的具体案例，且论文、Lean 代码和第三方回应均已公开，具备可追踪的核验路径。但核心主张尚未经同行验证，数值证书缺失和 Lean 包未重建也构成当前复核的明确障碍。

**「内容切入角度」** 可做角度：围绕“有论文、有 Lean 代码不等于已完整验证”这一张力，梳理该证明从公开到可独立复核还缺哪些环节——数值证书何时公开、计算能否复现、形式化代码能否独立检查，以及陶哲轩所说“策略清楚但需规范文本”具体指什么。

**标签**: `#Navier-Stokes`, `#千禧难题`, `#Lean形式化证明`, `#AI辅助数学`, `#Anthropic`

---

<a id="item-ai-creator-4"></a>
### [OpenCode 页面显示 GLM-5.3 与 DeepSeek V4.1 Flash API 价格四折](https://opencode.ai/console/models) ⭐️ 7.0/10

OpenCode 模型价格页显示，GLM-5.3 与 DeepSeek V4.1 Flash 的 API 价格均标注「60% off」，即按原价四折计费。页面列出每百万 token 费用：GLM-5.3 输入 $0.56、输出 $1.76、缓存读取 $0.104；DeepSeek V4.1 Flash 输入 $0.12、输出 $0.48、缓存读取 $0.0024。该信息来自 Telegram 频道转述，未附官方公告或折扣期限，折扣是否长期、是否仅限 OpenCode 渠道尚不确定。

telegram · zaihuapd · 11月22日 03:48

**「为何值得注意」** 两款模型同时出现四折标价，对正在做 API 成本核算的开发者有直接参考价值；但折扣的生效范围与持续时间尚未由官方渠道确认。

**「内容角度」** 可做角度：以 OpenCode 页面列出的每百万 token 单价为基准，对比 GLM-5.3 与 DeepSeek V4.1 Flash 在输入、输出和缓存读取三项上的费用差异，并注明该折扣仅见于第三方聚合页面、官方公告与期限待核实。

**标签**: `#API 定价`, `#GLM-5.3`, `#DeepSeek V4.1`, `#OpenCode`, `#开发者成本`

---

<a id="item-ai-creator-5"></a>
### [待核实：美方被指放行英伟达对华出售约 87.9 万颗 AI 芯片](https://news.google.com/rss/articles/CBMimwFBVV95cUxOSkNyOXNKcTlJNm9tZ3lqcGV0UFZ1Tmc2c2l4alZYU1AxWl9yYlV0MF9YTUxaQ3NtaXFROC03eEd5dklsWTQ4UXhnS29wV3FIUG1rSnFYQkh5YlRjLURXR3RCM0MwemZZS0pEcHdDMmxnUno2ZjR6NENMMmREVkZHNFdlbXNxNTRpZklJZ21IdWY4dWVsRUpOa2c1cw?oc=5) ⭐️ 7.0/10

Korben 的一篇报道标题称，美国放行英伟达向与军方有关联的中国巨头出售约 87.9 万颗 AI 芯片。目前可获取的内容仅为标题和 Google News 跳转链接，没有原始公告、官方文件或芯片型号、交易条件、时间窗口等可核实细节，因此该数字与“军方关联”的表述均无法确认。若属实，这一规模将直接影响 AI 算力供给与出口管制执行，但现阶段应视为待核实线索。

google\_news · Korben · 11月22日 07:56

**「为何值得注意」** 该标题指向一项具体的政策与出口变化，涉及英伟达对华销售和出口管制，属于当下中美科技与 AI 算力议题的敏感方向。但材料未提供一手来源，变化是否已发生、适用范围如何均未证实。

**「内容角度」** 可做角度：以“一条只有标题的放行传闻”为切口，梳理核实这类出口管制消息需要哪些一手证据（官方公告、许可文件、芯片型号与数量口径），并说明在缺乏这些信息时为何不宜直接下结论。

**标签**: `#英伟达`, `#出口管制`, `#AI芯片`, `#中美科技`, `#政策监管`

---