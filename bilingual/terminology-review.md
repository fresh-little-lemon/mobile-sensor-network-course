# 双语课程稿术语核对

核对日期：2026-10-18。当前覆盖：19份课程，共1465组双语段落；各录音的补充核对如下。

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

## 20261009-0759：停止等待ARQ与Wi-Fi协议栈

| 英文 | 中文译法 | 核对与语境 |
|---|---|---|
| CRC | 循环冗余校验；字段值称CRC校验值 | 属于差错检测，不能将其与密码学摘要等同 |
| digest | 摘要 | 本课用作CRC的直观类比，不代表抗碰撞的密码学哈希 |
| stop-and-wait ARQ | 停止等待式ARQ | 发一包后等待确认，超时可触发重传；ARQ与确认机制见RFC 3366[16] |
| acknowledgment / ACK | 确认／确认包 | 区别于用户有效载荷；不译为“承认”[16] |
| timeout / retransmission | 超时／重传 | “未收到ACK”可由数据包丢失或ACK丢失引起，不单独证明对方未收到数据[16] |
| PHY / MAC | 物理层／介质访问控制层 | IEEE 802.11规范范围为MAC与PHY[17] |
| protocol stack | 协议栈 | 各层处理及其相互接口，不能等同于某个单一硬件 |
| WLAN | 无线局域网 | IEEE 802.11工作组与规范的正式领域[17] |
| transport / network / application layer | 传输层／网络层／应用层 | 本课分别以TCP、IP和应用为例 |
| ICT | 信息与通信技术 | 指知识及专业领域，不是某一种无线技术 |

### 对照稿保留与科学校核

- 原文19:18附近把等待ACK、超时后重传的一方说成receiver。按本课停止等待流程，这些动作属于transmitter。英文及中文保留原修订稿角色措辞，纠正说明集中放在本文件，不悄悄修改原讲述。
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
- 本节停止等待确认说明针对基本单播流程，不覆盖所有Wi-Fi帧种类、组播、聚合与块确认机制。
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


其他记录中少量纯中文课间片段也按英文译文在前、中文原文在后排列，段落位置保留。混合语种原句及含混语音仍可回到修订稿与diff追溯。

## 20261010-1000：隐藏终端、RTS/CTS与随机退避

| 英文 | 中文译法 | 区分 |
|---|---|---|
| hidden terminal / hidden node | 隐藏终端／隐藏节点 | 节点之间无法侦听对方，不代表它们无法干扰共同接收方 |
| RTS / CTS | 请求发送／允许发送 | Request to Send / Clear to Send；不要把CTS译成数据确认ACK |
| explicit channel reservation | 显式信道预留 | 用控制交换告知相邻节点预留时间，不是永久独占频段 |
| RTS threshold | RTS阈值 | 帧长相关的可配置门限，不是信号强度门限 |
| NAV | 网络分配向量 | 此处表示虚拟载波侦听的预留计时，与退避计数器不同 |
| backoff / freeze / resume | 退避／冻结／恢复倒计时 | 冻结时保留剩余值，不能理解为每次遇忙都重新抽签 |
| contention window | 竞争窗口 | CW是抽签范围的参数，不直接等同某一次抽到的等待时间 |
| CW_min / CW_max | 最小／最大竞争窗口 | PHY及接入类别不同，参数可以不同[25] |
| slot time | 时隙长度 | 本课退避时间是整数个时隙 |
| ACK timeout | 确认超时 | 未收到确认触发失败判断，但不能仅凭无ACK断定必定发生碰撞 |

### 数值与技术表述核查

1. 本课说RTS阈值通常为400字节，这不能作为所有Wi-Fi设备的统一默认值。Cisco示例设备文档给出的默认值为2347。译文保留课堂数字，配置时应查具体设备和帧长口径[26]。
2. CW从31变63时，可抽整数数目从32变64；不是把31直接乘2。按本课上界记法可写为CW_next=min(2(CW+1)-1,CW_max)。课中“右端点翻倍”是近似口语。
3. 末尾CW_max的语音数值仍未裁决。RFC8325所述DCF示例为1023，并指出OFDM的CW_min为15；这帮助理解协议，却不能证明录音实际说出了哪个数。正文继续保留“数值不清”，不把标准数值冒充录音[25]。
4. “控制帧总按最低速率发送”是教学简化。基本速率集合不等于唯一最低速率；实际响应速率与PHY和标准规则相关。首部能否解调也依赖接收条件。
5. 教师先按旧拓扑说B连接接入点二，随后明确改为A、B都连接接入点一。两处都保留，后续图解按修改后的拓扑理解。
6. “其他节点是B”在两种转写中均出现，但后续修改后的例子明确指A和接入点二。这是保留的讲话疑点，并非译文擅自改换节点。

[26] Cisco，DPC/EPC系列无线参数说明，RTS Threshold默认值：https://www.cisco.com/en/US/docs/video/at_home/Cable_Modems/2300_Series/4042832_A.pdf


## 20261012-1331｜竞争窗口、概率退避与发送后退避

本节将录音校订与专业解释分开。以下补充不是讲者新增发言，也不用于填补听不清的词句。

- **Backoff／退避**：随机计数器按空闲时隙递减；忙时冻结，重新满足等待条件后继续，不能把冻结理解成重新随机抽取。本录音中的backup、because、kickoff、beak of等统一按退避语境修订。
- **CW、CW_min、CW_max与退避指数**：课堂写法为CW=2^BE−1。未到上限时递增指数对应CW_new=2(CW_old+1)−1，因此31变63，不是精确的31×2。随机整数范围[0,CW]包含CW+1个值。CW_min不是每次失败都增大的变量；原段7的“contention window minimum value”是讲者口头用语，英文留标记。早期示例BE=5、CW_min=31不代表所有PHY或接入类别都用31。[IEEE工作组关于CW递增式的说明](https://www.ieee802.org/11/email/stds-802-11/msg02014.html)
- **碰撞概率1/(CW+1)**：课堂推导是在两个节点独立地从相同的CW+1个整数中均匀抽取、同时开始倒计时且其余条件相同的简化例子中成立：Σ_n P(B=n)P(C=n)=(CW+1)/(CW+1)^2。不能把它直接当成任意节点数或真实网络负载下的总体碰撞概率。这是对讲稿推导适用条件的说明。
- **Post-backoff／发送后退避**：这里讨论成功传输后的退避及公平性，不是叫“fast backoff”的另一种快速算法。早期两种转写都近似fast，但同一录音后文反复明确post-backoff，所以标注为上下文推定。讲者提到“仅有一点不同”，本段录音没有完整展开所有队列与计数器细节，不自行补讲。商业网卡实验的研究者和型号未在来源中明确，未补造引用或名称。
- **失败不等于碰撞**：ACK缺失也可能来自信道差错；讲者的“Wi-Fi假设拥挤”是在解释退避设计，不表示协议能准确判定每次失败原因。扩大窗口可能增加接入时延，这一点保留原口语论述。
- **DIFS、SIFS、PIFS、EIFS**：数据竞争前的DIFS与ACK前的SIFS不能混用；末尾ASR的PIFS/SIFS混淆依据原始文本及语境修正。50 μs DIFS属于课堂所取的早期参数示例；DIFS=SIFS+2×slot time，数值依PHY而变，不能推广到所有Wi-Fi。约300 μs EIFS也是讲者给的近似量级。[Cisco的早期DCF时序示例](https://www.cisco.com/en/US/docs/solutions/Enterprise/Mobility/emob30dg/WANQoS.html)
- **NAV、Duration字段**：NAV是虚拟载波侦听所用的网络分配向量，记录介质预留时间；原文nuts、noth、now等按上下文改为NAV。物理侦听与NAV共同影响媒介忙闲判断。
- **广播/多播确认**：讲者讲的是基础传统组播/广播发送，不逐个接收者返回普通单播ACK；“只发一次”应在该课堂范围内理解，不能据此否认其他版本或增强机制。未用后续标准功能改写课堂发言。
- **BSS、ESS与地址字段**：原段86的“独立BSS只需发射/接收两个地址”是过度简化；标准数据帧即使源/发送者、目的/接收者身份重合，也仍可能有第三个BSSID字段。RA/TA是当前无线一跳收发者，SA/DA是端到端源/目的；不能把逻辑角色数直接当作帧中字段数。四地址帧对应To DS=From DS=1的无线分布场景，而不是只要两个AP通过有线网络连接、属于ESS，就必然在它们之间传四地址802.11帧。正文保留讲者原话，并在校订版标明范围问题。[Cisco帧地址字段说明](https://community.cisco.com/t5/networking-knowledge-base/802-11-frames-a-starter-guide-to-learn-wireless-sniffer-traces/ta-p/3110019) · [Cisco对WDS无线AP互联的定义](https://www.cisco.com/c/en/us/support/docs/smb/wireless/cisco-small-business-100-series-wireless-access-points/smb2040-connect-multiple-access-points-together-through-wireless-dis.html?dtid=osscdc000283)
- **开销、basic rate与50–55%效率**：前导、PHY头、MAC头、帧间间隔及ACK占用时间是课堂解释重点。不同PHY前导/头的发送规则并不能全部概括成“一个basic rate”；1 Mb/s是本段示例。50–55%是讲者给出的粗略效率估计，录音未提供负载、帧长、PHY速率、聚合和重传等实验条件，不把它写成所有Wi-Fi版本的固定上限或经验证结论。



## 20261012-1530｜EIFS、PCF轮询与信标延迟

以下是独立技术核查，不是讲者新增发言，也不用于把听不清的片段补成标准条文。正文保留讲者的历史协议讲解和教学简化；本节注明适用范围。

- **EIFS／Extended Interframe Space／扩展帧间间隔**：external FS、extended effects、external force等均按同课明确的extended IFS统一。讲者用“物理层与MAC层侦听不一致”解释动机；正式条件更具体，包括接收结束报告错误或MAC FCS错误，不是任何忙闲不一致都触发。提前结束EIFS的标准表述是收到无差错帧后恢复接入规则，不只是“能读出头部”；恢复后仍按DIFS及必要的退避操作，不能理解为立即发送。[IEEE 802.11-2012，9.3.2.3.7（历史标准，第三方镜像）](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=926)
- **NAV／Network Allocation Vector／网络分配向量**：本例A听到B却无法正确接收其Duration信息，因而没有从该帧建立预留；“NAV空闲”不等于物理信道必然空闲。原文闹钟、nap、now等据上下文修复。A/B/C的无线范围和信道衰落条件保留原例，不推断新的拓扑。
- **PCF／Point Coordination Function／点协调功能**与**DCF／Distributed Coordination Function／分布式协调功能**：PCF是AP内点协调器控制的轮询接入，DCF是课堂前文的竞争接入。原文PCS、PCL、VCS及ASR将协议名误作PIFS的地方按整段对象区分，不能将协议PCF与帧间隔PIFS混同。
- **CFP／无竞争期与CP／竞争期**：课堂采用一个信标间隔内先CFP后CP的简化图。历史标准还允许CFP按若干信标/DTIM间隔重复，并非每个信标之后都必有CFP。正文照录“superframe”，不把示例扩展为所有配置的定义。[IEEE历史PCF方案，5.3.1及图5-16](https://www.ieee802.org/11/Documents/DocumentArchives/1995_docs/1195101_scan.pdf#page=4)
- **CF-Poll、数据与确认的合并**：讲者的fast ACK是在解释对前一传输的及时捎带确认；正式帧子类型使用CF-ACK，可与Data、CF-Poll组合。它不是把一个完整ACK分组塞进另一个MAC头部。正文“ACK packet in the header”两种转写均有，故保留并在此说明，未无声改口。历史资料明确允许发往新站点的帧携带对上一站点的确认。[IEEE历史PCF方案，5.3.3.1](https://www.ieee802.org/11/Documents/DocumentArchives/1995_docs/1195101_scan.pdf#page=8)
- **Null frame／空帧**：表示此轮没有数据可发的课堂说明保留；“control packet”是用途描述，不等于MAC Type字段的Control分类。不能把Null frame理解成根本没有发送任何帧。**CF-End／无竞争结束帧**结束CFP；原文contention free period and按上下文推定为end，校订版保留推定标记。[IEEE历史PCF方案，5.3.3.1](https://www.ieee802.org/11/Documents/DocumentArchives/1995_docs/1195101_scan.pdf#page=9)
- **SIFS、PIFS、DIFS**：本例连续成功交换用SIFS；“PCF期间所有分组一律SIFS、完全不侦听”不能泛化。未收到预期响应时可用PIFS恢复控制，历史方案也明确列出CCA条件。PIFS比DCF竞争使用的DIFS短；正文第二个比较项的ASR不可靠，按论证推定DIFS并保留不确定性。[IEEE历史PCF方案，5.3.2.1与5.3.3.1](https://www.ieee802.org/11/Documents/DocumentArchives/1995_docs/1195101_scan.pdf#page=6)
- **TBTT／Target Beacon Transmission Time／目标信标发送时间**：信标可因正在进行的DCF交换而延迟，目标时刻与实际发送时刻要区分。课堂每100毫秒是示例，不是标准固定值；100 TU等于102.4毫秒。原段40的100 seconds由独立ASR直接支持修为100 milliseconds，不将讲者数字改为100 TU。[Linux Wireless对TBTT与TU的说明](https://linuxwireless.sipsolutions.net/en/developers/Documentation/ieee80211/power-savings/__v3.html)
- **Polling list／轮询列表与实时队列信息**：关联时表达参与意愿，不代表标准要求列表永不更新。历史标准有重关联和动态加入列表的机制；课堂关于轮询空队列、缺乏精细实时状态所导致低效的论证仍然保留。[IEEE 802.11-2012，9.4.5.3（历史标准，第三方镜像）](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=950)
- **“PCF仍在标准中”是有年代限制的课堂陈述**：不应将其作为当前标准状态。IEEE TGmd的2018年1月工作记录已经记载批准删除PCF；正文仍照录讲者说法，而不替讲者改写。“商用产品未实现”也没有在本次转写核查中作为覆盖全部产品的市场调查结论验证。[IEEE工作组2018年1月记录](https://grouper.ieee.org/groups/802/11/email/stds-802-11-cac/msg02707.html)
- **时延与未讲完的第三个问题**：本段讲了轮询空队列的开销及信标起点被延迟的问题，最后只预告第三点。可变载荷及发送速率已在正文出现，但不能据此把下一段录音的完整第三点提前写入本段。



## 20261012-1620｜PCF时延局限、EDCA与传输机会

以下是独立技术核查，不是补写讲者发言。正文保留讲者的口语解释、图中编号和教学简化；明显技术范围问题在此说明，不用外部资料假装补听录音。

- **Wi-Fi 4与IEEE 802.11e不能等同**：本课两种转写都把二者连在一起，因此正文照录。Wi-Fi联盟的代际命名把Wi-Fi 4对应到802.11n；802.11e-2005则是MAC服务质量增强修订案。二者可以共同出现在同一设备中，但不是同一个标准名称。[Wi-Fi联盟原始公告，2018年10月3日](https://www.globenewswire.com/news-release/2018/10/03/1600662/0/en/Wi-Fi-Alliance-introduces-Wi-Fi-6.html)；[IEEE 802.11e标准页](https://standards.ieee.org/ieee/802.11e/3131/)
- **HCF、EDCA、HCCA**：分别为Hybrid Coordination Function／混合协调功能、Enhanced Distributed Channel Access／增强型分布式信道接入、HCF Controlled Channel Access／HCF控制信道接入。原文announced、Ann's、HTS等按明确的术语对象修复。HCF包含竞争式EDCA和由混合协调器控制的HCCA；讲者称后者“PCF 2.0”是类比。Q用于标识QoS能力。[IEEE术语与机制说明](https://technav.ieee.org/topic/ieee-80211e-standard/)
- **“都已实现”与PCF“从未实现”是课堂概括**：不能据此推断所有产品。IEEE工作组2008年教程称PCF实际未使用、HCCA为可选机制且当时未被广泛实现，不能把“标准定义了HCCA”当作“所有Wi-Fi 4设备都实现HCCA”。正文保留原话。[IEEE QoS教程，第6、18页](https://www.ieee802.org/1/files/public/docs2008/avb-gs-802-11-qos-tutorial-1108.pdf#page=18)
- **四个接入类别与课堂队列编号**：课堂从高到低称队列0、1、2、3。这是图中编号。正式ACI编码是0→AC_BE、1→AC_BK、2→AC_VI、3→AC_VO。语音、视频、尽力而为、后台四类应分开；本课一度把最低优先级文件流量也称best effort，正文没有替讲者改口。[IEEE QoS教程，第9页](https://www.ieee802.org/1/files/public/docs2008/avb-gs-802-11-qos-tutorial-1108.pdf#page=9)
- **AIFS与CWmin**：AIFS是Arbitration Interframe Space／仲裁帧间间隔，不是arbitrary。“四类侦听时间必须各不相同”和CWmin依次3、7、15、31只是课堂示例。常见OFDM非AP默认值按VO、VI、BE、BK排列，AIFSN为2、2、3、7，CWmin为3、7、15、15。语音和视频的默认AIFS相同；后台和尽力而为的CWmin也相同。CWmax的作用仍取决于碰撞与重传状态，不能普遍视为无关紧要。[OpenBSD官方802.11实现中的默认EDCA表及重试窗口参数](https://github.com/openbsd/src/blob/master/sys/net80211/ieee80211_output.c)
- **TXOP／Transmission Opportunity／传输机会**：它是有界的媒介控制时间，包含即时响应。课堂“任意使用五毫秒”应结合帧交换规则理解，不能当作取消长度、确认或保护约束。TXOP limit为0有专门含义，仍可进行规定的单次数据传输及必要响应，不是禁止发送。[IEEE 802.11-2012，9.19.2.2，历史标准原文镜像](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=972)
- **语音与视频的TXOP上限**：常见OFDM非AP默认值，VO为1.504毫秒，VI为3.008毫秒，而BE和BK为0。课堂说明语音分组短、视频可需要更长突发发送，便于理解；“其他数据文件也应统一用更长TXOP”不是这组默认值。具体数值还随PHY和配置变化。[OpenBSD官方默认EDCA参数](https://github.com/openbsd/src/blob/master/sys/net80211/ieee80211_output.c)
- **50/34微秒、20/9微秒**：这是与PHY及配置有关的示例，不能简单等同于引入802.11e的前后变化。教程把9微秒时隙与802.11a的16微秒SIFS并列；DIFS按SIFS加两个时隙计算时得到34微秒。正文该间隔名是由数字与上下文推定，双语版保留“应该是DIFS”。[IEEE QoS教程，第8页](https://www.ieee802.org/1/files/public/docs2008/avb-gs-802-11-qos-tutorial-1108.pdf#page=8)；[IEEE 802.11-2012，9.3.2.3.5](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=926)
- **QoS Control／服务质量控制字段**：正式结构是16位字段，内含TID等子字段；不是简单记录四个队列号。Queue Size在特定非AP QoS数据帧条件下报告相应TID的缓存量，以256字节为单位，不是字面上的剩余分组个数。正文保留讲者的subfield及how many packets表述。[IEEE 802.11-2012，8.2.4.5.1、8.2.4.5.2、8.2.4.5.6](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=487)
- **CRC、FCS与停止等待**：CRC用于检错；承载32位CRC的FCS位于帧尾，不是MAC头内部字段。停止等待还涉及确认与重传，不能仅由“有CRC”推出。正文保留课堂枚举，没有把讲者的CRC无声改成其他字段。[IEEE 802.11-2012，8.2.3与8.2.4.8](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=498)
- **RTS/CTS阈值**：标准机制以帧长度等条件决定是否使用RTS/CTS；课堂说payload size是简化，不应直接当作只比较应用载荷的实现规则。[IEEE 802.11-2012，9.3.1](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=923)
- **FIFO与播放缓冲区**：FIFO的正式展开是first in, first out／先进先出。正文保留讲者first input, first output的口语说法。Playout buffer译为播放缓冲区；voice、video、data-file同步的时延容忍比较仍是本课例子，并非对所有实时视频或语音应用给出同一时延上限。EDCA提供统计优先级，本身不保证每个分组的确定时延。[IEEE QoS教程，第12、14页](https://www.ieee802.org/1/files/public/docs2008/avb-gs-802-11-qos-tutorial-1108.pdf#page=12)

保留待核：开头basic DCF/PCF名称冲突；HCCA自纠前的缩写；一处短帧间隔名单；直觉回答的具体措辞；缺失的队列号与DIFS名称已在双语正文中保留推定语气。以上资料不能代替原声裁定。

## 20261013-0803｜Block Ack、公平性、HCCA 与 Wi-Fi 4 物理层

核查日期：2026-10-18。依据本节原始文字、完整独立 ASR 及下列一手标准/工作组/厂商材料。本节是独立术语与技术范围说明，不属于讲者发言，也没有把这里的知识反向补入英文或中文正文。原段编号指原始 95 个讲话块，时间只是定位锚点。

### 一、术语统一

- Block Ack / BA：块确认；Block Ack Request / BAR：块确认请求。正文保留讲者对控制分组的口语说明，没有擅自给未说出的短控制分组补上 BAR 名称
- bitmap：位图；acknowledgment：确认；payload：有效载荷
- DCF：Distributed Coordination Function，分布式协调功能；post-backoff：后退避
- EDCA：Enhanced Distributed Channel Access，增强型分布式信道接入；不要把 enhanced 误作 announced
- per-packet fairness：逐分组公平；temporal fairness：时间公平；throughput：吞吐量
- TXOP：Transmission Opportunity，传输机会；TXOP limit：传输机会限额。讲者讨论时通常指允许占用的时长
- HCCA：HCF Controlled Channel Access，HCF 受控信道接入；poll / polled station：轮询／被轮询站点，不是 pull
- CFP / CP：无竞争期／竞争期；PIFS / SIFS：PCF 帧间间隔／短帧间间隔
- QoS Control：服务质量控制字段；queue status：队列状态；BSS：Basic Service Set，基本服务集
- traffic signaling：业务信令；call admission control：呼叫接纳控制；TSPEC：业务规格
- beamforming：波束成形；radiation pattern：辐射方向图；omnidirectional antenna：全向天线
- OFDM：正交频分复用；MIMO：多输入多输出；spatial stream：空间流；modulation and coding scheme / MCS：调制与编码方案
- bit/s、Mbps、Gbps 是比特速率；不与 byte/s 混用。正文原段34的 gigabyte 已根据独立 ASR 和本课多处一致证据修成 gigabit

EDCA/HCCA 的命名与 802.11e 的 MAC QoS 归属见 [IEEE 对 802.11e 的技术说明](https://technav.ieee.org/topic/ieee-80211e-standard/)。本课原段4称 enhanced distributed coordination function，正文保留该课堂措辞，并未假装讲者处处用了统一的标准全称。

### 二、Block Ack 的字段与适用范围（原段1–4，00:00:02–00:01:54）

讲者用一个比特表示一个分组是否收到，是解释位图的简化示例。标准的基本 Block Ack 位图还涉及起始序列号与分片位置，不能把这个例子视为所有 BA 格式的完整定义。MAC header 与 Block Ack Bitmap 是需要区分的结构部分，原段2“位图在 MAC 首部”保留为讲者说法。可核对 [IEEE 802.11e-2005 标准留存件的 Block Ack 格式](https://ptacts.uspto.gov/ptacts/public-informations/petitions/1538342/download-documents?artifactId=H6RT3We3fFJVLYYHKI21UZsRznbsMktrmc0uDtoZSR3MiK-nEnrQvAs)；该链接的搜索索引可读，直接获取此次返回 403，未宣称已逐页打开全文。

原段4“新版本中 mandatory / always”是讲者概括，不能据此断言每一种帧、每次传输都必须使用 BA。机制存在 Immediate 与 Delayed Block Ack 等不同流程，需结合协商及具体传输方式判断。参见 [Cisco 员工撰写的 Block Ack 机制说明](https://community.cisco.com/t5/networking-blogs/blockack-mechanism-and-ap-debugging-for-blockack-exchange/ba-p/3106301)。正文没有补写讲者未讲的协商流程。

### 三、课堂公平性推导的前提（原段5–34与50–65）

下列公式是对本节已讲数量关系的独立整理，未新增到讲者正文：

- 共同观察时长为 T，两个饱和站点相互可听、同类队列采用相同接入条件，长期平均接入次数均记为 n
- DCF 的一包模型：Th_A = n × L_A / T；Th_B = n × L_B / T。此模型中，相同有效载荷长度使两者吞吐量相同
- 等长 TXOP 简化模型：Th_A ≈ n × τ × R_A / T；Th_B ≈ n × τ × R_B / T。τ 表示相同发送时长；只有把协议开销等忽略或等效处理，才可以直接用 τR 表示有效数据量
- 因而，同样的接入次数、同样的占用时间、同样的有效吞吐量是三个不同概念。课堂图中的 A、B 交替表示平均模型，不能读成协议强制逐次轮流

TXOP limit 是上限，不代表每次必定填满；实际还涉及队列可用数据、帧交换开销、重传、终止条件和所选参数。EDCA 的 TXOP limit 为零还具有单帧发送的特定含义，不能解释为完全不能发送。见 [NTT 对 EDCA 参数和 TXOP 的说明](https://www.ntt-review.jp/archive/ntttechnical.php?contents=ntr200711sf6.html)。因此，正文保留讲者“相同持续时间”和一分钟跑步比喻，技术核查不把它们提升为无条件协议保证。

### 四、HCCA、轮询与服务质量（原段35–45，00:28:37–00:42:16）

HCCA 与 EDCA 源自 802.11e 的 QoS 增强；将这整段称作“Wi-Fi 4 引入的新集中式机制”，是本课的组织方式，不等于历史上首次定义于 802.11n。Wi-Fi 4 对应 802.11n，可参见 [Cisco 2026 官方无线课程材料](https://community.cisco.com/kxiwq67737/attachments/kxiwq67737/documents-routage-et-commutation/175/2/Webcast_R%26S-Wireless-Episode-1-mar25-2026_extended.pdf)。

“PCF 不再有”“HCCA 现在 works”不可等同于每台设备都部署。IEEE 工作组 2008 教程明确区分机制、可选支持和实际实现情况，并介绍按 TSPEC 分配 TXOP 与接纳控制；这是当年的材料，不能当作 2026 市场覆盖率调查。见 [IEEE QoS Tutorial，特别是第4、15、18页](https://www.ieee802.org/1/files/public/docs2008/avb-gs-802-11-qos-tutorial-1108.pdf)。

原段41的 contention period 与正在讨论的 CFP 不完全一致，英文和中文均保留阶段名不确定。原段43轮询后的间隔，原文 shifts 倾向 SIFS，独立 ASR 却作 PIFS；正文保留冲突。技术上应区分 HC 获取/恢复媒介和站点对轮询的响应，不能只把两者缩写互换。上述 IEEE 教程第18页也把轮询响应的 SIFS 与 HC 接管时的 PIFS 分开说明。

### 五、队列信息与接纳控制（原段37–41、66–70）

QoS Control 中的队列信息不是无延迟、无条件完整的全局队列快照。Queue Size 表示的是特定类别或业务流的缓冲量，存在编码单位及适用条件；“AP 获得实时状态、只轮询有包的站点”是讲者的调度直觉。见 [IEEE 802.11-2007，第7.1.3.5.5节](https://www.cs.mun.ca/~yzchen/bib/802.11-2007.pdf)。该 PDF 本次网页工具因文件过大未完整打开，已核对搜索索引中该节的原文摘录。

原文 implicit handshake 已依据窗口35明确的 explicit handshake 修复为“显式握手”。本课用接受、降低可提供吞吐量、拒绝或等待解释接纳控制；不要把这一口语对话理解为所有上传照片都会进行同样协商。接纳控制可以限制业务负载，但不自动保证所有干扰环境下的端到端 QoS。[IEEE 教程的接纳控制流程与限制，第14–17页](https://www.ieee802.org/1/files/public/docs2008/avb-gs-802-11-qos-tutorial-1108.pdf)。

### 六、波束成形与天线数（原段74–79、85）

拢手喊人的比喻用于说明定向增加接收信号，不表示真实电磁传播是一条没有旁瓣或多径的细线。Wi-Fi 4 的波束成形曾存在可选反馈方式和实现互通问题；不能由“较新版本很好用”推出所有上下行传输都必有同样的波束处理。参见 [Cisco《802.11n: The Standard Revealed》](https://community.cisco.com/kxiwq67737/attachments/kxiwq67737/4931-docs-wireless-mobility/2143/1/68311-white_paper_c11-427843_v1.pdf)。此次使用其可读取的搜索摘录，直接打开失败。

天线数量增加提供更多空间处理的可能，但天线数不必等于可同时使用的空间流数。例如厂商给出的 4×4:3 配置就是四发四收、三条空间流。见 [Cisco Aironet 4800 部署指南](https://team-development.cisco.com/c/en/us/td/docs/wireless/controller/technotes/8-7/b_cisco_aiironet_series_4800_acces_point_deployment_guide.html)。正文保留讲者2×2、3×3、4×4的完整列举，不加入未讲的天线秩条件。

### 七、频段、信道与调制（原段80–85）

- 本课泛指 Wi-Fi 可使用2.4/5/6 GHz，不表示 Wi-Fi 4 本身支持6 GHz。Wi-Fi 6E 是向6 GHz扩展的命名；见 [Cisco Wi-Fi 6/6E/7说明](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-wifi-6-vs-wifi-6e.html)
- “三个”“12个”须结合信道宽度与监管域。原段81的12在独立ASR中不够清楚，正文保留数字并标不确定，没有换成别的常见数量。厂商设备的频率/信道表按监管域列出不同集合，见 [Cisco Aironet 700数据表](https://www.cisco.com/c/en/us/products/collateral/wireless/aironet-700-series/data_sheet_c78-726725.html)
- 20→40 MHz是信道绑定的课堂示例；“速度基本翻倍”仍有调制、编码、保护间隔及空间流等前提，不能直接等于应用下载速度翻倍
- 16点星座可携带4比特/符号，64点星座为6比特/符号。原段83先指16、又指64，随后说“这个情况4比特”，图中指代不清；正文保留全部原数值并标明指代问题。此基本映射见 [Cisco QAM编码说明](https://www.cisco.com/c/en/us/td/docs/cable/cmts/cmd_ref/b_cmts_cable_cmd_ref/cable_commands__cable_d.html)，引用的只是调制映射，不把电缆系统参数挪用于Wi-Fi

### 八、6.5、600、11与46的范围（原段34、86、90–95）

802.11n 的6.5 Mbps与600 Mbps对应不同配置，600 Mbps需要四条空间流、40 MHz信道和400 ns保护间隔等条件。[Cisco 802.11n速率表](https://www.cisco.com/c/dam/global/en_ca/training-events/pdfs/Next_Generation_Wireless_Solutions-Atlantic-Spring08-Customers.pdf)。同表将11 Mbps列在802.11b之下，因此讲者“very initial version=11 Mbps”不宜用作整个802.11系列起点的严格历史定义。

46 Gbps在窗口48、50明确转写为forty-six，窗口15也给出46；没有依据改成4.6。“46”作为概述数字也见于 [Cisco官方Wi-Fi 7介绍](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-wifi-6-vs-wifi-6e.html)。但最终标准的空间流范围、单链路或聚合口径仍须区别，不能由一个概述峰值确认所有设备的可达速率；[IEEE TGbe 2022讨论](https://www.ieee802.org/11/email/stds-802-11-tgbe/msg07919.html)已涉及不定义超过八条空间流的范围。该邮件是当时的标准化讨论，不替代最终条文。本次保留讲者46并列出范围限制，没有以23、4.6或其他熟悉数字静默替换。

PHY速率与MAC/应用有效吞吐量仍须区分。正文保留讲者以高物理速率引出“这些能力究竟用来做什么”的追问，没有替学生补答或提前添加下一节内容。Wi-Fi 8/802.11bn仍在标准化的授课背景可与 [IEEE TGbn 2026年9月进展](https://www.ieee802.org/11/Reports/tgbn_update.htm)对照；没有把未来预计日期当作已完成事项。

### 九、仍未解决的录音范围问题

所有95个原讲话块均已校订并翻译，但“全部音频样本已运行ASR”不等于每秒均可靠转写。5610–5840秒的主窗口51/52及拆分复核反复达到生成上限；其中文残片不能可靠归属讲者或补成课程内容。最后主窗口与90秒尾部只出现一个孤立、无语境的英文词，不能据此认定真实说话者或完整尾部发言。原始输出全部保留；此处没有声明这些区间静音，也没有伪造逐字可恢复内容。

## 20261013-1000｜Wi-Fi 吞吐效率、聚合与 DCF/EIFS 例题

本节是独立术语与技术核查，不属于讲者发言。以原讲话块编号定位；正文仍保留课堂简化、口头重复和自纠。没有看过本课板书或幻灯片图，因此不能用推算出来的答案冒充图中给定值。独立 ASR 是文字核对证据，不是标准正确性的证明。

### 一、术语与单位

- PHY / physical layer：物理层；preamble：前导码；header：头部；payload：载荷。不要将 payload/preamble/MAC 错识的 pillow、runtime、mark 等词当成新的技术概念
- Mbps = megabits per second，兆比特每秒；MB/s 是兆字节每秒，数值换算差 8 倍。原段3的 megawatt、5的 megabyte、26的 megabytes 均须对照前后数字及独立 ASR 修复，不是给讲者重新计算速率
- MAC：媒体访问控制；DCF：分布式协调功能；DIFS：DCF 帧间间隔；SIFS：短帧间间隔；EIFS：扩展帧间间隔；ACK：确认；NAV：网络分配向量；BSS：基本服务集；SINR：信号与干扰加噪声之比
- 本课 TF 是讲者用于等候确认并判断发送失败的超时记号。不能因为原识别为 DF、ts、PDF，就引入多个不同的计时器
- 微秒、毫秒、秒须区分。练习数据包的 1、1.4、1.5 用毫秒；TF 的 100/150 讨论用微秒。原段49的100与150冲突没有用量纲修复来掩盖

DCF、DIFS、EIFS、SIFS、CW及slot time的定义可见 [RFC 8325 §1.6、§6.1](https://www.rfc-editor.org/info/rfc8325/)。该RFC也说明BSS成员关系本身不保证成员间都可直接通信；本题“所有节点互相能听见”是额外明确给定条件。

### 二、物理速率不等于用户吞吐量（原段1–30）

讲者以同样的载荷大小说明：数据部分发送得越快，固定等待和封装开销的相对占比越大。这是分析未聚合情形的课堂比较，不能摘成“Wi-Fi 4总体比早期Wi-Fi更慢”。应区分PHY数据速率、MAC有效吞吐量、应用层有效吞吐量，以及这里所说的有效发送时间占比。

为说明原段18的量纲，若长度L以比特计、速率R以比特/秒计，则时间为L/R；以字节计时先乘8。这是独立量纲推导。原段14及独立ASR却都说“multiplied by 1 Mbps”，正文保留该说法；不可偷偷改成“divided”然后声称是逐字校订。原段18补回的192微秒来自ASR窗口8，不是查表后塞回正文的数字。

### 三、1、6.5、600 Mbps 的不同含义（原段11–28）

1 Mbps 是本课早期Wi-Fi例子采用的基本速率。不能把某个PHY的前导码/头部格式，概括成所有Wi-Fi版本都用同一个“最低数据速率”发送整个前导码。

6.5 Mbps 可对应802.11n的MCS 0、20 MHz、800 ns保护间隔数据速率，见 [Cisco 6300系列数据表的MCS表](https://www.cisco.com/c/en/us/products/collateral/wireless/6300-series-embedded-services-access-points/datasheet-c78-742906.pdf)。它不是“所有Wi-Fi 4前导码与头部统一按6.5 Mbps发送”的通则。600 Mbps则是特定四空间流、40 MHz和短保护间隔配置的峰值。

HT-mixed格式包含让旧设备识别的传统前导码/信令以及HT专用字段，不能把这些字段都等同于载荷MCS。聚合、速率和HT-mixed格式的区别见 [Cisco《802.11n: The Standard Revealed》pp.13–18](https://community.cisco.com/kxiwq67737/attachments/kxiwq67737/4461-docs-network-infrastructure/10346/1/68311-white_paper_c11-427843_v1.pdf)。正文保留讲者6.5/600的原始问答，技术范围在这里解释。

### 四、1500 字节不是所有 IP 数据包的上限（原段22、27、31）

1500字节是常见以太网IP MTU的例子；[RFC 894](https://www.rfc-editor.org/info/rfc894/)规定了该封装场景，并有[已验证勘误](https://www.rfc-editor.org/errata_search.php?rfc=894)将误写的minimum改成maximum。它不是IP协议自身的通用最大长度。IPv4 Total Length字段可表示到65535字节，包含IP头部，见 [RFC 791 §3.1](https://www.rfc-editor.org/info/rfc791/)。正文保留讲者“at most 1500”的课堂假设，没有改成另一套课程内容。

### 五、两级聚合（原段31–35）

讲者先讲高层载荷组合、共用一个外层MAC头，再讲多个MAC帧组合、共用一次PHY发送；术语上分别对应A-MSDU与A-MPDU层次。两者可以组合，但并非每次发送都必须经过两级聚合。原文没有可靠出现这两个缩写，因此没有将它们伪装成讲者说过的话加入正文。

聚合不是无条件把任意比特直接拼在一起：仍有子帧边界、必要头部、校验和长度/填充规则。A-MPDU中的MPDU保留各自MAC帧结构，并可被分别解码；[MathWorks官方MAC解码示例](https://www.mathworks.com/help/wlan/ug/802-11-mac-frame-decoding.html)直接展示分隔符校验和逐MPDU处理。讲者的“只加一个头部”应按所指层级理解，不表示所有内部开销消失。

### 六、ACK 速率与固定开销（原段21–22）

正文保留本例ACK按11 Mbps的最优情形，不扩展成“ACK总与数据帧同速”。控制应答帧速率有Basic Rate Set及前一帧速率/调制等约束。IEEE工作组关于控制应答速率的[正式讨论记录](https://www.ieee802.org/11/email/stds-802-11-tgm/msg00442.html)明确区分ACK的基本速率规则与更高速的触发数据帧。此记录用于说明范围，不冒充本课板书或逐字录音证据。

### 七、EIFS不是任意两层状态不一致的通用修复（原段52–55、59、85–94）

“物理层听到功率、MAC无法读出Duration/NAV”是讲者解释这个碰撞例子的直观模型。严格条件涉及错误接收的帧，例如PHY接收结束指示错误或FCS不正确；待介质空闲后才开始相应的延后。不能仅由NAV为零就推断一定使用EIFS，也不能只要检测到任意能量就笼统套用。

IEEE工作组邮件引述802.11-2016 §10.3.2.3.7，区分DCF用EIFS、EDCA用EIFS−DIFS+AIFS[AC]，见 [IEEE TGbd对EIFS条款的讨论](https://www.ieee802.org/11/email/stds-802-11-tgbd/msg00433.html)。本课明确采用基本DCF，不能把后者EDCA公式无提示地改进课堂时间图。原段89与窗口46均写idle，正文保留并提示与前文检测到B信号的冲突，不能单靠协议常识悄改。

### 八、退避窗口、冻结与重传（原段60–71、90–99）

退避从当前CW范围抽取整数；CWmin是最小边界，重试时窗口会增长至上限，不能把每一次失败后的抽签都概括成始终从CWmin抽取。正文仍保留讲者原段60的“0 to CWmin”，独立核查见 [Cisco DCF重试与竞争窗口说明](https://www.cisco.com/en/US/docs/solutions/Enterprise/Mobility/emob30dg/WANQoS.html)。这个区别不改变本题已直接给定退避整数的计算方式。

冻结后继续递减的是剩余计数，并非听到其他节点就重新随机抽签。例一给定A=10、B=11；先各减5，剩5/6；A再减完5后，B剩1。这些数值在原文内部一致。例二先由C完成5个槽；A和B开始递减的时刻不同，故在C发送前可分别减5和11，不可因为C用了5槽就强制所有节点也只减5。

### 九、例题中的未见图信息与转写冲突

- 原段49同时出现TF=100微秒与150微秒；后面例二明确150微秒。不据后例抹掉前例两种说法
- 原段69将恢复退避者写成A/C，而上下文是A/B；须保留修复证据或自然的不确定限定
- 原段94将B的退避整数写成13，原段97为30，而且“even longer”与13小于19不符。独立ASR窗口49和51均给13，仍不足以裁定原段97的30；正文保留冲突，不能只按想要的答案改数
- 原段96先说B先到零，随后明确自纠为A，必须保留这一自纠。原段97及窗口50–51都说increases，正文保留“增加”，另提示倒计数语境可能应为“递减”。19=5+14只是与讲者给定数字一致的算术核验，不等于看过时间图
- 原段57–58是课间对话，不属于协议推导。原有文字保留并译出，无法验证的身份字段和词义应自然标注；不从失控ASR的重复串中创造人物、事件或新对话

### 十、证据范围

校订使用原始转写、独立ASR窗口和上下文；不使用智能纪要代替逐字正文。对生成上限、空输出和无上下文孤立语句，保留原始结果但不把它们当作补回讲话的依据。“整段音频已处理”与“每一秒讲话均可靠转写”是不同结论；空输出不能证明静音。

## 20261014-0801｜隐藏节点、后退避与ACK时序例题

以下为独立术语和技术范围核查，不是讲者发言。原段编号从1开始，ASR窗口索引从0开始。没有看过本课板书或幻灯片图，不能把推算值冒充题目给定值，也不能用标准知识补造听不清的原话。

### 一、术语与单位

- DCF：分布式协调功能；DIFS：DCF帧间间隔；SIFS：短帧间间隔；EIFS：扩展帧间间隔。原文中的VCS/BCF、diffs/gifts、sieves/shifts及extended fs/fast均须按完整上下文区分，不是新协议
- ACK：确认；NAV：网络分配向量；MAC：媒体访问控制；PHY：物理层；CWmin：最小竞争窗口。原none/nap/knob/now在明确设置虚拟载波侦听计时器的语境下恢复为NAV
- backoff：退避；post-backoff：后退避。这里的post-backoff是成功发送之后执行的退避，不应把所有重传退避、恢复倒计数都混叫后退避
- time slot：时隙；transceiver turnaround：收发切换；hidden nodes：隐藏节点；half-duplex：半双工；duration field：持续时间字段。TF沿用讲者用于检测发送失败的计时符号
- 1毫秒=1000微秒。题目的0.2、0.3、0.4、0.65、0.7是毫秒量级；SIFS10和时隙20是微秒量级。换算只用于检查，不可据常见参数自动确定原文所有数值

DCF、SIFS/DIFS/EIFS、时隙和竞争窗口的概念见[RFC 8325 §1.6及§6.1](https://www.rfc-editor.org/rfc/rfc8325.html#section-6.1)。CWmin、SIFS和slot time取决于所用PHY；本课的CWmin=31、SIFS=10微秒、slot=20微秒不能泛化为所有Wi-Fi版本。抽签使用当前CW；失败重试时CW可增大，不能把讲者“CWmin是能抽到的最大整数”扩展为每次重试都固定使用CWmin。

### 二、隐藏节点与“听到”/“通信”

本课题设中，A与B彼此不可听；AP、A、C之间可听，AP、B、C之间也可听。A/B的隐藏关系不影响它们分别与AP通信。一个节点检测不到另一个节点，不表示AP处没有碰撞；同一个时刻，各节点的物理载波感知结果可以不同。

“位于同一BSS”本身不保证每对节点都能直接通信，这是[RFC 8325 §1.6的BSS定义](https://www.rfc-editor.org/rfc/rfc8325.html#section-1.6)明确区分的事项。本题必须使用给定拓扑，不能从所有节点都连接同一个AP推断它们彼此可听。

课末讲者对有基础设施Wi-Fi和设备到设备通信的对比，是本课采用的拓扑模型。正文保留原话，不将“Wi-Fi节点只能与AP通信”扩展为所有802.11部署或所有直连扩展机制都如此。

### 三、NAV与物理载波感知不能混同（原段38–40、55、85–86）

正文反复保留讲者“B听到ACK、读取Duration字段、设置NAV并冻结计数器”的说法。需要另行注意：对非QoS站点，若被确认的前一帧More Fragments=0，普通ACK的Duration值为0；有后续分片等情形另有规则。不能推断每一个最终ACK都会建立非零NAV预约。即便ACK中的Duration为0，实际正在接收ACK期间仍可以通过物理载波感知判断信道忙。

依据：[IEEE 802.11-2012 §8.3.1.4，印刷页405–406，PDF页503–504，标准原文的第三方镜像](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=503)。已对照本地保存的完整标准文本；网络工具因PDF大小限制未重新展开全文。

本课“没有ACK仍按预期对话时长设置NAV”的说明有助于区别预约与实际发送。Duration描述后续交换所需的剩余保留时间，不应简单理解为每次都把正在接收的整个DATA时长重新加在当前时刻之后。正文保留讲者的时间图语言，不偷偷重画时间原点。

### 四、ACK帧结构（原段39）

讲者说控制包没有载荷、全是首部。对于本题普通ACK，可理解为不携带用户数据载荷；但完整ACK还含FCS，不能把所有比特都严格叫MAC首部，更不能把这句话当作所有控制帧子类型的完整格式说明。Duration/ID也不是ACK的第一个字节；其前有Frame Control字段。

格式依据同上[IEEE 802.11-2012图8-15及§8.3.1.4](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=503)。原转写“in correspondence of”与ASR“in first byte”有差异，校订正文保留“在ACK中读取Duration字段”，没有凭ASR制造首字节位置这一技术断言。

### 五、SIFS不仅仅是收发器切换（原段56、60–63）

正文保留讲者把SIFS解释为收发切换时间、切换时不能收发的课堂简化。标准aSIFSTime包含接收RF延迟、接收PLCP延迟、MAC处理延迟以及接收到发送的切换时间；不能把整个SIFS完全等同于硬件切换时间。DIFS=SIFS+2×slot time是所述DCF定时关系。

依据：[IEEE 802.11-2012 §9.3.7，印刷页843，PDF页941](https://mrncciew.com/wp-content/uploads/2014/10/ieee-802-11-2012.pdf#page=941)。讲者的半双工解释服务于“AP正在发ACK就不能同时接收B的数据”这一题设；没有在正文扩展成其他无线系统的通则。

### 六、EIFS条件（原段9–13）

原课用PHY忙而MAC不能读懂来直观解释EIFS。正式规则涉及错误接收的帧，例如PHY结束报告错误或FCS错误；不是任意能量检测、NAV为零或两层状态不同都自动触发EIFS。基本DCF与EDCA的相关等待表达式也不同。

依据：[IEEE TGbd讨论中引述的802.11-2016 §10.3.2.3.7](https://www.ieee802.org/11/email/stds-802-11-tgbd/msg00433.html)。这里不把EDCA规则代入讲者明确采用的基本DCF算例。

### 七、后退避的总整数与剩余整数

本题反复讨论B的后退避为13+n，n取1、2、3、4。总整数对应14、15、16、17，不能把“剩余计数可以为1”误读为“最初只抽1”。C已从7减去2，余5；B若在恢复时也余5，两者可能同时到0。B若余更多，C可先成功发送，但这不满足“B的两个包都要在C之前成功”的题意。

这里的0也有两个讨论位置：整次后退避为0，和先经过13个槽后剩余部分取0。讲者分别解释它们为何不满足目标，校订没有将两个问答压缩成一个结论。

以上是对原话内部算术的独立核对，未声称看过图中每个绝对时刻；特别是C到包的0.35/0.55毫秒冲突，两个值都早于某些后续事件并不等于能据此裁定原话。

### 八、转写证据与未决项

- 原段21的C到包时刻为0.35毫秒，独立ASR窗口8为0.55毫秒。正文保留原值及明确冲突，不用预期答案选值
- 原段44及窗口26都只口头列出14、15、16，却在此前列出13+4；后面原段66明确包括17。正文保留本处漏项，并自然说明
- 原段51的0.065毫秒由独立ASR窗口31明确的0.65修复，并与原段21、窗口21一致；属于转写修复，不是推导后改题
- 原段55补回内容及原段56、窗口34–35都出现15个时隙，与后续13+n不一致。两份转写均支持15，所以保留原说法并标示冲突，不悄悄改13
- 原段56的B will stop在两份转写中都出现，但这一分支发送者正是B，按拓扑应是C暂停；正文保留B并说明矛盾。该段第二种余数原文为2、独立ASR为4，也保留原读法及差异
- 原段76的ACK时长，原文与窗口43都给140 seconds。正文保留140秒并明示单位疑问；微秒虽符合题目时标，但不能据常识将其当作已核实原话
- 原段9两份转写均出现sending a signal，但上下文是A接收时感知信号；sensing属于有标记的语境推定
- 练习暂停、课间空输出不能证明静音；生成上限后的“嗯”“学习”等长重复串也不等于真实重复。原课间中文片段保留并译出，模型新出现的学校/退学等不稳定语句不当作可靠私人谈话补入正文

以上核查不会把标准条文变成讲者新增内容。最终数字、残片及尾部结论以独立修改记录的逐段证据为准。


## 20261014-1000｜设备到设备网络、空间复用与多跳路由

以下是独立术语和技术范围核查，不是讲者发言。源块编号从1开始，独立ASR窗口索引从0开始。没有看过本课图示或板书，数学推导和标准知识不充当听不清原话的转写证据。原段79的n−1由窗口38明确识别后才补回，并非依据树的性质代填原话。

### 一、术语统一

- device-to-device communication（D2D）：设备到设备通信；ad hoc network：自组织网络。两者密切相关，但不宜把所有D2D功能都定义成无基础设施、多跳、移动的网络
- spatial reuse：空间复用；spectrum/frequency reuse：频谱／频率复用；densification：密集化；radio resources：无线电资源
- unicast／broadcast／multicast／geocast／anycast：单播／广播／多播／地理广播／任播。geogas、any gas等为语境明确的近音误识
- neighbor：邻居节点；radio range：无线电覆盖范围；interference range：干扰范围；half-duplex：半双工
- flat/mesh topology：平面／网状拓扑；tree topology：树形拓扑；cluster-based topology：基于簇的拓扑；cluster head：簇头；bridge node：桥接节点
- relay：中继；hop：跳；multihop：多跳；routing：路由；network layer：网络层；MAC：媒体访问控制；physical layer：物理层；IP：互联网协议
- DCF：分布式协调功能；EDCA：增强型分布式信道接入。原DCS、VCF、VCA等必须按上下文区分，不能当作额外协议。原段89–90的第二个缩写，原文为EDCA，独立ASR窗口43为EDCF；正文保留EDCA并明确记录冲突，不因标准术语更常见就断定发音。二者机制及QoS差异见[RFC 8325 §6](https://www.rfc-editor.org/rfc/rfc8325.html#section-6)

### 二、D2D、蜂窝侧链路与自组织网络不是同一范围

讲者说明D2D可属于4G/5G规范，又用无基础设施网络解释其便利性。正文保留这两种应用场景。LTE的ProSe及5GS的ProSe是有具体服务、授权和架构约束的标准体系，不能据“支持D2D”断定任何手机都能不经配置建立任意多跳网络。参考[3GPP ProSe研究条目](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=653)及[3GPP TS 23.304：5GS ProSe](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3855)。音乐会歌词分发是课堂示例，未据此声称某个实际演唱会部署过该服务。

### 三、空间复用和环形范围是课堂模型

原段32的diversification在原文和独立ASR中都出现；上下文可能指densification，但正文保留diversification并提示，不把这项语义判断冒充确定转写。

降低发射功率、缩短收发距离可以使同频并行通信成为可能，但“低功率”本身不保证没有干扰。还需考虑期望信号、噪声、其他发射机、传播条件和可接受解码门限。讲者用两个远离的短链路和同室低声说话来作解释，保留这些类比，不把它们提升为所有蜂窝系统的资源分配定理。

无线电覆盖范围与干扰范围画成圆及圆环，是简化建模。实际链路可受障碍物、功率和同频干扰影响，还可能不对称；“邻居一定能可靠双向通信”是本课假设。[RFC 2501 §3](https://www.rfc-editor.org/rfc/rfc2501.html#section-3)明确讨论移动、发射／接收覆盖、功率、干扰和双向／单向链路。正文不把能检测能量、能解调、可成功交付混为一谈，也不将原话中的“不会干扰”静默改成另一个论断。

### 四、Geocast与Anycast

本课的路面结冰通知按目标地理区域传播，与GeoBroadcast的目标区域概念一致。ETSI同时定义了向目标区域内任意一个站点传送的GeoAnycast；这些通信都可能跨多跳，不能只按发射机附近一跳来理解。参见[ETSI EN 302 636-2 V1.2.1 §4、§5.4–5.5](https://www.etsi.org/deliver/etsi_en/302600_302699/30263602/01.02.01_60/en_30263602v010201p.pdf#page=6)。

讲者把anycast概括为“附近任意一个节点收到即可”。在IP任播中，目标是同一任播地址标识的接口集合中的一个，通常由路由度量选择；不是任意陌生节点，也不保证地理最近，更不是“广播后碰巧有一个收到”就算任播。参见[RFC 4291 §2及§2.6](https://www.rfc-editor.org/rfc/rfc4291.html#section-2.6)。正文保留讲者的简化，不替换为标准定义。

### 五、图、树和“fully connected”

n个顶点的无向简单图最多有n(n−1)/2条边，因为每一对不同顶点至多对应一条无向边。n个顶点的树有n−1条边，是连通且无环的情况；不是任何称作“平面”的实际无线拓扑都拥有最大边数。原段80的maximum number of nodes在两份转写中均出现，尽管上下文固定节点数、比较链路数；正文保留nodes并提示该混用，不静默改成links。树中任一边断开会破坏整棵树的连通性，而有替代路径的网状图可能维持相应节点对的连通。这是对课堂数学模型的独立核查，不据公式填造转写缺口。

讲者在簇间桥接时说fully connected，同时解释为“不希望有孤岛、整个网络相连”。这里应理解为连通，不是每对节点都有直接边的完全图。不同簇结构也不一定都要求普通节点只能与簇头通信；该要求属于本课采用的簇内星形模型。

### 六、Bluetooth的角色与桥接

手机／耳机的“更重要角色”应理解为示例中的通信控制角色，不是设备本体或人的等级。Bluetooth BR/EDR的piconet中有Central与Peripheral角色；Peripheral之间不在同一个piconet信道上直接通信，同一设备可分时参与多个piconet。但参与scatternet本身并不自动提供网络层路由。LE的拓扑和多连接角色又有不同约束，不能将BR/EDR限制无差别推广到所有Bluetooth。依据[Bluetooth Core 6.2 Architecture §3.3.1.1.3及§4.1](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-62/out/en/architecture%2C-change-history%2C-and-conventions/architecture.html)。

### 七、路由器与协议分层

本课假定多跳网络中的节点能转发别人的包，因而称每个节点为路由器。不能推出每个D2D、蓝牙或Wi-Fi终端天然都实现IP路由。MANET可以让节点同时担当主机和路由器，也可以连接固定互联网；见[RFC 2501 §1、§5](https://www.rfc-editor.org/rfc/rfc2501.html#section-1)。家用“无线路由器”经常组合AP和网络层路由功能，AP这一角色本身不能与路由器完全等同。

### 八、多跳不必然使全网总能耗增加

原段116的一处修饰词在原文中为globally、独立ASR中为probably；正文显式保留这项不确定性，不能把它当作确定的全局断言。随后原段117及窗口54又明确说增加总能耗，因此保留后一句的无条件说法。原段116–117反复强调，每一次中继都会新增收发操作，因而全网总能耗增加。正文保留该说法和传递物品的类比。但独立技术核查需要区分：额外接收、电子电路开销会增加，长距离发射放大器所需能量则可能因分段而降低。总能耗取决于距离、路径损耗、硬件、重传和跳数，不能只由“收发次数多”推出必然增加，也不能反向认定多跳必然节能。

[Heinzelman、Chandrakasan与Balakrishnan，HICSS 2000，§2–3及式(1)–(7)](https://pdos.csail.mit.edu/archive/decouto/papers/heinzelman00.pdf#page=2)的原始研究明确比较直接传输和多跳：在短距离或电子电路开销较高时，直接传输可能更省总能量；不同参数下结果可变。这里仅作范围说明，不把论文的数值或模型插入讲者正文。

### 九、RFID与寻物标签

窗口7补回讲者的RFID标签示例，正文保留该技术名称。RFID包含不同频段与有源／无源实现；无源标签利用读写器供给的射频能量及反向散射通信，不能把所有标签都理解成自主发射、任意手机均能直接远距离定位的设备。这个范围提醒不将讲者原话悄悄改成Bluetooth或UWB。参见[GS1：有源与无源标签的区别](https://support.gs1.org/support/solutions/articles/43000733398-what-is-the-difference-between-passive-and-active-tags-)及[GS1 EPC UHF Gen2](https://www.gs1.org/standards/rfid/uhf-air-interface-protocol)。


## 20261015-0803｜隐藏节点算例、路由与能量管理、传感器采样

以下是独立术语与技术范围核查，不是讲者发言。原段编号从1开始。没有查看本课板书或幻灯片图，不用标准知识补造原转写缺句；具体转写证据和未决处以本课独立修改记录为准。

### 一、术语统一

- NAV：网络分配向量；ACK：确认；DIFS：DCF帧间间隔；SIFS：短帧间间隔；backoff：退避；backoff counter：退避计数器；contention window：竞争窗口；CWmin：最小竞争窗口
- hidden nodes：隐藏节点；half-duplex：半双工；transceiver turnaround：收发切换；Duration field：持续时间字段；freeze/resume：冻结/恢复倒计数
- routing：路由；route：路径；source：源节点；relay/intermediate node：中继/中间节点；next hop：下一跳；primary/backup route：主/备用路径；multi-hop：多跳
- MAC：媒体访问控制；PHY：物理层；network layer：网络层；protocol stack：协议栈；spatial reuse：空间复用，不是special reuse
- transmit power：发射功率；power control：功率控制；energy consumption：能量消耗；battery capacity：电池容量；ampere-hour：安时；sleep state：休眠状态；wake-up delay：唤醒时延
- distributed decision-making：分布式决策；ad hoc network：自组织网络；WPAN：无线个域网；body area network：体域网；UAV：无人机；IoT：物联网
- sink：汇聚节点；gateway：网关；sensing board：传感板；physical field：物理场；sample：样本/采样；interpolation：插值；signal reconstruction：信号重建；spatial coordinates：空间坐标

NAV、DIFS/SIFS、竞争窗口等基本术语可参看[RFC 8325 §1.6与§6.1](https://www.rfc-editor.org/rfc/rfc8325.html#section-6.1)。这里只用于核验术语，不把另一标准版本的参数代入本题。

### 二、本题退避值的总数与余数（原段1–16）

讲者给定A抽1、C抽5；B最初抽取的总整数需大于16。B抽17、18、19、20时，先消耗16个时隙后分别余1、2、3、4，因此在C之前接入；抽21时剩5，与C同时到0而碰撞；抽22–31时在C之后接入。这里是对讲者内部算术的核对，不是独立重画了未见的时间图。

“16不能取”的解释同时涉及A发送完成、AP收发切换及ACK发送。B听不到A，不代表AP可以同时发送ACK和接收B；B听得到AP，在ACK期间会冻结倒计数，所以不能把整个ACK时长机械地加进最初抽取的退避整数。正文保留完整问答和讲者的切换说明。

31是本题采用的CWmin值，不是所有PHY、所有重试阶段的统一上限。窗口会随所用接入机制、参数及重试状态变化；同上RFC的DCF/EDCA讨论不能被缩写成“退避只能抽0至31”。

NAV是虚拟载波侦听机制，接收中的实际信道忙也可来自物理载波侦听。正文关于“按数据包+SIFS+ACK设置NAV”的图示语言保留，不能由此推断每个ACK都会建立非零NAV，也不能把某个字段的剩余预约时长与整次交换的总时长混为一谈。

### 三、多跳、总能耗和备用路径（原段20–42）

正文保留讲者“多跳需要更多次收发，所以全网总能耗更高”的原说法。应把它理解为课堂所比较的开销，而不是无条件定理：比较全网能量需同时计入各跳发射功率、发送时长、接收电路、重传和空闲开销。仅增加收发次数，不能单独决定两种路由的总能量孰高。降低单个源节点发射能量，也不等于已经求出了全网最优。

备用路径已经存好可以减少重新寻找路径的等待，但是否仍然可用，仍取决于其链路当时的状态。此处是术语范围提醒，未为讲者添加新的路由算法或假设。

### 四、电池容量不是功率（原段46–53）

讲者把battery capacity解释为可提供的最大“power”，正文保留该词。严格量纲上，Ah度量电荷；1 Ah = 3600 C。功率的单位是W，能量的单位是J或Wh。能量还与端电压有关，不能把Ah单独当作Wh，也不能把电池容量当成额定输出功率。1 A持续1 h的课堂例子说明了电荷容量的含义，并不保证任意实际电池在各种放电条件下都恰好工作1小时。

依据：[NIST SI单位表](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes)、[NIST单位换算表中的ampere hour → coulomb](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9)。正文仍保留讲者重复解释1安时的两个句子，没有改写为教科书段落。

### 五、Wi-Fi与Bluetooth休眠的适用范围（原段55–73）

讲者先说Wi-Fi节点总是醒着，随后也承认可使网卡休眠，并以用户是否手动关闭Wi-Fi解释实际使用习惯。应区分接口“开着”、MAC节能模式及无线电当前处于awake/doze状态，不能把这些概念合并。IEEE 802.11已有节能机制；官方工作组概览也明确提到活动TDLS会话中的站点可以进入power save mode。参看[IEEE 802.11工作组概览的TGz条目](https://www.ieee802.org/11/overview.html)。正文未把讲者评价静默改成技术反驳。

“蓝牙有三种休眠状态”有历史语境：Bluetooth SIG的2008年白皮书列出Sniff、Hold、Park，但也指出Park不鼓励使用并预期移除。不能将此无条件扩展为现代BR/EDR与Bluetooth LE共享、严格按浅到深排列的三种状态。白皮书还说明Sniff安排与同步业务等限制，不能把“没有业务就立刻睡眠”当作所有蓝牙运行模式的规则。参看[Bluetooth SIG白皮书§2.4，PDF第10页](https://www.bluetooth.com/wp-content/uploads/2019/03/Sniff-and-Sniff-Sub-rating-Modes_WP_V10.pdf#page=10)。

较新的[Bluetooth Core 6.1，BR/EDR Baseband §8.7–8.8](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-61/out/en/br-edr-controller/baseband-specification.html)分别规定Sniff和Hold的行为，包含约定的监听/恢复时机。以上只是独立范围核查，正文没有替讲者补出未明确说过的三种模式名称。

### 六、路径损耗与功率控制（原段60–68）

固定频率与天线条件的自由空间模型中，接收功率随距离平方反比变化，对应常用路径损耗指数2。自由空间本身有理想化和距离条件，不能只凭这条知识将原音中的缺失数值当作已核实讲话；本次正文的2由独立ASR窗口34明确补回。依据：[ITU-R P.525-5，Calculation of free-space attenuation](https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.525-5-202411-I%21%21PDF-E.pdf)。

正文保留“真实环境指数大于2”及“所有无线设备都有功率控制”的课堂概括；读者应注意，它们不是对所有传播环境、所有设备控制机制的逐项保证。高发射功率带来更多可达链路与干扰、过低功率可能使网络断连，是本课图示强调的权衡，没有据未见图计算最优功率。

### 七、802.15.4不是完整应用协议栈（原段84）

讲者通过“15”和Wi-Fi中的“11”作对比，并把标准说成指导这类设备的协议栈设计。独立核查中，与低速率低功耗传感器语境相符的是IEEE 802.15.4；它规定PHY与MAC子层，不是单独规定从物理层到应用层的所有协议，也不专属于某一种传感器应用。正文是否出现完整编号，只以实际转写证据为准。

依据：[IEEE 802.15.4-2024官方范围说明](https://standards.ieee.org/ieee/802.15.4/11041/)。本课的“每秒几比特”是应用可能产生的数据量示例，不应误作该标准全部PHY的固定速率。

### 八、采样与插值（原段85–90）

正文区分空间位置x、y、z与时间t，保留讲者从离散测量值重建连续物理场、以及单个传感器在本地处理样本的说明。严格意义的精确重建需要信号及采样条件；插值本身并不保证任意有限、不规则或有噪声的样本能完全恢复未知连续场。单个固定位置的时间样本，也不能无条件恢复整个空间场。

依据：[MIT Signals and Systems Lecture 16: Sampling](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-16-sampling/)、[Lecture 17: Interpolation](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-17-interpolation/)。这里没有把采样定理的前提补写为讲者当时已经说出的内容。

### 九、转写差异仍需保留

- 原段1的0.1缺少明确单位，独立ASR的小数措辞也不稳定，未据图推定具体绝对时刻
- 原段11本处为20，窗口5为17；后面两份转写都列17、18、19、20，正文保留原值并说明差异
- 原段13两份转写都出现C before C；没有按预期主语静默改成B
- 原段37和40的节点D在独立ASR中为B；未见图，不凭路径常识裁定
- 原段82原文六次有限in a保留，但窗口46与拆分46a均触及生成上限并长循环，真实口头重复次数尚未独立核实
- 原段86两份转写均写lightning，而后一句明确说light；正文保留闪电/可能光照的不确定性，未静默更换测量对象
- 原课间中文保留、译出并标明未决词；末尾新出现的设备/白板片段只在原始ASR保留，未作为可靠新增讲话


## 最后两份独立术语核对

- [20261015-1000：IEEE 802.15.4、CSMA/CA及相关技术边界](../diffs/20261015-1000.terminology.md)
- [20261016-0805：停止等待、时隙CSMA/CA、EIFS、NAV与RTS/CTS](../diffs/20261016-0805.terminology.md)

停止等待为用户指定的stop-and-wait译法。术语核查与讲话逐句翻译分开；讲者原话存在技术概括或歧义时，不用标准文字替换原话。
