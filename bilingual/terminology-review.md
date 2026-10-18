# 双语课程稿术语核对

核对日期：2026-10-18。当前覆盖：20261008-0910，共46组英中段落。后续课程逐份补充。

## 采用的译法与依据

| 英文 | 本稿采用译法 | 语境与核对依据 |
|---|---|---|
| mesh network | 网状网络 | 保留无线多节点互连语义；华为官方技术文章使用“网状Mesh组网”[1] |
| access point | 接入点 | 无线接入设备；同一华为文章使用“接入点”[1] |
| radio interface | 无线接口 | 本课涵盖Wi-Fi、蜂窝通信及蓝牙接口，不限于单个射频器件 |
| base station | 基站 | 本课手机连接的蜂窝网络接入设备；不译为“基地” |
| modulation / demodulation | 调制／解调 | 区分把信息映射到信号与从信号恢复信息的操作[2][3] |
| amplitude / frequency / phase | 幅度／频率／相位 | 信号的三个不同参数，不把phase译为“阶段”[2][3] |
| bit / bit string | 比特／比特串 | 与调制符号区分，0与1是比特的可能取值[2] |
| symbol | 符号（首次加“也叫码元”） | 在本课调制映射中，一个调制符号对应一组比特；MathWorks中文文档采用“每符号比特数”[2] |
| binary modulation | 二进制调制 | 对应两种可选调制符号，每符号携带一比特；不是所有数字调制都只包含两种信号 |
| bit rate | 比特率 | 单位时间内传送的比特数，不能混同符号率；固定符号率下，M=2^k时每符号携带k比特[2] |
| signal constellation | 信号星座 | 一组可选信号点；本课“the set of signals ... is called constellation”采用此译法[4] |
| constellation diagram | 星座图 | 信号星座的图形表示；MathWorks中文文档明确使用“绘制QAM星座图”[2] |
| constellation size | 星座点数 | 指可选信号点数量，不指画面尺寸；涉及large constellations时表达为“星座点数更多的调制方案”[2][4] |
| baseband | 基带 | 与搬移到载波附近的信号区分[3] |
| carrier / carrier frequency | 载波／载波频率 | 载波是信号；载波频率是其频率，不能把整个频段与载波严格等同[3] |
| frequency spectrum | 频谱 | 讲述某一技术使用的频率范围时，中文采用“频段”或“频谱区域”[3] |
| upconversion / downconversion | 上变频／下变频 | 将基带信号搬移到载波附近，以及接收端搬回基带的过程[3] |

## 原讲述的概念边界与保留事项

1. 原讲述把频谱搬移阶段称为“analog modulation”。双语正文按原文译为“模拟调制”，不暗改英文。就所描述的具体操作，更精确的术语是上变频；接收端对应下变频。两者在此处不能作为所有场合下的同义词。
2. 原讲述用“carrier”指信号所处的中心频率。概念上应区分载波、载波频率和工作频段；正文保留讲述的表达，读者可依据本页区分。
3. “一个信号携带三个比特，速度变为三倍”的比较以符号持续时间／符号率不变为前提。本页补足这一条件，不向逐段译文添加原文未说出的推导。
4. 本课用“一组比特”介绍symbol。严格说，调制符号是调制信号集合中的元素，输入比特组映射到该符号；不能在所有通信语境中把symbol简单定义成比特序列。
5. 原文的01→10自我纠正和最后休息时间的矛盾保留。去掉时间戳、说话人标签及校订编号仅改变阅读格式，不构成对原修订稿中不确定内容的再次确认。相关记录仍在原修订稿及独立diff中。
6. 教授姓名、会议创办沿革及人物经历属于专名和事实核查范围，本次术语核对没有将其独立验证。双语稿表达的是课程修订文本的内容。

## 核对来源

[1] 华为，《Wi-Fi 6是电信运营商的新武器》：https://www.huawei.com/cn/huaweitech/publication/84/wifi-6-new-growth-point-operators

[2] MathWorks，qammod中文文档（调制阶数、每符号比特数、QAM星座图）：https://ww2.mathworks.cn/help/comm/ref/qammod.html

[3] 清华大学王继良《物联网前沿实践》，6.5载波上变频：https://iot-book.github.io/6_%E6%95%B0%E5%AD%97%E8%B0%83%E5%88%B6%E4%B8%8E%E8%A7%A3%E8%B0%83/S5_%E5%9F%BA%E5%B8%A6%E4%BF%A1%E5%8F%B7%E5%92%8C%E8%BD%BD%E6%B3%A2%E4%B8%8A%E5%8F%98%E9%A2%91/

[4] MathWorks，Scatter Plots and Constellation Diagrams：https://www.mathworks.com/help/comm/ug/scatter-plots-and-constellation-diagrams.html

此表中的语境判断依据本课修订正文。来源明确支持的术语与对原讲述的解释分别列出；后续核对遇到新的语境时继续补充。
