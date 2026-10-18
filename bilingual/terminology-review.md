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

## 20261008-0800：导论与无线网络分类

本份保留121个原段落。开场包含中文和中英混合发言：纯中文段落的英文为译文，中文保留原话；主体英语授课部分英文来自清除标记后的修订正文。所有段落仍按原顺序一英一中排列。

| 英文 | 中文译法 | 本课语境与说明 |
|---|---|---|
| wireless network / wireless link | 无线网络／无线链路 | 网络与单条通信连接分别表达 |
| wireless host / mobile node | 无线主机／移动节点 | host强调承载应用；node强调网络中的节点 |
| coverage / range | 覆盖范围／覆盖距离 | 面积范围与距离按具体句子区分 |
| network architecture / topology | 网络架构／拓扑结构 | 功能组织与节点连接关系不同 |
| network edge / network core | 网络边缘／网络核心（核心网） | edge不一律等于某种特定无线接入网标准 |
| edge computing | 边缘计算 | 在靠近设备或网络边缘的计算资源上处理信息；英特尔官方中文材料采用此译法[5] |
| latency / throughput / data rate | 时延／吞吐量／数据速率 | 分别描述延迟、实际传送量与传输速率，不混用[5] |
| power / energy consumption | 功率消耗／能量消耗 | 功率对应单位时间的耗能，能量对应累计耗能 |
| ad hoc network | 自组织网络（ad hoc网络） | 本课强调无固定接入节点的直接通信；实际ad hoc网络也可多跳 |
| device-to-device communication | 设备到设备通信 | 首次可保留D2D缩写，描述直接通信 |
| nomadic mobility | 游牧式移动性 | 本课指移动到新地点后停留一段时间，再移动的模式 |
| handoff / handover | 切换 | 连接由一个服务基站／接入节点转移到另一个的过程；中文通信专利文本也将Handover Request称为切换请求[6] |
| satellite footprint | 卫星地面覆盖区（覆盖足迹） | footprint指地面覆盖，不是卫星实体尺寸 |
| roadside unit | 路侧单元 | 道路沿线的通信设备，不能简单把它等同于一根天线 |
| lidar / radar / UAV | 激光雷达／雷达／无人机 | 保留不同传感器类别；UAV cage按实验场景译为无人机笼式试验场 |
| Internet service provider | 互联网服务提供商 | 保留ISP缩写 |
| near-field communication | 近场通信 | 原修订稿为near communication field，中文按该语境对应NFC的通行概念表达；原英文不改写 |
| IEEE Fellow | IEEE会士 | 开场中文原话含Fellow，保留；“HV Fellow”及教授姓名/职务仍需专名事实复核 |

### 对原讲述的事实和概念说明

- 蓝牙、Wi-Fi和蜂窝网络的覆盖距离是课堂数量级示例，不是设备统一上限。实际距离与发射功率、天线、PHY、环境等相关，蓝牙官方文档也明确说明范围取决于条件[7]。
- 本课的mesh例子是无线网状网络的一种实现。mesh不局限于Wi-Fi，蓝牙同样有mesh网络规范[8]。
- “Wi-Fi适合游牧、蜂窝适合高速移动”是课程比较框架，不表示Wi-Fi不支持切换或漫游。
- 卫星移动性除了覆盖足迹，还与轨道、波束及切换策略有关；原讲述的大覆盖解释不是所有卫星系统的完整结论。
- 课程中的80%/60%统计、6G时间判断及mesh起源故事均按修订稿翻译，本页未独立证实其统计口径或历史事实。
- 开场人名、职务、混合语言和票务对话存在原修订稿已记录的不确定之处。特别是“82年”、HV Fellow及第27个源段落的英文保留语义不清。双语稿保留内容，不据语境创造一个确定的身份或事件；这些问题仍可在原修订稿和diff追溯。

[5] 英特尔官方中文，融合5G与边缘计算：https://www.intel.cn/content/www/cn/zh/cloud-computing/integrating-5g-accelerate-transformation.html

[6] CN113261340B原始专利文本（切换术语）：https://patentimages.storage.googleapis.com/32/e2/e1/01b9b91d43cca0/CN113261340B.pdf

[7] Bluetooth SIG，蓝牙信道探测：https://www.bluetooth.com/zh-cn/learn-about-bluetooth/feature-enhancements/channel-sounding/

[8] Bluetooth SIG，蓝牙网状网络入门指南：https://www.bluetooth.com/zh-cn/bluetooth-mesh-networking-primer/

## 20261008-1000：调制、传播与空间复用

| 英文 | 采用译法 | 区分与依据 |
|---|---|---|
| Gaussian noise | 高斯噪声 | 指概率分布模型，不等于所有干扰；MathWorks AWGN文档[9] |
| noise power density | 噪声功率谱密度 | 本课N0的语境是每单位带宽功率，区别于空间中的功率密度；单边／双边定义须随公式一致[9] |
| QAM | 正交幅度调制 | MathWorks中文标题使用“正交调幅”；本稿采用常用完整译名，缩写相同[2] |
| free-space path loss | 自由空间路径损耗 | MathWorks给出20 log10(4πR/λ)的dB形式[10] |
| attenuation | 衰减 | 本课以发射功率／接收功率的线性比表示，注意不要将线性比与dB数值混算 |
| wavelength | 波长 | λ=c/f，区别于信号持续时间[10] |
| antenna gain / isotropic antenna | 天线增益／各向同性天线 | 三维各向同性辐射覆盖4π球面立体角[11] |
| directional antenna | 定向天线 | 不译为“方向天线”；强调辐射方向图 |
| spatial reuse | 空间复用 | 此课具体指不同小区在空间上重复使用相同频谱，不等同于MIMO空间复用流 |
| densification | 网络密集化 | 指节点部署及通信距离的变化，不是数据压缩 |
| licensed spectrum | 授权频谱 | 指使用权许可，不把许可表达为对频谱本身的永久所有权 |
| bit duration / symbol duration | 比特持续时间／符号持续时间 | 与对应速率的倒数关系一致 |
| energy per bit | 每比特能量 | 在本课条件下Eb=P×Tb=P/Rb |
| dB / dBm | 分贝／相对于1毫瓦的功率单位 | dB表达比值；dBm以1 mW为参考表示功率 |

### 原讲述中的科学核对

1. 原文“48 dB of power”没有给出参考功率，不能作为完整的绝对发射功率值。正文保留48 dB，不能自行补成48 dBm或48 dBW。
2. 原文把各向同性天线辐射范围说成2π。二维方位角可取2π，但三维各向同性辐射对应4π sr，增益为1（0 dBi）；全向天线在一个平面内均匀也不等于三维各向同性[11]。
3. 自由空间损耗随f²变化的比较需要保持距离和天线增益等条件一致；若固定的是物理孔径，增益也会随频率改变，不能笼统推出所有高频链路一定更差[10]。
4. “避免覆盖区重叠”是课堂理想化的频谱复用例子。实际蜂窝覆盖可以重叠，关键在于同频干扰、频率规划、功率和调度，而不是把任何覆盖重叠都视为不可用。
5. “地球曲率使信号不沿直线传播”混合了地平线遮挡与射线弯曲两件事。地球曲率会限制视距；大气折射才会使传播路径偏折，不能把两者直接等同。
6. “20 GHz附近水蒸气吸收”是粗略表述。代表性水汽谱线约为22.235 GHz，具体链路影响与距离、湿度等有关，并非任何20 GHz附近频率都无法通信[12]。
7. 16-QAM每符号4比特、256-QAM每符号8比特符合k=log2(M)的映射关系；实际净信息速率还会受编码率和协议开销影响[2][9]。

[9] MathWorks，AWGN信道：https://ww2.mathworks.cn/help/comm/ug/awgn-channel.html

[10] MathWorks，fspl：https://www.mathworks.com/help/phased/ref/fspl.html

[11] MathWorks，Element and Array Radiation and Response Patterns：https://www.mathworks.com/help/phased/ug/element-and-array-radiation-patterns-and-responses.html

[12] EUMETSAT，MW/sub-mm Spectroscopy Literature Review（水汽谱线）：https://www-cdn.eumetsat.int/files/2024-03/Task1_report_submm_literature_review_pdf.pdf
