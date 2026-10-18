# 第61–78段独立修改记录

状态：候选，不是已确认逐字稿。所有变更均相对现飞书检查点，不修改远端。技术近音修复、恢复旧删改与仍待听辨的候选分别说明；不把机器差异数当错误数。

## 61 · 01:13:44

稳定块ID：doxcnOafaFDOATqssKwhE22BQ4g
写回前应验证原块SHA256：fa9d0b1d6f6f221baa386dfa659474b58064007c3673983255c2b025d0163768

### 具体修改

1. Again, to understand how useful a mechanism or solution is, let's play our little game of ablation. → So again, in order to understand how useful [a / the unclear] mechanism is, or solution is, let's play our little game of ablation, right?
   - 理由：恢复So、in order to、两次is及right，撤销原校订的合并；a/the保持冲突。
   - 来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 11–12, absolute 4421.20–4441.52s
2. Let's remove post-backoff and see what happens. What if A does not have to run any post-backoff? → So let's remove the post-backoff and see what happens. So what if A does not have to run any, [any unclear] post-backoff?
   - 理由：恢复两次So与the，Qwen独有any重复明确标待听辨，不机械吸收上下段。
   - 来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 12–13, absolute 4432.24–4455.72s；Unprompted Whisper medium.en raw: chunk-025, segments 13–13, absolute 4441.60–4455.72s
3. Let's add an event here to understand what would happen, considering all possible cases. → Well, let's add an event here to better understand what would happen considering all possible cases.
   - 理由：恢复三类证据均保留的Well及better。
   - 来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 14–15, absolute 4458.16–4482.56s

### 逐句证据

1. So again, in order to understand how useful [a / the unclear] mechanism is, or solution is, let's play our little game of ablation, right?
所以，再一次，为了理解[一种／这一个，待听辨]机制有多有用，或者解决方案有多有用，让我们玩一下我们的小小消融游戏，对吧？
   - Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 11–12, absolute 4421.20–4441.52s
   - 限制：历史Feishu为a mechanism、Our solution；Qwen与medium为the mechanism、or solution。恢复口语重复is，不改成精炼的a mechanism or solution；冠词待听辨。right由历史Feishu与Qwen保留。
2. So let's remove the post-backoff and see what happens.
所以，让我们去掉发送后退避，看看会发生什么。
   - Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 12–13, absolute 4432.24–4455.72s
   - 限制：post-backoff按历史post back off及medium pass back off近音作技术术语规范；Qwen为post go。
3. So what if A does not have to run any, [any unclear] post-backoff?
所以，如果A不必执行任何、[任何，重复待听辨]发送后退避，会怎么样？
   - Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 13–13, absolute 4441.60–4455.72s
   - 限制：Qwen同一窗口保留any any；Feishu与medium仅一次，不把第二个any写成已确认。
4. Well, let's add an event here to better understand what would happen considering all possible cases.
嗯，让我们在这里加一个事件，考虑所有可能的情况，来更好地理解会发生什么。
   - Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 14–15, absolute 4458.16–4482.56s

### 待听辨记录

- [a / the unclear]; [any unclear]
  - 候选：a mechanism / the mechanism / one any / any any
  - 证据：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 11–13, absolute 4421.20–4455.72s
  - 处理：冠词和第二个any均待听辨；不按来源票数确定。

## 62 · 01:14:31

稳定块ID：doxcniDom3MTYG6SdyGg8uIbLqh
写回前应验证原块SHA256：acfbe892156f61001dad4a05a8b5fe3b3ca7ec182b47e16e5991168ca9a0458a

### 具体修改

1. Let's consider that A has another packet in its MAC queue. Remember that we said the MAC layer can be modeled as a queue with a server. → Let's consider that A has got another packet in [a unclear] its MAC queue. Remember that we said the MAC layer can be modeled, right, as a queue with a server.
   - 理由：恢复has got及right，并明确标出Feishu独有in a its口语残片。
   - 来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 15–15, absolute 4468.46–4482.56s；Unprompted Whisper medium.en raw: chunk-025, segments 15–16, absolute 4468.46–4492.98s；Unprompted Whisper medium.en raw: chunk-026, segments 1–1, absolute 4485.00–4494.78s
2. A has transmitted the packet here successfully, but let's assume it has another packet in the queue waiting to be transmitted. → So let's consider that A has transmitted the packet here successfully, but let's assume that A has [got / put unclear] another packet in the queue waiting to be transmitted.
   - 理由：恢复So let's consider that、重复主语A及has got/put词冲突；不以代词压缩原话。
   - 来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 16–17, absolute 4482.56–4503.40s；Unprompted Whisper medium.en raw: chunk-026, segments 1–2, absolute 4485.00–4503.42s
3. This first packet goes through successfully; that's what we represented here. But now A has another packet right here. → So this first packet goes through, right, successfully. This is what we [represented / represent unclear] here. But now A has got another packet right here, right?
   - 理由：恢复So、right、This is、has got及尾部right，保留represent/represented时态冲突；两组重叠窗口只保留一次句子。
   - 来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 18–18, absolute 4505.12–4514.78s；Unprompted Whisper medium.en raw: chunk-026, segments 3–3, absolute 4503.42–4518.58s；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 3–4, absolute 4503.42–4529.80s

### 逐句证据

1. Let's consider that A has got another packet in [a unclear] its MAC queue.
让我们考虑A在[一个，待听辨]它的MAC队列里又有了一个数据包。
   - Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 15–15, absolute 4468.46–4482.56s
   - 限制：历史Feishu为in a its，Qwen和medium为in its；a可能是口误或识别插入，保留待听辨。MAC由medium明确识别，历史/Qwen的mark为技术近音。
2. Remember that we said the MAC layer can be modeled, right, as a queue with a server.
记住，我们说过，MAC层可以被建模，对吧，建模成一个带有服务台的队列。
   - Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 15–16, absolute 4468.46–4492.98s；Unprompted Whisper medium.en raw: chunk-026, segments 1–1, absolute 4485.00–4494.78s
   - 限制：right由历史Feishu及Qwen保留；modeled由medium明确识别，历史modern/Qwen modded为近音。
3. So let's consider that A has transmitted the packet here successfully, but let's assume that A has [got / put unclear] another packet in the queue waiting to be transmitted.
所以，让我们考虑A已经在这里成功地发送了这个数据包，但让我们假设A在队列里[还有／放入了，待听辨]另一个等待发送的数据包。
   - Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 16–17, absolute 4482.56–4503.40s；Unprompted Whisper medium.en raw: chunk-026, segments 1–2, absolute 4485.00–4503.42s
   - 限制：历史Feishu及medium为has got；Qwen为has put。两者含义不同，不强选。
4. So this first packet goes through, right, successfully.
所以，这第一个数据包通过了，对吧，成功地通过了。
   - Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 18–18, absolute 4505.12–4514.78s；Unprompted Whisper medium.en raw: chunk-026, segments 3–3, absolute 4503.42–4518.58s
5. This is what we [represented / represent unclear] here.
这就是我们在这里[已经表示出的／所表示的，时态待听辨]内容。
   - Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 18–18, absolute 4505.12–4514.78s；Unprompted Whisper medium.en raw: chunk-026, segments 3–3, absolute 4503.42–4518.58s
   - 限制：medium chunk-025句尾为represent，重叠chunk-026为represented；历史Feishu和Qwen为represented。重叠只对应一句，时态待听辨。
6. But now A has got another packet right here, right?
但现在A在这里又有了一个数据包，对吧？
   - Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 3–4, absolute 4503.42–4529.80s
   - 限制：此尾句在Qwen41及medium26中完整出现；Qwen40只到But now A is going，不能将截断另作新句。历史Feishu本段未收该句，按现有段边界保留于62。

### 待听辨记录

- in [a unclear] its; [got / put unclear]; [represented / represent unclear]
  - 候选：in a its / in its / has got / has put / represented / represent
  - 证据：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 15–18, absolute 4468.46–4514.78s；Unprompted Whisper medium.en raw: chunk-026, segments 1–4, absolute 4485.00–4529.80s
  - 处理：口误残片、动词及过去时不能据现有文本认证，逐处留待听辨。

## 63 · 01:15:22

稳定块ID：doxcnfJ7kuePp8OBvwoAxXJk1sc
写回前应验证原块SHA256：7087863a79c0033c8c9f39969cc86ca00dc44319e77b888911aaddb161d060cf

### 具体修改

1. When it is done with this dialogue, it has another packet to deal with. What if A didn't have any post-backoff to run? → So when [it's / he's unclear] done with this dialogue, [we'll / we unclear] have another packet to deal with. So what if A didn't have any post-backoff to run?
   - 理由：恢复两个So与we'll/we have，撤销无依据改成it has；保留he/it、时态冲突。
   - 来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 4–5, absolute 4518.58–4540.46s；Unprompted Whisper medium.en raw: chunk-026, segments 5–5, absolute 4529.80–4540.46s
2. It would sense the channel for DIFS, find it idle, and be able to access it and transmit its other data packet. → Well, [it / he / you unclear] will have to sense the channel for DIFS. The channel is idle, and [it / you unclear] will be able to access the channel [and transmit / trust me unclear]. So [it / you unclear] will have to transmit its [other / own unclear] data.
   - 理由：撤销合句压缩及would/find；恢复Well、will have to、The channel is idle、重复the channel、So，移除无原始支持的packet；缺失尾部与代词、other/own分别待听辨。
   - 来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 5–6, absolute 4529.80–4550.44s；Unprompted Whisper medium.en raw: chunk-026, segments 6–7, absolute 4540.46–4562.60s；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s
3. This may be successful. Would that be fair with respect to B and C? → This may be successful. And what would be that? Would that be fair with respect to B and C?
   - 理由：保留原有两句并恢复Qwen及medium均显示但旧校订删去的And what would be that?。
   - 来源：Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s；Unprompted Whisper medium.en raw: chunk-026, segments 8–8, absolute 4564.02–4571.70s

### 逐句证据

1. So when [it's / he's unclear] done with this dialogue, [we'll / we unclear] have another packet to deal with.
所以，当[它／他，待听辨]完成这轮对话时，我们[将会有／有，待听辨]另一个数据包要处理。
   - Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 4–5, absolute 4518.58–4540.46s
   - 限制：历史Feishu为he's、we'll；Qwen为it's、we'll；medium为it's、we。不能按技术叙述习惯改为it has。
2. So what if A didn't have any post-backoff to run?
所以，如果A没有任何发送后退避要执行，会怎么样？
   - Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 5–5, absolute 4529.80–4540.46s
   - 限制：post-backoff为同一机制的术语规范：历史cost、Qwen possible cost、medium phospho-cov均为近音输出。
3. Well, [it / he / you unclear] will have to sense the channel for DIFS.
嗯，[它／他／你，待听辨]将必须侦听信道一个DIFS的时间。
   - Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 5–6, absolute 4529.80–4550.44s
   - 限制：保留will have to，不改为would；Qwen it、Feishu he、medium you冲突。sense与DIFS是技术近音规范（Since/Sends、B's/this），不改成find idle。
4. The channel is idle, and [it / you unclear] will be able to access the channel [and transmit / trust me unclear].
信道是空闲的，而[它／你，待听辨]将能够接入信道[并发送／相信我，待听辨]。
   - Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 6–7, absolute 4540.46–4562.60s
   - 限制：Feishu尾部独立Trust me，medium为and trust me，Qwen未保留此尾部；不能凭技术语义直接补transmit，也不删除残片。
5. So [it / you unclear] will have to transmit its [other / own unclear] data.
所以，[它／你，待听辨]将必须发送它的[其他／自己的，待听辨]数据。
   - Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s
   - 限制：Qwen为it、own；Feishu为you、other；medium为you、other但transmit误成ask me。未擅加packet。
6. This may be successful.
这可能会成功。
   - Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s
7. And what would be that?
那这会是什么情况？
   - Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–8, absolute 4564.02–4571.70s
8. Would that be fair with respect to B and C?
这对B和C来说会公平吗？
   - Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–8, absolute 4564.02–4571.70s
   - 限制：两份ASR均为fear；与后文unfair/fairness构成同一讨论，作fair技术语境近音规范，不改原疑问句结构。

### 待听辨记录

- pronouns and tense
  - 候选：he / it / you / we'll have / we have
  - 证据：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 4–7, absolute 4518.58–4562.60s
  - 处理：逐处保留词冲突，不把讲者叙述统一成it或would。
- [and transmit / trust me unclear]; [other / own unclear]
  - 候选：and transmit (仅近音候选) / Trust me / and trust me (历史/medium原输出) / other data / own data
  - 证据：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s
  - 处理：尾部疑似transmit但未听音，保留可追溯残片及两种data限定词。

## 64 · 01:16:10

稳定块ID：doxcnOX3I4DDVfFDghwN2D719Lf
写回前应验证原块SHA256：143a3e8651c731052c2c8e6589ff598ed433e5fc310d72bc7cf2a7373cc0c291

### 具体修改

1. Poor B and C are waiting for their backoff time, and A just gets the next packet and goes ahead with its transmission. This is unfair. → The poor B and C are waiting [right there unclear], their backoff time, and A just gets the next packet and go ahead with its transmission. So this is unfair.
   - 理由：恢复The、right there残片、So和讲者原有go语法；撤销替补介词for，不伪装为完整顺畅句。
   - 来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–10, absolute 4564.02–4592.18s；Unprompted Whisper medium.en raw: chunk-026, segments 10–10, absolute 4580.36–4592.18s
2. If a Wi-Fi card like A has several packets to transmit, in this situation without post-backoff it will just continue accessing the channel and transmitting its packets. → And indeed, if a Wi-Fi card like A has got several packets to transmit, under this situation without post-backoff, we just continue accessing the channel and transmitting its packets.
   - 理由：恢复And indeed、has got、under this situation及原始we just continue，不把主语语法整理成it will。
   - 来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 10–12, absolute 4580.36–4609.86s
3. With very high probability it will seize the channel for a very long time and transmit, transmit, transmit, while the others have to wait, wait, and wait, because the channel will become busy continuously. → With very high probability, [it / you unclear] will actually seize the channel for a very long time and transmit, transmit, transmit, while the others [will have / we have / we had unclear] to wait, wait, [and unclear] wait, because the channel [will / would unclear] become busy [confused unclear].
   - 理由：恢复actually并标代词、时态及and冲突；continuously无三类原始文本支持，回退为busy之后的待听辨残片。
   - 来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 12–13, absolute 4601.40–4620.60s
4. This was indeed observed experimentally. Years ago, some researchers experimented with different Wi-Fi cards that were commercial products. → And this was indeed observed, also experimentally. Years ago, some researchers made experiments with different Wi-Fi cards. [They / which unclear] were commercial products.
   - 理由：恢复And、also、made experiments和they/which were，不用experimented/that were润色替换。
   - 来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 14–14, absolute 4622.54–4632.44s；Unprompted Whisper medium.en raw: chunk-026, segments 14–15, absolute 4622.54–4642.06s；Unprompted Whisper medium.en raw: chunk-026, segments 15–15, absolute 4632.44–4642.06s
5. All these cards claimed to follow the standard; products must follow the standard. They claimed to do that, but one card was applying everything specified by the standard except post-backoff. → They claimed, all these cards [claimed / claim unclear] to follow the standard. [Of course / for unclear] products must follow the standard. They [claimed / claim unclear] to do that. But actually, one of these cards was applying everything, okay, as specified by the standard, but the post-backoff.
   - 理由：恢复They claimed起句、all these cards重复、Of course/for、But actually、one of these cards、okay、as和句尾but；两处claim时态保留冲突。
   - 来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 15–16, absolute 4632.44–4648.32s；Unprompted Whisper medium.en raw: chunk-026, segments 16–16, absolute 4642.06–4648.32s；Unprompted Whisper medium.en raw: chunk-026, segments 16–18, absolute 4642.06–4669.06s

### 逐句证据

1. The poor B and C are waiting [right there unclear], their backoff time, and A just gets the next packet and go ahead with its transmission.
可怜的B和C[就在那儿，待听辨]等着，等它们的退避时间，而A只是拿到下一个数据包，就继续它的发送。
   - Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–10, absolute 4564.02–4592.18s
   - 限制：历史为right there, their back off time；Qwen为right there because time；medium为very good, their pick-off time。保留历史残句和go语法，right there标待听辨；backoff为术语近音规范。
2. So this is unfair.
所以，这是不公平的。
   - Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 10–10, absolute 4580.36–4592.18s
3. And indeed, if a Wi-Fi card like A has got several packets to transmit, under this situation without post-backoff, we just continue accessing the channel and transmitting its packets.
而且确实，如果像A这样的Wi-Fi网卡有好几个数据包要发送，在这种没有发送后退避的情况下，我们就一直接入信道，并发送它的数据包。
   - Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 10–12, absolute 4580.36–4609.86s
   - 限制：三类文本均呈现we just continue，保持讲者主语漂移，不改成it will；to transmit见历史及Qwen，medium略去。post-backoff为pass the cost/possible cost/cost because近音规范。
4. With very high probability, [it / you unclear] will actually seize the channel for a very long time and transmit, transmit, transmit, while the others [will have / we have / we had unclear] to wait, wait, [and unclear] wait, because the channel [will / would unclear] become busy [confused unclear].
以非常高的概率，[它／你，待听辨]实际上会占据信道很长时间，并且发送、发送、发送，而其他那些[将必须／我们必须／我们过去必须，待听辨]等、等、[并且，待听辨]等，因为信道[将会／会，待听辨]变忙[后词疑似confused，待听辨]。
   - Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 12–13, absolute 4601.40–4620.60s
   - 限制：历史it、will have、and wait、will；Qwen you、we have、无and、will；medium you、we had、无and、would。seize由历史明确，其余size为近音；transmit由历史/Qwen明确。busy后的confused三类均不可靠，不采纳旧校订补出的continuously。
5. And this was indeed observed, also experimentally.
而且，这也确实在实验中被观察到了。
   - Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 14–14, absolute 4622.54–4632.44s
   - 限制：observed有历史及Qwen明确词形；medium absurd属近音。
6. Years ago, some researchers made experiments with different Wi-Fi cards.
几年前，一些研究人员用不同的Wi-Fi网卡做了实验。
   - Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 14–15, absolute 4622.54–4642.06s
7. [They / which unclear] were commercial products.
[它们／这些，连接形式待听辨]是商业产品。
   - Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 15–15, absolute 4632.44–4642.06s
   - 限制：历史与medium为独立they were，Qwen为which were；保留冲突，不顺写从句。
8. They claimed, all these cards [claimed / claim unclear] to follow the standard.
它们声称，所有这些网卡都[声称过／声称，时态待听辨]遵循标准。
   - Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 15–16, absolute 4632.44–4648.32s
   - 限制：恢复They claimed起句和重复cards主语；Qwen第二处claim，历史及medium claimed。
9. [Of course / for unclear] products must follow the standard.
[当然／因为，待听辨]产品必须遵循标准。
   - Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 16–16, absolute 4642.06–4648.32s
   - 限制：medium明确of course，历史/Qwen为for；不能靠语句流畅度决定。
10. They [claimed / claim unclear] to do that.
它们[声称过／声称，时态待听辨]自己这样做。
   - Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 16–16, absolute 4642.06–4648.32s
11. But actually, one of these cards was applying everything, okay, as specified by the standard, but the post-backoff.
但实际上，这些网卡中的一张实施了标准所规定的所有内容，好吧，唯独发送后退避除外。
   - Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 16–18, absolute 4642.06–4669.06s
   - 限制：保留but的except义及okay口语插入；post-backoff由Qwen post pickoff和medium post the cop近音规范。历史the cost became off不另增句。

### 待听辨记录

- waiting [right there unclear], their backoff time
  - 候选：right there, their back off time (Feishu) / right there because time (Qwen) / very good, their pick-off time (medium)
  - 证据：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 9–10, absolute 4572.60–4592.18s
  - 处理：仅规范backoff，前段残片待听辨，不补for。
- busy [confused unclear]
  - 候选：busy. Confused (历史跨段) / busy confused (Qwen/medium) / busy continuously (旧校订才有，非原始支持)
  - 证据：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 13–13, absolute 4609.86–4620.60s
  - 处理：不以语义推测补continuously；保留confused疑似词，待听辨。
- pronouns, modal tense, and reporting tense
  - 候选：it / you / will have / we have / we had / will / would / claimed / claim / Of course / for / They / which
  - 证据：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 12–17, absolute 4601.40–4660.40s
  - 处理：逐处括注；不统一时态或主语，不按模型票数取舍。

## 65 · 01:17:42

稳定块ID：doxcn1cpQfGyubHhKy2AGOYZv2e
写回前应验证原块SHA256：dcfb30afb26fdc0c88910a467b8a625b5f56f83d09151b32566410aac740f5fd

### 具体修改

1. The researchers observed that this Wi-Fi card obtained very, very high throughput, meaning it could transmit a lot of data, while the other cards were starving: they could not get access to the channel. → And what these researchers observed was that this Wi-Fi card was [obtaining / obtained unclear] a very, very high throughput; that means the ability to transmit a lot of data, while the other Wi-Fi cards were starving, so they could not get access to the channel.
   - 理由：恢复And what、was that、a、was obtaining/obtained冲突、that means the ability、完整other Wi-Fi cards及so；撤销meaning it could解释式改写。
   - 来源：Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 18–21, absolute 4660.40–4692.22s；Unprompted Whisper medium.en raw: chunk-027, segments 1–3, absolute 4665.00–4690.20s
2. It was a very unfair service because that commercial Wi-Fi card did not implement post-backoff. → A very unfair service, and this is because, this was because that commercial Wi-Fi card at that time did not implement the post-backoff procedure.
   - 理由：撤销补写It was，恢复不完整名词句、is because/was because自修、at that time、the及procedure。
   - 来源：Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 21–22, absolute 4683.38–4694.20s；Unprompted Whisper medium.en raw: chunk-027, segments 3–5, absolute 4681.32–4708.56s

### 逐句证据

1. And what these researchers observed was that this Wi-Fi card was [obtaining / obtained unclear] a very, very high throughput; that means the ability to transmit a lot of data, while the other Wi-Fi cards were starving, so they could not get access to the channel.
而这些研究人员观察到的是，这张Wi-Fi网卡当时[正在获得／obtained形式，待听辨]非常、非常高的吞吐量；那意味着发送大量数据的能力，而其他Wi-Fi网卡则处于饥饿状态，所以它们无法接入信道。
   - Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 18–21, absolute 4660.40–4692.22s；Unprompted Whisper medium.en raw: chunk-027, segments 1–3, absolute 4665.00–4690.20s
   - 限制：was obtaining保留历史、Qwen及medium27的进行时；medium26重叠为was obtained，登记待听辨但不把同一内容重复写两遍。
2. A very unfair service, and this is because, this was because that commercial Wi-Fi card at that time did not implement the post-backoff procedure.
一种非常不公平的服务，而这是因为，当时这是因为，那张商业Wi-Fi网卡在那个时候没有实现发送后退避程序。
   - Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 21–22, absolute 4683.38–4694.20s；Unprompted Whisper medium.en raw: chunk-027, segments 3–5, absolute 4681.32–4708.56s
   - 限制：保留is because → was because自我修正与at that time限定；post-backoff procedure据post pickoff/prospect of近音规范。

### 待听辨记录

- was [obtaining / obtained unclear]
  - 候选：was obtaining (历史/Qwen/medium27) / was obtained (medium26)
  - 证据：Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 19–19, absolute 4669.06–4675.54s；Unprompted Whisper medium.en raw: chunk-027, segments 1–1, absolute 4665.00–4672.82s
  - 处理：两次medium跨窗同一处，不当成两次发言；动词形式待听辨。

## 66 · 01:18:22

稳定块ID：doxcn61liWTicB4PpLe3q93NYVc
写回前应验证原块SHA256：e0013ddf3419b4abf5ddc0ddd76209a149bd663b9dbfd6c500fc84ba3e673193

### 具体修改

1. This seems like a detail, or one more thing that a node has to do, but it is extremely important for fairness. In Wi-Fi we want to be fair and give everyone the same probability of channel access. It is a very important feature. → So this seems to be, you know, a detail or one more thing that a node has to do, but it's actually extremely important to ensure fairness. In Wi-Fi, we want to be fair, we want to give the same probability to everyone in channel access. So it is a very important feature,
   - 理由：恢复So、seems to be、you know、actually、ensure、we want重复及to everyone in channel access；不精炼改写。
   - 来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 5–6, absolute 4699.64–4716.60s；Unprompted Whisper medium.en raw: chunk-027, segments 6–7, absolute 4708.56–4725.66s；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 7–9, absolute 4716.60–4751.78s
2. Notice that the same would happen without post-backoff even if A had no packet immediately after successfully completing its dialogue. Even if it got a packet a few microseconds later, it would still have an advantage over B and C, who must run backoff. → and notice that the same would happen if we didn't have the post-backoff procedure. Even if A, right after its, [its unclear] completion, successful completion of, [of unclear] its dialogue, didn't have any packet. But even in the case where it gets a packet right after, [a unclear] few microseconds after, [it / you unclear] will still get an advantage [with unclear] respect to B and C, who must run the backoff.
   - 理由：恢复if we didn't have、procedure、Even if A原停顿与completion自修、right after/few microseconds after重复、gets/will still get原时态、the backoff；标记its/of、代词及with冲突。
   - 来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 7–9, absolute 4716.60–4751.78s；Unprompted Whisper medium.en raw: chunk-027, segments 9–10, absolute 4738.30–4759.68s；Unprompted Whisper medium.en raw: chunk-027, segments 10–12, absolute 4752.58–4781.04s
3. That's why the standard says: no matter what the state of your MAC queue is, once you complete a transmission successfully, you must run post-backoff. It is mandatory; we cannot do otherwise. → So that's why the standard says, no matter what your MAC queue state is, we don't care. Once you complete a transmission successfully, you must run the post-backoff procedure, [right / okay unclear]? So that's, [it's unclear] that's mandatory. We cannot do [anything otherwise / any, any number one unclear].
   - 理由：恢复So、原词序your MAC queue state、删去的we don't care、procedure、So that's自修、句尾right/okay和anything otherwise残片；明确medium这里大段漏识别，不拿压缩旧稿补证。
   - 来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 12–13, absolute 4771.14–4810.36s；Unprompted Whisper medium.en raw: chunk-027, segments 13–13, absolute 4781.04–4810.36s
4. Help me out here. Do we have the long break now? No, sorry. Our time... [number unclear]. Okay, thanks. → Help me out here. We, [we unclear] have the long break now? [No / oh unclear], sorry. Our time [three five, five plus three; numbers unclear]. Okay, thanks.
   - 理由：恢复We have原词序与可能重复，记录No/oh冲突，保留原ASR数字碎片但不解释成课间安排；原稿省略号此处是existing_english真实字符。
   - 来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 14–14, absolute 4810.36–4815.20s；Unprompted Whisper medium.en raw: chunk-027, segments 15–15, absolute 4816.52–4817.22s
5. We still have about fifteen minutes. Let me know if I get it wrong, please; I need to adjust the schedule. → Okay, so we still have about fifteen minutes before. Let me know if I [get it wrong / get this one wrong / did something wrong unclear], please. I need to adjust the, [the unclear] schedule, of course.
   - 理由：恢复Okay so、before、of course及可能的the重复；if I后的三种措辞逐处待听辨，不省略限定。
   - 来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 16–16, absolute 4817.80–4822.84s；Unprompted Whisper medium.en raw: chunk-027, segments 17–17, absolute 4823.14–4825.50s；Unprompted Whisper medium.en raw: chunk-027, segments 18–18, absolute 4826.36–4830.72s
6. We have essentially gone through all these slides, using the whiteboard for greater clarity, but the essential information is also in the slides. What I would like to show now is another example presented here. Don't get scared by the many figures in these slides. → Okay, so we run essentially through all these slides, using the whiteboard for greater clarity, but you have the essential information also in, [in unclear] the slides. Okay, so what I would like to show now is another example that is here presented in [the / these unclear] slides. Don't get scared by the many figures that are used in these, [in these unclear] slides.
   - 理由：撤销have gone、the information is改写，恢复we run、you have、Okay so、that is here presented及in these重复；the/these不强选。
   - 来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 19–21, absolute 4832.70–4847.90s；Unprompted Whisper medium.en raw: chunk-028, segments 1–1, absolute 4845.00–4854.86s；Unprompted Whisper medium.en raw: chunk-027, segments 22–23, absolute 4849.10–4858.34s；Unprompted Whisper medium.en raw: chunk-028, segments 1–2, absolute 4845.00–4861.34s；Unprompted Whisper medium.en raw: chunk-027, segments 24–24, absolute 4858.56–4865.64s；Unprompted Whisper medium.en raw: chunk-028, segments 2–3, absolute 4854.86–4869.20s
7. They just highlight something we already know, but here you have a concrete example to emphasize it further. We now know more or less how the basic version of Wi-Fi works. → It's just to highlight something that we already know, but here you have indeed concrete example to further emphasize this. That is, we now know more or less how the basic version of Wi-Fi works.
   - 理由：恢复It's just to、that、indeed及That is，去掉原校订补出的a，并保留this指代和原句词序。
   - 来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 25–25, absolute 4867.20–4874.92s；Unprompted Whisper medium.en raw: chunk-028, segments 3–5, absolute 4861.34–4886.14s；Unprompted Whisper medium.en raw: chunk-028, segments 5–6, absolute 4878.50–4893.94s
8. We already said Wi-Fi is so successful because it works quite well for our needs, but it has a big problem in general: overhead. We already commented on that. Now that we know how the channel is used in Wi-Fi, this practical example gives evidence of it. → We already said that Wi-Fi is so successful because it works quite well for our needs. But it has got a big problem in general, that is overhead, right? We already commented on that. So now that we know how channel is used in Wi-Fi, this is a practical example that gives evidence to that.
   - 理由：恢复that、has got、that is、right、So、this is a practical example that gives evidence to that；不补how channel中的冠词。
   - 来源：Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 6–7, absolute 4886.14–4897.34s；Unprompted Whisper medium.en raw: chunk-028, segments 8–9, absolute 4897.98–4904.22s；Unprompted Whisper medium.en raw: chunk-028, segments 10–10, absolute 4904.28–4906.22s；Unprompted Whisper medium.en raw: chunk-028, segments 11–12, absolute 4906.62–4917.88s

### 逐句证据

1. So this seems to be, you know, a detail or one more thing that a node has to do, but it's actually extremely important to ensure fairness.
所以，这似乎是，你知道，一个细节，或者一个节点必须多做的一件事，但它实际上对于保证公平性极其重要。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 5–6, absolute 4699.64–4716.60s
   - 限制：a node由medium明确识别；Feishu I know that、Qwen and no that为近音残片。保留you know、actually及ensure，不压缩成for fairness。
2. In Wi-Fi, we want to be fair, we want to give the same probability to everyone in channel access.
在Wi-Fi中，我们想要公平，我们想在信道接入方面给予每个人相同的概率。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 6–7, absolute 4708.56–4725.66s
3. So it is a very important feature, and notice that the same would happen if we didn't have the post-backoff procedure.
所以，这是一个非常重要的特性，而且注意，如果我们没有发送后退避程序，同样的情况就会发生。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 7–9, absolute 4716.60–4751.78s
   - 限制：历史now is that由Qwen与medium完整notice that支持作近音规范。post-backoff规范自post pickoff/postback/post-bacov。
4. Even if A, right after its, [its unclear] completion, successful completion of, [of unclear] its dialogue, didn't have any packet.
即便A，恰好在它的、[它的，重复待听辨]完成之后，成功完成了、[了，of重复待听辨]它的对话之后，没有任何数据包。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 9–10, absolute 4738.30–4759.68s
   - 限制：completion → successful completion三类文本均见；第二个its、of只见历史Feishu，不能认证为口语重复，也不直接删去。此处保留even if不完整句。
5. But even in the case where it gets a packet right after, [a unclear] few microseconds after, [it / you unclear] will still get an advantage [with unclear] respect to B and C, who must run the backoff.
但即便在它随即收到一个数据包的情况下，几微秒之后，[few前的a待听辨]，[它／你，待听辨]相对于B和C仍会得到一个优势，[with是否存在待听辨]，而B和C必须执行退避。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 10–12, absolute 4752.58–4781.04s
   - 限制：保留right after、few microseconds after重复及must；medium有a、you、with，历史/Qwen无a、it、respect to。backoff规范自vehicle/record近音，不把优势改写成抽象summary。
6. So that's why the standard says, no matter what your MAC queue state is, we don't care.
所以，这就是为什么标准说，不管你的MAC队列处于什么状态，我们不在乎。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 12–13, absolute 4771.14–4810.36s
   - 限制：MAC queue state规范自mark/max queue/max Q-step the state；medium在此有长段遗漏，不据其分段把we don't care延伸至后面。
7. Once you complete a transmission successfully, you must run the post-backoff procedure, [right / okay unclear]?
一旦你成功完成一次发送，你就必须执行发送后退避程序，[对吧／好吧，待听辨]？
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 13–13, absolute 4781.04–4810.36s
   - 限制：历史Feishu完整transmission successfully ... right，Qwen为permission successfully ... Okay；medium仅到once you complete a，后续遗漏到4810.36秒。transmission及post-backoff为技术近音规范，句尾词冲突待听辨；后半句不能声称由新medium确认。
8. So that's, [it's unclear] that's mandatory.
所以，那是，[它是，待听辨]，那是强制的。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   - 限制：Qwen为So that's that's mandatory；历史为So that's it's that's manual。mandatory由Qwen支持并对应历史manual近音；it's仅历史，保留待听辨。新medium漏掉。
9. We cannot do [anything otherwise / any, any number one unclear].
我们不能[用其他方式做任何事／any, any number one残片，待听辨]。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   - 限制：历史We cannot do anything otherwise；QwenWe cannot do any any number one；medium整句遗漏。不能强选或把残片润色成标准英语。
10. Help me out here.
在这里帮我一下。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   - 限制：历史与Qwen完整支持；medium在4781.04–4810.36秒漏掉本句及相邻课间问句。
11. We, [we unclear] have the long break now?
我们，[我们，重复待听辨]现在要放长课间了吗？
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   - 限制：Qwen为We we have，历史为We have；新medium遗漏。保留陈述词序作提问，不补旧校订的Do。
12. [No / oh unclear], sorry.
[不／哦，待听辨]，抱歉。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 14–14, absolute 4810.36–4815.20s
   - 限制：历史/Qwen No sorry；medium Oh sorry。
13. Our time [three five, five plus three; numbers unclear].
我们的时间[three five, five plus three；数字及其含义待听辨]。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 14–14, absolute 4810.36–4815.20s
   - 限制：三类来源均仅转出three five, five plus three一类碎片。不得据此推断13:55、15:35、五分钟加三分钟或任何课间安排。
14. Okay, thanks.
好，谢谢。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 15–15, absolute 4816.52–4817.22s
15. Okay, so we still have about fifteen minutes before.
好，所以在那之前我们还有大约十五分钟。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 16–16, absolute 4817.80–4822.84s
   - 限制：三类来源均保留fifteen minutes及before；before的参照对象未说清，不补课间具体起止时间。
16. Let me know if I [get it wrong / get this one wrong / did something wrong unclear], please.
如果我[弄错了／把这一次弄错了／做错了什么，待听辨]，请告诉我。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 17–17, absolute 4823.14–4825.50s
   - 限制：历史get it wrong，Qwen did something wrong，medium get this one wrong；未用旧稿覆盖冲突。
17. I need to adjust the, [the unclear] schedule, of course.
当然，我需要调整这个、[这个，重复待听辨]时间安排。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 18–18, absolute 4826.36–4830.72s
   - 限制：I由Qwen及medium保留，历史开头省略；第二个the仅Qwen。
18. Okay, so we run essentially through all these slides, using the whiteboard for greater clarity, but you have the essential information also in, [in unclear] the slides.
好，所以我们基本上讲过了所有这些幻灯片，为了更清楚而使用了白板，但你们在、[在，重复待听辨]幻灯片中也有这些基本信息。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 19–21, absolute 4832.70–4847.90s；Unprompted Whisper medium.en raw: chunk-028, segments 1–1, absolute 4845.00–4854.86s
   - 限制：保留we run现在形式、you have及also词位，不改have gone；第二个in只见Qwen43，44为重叠窗口，不重复拼接。
19. Okay, so what I would like to show now is another example that is here presented in [the / these unclear] slides.
好，所以我现在想展示的是在这里的[这些／该组，指示词待听辨]幻灯片中呈现的另一个例子。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 22–23, absolute 4849.10–4858.34s；Unprompted Whisper medium.en raw: chunk-028, segments 1–2, absolute 4845.00–4861.34s
   - 限制：历史/Qwen为the slides，medium两窗为these slides；恢复完整what I would like及that is here presented。
20. Don't get scared by the many figures that are used in these, [in these unclear] slides.
不要被这些、[这些，in these重复待听辨]幻灯片中使用的许多图示吓到。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 24–24, absolute 4858.56–4865.64s；Unprompted Whisper medium.en raw: chunk-028, segments 2–3, absolute 4854.86–4869.20s
   - 限制：历史及Qwen有in these in these，medium仅一次；标出重复而不平滑删去。figures不在无图的情况下限定为数字。
21. It's just to highlight something that we already know, but here you have indeed concrete example to further emphasize this.
这只是为了突出我们已经知道的某件事，但在这里，你们确实有一个具体的例子，来进一步强调这一点。
   - Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 25–25, absolute 4867.20–4874.92s；Unprompted Whisper medium.en raw: chunk-028, segments 3–5, absolute 4861.34–4886.14s
   - 限制：恢复just、indeed、further，保留concrete example前缺冠词的口语语法；历史165/167跨段实际同一句，不额外重复here you have indeed。
22. That is, we now know more or less how the basic version of Wi-Fi works.
也就是说，我们现在或多或少知道Wi-Fi的基本版本是如何工作的。
   - Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 5–6, absolute 4878.50–4893.94s
23. We already said that Wi-Fi is so successful because it works quite well for our needs.
我们已经说过，Wi-Fi如此成功，是因为它能相当好地满足我们的需求。
   - Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 6–7, absolute 4886.14–4897.34s
24. But it has got a big problem in general, that is overhead, right?
但总的来说，它有一个大问题，那就是开销，对吧？
   - Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 8–9, absolute 4897.98–4904.22s
25. We already commented on that.
我们已经就此作过评论。
   - Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 10–10, absolute 4904.28–4906.22s
26. So now that we know how channel is used in Wi-Fi, this is a practical example that gives evidence to that.
所以，既然我们现在知道在Wi-Fi中信道是怎样被使用的，这就是为这一点提供证据的一个实际例子。
   - Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 11–12, absolute 4906.62–4917.88s
   - 限制：保留how channel的口语缺冠词，不补the；止于4917.88秒，不吞入下一段So we know that。

### 待听辨记录

- 4781.04–4810.36s omitted passage
  - 候选：历史Feishu与Qwen的成功发送／强制post-backoff／long break提问 / medium只有once you complete a后即跳到Oh sorry
  - 证据：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 13–14, absolute 4781.04–4815.20s
  - 处理：用历史和旧Qwen恢复候选，逐句标注新medium缺失；不声称已听音确认。
- Our time [three five, five plus three; numbers unclear]
  - 候选：three five, five plus three (三类文字碎片) / 实际数字、单位、含义及说话人归属未核实
  - 证据：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 14–14, absolute 4810.36–4815.20s
  - 处理：仅记录碎片，不推断钟点或课间长度；about fifteen minutes保留为另句，不和碎片拼算。
- We cannot do [anything otherwise / any, any number one unclear]
  - 候选：anything otherwise (Feishu) / any any number one (Qwen) / medium缺失
  - 证据：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
  - 处理：真实词仍不明，不用we cannot do otherwise的润色句掩盖。
- minor repetitions and alternatives
  - 候选：its its / its / of of / of / a few / few / it / you / with respect / respect / right / okay / that's it's that's / that's that's / we we / we / No / Oh / get it wrong / get this one wrong / did something wrong / the the / the / in in / in / the / these / in these in these / in these
  - 证据：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 5–25, absolute 4699.64–4874.92s；Unprompted Whisper medium.en raw: chunk-028, segments 1–12, absolute 4845.00–4917.88s
  - 处理：每个对应词组已在句内括注并注明局部证据；不把重叠窗的重复当口语重复。

## 67 · 01:21:58

稳定块ID：doxcnZ562lYsPjFnhaKLUa6k3pf
写回前应验证原块SHA256：a0d2961fffd810c43a87db58b23ef582d1e3694d4f638989fa738150e3567cf0

### 具体修改

1. When we need to transmit a data packet, first we sense the channel for DIFS. We can consider DIFS to be fifty microseconds long. That is certainly time we need to wait. → So we know that in the case where we need to transmit [the / a unclear] data packet, first of all we need to sense the channel for DIFS. We can consider [DIFS / this unclear] to be fifty microseconds long. So that's for sure something that we need to wait for.
   - 理由：恢复So we know that in the case where、first of all we need to、So that's for sure something ... for；冠词及DIFS/this不强选。
   - 来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 13–15, absolute 4918.14–4931.74s；Unprompted Whisper medium.en raw: chunk-028, segments 15–16, absolute 4923.16–4938.60s；Unprompted Whisper medium.en raw: chunk-028, segments 16–16, absolute 4931.74–4938.60s
2. If we are lucky, if we are lucky, the channel is idle and we can transmit our packet right away. But the packet has headers. → Then if we are lucky, if we are lucky, the channel is idle, and we can transmit our packet right away. But the packet that we transmit, we [know already / already know unclear] that [it unclear] has got some headers, right?
   - 理由：恢复Then及But the packet that we transmit整句、we know already、has got some和right，不摘要替代句子；know/already词序和it待听辨。
   - 来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 16–18, absolute 4931.74–4953.50s；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 18–19, absolute 4946.42–4958.94s
3. We already said it has a physical-layer preamble used by transmitter and receiver to synchronize, so the receiver can start demodulating what the transmitter sends. At the electronics level, they need this preamble to start the communication. → Actually, we already said it has got a physical layer preamble that is used by the transmitter and receiver to essentially synchronize, and so that the receiver can start [to unclear] demodulating what the transmitter is sending. So at the electronics level, they need this preamble to start the, [the, let's see unclear] communication.
   - 理由：恢复Actually、has got、that is used、essentially、and so that、is sending进行时、So；标出历史start to demodulating和Qwen独有the the let's see。
   - 来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 19–22, absolute 4953.50–4982.90s；Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Unprompted Whisper medium.en raw: chunk-028, segments 22–22, absolute 4971.46–4982.90s
4. Then there is the physical-layer header, and then the physical—sorry, the MAC-layer header, where, for example, we have the Duration field. All these headers are just control information. They are not the payload. → And then there is the physical layer header, and then there is the physical, sorry, the MAC layer header, where we have, for example, the duration field. So all these headers are just control information. It's not [a / the unclear] payload.
   - 理由：恢复And、第二次there is、原where we have for example词序、So及It's单数；a/the payload冲突不按标准英语选择。
   - 来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 23–24, absolute 4983.80–4995.74s；Unprompted Whisper medium.en raw: chunk-028, segments 25–25, absolute 4996.94–5004.04s
5. It's not something useful at the MAC layer. It is useful for the protocol, but these are not application-layer bits. They are there, fine, but from the application's perspective they are not useful or interesting. → It's not something useful at the MAC layer. It is something that is there. It is useful for the protocol, but not, they are not application layer bits, right? So [they are / you're unclear] there, fine, but from the application, from what would be the application layer perspective, that's something that is not useful, it's not interesting.
   - 理由：补回完全删掉的It is something that is there，恢复but not、they are、right、So及from the application自修长结构；保留MAC layer原技术说法，代词冲突待听辨。
   - 来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–26, absolute 4996.94–5012.44s；Unprompted Whisper medium.en raw: chunk-028, segments 26–26, absolute 5004.04–5012.44s；Unprompted Whisper medium.en raw: chunk-028, segments 26–27, absolute 5004.04–5020.40s；Unprompted Whisper medium.en raw: chunk-028, segments 27–29, absolute 5012.44–5033.84s；Unprompted Whisper medium.en raw: chunk-029, segments 1–1, absolute 5025.00–5033.86s

### 逐句证据

1. So we know that in the case where we need to transmit [the / a unclear] data packet, first of all we need to sense the channel for DIFS.
所以，我们知道，在我们需要发送[这个／一个，待听辨]数据包的情况下，首先我们需要侦听信道一个DIFS的时间。
   - Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 13–15, absolute 4918.14–4931.74s
   - 限制：历史及medium为the data packet，Qwen为a data packet；DIFS据历史dips及其他this近音规范，不压缩成When we need。
2. We can consider [DIFS / this unclear] to be fifty microseconds long.
我们可以认为[DIFS／这个，待听辨]持续五十微秒。
   - Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 15–16, absolute 4923.16–4938.60s
   - 限制：数字50三类均有，不引入其他制式数值；历史为dips，Qwen/medium为this，可能术语亦可能代词，保持词冲突。
3. So that's for sure something that we need to wait for.
所以，那肯定是我们需要等待的一段时间。
   - Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 16–16, absolute 4931.74–4938.60s
4. Then if we are lucky, if we are lucky, the channel is idle, and we can transmit our packet right away.
然后，如果我们幸运，如果我们幸运，信道是空闲的，我们就可以立即发送我们的数据包。
   - Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 16–18, absolute 4931.74–4953.50s
5. But the packet that we transmit, we [know already / already know unclear] that [it unclear] has got some headers, right?
但是，我们发送的这个数据包，我们[已经知道，know与already词序待听辨]，[it是否存在待听辨]它有一些首部，对吧？
   - Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 18–19, absolute 4946.42–4958.94s
   - 限制：历史we already know；Qwen44与medium we know already that has；Qwen45重叠为we know already that it has。不把两个重叠窗口拼接成重复发言。
6. Actually, we already said it has got a physical layer preamble that is used by the transmitter and receiver to essentially synchronize, and so that the receiver can start [to unclear] demodulating what the transmitter is sending.
实际上，我们已经说过，它有一个物理层前导码，由发送方和接收方用来基本上实现同步，并使接收方能够开始[to是否存在待听辨]解调发送方正在发送的内容。
   - Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 19–22, absolute 4953.50–4982.90s
   - 限制：恢复Actually、has got、essentially及and so that；历史start to demodulating，Qwen与medium start demodulating。transmitter is sending由Qwen明确识别，历史/medium尾部近音破碎，保留此候选并注明不是听音认证。
7. So at the electronics level, they need this preamble to start the, [the, let's see unclear] communication.
所以，在电子电路层面，它们需要这个前导码来开始这、[这，让我们看看，待听辨]通信。
   - Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 22–22, absolute 4971.46–4982.90s
   - 限制：Qwen独有the the let's see，历史及medium只一次the且无let's see；不将Qwen单源口头填充当已确认。
8. And then there is the physical layer header, and then there is the physical, sorry, the MAC layer header, where we have, for example, the duration field.
然后有物理层首部，接着有物理，抱歉，MAC层首部，其中我们有，例如，时长字段。
   - Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 23–24, absolute 4983.80–4995.74s
   - 限制：保留physical → sorry → MAC自修及两次and then there is；field在Qwen及medium明确，历史至duration。
9. So all these headers are just control information.
所以，所有这些首部都只是控制信息。
   - Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–25, absolute 4996.94–5004.04s
10. It's not [a / the unclear] payload.
它不是[一个／该，冠词待听辨]有效载荷。
   - Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–25, absolute 4996.94–5004.04s
   - 限制：历史the payload；Qwen与medium a payload。保留单数It's，不改成They。
11. It's not something useful at the MAC layer.
它不是在MAC层有用的东西。
   - Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–26, absolute 4996.94–5012.44s
   - 限制：讲者原话的MAC layer保留；不因其下一句讨论application layer而代改。
12. It is something that is there.
它是存在在那里的某种东西。
   - Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 26–26, absolute 5004.04–5012.44s
13. It is useful for the protocol, but not, they are not application layer bits, right?
它对协议是有用的，但不是，它们不是应用层的比特，对吧？
   - Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 26–27, absolute 5004.04–5020.40s
   - 限制：保留but not口语转折残片与right；没有补造主语these或删掉自修。
14. So [they are / you're unclear] there, fine, but from the application, from what would be the application layer perspective, that's something that is not useful, it's not interesting.
所以，[它们／你，待听辨]在那里，好吧，但从应用，从所谓的应用层角度来看，那是没有用的东西，是没有意思的东西。
   - Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 27–29, absolute 5012.44–5033.84s；Unprompted Whisper medium.en raw: chunk-029, segments 1–1, absolute 5025.00–5033.86s
   - 限制：历史they're there、Qwenthey are there，medium28 you're there；保留from the application → from what would be the application layer perspective自修和重复not，不压成application's perspective。medium29只是跨窗尾部，不额外拼接。

### 待听辨记录

- lexical and repetition conflicts
  - 候选：the / a data packet / DIFS / this / we know already / we already know / that it has / that has / start to demodulating / start demodulating / the the let's see communication / the communication / a / the payload / they are / you're
  - 证据：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 13–29, absolute 4918.14–5033.84s；Unprompted Whisper medium.en raw: chunk-029, segments 1–1, absolute 5025.00–5033.86s
  - 处理：相应句内全部明示，不以英语语法、来源数量或技术常识删除口语形式。
- It's not something useful at the MAC layer.
  - 候选：MAC layer (三类原文) / application layer (可能是技术上想表达的意思，但不是此句原词)
  - 证据：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–27, absolute 4996.94–5020.40s
  - 处理：讲者技术概括原样保留；解释用途时可另注，不修改原话。

## 68 · 01:23:51

稳定块ID：doxcnBiFI1L4BIG5iB170r9SIdd
写回前应验证原块SHA256：60eac5cf731d29b7215135bd8514d1e99aaff9df0aa9f04d543360bc750c844f

### 具体修改

1. We spend time transmitting this physical-layer preamble and header, and they are transmitted at the basic rate. → Okay. So, [but / when unclear] we spend time to transmit [this / these unclear] physical layer preamble, physical layer header, and they are transmitted at the basic rate.
   - 理由：恢复Okay、So but/when、spend time to transmit、physical layer header重复全称；this/these不强选。
   - 来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 29–31, absolute 5025.18–5047.42s；Unprompted Whisper medium.en raw: chunk-029, segments 1–3, absolute 5025.00–5047.80s
2. As we already commented, the basic rate is a low speed, so they are transmitted slowly. → So as we commented already, the basic rate is a low speed. So they are transmitted slowly at low speed.
   - 理由：恢复两次So、as we commented already原词序及被删除的at low speed，保留口语重复。
   - 来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 31–32, absolute 5040.56–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 3–4, absolute 5041.36–5057.02s；Unprompted Whisper medium.en raw: chunk-028, segments 32–32, absolute 5047.42–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 4–4, absolute 5047.80–5057.02s
3. If, as in this example, the basic rate is one megabit per second, you have to wait; this takes time. Then we have the MAC header. → And if you consider the basic rate, like in this example, to be one megabit per second, well then you have to wait; it takes time to do that. And then we have the MAC header.
   - 理由：恢复And if you consider、like in this example、to be、well then、it takes time to do that和And then，不压成客观陈述。
   - 来源：Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 4–6, absolute 5047.80–5074.76s；Unprompted Whisper medium.en raw: chunk-029, segments 6–6, absolute 5064.78–5074.76s

### 逐句证据

1. Okay.
好。
   - Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output
   - 限制：Okay在历史Feishu及Qwen45出现，新medium两窗均未转出。
2. So, [but / when unclear] we spend time to transmit [this / these unclear] physical layer preamble, physical layer header, and they are transmitted at the basic rate.
所以，[但是／当，待听辨]我们花时间来发送[这个／这些，待听辨]物理层前导码、物理层首部，而它们是以基本速率发送的。
   - Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 29–31, absolute 5025.18–5047.42s；Unprompted Whisper medium.en raw: chunk-029, segments 1–3, absolute 5025.00–5047.80s
   - 限制：历史/Qwen So but，medium两窗So when；历史these，Qwen/mediumthis。保留spend time to transmit及重复physical layer，不用流畅性强选。
3. So as we commented already, the basic rate is a low speed.
所以，正如我们已经评论过的，基本速率是一个低速率。
   - Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 31–32, absolute 5040.56–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 3–4, absolute 5041.36–5057.02s
4. So they are transmitted slowly at low speed.
所以，它们被慢慢地以低速率发送。
   - Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 32–32, absolute 5047.42–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 4–4, absolute 5047.80–5057.02s
   - 限制：恢复slowly及at low speed同义重复；at有历史及medium29明确支持，Qwen/medium28为a low speed近音，不当成重复发言。
5. And if you consider the basic rate, like in this example, to be one megabit per second, well then you have to wait; it takes time to do that.
而且，如果你认为基本速率，像这个例子中一样，是每秒一兆比特，那么，嗯，你就必须等待；做这件事需要时间。
   - Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 4–6, absolute 5047.80–5074.76s
   - 限制：历史Feishu本段止于low speed；此例及one megabit per second由Qwen45、46重叠及medium29支持，不把Qwen46截断A bit per second另算新句。
6. And then we have the MAC header.
然后我们还有MAC首部。
   - Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 6–6, absolute 5064.78–5074.76s
   - 限制：本句结束本段；其后The MAC header again are属于69段开头，避免Qwen45尾部或medium6跨段造成机械重复。

### 待听辨记录

- [but / when unclear]; [this / these unclear]
  - 候选：So but / So when / this physical layer preamble / these physical layer preamble
  - 证据：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 29–31, absolute 5025.18–5047.42s；Unprompted Whisper medium.en raw: chunk-029, segments 1–3, absolute 5025.00–5047.80s
  - 处理：连接词和指示词影响句法，留待听辨；不按两个重叠medium窗口的数量确定。

## 69 · 01:24:28

稳定块ID：doxcnaPSN6RL8HcSamaAISyuJqf
写回前应验证原块SHA256：47c0214dc5c65b426abe8c2f9335c70f9f329bb9bff182ee2009e7157e463002

### 具体修改

1. Again, the MAC header consists of uninteresting bits from the application's point of view. → The MAC header again are, [I would say / we say / it's a unclear] non-interesting bits from the point of view of the application.
   - 理由：撤销consists of语法修补及uninteresting同义替换，恢复The MAC header again are、non-interesting、from the point of view of the application；口头插入词三源冲突逐字保留。
   - 来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 6–7, absolute 5064.78–5079.76s
2. Its size in Wi-Fi may vary, depending, for example, on how many addresses you need. → The size of the MAC header in Wi-Fi may actually vary, depending on, for example, how many addresses you need.
   - 理由：恢复The size of the MAC header全称、actually及depending on, for example原词序。
   - 来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 7–9, absolute 5074.76–5094.32s
3. If you are in an isolated BSS, like the one in your apartment, the only addresses you need are the transmitter and receiver addresses. → So if you are in a BSS, isolated BSS, as the one that you have got in your apartment, the only addresses that you need are the transmitter address and [a unclear] receiver address.
   - 理由：恢复So、a BSS, isolated BSS重复、as the one that you have got、that及重复address；接收方地址前a待听辨，不改讲者两地址简化。
   - 来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 9–11, absolute 5086.80–5109.56s

### 逐句证据

1. The MAC header again are, [I would say / we say / it's a unclear] non-interesting bits from the point of view of the application.
MAC首部又是，[我会说／我们说／它是一个，待听辨]，从应用的角度来看没有意思的比特。
   - Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 6–7, absolute 5064.78–5079.76s
   - 限制：保留header are的讲者语法；历史we say，Qwenit's a，mediumI would say，均不可据语义强选；不润色成consists of uninteresting。
2. The size of the MAC header in Wi-Fi may actually vary, depending on, for example, how many addresses you need.
Wi-Fi中的MAC首部大小实际上可能会变化，这取决于，例如，你需要多少个地址。
   - Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 7–9, absolute 5074.76–5094.32s
   - 限制：MAC由历史/Qwen明确，mediummount为近音；保留actually、完整The size of the MAC header及on。
3. So if you are in a BSS, isolated BSS, as the one that you have got in your apartment, the only addresses that you need are the transmitter address and [a unclear] receiver address.
所以，如果你处在一个BSS中，一个孤立的BSS，就像你公寓里有的那一个，你需要的地址就只有发送方地址和[一个，a是否存在待听辨]接收方地址。
   - Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 9–11, absolute 5086.80–5109.56s
   - 限制：三类原始文本均写VSS，此处按既有稿BSS及basic/extended service set语境作B/V技术近音规范，不能视为音频确认。保留a BSS, isolated BSS重复和as the one；a receiver在历史及medium有，Qwen无，留待听辨。you've got/you have got仅缩合差异，以展开词形显示。讲者关于孤立BSS只需两地址的简化原样保留，不能暗改为规范地址数量。

### 待听辨记录

- [I would say / we say / it's a unclear]
  - 候选：we say (历史Feishu) / it's a (Qwen) / I would say (medium)
  - 证据：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 6–7, absolute 5064.78–5079.76s
  - 处理：保留header are，插入语待听辨，不因语法自然而选I would say。
- BSS / VSS; [a unclear] receiver address
  - 候选：VSS (三类原始文本) / BSS (技术近音规范候选，原校订已用) / a receiver address / receiver address
  - 证据：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 9–11, absolute 5086.80–5109.56s
  - 处理：BSS明确标为术语规范候选而非听音事实；如只做极严格音形保留，可改为[BSS / VSS unclear]。接收方地址前a在句内待听辨。
- the only addresses that you need are the transmitter address and [a unclear] receiver address
  - 候选：讲者的孤立BSS两地址表述 / 具体802.11帧地址用法需另行技术说明，不能拿来改写讲者
  - 证据：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 9–11, absolute 5086.80–5109.56s
  - 处理：保留讲者简化，另注技术问题；不把下一段If you are in an extended service set并入69。

## 70 · 01:25:04

稳定块ID：doxcne0VOVXpSN5fpm81zBk9gpc
写回前应验证原块SHA256：f8dcca481b3309a1847f05ff47868face47e35e768a11c7b046fb7e399786de0

### 具体修改

1. like on the Tongji campus → like here on Tongji campus [place-introduction wording unclear]
   - 理由：恢复地点引入词的可能措辞，不用现稿流畅表达替代；差异标疑。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5100–5121.72s
2. with many access points connected through the wired network → where we have many access points connected through, you know, the, the wired network
   - 理由：恢复where we have、you know和the,the重复。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46
3. The reason is that, in an extended service set, we may have access points connected to each other. → and the reason for that is that, in an extended service set, you may have, as we know, access points that are connected to each other, right?
   - 理由：恢复for that、you、as we know、that are、right及原长句结构。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5121.72–5150.32s

### 逐句证据

1. If you are in an extended service set, like here on Tongji campus [place-introduction wording unclear], where we have many access points connected through, you know, the, the wired network.
如果你处在一个扩展服务集里，就像这里的同济校园〔引出地点的措辞待听辨〕，这里我们有许多接入点，通过，你知道的，这个、这个有线网络连接起来。
   - Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5100.02–5121.72s
   - 限制：Tongji由Feishu与新medium支持；here on是新medium，Feishu your on、Qwen your Monton G近音不清。you know/the,the由Feishu与Qwen保留，新medium省略。
2. Then you may need four different addresses, and the reason for that is that, in an extended service set, you may have, as we know, access points that are connected to each other, right?
那么你可能需要四个不同的地址，而其原因是，在一个扩展服务集中，你可能有，正如我们所知道的，彼此连接的接入点，对吧？
   - Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5121.72–5150.32s
   - 限制：保留讲者关于四地址的解释；不在正文把它改写为标准适用范围说明。
3. We already explained the architecture of the network.
我们已经解释过这个网络的架构。
   - Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5142.28–5150.32s

### 待听辨记录

- here on Tongji campus
  - 候选：here on Tongji campus / your on tongji campus (Feishu near-sound) / your Monton G campus (Qwen near-sound)
  - 证据：新medium here on；旧两来源地点引入有近音
  - 处理：暂用新medium可读候选并显式标注，待听辨；非声学确认。

## 71 · 01:25:52

稳定块ID：doxcnq3VlLHsxPBYm8fqFaxRdCf
写回前应验证原块SHA256：ddfb6ba20961124445fa6aeda3f62f07121fdd3f880b7b8e5855c7d551c352d9

### 具体修改

1. You are A, and you want to send a packet to B. You send it to the access point you are connected to. → And so, if you are A and you want to send a packet to B, well, then you have to send your packet to the access point you are connected with.
   - 理由：恢复And so if条件、well/then、have to、your packet和with，不用简写send it。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5142–5167s
2. Access point one sends it to access point two, and access point two delivers it to B. → This access point one will send the packet to access point two, and then access point two will deliver the packet to B.
   - 理由：恢复This、两次will、then及重复the packet。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5160–5183s

### 逐句证据

1. And so, if you are A and you want to send a packet to B, well, then you have to send your packet to the access point you are connected with.
所以，如果你是A，并且你想把一个数据包发送给B，嗯，那么你必须把你的数据包发送给与你连接的那个接入点。
   - Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5142.28–5167.44s
2. This access point one will send the packet to access point two, and then access point two will deliver the packet to B.
这个接入点一会把这个数据包发送给接入点二，然后接入点二会把这个数据包递送给B。
   - Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5160.84–5183.18s
3. This happens in an extended service set.
这发生在一个扩展服务集中。
   - Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5173.86–5183.18s

### 待听辨记录


## 72 · 01:26:20

稳定块ID：doxcn57rutxrKFZjcBVeZsksgmf
写回前应验证原块SHA256：f930152bb48a96a38cb4b9b0ca850264d7101660ffe323f3fcd5e407f2706a38

### 具体修改

1. In this case A is the sender, the transmitter, so it is the original source and also the transmitter of the packet. → Okay, now in this case, A is the sender, okay, the transmitter
   - 理由：恢复Okay/now及原口语插语，the/your原始限定词冲突标疑。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 89；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5173–5200s
2. It has access point one's address as the receiver address, and B's address as the destination address. → You will have access point one address as a receiver, and then you will have the destination address, the B's address as destination address.
   - 理由：恢复You will have、then、重复destination address和原语法，不压成It has。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5219–5241s
3. Once the packet is received at access point one, that access point has to send it to access point two so that it eventually can be delivered to the final destination. → Once the packet is received at access point one, [and unclear] access point one has to send the packet to access point two, so that the packet eventually can be delivered to the final destination.
   - 理由：补句由旧Qwen和新medium支持；恢复重复名词，不替换为that access point/it；and异文标疑。
   - 来源：Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5241–5266s
4. Here the packet needs four addresses in the header. → This packet, when the packet is here, it [needs/means/names unclear] four addresses in the [MAC unclear] header.
   - 理由：恢复重复主语和when从句；动词及MAC冲突不靠标准表述裁定。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5259–5276s
5. The transmitter now is access point one, the receiver is access point two, and the final destination is B. → The transmitter now is access point one. The receiver now is access point two. And the final destination where this packet has to go is B, right?
   - 理由：恢复第二个now、where this packet has to go及尾问。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5276–5308s
6. Anyway, you already have to account for DIFS, the physical preamble, physical header, and MAC header. → Anyway, [um unclear], so you already have to account for [DIFS/SIFS unclear], physical preamble, physical header, MAC header.
   - 理由：恢复so与单源um疑点；DIFS/SIFS来源冲突不能按技术预期强选。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5327–5344s
7. The payload is the useful, interesting part, so it is not overhead. → The payload is the useful, interesting part. [Okay, so that's not overhead; wording unclear]
   - 理由：保留已支持的payload句，not overhead只有旧Qwen近音孤证，改为待听辨而非确认事实。
   - 来源：Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5337–5355s

### 逐句证据

1. Okay, now in this case, A is the sender, okay, the transmitter, so it's [the/your unclear] original source and also transmitter of the packet.
好，现在在这种情况下，A是发送方，好，发送机，所以它是〔the/your，限定词待听辨〕最初的源，同时也是这个数据包的发送方。
   - Feishu historical snapshot 08e6132, original source paragraph 89；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5173.86–5200.4s
   - 限制：Feishu your original source，Qwen与medium the original source；保留词级冲突，不因your不自然而去掉。Okay由原Feishu支持。
2. And access point one is the receiver, but the final destination is B.
而接入点一是接收方，但是最终目的地是B。
   - Feishu historical snapshot 08e6132, original source paragraph 89；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5191.68–5211.96s
3. So, this packet that travels from A to access point one will have A as the transmitter address, which is also the source's address.
所以，这个从A传到接入点一的数据包，会把A作为发送方地址，这同时也是源的地址。
   - Feishu historical snapshot 08e6132, original source paragraph 89；Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5200.4–5234.82s；new unprompted medium.en chunk-030, absolute 5205–5229.84s
4. You will have access point one address as a receiver, and then you will have the destination address, the B's address as destination address.
你会把接入点一的地址作为接收方地址，然后你会有目的地址，B的地址作为目的地址。
   - Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5219.4–5241.22s
   - 限制：保留as a receiver及the B’s的口语形式，不改成receiver address语法润色。
5. So it needs to have three addresses in the MAC header.
所以它需要在MAC首部中有三个地址。
   - Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5231.72–5252.1s
6. Once the packet is received at access point one, [and unclear] access point one has to send the packet to access point two, so that the packet eventually can be delivered to the final destination.
一旦这个数据包在接入点一被接收，〔and，连接词有无待听辨〕接入点一就必须把这个数据包发送给接入点二，这样这个数据包最终才能被递送到最终目的地。
   - Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5241.22–5266.76s
   - 限制：原Feishu前半句漏录；Qwen与medium补回，但medium有and、Qwen无，标疑。
7. This packet, when the packet is here, it [needs/means/names unclear] four addresses in the [MAC unclear] header.
这个数据包，当这个数据包在这里时，它〔needs/means/names，需要/意味着/说出，待听辨〕四个地址，在〔MAC有无待听辨〕首部里。
   - Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5259.4–5276.64s
   - 限制：Feishu it means four addresses in the header；Qwen it needs four addresses in the MAC header；medium it names four addresses in the MAC header。动词保留待听辨，MAC也记录F省略。
8. Why? Because we need to [specify/specifying unclear] that this packet originally came from source A.
为什么？因为我们需要〔specify/specifying，词形待听辨〕说明这个数据包最初来自源A。
   - Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5266.76–5287.6s
   - 限制：Feishu和Qwen specify，新medium specifying，不能仅为语法修掉来源词形差异。
9. The transmitter now is access point one. The receiver now is access point two. And the final destination where this packet has to go is B, right?
现在的发送方是接入点一。现在的接收方是接入点二。而这个数据包必须到达的最终目的地是B，对吧？
   - Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5276.64–5308.94s
10. So, in extended service sets, when the Wi-Fi packets travel from one access point to another, they need four addresses.
所以，在扩展服务集中，当Wi-Fi数据包从一个接入点传到另一个接入点时，它们需要四个地址。
   - Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5298.78–5318.12s
   - 限制：这是讲者说法，适用范围的技术简化不在讲稿正文中悄悄改正。
11. So this is just to say that the size of the MAC header may vary, okay, may be shorter or longer.
所以这只是要说明，MAC首部的大小可能变化，好，可能更短或者更长。
   - Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5318.12–5337.26s
12. Anyway, [um unclear], so you already have to account for [DIFS/SIFS unclear], physical preamble, physical header, MAC header.
总之，〔um，语气词有无待听辨〕，所以你已经必须把〔DIFS/SIFS待听辨〕、物理层前导码、物理层首部、MAC首部计算在内。
   - Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5327.7–5344.82s
   - 限制：Feishu与medium for this可近音DIFS，Qwen明确SIFS；不能仅凭协议正确值把讲者原话裁定为DIFS。um仅Qwen有。
13. The payload is the useful, interesting part. [Okay, so that's not overhead; wording unclear]
有效载荷是有用的、有意思的部分。〔好，所以那不是开销；此句措辞待听辨〕
   - Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5337.26–5355.3s
   - 限制：payload句Qwen+medium支持；not overhead只Qwen字面not over it，原Feishu缺、medium未出。旧稿将它当确定句，现保留疑句不能声称已确认。

### 待听辨记录

- [the/your unclear] original source
  - 候选：the original source / your original source
  - 证据：F your，Q+W the
  - 处理：候选中显式待听辨，不作声学确认。
- [and unclear] access point one
  - 候选：and access point one / access point one
  - 证据：W有and，Q无，F漏句
  - 处理：候选中显式待听辨，不作声学确认。
- [needs/means/names unclear]
  - 候选：needs / names / means
  - 证据：Q needs；W names；F means
  - 处理：候选中显式待听辨，不作声学确认。
- [MAC unclear] header
  - 候选：MAC header / header
  - 证据：Q+W有MAC，F无
  - 处理：候选中显式待听辨，不作声学确认。
- [specify/specifying unclear]
  - 候选：specify / specifying
  - 证据：F+Q specify，W specifying
  - 处理：候选中显式待听辨，不作声学确认。
- [um unclear]
  - 候选：um / 无语气词
  - 证据：Q单源um
  - 处理：候选中显式待听辨，不作声学确认。
- [DIFS/SIFS unclear]
  - 候选：DIFS / SIFS
  - 证据：F/W this近音，Q SIFS
  - 处理：候选中显式待听辨，不作声学确认。
- [Okay, so that's not overhead; wording unclear]
  - 候选：Okay, so that is not overhead / 旧Qwen not over it的其他可能
  - 证据：Q孤证not over it；F/W无此句
  - 处理：候选中显式待听辨，不作声学确认。

## 73 · 01:29:08

稳定块ID：doxcnoz4iNyPcVFzBZa9v02rNAb
写回前应验证原块SHA256：80040f79599fd97482d5f6ec76f1878712397936a08962c1a96b8700b96b41c7

### 具体修改

1. Then, if the packet is hopefully delivered successfully, in the best case, there is SIFS, another interval you have to wait for. → But then, if the packet is hopefully, so in the best case, delivered successfully, you have SIFS.
   - 理由：恢复But、so、you have和原词序；另一个时间间隔的潜在重说列为独立待听辨句。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5344–5367s
2. Then comes the acknowledgment, a control packet, so it is not interesting from the application's point of view. → And then acknowledgment, that is a control packet, so not interesting from the application point of view.
   - 理由：恢复原口语无主语结构及that is；不增comes/it is或所有格。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5360–5372s

### 逐句证据

1. But then, if the packet is hopefully, so in the best case, delivered successfully, you have SIFS.
但是然后，如果这个数据包，希望如此，所以是在最好的情况下，被成功递送了，你会有SIFS。
   - Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5344.82–5360.9s
   - 限制：SIFS由Qwen明确、F sips与medium sieves近音共同支持；保留hopefully/so在句中的位置。
2. That is [another time interval / another time you have ... interval; wording unclear] you have to wait for.
那是〔another time interval / another time you have ... interval，另一段时间间隔及可能的起句重说，待听辨〕，你必须等过的。
   - Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5355.3–5367.04s
   - 限制：Feishu another time you have interval you have to wait for；Qwen another time you are involved. You have to wait for；medium another time interval you have to wait for，不能靠顺语法把可能的重说删除。
3. And then acknowledgment, that is a control packet, so not interesting from the application point of view.
然后是确认，那是一个控制包，所以从应用的角度看并不有意思。
   - Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5360.9–5372.52s

### 待听辨记录

- another time ... interval
  - 候选：another time interval / another time you have interval / another time you are involved (Qwen near-sound)
  - 证据：三源在time与interval之间不一致，可能是自我修正，也可能ASR近音
  - 处理：整段小片语显式待听辨，不强行选择流畅表达。

## 74 · 01:29:30

稳定块ID：doxcnjlEVlqixKzyDteKtNUUyQb
写回前应验证原块SHA256：54af5b9fc922f707d762a3f7d55d006c65d0151c2ff1ef500eb2fcd7ea1f4d7d

### 具体修改

1. The acknowledgment again is made of a physical preamble, physical header, and MAC header, so there are lots of things to transmit. That is the best case. → And the acknowledgment again is made of physical preamble, physical header, MAC header, so lots of things to be transmitted. And that's the best case.
   - 理由：恢复And、原列表无额外冠词/and、无主语lots of things、被动to be transmitted和缩写that’s。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5367–5387s
2. To transmit the payload, you have to wait for DIFS, transmission of the physical-layer preamble, physical-layer header, and MAC header, then SIFS and then ACK. → So, you, to transmit the payload, you have to wait [DIFS/SIFS unclear], transmission of physical layer preamble, physical layer header, MAC header, and then SIFS, and then ACK.
   - 理由：恢复So you假起句及反复and then；不把DIFS按知识直接定词。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5380–5405s；new unprompted medium.en chunk-031, absolute 5385–5407s
3. Lots of time just to transmit the payload. → [Okay unclear], lots of time to just transmit [a/the/zero-article unclear] payload.
   - 理由：恢复to just词序；Okay和冠词来源不一，留明确标记。
   - 来源：Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395–5405s；new unprompted medium.en chunk-031, absolute 5400–5407s

### 逐句证据

1. And the acknowledgment again is made of physical preamble, physical header, MAC header, so lots of things to be transmitted. And that's the best case.
并且这个确认又由物理层前导码、物理层首部、MAC首部构成，所以有许多东西要传输。而且那还是最好的情况。
   - Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5367.04–5387.66s
2. So, you, to transmit the payload, you have to wait [DIFS/SIFS unclear], transmission of physical layer preamble, physical layer header, MAC header, and then SIFS, and then ACK.
所以，你，为了传输有效载荷，你必须等待〔DIFS/SIFS待听辨〕、物理层前导码的传输、物理层首部、MAC首部，然后是SIFS，然后是ACK。
   - Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5380.66–5405.34s；new unprompted medium.en chunk-031, absolute 5385–5407.16s
   - 限制：保留So you to transmit...you have to口语起句，不删除第一个you。发送前间隔F dewes、W dips/this，Q SIFS冲突；发送后SIFS/ACK由Qwen与新medium近音支持。
3. [Okay unclear], lots of time to just transmit [a/the/zero-article unclear] payload.
〔Okay有无待听辨〕，要用很多时间，就为了传输〔a/the/无冠词待听辨〕有效载荷。
   - Qwen recovery raw commit2887ed5, window 48；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395.66–5405.34s；new unprompted medium.en chunk-031, absolute 5400.72–5407.16s
   - 限制：Qwen有Okay和零冠词payload；medium chunk30为a payload、chunk31为the payload；Feishu尾部漏录。

### 待听辨记录

- wait [DIFS/SIFS unclear]
  - 候选：DIFS / SIFS
  - 证据：Feishu dewes、medium dips/this；Qwen SIFS
  - 处理：保留时间间隔疑点，不以协议常识代替声学证据。
- [Okay unclear]
  - 候选：Okay / 无Okay
  - 证据：Qwen48/49有Okay，Feishu漏尾，新medium无
  - 处理：保留口头语有无疑点。
- [a/the/zero-article unclear] payload
  - 候选：a payload / the payload / payload
  - 证据：medium chunk30=a、chunk31=the；Qwen=无冠词
  - 处理：相邻Whisper窗不当作两独立票；冠词待听辨。

## 75 · 01:30:04

稳定块ID：doxcnVIlMbRLnNFqo5tFGAYyaqh
写回前应验证原块SHA256：91b39d35bd0816ca0459ad5c6becf456b03d98747b825e55d292c29172a20fb6

### 具体修改

1. You had better have a long payload, because otherwise your protocol is very, very inefficient. → So you better have a long payload because otherwise your protocol is very, very inefficient, [okay unclear].
   - 理由：去掉旧编辑补的had，恢复So和来源中存在的Okay疑点。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395–5414s；new unprompted medium.en chunk-031, absolute 5400–5419s
2. If transmission fails and you have to perform backoff and retransmit the packet, you must wait for the channel to become idle: → If your transmission fails and you have to perform backoff and retransmit the packet, then you have to wait for the channel to become idle.
   - 理由：恢复your、then、have to，不以must替换原话。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5413–5424s
3. and hope the channel remains idle so that you can keep decreasing the backoff counter until it reaches zero. → Hope that the channel remains idle and you can decrease the backoff counter continuously and over time reach zero
   - 理由：恢复原祈愿开句及continuously and over time，不概括为keep/until。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5424–5437s
4. Lots of things, right, just to transmit a single payload again. → Lots of things, right? Just again to transmit a single [payload/failure unclear].
   - 理由：恢复原again词序；payload/failure是实质异文，不能凭语义选payload。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5437–5452s

### 逐句证据

1. So you better have a long payload because otherwise your protocol is very, very inefficient, [okay unclear].
所以你最好有一个长的有效载荷，因为否则你的协议就非常、非常低效，〔okay有无待听辨〕。
   - Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395.66–5414.82s；new unprompted medium.en chunk-031, absolute 5400.72–5419.92s
   - 限制：保留you better，不补had。Okay在Qwen与medium chunk31有，Feishu与chunk30无；口头语暂标疑。
2. And this is the best case. If your transmission fails and you have to perform backoff and retransmit the packet, then you have to wait for the channel to become idle.
而且这是最好的情况。如果你的传输失败了，并且你必须执行退避并重传这个数据包，那么你必须等待信道变为空闲。
   - Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5407.16–5424.14s
3. [DIFS/SIFS unclear], backoff time. Hope that the channel remains idle and you can decrease the backoff counter continuously and over time reach zero, and then transmit your packet, and then SIFS and ACK.
〔DIFS/SIFS待听辨〕，退避时间。希望信道保持空闲，而且你能够持续地递减退避计数器，并随着时间推移到达零，然后传输你的数据包，然后是SIFS和ACK。
   - Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5424.6–5445.16s
   - 限制：F Dips、medium This、Qwen SIFS；仍标疑，不按流程强改。其后continuously and over time三方有对应，恢复原措辞。
4. Lots of things, right? Just again to transmit a single [payload/failure unclear].
很多东西，对吧？仅仅又是为了传输一个〔payload/failure，有效载荷/失败，待听辨〕。
   - Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5437.66–5452.78s
   - 限制：Qwen payload，Feishu failure、新medium failure；不能单凭技术合理性把failure悄悄改为payload。

### 待听辨记录

- [okay unclear]
  - 候选：okay / 无okay
  - 证据：Qwen与medium31有；F与medium30无
  - 处理：显式保留有无待听辨。
- [DIFS/SIFS unclear]
  - 候选：DIFS / SIFS
  - 证据：F Dips、medium This、Qwen SIFS
  - 处理：不可按标准流程强行定字。
- single [payload/failure unclear]
  - 候选：payload / failure
  - 证据：Qwen payload；F及新medium failure
  - 处理：保留两种措辞候选，不以知识合理性覆盖。

## 76 · 01:30:46

稳定块ID：doxcnhiEoLg0Ehnqpu87QIE85Mf
写回前应验证原块SHA256：1ffb56b0ccf5487489937b8c6b5f6bd1c80efcb6ba8cac2069e2ae7715e8e5db

### 具体修改

1. We realize that Wi-Fi's efficiency is actually pretty low. → So, we [realize/realized unclear] that the efficiency of Wi-Fi is actually pretty low.
   - 理由：恢复So与the efficiency of Wi-Fi词序，不把ASR时态差异统一成现在时。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5445–5452s
2. Unfortunately this holds for all versions of Wi-Fi. → And this holds, unfortunately, for all versions of Wi-Fi.
   - 理由：恢复And及unfortunately原位置。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453–5461s
3. We looked at the basic version, but it is a curse for all versions. → Okay, we [looked / are looking / have looked unclear] at the basic version, but it's actually a curse for all versions.
   - 理由：恢复Okay、actually和it’s；三种时态不靠语法判断强选。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453–5470s
4. On average, you can consider this scheme's efficiency to be about fifty to fifty-five percent, which is definitely low. → And on average, you can consider that the efficiency of this scheme is about fifty, fifty-five percent, which is definitely low, right?
   - 理由：恢复And、that从句、of结构、原数字表达及尾问；不借听校修正讲者效率估计。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5461–5481s
5. Maximum efficiency would be one hundred percent. So, yeah, hopefully. → The maximum efficiency [would/will unclear] be one hundred percent. [So, yeah, hopefully / so, we are halfway; unclear]
   - 理由：恢复The，明确would/will与hopefully/halfway两处来源冲突。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5470–5490s

### 逐句证据

1. So, we [realize/realized unclear] that the efficiency of Wi-Fi is actually pretty low.
所以，我们〔realize/realized，时态待听辨〕认识到，Wi-Fi的效率实际上相当低。
   - Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5445.16–5452.78s
   - 限制：F与Qwen realize，新medium realized，保留时态冲突。
2. And this holds, unfortunately, for all versions of Wi-Fi.
而且不幸的是，这对所有版本的Wi-Fi都成立。
   - Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453.5–5461.3s
   - 限制：这是讲者泛化说法，未替换为技术上更严谨的范围表述。
3. Okay, we [looked / are looking / have looked unclear] at the basic version, but it's actually a curse for all versions.
好，我们〔looked/are looking/have looked，时态待听辨〕看的是基础版本，但是它实际上是所有版本的一个诅咒。
   - Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453.5–5470.46s
   - 限制：F looked；Q are looking；W have looked，不能任意统一时态。
4. And on average, you can consider that the efficiency of this scheme is about fifty, fifty-five percent, which is definitely low, right?
而且平均来看，你可以认为这个方案的效率大约是百分之五十、五十五，这确实很低，对吧？
   - Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5461.3–5481.06s
   - 限制：保留讲者百分数估计；来源没有可靠独立to词，按原相邻数字记录，不添加更高精度或适用性结论。
5. The maximum efficiency [would/will unclear] be one hundred percent.
最高效率〔would/will，情态或时态待听辨〕是百分之百。
   - Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5470.46–5490.18s
   - 限制：F would，Qwen与W will，词级待听辨。
6. [So, yeah, hopefully / so, we are halfway; unclear]
〔So, yeah, hopefully / so, we are halfway，所以，是的，希望如此／所以，我们到了一半；待听辨〕
   - Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5481.06–5490.18s
   - 限制：旧两源yeah hopefully，新medium we are halfway；语义不同，不能因50%上下文而强行选halfway，也不能把旧稿hopefully当已证原话。

### 待听辨记录

- realize/realized
  - 候选：realize / realized
  - 证据：F/Q realize，W realized
  - 处理：显式保留待听辨，不能以更合理语义或模型票数强选。
- looked/are looking/have looked
  - 候选：looked / are looking / have looked
  - 证据：F looked，Q are looking，W have looked
  - 处理：显式保留待听辨，不能以更合理语义或模型票数强选。
- would/will
  - 候选：would / will
  - 证据：F would，Q/W will
  - 处理：显式保留待听辨，不能以更合理语义或模型票数强选。
- hopefully/halfway
  - 候选：So, yeah, hopefully / So, we are halfway
  - 证据：F/Q hopefully，W halfway
  - 处理：显式保留待听辨，不能以更合理语义或模型票数强选。

## 77 · 01:31:25

稳定块ID：doxcnwoEYTymZ16TQtbNWfHjjff
写回前应验证原块SHA256：329e1098915d700ccac9cb1d5a5147c606804f6c3f83d6e66b731a1944c0d704

### 具体修改

1. That said, we are missing just one last mechanism in Wi-Fi channel access, → Okay, that said, we are just missing one last mechanism in the Wi-Fi channel access,
   - 理由：恢复Okay、are just missing词序和the；不改为更顺的叙述。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 96；Qwen recovery raw commit2887ed5, window 49；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5481–5509s
2. We just need to introduce it, and we will do that after the break: this last piece of the protocol, related to something we already know about, the famous four interframe spaces, the extended IFS. → Okay, so we just [need/needed unclear] to introduce, and we do that after the break, this last piece [for ... unclear] of the protocol that is related to what, actually, something that we know already about, the famous [four/for/form unclear] interframe space, the extended IFS.
   - 理由：恢复Okay/so、原省略宾语、do时态、what actually、know already词序与space单数；不保留编辑增补it/will。need/needed及起句介词冲突标疑。 famous后原Feishu for、Qwen50 four、medium031 segment18 form近音不稳，补显式待听辨；不定译四个。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 96；Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5500–5528s
3. Remember the extended IFS and the priority ladder: SIFS, PIFS, DIFS, and extended IFS. → Remember the extended IFS. Remember the priority ladder, we have SIFS, PIFS, [DIFS/PIFS unclear], and extended IFS.
   - 理由：恢复两次Remember与we have；列表部分漏识/近音冲突不按标准顺序无标记补齐。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5528–5551s
4. We said we would first focus on SIFS and DIFS and understand how they are used, then return to the other timing intervals. → So, we [said/start unclear], let's first focus on SIFS and [DIFS/PIFS unclear], understand how they are used, and then we'll go back to the other [time/timing unclear] intervals.
   - 理由：恢复So、let’s命令结构、we’ll go back原措辞，不改would/return；源词冲突保留。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5537–5555s
5. Now it is time to talk about the longest of these intervals, the extended IFS. → So, now it's time to talk about the longest among these [time/timing unclear] intervals. That was indeed the extended IFS.
   - 理由：恢复So、among、完整That was indeed句及过去式，非同位语压缩。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5556–5566s
6. To give you an idea, it can be as long as about three hundred microseconds, so it is definitely longer than the others we have considered. → And just to give you an idea, this extended IFS, [so/or unclear] this [time/timing unclear] interval, can be as long as about three hundred microseconds, so definitely longer than the others that we have considered so far.
   - 理由：恢复And/just、重复this extended IFS/time interval、that与so far；不补it is；so/or待听辨。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5566–5594s；new unprompted medium.en chunk-032, absolute 5565–5594s

### 逐句证据

1. Okay, that said, we are just missing one last mechanism in the Wi-Fi channel access, and then we are done with the basic version of Wi-Fi, that is the most important one.
好，说到这里，我们在Wi-Fi信道接入中就只剩最后一个机制还没有讲，然后我们就讲完Wi-Fi的基础版本了，那是最重要的一个版本。
   - Feishu historical snapshot 08e6132, original source paragraph 96；Qwen recovery raw commit2887ed5, window 49；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5481.06–5509.24s
   - 限制：Qwen49尾部but it is，Qwen50/F/medium that is；此候选按相邻更完整窗口及F保留that is，不新增which从句。
2. Okay, so we just [need/needed unclear] to introduce, and we do that after the break, this last piece [for ... unclear] of the protocol that is related to what, actually, something that we know already about, the famous [four/for/form unclear] interframe space, the extended IFS.
好，所以我们只是〔need/needed，时态待听辨〕需要介绍，而且我们在休息之后来做这件事，这最后一部分〔for，起句词有无待听辨〕协议，它关联到什么，实际上，关联到我们已经知道的一些东西，那著名的〔four/for/form，确切措辞待听辨〕帧间间隔，扩展IFS。
   - Feishu historical snapshot 08e6132, original source paragraph 96；Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 49；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5500.96–5528.54s
   - 限制：保留introduce后缺宾语、what actually与singular space；F last piece for.Of，Q/W last piece of，介词可能是假起句，标疑；W needed，F/Q need。 原Feishu为for、Qwen50为four、medium031 segment18为form；不按协议知识强定four或fourth，正文显式待听辨。
3. Remember the extended IFS. Remember the priority ladder, we have SIFS, PIFS, [DIFS/PIFS unclear], and extended IFS.
记住扩展IFS。记住这个优先级阶梯，我们有SIFS、PIFS、〔DIFS/PIFS待听辨〕，还有扩展IFS。
   - Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5528.54–5551.26s
   - 限制：F sieves/peeves/diffs/extended，Q50 SIFS/PIFS/PIFS/extended，Qtail漏一项，新medium此列表漏录。可恢复四项框架，但第三项必须暴露来源差异。
4. So, we [said/start unclear], let's first focus on SIFS and [DIFS/PIFS unclear], understand how they are used, and then we'll go back to the other [time/timing unclear] intervals.
所以，我们〔said/start，确切措辞待听辨〕，我们先关注SIFS和〔DIFS/PIFS待听辨〕，理解它们是怎样使用的，然后我们再回到其他的〔time/timing，时间修饰词待听辨〕间隔。
   - Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5537.1–5555.02s
   - 限制：F said let’s first focus on sieves/diffs，Q50 start last first ...SIFS/PIFS，Qtail start let’s first ...SIFS/PIFS；medium we said let’s first...sieves/dieves。句首和第二种IFS均标疑，不按优先级知识强定。
5. So, now it's time to talk about the longest among these [time/timing unclear] intervals. That was indeed the extended IFS.
所以，现在到了讨论这些〔time/timing，时间修饰词待听辨〕间隔中最长的那个的时候了。那确实就是扩展IFS。
   - Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5556.04–5566.22s；new unprompted medium.en chunk-032, absolute 5565–5576.72s
   - 限制：保留原that was indeed过去式，不改is或同位语；time/timing因Q主窗与tail/新ASR不同保留。
6. And just to give you an idea, this extended IFS, [so/or unclear] this [time/timing unclear] interval, can be as long as about three hundred microseconds, so definitely longer than the others that we have considered so far.
而且，只是为了让你有个概念，这个扩展IFS，〔so/or，所以/或者，待听辨〕这个〔time/timing，时间修饰词待听辨〕间隔，可以长到大约三百微秒，所以肯定比我们到目前为止考虑过的其他那些更长。
   - Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5566.22–5594.98s；new unprompted medium.en chunk-032, absolute 5565–5594.28s
   - 限制：so为F和Q50，or为Qtail及medium两窗；保留this extended IFS重复，不压成it；300微秒三方明确，适用版本限定在下段。

### 待听辨记录

- need/needed
  - 候选：need / needed
  - 证据：F/Q need；W needed
  - 处理：相关位置保留待听辨，不把标准说法或流畅语法当原话。
- last piece for/of
  - 候选：last piece for ... of / last piece of
  - 证据：F for.Of；Q/W of
  - 处理：相关位置保留待听辨，不把标准说法或流畅语法当原话。
- priority ladder third IFS
  - 候选：DIFS / PIFS
  - 证据：F diffs；Q50 PIFS重复；Qtail和新medium缺项
  - 处理：相关位置保留待听辨，不把标准说法或流畅语法当原话。
- we said/start let’s
  - 候选：we said let’s / we start let’s / we start last first (Qwen near-sound)
  - 证据：F/W said；Q多窗start
  - 处理：相关位置保留待听辨，不把标准说法或流畅语法当原话。
- focus on SIFS and DIFS/PIFS
  - 候选：DIFS / PIFS
  - 证据：F diffs/W dieves；Q两窗PIFS
  - 处理：相关位置保留待听辨，不把标准说法或流畅语法当原话。
- time/timing intervals
  - 候选：time intervals / timing intervals
  - 证据：Q主窗time、tail timing；F有time和timing；W近音tummy
  - 处理：相关位置保留待听辨，不把标准说法或流畅语法当原话。
- so/or this time interval
  - 候选：so / or
  - 证据：F/Q50 so；Qtail/W or
  - 处理：相关位置保留待听辨，不把标准说法或流畅语法当原话。
- famous four/for/form interframe space
  - 候选：four / for / form
  - 证据：Feishu source paragraph97: the famous for interframe space; Qwen window50: The famous four interframe space; medium chunk031 segment18 absolute5519.40–5528.54: the famous form in the frame space.
  - 处理：补正文英中显式疑点；fourth不是已识别候选，不凭协议语义强定四个或第四。

## 78 · 01:33:12

稳定块ID：doxcnH3EBc16mt3kuRZNdO8FJpe
写回前应验证原块SHA256：9f2eab41bdab1b95b846093fbb6d2e0a73378114bd71708b947a6c20878088c1

### 具体修改

1. It depends on the version of Wi-Fi we consider, but to keep an approximate figure in mind, you can consider it equal to three hundred microseconds. → Okay, it depends on the version of Wi-Fi that we consider, but just [yeah / you know / no filler; unclear], to keep in mind, again, [you can be considered; subject/construction unclear] equal to three hundred microseconds.
   - 理由：恢复Okay/that/just/again及三方原口语you can be considered；删去旧稿无来源的approximate figure和主语语法改写；语气词冲突标疑。 多源相同仍不能排除共同ASR误识，主语/句式补正文显式待听辨，不擅改it。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5586–5616s
2. Just to have an idea. → [Okay unclear], so just to [have an idea / verify / evaluate; unclear].
   - 理由：恢复可能Okay/so；have an idea并非一致结果，全文保留精确片语冲突。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603–5616s
3. If I'm not wrong, we now stop for twenty-five minutes. Okay. → So if I'm not wrong, now we stop for twenty-five minutes. Okay.
   - 理由：恢复So及now原词序；不改动三源共同的25分钟。
   - 来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603–5616s

### 逐句证据

1. Okay, it depends on the version of Wi-Fi that we consider, but just [yeah / you know / no filler; unclear], to keep in mind, again, [you can be considered; subject/construction unclear] equal to three hundred microseconds.
好，这取决于我们考虑的是Wi-Fi的哪个版本，但是只是〔yeah / you know / 无语气词；待听辨〕，为了记在心里，再说一次，〔你可以被认为；主语/句式待听辨〕等于三百微秒。
   - Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5586.7–5616.34s
   - 限制：原Feishu justyeah，Qwen just you know，新medium just to keep in mind；保留you can be considered这一三方共有但不自然的口语，不改成you can consider it。中文逐字保留主语以免替讲者修理；其意思或转写仍需回听。 即使多源表面一致，you can be considered主语/句式仍可能共同识别错误；正文英中同步标疑，不擅自改为it。
2. [Okay unclear], so just to [have an idea / verify / evaluate; unclear].
〔Okay有无待听辨〕，所以只是为了〔have an idea / verify / evaluate，有个概念/核实/评估，待听辨〕。
   - Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603.2–5616.34s
   - 限制：F So just to后残缺；Q50 verify、Q51及tail have an idea、W evaluate。旧稿选have an idea不应当作已确认。
3. So if I'm not wrong, now we stop for twenty-five minutes. Okay.
所以，如果我没有记错，现在我们停二十五分钟。好。
   - Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603.2–5616.34s
   - 限制：twenty-five三源对应一致；尾Okay来自F及Q50/tail，新medium未转出。不用前文其他课间安排猜测替换25。

### 待听辨记录

- but just yeah/you know/no filler
  - 候选：just yeah / just you know / just (无语气词)
  - 证据：F yeah，Q50/tail you know，W无
  - 处理：保留语气词是否出现及其措辞待听辨。
- Okay, so just to ...
  - 候选：have an idea / verify / evaluate / Feishu句尾缺失
  - 证据：Q51/tail have an idea、Q50 verify、W evaluate；F残缺
  - 处理：不选择旧稿最顺候选，明确列待听辨。
- you can be considered equal
  - 候选：you can be considered equal (三方文本) / you can consider it equal (旧校订)
  - 证据：F/Q/W均近似you can be considered equal，旧稿改为you can consider it equal
  - 处理：保留三方表面词串但用正文英中括号明确主语/句式待听辨；不擅改it，不标为完成音证。

