# 20261012-1620 逐图只读审计

## 结论

完整审阅51段和13张原图，13张均应保留现有位置。确认的图60已从固定PDF忠实栅格化并补到第2段标题后、正文前，最终14图。完整回读和远端图像SHA256核验通过；全部原正文、13原图和导航不变。PCF现场A/C轮询时序原图仍未找到。

## 逐图证据

### 图61：DCF vs. PCF: the Bottom Line
- 原图块：doxcneuEvb3naEgRCNq7JKBREVL
- 位置：第6段后、第7段前
- 固定PDF：第31页上半页
- 结论：保留。第6段明确说This is a slide that highlights the differences between DCF and PCF，图61正是DCF/PCF两栏比较；第2–5段收束PCF问题，7–8段转入改进版，位置准确。
- 原图：../slide-images/slide-061.png

### 图62：Wi-Fi 4 (802.11e) — Quality of Service
- 原图块：doxcnFjE7Hp8akgjVx8AuqDcGug
- 位置：第9段后、第10段前
- 固定PDF：第31页下半页
- 结论：保留。第9段明确进入new chapter；第10–12段引入QoS、HCF、EDCA/HCCA。章节页在第9段后准确。
- 原图：../slide-images/slide-062.png

### 图63：Why Wi-Fi 4? Two Amendments, One Brand
- 原图块：doxcn0ZK29zGiIEYYeuiQALzJEg
- 位置：第10段后、第11段前
- 固定PDF：第32页上半页
- 结论：保留。第10段指first slide并讲应用从文件传输转向低时延、高吞吐；第11段具体说voice/video/video calls，正对应图63应用需求部分。正文沿用原文，不额外校订其Wi-Fi名称表述。
- 原图：../slide-images/slide-063.png

### 图64：The Hybrid Coordination Function (HCF)
- 原图块：doxcnhHyn4jUEV3GjOqLxnju1jh
- 位置：第12段后、第13段前
- 固定PDF：第32页下半页
- 结论：保留。第12段逐个解释HCF包含分布式EDCA与集中式HCCA，图64定义相同，紧跟12段准确。
- 原图：../slide-images/slide-064.png

### 图65：Some Definitions
- 原图块：doxcnX3hJDzU1DGjNYpjOqKyGfg
- 位置：第16段后、第17段前
- 固定PDF：第33页上半页
- 结论：保留。第13段解释QBSS/QSTA/HC，14段指last point，15–17段定义TXOP及TXOP limit；图65末项正是TXOP，放16段后完整覆盖这组定义。
- 原图：../slide-images/slide-065.png

### 图74：EDCA Bursting
- 原图块：doxcnqXDqC9g5Qidfnmq6L3cxCc
- 位置：第16段后、第17段前
- 固定PDF：第37页下半页
- 结论：保留。第16–17段明确一次接入可在时间上限内发一个、两个、三个分组；图74前两条正是多帧burst和TXOP_Limit。图中SIFS和Block ACK细节留到下节，51段明确预告acknowledgments明天讲，但不因此移动与当前多包概念直接相关的原图。
- 原图：../slide-images/slide-074.png

### 图66：EDCA: Crucial Features
- 原图块：doxcnKs3uoEwfSRGlxBoFkROOle
- 位置：第20段后、第21段前
- 固定PDF：第33页下半页
- 结论：保留。第18–20段引入增强DCF并从一队列改为四队列/虚拟站点，后续31–42段解释各AC参数不同。图66列四AC及独立CSMA/CA，20段后正确。
- 原图：../slide-images/slide-066.png

### 图73：Virtual Stations and Internal (Virtual) Collisions（队列结构图）
- 原图块：doxcnKFkz3uMpfAXURqP4OclNed
- 位置：第20段后、第21段前
- 固定PDF：第37页上半页
- 结论：保留。图实际左侧为legacy单队列+server、右侧为AC0–3四队列及AIFS/CW/TX，与19–20段画queue/server再扩展四虚拟站点逐项一致。虽然标题含virtual collisions，本课并未展开内碰撞；不因标题或页码把该结构图移走。
- 原图：../slide-images/slide-073.png

### 图68：Traffic Differentiation: How Priority Is Enforced
- 原图块：doxcnc0Cmt8pBliDO0o5AfRlEKf
- 位置：第34段后、第35段前
- 固定PDF：第34页下半页
- 结论：保留。第32–34段从相同规则转向参数差异，34段定义AIFS并开始CWmin，后续35–42段讲CW和TXOP limit；图68三参数概览放34段后合适。QoS字段由47–50段补充。
- 原图：../slide-images/slide-068.png

### 图67：The Four Access Categories
- 原图块：doxcngqb6H1B4LdeaISFmv3P3cb
- 位置：第43段后、第44段前
- 固定PDF：第34页上半页
- 结论：保留。第43段明确说Here you have the access categories并按图读VO、VI、BE、background；图67四行表正对应，因此保持43段后而非按67<68提前。
- 原图：../slide-images/slide-067.png

### 图69：Traffic Differentiation: How Priority Is Enforced（AIFS时间图）
- 原图块：doxcnQaE1LCqxxxKSytSwgM27vf
- 位置：第44段后、第45段前
- 固定PDF：第35页上半页
- 结论：保留。第44段明确说graphical representation regarding arbitration IFS，只画AC0/1/2；还读取DIFS 34µs、slot 9µs。图69恰有三个AIFS和底部数值，位置精准。
- 原图：../slide-images/slide-069.png

### 图70：Backoff and CW
- 原图块：doxcnnhDHiNh6GtKnHUGwI8jFfh
- 位置：第45段后、第46段前
- 固定PDF：第35页下半页
- 结论：保留。44段末转到backoff/CW图，45段解释CW更新式及较小CWmin统计上更快，46段补RTS/CTS；图70有更新公式和RTS/CTS时间线，45段后正确。
- 原图：../slide-images/slide-070.png

### 图71：MAC Header with QoS Control Field
- 原图块：doxcnt01ZEobX5XQm9VbbpZNiTf
- 位置：第48段后、第49段前
- 固定PDF：第36页上半页
- 结论：保留。47段开始MAC header，48段逐项点Duration、四地址、CRC和新增QoS Control字段，49–50段讲队列信息；图71框架及高亮QoS字段直接对应48段。
- 原图：../slide-images/slide-071.png

## 确切缺图

{
  "figure_number": 60,
  "title": "Why PCF Never Really Happened",
  "pdf_page": 30,
  "pdf_half": "lower",
  "paragraph_spans": [
    [
      2,
      5
    ]
  ],
  "status": "confirmed_relevant_slide_absent_from_this_document",
  "evidence": "第2段01:12正式续讲PCF第三问题，明确说被轮询用户持续多久取决于payload和速率；第3段以A/C占用多久提问；第4–5段解释无法预知时长便无法控制delay。这正对应图60的Unknown transmission duration/variable frame sizes make scheduling difficult，而本课13图不含60。第6段之后才是61的DCF/PCF比较。",
  "placement": "在第2段H2后、原第2段正文前；不移动任何原图",
  "prepared_image_source": "/workspace/shared/course-1012-1530/slide-images/slide-060.png",
  "provenance": "该PNG是上一课授权Feishu原图，已逐张对照固定PDF第30页下半页确认；可复用忠实原图，或从固定PDF重新栅格化。",
  "not_based_on_page_gap": "判断来自第2–5段连续机制讲解，不是因为61之前缺60。"
}

## 原课件未找到的课堂图

{
  "id": "pcf-a-c-polling-continuation",
  "title": "A/C各发送多久的PCF课堂轮询时间线",
  "paragraph_spans": [
    [
      2,
      4
    ]
  ],
  "status": "unresolved_classroom_visual_source_not_found",
  "evidence": "第3段具体询问A与C各占信道多久，承接上一课现场画的A/C/D轮询图；固定PDF的图58仅宏观CFP/CP，图60为文字总结，没有该详细时序。",
  "action": "补图60可覆盖机制总结，但不能声称恢复现场原图；沿用上一课的源图待确认说明。"
}

## 不机械补图

{
  "figure_number": 72,
  "reason": "本课只解释四虚拟队列和参数差异，没有说明同一站内部两个计数器同时归零、高优先级胜出、低优先级翻倍CW，故不能仅凭队列关键词补内碰撞文字页。"
}

{
  "figure_numbers": [
    75,
    76,
    77
  ],
  "reason": "第51段明确把acknowledgments留到明天，本课未讲Block ACK请求/bitmap/延迟确认；不能因74已有便续插75–77。"
}

## 发布及修改建议

本审计和13原图可备份；图60建议由父任务复核后插入。缺图未补前，不把本课标成所有PPT已补齐。

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf
PDF SHA256：15011ccc6e929fd6f0b9fb7837ee450734a12058891fa028e6e1bf658c4902e8


## 最终写入核验

- 新图块：doxcnmf3Se0kTYE1lRPBJAzZERd
- 位置：第2段H2之后、正文之前，精确相邻关系已回读核验
- 51段原正文、13张原图、51个H2、8个H1及其他原非根块（状态行除外）逐块完全不变
- 状态行更新至14图
- 上传前后图60 SHA256：2dcb275c27e3f09fe2115e1645d6e8e6ac2d21c475ff2f4af1fb1583354873f7
- 详细证明：remote-verification.json
- 以上补图已完成；本报告前面的缺图记录保留为发现时证据，manifest中已标resolved_and_verified
