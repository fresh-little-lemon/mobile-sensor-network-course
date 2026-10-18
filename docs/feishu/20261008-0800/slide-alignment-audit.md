# 20261008-0800 课件图片审计

## 结论

- 已逐一下载并查看飞书原有24张PNG，与固定版本PDF对应页核对标题、版式、图示和页内幻灯片编号。24张均匹配，未发现错误图片或损坏图片
- 完整阅读121对双语段落及所有图片上下文。24张均与相邻讲解语义对应；未发现必须移动或补图的明确缺陷
- 现有图片覆盖幻灯片1–25，跳过4。图4是考试评分；00:11:26明确说忽略该评分说明并将修改，因此不按数字缺口判定漏图
- PDF的26–31页内幻灯片未出现在这段录音的相应讲解中；录音停于图25网状网络和休息安排，不能据此批量补到本稿
- 只读审计；未修改飞书双语文档、原始文字记录或妙记/音频

## 需保留的上下文细节

- 图2和3紧邻放在同一00:09:33长段之后；该段同时覆盖课程计划和参考资料，连续双图合理
- 图8和9紧邻放在00:19:16同一段之后；前半讲车辆测量，后半讲边缘计算和GPU，连续双图合理
- 图10在00:20:53提问/导论过渡段之后；图23在00:52:47 D2D/混合架构过渡段之后。两者对应混合段落的首句，位置可保留
- 所有重复时间戳均沿用原稿；本审计没有推断更精细的录音时间
- 图4的缺失具备讲稿解释，但无法仅凭当前稿证明最初插图者的意图，故结论为“可解释的省略”，而非断言其人为决策

## 图片对应表

|图|PDF|对应段落|标题|结论|
|---:|---|---|---|---|
|1|1 上|28 · 00:06:43|Welcome to MOBILE and SENSOR NETWORKS|匹配|
|2|1 下|32 · 00:09:33|Schedule|匹配|
|3|2 上|32 · 00:09:33|Available material|匹配|
|5|3 上|34 · 00:11:26|Exam rules|匹配|
|6|3 下|35 · 00:11:26|Available thesis|匹配|
|7|4 上|41 · 00:16:13|A real-world experimental infrastructure|匹配|
|8|4 下|44 · 00:19:16|Coverage and latency, measured on the street|匹配|
|9|5 上|44 · 00:19:16|Edge computing and hardware acceleration|匹配|
|10|5 下|45 · 00:20:53|QUESTIONS?|匹配|
|11|6 上|47 · 00:22:46|Introduction to Wireless Networks|匹配|
|12|6 下|49 · 00:22:46|Wireless applications and their needs|匹配|
|13|7 上|59 · 00:29:27|Elements of a wireless network: overview|匹配|
|14|7 下|63 · 00:31:50|Elements of a wireless network: wireless hosts|匹配|
|15|8 上|65 · 00:32:57|Elements of a wireless network: Point of Access|匹配|
|16|8 下|66 · 00:34:02|Elements of a wireless network: wireless link|匹配|
|17|9 上|68 · 00:34:43|Elements of a wireless network: wireless device radio|匹配|
|18|9 下|71 · 00:35:54|Classification|匹配|
|19|10 上|74 · 00:37:50|Coverage: Characteristics of selected wireless links|匹配|
|20|10 下|82 · 00:39:47|Networks architecture: edge and core|匹配|
|21|11 上|86 · 00:43:47|Network architecture: Taxonomy|匹配|
|22|11 下|101 · 00:50:36|With infrastructure|匹配|
|23|12 上|103 · 00:52:47|No infrastructure|匹配|
|24|12 下|104 · 00:54:39|The hybrid case: Connected Cars|匹配|
|25|13 上|110 · 00:56:29|Wireless Mesh Networks|匹配|

## 来源与文件

- [飞书双语文档](https://lcn6dqn3m0yr.feishu.cn/docx/SJM4dzPKHo4upfxK4yjcLTz9nBj)
- [固定版本源PDF](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/01_Introduction_MSN_26-27.pdf)
- bilingual-20261008-0800.md：含章节/逐段标题、原121对段落及24张原图的可发布Markdown；未发布到外部平台
- slide-source-manifest.json：每图的源页、标题、精确段落位置、文件路径、尺寸、SHA-256和审计说明
- slide-images/：从现有飞书文档下载的原PNG；未重新裁切或重绘
- 01_Introduction_MSN_26-27.pdf：固定版本PDF原文件
- audit/existing-contact-1.png 至 existing-contact-3.png：全部24张原图的审阅联络表

音频二进制不在此包内；Markdown保留原始录音播放链接。图片和讲稿的再发布许可未在本次只读审计中另行核验。
