# 20261008-1000 课件图片审计

## 结论

- 完整阅读81对原有双语段落，并下载、逐一查看18张原PNG；全部与固定版本PDF第5–13页的图9–26匹配，没有错误、损坏或必须移动的图片
- 确认一处缺图：第1–18段（00:00:00–00:10:20）讲8点星座、接收判决及16-QAM，原稿却从第20段后的图9开始配图；应补图8，即PDF第4页下半页
- 原图8已由主任务写入第01个二级标题后、原第1段前；图片复用上一段0910稿的原PNG，没有重新绘制或裁剪。已完成全量回读：19张图、7个一级标题、81个二级标题的位置正确，81个原正文块与18个原图块完全未变
- 最终本地Markdown包含19张图：18张原图顺序及相邻正文位置不变，新增图8明确标作补充课件
- 第26–29段临时跳到自由空间公式，图19/20已在第69–73段正式讲解处出现；不把临时前引误判为遗漏，也不额外插入重复图
- 图27起的详细衍射、反射等内容尚未在这段录音展开，第81段明确留到休息后；没有依据批量补后续PDF页

## 原稿完整性与边界

- 81个原正文块、原说话人标签、全部时间戳（含重复时间戳）及段内换行逐字保留；新增7个章节标题和81个逐段标题独立于正文
- 图8的源图确有8点圆形星座和16-QAM，但没有001/010点标签，也没有256-QAM图；这些为口头讲解，不应自行在课件上加绘
- 图11保留历史意大利5G频谱拍卖示例，不把金额当作当前新闻或价格
- 只核对课件身份与语义位置，不改写逐字稿中的技术表述、口误或转写细节
- 本审计工作仅执行远程读取；补图由主任务执行。私仓同步材料已准备，审计工作未发布仓库，也未修改原始文字记录或音频

## 图片对应表

|序号|图号|PDF页 / 半页|放置位置|内容|结论|
|---:|---:|---|---|---|---|
|1|8|4 / 下|第01个二级标题后、第1段前（补充）|Digital modulation: eight-point constellation and 16-QAM|匹配|
|2|9|5 / 上|第20段后 · 00:11:22|Analog modulation: antenna size, attenuation and capacity trade-offs|匹配|
|3|10|5 / 下|第40段后 · 00:22:52|Wireless System Capacity: frequencies, users and revenue|匹配|
|4|11|6 / 上|第43段后 · 00:22:52|Operators splash €6.5B in Italy 5G spectrum auction|匹配|
|5|12|6 / 下|第48段后 · 00:28:17|Wireless System Capacity: one base station|匹配|
|6|13|7 / 上|第49段后 · 00:28:50|Wireless System Capacity: three-base-station spatial reuse|匹配|
|7|14|7 / 下|第53段后 · 00:31:04|Wireless System Capacity: nine-base-station spatial reuse|匹配|
|8|15|8 / 上|第57段后 · 00:32:42|Radio Propagation|匹配|
|9|16|8 / 下|第59段后 · 00:33:59|Definitions: energy per bit, transmit power and noise density|匹配|
|10|17|9 / 上|第66段后 · 00:36:44|Power in dB|匹配|
|11|18|9 / 下|第68段后 · 00:37:31|dBm (absolute measurement power)|匹配|
|12|19|10 / 上|第69段后 · 00:38:27|Attenuation in the free space: received power and antenna gain|匹配|
|13|20|10 / 下|第73段后 · 00:40:28|Attenuation in the free space: distance and frequency|匹配|
|14|21|11 / 上|第73段后 · 00:40:28|Attenuation in the free space: summary|匹配|
|15|22|11 / 下|第74段后 · 00:40:28|Propagation in real world|匹配|
|16|23|12 / 上|第75段后 · 00:41:42|Attenuation due to the atmosphere|匹配|
|17|24|12 / 下|第76段后 · 00:41:42|Absorption by diffusion|匹配|
|18|25|13 / 上|第77段后 · 00:41:42|Refraction|匹配|
|19|26|13 / 下|第79段后 · 00:43:55|Diffraction: fixed and variable obstacles|匹配|

## 核验资料

- [飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/BaBFdm7AzoHPSYxulLwcWRgenBf)
- [001-BasicConcepts.pdf固定版本](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/001-BasicConcepts.pdf)
- slide-source-manifest.json：源文件版本/哈希、源页/半页、图片哈希、原块ID、原图注、相邻段落与语义范围
- bilingual-20261008-1000.md：全部原文、7个章节标题、81个逐段标题与19张图
- slide-images/：18张原稿PNG与补充图8的同源原PNG
- audit/existing-contact-1.png 至 existing-contact-3.png：18张原图视觉审阅联络表
- audit/basic-04.png 至 basic-14.png：固定PDF对应页、缺图源页及后续边界页
- receipts/add-slide-008.json：新增图8的写入回执

音频二进制未打包；Markdown保留原始录音播放链接。
