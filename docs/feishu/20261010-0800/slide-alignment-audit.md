# 20261010-0800 课件图片与导航审计

## 结论

- 81对双语正文及81个H2、7个H1已完整审阅：现有标题的编号、时间戳、中文主题与正文吻合，无须重建导航
- 12张原PNG逐张与固定PDF第13–20页视觉核验一致；原图均与附近讲述相关，未移动、重绘或重排
- 补入图34《The Four Interframe Spaces》：第43–58段已讲SIFS/DIFS、优先级和同一对话中的DATA→ACK；图位于第58段原标题之后、原文之前
- 图34直接从固定PDF第17页下半页高分辨率渲染，未改写内容。新增后远端重下载的SHA256与本地源PNG一致
- 完整回读核验通过：81H2、7H1、13图。全部原正文、原导航和原12图块逐块不变；仅文首状态统计更新、增加1个图块

## 仍待确认的课堂图来源

这些是文字中指向的课堂说明图，尚不能确认为固定PDF中的遗漏页，也可能来自板书或补充材料。

- MAC队列与服务台模型示意：第7段末说用这种方式建模，第8段明确MAC抽象为queue and server，并反复指这里是cashier、这里是queue；第10–12段讲FIFO和排队分析。 保留原文，记录原图来源待确认；可能是板书或补充材料，不用后续EDCA图替代。
- 功率随时间、侦听区间与能量门限示意：第18段明确说在这里表示天线随时间感知的功率，并标注sensing time；第19–20段解释能量门限与busy/idle。 保留原文，不将图38或Wi-Fi6后部的能量/门限页当作该曲线，不自行重绘。
- A/B两节点高低优先级竞争的具体时间线：第47–50段设A持高优先级包、B持低优先级包，A等待SIFS后占信道、B在DIFS后半段侦听到busy，并指向这个时刻与这最后一段。 保留原文及相关图33/34，不用后续QoS图片替代，不声称已恢复独立课堂示意。

已检索固定74页PDF全文，并视觉核查正文对应页及第3、23、25、34–37页的候选。后续EDCA队列、AIFS/CW图不是本次基础排队模型或A/B例图，未用作替代。因此不能把13张图解读为所有课堂视觉资料均已恢复。

## 补图边界与原顺序

- 图34的SIFS/DIFS和对话优先级已展开；PIFS/EIFS具体用途在第44、58段明确推迟。原课件整页保留，不声称所有条目本节都讲完
- 不补图29：本节没有讲non-persistent/p-persistent等持久策略
- 不补图35：EIFS错误后等待和指数退避尚未展开，基础DATA/ACK由图36/37覆盖
- 图39在图38和37之前正确：先定义NAV，随后讲双重侦听，再用步骤页总结；不按PDF编号重排
- 图36在第71段后是完整示例讲完后的归纳，保留原位置
- 图40位于末段后有明确预告依据；第81段说隐藏节点场景在休息后继续，不补图41起RTS/CTS页

## 保留说明

- 中英文正文、说话人、时间戳、重复时间戳、段内换行逐字保留
- 第39–40段课间插话、第70段混合语言及转写异常均未修正。该审计不承担音频核对或技术纠错
- 原PNG中的字体、版式和源PDF已有的小标题重叠均保留原字节；补图34忠实保留PDF内容
- 原始文字记录、智能纪要、录音未修改；音频仅保留播放链接，不打包二进制

## 图片对应表

|图号|固定PDF位置|正文位置|内容|核验结论|
|---:|---|---|---|---|
|26|第13页下半页|第1/2段间|The MAC Layer: DCF and PCF|匹配第1–2段|
|27|第14页上半页|第24/25段间|MAC Layer: Role and Functions|匹配第3–7,13–20,24–26段|
|28|第14页下半页|第24/25段间|Why Not Reuse Ethernet's CSMA/CD?|匹配第21–26段|
|30|第15页下半页|第28/29段间|Three MAC Frame Types|匹配第27–29段|
|31|第16页上半页|第33/34段间|Two Coordination Functions|匹配第1–2,30–33段|
|32|第16页下半页|第35/36段间|Time Slot|匹配第34–38,41–43段|
|33|第17页上半页|第45/46段间|Interframe Spaces (IFS): a Priority Ladder|匹配第43–54段|
|34|第17页下半页|第58段标题后、正文前（新增）|The Four Interframe Spaces|匹配第43–58段|
|36|第18页下半页|第71/72段间|DCF Basic Access: Unicast DATA + ACK|匹配第55–71,79–80段|
|39|第20页上半页|第71/72段间|Network Allocation Vector (NAV)|匹配第69–77段|
|38|第19页下半页|第77/78段间|Carrier Sensing: Physical and Virtual|匹配第17–20,74–78段|
|37|第19页上半页|第78/79段间|Unicast Transmission Procedure|匹配第55–58,64–80段|
|40|第20页下半页|末段81之后|The Hidden-Terminal Problem|匹配第81段|

## 核验文件

- [飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/FfgDdqktToKXpyxwlCxcv7GanSb)
- [固定版本PDF](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf)
- bilingual-20261010-0800.md：完整81对双语段落、原88个标题、13张原课件图
- slide-source-manifest.json：逐图来源、哈希、页/半页、块ID、图注、相邻段落和语义依据
- audit/verification.json：原文、顺序、标题、原块、原图位置和新增图远端字节核验
- audit/missing-slide-034.json 与 audit/render_slide_034.py：补图来源、裁剪范围、完整依据和可复现渲染
- audit/compare-page-13.png 至 compare-page-20.png：12张原图与固定PDF的逐页视觉比对
- blocks-before.json、blocks-final.json、receipts/：修改前后全量快照与父任务写入回执

已执行修改均核验通过；3项课堂说明图来源仍待确认。
