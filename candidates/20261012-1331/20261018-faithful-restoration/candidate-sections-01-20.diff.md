# 第01–20段独立修改记录

状态：候选，不是已确认逐字稿。所有变更均相对现飞书检查点，不修改远端。技术近音修复、恢复旧删改与仍待听辨的候选分别说明；不把机器差异数当错误数。

## 01 · 00:00:03

稳定块ID：doxcnYwPV6wJgi1S8geP75FfU5g
写回前应验证原块SHA256：5242993c1dac372666483c15471c0df8dd13546fb41c146d2496435c2d24271a

### 具体修改

1. a Wi-Fi node → [a/the unclear] Wi-Fi node
   - 理由：旧稿为a，Feishu与新Whisper为the，Qwen为a；不按二比一决定原词，正文保留冠词待听辨。
   - 来源：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
2. because it has to retransmit a packet that failed → because this node has to retransmit [a/the unclear] packet that failed
   - 理由：三方都支持this node，旧校订以it替代了原来的重复名词；packet冠词有冲突，不擅定。
   - 来源：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
3. this node will perform the backoff procedure. → then this node will perform the backoff procedure.
   - 理由：恢复三方都有的then。
   - 来源：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）

### 逐句证据

1. And we said that whenever [a/the unclear] Wi-Fi node needs to recontend for the channel, because this node has to retransmit [a/the unclear] packet that failed, then this node will perform the backoff procedure.
而且我们说过，每当[一个/这个待听辨] Wi-Fi 节点需要重新竞争信道，因为这个节点必须重新发送[一个/这个待听辨]发送失败的数据包，那么这个节点就会执行退避过程。
   - Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
   - 限制：Wi-Fi node前Qwen为a，Feishu与新Whisper为the；packet前Qwen为a，新Whisper为the，Feishu断句处无冠词。两处均待听辨。 新Whisper的reclassmate、bake-off仅按Feishu/Qwen共同支持的明确技术近音规范为retransmit、backoff。

### 待听辨记录

- [a/the unclear] packet
  - 候选：a packet / the packet / packet（无冠词）
  - 证据：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）: retransmit.Packet；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）: retransmit a packet；新无提示Whisper medium.en chunk-001, segment=2 word, absolute=20.52–21.12s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）: the
  - 处理：保留[a/the unclear]，中文同步待听辨；不能凭语法或新ASR单方决定。
- [a/the unclear] Wi-Fi node
  - 候选：the Wi-Fi node / a Wi-Fi node
  - 证据：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）: the Wi-Fi node；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）: a Wi-Fi node；新无提示Whisper medium.en chunk-001, segment=1 word, absolute=8.3–10.66s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）: the Wi-Fi node
  - 处理：正文保留[a/the unclear]及中文待听辨，不按二比一决定冠词。
- 00:00:00–00:00:03开头
  - 候选：We start to see this ... / I want you to stop to see the reports ...
  - 证据：Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）: We start to see this, and we send them.；新无提示Whisper medium.en chunk-001, segment=1, absolute=0–3.02s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）: I want you to stop to see the reports；Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）: 起于And we said
  - 处理：此片语在当前01锚点之前，三方无法核实；未把任一新旧ASR片语硬塞进01，需单独听辨开头。

## 02 · 00:00:29

稳定块ID：doxcn7SsOH6o33jPzXgM5V6cyXd
写回前应验证原块SHA256：775578c71881795185e4a73cd7bff496718ffd04099f8ce956ce907abb34eda9

### 具体修改

1. We explained how the backoff procedure works. First, → And we explained how the backoff procedure works. Okay? Now, we [said/send unclear] that first
   - 理由：恢复开头And、Okay与Now, we said that；旧稿删掉了讲者的连接和回指。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
2. Then it will draw an integer out of a range of possible values, selecting each of them with equal probability. → Then [it/you unclear] will draw an integer out of a range of possible values with equal probability, selecting each of them with equal probability.
   - 理由：恢复两遍with equal probability；三方都支持这次重复，不把第二分句当多余。代词冲突另留标记。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
3. This range goes from zero to the contention window parameter. → And this range of values goes from zero to the contention window parameter, okay?
   - 理由：恢复And、of values和okay。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
4. we set this parameter to its minimum value. → we set this contention window parameter to its minimum value.
   - 理由：恢复重复说出的contention window，不用this parameter概括。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
5. If we need to perform backoff again to transmit this packet → And then, if we need to perform the backoff procedure again in order to transmit this packet
   - 理由：恢复And then、the backoff procedure、in order to的完整措辞。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
6. every time we increase the contention window. → every time we will increase the value of contention window.
   - 理由：恢复will及the value of，保留原口语结构。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
7. We said that, roughly speaking, this value doubles every time. → And we said, roughly speaking, this value of contention window doubles every time, right?
   - 理由：恢复And、of contention window与right；Feishu此句不全，完整后半由Qwen和新Whisper补足。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=11–12, absolute=116.56–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
8. To be more precise, the relation according to which CW increases is the following. → Now, to be more precise, the relation according to which the CW parameter increases is the following.
   - 理由：恢复Now与the CW parameter。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
9. The CW value is expressed as a power of two minus one, where this exponent is called the backoff exponent. → So, CW value is actually expressed as a power of two minus one, where this exponent is called backoff exponent.
   - 理由：恢复So、actually及无the的backoff exponent；用相邻窗补出指数名，不把新窗开头视为03内容。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1, absolute=165–178.2s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
10. First, a node needs to wait → Now, we [said/send unclear] that first a node needs to wait
   - 理由：Now, we said that由Feishu和新Whisper共同支持；Qwen的send为单来源异文，正文保留简洁待听辨，不把两种候选等权或靠语法裁定。
   - 来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）

### 逐句证据

1. And we explained how the backoff procedure works.
而且我们解释过退避过程是怎样工作的。
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
2. Okay?
好吗？
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）
   - 限制：Okay在Feishu和Qwen中存在；新Whisper未转出，问号仅为书面断句。
3. Now, we [said/send unclear] that first a node needs to wait for the channel to be idle for DIFS.
现在，我们[“说过/发送”待听辨]，首先一个节点需要等待信道空闲一个 DIFS。
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
   - 限制：said有Feishu和新Whisper共同支持，send仅见Qwen；候选不是等可信。DIFS为技术近音候选：Feishu dips、Qwen this、新Whisper bifs；均未经听音认证。
4. Then [it/you unclear] will draw an integer out of a range of possible values with equal probability, selecting each of them with equal probability.
然后[它/你待听辨]会以相等的概率从一组可能的值中抽取一个整数，以相等的概率选择其中的每一个。
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
   - 限制：Feishu和Qwen为it，新Whisper为you；保留代词待听辨。
5. And this range of values goes from zero to the contention window parameter, okay?
而且这个取值范围从零到竞争窗口参数，好吗？
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
6. The first time that we use the backoff procedure to transmit a packet, we set this contention window parameter to its minimum value.
第一次我们使用退避过程来发送一个数据包时，我们把这个竞争窗口参数设为它的最小值。
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
7. And then, if we need to perform the backoff procedure again in order to transmit this packet, because, for example, we fail and fail and fail, every time we will increase the value of contention window.
然后，如果我们需要再次执行退避过程来发送这个数据包，因为，例如，我们失败、失败、再失败，每一次我们都会增大竞争窗口的值。
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
8. And we said, roughly speaking, this value of contention window doubles every time, right?
而且我们说过，粗略地说，竞争窗口的这个值每次都会翻倍，对吧？
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=11–12, absolute=116.56–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
9. Now, to be more precise, the relation according to which the CW parameter increases is the following.
现在，更准确地说，CW 参数据以增大的关系是下面这个。
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
10. So, CW value is actually expressed as a power of two minus one, where this exponent is called backoff exponent.
所以，CW 的值实际上表示为二的一个幂减一，其中这个指数叫作退避指数。
   - Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1, absolute=165–178.2s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   - 限制：Feishu在power of two处截断；minus one及backoff exponent由Qwen和新Whisper跨chunk-001/002互补，未把窗口重叠重复计入。

### 待听辨记录

- [it/you unclear] will draw
  - 候选：it will draw / you will draw
  - 证据：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）: it will draw；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）: it will draw；新无提示Whisper medium.en chunk-001, segment=5, absolute=51.1–64.12s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）: you will draw
  - 处理：保留[it/you unclear]及中文待听辨，不凭上下文将you改写成it。
- DIFS
  - 候选：DIFS（技术近音校正候选） / dips / this / bifs（来源字面）
  - 证据：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）: dips；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）: this；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）: bifs
  - 处理：按Wi-Fi信道空闲等待的术语近音暂写DIFS；记录尚无逐字听证，未添加continuous、一个完整时隙等解释。
- we [said/send unclear] that
  - 候选：said（Feishu与新Whisper共同支持） / send（仅Qwen）
  - 证据：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
  - 处理：正文保留待听辨；文字交叉支持较强的是said，尚未据音频裁定。

## 03 · 00:02:48

稳定块ID：doxcnUQ7t1Sai3ADMWsg75dZvye
写回前应验证原块SHA256：e959ab818f3cee68f0ecf47bcc72fa0d64e9bf72840bcab95d2a29801c18ffb1

### 具体修改

1. For example, the first time we use the backoff procedure for a data packet, we set the backoff exponent to its minimum. → Okay? So, for example, the first time that we use the backoff procedure for a data packet, we set the, so the first time, we set the backoff exponent to the backoff exponent minimum, okay?
   - 理由：恢复Okay、So、that、we set the的中断与so the first time的重新起句，恢复重复的backoff exponent及minimum位置；三方可交叉支持。
   - 来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=15–16, absolute=167.54–194.5s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
2. By default, in the early versions of Wi-Fi, this is equal to five. → Now, by default, in the early versions of Wi-Fi, this is equal to five, okay?
   - 理由：恢复Now和okay；不把新Whisper的phi phi/phi当成原词。
   - 来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
3. This example refers to the early versions of Wi-Fi. → This is an example that refers to the early versions of Wi-Fi, okay?
   - 理由：恢复This is an example that...和okay，撤回缩写句式。
   - 来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
4. If we take this example value, we see that → Now, so, if we take this example here, this example value here, we see that
   - 理由：恢复Now, so和this example here / this example value here两次指代及here。
   - 来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
5. Since this is five, it will be two to the five minus one, which is 31. → Since this is five, right, this will be two to the five minus one, which is 31, right?
   - 理由：恢复this而非it，并恢复两次right。
   - 来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
6. That is why on Saturday, when we introduced this procedure, we said: let's consider the minimum contention window 31. → So that's why, yes, on Saturday, when we [introduce/produce tense unclear] this procedure, we said, well, let's consider the minimum contention window 31, okay?
   - 理由：恢复So、yes、well与okay；词根/时态不一致，撤回未经证实的introduced，明确待听辨。
   - 来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=9–10, absolute=267.8–290.5s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
7. The second time we use backoff for the same packet, we are going to increase the backoff exponent. → Then, the second time that we use the backoff procedure for the same packet, we are going to increase the backoff exponent.
   - 理由：恢复Then、that及the backoff procedure。
   - 来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
8. If this was our first value, the second time we will have a second value equal to the previous one plus one. → So, if this was our first value, the second time, [sorry unclear], we'll have second value, right, that is equal to what, is equal to the previous one plus one.
   - 理由：恢复So、right及that is equal to what, is equal to重复；删除旧校订额外补入的a，不把second value改成标准语法。sorry列待听辨。
   - 来源：Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）

### 逐句证据

1. Okay?
好吗？
   - Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）
2. So, for example, the first time that we use the backoff procedure for a data packet, we set the, so the first time, we set the backoff exponent to the backoff exponent minimum, okay?
所以，例如，第一次我们对一个数据包使用退避过程时，我们设置这，所以第一次，我们把退避指数设为退避指数最小值，好吗？
   - Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=15–16, absolute=167.54–194.5s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
3. Now, by default, in the early versions of Wi-Fi, this is equal to five, okay?
现在，默认地，在早期版本的 Wi-Fi 中，这等于五，好吗？
   - Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
4. This is an example that refers to the early versions of Wi-Fi, okay?
这是一个指的是早期版本的 Wi-Fi 的例子，好吗？
   - Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
5. Now, so, if we take this example here, this example value here, we see that, as we said last time, the first time that we use this contention window minimum, the value will be two to the power of the minimum exponent minus one.
现在，所以，如果我们采用这里的这个例子，这里的这个示例值，我们看到，正如我们上次说过的，第一次我们使用这个竞争窗口最小值时，这个值会是二的最小指数次方减一。
   - Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   - 限制：Feishu的first time与Exponent之间缺文字；Qwen完整窗口和新Whisper共同补足that we use this contention window minimum, the value will be two to the power of the minimum。
6. Since this is five, right, this will be two to the five minus one, which is 31, right?
因为这是五，对吧，这会是二的五次方减一，也就是 31，对吧？
   - Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
7. So that's why, yes, on Saturday, when we [introduce/produce tense unclear] this procedure, we said, well, let's consider the minimum contention window 31, okay?
所以这就是为什么，是的，在星期六，当我们[“介绍/产生”及其时态待听辨]这个过程时，我们说，嗯，让我们考虑最小竞争窗口 31，好吗？
   - Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=9–10, absolute=267.8–290.5s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   - 限制：Feishu为introduce，Qwen为produced，新Whisper为produce；不能延用旧校订的introduced而掩盖词根与时态冲突。
8. Then, the second time that we use the backoff procedure for the same packet, we are going to increase the backoff exponent.
然后，第二次我们对同一个数据包使用退避过程时，我们要增大退避指数。
   - Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
9. So, if this was our first value, the second time, [sorry unclear], we'll have second value, right, that is equal to what, is equal to the previous one plus one.
所以，如果这是我们的第一个值，第二次，[“抱歉”待听辨]，我们会有第二个值，对吧，它等于什么，等于前一个值加一。
   - Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   - 限制：恢复that is equal to what, is equal to这一口语自问重述；sorry只有Feishu转出，不能静默删去或当作已证实。

### 待听辨记录

- [introduce/produce tense unclear]
  - 候选：introduce（Feishu） / produced（Qwen） / produce（新Whisper） / introduced（旧校订）
  - 证据：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）: when we introduce this procedure；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）: when we produced this procedure；新无提示Whisper medium.en chunk-002, segment=9 word, absolute=271.78–272.3s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）: produce
  - 处理：保留词根和时态待听辨；不以“上周六”或更合理的课堂语义擅自选择introduced。
- [sorry unclear]
  - 候选：sorry / 无sorry
  - 证据：Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）: the second time, sorry, we’ll have；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）: the second time, we’ll have；新无提示Whisper medium.en chunk-002, segment=12, absolute=299.84–312.78s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）: the second time we’ll have
  - 处理：保留[sorry unclear]，中文同步待听辨；不将Feishu孤证当确定口头语，也不静默丢弃。

## 04 · 00:05:24

稳定块ID：doxcnSFMtuDH3wqf3m1ZJ1FECpf
写回前应验证原块SHA256：ea085ff66e253445fc86e6a20532bcb984860b247441186bc99b8142c211359e

### 具体修改

1. This means that the second time we compute the contention window, it will equal → Okay? So this means that the second time that we have to compute the contention window, this will be equal to
   - 理由：恢复Okay、So、that we have to和this will be equal to，撤回缩写和代词替换。
   - 来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
2. two to the power of the backoff exponent at the second step, minus one. → two to the power of the, the backoff exponent [on/at unclear] the second step minus one,
   - 理由：恢复重复的the, the；原来源介词有on/at冲突，不沿用旧稿at。
   - 来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=1–2, absolute=345–360.66s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. This is two to the power of the exponent at the first step increased by one, minus one. → which is two to the backoff exponent [on/at unclear] the first step increased by one minus one, right?
   - 理由：恢复which is连接、backoff及right；移除原话未见的第二个power of，保留不规整的口头数学表述。
   - 来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=1–2, absolute=345–360.66s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）

### 逐句证据

1. Okay?
好吗？
   - Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
2. So this means that the second time that we have to compute the contention window, this will be equal to two to the power of the, the backoff exponent [on/at unclear] the second step minus one, which is two to the backoff exponent [on/at unclear] the first step increased by one minus one, right?
所以这意味着，第二次我们必须计算竞争窗口时，这会等于二的这个、这个[on/at 介词待听辨]第二步的退避指数次方减一，这就是二的“[on/at 介词待听辨]第一步的退避指数加一”次方减一，对吧？
   - Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=1–2, absolute=345–360.66s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   - 限制：on/at两处：Feishu及新Whisper为on，Qwen为at；留标记，不把口语介词统一。backoff为cost/Bechov/cot/cub的技术近音恢复；the, the有Feishu与Qwen共同支持。

### 待听辨记录

- [on/at unclear] the second step / the first step
  - 候选：on the second step; on the first step / at the second step; at the first step
  - 证据：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）: on the second step / on the first step；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）: at the second step / at the first step；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）: on the second step / on the first step；新无提示Whisper medium.en chunk-003, segment=1–2, absolute=345–360.66s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: on the second step / on the first step
  - 处理：两处均保留介词待听辨；共同语义不能证明准确介词。

## 05 · 00:06:01

稳定块ID：doxcn3oscwOg3HvqxY1TQD4dKfb
写回前应验证原块SHA256：13ba4eaae4467afea715f5223ef0d8f0ca36d1ec383951072f42648567c619f3

### 具体修改

1. In our example this is two to the power of six minus one, which is 63. → So now this is two to the power, in our example, to the power of six minus one, which is 63, okay?
   - 理由：恢复So now、this is的位置及两次to the power；不将口头中断合并成干净公式。
   - 来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=17, absolute=361.14–373.98s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. This is the way we increase the contention window minimum value every time until we reach CW_max. → So this is the way we increase the contention window minimum value every time till, as we said, we reach this value, CW max.
   - 理由：恢复So、till、as we said及this value；保留minimum value，即使技术上显得不严谨。
   - 来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. After reaching this value, we do not increase CW beyond it → After we reach this value, we do not increase [the/this unclear] CW value any longer [beyond/behind unclear] this value
   - 理由：恢复完整从句、CW value、any longer及再次说出的this value；the/this与beyond/behind来源冲突留待听辨，不用语义选词。
   - 来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
4. even if we still need to perform backoff for the same packet. → even if we need to still perform the backoff procedure for the same time.
   - 理由：恢复need to still的词序、the backoff procedure与三方一致的same time；不以技术语义把time改成packet。
   - 来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）

### 逐句证据

1. So now this is two to the power, in our example, to the power of six minus one, which is 63, okay?
所以现在这是二的次方，在我们的例子中，是六次方减一，也就是 63，好吗？
   - Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=17, absolute=361.14–373.98s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. So this is the way we increase the contention window minimum value every time till, as we said, we reach this value, CW max.
所以这就是我们每次增大竞争窗口最小值的方式，直到，正如我们说过的，我们达到这个值，CW max。
   - Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. After we reach this value, we do not increase [the/this unclear] CW value any longer [beyond/behind unclear] this value, even if we need to still perform the backoff procedure for the same time.
在我们达到这个值之后，我们不再把[限定词待听辨] CW 值增大到这个值的[以上/后面待听辨]，即使我们还需要为同一次执行退避过程。
   - Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   - 限制：三方均为for the same time，原词保留。CW前the/this及beyond/behind有文字冲突，正文留标记，不按多数或技术意义选择。

### 待听辨记录

- [the/this unclear] CW value / [beyond/behind unclear] this value
  - 候选：the CW value; beyond this value（Feishu、Qwen） / this CW value; behind this value（新Whisper）
  - 证据：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=5–6, absolute=388.08–412.12s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
  - 处理：正文保留两处标记及中文待听辨；不按二比一或语法选择the、beyond。
- for the same time
  - 候选：for the same time（三方一致） / for the same packet（仅旧校订）
  - 证据：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）: for the same time；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）: for the same time；新无提示Whisper medium.en chunk-003, segment=7, absolute=412.35–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: for the same time
  - 处理：恢复time；它在三方文字中没有冲突，不能仅因术语逻辑而改写成packet。仍属未听音候选。

## 06 · 00:06:57

稳定块ID：doxcn89Uuu4pPtyRwDp131FVbVb
写回前应验证原块SHA256：5aee0f606bcff550fd1172c8ff24858506cdbd756389748a54678e20ad886222

### 具体修改

1. The general rule is that → So, the general, [ah unclear] the general rule is that
   - 理由：恢复So和重复的the general；ah单来源留待听辨。
   - 来源：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=7–8, absolute=412.35–447.83s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. we set the backoff exponent equal to the exponent at the previous step increased by one. → we set the backoff exponent [at/as unclear] step i equal to the backoff exponent [at/and unclear] the previous step increased by one, right?
   - 理由：恢复at step i位置及第二遍backoff exponent、right；介词冲突不直接修成标准语法。
   - 来源：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=7–8, absolute=412.35–447.83s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）

### 逐句证据

1. So, the general, [ah unclear] the general rule is that at step i, the generic step i, we set the backoff exponent [at/as unclear] step i equal to the backoff exponent [at/and unclear] the previous step increased by one, right?
所以，一般的，[语气词待听辨]一般规则是，在第 i 步，任意的第 i 步，我们把[在/作为待听辨]第 i 步的退避指数设为[在/以及待听辨]前一步的退避指数增加一，对吧？
   - Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=7–8, absolute=412.35–447.83s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   - 限制：重复the general有Feishu与Qwen支持；ah仅Qwen转出。第一介词at/as、第二介词at/and分歧保留；不把来源不稳的口语语法悄悄规范化。

### 待听辨记录

- [ah unclear]
  - 候选：ah / 仅停顿/无词
  - 证据：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）: the general.The general；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）: the general ah the general；新无提示Whisper medium.en chunk-003, segment=7–8, absolute=412.35–447.83s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: the general rule（未转出重复）
  - 处理：两遍the general有双来源支持并恢复；语气词是否为ah待听辨。
- [at/as unclear] step i
  - 候选：at step i / as step i
  - 证据：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）: at step I；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）: at step i；新无提示Whisper medium.en chunk-003, segment=8 word, absolute=436.27–438.81s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: as step i
  - 处理：保留介词待听辨，不直接按公式语义纠成at。
- [at/and unclear] the previous step
  - 候选：at the previous step / and the previous step / And the view step（Feishu字面）
  - 证据：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）: And the view step；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）: at the previous step；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）: at the previous step；新无提示Whisper medium.en chunk-003, segment=8 word, absolute=442.41–444.41s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: and the previous step
  - 处理：previous由Qwen与新Whisper共同支持；at/and仍待听辨，不用语法替原声做决定。

## 07 · 00:07:28

稳定块ID：doxcnJ4V6DfRd4wtrg1ZLZ38BQd
写回前应验证原块SHA256：0544d3b629146ba8af5055fa7ae2bbdaaf7f407c0debd88b7836970453752be0

### 具体修改

1. At the generic step i, the contention window is computed → And at the generic step i, the contention window will be computed
   - 理由：恢复And与will be，保留原将来时。
   - 来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. This is the general expression used to compute the backoff exponent and the corresponding contention window at each step. → Okay, this is the general expression that we use to compute the, the backoff exponent and the corresponding contention window at each step.
   - 理由：恢复Okay、that we use及the, the重复；backoff是多次技术近音的统一拼写，不是改写句法。
   - 来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. Every time we need to perform backoff for a given data packet, we roughly double the contention window. → Okay, that said, therefore we understand that [every time/at every time unclear] that we need to perform the backoff for a given data packet, we roughly double the contention window, as we said.
   - 理由：恢复被删掉的Okay, that said, therefore we understand that、that、the及as we said；at分歧留待听辨。
   - 来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
4. We enlarge the possible integer values that we can draw to compute the backoff time. → Okay, so we are going to [enlarge/launch unclear] the possible values, integer values, that we can draw to compute [backoff repetition unclear] time.
   - 理由：恢复Okay, so、are going to及possible values, integer values的重复重述；backoff重复是否实说列待听辨。 enlarge有Feishu和新Whisper共同支持、launch仅为Qwen异文，正文另留待听辨。
   - 来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
5. Before explaining why the standard says to double the contention window every time we need to perform backoff to transmit a packet, let me mention something reported in one of the earlier slides. → Okay, so before explaining why we do that, okay, why the [standard said/standards say unclear] let's double the contention window every time we need to perform a backoff to transmit [a/the unclear] packet. So before explaining the reason because we do that, let me mention what was reported in one of the earlier slides.
   - 理由：撤回把两次before explaining压成一句的处理；恢复why we do that、第二个okay、let’s、the reason because we do that及what was reported；保留词法/时态冲突。
   - 来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=15–18, absolute=513.05–547.99s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=1–3, absolute=525–550.16s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）

### 逐句证据

1. And at the generic step i, the contention window will be computed as two to the power of the backoff exponent at step i minus one.
而且在任意的第 i 步，竞争窗口将被计算为二的第 i 步的退避指数次方减一。
   - Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. Okay, this is the general expression that we use to compute the, the backoff exponent and the corresponding contention window at each step.
好，这就是我们用来计算每一步的这个、这个退避指数和相应竞争窗口的一般表达式。
   - Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. Okay, that said, therefore we understand that [every time/at every time unclear] that we need to perform the backoff for a given data packet, we roughly double the contention window, as we said.
好，说到这里，因此我们明白，[“每一次”前介词待听辨]我们需要对一个给定的数据包执行退避时，我们大致把竞争窗口翻倍，正如我们说过的。
   - Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   - 限制：every time前是否有at：仅Qwen含at；保留词序待听辨。
4. Okay, so we are going to [enlarge/launch unclear] the possible values, integer values, that we can draw to compute [backoff repetition unclear] time.
好，所以我们要[“扩大/发起”待听辨]那些可能的值，整数值，我们可以抽取它们来计算[“退避”的重复待听辨]时间。
   - Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   - 限制：enlarge有Feishu和新Whisper共同支持，launch仅见Qwen，不表示两者等可信。Qwen另为the because the because time，另两来源未明确转出双重backoff；重复仍待听辨。
5. Okay, so before explaining why we do that, okay, why the [standard said/standards say unclear] let's double the contention window every time we need to perform a backoff to transmit [a/the unclear] packet.
好，所以在解释我们为什么这样做之前，好，为什么[“标准说”的单复数和时态待听辨]让我们每次需要执行一次退避来发送[一个/这个待听辨]数据包时把竞争窗口翻倍。
   - Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=15–18, absolute=513.05–547.99s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=1–3, absolute=525–550.16s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
   - 限制：保留这一口语未闭合的before explaining句，不改写为顺畅主句。standard(s)、said/say及packet冠词都有冲突。
6. So before explaining the reason because we do that, let me mention what was reported in one of the earlier slides.
所以在解释因为我们这样做的原因之前，让我提一下前面一张幻灯片中报告过的内容。
   - Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=15–18, absolute=513.05–547.99s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=1–3, absolute=525–550.16s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
   - 限制：该完整重复起句来自Qwen和两个新Whisper重叠窗口；Feishu 09止于上句，Feishu 10从But I didn’t comment开始。按内容接回，不因旧锚点截去。

### 待听辨记录

- [every time/at every time unclear]
  - 候选：every time / at every time
  - 证据：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）: every time；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）: at every time；新无提示Whisper medium.en chunk-003, segment=12 word, absolute=489.99–491.73s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: every time
  - 处理：保留待听辨；不按标准语法直接去掉Qwen独有at。
- [backoff repetition unclear] time
  - 候选：the backoff, the backoff time / the backoff time
  - 证据：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）: compute.Difficult time；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）: compute the because the because time；新无提示Whisper medium.en chunk-003, segment=14 word, absolute=510.97–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: the bit of time
  - 处理：此处backoff技术词可确定为候选，但重复次数不明；正文保留简洁标记和中文待听辨。
- [standard said/standards say unclear]
  - 候选：the standard said（Feishu） / the standards say（新Whisper） / they stand us at（Qwen字面，可能为近音）
  - 证据：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=15 word, absolute=523.43–525.01s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
  - 处理：不改成旧稿standard says；单复数与时态需听辨。
- [a/the unclear] packet
  - 候选：a packet（Qwen） / the packet（Feishu、新Whisper两重叠窗）
  - 证据：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）: the packet；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）: a packet；新无提示Whisper medium.en chunk-003, segment=16 word, absolute=532.61–533.21s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）: the packet；新无提示Whisper medium.en chunk-004, segment=1 word, absolute=532.6–533.22s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）: the packet
  - 处理：两次新Whisper为同音频重叠窗，不当成两项独立语音证据；冠词仍保留待听辨。
- [enlarge/launch unclear]
  - 候选：enlarge（Feishu与新Whisper共同支持） / launch（仅Qwen）
  - 证据：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
  - 处理：正文保留待听辨；文字交叉支持较强的是enlarge，不依据句意或二比一宣称精确听证。

## 08 · 00:09:04

稳定块ID：doxcnHZ5g5teuPb75H042YGavgb
写回前应验证原块SHA256：31fb3d36c89d426bb56eac5981d0f8dc4c8689b7bf4681d4b0f660a8ccef91ed

### 具体修改

1. I didn't comment on that because I didn't want to put too many things together at the same time. → But I didn't comment on that because I didn't want to put too many things at the same time.
   - 理由：恢复句首But；三方均无together，移除旧校订增词。
   - 来源：Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=18–19, absolute=540.59–554.97s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
2. One more important thing to say about backoff is that → But one more thing that we need to say important about the backoff is that the backoff procedure
   - 理由：恢复But、that we need to say important的原词序、the backoff和再次说出的the backoff procedure；不调换important以润色。
   - 来源：Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
3. when we have a packet that has been transmitted and failed. → when we have essentially a packet, right, that has been transmitted and it failed.
   - 理由：恢复essentially、right及and it failed的独立主语与过去时；不把failed并入has been的并列结构。
   - 来源：Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-004, segment=6 word, absolute=570.82–579.86s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）

### 逐句证据

1. But I didn't comment on that because I didn't want to put too many things at the same time.
但我没有对此作解释，因为我不想同时放入太多事情。
   - Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=18–19, absolute=540.59–554.97s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
2. But one more thing that we need to say important about the backoff is that the backoff procedure, of course, it is performed, as we said, when we have essentially a packet, right, that has been transmitted and it failed.
但还有一件我们需要说的重要的关于退避的事情，是退避过程，当然，它会被执行，正如我们说过的，当我们基本上有一个数据包，对吧，它已经被发送了，而且它失败了。
   - Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
   - 限制：保留thing that we need to say important、the backoff procedure ... it及has been transmitted and it failed，不以标准书面语改写。Feishu到as we said，后面的条件由Qwen和新Whisper补足；so we归09。

### 待听辨记录


## 09 · 00:09:40

稳定块ID：doxcnvRjxRufvfMiuNnxSymfMlh
写回前应验证原块SHA256：72da87b0e1a669253f8f3f17fc1da94bb9b80d92d390a38a72a1b2c27a9323f9

### 具体修改

1. exactly the same backoff procedure → a backoff procedure ... Exactly as we explained ... The same procedure that we just explained
   - 理由：恢复原飞书、校订前Qwen、新独立短窗均有的两个完整重复从句；不再压缩表达
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new base/small/medium unprompted 09:10–11:50 sample
2. We get a packet → we got [a/the unclear] packet
   - 理由：恢复三个来源共同的got，不替讲者改时态；冠词冲突保留
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
3. in which → under which
   - 理由：旧两来源和新medium均为under which，两处恢复
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
4. It also needs to be performed → This procedure indeed needs to be performed also
   - 理由：恢复主语、indeed和also的原位置
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
5. a transmitting node has a packet → a node, a transmitter [wording unclear], has got a packet
   - 理由：恢复has got；节点称呼不凭语法润色决定，按新medium候选保留并标来源冲突
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
6. senses the channel, and finds it busy → It senses the channel, but the channel is busy, right?
   - 理由：恢复原叙述、转折和尾问，不用finds改写
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
7. We get a packet from the higher layers → So, if we sense the channel, we got [a/the unclear] packet from the higher layers
   - 理由：恢复被删的条件开头及口语结构，不修成更顺的句子
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
8. carrier-sense multiple-access principle → carrier sensing multiple access principle
   - 理由：恢复原词形sensing，而非只统一连字符
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
9. What we knew so far is that we cannot access the channel because it is busy. → So, what we knew so far is that in this case, we cannot ... right? Because the channel is busy.
   - 理由：恢复So、in this case、right及重复名词；末句分开遵循两ASR，非合并简写
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
10. who is already talking → who is talking already
   - 理由：旧Qwen和新medium一致，恢复词序
   - 来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
11. （新增不确定性标记） → case/phase、两个okay、node/transmitter、a/the冠词及末尾okay/right待听辨标记
   - 理由：来源冲突不能通过猜测消除；明确范围，候选不冒称准确逐字稿
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json

### 逐句证据

1. So, we need to recontend for the channel and transmit the packet again, right?
所以，我们需要重新竞争信道，并且再次传送这个数据包，对吧？
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 580–587s
2. This is the [case/phase unclear] that we have considered so far, under which we need to perform the backoff.
这就是我们到目前为止考虑过的这个〔case/phase，情况/阶段，待听辨〕，在这种情况下，我们需要执行这个退避。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 586.66–601.58s
   - 限制：原飞书及旧Qwen均case，新三路短窗及全文medium均phase；不能以新ASR多数机械推翻旧来源，保留词级待听辨
3. However, there are two more situations under which we need to perform a backoff procedure, [okay? unclear]
不过，还有另外两种情况，在这些情况下，我们需要执行一个退避过程，〔okay?，好吗？待听辨〕
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 592.8–610s
   - 限制：末尾okay只见原飞书，旧Qwen与新无提示medium未转出，暂显式标记而不无痕删除或确认
4. Exactly as we explained, [okay? unclear]
正如我们解释过的那样，〔okay?，好吗？待听辨〕
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 601.58–610s
   - 限制：从句三方支持；末尾okay只见原飞书，待听辨
5. The same procedure that we just explained.
就是我们刚刚解释过的同一个过程。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en 09:10–11:50 sample raw；new unprompted base.en/small.en 09:10–11:50 sample raw
   - 限制：全文medium此处just this way误识；F、Qwen及新独立短窗支持just explained，因此保留完整从句
6. This procedure indeed needs to be performed also when a node, a transmitter [wording unclear], has got a packet to transmit.
这个过程确实也需要在一个节点、一个发送方〔此处措辞待听辨〕有了一个要传送的数据包时执行。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 610–633.44s；new unprompted medium.en 09:10–11:50 sample raw
   - 限制：新medium两种窗均支持a node, a transmitter；原飞书one and node transmitter、Qwen a known transmitter不清。保留候选结构并明确标注，不能改写成a transmitting node
7. It senses the channel, but the channel is busy, right?
它侦听信道，但是信道是忙的，对吧？
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 624.38–644.71s
   - 限制：senses由原飞书与新medium支持；Qwen sends是近音。新全文medium漏第二个channel，原飞书、Qwen及新small短窗保留，故补回
8. So, we already know that in this case, we cannot access the channel right away because of the carrier sensing multiple access principle, right?
所以，我们已经知道，在这种情况下，因为载波侦听多址接入的原则，我们不能马上接入信道，对吧？
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 634.03–652.13s
9. So, if we sense the channel, we got [a/the unclear] packet from the higher layers.
所以，如果我们侦听信道，我们从更高层拿到了〔a/the，冠词待听辨〕数据包。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 644.71–659.23s
   - 限制：got三方明确；原飞书及新全文medium是the，旧Qwen为a。保留got及条件开头，不改成get；冠词显式待听辨
10. At the MAC layer, we sense the channel for DIFS, but the channel is busy, [okay/right unclear]
在MAC层，我们侦听信道一个DIFS的时间，但是信道是忙的，〔okay/right，好吗/对吧，待听辨〕
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 652.13–669.69s
   - 限制：MAC/DIFS是明确Wi-Fi术语近音归一：旧mark/for this，新max/for this。未据此改句式；尾问原Feishu、旧Qwen、新medium短窗及全文为okay，但small短窗655.94–668.02s为right，base未保留，故显式[okay/right unclear]
11. So, what we knew so far is that in this case, we cannot access the channel, right?
所以，我们到目前为止知道的是，在这种情况下，我们不能接入信道，对吧？
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 659.23–677.39s
12. Because the channel is busy.
因为信道是忙的。
   - Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 670.67–677.39s
13. We are like polite people.
我们就像有礼貌的人。
   - Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 670.67–677.39s
14. We don't want to interrupt someone who is talking already.
我们不想打断一个已经在讲话的人。
   - Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 677.39–687.43s

### 待听辨记录

- okay/right after channel is busy
  - 候选：okay / right
  - 证据：F/Qwen/medium短窗及全文=okay；small短窗655.94–668.02s=right；base省略
  - 处理：保留[okay/right unclear]，不以数量表决
- case/phase
  - 候选：case / phase
  - 证据：F+Qwen=case；新Whisper体系多次phase
  - 处理：词级待听辨，不以模型数量表决
- two okay fillers after procedure and explained
  - 候选：okay? / not present
  - 证据：F有；旧Qwen和新medium未转出
  - 处理：标为[okay? unclear]
- a node, a transmitter
  - 候选：a node, a transmitter / node transmitter / a known transmitter (Qwen near-sound)
  - 证据：新medium两个窗一致，F/Qwen近音不清
  - 处理：保留新medium候选结构+措辞待听辨
- a/the packet
  - 候选：a / the
  - 证据：Qwen=a；F+新全文medium=the
  - 处理：保留[a/the unclear]

## 10 · 00:11:21

稳定块ID：doxcnPqzDaGsf13GV71CGVfXjmh
写回前应验证原块SHA256：a7fec0aef2159d772f72c52411a6fd17caecacf4fe4ea7403d9e0f1fff5e544e

### 具体修改

1. So we wait. → So, we wait. We wait.
   - 理由：恢复旧Qwen与新medium单窗内共有的第二次We wait；不是上下文窗拼接重复
   - 来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
2. what exactly do we mean by waiting, and for how long? → What do we mean exactly that we need to wait? [question wording unclear] For how long?
   - 理由：恢复原有问句词序和两个问句，保留措辞冲突而不润色为by waiting
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
3. In reality, also in this case we need to apply → Well, in reality, also in this case, what we need to do is to apply
   - 理由：恢复Well、what we need to do is以及重复解释结构
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
4. We wait for the backoff time according to this procedure. → So, how long do we wait for? We will wait for the backoff time, according to this procedure.
   - 理由：恢复被删的完整问句和will，不把再次提问压掉
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json；new unprompted medium.en full-run chunk-005.raw.json
5. This is the rule again also in this first case, when a Wi-Fi node gets a new packet → So, this is the rule again. Also in this first case, when we have that the node, Wi-Fi node, gets a new packet
   - 理由：恢复So、分句和when we have that/the node, Wi-Fi node口语；不改成语法更流畅的简写
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json
6. and the MAC needs to apply the protocol to transmit it → And the MAC needs to apply the protocol in order to transmit that packet
   - 理由：恢复in order to、that packet及讲者的And开句；MAC技术近音按Qwen及上下文校正
   - 来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json

### 逐句证据

1. So, we wait.
所以，我们等着。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 677.39–687.43s
2. We wait.
我们等着。
   - Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 677.39–687.43s
   - 限制：原飞书只一次；旧Qwen与新medium在各自同一窗口内部均有两次，不是将重叠窗口拼接形成的重复，恢复第二次；仍未人工听辨
3. That's what we said, but now we need to be more precise.
我们之前就是这么说的，但是现在我们需要更精确一些。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 687.43–695.45s
4. What do we mean exactly that we need to wait? [question wording unclear]
我们说需要等着，到底是什么意思？〔问句的确切措辞待听辨〕
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 687.43–704.87s
   - 限制：新medium为What do we mean exactly that we need to wait，原飞书do we mean exactly that we need to wait，Qwen为What do we do? We mean exactly that we need to wait；保留较完整候选并显式标疑，不替讲者改写为what exactly do we mean by waiting
5. For how long?
等多久？
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 695.45–704.87s
   - 限制：F和Qwen为for how long；新medium此窗为or how long，按旧双源保留for，不静默合并上一问句
6. Well, in reality, also in this case, what we need to do is to apply the backoff procedure.
嗯，实际上，在这种情况下也是，我们需要做的就是应用退避过程。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 695.45–714.71s；new unprompted medium.en full-run chunk-005.raw.json 705–715.32s
7. So, how long do we wait for?
那么，我们要等多久呢？
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 704.87–714.71s；new unprompted medium.en full-run chunk-005.raw.json 705–715.32s
8. We will wait for the backoff time, according to this procedure.
我们会按照这个过程，等待这个退避时间。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 714.71–723.27s；new unprompted medium.en full-run chunk-005.raw.json 715.32–723.52s
9. So, this is the rule again.
所以，这又是这个规则。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 714.71–723.27s；new unprompted medium.en full-run chunk-005.raw.json 715.32–723.52s
10. Also in this first case, when we have that the node, Wi-Fi node, gets a new packet from the higher layers.
在这第一种情况下也是，当这个节点，Wi-Fi节点，从更高层拿到一个新的数据包时。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json 724.58–744.3s
   - 限制：保留讲者when we have that和node, Wi-Fi node口语结构；不改成流利单句
11. And the MAC needs to apply the protocol in order to transmit that packet.
并且MAC需要应用这个协议，才能传送那个数据包。
   - Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json 733.18–750.02s
   - 限制：原飞书mark、新medium mask，Qwen明确MAC；依技术近音与旧Qwen归一。that由原飞书、新medium支持，Qwen the

### 待听辨记录

- What do we mean exactly that we need to wait?
  - 候选：do we mean exactly that we need to wait? (Feishu) / What do we do? We mean exactly that we need to wait (Qwen) / What do we mean exactly that we need to wait? (medium)
  - 证据：三源问句词序略冲突
  - 处理：保留新medium完整候选及[question wording unclear]，不润色
- For how long?
  - 候选：For how long? / or how long?
  - 证据：F/Qwen支持For，新medium此窗or
  - 处理：保留旧双源For，差异留记录待听辨

## 11 · 00:12:27

稳定块ID：doxcnxO1XrFqJ8vDuFhY9nCToXb
写回前应验证原块SHA256：6d12f435de26c268f0d80fa59f37f32e270fb5895be7391f4e9130ade9cb6303

### 具体修改

1. First we need to sense the channel for DIFS. → So, we know that first of all, we need to sense the channel for DIFS.
   - 理由：恢复原来的起句与 first of all；只将技术近音 this/dips 规范为 DIFS。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 5–6, relative 39.30–56.42s + offset 705s = absolute 744.30–761.42s
2. If the channel is sensed busy, we apply backoff. → If the channel is sense busy, then what [we’ll / we unclear] do is apply the backoff.
   - 理由：撤销语法润色和压缩；原始识别保留 is sense busy；未来/现在式冲突不擅选。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 6–7, relative 45.02–64.58s + offset 705s = absolute 750.02–769.58s
3. First we wait for it to become idle again and sense it as idle for DIFS. → That is, first of all, we need to wait for the channel to become idle again, and sense the channel idle for DIFS.
   - 理由：恢复 That is、we need to、the channel 的重复及原句式。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 7–8, relative 56.42–75.90s + offset 705s = absolute 761.42–780.90s
4. Then we draw an integer with equal probability from the range zero to CW_min, set the backoff time to that integer multiplied by the time slot → Then draw an integer with equal probability out of the range zero, CW_min, set that integer multiplied by the time slot as backoff time
   - 理由：恢复无主语 draw、out of 和 set that integer ... as 的措辞，不重组计算步骤。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 8–10, relative 64.58–96.12s + offset 705s = absolute 769.58–801.12s
5. If the channel becomes busy while we are decreasing the counter, we need to stop and freeze it; we cannot decrease it. → If the channel becomes busy at a certain point, while we are still decreasing the backoff counter, we need to stop the counter, right? And freeze it; we cannot decrease it.
   - 理由：恢复 at a certain point、still、counter 重复及口头 right。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 10–12, relative 86.28–112.24s + offset 705s = absolute 791.28–817.24s
6. When the channel becomes idle again, we sense it for DIFS. If it stays idle for that time, we resume decreasing the counter until it reaches zero. → And then, when the channel becomes idle again, we will sense the channel for DIFS. If it’s idle, of course, for that time, we will resume decreasing our backoff counter. Till we do that, till the counter reaches zero, right?
   - 理由：恢复两处 will、our、of course，以及 till ... till 的重复从句；不把未来式改成现在式。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 12–15, relative 102.30–140.68s + offset 705s = absolute 807.30–845.68s
7. As soon as it reaches zero, we can access the channel and transmit our packet. The transmission may be successful, in which case we are done. → As soon as the counter reaches zero, then we can access the channel and transmit our packet. And then of course it depends. The transmission may be successful; that is fine, we are done.
   - 理由：恢复 the counter、then、被删的 it depends 及口语 that is fine，不以 in which case 替写。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 15–17, relative 132.30–151.66s + offset 705s = absolute 837.30–856.66s
8. Or the packet may fail, and we must recontend for the channel using backoff. → Or the packet may fail, and in that case, we have to recontend for the channel by using the backoff [receiver / procedure unclear]. Right?
   - 理由：恢复 in that case、have to、by using 和句末词；receiver 与技术上可能的 procedure 不经音频不能裁决。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 17–18, relative 144.80–164.66s + offset 705s = absolute 849.80–869.66s
9. Now we know two conditions under which we perform backoff. → Okay, so now we know that actually there are two conditions, one and two, under which we will perform the backoff.
   - 理由：恢复 actually、one and two、will 和连接语；Qwen/Whisper均为 and，Feishu误识别为 or。
   - 来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 18–19, relative 151.90–176.32s + offset 705s = absolute 856.90–881.32s

### 逐句证据

1. So, we know that first of all, we need to sense the channel for DIFS.
所以，我们知道，首先我们需要侦听信道一个 DIFS 的时间。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 5–6, relative 39.30–56.42s + offset 705s = absolute 744.30–761.42s
2. If the channel is sense busy, then what [we’ll / we unclear] do is apply the backoff.
如果信道被侦听为忙，那么[我们将要／我们，待听辨]做的就是执行退避。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 6–7, relative 45.02–64.58s + offset 705s = absolute 750.02–769.58s
   - 限制：Feishu and Whisper retain “is sense busy”; no grammatical repair to “is sensed busy”. The future/present wording before “do” differs across sources.
3. That is, first of all, we need to wait for the channel to become idle again, and sense the channel idle for DIFS.
也就是说，首先我们需要等信道再次变为空闲，并侦听信道空闲一个 DIFS 的时间。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 7–8, relative 56.42–75.90s + offset 705s = absolute 761.42–780.90s
4. Then draw an integer with equal probability out of the range zero, CW_min, set that integer multiplied by the time slot as backoff time, and then decrease the backoff counter slot by slot as long as the channel is idle.
然后从零、CW_min 这个范围中等概率地抽取一个整数，把那个整数乘以时隙设为退避时间，然后只要信道空闲，就逐个时隙递减退避计数器。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 8–10, relative 64.58–96.12s + offset 705s = absolute 769.58–801.12s
5. If the channel becomes busy at a certain point, while we are still decreasing the backoff counter, we need to stop the counter, right?
如果信道在某个时刻变忙，而我们还在递减退避计数器，我们就需要停止计数器，对吧？
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 10–12, relative 86.28–112.24s + offset 705s = absolute 791.28–817.24s
6. And freeze it; we cannot decrease it.
并把它冻结；我们不能递减它。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 12–12, relative 102.30–112.24s + offset 705s = absolute 807.30–817.24s
7. And then, when the channel becomes idle again, we will sense the channel for DIFS.
然后，当信道再次变为空闲时，我们会侦听信道一个 DIFS 的时间。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 12–13, relative 102.30–121.94s + offset 705s = absolute 807.30–826.94s
8. If it’s idle, of course, for that time, we will resume decreasing our backoff counter.
当然，如果它在那段时间里是空闲的，我们就会恢复递减我们的退避计数器。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 13–14, relative 112.24–131.96s + offset 705s = absolute 817.24–836.96s
9. Till we do that, till the counter reaches zero, right?
直到我们这样做，直到计数器到达零，对吧？
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 14–15, relative 122.46–140.68s + offset 705s = absolute 827.46–845.68s
10. As soon as the counter reaches zero, then we can access the channel and transmit our packet.
计数器一到零，那么我们就可以接入信道并发送我们的数据包。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 15–15, relative 132.30–140.68s + offset 705s = absolute 837.30–845.68s
11. And then of course it depends.
然后，当然，这要看情况。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 16–16, relative 140.68–144.80s + offset 705s = absolute 845.68–849.80s
12. The transmission may be successful; that is fine, we are done.
这次传输可能成功；那很好，我们完成了。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 16–17, relative 140.68–151.66s + offset 705s = absolute 845.68–856.66s
13. Or the packet may fail, and in that case, we have to recontend for the channel by using the backoff [receiver / procedure unclear].
或者这个数据包可能失败，而在那种情况下，我们必须使用退避[接收器／过程，待听辨]来重新竞争信道。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 17–18, relative 144.80–164.66s + offset 705s = absolute 849.80–869.66s
   - 限制：All three recognitions give receiver or a near spelling; procedure is only a contextually plausible technical alternative, not established by these outputs.
14. Right?
对吧？
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 18–18, relative 151.90–164.66s + offset 705s = absolute 856.90–869.66s
15. Okay, so now we know that actually there are two conditions, one and two, under which we will perform the backoff.
好，所以现在我们知道，实际上有两种情况，第一种和第二种，在这些情况下我们会执行退避。
   - Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 18–19, relative 151.90–176.32s + offset 705s = absolute 856.90–881.32s

### 待听辨记录

- what [we’ll / we unclear] do
  - 候选：what we’ll do / what we do
  - 证据：Feishu: what will do; Qwen chunk 6: what we do; Whisper chunk-005 segment 6: what we’ll do.
  - 处理：保留时态候选与中文待听辨；不根据旧校订的现在式裁决。
- backoff [receiver / procedure unclear]
  - 候选：backoff receiver / backoff procedure
  - 证据：Feishu: backup receiver; Qwen chunk 7: back of receiver; Whisper chunk-005 segment 18 (856.90–869.66s): back-off receiver. None explicitly gives procedure.
  - 处理：保留 receiver 的文本证据；procedure 只列技术近音候选，需回听。

## 12 · 00:14:39

稳定块ID：doxcnWAgzkaE1V9NzLFbhdUxUsh
写回前应验证原块SHA256：4e78dfe8a2b1eabc9184b4eb9bdf50c37de08c5e79a49fee65b9ea54ca0911ff

### 具体修改

1. Let's leave the third condition for later. Before introducing it, I want to present an example of a situation where we apply backoff. → Okay, let’s leave the third condition for later. Okay, before introducing the third condition, I want to present an example of a situation when we apply the backoff.
   - 理由：恢复 Okay、重复的 the third condition 及 when；不以 it 消除重复。
   - 来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 19–21, relative 164.66–198.06s + offset 705s = absolute 869.66–903.06s；Unprompted Whisper medium.en raw: chunk-006, segments 1–2, relative 1.46–22.14s + offset 885s = absolute 886.46–907.14s
2. With this example, I want to clarify why we use backoff, why it is actually useful, and why the standard says → And what I want to do with this example is to clarify why, why we are using the backoff. Why is the backoff actually useful? Okay, and why the standard says
   - 理由：恢复完整引入从句、why why 重复、are using 进行式及独立问句，不合并列举。
   - 来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 21–22, relative 186.66–208.98s + offset 705s = absolute 891.66–913.98s；Unprompted Whisper medium.en raw: chunk-006, segments 2–4, relative 11.28–34.30s + offset 885s = absolute 896.28–919.30s
3. every time we perform backoff for a given packet, we need to double the contention window parameter. → every time we perform the backoff for a given packet, we need to double the contention window parameter.
   - 理由：恢复 the；pattern/Bechov/window pattern仅作有来源支持的技术近音校正，不据此增添协议解释。
   - 来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 4–6, relative 24.70–49.18s + offset 885s = absolute 909.70–934.18s

### 逐句证据

1. Okay, let’s leave the third condition for later.
好，我们把第三种情况留到后面。
   - Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 19–20, relative 164.66–186.66s + offset 705s = absolute 869.66–891.66s
2. Okay, before introducing the third condition, I want to present an example of a situation when we apply the backoff.
好，在介绍第三种情况之前，我想给出一个我们执行退避的情况的例子。
   - Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 20–21, relative 176.32–198.06s + offset 705s = absolute 881.32–903.06s；Unprompted Whisper medium.en raw: chunk-006, segments 1–2, relative 1.46–22.14s + offset 885s = absolute 886.46–907.14s
3. And what I want to do with this example is to clarify why, why we are using the backoff.
而我想用这个例子做的，是说明为什么，为什么我们在使用退避。
   - Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 21–22, relative 186.66–208.98s + offset 705s = absolute 891.66–913.98s；Unprompted Whisper medium.en raw: chunk-006, segments 2–3, relative 11.28–24.70s + offset 885s = absolute 896.28–909.70s
4. Why is the backoff actually useful?
退避实际上为什么有用？
   - Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 22–22, relative 198.06–208.98s + offset 705s = absolute 903.06–913.98s；Unprompted Whisper medium.en raw: chunk-006, segments 4–4, relative 24.70–34.30s + offset 885s = absolute 909.70–919.30s
5. Okay, and why the standard says that every time we perform the backoff for a given packet, we need to double the contention window parameter.
好，还有为什么标准说，每次我们为一个给定的数据包执行退避时，我们都需要把竞争窗口参数加倍。
   - Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 4–6, relative 24.70–49.18s + offset 885s = absolute 909.70–934.18s
   - 限制：packet follows Feishu and the packet/backoff context; pattern in Qwen/Whisper is treated as a technical near-sound error. parameter is explicit in Feishu and Qwen.

### 待听辨记录


## 13 · 00:15:26

稳定块ID：doxcnAxAESMqbsUmzgLpNkXu0hB
写回前应验证原块SHA256：dcc622357e0ecd7f79788c133b5f67920fa115c473b6636f0954c7174890f806

### 具体修改

1. The main thing here, when we study Wi-Fi, is of course to learn how we use a technology that is used every day by almost everyone. → Okay, because the main thing here, when we study Wi-Fi, okay, is to, of course, learn how we use a technology that is actually used every day, right, by almost everyone.
   - 理由：恢复 because、actually、okay、right 以及原来插入语次序。
   - 来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 6–8, relative 39.38–64.94s + offset 885s = absolute 924.38–949.94s
2. It's good to know how things work, but it is also important to understand the rationale. Why do things happen? → So it’s good to know how things work. But it’s also important to understand the rationale, okay? Why things happen?
   - 理由：恢复 So/But 和 okay；撤销给原问句补 do 的语法润色。
   - 来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 8–9, relative 56.78–74.82s + offset 885s = absolute 941.78–959.82s
3. That's the really important thing this class should give you: strengthening your ability to understand why certain things have been decided in a certain manner when designing a system. → That’s the really important fact that this class should give you, okay? To strengthen your ability to understand why certain things have been decided in certain manner in designing a system.
   - 理由：恢复 fact、that、To strengthen、in certain manner 和 in designing，不补冠词、不改成分词。
   - 来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 10–12, relative 74.82–109.66s + offset 885s = absolute 959.82–994.66s
4. There is always a reason, and we need to learn how to reason about things and understand the solutions that have been created. → Okay, because there is always a reason, and what we need to do is to learn how to reason about things, and understand the solutions that have been created.
   - 理由：恢复 Okay/because 和 what we need to do is to；Feishu在尾部截断，后续由两个Qwen重叠窗与Whisper共同补足。
   - 来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 12–14, relative 101.82–126.78s + offset 885s = absolute 986.82–1011.78s

### 逐句证据

1. Okay, because the main thing here, when we study Wi-Fi, okay, is to, of course, learn how we use a technology that is actually used every day, right, by almost everyone.
好，因为这里主要的事情，当我们学习 Wi-Fi 时，好，当然是去了解我们怎样使用一种实际上每天都在被使用的技术，对吧，几乎每个人都在使用。
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 6–8, relative 39.38–64.94s + offset 885s = absolute 924.38–949.94s
2. So it’s good to know how things work.
所以，知道事情怎样运作是好的。
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 8–8, relative 56.78–64.94s + offset 885s = absolute 941.78–949.94s
3. But it’s also important to understand the rationale, okay?
但理解其中的道理也很重要，好吗？
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 8–9, relative 56.78–74.82s + offset 885s = absolute 941.78–959.82s
4. Why things happen?
为什么事情会发生？
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 9–9, relative 64.94–74.82s + offset 885s = absolute 949.94–959.82s
5. Why do we make certain choices while developing a technology?
为什么我们在开发一项技术时会作出某些选择？
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 9–10, relative 64.94–88.44s + offset 885s = absolute 949.94–973.44s
6. That’s the really important fact that this class should give you, okay?
那是这门课应该给你们的真正重要的事实，好吗？
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 10–10, relative 74.82–88.44s + offset 885s = absolute 959.82–973.44s
7. To strengthen your ability to understand why certain things have been decided in certain manner in designing a system.
去增强你们的能力，理解为什么在设计一个系统时，某些事情被以某种方式决定下来。
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 10–12, relative 74.82–109.66s + offset 885s = absolute 959.82–994.66s
8. Okay, because there is always a reason, and what we need to do is to learn how to reason about things, and understand the solutions that have been created.
好，因为总是有一个原因，而我们需要做的是学会怎样思考事情，并理解已经被创造出来的解决方案。
   - Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 12–14, relative 101.82–126.78s + offset 885s = absolute 986.82–1011.78s
   - 限制：Feishu stops at “to look”; Qwen overlapping chunks 8/9 and Whisper supply the continuation. The overlap is retained once, not twice.

### 待听辨记录


## 14 · 00:16:47

稳定块ID：doxcnusJMQ3VdFmXjsWY3Iw9EOh
写回前应验证原块SHA256：f3580b7ccfccb74a0d0be0bbf140e7d708b60077ad5d19b37f63f934a10af5b5

### 具体修改

1. That's the important attitude we need to develop. → Okay, [that ... unclear] that’s the important attitude that we need to develop.
   - 理由：恢复 Okay 和 that；Qwen独有的 that 起头重复保留为待听辨，不直接删掉或认定。
   - 来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–14, relative 120.56–126.78s + offset 885s = absolute 1005.56–1011.78s
2. Understanding why is a kind of mental exercise that we need to do. → So, this is understanding [why / Wi-Fi unclear], is a kind of mental exercise, okay, that we need to [to ... unclear] do.
   - 理由：恢复 So, this is 和第二个 is 的口语句法、okay；why/Wi-Fi不依据语意擅选；可能重复to另标待辨。
   - 来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–15, relative 120.56–135.06s + offset 885s = absolute 1005.56–1020.06s
3. Good. Let's consider a simple topology where we have an access point and then A, B, and C. → Okay, good. So, let’s consider a simple topology where we have an access point, and then we have A, B, and C.
   - 理由：恢复 Okay、So 和第二个 we have，不删除平行从句中的重复。
   - 来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 16–17, relative 136.18–165.16s + offset 885s = absolute 1021.18–1050.16s

### 逐句证据

1. Okay, [that ... unclear] that’s the important attitude that we need to develop.
好，[那……待听辨]那是我们需要培养的重要态度。
   - Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–14, relative 120.56–126.78s + offset 885s = absolute 1005.56–1011.78s
   - 限制：Qwen has “that that’s”; Feishu/Whisper have “that’s”. The possible false start is not silently deleted.
2. So, this is understanding [why / Wi-Fi unclear], is a kind of mental exercise, okay, that we need to [to ... unclear] do.
所以，这是理解[为什么／Wi-Fi，待听辨]，是一种思维练习，好，我们需要去[去……待听辨]做的。
   - Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–15, relative 120.56–135.06s + offset 885s = absolute 1005.56–1020.06s
   - 限制：Feishu: understanding why; Qwen: understanding why fire; Whisper: understanding Wi-Fi. Qwen alone also repeats “to”. mental is supported by Feishu and Whisper; Qwen’s experimental is not adopted.
3. Okay, good.
好，很好。
   - Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 16–16, relative 136.18–149.64s + offset 885s = absolute 1021.18–1034.64s
4. So, let’s consider a simple topology where we have an access point, and then we have A, B, and C.
所以，我们来考虑一个简单的拓扑，其中我们有一个接入点，然后我们有 A、B 和 C。
   - Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 16–17, relative 136.18–165.16s + offset 885s = absolute 1021.18–1050.16s

### 待听辨记录

- [that ... unclear] that’s
  - 候选：that that’s / that’s
  - 证据：Qwen chunk 9 begins “Okay, that that’s”; Feishu source 17 and Whisper chunk-006 segment 14 omit the first that.
  - 处理：保留可能的起句重复，需回听确定有无。
- understanding [why / Wi-Fi unclear]
  - 候选：understanding why / understanding Wi-Fi
  - 证据：Feishu source 17: why; Qwen chunk 9: why fire; Whisper chunk-006 segment 15 (1011.78–1020.06s): Wi-Fi.
  - 处理：保留两个词义候选，中文也标待听辨。
- need to [to ... unclear] do
  - 候选：need to to do / need to do
  - 证据：Qwen chunk 9 has “need to to do”; Feishu and Whisper have one to.
  - 处理：保留可能重复to；不把单一ASR重复直接当作原话。

## 15 · 00:17:18

稳定块ID：doxcnDM0vMtHUpnWdnzpcERTuof
写回前应验证原块SHA256：d4f9e44ff7937c69b05c5abd6e5ff7e64871e1e2ef3a4f14016b5c81c19232d3

### 具体修改

1. The access point is here. These are our user nodes, and they are part of this BSS, which means they can talk with the access point. → Okay, the access point is here. These are our user nodes, and [we / they unclear] are of course part of this BSS; that means they can talk with the access point.
   - 理由：恢复 Okay、of course、that means；we/they确有来源冲突，不能因为指代逻辑通顺便改成they。
   - 来源：Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 17–18, relative 149.64–175.10s + offset 885s = absolute 1034.64–1060.10s
2. Let's consider the simple case where all nodes can hear each other. Now let's represent their behavior over time. → And also, let’s consider the simple case where all nodes can hear each other. Okay, now let’s represent the behavior of these nodes over time.
   - 理由：恢复 And also、Okay 和 the behavior of these nodes；Feishu尾部缺失由Qwen及Whisper两窗补足，同一边界句不重复粘贴。
   - 来源：Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 18–19, relative 165.16–193.16s + offset 885s = absolute 1050.16–1078.16s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s

### 逐句证据

1. Okay, the access point is here.
好，接入点在这里。
   - Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 17–17, relative 149.64–165.16s + offset 885s = absolute 1034.64–1050.16s
2. These are our user nodes, and [we / they unclear] are of course part of this BSS; that means they can talk with the access point.
这些是我们的用户节点，并且[我们／它们，待听辨]当然是这个 BSS 的一部分；那意味着它们可以和接入点通信。
   - Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 17–18, relative 149.64–175.10s + offset 885s = absolute 1034.64–1060.10s
   - 限制：Feishu and Whisper say we; Qwen says they. Do not repair the pronoun solely on technical semantics.
3. And also, let’s consider the simple case where all nodes can hear each other.
还有，我们来考虑所有节点都能听到彼此的这个简单情况。
   - Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 18–19, relative 165.16–193.16s + offset 885s = absolute 1050.16–1078.16s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s
   - 限制：Feishu stops after all nodes; Qwen and the Whisper overlap provide can hear each other.
4. Okay, now let’s represent the behavior of these nodes over time.
好，现在我们来表示这些节点随时间的行为。
   - Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 19–19, relative 175.10–193.16s + offset 885s = absolute 1060.10–1078.16s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s

### 待听辨记录

- [we / they unclear] are of course part of this BSS
  - 候选：we are of course part of this BSS / they are of course part of this BSS
  - 证据：Feishu source 18: we are of course part of these BSS; Whisper chunk-006 segment 17: we are of course part of this; Qwen chunk 9: they are of course part of this BSS.
  - 处理：we/they保留待听辨；不做语法或指代合理化。

## 16 · 00:17:58

稳定块ID：doxcnGEPwbf7ydvGtRF2lbJtene
写回前应验证原块SHA256：a58950f964e05ce19361b2192af289c552afcb78061a3f79599d821ca4425cb1

### 具体修改

1. This is the timeline. We will draw a timeline for each node: the access point, user A, user B, and user C. → So, this is the timeline. We will represent it by drawing a timeline for each node: access point, user A, user B, and user C.
   - 理由：恢复 So 和 represent it by drawing；各节点列表以完整的chunk-007为准补全，不用chunk-006窗口截断遗漏C。
   - 来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 20–21, relative 193.60–209.74s + offset 885s = absolute 1078.60–1094.74s；Unprompted Whisper medium.en raw: chunk-007, segments 1–2, relative 0.00–33.30s + offset 1065s = absolute 1065.00–1098.30s
2. Assume that when we start looking at the system, we observe that A has received a packet from its higher layers. Its application layer has generated some data. → Okay, now let’s assume that when we start looking at the system, what we observe is that A has received a packet from its higher layers. Okay, its application layer has generated some data.
   - 理由：恢复 Okay、now let’s、what we observe is that 的完整口语结构。
   - 来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 3–5, relative 33.30–66.44s + offset 1065s = absolute 1098.30–1131.44s
3. A gets this packet at its MAC layer and understands that it has to try to transmit it. → So, A gets this packet at [its / this unclear] MAC layer, and A understands that it has to try and transmit this packet, right?
   - 理由：恢复 So、重复主语A、try and、重复this packet及right；its/this依来源留疑点。
   - 来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 5–6, relative 55.68–76.68s + offset 1065s = absolute 1120.68–1141.68s
4. We know that in this case a Wi-Fi node will first sense the channel for DIFS. Let's assume that the channel is idle. → So, we know that in this case, a Wi-Fi node will first sense the channel for DIFS, right? Let’s assume that the channel is idle.
   - 理由：恢复 So 与 right；Feishu截断后由Qwen/Whisper补齐，diffs仅作DIFS技术近音校正。
   - 来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 6–7, relative 66.44–86.10s + offset 1065s = absolute 1131.44–1151.10s

### 逐句证据

1. So, this is the timeline.
所以，这是时间轴。
   - Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 20–20, relative 193.60–204.86s + offset 885s = absolute 1078.60–1089.86s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s
2. We will represent it by drawing a timeline for each node: access point, user A, user B, and user C.
我们会通过给每个节点画一条时间轴来表示它：接入点、用户 A、用户 B 和用户 C。
   - Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 20–21, relative 193.60–209.74s + offset 885s = absolute 1078.60–1094.74s；Unprompted Whisper medium.en raw: chunk-007, segments 2–2, relative 14.68–33.30s + offset 1065s = absolute 1079.68–1098.30s
3. Okay, now let’s assume that when we start looking at the system, what we observe is that A has received a packet from its higher layers.
好，现在我们来假设，当我们开始看这个系统时，我们观察到的是 A 从它的高层收到了一个数据包。
   - Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 3–4, relative 33.30–55.68s + offset 1065s = absolute 1098.30–1120.68s
4. Okay, its application layer has generated some data.
好，它的应用层生成了一些数据。
   - Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 4–5, relative 46.72–66.44s + offset 1065s = absolute 1111.72–1131.44s
5. So, A gets this packet at [its / this unclear] MAC layer, and A understands that it has to try and transmit this packet, right?
所以，A 在[它的／这个，待听辨] MAC 层收到这个数据包，而 A 明白它必须尝试去发送这个数据包，对吧？
   - Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 5–6, relative 55.68–76.68s + offset 1065s = absolute 1120.68–1141.68s
   - 限制：Qwen: at its MAC layer; Whisper: at this MAC layer; Feishu: and this mark layer. MAC is a clear technical near-sound correction; the determiner remains unresolved.
6. So, we know that in this case, a Wi-Fi node will first sense the channel for DIFS, right?
所以，我们知道，在这种情况下，一个 Wi-Fi 节点会首先侦听信道一个 DIFS 的时间，对吧？
   - Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 6–7, relative 66.44–86.10s + offset 1065s = absolute 1131.44–1151.10s
   - 限制：Feishu truncates after a corrupted “I will find out will first”; the full predicate is supported by Qwen and Whisper.
7. Let’s assume that the channel is idle.
我们来假设信道是空闲的。
   - Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 7–7, relative 76.68–86.10s + offset 1065s = absolute 1141.68–1151.10s

### 待听辨记录

- at [its / this unclear] MAC layer
  - 候选：at its MAC layer / at this MAC layer
  - 证据：Feishu source 19: and this mark layer; Qwen chunk 10: at its MAC layer; Whisper chunk-007 segment 5 (1120.68–1131.44s): at this MAC layer.
  - 处理：保留its/this和中文待听辨；不因所有格更自然而裁决。

## 17 · 00:19:08

稳定块ID：doxcnlR1VavXUPuMoZJxMqbHYie
写回前应验证原块SHA256：b5c9bca604a195405788560a93d584f8308c4debdb7a63cf6471e3e8c508f66f

### 具体修改

1. In this case, A can access the channel and transmit its data packet. It is a unicast packet intended for the access point. → So, we know that in this case, A can access the channel and transmit its data packet. That is a unicast data packet, so it is intended for the access point.
   - 理由：恢复 So, we know that、That is、data 和独立的so从句，不压缩成后置修饰。
   - 来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 7–9, relative 76.68–100.66s + offset 1065s = absolute 1141.68–1165.66s
2. Let's be optimistic and consider that it is successfully received by the access point. → And let’s be optimistic, and let’s consider that this data packet is successfully received by the access point.
   - 理由：恢复两个and、第二个let’s和this data packet，保留讲者重复。
   - 来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 9–11, relative 91.88–115.74s + offset 1065s = absolute 1156.88–1180.74s
3. Therefore, the access point will send an acknowledgment after SIFS. → Therefore, we know that the access point will send an acknowledgment after SIFS.
   - 理由：恢复we know that；Feishu的six按Qwen/Whisper共同支持校为SIFS。
   - 来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 11–12, relative 109.14–124.28s + offset 1065s = absolute 1174.14–1189.28s

### 逐句证据

1. So, we know that in this case, A can access the channel and transmit its data packet.
所以，我们知道，在这种情况下，A 可以接入信道并发送它的数据包。
   - Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 7–8, relative 76.68–91.88s + offset 1065s = absolute 1141.68–1156.88s
2. That is a unicast data packet, so it is intended for the access point.
那是一个单播数据包，所以它是发给接入点的。
   - Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 8–9, relative 86.10–100.66s + offset 1065s = absolute 1151.10–1165.66s
3. And let’s be optimistic, and let’s consider that this data packet is successfully received by the access point.
而且我们来乐观一点，而且我们来认为这个数据包被接入点成功接收了。
   - Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 9–11, relative 91.88–115.74s + offset 1065s = absolute 1156.88–1180.74s
4. Therefore, we know that the access point will send an acknowledgment after SIFS.
因此，我们知道，接入点会在 SIFS 之后发送一个确认。
   - Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 11–12, relative 109.14–124.28s + offset 1065s = absolute 1174.14–1189.28s
5. This is the usual story that we have told many times.
这是我们已经讲过很多次的通常的故事。
   - Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 12–12, relative 115.74–124.28s + offset 1065s = absolute 1180.74–1189.28s

### 待听辨记录


## 18 · 00:19:49

稳定块ID：doxcnm1bGEyxYyL64fY1q3gB9Kg
写回前应验证原块SHA256：8f18bac75f40e1f43892bc2972c3be68246bdaeb48f17473898f792133c9165f

### 具体修改

1. We also know that under these conditions the other nodes, B and C, demodulate the data packet's header. → Okay, we also know that under these conditions, the other nodes B and C demodulate the header, right, of the data packet.
   - 理由：恢复Okay、插入的right和the header ... of the data packet的原顺序；they modulate按Whisper及技术词边界校为demodulate。
   - 来源：Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 13–13, relative 124.28–139.86s + offset 1065s = absolute 1189.28–1204.86s
2. They read the Duration field so they can set their NAV counter, extending over the expected duration of the dialogue. → They read the Duration field, so that they can set their NAV counter, and this will extend over the all expected duration of the dialogue.
   - 理由：恢复so that、and this will和三方一致的the all expected，撤销分词压缩及语法修正；NAV由Qwen下一窗明确支持。
   - 来源：Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 14–15, relative 139.86–159.18s + offset 1065s = absolute 1204.86–1224.18s

### 逐句证据

1. Okay, we also know that under these conditions, the other nodes B and C demodulate the header, right, of the data packet.
好，我们还知道，在这些条件下，其他节点 B 和 C 解调首部，对吧，这个数据包的首部。
   - Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 13–13, relative 124.28–139.86s + offset 1065s = absolute 1189.28–1204.86s
   - 限制：Feishu/Qwen split the sound as “they modulate”; Whisper gives demodulate. This is treated as a clear technical word-boundary error rather than adding a second subject.
2. They read the Duration field, so that they can set their NAV counter, and this will extend over the all expected duration of the dialogue.
它们读取 Duration 字段，这样它们就能设置它们的 NAV 计数器，而这将延伸覆盖这次对话的全部预期持续时间。
   - Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 14–15, relative 139.86–159.18s + offset 1065s = absolute 1204.86–1224.18s
   - 限制：The ungrammatical “the all expected duration” is common to all three sources and intentionally retained. Singular field follows Feishu/Qwen; Whisper has fields.

### 待听辨记录


## 19 · 00:20:25

稳定块ID：doxcntMYbHlAQ6Z78lxolPfpwkd
写回前应验证原块SHA256：f4332be8c31b0fc429e7ee3e1c35f9ec9a15b2c90497fa700a72bf15b4a82ced

### 具体修改

1. So far so good; this is exactly what we did in the past. Now let's add some events. → Okay, so, so far so good; this is exactly what we did in the past. Now, let’s add some events here.
   - 理由：恢复Okay、前置so与so far的重复以及here；以Feishu/Qwen共同支持保留，不能只跟Whisper省略。
   - 来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 16–16, relative 160.96–170.66s + offset 1065s = absolute 1225.96–1235.66s
2. Let's say that B and C, while their NAV is set to a positive value, also receive a data packet from their respective upper layers. → Let’s say B and also C, while they have their NAV set to a positive value, will also receive a data packet from their respective upper layers.
   - 理由：恢复and also、they have their NAV set和will；不把未来式改成现在式。
   - 来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 17–18, relative 170.66–196.76s + offset 1065s = absolute 1235.66–1261.76s；Unprompted Whisper medium.en raw: chunk-008, segments 1–2, relative 0.00–22.30s + offset 1245s = absolute 1245.00–1267.30s
3. For example, at this point B gets a packet queued at its MAC layer, and at this other point C also gets a packet from its higher layers. → So, this means that, for example, at this point in time, B gets a packet that is queued at its MAC layer, and let’s assume that C at this point in time also gets a packet from its higher layers.
   - 理由：恢复So, this means that、that is、let’s assume以及两次at this point in time；删除旧校订无来源的other，不替讲者标明另一个时刻。
   - 来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 18–20, relative 185.70–209.98s + offset 1065s = absolute 1250.70–1274.98s；Unprompted Whisper medium.en raw: chunk-008, segments 2–4, relative 13.00–41.72s + offset 1245s = absolute 1258.00–1286.72s

### 逐句证据

1. Okay, so, so far so good; this is exactly what we did in the past.
好，所以，到目前为止一切顺利；这正是我们过去做过的。
   - Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 16–16, relative 160.96–170.66s + offset 1065s = absolute 1225.96–1235.66s
2. Now, let’s add some events here.
现在，我们在这里加一些事件。
   - Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 16–16, relative 160.96–170.66s + offset 1065s = absolute 1225.96–1235.66s
3. Let’s say B and also C, while they have their NAV set to a positive value, will also receive a data packet from their respective upper layers.
假设 B，还有 C，在它们把各自的 NAV 设为一个正值的时候，也会从它们各自的高层收到一个数据包。
   - Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 17–18, relative 170.66–196.76s + offset 1065s = absolute 1235.66–1261.76s；Unprompted Whisper medium.en raw: chunk-008, segments 1–2, relative 0.00–22.30s + offset 1245s = absolute 1245.00–1267.30s
4. So, this means that, for example, at this point in time, B gets a packet that is queued at its MAC layer, and let’s assume that C at this point in time also gets a packet from its higher layers.
所以，这意味着，例如，在这个时间点，B 收到一个在它的 MAC 层排队的数据包，而我们假设 C 在这个时间点也从它的高层收到一个数据包。
   - Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 18–20, relative 185.70–209.98s + offset 1065s = absolute 1250.70–1274.98s；Unprompted Whisper medium.en raw: chunk-008, segments 2–4, relative 13.00–41.72s + offset 1245s = absolute 1258.00–1286.72s

### 待听辨记录


## 20 · 00:21:21

稳定块ID：doxcnfJ6YnYDMIM2F7E4sDqTb6M
写回前应验证原块SHA256：09b82fe10df6af07a99fb4aac4136ab0147942a9c4b735d048104ae362382a6e

### 具体修改

1. While the dialogue between A and the access point is going on, B and C now also have a packet to transmit. → Okay, so now while we have this dialogue between A and the access point going on, we have B and C who have a packet to transmit as well.
   - 理由：恢复Okay, so now、两次we have和who have从句，不能把原来句法改写得更简洁。
   - 来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 4–6, relative 30.50–61.80s + offset 1245s = absolute 1275.50–1306.80s
2. Clearly their NAV is set, so they know the channel is busy and cannot access it. → Now, clearly, they have got their NAV set, so they know the channel is busy, so they cannot access the channel, right?
   - 理由：恢复Now、have got、重复so和the channel及right；NAV是Qwen明确词，不采用Whisper knobs。
   - 来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 6–7, relative 50.96–68.94s + offset 1245s = absolute 1295.96–1313.94s
3. That is the principle of carrier sensing. We are essentially in this situation, situation number one: B and C get a new packet but sense that the channel is busy. → That’s the principle of carrier sensing. We are essentially in this situation, situation number one, right? B and C [get / got unclear] a new packet, but they sense the channel as busy.
   - 理由：恢复right、they和as busy；Qwen重叠窗get/got冲突保留时态待听辨，不能让旧校订决定。
   - 来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 7–9, relative 62.56–90.92s + offset 1245s = absolute 1307.56–1335.92s
4. What do we have to do? Apply backoff. Remember that our scheme is distributed, so each node makes decisions for itself based on the state of the system that it observes. → So, what do we have to do? Apply backoff, right? So, this means that both B and C, remember our scheme is distributed, so everyone makes decisions by itself based on the state of the system that it observes.
   - 理由：恢复两次So、right以及被删的both B and C残留从句；恢复everyone/by itself，不以each node/for itself润色。
   - 来源：Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 9–11, relative 79.76–113.80s + offset 1245s = absolute 1324.76–1358.80s
5. B will say: I got a packet, but the channel is busy. → So, B will say, “[Hmm ... unclear] I got [a / the unclear] packet, but the channel is busy.”
   - 理由：恢复So；Hmm有无和a/the在两种ASR之间冲突，列为待听辨，不凭旧校订取舍。
   - 来源：Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 11–12, relative 102.48–123.02s + offset 1245s = absolute 1347.48–1368.02s

### 逐句证据

1. Okay, so now while we have this dialogue between A and the access point going on, we have B and C who have a packet to transmit as well.
好，所以现在，当我们有 A 和接入点之间的这段对话正在进行时，我们有 B 和 C，它们也有一个数据包要发送。
   - Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 4–6, relative 30.50–61.80s + offset 1245s = absolute 1275.50–1306.80s
2. Now, clearly, they have got their NAV set, so they know the channel is busy, so they cannot access the channel, right?
现在，显然，它们已经把 NAV 设置好了，所以它们知道信道忙，所以它们不能接入信道，对吧？
   - Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 6–7, relative 50.96–68.94s + offset 1245s = absolute 1295.96–1313.94s
3. That’s the principle of carrier sensing.
那就是载波侦听的原则。
   - Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 7–7, relative 62.56–68.94s + offset 1245s = absolute 1307.56–1313.94s
4. We are essentially in this situation, situation number one, right?
我们基本上处在这种情况，第一种情况，对吧？
   - Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 8–8, relative 70.72–79.76s + offset 1245s = absolute 1315.72–1324.76s
5. B and C [get / got unclear] a new packet, but they sense the channel as busy.
B 和 C [收到／收到了，待听辨]一个新数据包，但是它们侦听到信道忙。
   - Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 8–9, relative 70.72–90.92s + offset 1245s = absolute 1315.72–1335.92s
   - 限制：Qwen’s two overlapping windows disagree get/got; Feishu/Whisper read get. Both tenses are left for listening because the current task specifically forbids silent tense changes.
6. So, what do we have to do?
所以，我们必须做什么？
   - Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 9–9, relative 79.76–90.92s + offset 1245s = absolute 1324.76–1335.92s
7. Apply backoff, right?
执行退避，对吧？
   - Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 9–9, relative 79.76–90.92s + offset 1245s = absolute 1324.76–1335.92s
8. So, this means that both B and C, remember our scheme is distributed, so everyone makes decisions by itself based on the state of the system that it observes.
所以，这意味着 B 和 C 两者，记住我们的方案是分布式的，所以每一个都根据它观察到的系统状态自己作出决定。
   - Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 10–11, relative 91.92–113.80s + offset 1245s = absolute 1336.92–1358.80s
   - 限制：Retains the interrupted “both B and C” clause and everyone/by itself wording; it is not completed or repaired to “each node”.
9. So, B will say, “[Hmm ... unclear] I got [a / the unclear] packet, but the channel is busy.”
所以，B 会说：“[嗯……待听辨]我收到了[一个／这个，待听辨]数据包，但信道忙。”
   - Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 11–12, relative 102.48–123.02s + offset 1245s = absolute 1347.48–1368.02s
   - 限制：This continuation is absent from the supplied Feishu fragments. Qwen has “Hmm, I got a packet”; Whisper has “I got the packet”. The later what-I-need sentence belongs to section 21.

### 待听辨记录

- B and C [get / got unclear] a new packet
  - 候选：get / got
  - 证据：Feishu source 24: get (preceded by corrupted words); Qwen chunk 11: get; Qwen chunk 12: got; Whisper chunk-008 segment 8: get.
  - 处理：明确暴露Qwen相邻窗口的时态冲突，回听裁决。
- [Hmm ... unclear] I got [a / the unclear] packet
  - 候选：Hmm, I got a packet / I got the packet
  - 证据：Qwen chunk 12: Hmm, I got a packet; Whisper chunk-008 segment 12 (1358.80–1368.02s): I got the packet; supplied Feishu fragments end before this sentence.
  - 处理：保留口头语有无及冠词疑点；不删除潜在口语，也不把Qwen单独词盲当原话。

