# 20261009-0759 课件图片审计

## 结论

- 完整阅读67对双语正文，6张原PNG全部下载成功并逐一与固定版本PDF视觉比对；原图身份匹配、无损坏，均可保留现有位置
- 确认缺少《001-BasicConcepts.pdf》图52（PDF26下，Packet header）：第8–16段详细讲首部、载荷与CRC摘要，源图的首部校验位展开直接对应。原图51的纠错/检错比较和图54的收发确认示意不能代替此图
- 主任务已在飞书与本地Markdown第11段标题后、原文前加入图52；使用1049双语稿已下载核验的同一原PNG字节，不重绘图示、不改写图内术语
- 基础讲义图53的序列号未讲；Wi-Fi图2目录未逐项展开；图6–8的详细标准/速率/命名表未展开，不能仅凭编号跳过而判定缺图
- Wi-Fi图4虽在第49段后，但该段正好再次概括WLAN与IEEE标准，位置合理；不移动至前文首次提及处
- 已准备完整Markdown、7张原PNG、2份源PDF及逐图来源与段落映射清单。审计执行方未远程修改或发布；主任务已完成远程补图，审计执行方已独立复核完整快照与新增图下载字节

## 完整性与边界

- 67个原正文块的中英文、说话人、全部时间戳及段内换行逐字保留；首段保持原来的00:01:04，不虚构00:00:00
- 7个章节标题和67个逐段标题来自主任务heading-plan.json，独立于原文
- 6张原图的ID、图注、图片顺序及相邻正文位置完整保留；补图52位于第10与11段之间、第11段标题之后
- 图54原课件同时列出三种ARQ；正文明确只讲停止等待，不把另外两种方法当作已授课内容
- 原稿把CRC放入首部、个别receiver/transmitter称呼等技术/口述问题逐字保留，本审计不擅自科学核改
- 文首状态已更新为7张图、67个分段标题和7个主题标题；仅这条原状态信息作必要更新，67段正文与其他原块保持不变
- 不打包音频二进制，保留原始录音播放链接

## 图片对应表

|序号|来源/图号|PDF页/半页|位置|内容|结论|
|---:|---|---|---|---|---|
|1|001-BasicConcepts.pdf 图51|26 / 上|第10段后 · 00:09:00|FEC vs. ARQ: error correction and CRC detection|匹配|
|2|001-BasicConcepts.pdf 图52|26 / 下|第11段标题后、正文前（新增）|Packet header: parity bits in the header|匹配|
|3|001-BasicConcepts.pdf 图54|27 / 下|第19段后 · 00:16:58|ARQ: stop-and-wait and acknowledgments|匹配|
|4|02-WiFi_1-7.pdf 图1|1 / 上|第36段后 · 00:26:28|Wireless LANs: From IEEE 802.11 to Wi-Fi 7|匹配|
|5|02-WiFi_1-7.pdf 图3|2 / 上|第48段后 · 00:30:07|Introduction & 802.11 Architecture|匹配|
|6|02-WiFi_1-7.pdf 图4|2 / 下|第49段后 · 00:30:07|What is IEEE 802.11?|匹配|
|7|02-WiFi_1-7.pdf 图5|3 / 上|第50段后 · 00:30:07|Where 802.11 Sits in the Protocol Stack|匹配|

## 核验资料

- [飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/GSiDdfhZHoJ99Ux1XducLUkgn6b)
- [001-BasicConcepts.pdf固定版本](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/001-BasicConcepts.pdf)
- [02-WiFi_1-7.pdf固定版本](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf)
- slide-source-manifest.json：源PDF版本/哈希、页/半页、图片哈希、原块ID和图注、相邻段落、语义范围和逐图判定
- bilingual-20261009-0759.md：67对原文、7个章节标题、67个逐段标题与7张图
- slide-images/：6张原稿PNG及新增图52原PNG
- audit/existing-contact.png：6张原图视觉审阅联络表
- audit/source-contact.png：固定PDF对应原页与边界页视觉比对表
- audit/missing-slide-052.json：补图依据、原PNG来源、哈希和建议插入位置
- audit/verification.json：逐字、顺序、原图位置和标题数量自动验证结果

最终远程快照已独立回读比对：67个二级标题、7个章节标题及7张图准确；除文首状态计数外，所有原非根块逐块不变。新增图52位置准确，远程重新下载的PNG与原PNG的SHA256完全相同。
