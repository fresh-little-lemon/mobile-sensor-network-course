# 20261014-0801 逐图只读审计

## 结论

62段全文语义核验，2张原图分别来自考试说明和D2D课件，均定位正确，0张需移动、0张已提供PDF中的确切缺图。课堂主要讲独立数值习题及手绘时序；原题/解答讲义不在已提供课件清单，不能用通用EIFS或DCF页替代。考试评分口述与PDF有差异，保留原正文并显式提示。

## 逐图证据

### Exam_Information.pdf 图1：Information about the final exam
- 原图块：doxcneAmxHOPVHTYeGhuAa0kd0e
- 位置：第1段后、第2段前
- 固定PDF：第1页 whole
- 结论：保留。原图为完整考试说明页；P1说明闭卷、笔/橡皮/计算器，P2补充最终答案用笔，P3讨论各题分值，P4明确关闭考试slides，放P1后直接覆盖本话题。注意PDF两道数值题各30、两道开放题各20，P3口述看似将开放题也说成30；这是源信息差异，不能据PDF改正文。
- 原图：../slide-images/slide-Exam_Information-001.png

### 03-D2D-Networks.pdf 图1：Wireless D2D Networks
- 原图块：doxcnclDSJvHyPjOO3QZUWbYMXe
- 位置：第61段后、第62段前
- 固定PDF：第1页 upper
- 结论：保留。P60明确切到已发的下一套slides并准备休息后课程；P61首次报Device-to-device communication networks，P62预告设备直接互通与基础设施Wi-Fi差异。标题页在P61后准确承接新课件开场，没有将概念页猜插进习题部分。
- 原图：../slide-images/slide-03-D2D-Networks-001.png

## 确切缺图

## 原课件未找到的课堂图

{
  "kind": "unprovided_numerical_problem_deck",
  "paragraphs": [
    5,
    14
  ],
  "description": "回看前一课第2道题：全互听AP/A/B/C、A/B包长不同、A19/B30/C5、C先发与NAV冻结的原题/解答时序图。提供的02-WiFi课件没有此完整题与数值时序。"
}

{
  "kind": "unprovided_numerical_problem_deck",
  "paragraphs": [
    15,
    33
  ],
  "description": "第3题：A/B隐藏、A/C0.2ms与B0.4ms、B两包、A0.65ms到达、C到达0.35/0.55ms未定、A/C退避7、求B后退避14至17的原题与解答图未提供。"
}

{
  "kind": "classroom_whiteboard_not_in_pdf",
  "paragraphs": [
    37,
    50
  ],
  "description": "P37明确重新画拓扑、P38只重画B首包成功后的局部时序；解释13+n、SIFS/ACK、n=0或5失败、n1至4可行的实际手绘图。与原题解答相关但属于现场追加图，不能拿一般DCF图或猜绘补。"
}

{
  "kind": "unprovided_numerical_problem_deck",
  "paragraphs": [
    52,
    59
  ],
  "description": "第4题原题截图及开头提示图：A/B隐藏，A/C0.3ms、B0.4ms，B在t0发/A在t0+0.1发，C0.7ms到达，A/C退避1/5，C读B首部设置含期望ACK的NAV，求B最多一次碰撞。老师让学生拍照并次日讲解，当前源文件没有。"
}

## 不机械补图

{
  "source": "03-D2D-Networks.pdf",
  "figure_numbers": [
    2,
    3,
    4
  ],
  "reason": "最后3段只为休息后新课开场，未讲Outline条目或具体示意图；不能因提到D2D就把后续整套概念图提前插入。"
}

{
  "source": "02-WiFi_1-7.pdf",
  "reason": "数值题讲EIFS、NAV、后退避不等于再次展示通用机制课件；没有所讲相同拓扑/数值，不能替换缺失习题页。"
}

## 发布及修改建议

2张原图及现有导航正文保留，独立slide-audit检查点可发布。4项课堂图来源缺口需原习题/板书资料才能恢复，不做推测补图。

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/Exam_Information.pdf
PDF SHA256：901a9e6927af00b8a450a8c9f759e6485735bc9bcfbc31449fea9a4f342d7d11

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/03-D2D-Networks.pdf
PDF SHA256：32577de32b488a6078b341071f97818b5b4bbd884936f241b47cbfaaf7e50424

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf
PDF SHA256：15011ccc6e929fd6f0b9fb7837ee450734a12058891fa028e6e1bf658c4902e8
