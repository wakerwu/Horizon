---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 92 条内容中筛选出 7 条重要资讯。

---

**AI 创作者雷达**
1. [美团开源 LongCat-2.5，称训练未用英伟达 GPU](#item-ai-creator-1) ⭐️ 8.0/10
2. [超 11.5 万人联署请愿，要求英伟达恢复黄仁勋职务](#item-ai-creator-2) ⭐️ 7.0/10
3. [Meta FAIR 与 NYU 训练 200+ 多模态模型，拆解视觉编码的三个选择](#item-ai-creator-3) ⭐️ 7.0/10
4. [开源工具称在 B300 上将 pageable cudaMemcpy 提速 5 倍](#item-ai-creator-4) ⭐️ 7.0/10
5. [世界模型驱动的多人游戏 beta：本地 GPU 生成各自视角](#item-ai-creator-5) ⭐️ 7.0/10
6. [特斯拉 Cybercab 条款：车价 29,990 美元，月付 299 美元订阅才能开](#item-ai-creator-6) ⭐️ 7.0/10
7. [华为云上线开源盘古模型 openPangu-2.1-Pro](#item-ai-creator-7) ⭐️ 7.0/10

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [美团开源 LongCat-2.5，称训练未用英伟达 GPU](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美团 LongCat 团队在模型发布一周后开源了 LongCat-2.5 的权重，该模型面向可自主完成多步骤任务的智能体，尤其针对编程场景。官方称训练全程使用华为升腾加速卡、未使用英伟达 GPU，模型每个 token 激活约 480 亿参数，支持文本、图像和视频输入，以 MIT 许可证发布、可商用。官方给出的 Terminal Bench v2.1 得分为 88.4，略低于 Claude Opus 5 的 89.1。上述性能与“未用英伟达”均为公司主张，尚无第三方复现，且来源为二手转述，标题所称 1.6 万亿参数与正文“每 token 激活约 480 亿”需在成稿时核对原始公告。

telegram · zaihuapd · 11月15日 11:08

**「为何值得注意」** 这是可复核的发布事件：权重已以 MIT 许可证公开，开发者可自行验证与选型；同时“全程升腾训练”的说法为国产算力叙事提供了新的具体案例。但该说法与基准得分目前均停留在官方口径，实际影响尚待第三方复现。

**「内容切入角度」** 可做角度：把“官方称全程升腾训练、未用英伟达”与“Terminal Bench v2.1 得分 88.4 对比 Claude Opus 5 的 89.1”并列呈现，说明哪些是可自行下载验证的事实（MIT 权重、多模态输入），哪些仍是待复现的公司主张，并提醒核对 1.6 万亿总参数与每 token 激活约 480 亿的表述差异。

**标签**: `#开源模型`, `#国产算力`, `#智能体编程`, `#模型评测`, `#美团 LongCat`

---

<a id="item-ai-creator-2"></a>
### [超 11.5 万人联署请愿，要求英伟达恢复黄仁勋职务](https://techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/) ⭐️ 7.0/10

一份请愿书要求英伟达董事会恢复近日辞职的 CEO 黄仁勋的职务，截至周六下午已获超过 11.5 万个签名。请愿网站称签名者包括 5965 名英伟达现任员工、1108 名前员工和 63063 名股东，知名支持者包括马斯克、Replit CEO Amjad Masad、Epic Games CEO Tim Sweeney 和 Y Combinator CEO Garry Tan。请愿书称签名者“担心黄仁勋在缺乏有意义的正当程序的情况下被免职”，要求董事会“在独立调查查明事实期间让他回来”。黄仁勋于周四辞职，此前四天他承认与一名被美国情报部门怀疑为中国间谍的芯片高管有婚外情；报道还称他有多段婚外情。英伟达已任命 CFO Colette Kress 为临时 CEO，公司股价本周大幅下跌。

rss · TechCrunch AI · 11月14日 21:41

**「为何值得关注」** 这是英伟达公司治理层面正在发生的事件：CEO 辞职、临时 CEO 接任、大规模请愿要求复职，且请愿方明确要求独立调查。黄仁勋辞职对 AI 行业融资的预期影响目前只是报道中的判断，尚未有可验证的结果。

**「内容角度」** 可做角度：梳理请愿书的具体诉求（恢复职务、独立调查、公开信息）与英伟达已采取的公司治理动作（任命临时 CEO、寻找正式继任者）之间的张力，并明确区分已确认的辞职事实与尚未证实的婚外情、间谍嫌疑等指控。

**标签**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#AI hardware`, `#tech industry petition`

---

<a id="item-ai-creator-3"></a>
### [Meta FAIR 与 NYU 训练 200+ 多模态模型，拆解视觉编码的三个选择](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 7.0/10

Meta FAIR 与 NYU 在相同数据和统一计算预算下从零训练了 200+ 个多模态大模型，分别检验视觉编码中常被捆绑的三个选择：独立预训练、仅视觉 token 使用的参数、以及编码器放在 LLM 之前。主要对比基于 Qwen3-1.7B 和 4B 配置、0.4B 视觉容量，并在 0.6B 到 6.4B 的骨干规模上做扩展，评测覆盖 Cambrian 的 16 个 VQA 基准（448 像素）和 12 个语言基准。结论是：编码器独立预训练可选，仅视觉参数必需，编码器放在 LLM 之前也可选。该工作目前是 alphaxiv 预印本，附博客和 FAQ，尚未经过同行评审。

reddit · r/MachineLearning · /u/trungh98 · 11月15日 17:38

**「为什么现在值得注意」** 作者指出当前已发布模型对视觉编码器的做法并不一致：Gemma 4 12B 去掉了编码器，Kimi K3 从零训练编码器，Inkling 2 Small 又把编码器加了回来；但这些模型在数据和计算上不同，且很少单独核算编码器预训练的成本，因此难以据此判断哪种选择更优。这项控制变量式的消融正好针对这一空白，不过其结论仍来自预印本，尚未经同行评审。

**「可做角度」** 可做角度：围绕“视觉需要自己的参数，但不需要自己的预训练或独立编码器”这一组拆分结论，解释实验中三个变量如何被分别控制、在哪些规模上成立，以及“免费预训练也不帮助 VQA”和“编码器免模型需约 3 倍计算追赶”这些具体数字的边界条件。

**标签**: `#multimodal-llm`, `#vision-encoder`, `#model-architecture`, `#research-paper`, `#training-ablation`

---

<a id="item-ai-creator-4"></a>
### [开源工具称在 B300 上将 pageable cudaMemcpy 提速 5 倍](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

开发者发布开源工具 cudamemcpy-tuner，用于加速 pageable 的 cudaMemcpy 传输。在 PyTorch 基准中，将 1 GB uint8 张量从 CPU 拷贝到 GPU 并同步，B300 上速度从 10.2 GB/s 提升到 51.5 GB/s，约 5 倍。该结果来自作者自测的单机基准，尚未经同行评审，主要影响需要大量主机到设备传输的开发者。

reddit · r/MachineLearning · /u/makneeee · 11月15日 18:20

**「为何值得注意」** 工具已开源并附博客与代码仓库，给出了可复现的基准脚本和具体数字；但 5 倍提升目前仅是作者在 B300 单机上的自报结果，尚未有第三方验证或更广泛硬件上的表现。

**「内容角度」** 可做角度：拆解 cudamemcpy-tuner 如何针对 pageable 传输做优化，并复现其 1 GB 张量 CPU→GPU 基准，说明 10.2→51.5 GB/s 的测量条件与适用边界。

**标签**: `#CUDA`, `#GPU内存传输`, `#性能优化`, `#开源工具`, `#PyTorch`

---

<a id="item-ai-creator-5"></a>
### [世界模型驱动的多人游戏 beta：本地 GPU 生成各自视角](https://www.reddit.com/r/MachineLearning/comments/1xx4ta3/we_made_a_multiplayer_game_where_each_players/) ⭐️ 7.0/10

团队基于自建 10 人 CS:GO bot 对局数据集（约 3,958 小时，所有视角与输入按 16 Hz 对齐）训练世界模型，并开放免费多人 beta。服务器只同步游戏状态，每位玩家用本地 GPU 运行扩散 Transformer，根据状态、操作和前一帧生成自己的画面。硬件要求 RTX 3080 及以上，另有实验性 Mac 构建；当前仅一张小地图、只用手枪，细节质量一般，团队称与原始游戏差距明显。

reddit · r/MachineLearning · /u/bengal7ion · 11月15日 19:46

**「为何值得注意」** 这是“世界模型作为游戏渲染器”的一次可实际游玩的多人演示，且配套数据集已公开在 Hugging Face。不过它仍属团队自述的测试阶段，尚无第三方评测或性能数据。

**「内容角度」** 可做角度：拆解“服务器只同步状态、客户端本地生成画面”的架构，对比传统游戏渲染管线，并如实标注当前限制（单地图、仅手枪、细节不足）与硬件门槛。

**标签**: `#世界模型`, `#扩散Transformer`, `#多人游戏`, `#本地推理`, `#开源数据集`

---

<a id="item-ai-creator-6"></a>
### [特斯拉 Cybercab 条款：车价 29,990 美元，月付 299 美元订阅才能开](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 7.0/10

特斯拉 Cybercab 配置器条款显示，车辆售价为 29,990 美元，车主须每月支付 299 美元自动驾驶订阅费，否则车辆无法运行。条款还规定特斯拉可提前一个月通知调价，欠费或违规使用可导致订阅暂停或取消，累计三次警告将停用自动驾驶一周；车辆仅在指定区域运行，未经授权不得接入网约车、配送或租赁平台。Electrek 指出，Cybercab 与用于 Robotaxi 的 Model Y 采用相同 AI4 硬件和自动驾驶软件，但面向普通车主的 FSD 仍需人类监督。上述内容为条款文本，实际执行细节（如区域范围、生效时间、是否已开放订购）在材料中尚不完整。

telegram · zaihuapd · 11月15日 01:10

**「为何值得注意」** 这是特斯拉首次在配置器条款中明确 Cybercab 的定价与订阅绑定模式，将车辆运行权与月度订阅直接挂钩，为理解其自动驾驶商业化路径提供了条款层面的依据。但条款不等于量产交付公告，实际落地方式仍有待观察。

**「内容角度」** 可做角度：从条款文本出发，梳理 Cybercab“车价+强制月订阅”的收费结构，对比传统一次性购车模式，并指出条款中调价权、停用规则和区域限制等关键约束，同时说明这些条款尚未等同于交付或开放订购。

**标签**: `#特斯拉`, `#Cybercab`, `#自动驾驶订阅`, `#商业模式`, `#Robotaxi`

---

<a id="item-ai-creator-7"></a>
### [华为云上线开源盘古模型 openPangu-2.1-Pro](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

11 月 15 日，华为云 MaaS 平台上线开源盘古模型 openPangu-2.1-Pro，主打 Agent 开发、AI 编码与推理优化，并公布每百万 tokens 定价：输入 0.8 元、输出 3.2 元、缓存命中输入 0.016 元。该模型基于 10 万余条专项数据优化 Skills 触发与工具调用，重点适配鸿蒙 ArkTS 开发与升腾算子生成，并接入智果 AgentArts、码道 CodeArts、果办 OfficeAce 等产品。来源为 Telegram 转发微信公众号，未见原始公告或技术报告，模型参数规模、基准表现、开源许可证及权重获取方式均未提供，“开源”的具体范围尚无法确认。

telegram · zaihuapd · 11月15日 16:03

**「为何值得关注」** 这是华为云首次在 MaaS 平台上线名为“开源”的盘古模型并公开按 token 计价，对关注国产模型定价与 Agent 开发工具链的开发者有直接参考价值；但“开源”是否包含权重下载、采用何种许可证，目前材料未说明，实际可用性仍需核实。

**「内容角度」** 可做角度：从“开源”标签与 MaaS 按量计费并存的矛盾切入，梳理 openPangu-2.1-Pro 已公布的三档 token 价格、适配的鸿蒙 ArkTS 与升腾算子场景，并列出参数规模、许可证、权重获取方式等尚未披露的信息，提醒读者区分“平台上线”与“真正可下载开源”。

**标签**: `#华为云`, `#盘古模型`, `#开源模型`, `#模型定价`, `#Agent开发`

---