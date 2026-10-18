# 20261012-1331 恢复后PPT语义复审

结论：revision124的78段恢复正文已完整阅读，8张课件图全部保持语义对齐；无需移动，无新增确认缺图。source_semantic_reaudit_after_revision124=true。

只读核验当前after.json中的正文，未使用历史paragraphs.json或heading-plan中的旧文本，也未修改飞书。8张PNG重新与固定PDF第23–26页比较，图块、导航块和顺序均与此前审计版本一致。

当前正文快照SHA256：b5fc3581e8d9e5d8e978637690d90c2f17d0d134762e1e9daa962f4b01ada591
固定PDF SHA256：15011ccc6e929fd6f0b9fb7837ee450734a12058891fa028e6e1bf658c4902e8

## 逐图核验

### 图47：Backoff Value: Binary Exponential Backoff
- 当前实际位置：P2之后、P3之前，前块类型2（4为H2）
- 图片块：doxcnxfTo4JUVDPN3hf2lJuS3gd
- 固定PDF：第24页 upper
- 结论：恢复P2仍明确随机[0,CW]、初次CWmin、重试扩大窗口和2^BE−1；P3–7讲BE从5逐次加1、CW31到63并封顶，与图47公式完整匹配。ASR冠词/词尾未定不影响图页识别。
- PNG SHA256：fbb0f271a1226f47d8dec4e29aee5a8414d00dfa93246070b268573f7cb76437

### 图48：Example: CW Growth (802.11b, CWmin = 31, CWmax = 1023)
- 当前实际位置：P3之后、P4之前，前块类型2（4为H2）
- 图片块：doxcnXPHO3jBPy2cpA3xE0Bh9Vc
- 固定PDF：第24页 lower
- 结论：恢复P3明确早期WiFi BEmin=5、CW=31；P4–5第二次指数6、CW63及CWmax封顶，与图48表的31/63/127/…/1023一致，原位置P3后正确。
- PNG SHA256：688283ffea5b42ff9ae2a3ff62129b4165558b3e14458ad26eb9886341ea20f3

### 图45：When Does a Station (Re)contend? — the Backoff Cases
- 当前实际位置：P9之后、P10之前，前块类型2（4为H2）
- 图片块：doxcnc7j1Yu1VqrAZpgPfPUc4le
- 固定PDF：第23页 upper
- 结论：P7明确回看earlier slides，恢复后的P9说已讲失败重传，并有two more situations，首先是新包到达但信道忙；P12把第三种留后，P55–66随后讲成功后退避。图45放P9后并未错位；第3条仅写有后续队列数据与P66/图50更宽表述的源差异继续保留。
- PNG SHA256：4d79267fa42ee59bd90a753283bedbf00a13596703cc2e7ea585e66a2a2eaab8

### 图46：Backoff Procedure (Collision Avoidance)
- 当前实际位置：P10之后、P11之前，前块类型4（4为H2）
- 图片块：doxcnWTFsquj2iIzhTunL0hhLyd
- 固定PDF：第23页 lower
- 结论：最新P11逐步讲空闲DIFS→均匀抽整数×slot→空闲递减→忙冻结→再空闲DIFS恢复→0发送，正是图46流程；原图紧跟P11标题、位于P11正文前，无需移动。
- PNG SHA256：72417b1284986366420e641bf250076c3b0d49f165cf9871ff8778d2b2d592d1

### 图49：Remarks on Backoff
- 当前实际位置：P51之后、P52之前，前块类型2（4为H2）
- 图片块：doxcnYA2YIgLfiTLfyHxySIUeed
- 固定PDF：第25页 upper
- 结论：恢复P51完整保留糖果类比、拥挤碰撞与信道差错的区别，末尾明确差错造成的CW翻倍只增加delay、不能改善信道；图49第3条正是此结论，前两条也对应P28–36，P51后是准确小结位置。
- PNG SHA256：0bc53e2d8cdb5b74ba026380ba63d6c1ca973b26219a5827005d460c68658163

### 图51：Remark: Broadcast and Multicast Traffic
- 当前实际位置：P55之后、P56之前，前块类型2（4为H2）
- 图片块：doxcn02sGtGH4i7wCWx46feJRs4
- 固定PDF：第26页 upper
- 结论：P53明确broadcast/multicast不期待ACK，P54解释多接收方同时ACK碰撞，P55一次发完即结束不重传；图51的广播多播条目与此匹配，放P55后与讲解结束相接，不应仅按图号移到post-backoff后。
- PNG SHA256：7c3f853e9d04309c47aba59efbf264a2779e0eba15003a95048ec5d8419bf269

### 图50：Post-Backoff
- 当前实际位置：P66之后、P67之前，前块类型2（4为H2）
- 图片块：doxcnETwbqqjz80GK8xGqUWwMKc
- 固定PDF：第25页 lower
- 结论：恢复P56–66讲成功后退避和公平性，P66明确no matter what your MAC queue state is…must run post-backoff，即使成功时无包也必须执行，与图50首段逐项匹配；P66末转开销，新主题前保留此总结图合理。
- PNG SHA256：b54270369fce12dd50aa3d2c696b7f8a3af69898b4101bf88a781ccd0189547b

### 图52：Worked Example: Why 11 Mb/s Never Feels Like 11 Mb/s
- 当前实际位置：P75之后、P76之前，前块类型4（4为H2）
- 图片块：doxcnQS6J19jan879PbrFimceGh
- 固定PDF：第26页 lower
- 结论：恢复P66明确切到课件实际开销例子，P67 DIFS50µs、P68基本速率1Mb/s，P67–75讲PHY/MAC首部、payload、SIFS、ACK、退避与重传；P76明确效率50–55%，与图52约55%的worked example匹配。该图在P76标题后正文前合理；不是宣称原音逐字读出了1500B/34B/6.06Mb/s所有数字。
- PNG SHA256：ffe14bd261ed7692dae468306acf69cd756ca3988f4aca1a9aad3e16917b8121

## 仍保留的来源缺口

- AP/A/B/C退避、移除退避和发送后退避的课堂白板时序
- 两节点碰撞概率1/(CW_min+1)的条件概率与求和白板推导

上述两类不是本固定PDF内已确认遗漏页；复审通过不等于课堂全部视觉恢复。正文未定词继续保留，图审不替代原音逐字认证。

本补充记录更新全19课索引的1331恢复后语义复审状态。此前已发布/交付的检查点与ZIP保留为历史，原hash不覆盖。
