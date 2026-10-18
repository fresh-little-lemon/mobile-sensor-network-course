# 双语课程稿术语核对

核对日期：2026-10-18。当前覆盖：按录音顺序的前8份课程，共669组双语段落。后续课程逐份补充。

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

## 20261008-1049：多径、信噪比和差错控制

| 英文 | 中文译法 | 核对与使用范围 |
|---|---|---|
| diffraction / reflection / scattering | 衍射／反射／散射 | 三种传播机制分开使用，不能都用“反射”替代 |
| constructive / destructive interference | 相长干涉／相消干涉 | 本段指同一信号不同路径的相干叠加，与其他发射机造成的干扰区分 |
| multipath fading | 多径衰落 | 不同传播路径的信号叠加导致接收幅相变化 |
| slow / fast fading | 慢衰落／快衰落 | 相对于符号、传输或应用时间尺度描述信道变化；MathWorks慢衰落示例以连续符号共享系数为假设[13] |
| shadowing | 阴影衰落 | 遮挡引起的大尺度功率变化，与快慢变化分类不完全等价 |
| SNR / SINR | 信噪比／信干噪比 | SNR=S/N；SINR=S/(I+N)，这里S、I、N均为同带宽内的线性功率 |
| intra-/inter-technology interference | 同技术内／跨技术干扰 | 注意不是intra/inter-cell的同小区／小区间干扰 |
| error detection / correction | 检错／纠错 | 发现错误不等于恢复正确内容 |
| forward error correction (FEC) | 前向纠错 | 发送冗余使接收端可在一定条件下纠错[14] |
| information / redundant bits | 信息比特／冗余比特 | k个信息比特编码为n比特码字，码率k/n[14] |
| code rate | 码率 | 此处是无量纲比值k/n，不是单位bit/s的比特率 |
| repetition code / majority rule | 重复码／多数判决 | 按各次接收结果的多数决定比特 |
| parity bit | 奇偶校验位 | 本例使总的1的数量为偶数，因此具体为偶校验 |
| convolutional code | 卷积码 | 不是“卷积神经网络”；编码器带有寄存器状态 |
| ARQ | 自动重传请求 | 通行英文展开为Automatic Repeat reQuest；原讲述的automatic retransmission request保留于英文原稿[15] |
| packet / header / payload | 数据包（分组）／首部／有效载荷 | 正文统一优先用数据包；header用“首部”，payload用“有效载荷” |

### 原讲述中的科学核对

- 衍射不能严格定义为“碰撞障碍物后复制出多个信号”。边缘绕射、反射、散射均可能形成不同传播分量；水滴粒子引起的传播影响也不能一概归为衍射。
- 两个分量只有在相反相位且幅度相等时才能完全抵消；反相本身不足以推出接收功率为零。
- 静止环境也可能存在很深的衰落。“慢衰落也叫shadowing”是本课的简化，快慢描述变化速度，阴影描述遮挡机制，两组概念不严格同义。快衰落也并非绝对无法补偿，可结合信道估计、分集、均衡和编码等处理。
- SNR与SINR公式必须使用线性功率相加，不能直接相加以dBm表示的干扰和噪声。
- 冗余位增多并不单独保证任意编码都更强，还需看码结构、最小距离、信道和译码方式。单校验位可检出奇数个位翻转，但可能漏掉偶数个位翻转，校验通过不证明内容一定正确。
- 本课二维行列校验的单比特定位依赖所述单错模型；多个错误可能产生不同检错或漏检情形，不扩展成任意多错纠正。
- 包首部字段随协议而异。课堂中的寄信类比有助入门，但并非每层每个包都同时含有源地址和目的地址；有效载荷也可能是上一层完整的包。

[13] MathWorks，berfading：https://www.mathworks.com/help/comm/ref/berfading.html

[14] MathWorks，Block Codes：https://www.mathworks.com/help/comm/ug/block-codes.html

[15] MathWorks，SDA Optical Communication Terminal Waveform Generation：https://www.mathworks.com/help/satcom/ug/sda-oct-waveform-generation.html

## 20261009-0759：停等ARQ与Wi-Fi协议栈

| 英文 | 中文译法 | 核对与语境 |
|---|---|---|
| CRC | 循环冗余校验；字段值称CRC校验值 | 属于差错检测，不能将其与密码学摘要等同 |
| digest | 摘要 | 本课用作CRC的直观类比，不代表抗碰撞的密码学哈希 |
| stop-and-wait ARQ | 停等式ARQ | 发一包后等待确认，超时可触发重传；ARQ与确认机制见RFC 3366[16] |
| acknowledgment / ACK | 确认／确认包 | 区别于用户有效载荷；不译为“承认”[16] |
| timeout / retransmission | 超时／重传 | “未收到ACK”可由数据包丢失或ACK丢失引起，不单独证明对方未收到数据[16] |
| PHY / MAC | 物理层／介质访问控制层 | IEEE 802.11规范范围为MAC与PHY[17] |
| protocol stack | 协议栈 | 各层处理及其相互接口，不能等同于某个单一硬件 |
| WLAN | 无线局域网 | IEEE 802.11工作组与规范的正式领域[17] |
| transport / network / application layer | 传输层／网络层／应用层 | 本课分别以TCP、IP和应用为例 |
| ICT | 信息与通信技术 | 指知识及专业领域，不是某一种无线技术 |

### 对照稿保留与科学校核

- 原文19:18附近把等待ACK、超时后重传的一方说成receiver。按本课停等流程，这些动作属于transmitter。英文及中文保留原修订稿角色措辞，纠正说明集中放在本文件，不悄悄修改原讲述。
- 原文“接收端不发ACK隐式请求接收端重传”的末尾角色也应按流程理解为发送端重传。
- CRC相等只表示校验没有检出错误，不能保证绝对无错；实际CRC字段的位置和覆盖范围由具体协议定义，并非总在首部，也并非总只覆盖有效载荷。
- “首部始终正确接收”是本课明确采用的简化假设，不能推广到真实信道。
- Wi-Fi是技术与认证生态的名称，IEEE 802.11是底层标准系列。IEEE官方资料确认其含MAC和PHY规范，不把两个名称当作组织意义上的完全同义词[17]。
- 原修订稿开场混合文本“签签到”及部分不清楚句子没有可靠重识别依据，译稿保留；逐字母列出的标准后缀边界也未强行合并成确定版本。

[16] RFC Editor，RFC 3366，Advice to Link Designers on Link Automatic Repeat reQuest：https://www.rfc-editor.org/info/rfc3366/

[17] IEEE 802.11工作组，About IEEE 802.11：https://www.ieee802.org/11/abt80211.html

## 20261009-0845：协议层、共享介质与Wi-Fi演进

| 英文 | 中文译法 | 核对与说明 |
|---|---|---|
| router / gateway | 路由器／网关 | 区分具体设备转发功能与连接不同网络的出入口角色 |
| LLC | 逻辑链路控制 | Logical Link Control，与MAC共同涉及数据链路层功能 |
| shared medium / collision | 共享介质／碰撞 | 此处讨论同时发送造成的重叠，不是设备物理撞击 |
| unlicensed spectrum | 免许可频谱 | 不需要逐个用户申请专用频谱许可，不等于没有功率、频段或地域规定 |
| OFDM | 正交频分复用 | 正式展开Orthogonal Frequency Division Multiplexing；原文“orthogonal frequency the gram modulation”有误，中文按已核实术语翻译[18] |
| MIMO / multi-user MIMO | 多输入多输出／多用户MIMO | MIMO与OFDM分别涉及空间维度和子载波组织，可结合使用[19] |
| channel / band | 信道／频段 | 频段是更大频谱范围，信道是按规定划分的可操作频率区间 |
| PHY data rate | 物理层数据速率 | 与应用吞吐量、单终端实际速度区分 |

### 原讲述中的概念校核

- “The antenna travels through the air”中的主体应是signal，而非antenna。对照稿英文保留原修订稿，该句中文也保留“天线”以便追溯，正确物理过程见本说明。
- 多人说话例子的分母包含其他发言者的功率，应使用SINR而非仅SNR。原文随后自行提到SINR，对照保留其展开过程。
- “物理层以外全是软件”是教学简化。MAC功能也可能由硬件或固件实现；路由器转发亦可由专用芯片完成，协议层不决定唯一实现形式。
- 本节停等确认说明针对基本单播流程，不覆盖所有Wi-Fi帧种类、组播、聚合与块确认机制。
- 2.4 GHz“三个信道”应结合不重叠信道及信道宽度理解；5 GHz“12个”、6 GHz“24个”不是全球通用常数。可用数量取决于监管域和信道宽度。例如Cisco的FCC-USA 1200 MHz示意给出59个20 MHz信道[20]。
- 46 Gbit/s属于特定多空间流、带宽、调制等配置下的理论PHY量级，不能当作任意手机网卡实际吞吐量。由1–2 Mbit/s到46 Gbit/s约为2.3万至4.6万倍，不只是精确的1000倍。
- 原修订稿中的“Muy”“我们的”“笑”等短片段未有足够依据重新辨识，保留在相应位置；这不是新增课堂内容。

[18] MathWorks，Introduction to OFDM：https://www.mathworks.com/help/comm/gs/introduction-to-ofdm.html

[19] MathWorks，Wireless Communications（MIMO与OFDM）：https://www.mathworks.com/help/phased/mimo-communication.html

[20] Cisco Live 2024，BRKEWN-3004：https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2024/pdf/BRKEWN-3004.pdf

## 20261009-1000：接入流程、吞吐量、OFDM与MIMO

| 英文 | 中文译法 | 核对与说明 |
|---|---|---|
| throughput / physical-layer data rate | 吞吐量／物理层数据速率 | 前者计入观察时间中的等待与失败，后者描述发射时速率；计算时还要说明统计哪一层的比特 |
| BSS / ESS / DS | 基本服务集／扩展服务集／分布式系统 | DS也常译分布系统；统一本稿译法，基础设施BSS与自组织IBSS区分 |
| station / access point | 站点／接入点 | STA为站点；AP承担接入点角色，不能将所有STA都等同终端用户 |
| scanning / authentication / association | 扫描／认证／关联 | 三种过程，不把关联译为登录；实际安全建立顺序取决于配置[21][22] |
| beacon / probe request / probe response | 信标／探测请求／探测响应 | 主动探测的应答不是简单地“立即发一个信标”[21] |
| association request / response | 关联请求／关联响应 | frame译帧；packet作为一般分组概念，不能认为各层严格相同 |
| basic rate set | 基本速率集 | 一组要求支持的速率，不是唯一的“最低数据速率” |
| rate adaptation | 速率自适应 | 依据链路质量或传输结果等选择速率，不只改变调制，还可能涉及编码等配置 |
| half-/full-duplex | 半双工／全双工 | 描述是否能同时双向通信，不由器件名字或收发器数量单独决定 |
| transceiver | 收发器 | 能承担发送和接收功能的电路／设备 |
| subcarrier / orthogonality | 子载波／正交性 | 正交性是接收积分／内积条件，不是“频谱重叠少”[18] |
| spatial stream / MIMO channel rank | 空间流／MIMO信道秩 | 可分离流数受信道秩及信噪比等约束，不是直接等于天线数[23] |

### 必须区分的课堂简化与实际机制

1. “Wi-Fi认证已被应用层用户名密码替代”不成立。网页门户登录、802.1X/EAP、WPA2/WPA3的安全建立是不同层面的机制。WPA3-SAE仍有明确的无线认证过程[22]。本稿保留原讲述并在这里指出区别。
2. 主动扫描通常使用Probe Request与Probe Response；有指定SSID的请求也可能采用广播目的MAC地址，不能把“指定网络名”直接等同于链路层单播[21]。现代设备的扫描隐私策略也因系统与版本而异，不把课堂缓存示例当作所有设备固定行为。
3. 网络列表名称通常涉及SSID，BSSID用于识别具体BSS；手机信号图标不必直接由SNR生成，不能把RSSI、接收功率和SNR视为同一量。
4. ESS可通过DS连接，DS实现不必总是有线。漫游也不必每次从头完整扫描并重新进行所有认证，缓存、快速转换等机制会影响流程。
5. “基本速率就是最低速率”“所有发送都至少2 Mbit/s”是课堂简化。基本速率集、支持速率集、管理／控制帧速率及数据帧速率应分别分析。
6. 半双工Wi-Fi链路不意味着设备里永远只有一条射频链。多天线、多频段和多链路设备不能按“一个收发器”概括；同频同时收发还涉及自干扰问题。
7. OFDM子载波频谱可以显著重叠；理想同步条件下，其符号区间内内积为零才是正交的关键。sinc频谱对应特定时间窗模型，不是所有电磁信号频域都呈sinc形状[18]。
8. MIMO中每根接收天线通常收到所有发射天线信号的叠加，而不是与某根发射天线一一对应。半波长间距也不保证信道独立。独立空间流数量受信道矩阵秩、散射条件及信噪比限制，天线数增加不保证速率线性增长[23]。
9. 课堂中的室内90／70／50米、室外160米和Wi-Fi代际名称按原文保留，不作为全球设备性能或认证名称的保证。课间中文闲聊保留原文，未当作课程专业内容解释。
10. GDPR相关内容仅为课堂原话的翻译，本次没有作法律适用性判断。

[21] Cisco，Catalyst CW9166D1 Access Point Deployment Guide（Probe Request/Response）：https://www.cisco.com/c/en/us/products/collateral/wireless/catalyst-9164-series-access-points/catalyst-9166i-9164i-dg.html

[22] Microsoft Learn，WiFiCx WPA3-SAE authentication：https://learn.microsoft.com/en-us/windows-hardware/drivers/netcx/wificx-wpa3-sae-authentication

[23] MathWorks，What Is MIMO?：https://www.mathworks.com/help/comm/ug/what-is-mimo.html

## 20261010-0800：DCF、帧间间隔与虚拟载波侦听

| 英文 | 中文译法 | 核对与说明 |
|---|---|---|
| DCF / PCF | 分布式协调功能／点协调功能 | 区分分布式争用和集中协调；现代机制还有扩展，不以此概括全部Wi-Fi |
| CSMA / CD / CA | 载波侦听多路访问／碰撞检测／碰撞避免 | 标准英文CSMA通常展开Carrier Sense Multiple Access；CA降低风险而不保证零碰撞[24][25] |
| FIFO | 先进先出 | First In, First Out；本课“first input, first output”不是通常展开 |
| queue / server | 队列／服务台 | 排队模型里的server不是必须指计算服务器 |
| unicast / multicast / broadcast | 单播／组播／广播 | 按目标接收集合区分，不意味着无线能量只传播到对应目的地 |
| uplink / downlink | 上行／下行 | 用户至接入端／接入端至用户，与实际安装高度无必然关系 |
| slot time / turnaround time | 时隙长度／收发转换时间 | 具体值依PHY而定，20微秒不是所有Wi-Fi通用值 |
| SIFS / PIFS / DIFS / EIFS | 短／点协调功能／分布式协调功能／扩展帧间间隔 | DIFS=SIFS+2×SlotTime；涉及随机退避等条件时不能仅按DIFS判可发[25] |
| Duration / NAV | 持续时间字段／网络分配向量 | NAV在此作为虚拟预留计时器理解，不是普通的随机退避计数器 |
| physical / virtual carrier sensing | 物理／虚拟载波侦听 | 区分PHY检测与MAC时间预留 |
| MPDU | MAC协议数据单元 | 原文“PD means ...”有缩写误识；标准术语为MPDU |

### 原讲述中的技术核对

- 原文把使用CSMA/CD的以太网称为全双工，这是错误的。经典共享介质以太网的CSMA/CD用于半双工；全双工以太网不使用CSMA/CD。边发边检测碰撞不等于全双工数据通信[24]。
- “DCF连续空闲DIFS后即可发送”只是这一节尚未展开退避的简化示意。完整分析还要考虑随机退避、退避冻结恢复、重传和后退避等条件[25]。
- SIFS主要保护ACK、CTS等规定响应及已获准交换，不是任意应用把包标为重要就能绕过争用直接用SIFS发送。
- 信标包含时间同步信息，但DCF不是所有节点按信标起点统一分配全局发送槽位的TDMA系统。时隙、TSF时钟同步及退避启动条件不能混为一谈。
- Duration字段常以微秒编码预留时长，NAV不能一般地按“固定五个时隙”理解。基础DATA/ACK交换中，数据帧Duration通常指该帧之后的SIFS及ACK预留；不能把当前数据帧本身也无条件重复计入。原讲述的时间线是示意。
- 物理载波侦听除能量检测外，还可涉及前导码／信号检测；实际CCA门限不是简单地与瞬时纯噪声能量比较。
- “人人解调每个帧首部”依赖可接收和可解码条件，不能保证所有站点总能读出Duration。
- “PCF从未实现”的表述过强；本课聚焦常用DCF并把PCF作补充，不据此宣称全部厂商全部历史实现均不存在PCF。
- 对话类比和原文混合语言用于保持课堂上下文，不能作为标准协议的精确描述。

[24] Cisco，Troubleshooting Ethernet：https://www.cisco.com/en/US/docs/internetworking/troubleshooting/guide/tr1904.html

[25] IETF，RFC 8325，Mapping Diffserv to IEEE 802.11：https://datatracker.ietf.org/doc/html/rfc8325
