# 20261008-0910 课件图片审计

## 结论

- 已下载并逐一查看飞书原有12张PNG，与两份固定版本PDF对应页核对标题、版式、图示和编号；全部匹配，无损坏或错误图片
- 完整阅读46对原有双语段落，12张图均与相邻的连续讲解对应；未发现必须移动或补图的明确缺陷
- Introduction 图26–31对应都灵网状网络、Belding/GHTC和Campbell研究；BasicConcepts 图1、2、3、4、7、8对应章节过渡、调制链路、二进制调制及星座
- BasicConcepts PDF第3页的图5/6重复第2页的图3/4，现有图注已说明；不按数字缺口补重复图
- 本录音止于二进制与8点相位星座比较及休息安排，PDF图9开始的天线尺寸、衰减和容量权衡没有在本段展开；没有依据批量补后页
- 此审计仅远程读取；审计工作未写入飞书、源文字记录或音频，也未发布到GitHub或其他平台

## 上下文与限制

- 图26/27位于第1段后，图28/29位于第2段后，图30/31位于第3段后，都是同段同时覆盖人物、网站或场景的双图，原位置合理
- BasicConcepts 图3在第9段后，连续第10–11段继续讲频率与相位，图4在第12段后，连续讲解至第23段；不必把总览图挪到所有解释之后
- 图7在第25段后，紧接第26–28段的FSK、ASK、PSK说明；图8在第36段后，左下8点星座与后续3比特/8信号对应，右侧16-QAM虽未展开但属于该源页
- 图29显示2025 GHTC；第2段明确称“去年的”网页，并提到后续2026会议。保留旧课件忠实反映讲解，不能把此图当成当前活动时间表
- 所有原说话人标签、时间戳、重复时间戳、46对双语正文与段内换行在Markdown内逐字保留；不修订转写口误或独立验证人物传记叙述
- 私仓同步准备；未执行远程同步。相关内容只适用于用户已授权的私有目的，图片和讲稿的对外再发布许可未另行核验

## 图片对应表

|序号|源文件 / 图号|PDF页 / 半页|原图紧随段落|内容|结果|
|---:|---|---|---|---|---|
|1|01_Introduction_MSN_26-27.pdf / 26|13 / 下|1 · 00:00:00|Wireless Mesh: An example (Turin map)|匹配|
|2|01_Introduction_MSN_26-27.pdf / 27|14 / 上|1 · 00:00:00|Wireless Mesh: An Example (tram and mesh nodes)|匹配|
|3|01_Introduction_MSN_26-27.pdf / 28|14 / 下|2 · 00:00:00|Elizabeth M. Belding: mobile networks and social impact|匹配|
|4|01_Introduction_MSN_26-27.pdf / 29|15 / 上|2 · 00:00:00|IEEE GHTC 2025: technology for humanity|匹配|
|5|01_Introduction_MSN_26-27.pdf / 30|15 / 下|3 · 00:02:24|Andrew T. Campbell: mobile AI and health|匹配|
|6|01_Introduction_MSN_26-27.pdf / 31|16 / 上|3 · 00:02:24|Dartmouth: mobile sensing, intervention and AI|匹配|
|7|001-BasicConcepts.pdf / 1|1 / 上|5 · 00:03:39|Basic Concepts|匹配|
|8|001-BasicConcepts.pdf / 2|1 / 下|5 · 00:03:39|Wireless communications|匹配|
|9|001-BasicConcepts.pdf / 3|2 / 上|9 · 00:05:27|Modulation: amplitude, frequency and phase|匹配|
|10|001-BasicConcepts.pdf / 4|2 / 下|12 · 00:08:26|Modulation: transmitter and receiver chain|匹配|
|11|001-BasicConcepts.pdf / 7|4 / 上|25 · 00:14:56|Digital modulation: ASK, FSK and PSK|匹配|
|12|001-BasicConcepts.pdf / 8|4 / 下|36 · 00:20:48|Digital modulation: FSK and signal constellation|匹配|

## 核验资料

- [飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/R8JJdjfT2oKLnVxpZTTcSJO6nth)
- [01_Introduction_MSN_26-27.pdf固定版本](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/01_Introduction_MSN_26-27.pdf)
- [001-BasicConcepts.pdf固定版本](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/001-BasicConcepts.pdf)
- slide-source-manifest.json：原图块ID、原图注、源页/半页、相邻段落、连续语义范围、图片尺寸与SHA-256
- bilingual-20261008-0910.md：46对原段落、6个章节标题、46个逐段标题与12张原图
- slide-images/：飞书原PNG；未重新裁切或重绘
- audit/existing-contact-1.png、existing-contact-2.png：全部原图审阅联络表
- audit/intro-13.png 至 intro-16.png、basic-01.png 至 basic-05.png：固定版本PDF对应页及下一页渲染

音频二进制未打包；Markdown保留原始录音播放链接。
