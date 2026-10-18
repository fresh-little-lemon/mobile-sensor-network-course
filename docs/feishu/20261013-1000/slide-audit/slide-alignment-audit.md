# 20261013-1000 逐图只读审计

## 结论

完整64段与5张原图核验：原5图均保留。确认第16–18段回看的Wi-Fi4速率表（图89）在本课缺失。33:14后已切换另一份数值练习课件，两个具体题目和解答图在当前唯一固定PDF中没有，不能用通用DCF图代替。未远端修改。

## 逐图证据

### 图52：Worked Example: Why 11 Mb/s Never Feels Like 11 Mb/s
- 原图块：doxcnj6U7QKxO2RsTe3uAizr8Jb
- 位置：第3段后、第4段前
- 固定PDF：第26页下半页
- 结论：保留。第3段直接读此标题，4–15段逐项解释frame time、192µs、11Mb/s、1500B、DIFS/backoff/SIFS/ACK，图52数值框与公式一致，紧跟第3段正确。原文某些ACK速率表述与课件存在出入，不在本次改正文范围。
- 原图：../slide-images/slide-052.png

### 图92：MAC Enhancements in 802.11n
- 原图块：doxcn2wnl1PqdG03yatYA7unheb
- 位置：第21段后、第22段前
- 固定PDF：第46页下半页
- 结论：保留。21段正式引入amendment通过aggregation解决效率下降；图92首条列A-MSDU/A-MPDU，作为增强概览置于21段后合适。其余RIFS/reverse direction并未展开，不续插相关页。
- 原图：../slide-images/slide-092.png

### 图94：A-MSDU: Aggregating at the MSDU Level
- 原图块：doxcnrL34xwf4FqK1I4KSkyj9Sy
- 位置：第21段后、第22段前
- 固定PDF：第47页下半页
- 结论：保留。21段详细说多个higher-layer payload依次拼接成一个MAC payload、只加一个MAC header；图94 MSDU1…N进入同一MPDU Header/FCS正对应，21段后精准。
- 原图：../slide-images/slide-094.png

### 图95：A-MPDU: Aggregating at the MPDU Level
- 原图块：doxcnVjx6AmxsWpzj0Tu82zTtce
- 位置：第22段后、第23段前
- 固定PDF：第48页上半页
- 结论：保留。22段说明多个MAC packet再次拼接只加一个PHY header/preamble；图95的MPDU1…N、共享PHY Header结构吻合。
- 原图：../slide-images/slide-095.png

### 图96：Two-Level Aggregation
- 原图块：doxcnPT83J8p94dWxTQBccKWmUe
- 位置：第22段后、第23段前
- 固定PDF：第48页下半页
- 结论：保留。22段明确总结two stages，第一层payload聚合+一个MAC头、第二层MAC packet聚合+一个PHY头；图96上下两级箭头即该过程，22段后与95并列恰当。
- 原图：../slide-images/slide-096.png

## 确切缺图

{
  "figure_number": 89,
  "title": "802.11n Example Data Rates",
  "pdf_page": 45,
  "pdf_half": "upper",
  "printed_pdf_slide_label": 90,
  "paragraph_spans": [
    [
      16,
      18
    ]
  ],
  "status": "confirmed_relevant_slide_absent_from_this_document",
  "evidence": "第16段20:03明确切回Wi-Fi4说here we are，读最高600和最低6.5；17–18段继续拿6.5/600比较packet不同部分的发送速率。固定图89的两行rate表恰好包含6.5和600这两个端点，该课现有5图完全没有这张表。不是仅凭出现Wi-Fi4关键词补入。",
  "placement": "第16段H2后、原第16段正文前",
  "prepared_image_source": "/workspace/shared/course-1013-0803/slide-images/slide-089.png",
  "provenance": "上一课授权Feishu原图与固定PDF第45页上半页已视觉核验；可从固定PDF原样栅格化。"
}

## 原课件未找到的课堂图

{
  "id": "numerical-problem-1-separate-deck",
  "title": "数值题1题目、AP/A/B/C拓扑与完整解答时序",
  "paragraph_spans": [
    [
      24,
      37
    ],
    [
      40,
      46
    ]
  ],
  "status": "separate_teaching_deck_not_in_authorized_fixed_source",
  "evidence": "第23段明确exit this slide deck and go to our numerical problems；25段说暂不发该课件避免看solution。题1：A/B时长1ms、C1.5ms，A/B同时发碰撞、backoff10/11、C在1.25ms到包、A于3.1ms重发；40段明确展示full solution。这是另一个独立课件，不是主PDF图54/EIFS示意。",
  "search_scope": "本课资源块与inventory只链接02-WiFi_1-7.pdf；该74页主PDF的完整文本及图页不含这两个具体题目，23段还明确说明换课件。",
  "action": "记录练习课件来源待提供/定位；不按不完整口述猜参数或重绘解答。"
}

{
  "id": "numerical-problem-2-separate-deck",
  "title": "数值题2题目与不等时长碰撞/EIFS解答时序",
  "paragraph_spans": [
    [
      47,
      51
    ],
    [
      54,
      64
    ]
  ],
  "status": "separate_teaching_deck_not_in_authorized_fixed_source",
  "evidence": "题2 A/C1ms、B1.4ms、TF150µs，C在忙期间到包；54段开始solution，A早停后听B尾部需EIFS，B常规DIFS。给定B backoff在61/63段有13/30不确定，不可凭推理替代原题。",
  "action": "需同一练习课件原图；保留所有不确定标注，不把题2当题1或通用图54。"
}

{
  "id": "packet-basic-rate-classroom-annotation",
  "title": "原包结构上标注1/11与6.5/600Mb/s的课堂示意",
  "paragraph_spans": [
    [
      5,
      18
    ]
  ],
  "status": "unresolved_classroom_visual_source_not_found",
  "evidence": "5段this is a packet，16段let us write here basic rate；18段指同一packet分别填写PHY与MAC/payload速率。图52有文字计算，图89有rate表，但未找到这次课堂对包结构的手写标注图。",
  "action": "保留52并补89作为原课件；不制作未经核实的手写恢复图。"
}

## 不机械补图

{
  "figure_number": 93,
  "title": "Why Aggregation? The Preamble-Overhead Problem",
  "status": "relevant_source_slide_but_display_not_confirmed",
  "reason": "19–21段确实讲高速payload缩短而固定开销仍在，但课件93具体300Mb/s、40µs案例未出现，已有图52和94–96覆盖开销计算及聚合结构。可作为相关阅读，不能仅因92与94之间少93就认定漏页。"
}

{
  "figure_numbers": [
    53,
    54,
    55
  ],
  "reason": "练习解答虽用EIFS，但其AP/A/B/C、具体毫秒时刻与题目变量不等于主PDF的B→C/A侦听示意；不以通用图代替缺失练习图。"
}

{
  "figure_numbers": [
    91,
    97,
    98
  ],
  "reason": "本课未展开PPDU formats、link adaptation或Wi-Fi5章节，23段明确结束主PDF并转练习，不补后续页。"
}

## 发布及修改建议

可先备份只读审计，图89由父任务核准后补；练习题源图未定位前应明确保留来源缺口，不能声称本课所有课件齐全。

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf
PDF SHA256：15011ccc6e929fd6f0b9fb7837ee450734a12058891fa028e6e1bf658c4902e8


## 最终写入核验（取代前述待补状态）

图89已补到第16段H2后、正文前。最终6图、64个H2、9个H1。全部原非根块除状态行外完全不变；新增图片远端下载SHA256与本地一致：d39525deed9f47eecfd12da345aab8a8849cf7793d003274407e69a4da4507d5。

完整证明：remote-verification.json。发现时缺图条目保留为审计轨迹，manifest状态已改为resolved_and_verified。原音与原transcript/minutes均不变。
