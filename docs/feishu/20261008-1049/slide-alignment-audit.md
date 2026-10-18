# 20261008-1049 课件图片审计

## 结论

- 完整阅读88对双语正文，25张原PNG全部下载成功并逐一与固定版本PDF视觉比对；图27–50及52均身份匹配，未发现损坏、明确缺图或必须移动的图片
- 图45虽在图48之后，但紧接第76段接收端重算和比较校验位的回顾，语义一致；保留原位置，不机械按PDF页码重排
- 图47本身同时包含重复码和单个奇偶校验位两种示例，已覆盖第52–70段；不存在独立校验位图片的遗漏
- 图51讲FEC/ARQ校验位用于纠错或检错、CRC的区别，本段只引入ARQ后即解释数据包结构，未展开该页内容，因此不能仅凭编号跳过而判定缺图
- 图53–54的序列号及三种ARQ协议未在这段展开；第87段明确留到明天继续，不补入尚未讲解的后页
- 已准备完整Markdown、25张原PNG、源PDF及逐图来源与段落映射清单；未发布仓库，未远程修改图片、原始文字记录或录音

## 完整性与边界

- 88个原正文块的文字、说话人、全部时间戳和段内换行逐字保留；首段保持原来的00:01:10，不虚构00:00:00
- 9个章节标题和88个逐段标题来自主任务heading-plan.json，独立于原文
- 25张图片保持原图顺序、原图注以及原相邻正文位置；图45非顺序位置也保留
- 图34配合快慢衰落时间尺度讲解；原稿对曲线颜色的口述细节原样保留，不把技术表述核改混入图片位置审计
- 源PDF审阅图的裁切只用于本地比对；私仓准备材料使用飞书下载的原PNG字节，不用审阅裁切图替换原图

## 图片对应表

|序号|图号|PDF页 / 半页|原位置|内容|结论|
|---:|---:|---|---|---|---|
|1|27|14 / 上|第1段后 · 00:01:10|Diffraction: secondary electromagnetic sources|匹配|
|2|28|14 / 下|第3段后 · 00:01:10|Reflection: reflected ray and receiver|匹配|
|3|29|15 / 上|第7段后 · 00:04:16|Diffraction: path lengths and phase differences|匹配|
|4|30|15 / 下|第9段后 · 00:06:54|Diffraction: constructive and destructive interference|匹配|
|5|31|16 / 上|第13段后 · 00:06:54|Multipath: echoes, amplitude and phase|匹配|
|6|32|16 / 下|第18段后 · 00:11:33|Shadowing: slow variation|匹配|
|7|33|17 / 上|第19段后 · 00:11:33|Fast Fading: moving obstacles|匹配|
|8|34|17 / 下|第21段后 · 00:13:11|Example: Shadowing and Fast Fading|匹配|
|9|35|18 / 上|第21段后 · 00:13:11|Urban multipath channel: 20–30 dB attenuation|匹配|
|10|36|18 / 下|第22段后 · 00:14:37|Example: macrocell|匹配|
|11|37|19 / 上|第24段后 · 00:16:01|Microcell environment|匹配|
|12|38|19 / 下|第25段后 · 00:16:01|Attenuation: distance, atmosphere, shadowing and multipath|匹配|
|13|39|20 / 上|第27段后 · 00:16:01|SNR: signal-to-noise ratio|匹配|
|14|40|20 / 下|第30段后 · 00:18:04|SINR: signal-to-interference-plus-noise ratio|匹配|
|15|41|21 / 上|第39段后 · 00:23:58|Errors: SNR/SINR and BER|匹配|
|16|42|21 / 下|第41段后 · 00:23:58|Error detection and recovery|匹配|
|17|43|22 / 上|第42段后 · 00:25:18|Possible techniques: FEC, ARQ and diversity|匹配|
|18|44|22 / 下|第42段后 · 00:25:18|FEC: block and convolutional codes|匹配|
|19|46|23 / 下|第44段后 · 00:25:18|Block codes: k user bits and n−k redundant bits|匹配|
|20|47|24 / 上|第55段后 · 00:29:49|Example: repetition code and parity bits|匹配|
|21|48|24 / 下|第71段后 · 00:38:05|Example: row and column parity|匹配|
|22|45|23 / 上|第76段后 · 00:38:45|FEC: receiver recomputes and compares codes|匹配|
|23|49|25 / 上|第78段后 · 00:38:45|Convolutional codes: shift register|匹配|
|24|50|25 / 下|第79段后 · 00:41:48|ARQ|匹配|
|25|52|26 / 下|第85段后 · 00:45:10|Packet header: PDU, PCI and SDU|匹配|

## 核验资料

- [飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/ENxEdQVrvoRZ6lxgUeAcu5yBnng)
- [001-BasicConcepts.pdf固定版本](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/001-BasicConcepts.pdf)
- slide-source-manifest.json：源PDF版本/哈希、页/半页、图片哈希、原块ID和图注、相邻段落、语义范围和逐图判定
- bilingual-20261008-1049.md：88对原文、9个章节标题、88个逐段标题与25张图
- slide-images/：25张原稿PNG
- audit/existing-contact-1.png 至 existing-contact-5.png：25张原图视觉审阅联络表（按图号排序，仅为审阅）
- audit/source-contact-1.png 至 source-contact-5.png：固定PDF对应半页视觉比对表
- audit/basic-14.png 至 basic-27.png：源PDF原页及后续边界页
- audit/verification.json：逐字、顺序、原图位置和标题数量自动验证结果

音频二进制未打包；Markdown保留原始录音播放链接。最终远程快照已独立回读比对：88个二级标题、9个章节标题准确；所有原非根块逐块不变，正文与25图顺序及相邻位置保持。
