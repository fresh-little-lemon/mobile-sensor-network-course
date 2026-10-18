# 20261016-0805 逐图审计与补图核验

## 最终结果

原22张图全部保留，已在P66/P72标题后分别补WiFi图36/45，最终24图、87段正文、87个H2与10个H1；所有原块除文首图数22→24之外完全不变，新增两图远端下载字节hash一致。当前已确认PDF缺图0项，4项课堂原图/批注来源缺口仍保留。

## 写入前审计结论（历史）

87段讲解、22张原图逐张视觉核验完成：原图全部语义对齐，0需移动；明确缺2张WiFi回指页（图36/P66、图45/P72），仅建议这两处补图。保留slotted/unslotted先外层再变量、先failure再timing的课堂顺序；EIFS两种碰撞例子未在固定PDF找到，不能用通用图54代替。

## 逐图证据

### 04-Sensors-MAC.pdf 图31：Operating Frequency Bands
- 原图块：doxcn6DXmfeTJtCTDGeOrUkWj3d
- 位置：第1段后、第2段前
- 固定PDF：第16页 upper
- 结论：保留。P1逐项比较868/915MHz窄带与2.4GHz宽带、频宽和速率，原图三组频带及1MHz/5MHz视觉结构相符。
- 原图：../slide-images/slide-031.png

### 04-Sensors-MAC.pdf 图32：PHY Layer
- 原图块：doxcnrRytRP2AeBq1GaxioYBn3c
- 位置：第2段后、第3段前
- 固定PDF：第16页 lower
- 结论：保留。P2指这张调制页不用背、转看PHY包长；P3明确6B头和127B最大payload，与页底粗体一致。
- 原图：../slide-images/slide-032.png

### 04-Sensors-MAC.pdf 图33：MAC LAYER
- 原图块：doxcnFQbwLAof6wdCuhRlE8h0Kd
- 位置：第4段后、第5段前
- 固定PDF：第17页 upper
- 结论：保留。P4明确Now let us move to the MAC layer，标题页放在此过渡段后正确。
- 原图：../slide-images/slide-033.png

### 04-Sensors-MAC.pdf 图34：MAC Layer: beacon-enabled mode
- 原图块：doxcn7dl0c5pj7dQ64Dp9JwqDYf
- 位置：第5段后、第6段前
- 固定PDF：第17页 lower
- 结论：保留。P5协调器定期beacon，P6超帧时间参考，P7明确beacon-enabled，正是三项概览。
- 原图：../slide-images/slide-034.png

### 04-Sensors-MAC.pdf 图35：Optional Superframe Structure
- 原图块：doxcnwCdIfXBPZRoN1JiDDanBbg
- 位置：第8段后、第9段前
- 固定PDF：第18页 upper
- 结论：保留。P7引出picture，P8按beacon间隔、先CAP再CFP讲解；P9时隙，P10 CFP按TDMA分配，图中顺序和颜色分区均相符。
- 原图：../slide-images/slide-035.png

### 04-Sensors-MAC.pdf 图36：Energy Saving: whole-network idle
- 原图块：doxcny2m5YkQW4qbsmh5pIh7ICc
- 位置：第10段后、第11段前
- 固定PDF：第18页 lower
- 结论：保留。P10后半明确as represented here全网包括coordinator可休眠，对应超帧后Idle白区；与同段CFP说明衔接合理。
- 原图：../slide-images/slide-036.png

### 04-Sensors-MAC.pdf 图37：Energy Saving: individual nodes
- 原图块：doxcnapgARX8rJCHcmvjedGWZmc
- 位置：第11段后、第12段前
- 固定PDF：第19页 upper
- 结论：保留。P10末单节点睡眠、P11缓存/存储压力与丢包，正对应本页individual LP、data storage、delay，不移至全网休眠图前。
- 原图：../slide-images/slide-037.png

### 04-Sensors-MAC.pdf 图38：Slotted CSMA-CA overview
- 原图块：doxcnZk3LJHzeZcKmvdbb6OySCb
- 位置：第11段后、第12段前
- 固定PDF：第19页 lower
- 结论：保留。P11后半明确focus contention-based interval/slotted CSMA-CA，P12同步但分布式，P15进入内外块。与本页CAP/对齐/两模块一一相符。
- 原图：../slide-images/slide-038.png

### 04-Sensors-MAC.pdf 图40：Slotted CSMA-CA Procedure: Outer Block
- 原图块：doxcnn7WojpX2n9YjmwS85QMUMd
- 位置：第15段后、第16段前
- 固定PDF：第20页 lower
- 结论：保留。P15先讲外层NF=0，P16把inner当黑盒并逐步讲Transmit/ACK，P17重试、P18直接failure。图40先于图39是实际讲解次序，必须保留。
- 原图：../slide-images/slide-040.png

### 04-Sensors-MAC.pdf 图39：Slotted CSMA-CA Algorithm: Variables
- 原图块：doxcnOukWzwQiYYq3uXsNWEAEvb
- 位置：第20段后、第21段前
- 固定PDF：第20页 upper
- 结论：保留。P20进入inner时才细讲NB/CW，P21 BE；变量表在这里与内层流程图41并列正合适，不因PDF顺序排回40之前。
- 原图：../slide-images/slide-039.png

### 04-Sensors-MAC.pdf 图41：Slotted CSMA-CA Procedure: Inner Block
- 原图块：doxcnB69ewCxW2WCuxHbCdH3yfc
- 位置：第20段后、第21段前
- 固定PDF：第21页 upper
- 结论：保留。P19说show diagram，P20初始化NB0/CW2，P22–26定位边界→随机退避→CCA→双slot感知/重置，P27超限failure，原流程箭头吻合。
- 原图：../slide-images/slide-041.png

### 04-Sensors-MAC.pdf 图42：Slotted CSMA-CA Algorithm: Inner Block summary
- 原图块：doxcntYgoDJJ0hh9Gp8y1IAwQkc
- 位置：第27段后、第28段前
- 固定PDF：第21页 lower
- 结论：保留。P27明确to summarize，先退避后感知、busy重试，与本页文字小结相符；P28回顾外层不要求把此图换为其他图。
- 原图：../slide-images/slide-042.png

### 04-Sensors-MAC.pdf 图44：Remarks: Failure Handling
- 原图块：doxcnW6o6KqEfYF1pTUpatiLfXb
- 位置：第30段后、第31段前
- 固定PDF：第22页 lower
- 结论：保留。P29区分两类失败，P30重进inner NB reset0是本页末行粗体精确内容。老师先讲此页再讲SIFS，因此44→43正确。
- 原图：../slide-images/slide-044.png

### 04-Sensors-MAC.pdf 图43：Remarks: Backoff and Timings
- 原图块：doxcn5lcG01XaYdEr18w4lKo8oj
- 位置：第38段后、第39段前
- 固定PDF：第22页 upper
- 结论：保留。P33–39讲sensor/sink时序，P38–39强调DATA-SIFS-ACK-SIFS才能再次接收，对应本页第二bullet；原图位于P38后恰承接关键第二个SIFS。
- 原图：../slide-images/slide-043.png

### 04-Sensors-MAC.pdf 图45：No Beacon-enabled Mode
- 原图块：doxcnjcvtAeqJO7TaNfDXAe13vb
- 位置：第40段后、第41段前
- 固定PDF：第23页 upper
- 结论：保留。休息后P40明确no beacon/no superframe/unslotted，当前转场匹配本页。
- 原图：../slide-images/slide-045.png

### 04-Sensors-MAC.pdf 图47：Unslotted CSMA-CA: Outer Block
- 原图块：doxcnymeJWberrIdmR98JPc8rsg
- 位置：第40段后、第41段前
- 固定PDF：第24页 upper
- 结论：保留。P40在同段后半逐步重讲NF0、inner两种输出、ACK和重传，P41两种失败，对应外层图；先47后46是实际先外层后内层顺序。
- 原图：../slide-images/slide-047.png

### 04-Sensors-MAC.pdf 图52：Remarks: Failure Handling (unslotted)
- 原图块：doxcnYV5Thn1MQexzoGiPF371B9
- 位置：第41段后、第42段前
- 固定PDF：第26页 lower
- 结论：保留。P40末引出two causes，P41整段区分inner负结果和最大重传，图52恰作失败小结，不应机械移到全章最后。
- 原图：../slide-images/slide-052.png

### 04-Sensors-MAC.pdf 图46：Unslotted CSMA-CA Algorithm: Variables
- 原图块：doxcn9k9OWVJXWvzFsGgwFRYwPK
- 位置：第42段后、第43段前
- 固定PDF：第23页 lower
- 结论：保留。P42初始化内层变量、P43随机退避，变量页没有CW，紧挨无slot边界内层图48正确。
- 原图：../slide-images/slide-046.png

### 04-Sensors-MAC.pdf 图48：Unslotted CSMA-CA: Inner Block flow
- 原图块：doxcnBlBxuARx4Ob2y1YkVMJ6Gd
- 位置：第42段后、第43段前
- 固定PDF：第24页 lower
- 结论：保留。P42明确fewer blocks/arrows、无需slot对齐，P43持续倒数后CCA，P44空闲发送或busy重试/超限，精确对应此图。
- 原图：../slide-images/slide-048.png

### 04-Sensors-MAC.pdf 图49：Unslotted CSMA-CA: Inner Block summary
- 原图块：doxcnkQi4FqKgUGVbAkf8VYniVf
- 位置：第44段后、第45段前
- 固定PDF：第25页 upper
- 结论：保留。P43–44连续退避/感知/忙时再退避以及ACK经SIFS，与文字小结一致。
- 原图：../slide-images/slide-049.png

### 04-Sensors-MAC.pdf 图50：Remarks: same observations
- 原图块：doxcnyPLIxjEj3Ql2cEmZrXESpb
- 位置：第44段后、第45段前
- 固定PDF：第25页 lower
- 结论：保留。P44强调also in this case/as before，回指相同backoff/timing/failure，是本页唯一bullet，放在无时隙小结内合理。
- 原图：../slide-images/slide-050.png

### 04-Sensors-MAC.pdf 图51：Remarks: Backoff and Timings (unslotted)
- 原图块：doxcnWiwUxvlT24Z0IuG8tjcChd
- 位置：第44段后、第45段前
- 固定PDF：第26页 upper
- 结论：保留。P44后半和P45再次强调ACK后的SIFS转换期不得接收；本页明列packet1-SIFS-ACK-SIFS-packet2，与图49/50同段保留。
- 原图：../slide-images/slide-051.png

## 确切缺图

{
  "source_pdf": "02-WiFi_1-7.pdf",
  "figure_number": 36,
  "pdf_page": 18,
  "pdf_half": "lower",
  "title": "DCF Basic Access: Unicast DATA + ACK",
  "semantic_paragraphs": [
    66,
    68
  ],
  "paragraph_ordinal": 66,
  "insert_after_heading2_block_id": "doxcnaYknFIjdLGzhNXN9cg0eP0",
  "before_body_block_id": "doxcnR4WaXTAk1trcGsRaF2uxAh",
  "evidence": "P66明确回到最初overview time diagram，P67按Source DATA、Destination SIFS ACK、others读Duration设NAV逐行说明；固定WiFi图36恰是该三行时序，而此课后半一张WiFi图都没有。角色A/AP/B的课堂命名不在源页，不能冒充恢复命名拓扑。",
  "status": "confirmed_missing_source_found",
  "receipt_stem": "wifi036"
}

{
  "source_pdf": "02-WiFi_1-7.pdf",
  "figure_number": 45,
  "pdf_page": 23,
  "pdf_half": "upper",
  "title": "When Does a Station (Re)contend? — the Backoff Cases",
  "semantic_paragraphs": [
    72,
    72
  ],
  "paragraph_ordinal": 72,
  "insert_after_heading2_block_id": "doxcnxOPQa9n0tEUKCBK6bkWP0e",
  "before_body_block_id": "doxcnS4u9sgspPGuzpo1AZOcsSf",
  "evidence": "P72明确说backoff在three possible situations使用，go back to the slide/read the slide；固定WiFi图45正好列且仅列三个触发情形，为明确页回指，不靠关键词补图。",
  "status": "confirmed_missing_source_found",
  "receipt_stem": "wifi045"
}

## 原课件未找到的课堂图

{
  "kind": "classroom_drawing_not_in_fixed_pdf",
  "paragraphs": [
    33,
    39,
    44,
    45
  ],
  "description": "sensor与sink两行DATA-SIFS-ACK-SIFS及192微秒收发转换课堂时序。Sensors图43/51只有文字规则，没有现场两行绘图；不据规则自行重画当原图。"
}

{
  "kind": "classroom_annotation_not_in_fixed_pdf",
  "paragraphs": [
    66,
    67
  ],
  "description": "A、B、AP互相可听的命名拓扑/时序批注；WiFi图36可恢复通用Source/Destination/Others原页，但不含课堂A/B/AP拓扑及手写标注。"
}

{
  "kind": "classroom_drawing_not_in_fixed_pdf",
  "paragraphs": [
    74,
    79
  ],
  "description": "A/B同起发送，C和AP碰撞后NAV=0而PHY忙，随后D插入使C提前结束EIFS的多节点课堂图。固定WiFi图54仅B→C数据与A错误接收，不是此例。"
}

{
  "kind": "classroom_drawing_not_in_fixed_pdf",
  "paragraphs": [
    80,
    82
  ],
  "description": "A短包、B长包同起碰撞，A收完自身短包后只听到B尾部而需EIFS的课堂图。所供固定PDF未含该双包长图，不能替以通用EIFS页。"
}

## 不机械补图

{
  "source_pdf": "04-Sensors-MAC.pdf",
  "figures": [
    29,
    30
  ],
  "reason": "本录音从频带图31续讲；29/30不因页码前缺就补。"
}

{
  "source_pdf": "04-Sensors-MAC.pdf",
  "sequence": [
    40,
    39,
    41,
    44,
    43,
    45,
    47,
    52,
    46,
    48,
    49,
    50,
    51
  ],
  "reason": "先外层后内层变量、先failure后timing、unslotted回顾失败后再进入inner，全部跟实际段落走，不按PDF重排。"
}

{
  "source_pdf": "02-WiFi_1-7.pdf",
  "figures": [
    35,
    38,
    41,
    46,
    53,
    54,
    55
  ],
  "reason": "答疑提到相关概念不自动证明逐页展示；其中54与实际碰撞例不符。除36/45明确回指外不扩大补图。"
}

{
  "kind": "review_question_list",
  "paragraphs": [
    47,
    50,
    62,
    72,
    84,
    87
  ],
  "reason": "学生收集问题被读出，未证明是PPT原图；不虚称可恢复的固定课件页。"
}

## 发布及修改建议

根任务已核准仅在P66/P72 H2后各补固定WiFi图36/45，22原图、87段正文和导航音频全部保留；最终24图。

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/04-Sensors-MAC.pdf
PDF SHA256：ea5f2788f3180267cc079e54cde419563b5529a46a72cd2ec3a3e5f69742b647

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf
PDF SHA256：15011ccc6e929fd6f0b9fb7837ee450734a12058891fa028e6e1bf658c4902e8


## 最终写入核验（取代前述待补状态）

已按prepared-additions列明锚点在相应H2后、正文前补图，最终24图、87个H2、10个H1。全部原非根块除文首图数字段外完全不变，所有原图保留；新增图片远端下载SHA256与本地一致。

完整证明：remote-verification.json；原缺图条目保留审计轨迹，manifest状态已改为resolved_and_verified。
