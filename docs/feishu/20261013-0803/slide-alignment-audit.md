# 20261013-0803 逐图只读审计

## 结论

完整69段与16张原图核验：16图均与实际讲述相符，保持原顺序，无确切漏掉的PDF页。2项课堂原始绘图/改注来源缺口保留说明；未远端修改。特别注意第82张之后PDF页外打印序号偏移1，本报告使用半页实际顺序，不机械按打印序号改图注。

## 逐图证据

### 图75：EDCA Bursting with Block ACK
- 原图块：doxcnyyYaKAb8iyExYgNyRZ9S1i
- 位置：第1段后、第2段前
- 固定PDF：第38页上半页
- 结论：保留。1段明确发送方最后控制包请求确认，接收方SIFS后Block Ack；图75的BlockAckReq→SIFS→BlockAck与该对话精确对应。
- 原图：../slide-images/slide-075.png

### 图76：Block ACK: How it works
- 原图块：doxcnySaEQ3OFfoeXp7fJZPgTjg
- 位置：第2段后、第3段前
- 固定PDF：第38页下半页
- 结论：保留。第2段逐bit解释bitmap的1/0成功失败，图76第三条一比特对应一个已发帧，紧跟该段准确。
- 原图：../slide-images/slide-076.png

### 图77：EDCA Bursting: Pros and Cons
- 原图块：doxcn2KvStLElqz7XPUT3RxEkUf
- 位置：第3段后、第4段前
- 固定PDF：第39页上半页
- 结论：保留。第3段解释少发ACK降低开销、提高效率，并明确提到delay jitter但不展开；图77左右优缺点正对应。
- 原图：../slide-images/slide-077.png

### 图79：Temporal Fairness vs. Per-Packet Fairness（双时间线与公式）
- 原图块：doxcnFU0u10LLUopJ10oczJWWvd
- 位置：第18段后、第19段前
- 固定PDF：第40页上半页
- 结论：保留。7–13段建立饱和A/B及n×L/T；14–22段转相同AC的相同TXOP和n×TXOP×R/T。18段明确用矩形简化TXOP并比较两条timeline，图79的上下时间线和公式一致，因此18段后准确。34–46段是课间回来回看此图与改符号，不另复制或移走原图。
- 原图：../slide-images/slide-079.png

### 图78：Temporal Fairness vs. Per-Packet Fairness（文字公式）
- 原图块：doxcnIL4rSxN3EyHmKuvvFg2jSf
- 位置：第22段后、第23段前
- 固定PDF：第39页下半页
- 结论：保留。第22段得出相同R才有相同吞吐量并总结temporal fairness，图78的L相等与R相等两公式总结正对应；图79先于78符合讲图后总结的授课顺序。
- 原图：../slide-images/slide-078.png

### 图82：The 802.11e Superframe
- 原图块：doxcnCDn4UhyiDqziPryonJECIl
- 位置：第24段后、第25段前
- 固定PDF：第41页下半页
- 结论：保留。24段明确通过graphical representation讲beacon起始CFP，再25段CP、轮询；28–32段指TXOP及CP内CF-Poll。图82含beacon/CFP/CP/CF-End和两种TXOP，放24段后是整套机制的图示入口。
- 原图：../slide-images/slide-082.png

### 图80：HCCA: Crucial Features
- 原图块：doxcnGb3Und59kPiOlHAmdvQE5g
- 位置：第25段后、第26段前
- 固定PDF：第40页下半页
- 结论：保留。第25段引入HCCA并解释仍由AP polling，图80强调HC控制与QoS CF-Poll，放25段后准确；其中8TC是图中文字，未强行声称课堂逐项讲过。
- 原图：../slide-images/slide-080.png

### 图84：Polling and Scheduling in HCCA
- 原图块：doxcntEo7QWLPZblFnfhl8D4ytg
- 位置：第26段后、第27段前
- 固定PDF：第42页下半页
- 结论：保留。26段专门解释QoS Control报告队列数量、AP实时了解谁有流量，图84第二条正是queue size/desired TXOP经QoS Control报告，与轮询决策相接。
- 原图：../slide-images/slide-084.png

### 图81：HC and QSTA Behavior in HCCA
- 原图块：doxcnvbPKnc1ZgFJiZQ1ymUVIpf
- 位置：第31段后、第32段前
- 固定PDF：第41页上半页
- 结论：保留。31段明确CP中AP等PIFS后也可发poll，恢复紧急流量；图81上部PIFS/CP/CAP与下部QSTA使用指定TXOP对应，31段后准确。
- 原图：../slide-images/slide-081.png

### 图85：Did HCCA Actually Fix PCF's Problems?
- 原图块：doxcnqy4heP5Nlfc1zvJPnr4uc4
- 位置：第31段后、第32段前
- 固定PDF：第43页上半页
- 结论：保留。26–29段解静态列表和未知时长问题；30段承认beacon仍可延迟，31–32段解释CP内poll/PIFS补救。图85的CAP作为结构性修复及队列信息更充分直接总结这些内容，保持31段后。
- 原图：../slide-images/slide-085.png

### 图83：Traffic Signaling
- 原图块：doxcngG1ZHJBZen1jZqWN4DWpf9
- 位置：第48段后、第49段前
- 固定PDF：第42页上半页
- 结论：保留。47段直接引出traffic signaling；48段区分QoS Control报告和显式握手协商吞吐量/时延/丢包要求，49段解释接纳控制；图83两类信令与TSPEC协商吻合。
- 原图：../slide-images/slide-083.png

### 图86：Wi-Fi 4 (802.11n) — PHY/MAC Enhancements
- 原图块：doxcnuYvrqtkPcCbCwrlbDSJRAf
- 位置：第50段后、第51段前
- 固定PDF：第43页下半页
- 结论：保留。50段最后明确转入802.11n，51段区分主要PHY增强与少量MAC变化，章节页在50段后准确。
- 原图：../slide-images/slide-086.png

### 图90：Beamforming
- 原图块：doxcnkCORWrWwu6FyGEaYTZUHkh
- 位置：第54段后、第55段前
- 固定PDF：第45页下半页
- 结论：保留。52–54段用喊话类比、AP与A/B方向解释集中功率，提高接收功率；55段谈从802.11n到后续版本改进；图90定义及隐式/显式演进对应，放54段后恰当，不能按序搬到89后。
- 原图：../slide-images/slide-090.png

### 图87：802.11n Physical Layer: Overview
- 原图块：doxcnSYZ46oIvzTFV30iVgC7SVg
- 位置：第58段后、第59段前
- 固定PDF：第44页上半页
- 结论：保留。52–55段OFDM/MIMO/beamforming概述后，56–58段讨论20MHz聚合40MHz；图87各项与该段落群一致，尤其58段直接对channel bonding，保留58段后。
- 原图：../slide-images/slide-087.png

### 图88：802.11n: Data Rates
- 原图块：doxcn6RxXlg3d6BUu9KGHtaCpsc
- 位置：第60段后、第61段前
- 固定PDF：第44页下半页
- 结论：保留。59段16/64QAM、60段coding rates与MCS、61段2x2/3x3/4x4MIMO，图88含对应调制/编码/空间流，60段后合理。
- 原图：../slide-images/slide-088.png

### 图89：802.11n Example Data Rates
- 原图块：doxcnGAbt4VVx2Xm6RTw2e6jWUb
- 位置：第62段后、第63段前
- 固定PDF：第45页上半页
- 结论：保留。62段明确指summary of possible bit rates并读6.5至600Mb/s，图89两行表正含这些端值；65–66段继续比较11/600/46G，位置准确。
- 原图：../slide-images/slide-089.png

## 确切缺图

## 原课件未找到的课堂图

{
  "id": "fairness-classroom-topology-and-symbol-annotations",
  "title": "饱和A/B连接AP的具体课堂拓扑与课间后的符号改注",
  "paragraph_spans": [
    [
      7,
      8
    ],
    [
      34,
      46
    ]
  ],
  "evidence": "7段明确说AP here、A/B及满队列；34段明确回到slide并现场更改大小写符号、逐处书写。固定图79保留原两时间线公式，但没有AP拓扑，也不包含这次现场改注的可靠记录。",
  "status": "unresolved_classroom_visual_source_not_found",
  "action": "保留原图79和原文不确定标注；不能根据口述臆造改符号后的图。"
}

{
  "id": "beamforming-a-b-ap-classroom-drawing",
  "title": "AP/A/B全向与定向辐射图",
  "paragraph_spans": [
    [
      52,
      55
    ]
  ],
  "evidence": "53段指A与AP的辐射pattern、omnidirectional antenna、AP改向B；固定图90是文字定义，没有这张A/B/AP辐射图。固定PDF相关beamforming页与后续ac/ax页无同一具体课堂图。",
  "status": "unresolved_classroom_visual_source_not_found",
  "action": "保留图90文字定义，不将后续MU-MIMO示意冒充课堂A/B/AP图。"
}

## 不机械补图

{
  "figure_numbers": [
    91,
    92
  ],
  "reason": "第63段明确跳过不重要PHY细节，课堂尚未展开PPDU compatibility或MAC aggregation；不能按后续页码补。"
}

{
  "figure_numbers": [
    3,
    13,
    14
  ],
  "reason": "第52/56–57/65段是对早前Wi-Fi总表、频段、信道图的口头回顾；本课87–89已有当下PHY概览/速率，未确认再次展示旧图，不机械复插。"
}

## 发布及修改建议

16张原图和69段可独立发布审计检查点，无远端改动需求；保留2项课堂图来源待确认及未做原音认证说明。

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf
PDF SHA256：15011ccc6e929fd6f0b9fb7837ee450734a12058891fa028e6e1bf658c4902e8
