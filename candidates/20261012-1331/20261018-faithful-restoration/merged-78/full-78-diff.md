# 78段完整候选独立diff

共252条原候选具体修改记录；以下before/after/理由/来源原样合并，不把条数当作确认错误数。
未人工听辨；本文不修改远端。

## 01 · 00:00:03 · 重传失败数据包需要退避

稳定块ID：doxcnYwPV6wJgi1S8geP75FfU5g
原块SHA256：5242993c1dac372666483c15471c0df8dd13546fb41c146d2496435c2d24271a
候选SHA256：a074142b9a40c37229ab9fdb01fa9bd9ef8ae48e85c2ddb6eb25c1eeeb64f526

### 具体修改

1. 原：a Wi-Fi node
   候选：[a/the unclear] Wi-Fi node
   理由：旧稿为a，Feishu与新Whisper为the，Qwen为a；不按二比一决定原词，正文保留冠词待听辨。
   来源：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
2. 原：because it has to retransmit a packet that failed
   候选：because this node has to retransmit [a/the unclear] packet that failed
   理由：三方都支持this node，旧校订以it替代了原来的重复名词；packet冠词有冲突，不擅定。
   来源：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
3. 原：this node will perform the backoff procedure.
   候选：then this node will perform the backoff procedure.
   理由：恢复三方都有的then。
   来源：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）

### 逐单元证据

1. And we said that whenever [a/the unclear] Wi-Fi node needs to recontend for the channel, because this node has to retransmit [a/the unclear] packet that failed, then this node will perform the backoff procedure.
而且我们说过，每当[一个/这个待听辨] Wi-Fi 节点需要重新竞争信道，因为这个节点必须重新发送[一个/这个待听辨]发送失败的数据包，那么这个节点就会执行退避过程。
   来源：Feishu历史快照 source_index_one_based=1（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=1–3, absolute=3.02–28.72s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
   限制：Wi-Fi node前Qwen为a，Feishu与新Whisper为the；packet前Qwen为a，新Whisper为the，Feishu断句处无冠词。两处均待听辨。 新Whisper的reclassmate、bake-off仅按Feishu/Qwen共同支持的明确技术近音规范为retransmit、backoff。

## 02 · 00:00:29 · 退避过程与竞争窗口指数表达式

稳定块ID：doxcn7SsOH6o33jPzXgM5V6cyXd
原块SHA256：775578c71881795185e4a73cd7bff496718ffd04099f8ce956ce907abb34eda9
候选SHA256：8008d764ec891b6f15b23d6e2c077ab5cd8bab60b66c42f7df73c146e0aa1709

### 具体修改

1. 原：We explained how the backoff procedure works. First,
   候选：And we explained how the backoff procedure works. Okay? Now, we [said/send unclear] that first
   理由：恢复开头And、Okay与Now, we said that；旧稿删掉了讲者的连接和回指。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
2. 原：Then it will draw an integer out of a range of possible values, selecting each of them with equal probability.
   候选：Then [it/you unclear] will draw an integer out of a range of possible values with equal probability, selecting each of them with equal probability.
   理由：恢复两遍with equal probability；三方都支持这次重复，不把第二分句当多余。代词冲突另留标记。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
3. 原：This range goes from zero to the contention window parameter.
   候选：And this range of values goes from zero to the contention window parameter, okay?
   理由：恢复And、of values和okay。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
4. 原：we set this parameter to its minimum value.
   候选：we set this contention window parameter to its minimum value.
   理由：恢复重复说出的contention window，不用this parameter概括。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
5. 原：If we need to perform backoff again to transmit this packet
   候选：And then, if we need to perform the backoff procedure again in order to transmit this packet
   理由：恢复And then、the backoff procedure、in order to的完整措辞。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
6. 原：every time we increase the contention window.
   候选：every time we will increase the value of contention window.
   理由：恢复will及the value of，保留原口语结构。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
7. 原：We said that, roughly speaking, this value doubles every time.
   候选：And we said, roughly speaking, this value of contention window doubles every time, right?
   理由：恢复And、of contention window与right；Feishu此句不全，完整后半由Qwen和新Whisper补足。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=11–12, absolute=116.56–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
8. 原：To be more precise, the relation according to which CW increases is the following.
   候选：Now, to be more precise, the relation according to which the CW parameter increases is the following.
   理由：恢复Now与the CW parameter。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
9. 原：The CW value is expressed as a power of two minus one, where this exponent is called the backoff exponent.
   候选：So, CW value is actually expressed as a power of two minus one, where this exponent is called backoff exponent.
   理由：恢复So、actually及无the的backoff exponent；用相邻窗补出指数名，不把新窗开头视为03内容。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1, absolute=165–178.2s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
10. 原：First, a node needs to wait
   候选：Now, we [said/send unclear] that first a node needs to wait
   理由：Now, we said that由Feishu和新Whisper共同支持；Qwen的send为单来源异文，正文保留简洁待听辨，不把两种候选等权或靠语法裁定。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）

### 逐单元证据

1. And we explained how the backoff procedure works.
而且我们解释过退避过程是怎样工作的。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
2. Okay?
好吗？
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）
   限制：Okay在Feishu和Qwen中存在；新Whisper未转出，问号仅为书面断句。
3. Now, we [said/send unclear] that first a node needs to wait for the channel to be idle for DIFS.
现在，我们[“说过/发送”待听辨]，首先一个节点需要等待信道空闲一个 DIFS。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=3–4, absolute=29–51.1s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
   限制：said有Feishu和新Whisper共同支持，send仅见Qwen；候选不是等可信。DIFS为技术近音候选：Feishu dips、Qwen this、新Whisper bifs；均未经听音认证。
4. Then [it/you unclear] will draw an integer out of a range of possible values with equal probability, selecting each of them with equal probability.
然后[它/你待听辨]会以相等的概率从一组可能的值中抽取一个整数，以相等的概率选择其中的每一个。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
   限制：Feishu和Qwen为it，新Whisper为you；保留代词待听辨。
5. And this range of values goes from zero to the contention window parameter, okay?
而且这个取值范围从零到竞争窗口参数，好吗？
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=5–7, absolute=51.1–79s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
6. The first time that we use the backoff procedure to transmit a packet, we set this contention window parameter to its minimum value.
第一次我们使用退避过程来发送一个数据包时，我们把这个竞争窗口参数设为它的最小值。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
7. And then, if we need to perform the backoff procedure again in order to transmit this packet, because, for example, we fail and fail and fail, every time we will increase the value of contention window.
然后，如果我们需要再次执行退避过程来发送这个数据包，因为，例如，我们失败、失败、再失败，每一次我们都会增大竞争窗口的值。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=0, absolute=0–120s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=7–12, absolute=79–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
8. And we said, roughly speaking, this value of contention window doubles every time, right?
而且我们说过，粗略地说，竞争窗口的这个值每次都会翻倍，对吧？
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=11–12, absolute=116.56–129s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
9. Now, to be more precise, the relation according to which the CW parameter increases is the following.
现在，更准确地说，CW 参数据以增大的关系是下面这个。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）
10. So, CW value is actually expressed as a power of two minus one, where this exponent is called backoff exponent.
所以，CW 的值实际上表示为二的一个幂减一，其中这个指数叫作退避指数。
   来源：Feishu历史快照 source_index_one_based=2（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=12–14, absolute=129–165.16s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1, absolute=165–178.2s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   限制：Feishu在power of two处截断；minus one及backoff exponent由Qwen和新Whisper跨chunk-001/002互补，未把窗口重叠重复计入。

## 03 · 00:02:48 · 最小退避指数与CW为31的例子

稳定块ID：doxcnUQ7t1Sai3ADMWsg75dZvye
原块SHA256：e959ab818f3cee68f0ecf47bcc72fa0d64e9bf72840bcab95d2a29801c18ffb1
候选SHA256：8b4ebc5078df9f9335fcffab5363e703e93d8a160c307bb20a153c7212f4b2f7

### 具体修改

1. 原：For example, the first time we use the backoff procedure for a data packet, we set the backoff exponent to its minimum.
   候选：Okay? So, for example, the first time that we use the backoff procedure for a data packet, we set the, so the first time, we set the backoff exponent to the backoff exponent minimum, okay?
   理由：恢复Okay、So、that、we set the的中断与so the first time的重新起句，恢复重复的backoff exponent及minimum位置；三方可交叉支持。
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=15–16, absolute=167.54–194.5s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
2. 原：By default, in the early versions of Wi-Fi, this is equal to five.
   候选：Now, by default, in the early versions of Wi-Fi, this is equal to five, okay?
   理由：恢复Now和okay；不把新Whisper的phi phi/phi当成原词。
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
3. 原：This example refers to the early versions of Wi-Fi.
   候选：This is an example that refers to the early versions of Wi-Fi, okay?
   理由：恢复This is an example that...和okay，撤回缩写句式。
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
4. 原：If we take this example value, we see that
   候选：Now, so, if we take this example here, this example value here, we see that
   理由：恢复Now, so和this example here / this example value here两次指代及here。
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
5. 原：Since this is five, it will be two to the five minus one, which is 31.
   候选：Since this is five, right, this will be two to the five minus one, which is 31, right?
   理由：恢复this而非it，并恢复两次right。
   来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
6. 原：That is why on Saturday, when we introduced this procedure, we said: let's consider the minimum contention window 31.
   候选：So that's why, yes, on Saturday, when we [introduce/produce tense unclear] this procedure, we said, well, let's consider the minimum contention window 31, okay?
   理由：恢复So、yes、well与okay；词根/时态不一致，撤回未经证实的introduced，明确待听辨。
   来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=9–10, absolute=267.8–290.5s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
7. 原：The second time we use backoff for the same packet, we are going to increase the backoff exponent.
   候选：Then, the second time that we use the backoff procedure for the same packet, we are going to increase the backoff exponent.
   理由：恢复Then、that及the backoff procedure。
   来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
8. 原：If this was our first value, the second time we will have a second value equal to the previous one plus one.
   候选：So, if this was our first value, the second time, [sorry unclear], we'll have second value, right, that is equal to what, is equal to the previous one plus one.
   理由：恢复So、right及that is equal to what, is equal to重复；删除旧校订额外补入的a，不把second value改成标准语法。sorry列待听辨。
   来源：Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）

### 逐单元证据

1. Okay?
好吗？
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）
2. So, for example, the first time that we use the backoff procedure for a data packet, we set the, so the first time, we set the backoff exponent to the backoff exponent minimum, okay?
所以，例如，第一次我们对一个数据包使用退避过程时，我们设置这，所以第一次，我们把退避指数设为退避指数最小值，好吗？
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-001, segment=15–16, absolute=167.54–194.5s; absolute_offset_seconds=0（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
3. Now, by default, in the early versions of Wi-Fi, this is equal to five, okay?
现在，默认地，在早期版本的 Wi-Fi 中，这等于五，好吗？
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
4. This is an example that refers to the early versions of Wi-Fi, okay?
这是一个指的是早期版本的 Wi-Fi 的例子，好吗？
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=1–4, absolute=165–220.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
5. Now, so, if we take this example here, this example value here, we see that, as we said last time, the first time that we use this contention window minimum, the value will be two to the power of the minimum exponent minus one.
现在，所以，如果我们采用这里的这个例子，这里的这个示例值，我们看到，正如我们上次说过的，第一次我们使用这个竞争窗口最小值时，这个值会是二的最小指数次方减一。
   来源：Feishu历史快照 source_index_one_based=3（原快照文本，可能已编辑）；Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=1, absolute=110–230s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   限制：Feishu的first time与Exponent之间缺文字；Qwen完整窗口和新Whisper共同补足that we use this contention window minimum, the value will be two to the power of the minimum。
6. Since this is five, right, this will be two to the five minus one, which is 31, right?
因为这是五，对吧，这会是二的五次方减一，也就是 31，对吧？
   来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=5–8, absolute=221–267.8s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
7. So that's why, yes, on Saturday, when we [introduce/produce tense unclear] this procedure, we said, well, let's consider the minimum contention window 31, okay?
所以这就是为什么，是的，在星期六，当我们[“介绍/产生”及其时态待听辨]这个过程时，我们说，嗯，让我们考虑最小竞争窗口 31，好吗？
   来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=9–10, absolute=267.8–290.5s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   限制：Feishu为introduce，Qwen为produced，新Whisper为produce；不能延用旧校订的introduced而掩盖词根与时态冲突。
8. Then, the second time that we use the backoff procedure for the same packet, we are going to increase the backoff exponent.
然后，第二次我们对同一个数据包使用退避过程时，我们要增大退避指数。
   来源：Feishu历史快照 source_index_one_based=4（原快照文本，可能已编辑）；Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
9. So, if this was our first value, the second time, [sorry unclear], we'll have second value, right, that is equal to what, is equal to the previous one plus one.
所以，如果这是我们的第一个值，第二次，[“抱歉”待听辨]，我们会有第二个值，对吧，它等于什么，等于前一个值加一。
   来源：Feishu历史快照 source_index_one_based=5（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=10–13, absolute=276.7–326.08s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
   限制：恢复that is equal to what, is equal to这一口语自问重述；sorry只有Feishu转出，不能静默删去或当作已证实。

## 04 · 00:05:24 · 第二次退避的竞争窗口计算

稳定块ID：doxcnSFMtuDH3wqf3m1ZJ1FECpf
原块SHA256：ea085ff66e253445fc86e6a20532bcb984860b247441186bc99b8142c211359e
候选SHA256：b38f10ce4ae0dca7c29517d1a58f79f5c83723d72e209b934b7abf35fe5b84d2

### 具体修改

1. 原：This means that the second time we compute the contention window, it will equal
   候选：Okay? So this means that the second time that we have to compute the contention window, this will be equal to
   理由：恢复Okay、So、that we have to和this will be equal to，撤回缩写和代词替换。
   来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
2. 原：two to the power of the backoff exponent at the second step, minus one.
   候选：two to the power of the, the backoff exponent [on/at unclear] the second step minus one,
   理由：恢复重复的the, the；原来源介词有on/at冲突，不沿用旧稿at。
   来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=1–2, absolute=345–360.66s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. 原：This is two to the power of the exponent at the first step increased by one, minus one.
   候选：which is two to the backoff exponent [on/at unclear] the first step increased by one minus one, right?
   理由：恢复which is连接、backoff及right；移除原话未见的第二个power of，保留不规整的口头数学表述。
   来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=1–2, absolute=345–360.66s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）

### 逐单元证据

1. Okay?
好吗？
   来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）
2. So this means that the second time that we have to compute the contention window, this will be equal to two to the power of the, the backoff exponent [on/at unclear] the second step minus one, which is two to the backoff exponent [on/at unclear] the first step increased by one minus one, right?
所以这意味着，第二次我们必须计算竞争窗口时，这会等于二的这个、这个[on/at 介词待听辨]第二步的退避指数次方减一，这就是二的“[on/at 介词待听辨]第一步的退避指数加一”次方减一，对吧？
   来源：Feishu历史快照 source_index_one_based=6（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=2, absolute=220–340s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=13–16, absolute=312.78–360.6s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=1–2, absolute=345–360.66s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   限制：on/at两处：Feishu及新Whisper为on，Qwen为at；留标记，不把口语介词统一。backoff为cost/Bechov/cot/cub的技术近音恢复；the, the有Feishu与Qwen共同支持。

## 05 · 00:06:01 · 窗口增至63并受CW最大值限制

稳定块ID：doxcn3oscwOg3HvqxY1TQD4dKfb
原块SHA256：13ba4eaae4467afea715f5223ef0d8f0ca36d1ec383951072f42648567c619f3
候选SHA256：a57ffb475e584f9b4a49adac3be5c9198f22176e5108c53117018f92222f91fb

### 具体修改

1. 原：In our example this is two to the power of six minus one, which is 63.
   候选：So now this is two to the power, in our example, to the power of six minus one, which is 63, okay?
   理由：恢复So now、this is的位置及两次to the power；不将口头中断合并成干净公式。
   来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=17, absolute=361.14–373.98s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. 原：This is the way we increase the contention window minimum value every time until we reach CW_max.
   候选：So this is the way we increase the contention window minimum value every time till, as we said, we reach this value, CW max.
   理由：恢复So、till、as we said及this value；保留minimum value，即使技术上显得不严谨。
   来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. 原：After reaching this value, we do not increase CW beyond it
   候选：After we reach this value, we do not increase [the/this unclear] CW value any longer [beyond/behind unclear] this value
   理由：恢复完整从句、CW value、any longer及再次说出的this value；the/this与beyond/behind来源冲突留待听辨，不用语义选词。
   来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
4. 原：even if we still need to perform backoff for the same packet.
   候选：even if we need to still perform the backoff procedure for the same time.
   理由：恢复need to still的词序、the backoff procedure与三方一致的same time；不以技术语义把time改成packet。
   来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）

### 逐单元证据

1. So now this is two to the power, in our example, to the power of six minus one, which is 63, okay?
所以现在这是二的次方，在我们的例子中，是六次方减一，也就是 63，好吗？
   来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-002, segment=17, absolute=361.14–373.98s; absolute_offset_seconds=165（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. So this is the way we increase the contention window minimum value every time till, as we said, we reach this value, CW max.
所以这就是我们每次增大竞争窗口最小值的方式，直到，正如我们说过的，我们达到这个值，CW max。
   来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. After we reach this value, we do not increase [the/this unclear] CW value any longer [beyond/behind unclear] this value, even if we need to still perform the backoff procedure for the same time.
在我们达到这个值之后，我们不再把[限定词待听辨] CW 值增大到这个值的[以上/后面待听辨]，即使我们还需要为同一次执行退避过程。
   来源：Feishu历史快照 source_index_one_based=7（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=3–7, absolute=361.26–432.15s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   限制：三方均为for the same time，原词保留。CW前the/this及beyond/behind有文字冲突，正文留标记，不按多数或技术意义选择。

## 06 · 00:06:57 · 退避指数逐次加一的规则

稳定块ID：doxcn89Uuu4pPtyRwDp131FVbVb
原块SHA256：5aee0f606bcff550fd1172c8ff24858506cdbd756389748a54678e20ad886222
候选SHA256：bf936a6900a50a545d310a4b6dd5774dba9ec69912d47ba3b1ccbd0b82cadac3

### 具体修改

1. 原：The general rule is that
   候选：So, the general, [ah unclear] the general rule is that
   理由：恢复So和重复的the general；ah单来源留待听辨。
   来源：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=7–8, absolute=412.35–447.83s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. 原：we set the backoff exponent equal to the exponent at the previous step increased by one.
   候选：we set the backoff exponent [at/as unclear] step i equal to the backoff exponent [at/and unclear] the previous step increased by one, right?
   理由：恢复at step i位置及第二遍backoff exponent、right；介词冲突不直接修成标准语法。
   来源：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=7–8, absolute=412.35–447.83s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）

### 逐单元证据

1. So, the general, [ah unclear] the general rule is that at step i, the generic step i, we set the backoff exponent [at/as unclear] step i equal to the backoff exponent [at/and unclear] the previous step increased by one, right?
所以，一般的，[语气词待听辨]一般规则是，在第 i 步，任意的第 i 步，我们把[在/作为待听辨]第 i 步的退避指数设为[在/以及待听辨]前一步的退避指数增加一，对吧？
   来源：Feishu历史快照 source_index_one_based=8（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=7–8, absolute=412.35–447.83s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   限制：重复the general有Feishu与Qwen支持；ah仅Qwen转出。第一介词at/as、第二介词at/and分歧保留；不把来源不稳的口语语法悄悄规范化。

## 07 · 00:07:28 · 竞争窗口扩大与随机取值范围

稳定块ID：doxcnJ4V6DfRd4wtrg1ZLZ38BQd
原块SHA256：0544d3b629146ba8af5055fa7ae2bbdaaf7f407c0debd88b7836970453752be0
候选SHA256：4fd4e610005070fdfaa67badc11efc99fe63a1226c07823745119fdc7896c026

### 具体修改

1. 原：At the generic step i, the contention window is computed
   候选：And at the generic step i, the contention window will be computed
   理由：恢复And与will be，保留原将来时。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. 原：This is the general expression used to compute the backoff exponent and the corresponding contention window at each step.
   候选：Okay, this is the general expression that we use to compute the, the backoff exponent and the corresponding contention window at each step.
   理由：恢复Okay、that we use及the, the重复；backoff是多次技术近音的统一拼写，不是改写句法。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. 原：Every time we need to perform backoff for a given data packet, we roughly double the contention window.
   候选：Okay, that said, therefore we understand that [every time/at every time unclear] that we need to perform the backoff for a given data packet, we roughly double the contention window, as we said.
   理由：恢复被删掉的Okay, that said, therefore we understand that、that、the及as we said；at分歧留待听辨。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
4. 原：We enlarge the possible integer values that we can draw to compute the backoff time.
   候选：Okay, so we are going to [enlarge/launch unclear] the possible values, integer values, that we can draw to compute [backoff repetition unclear] time.
   理由：恢复Okay, so、are going to及possible values, integer values的重复重述；backoff重复是否实说列待听辨。 enlarge有Feishu和新Whisper共同支持、launch仅为Qwen异文，正文另留待听辨。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
5. 原：Before explaining why the standard says to double the contention window every time we need to perform backoff to transmit a packet, let me mention something reported in one of the earlier slides.
   候选：Okay, so before explaining why we do that, okay, why the [standard said/standards say unclear] let's double the contention window every time we need to perform a backoff to transmit [a/the unclear] packet. So before explaining the reason because we do that, let me mention what was reported in one of the earlier slides.
   理由：撤回把两次before explaining压成一句的处理；恢复why we do that、第二个okay、let’s、the reason because we do that及what was reported；保留词法/时态冲突。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=15–18, absolute=513.05–547.99s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=1–3, absolute=525–550.16s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）

### 逐单元证据

1. And at the generic step i, the contention window will be computed as two to the power of the backoff exponent at step i minus one.
而且在任意的第 i 步，竞争窗口将被计算为二的第 i 步的退避指数次方减一。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=3, absolute=330–450s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
2. Okay, this is the general expression that we use to compute the, the backoff exponent and the corresponding contention window at each step.
好，这就是我们用来计算每一步的这个、这个退避指数和相应竞争窗口的一般表达式。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=9–11, absolute=448.47–482.29s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
3. Okay, that said, therefore we understand that [every time/at every time unclear] that we need to perform the backoff for a given data packet, we roughly double the contention window, as we said.
好，说到这里，因此我们明白，[“每一次”前介词待听辨]我们需要对一个给定的数据包执行退避时，我们大致把竞争窗口翻倍，正如我们说过的。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   限制：every time前是否有at：仅Qwen含at；保留词序待听辨。
4. Okay, so we are going to [enlarge/launch unclear] the possible values, integer values, that we can draw to compute [backoff repetition unclear] time.
好，所以我们要[“扩大/发起”待听辨]那些可能的值，整数值，我们可以抽取它们来计算[“退避”的重复待听辨]时间。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=12–14, absolute=483.71–513.05s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）
   限制：enlarge有Feishu和新Whisper共同支持，launch仅见Qwen，不表示两者等可信。Qwen另为the because the because time，另两来源未明确转出双重backoff；重复仍待听辨。
5. Okay, so before explaining why we do that, okay, why the [standard said/standards say unclear] let's double the contention window every time we need to perform a backoff to transmit [a/the unclear] packet.
好，所以在解释我们为什么这样做之前，好，为什么[“标准说”的单复数和时态待听辨]让我们每次需要执行一次退避来发送[一个/这个待听辨]数据包时把竞争窗口翻倍。
   来源：Feishu历史快照 source_index_one_based=9（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=15–18, absolute=513.05–547.99s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=1–3, absolute=525–550.16s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
   限制：保留这一口语未闭合的before explaining句，不改写为顺畅主句。standard(s)、said/say及packet冠词都有冲突。
6. So before explaining the reason because we do that, let me mention what was reported in one of the earlier slides.
所以在解释因为我们这样做的原因之前，让我提一下前面一张幻灯片中报告过的内容。
   来源：Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=15–18, absolute=513.05–547.99s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=1–3, absolute=525–550.16s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
   限制：该完整重复起句来自Qwen和两个新Whisper重叠窗口；Feishu 09止于上句，Feishu 10从But I didn’t comment开始。按内容接回，不因旧锚点截去。

## 08 · 00:09:04 · 发送失败时的退避回顾

稳定块ID：doxcnHZ5g5teuPb75H042YGavgb
原块SHA256：31fb3d36c89d426bb56eac5981d0f8dc4c8689b7bf4681d4b0f660a8ccef91ed
候选SHA256：f17ac5150e09945243fba63c72342bf576a1135ab729633eba7820da2072fa0d

### 具体修改

1. 原：I didn't comment on that because I didn't want to put too many things together at the same time.
   候选：But I didn't comment on that because I didn't want to put too many things at the same time.
   理由：恢复句首But；三方均无together，移除旧校订增词。
   来源：Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=18–19, absolute=540.59–554.97s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
2. 原：One more important thing to say about backoff is that
   候选：But one more thing that we need to say important about the backoff is that the backoff procedure
   理由：恢复But、that we need to say important的原词序、the backoff和再次说出的the backoff procedure；不调换important以润色。
   来源：Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
3. 原：when we have a packet that has been transmitted and failed.
   候选：when we have essentially a packet, right, that has been transmitted and it failed.
   理由：恢复essentially、right及and it failed的独立主语与过去时；不把failed并入has been的并列结构。
   来源：Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-004, segment=6 word, absolute=570.82–579.86s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）

### 逐单元证据

1. But I didn't comment on that because I didn't want to put too many things at the same time.
但我没有对此作解释，因为我不想同时放入太多事情。
   来源：Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-003, segment=18–19, absolute=540.59–554.97s; absolute_offset_seconds=345（相对时间加offset；未经人工听辨）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
2. But one more thing that we need to say important about the backoff is that the backoff procedure, of course, it is performed, as we said, when we have essentially a packet, right, that has been transmitted and it failed.
但还有一件我们需要说的重要的关于退避的事情，是退避过程，当然，它会被执行，正如我们说过的，当我们基本上有一个数据包，对吧，它已经被发送了，而且它失败了。
   来源：Feishu历史快照 source_index_one_based=10（原快照文本，可能已编辑）；Qwen原始恢复重跑 chunk_index=4, absolute=440–560s（完整窗口；非丢失的首次输出）；Qwen原始恢复重跑 chunk_index=5, absolute=550–670s（完整窗口；非丢失的首次输出）；新无提示Whisper medium.en chunk-004, segment=3–6, absolute=542.32–581.24s; absolute_offset_seconds=525（相对时间加offset；未经人工听辨）
   限制：保留thing that we need to say important、the backoff procedure ... it及has been transmitted and it failed，不以标准书面语改写。Feishu到as we said，后面的条件由Qwen和新Whisper补足；so we归09。

## 09 · 00:09:40 · 新包到达但侦听到忙信道

稳定块ID：doxcnvRjxRufvfMiuNnxSymfMlh
原块SHA256：72da87b0e1a669253f8f3f17fc1da94bb9b80d92d390a38a72a1b2c27a9323f9
候选SHA256：e6c46c08e10bbe75166c0d57bf9b5b7f889fe2bfc39d14a9c306ce5e4545c0e0

### 具体修改

1. 原：exactly the same backoff procedure
   候选：a backoff procedure ... Exactly as we explained ... The same procedure that we just explained
   理由：恢复原飞书、校订前Qwen、新独立短窗均有的两个完整重复从句；不再压缩表达
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new base/small/medium unprompted 09:10–11:50 sample
2. 原：We get a packet
   候选：we got [a/the unclear] packet
   理由：恢复三个来源共同的got，不替讲者改时态；冠词冲突保留
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
3. 原：in which
   候选：under which
   理由：旧两来源和新medium均为under which，两处恢复
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
4. 原：It also needs to be performed
   候选：This procedure indeed needs to be performed also
   理由：恢复主语、indeed和also的原位置
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
5. 原：a transmitting node has a packet
   候选：a node, a transmitter [wording unclear], has got a packet
   理由：恢复has got；节点称呼不凭语法润色决定，按新medium候选保留并标来源冲突
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
6. 原：senses the channel, and finds it busy
   候选：It senses the channel, but the channel is busy, right?
   理由：恢复原叙述、转折和尾问，不用finds改写
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
7. 原：We get a packet from the higher layers
   候选：So, if we sense the channel, we got [a/the unclear] packet from the higher layers
   理由：恢复被删的条件开头及口语结构，不修成更顺的句子
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
8. 原：carrier-sense multiple-access principle
   候选：carrier sensing multiple access principle
   理由：恢复原词形sensing，而非只统一连字符
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json
9. 原：What we knew so far is that we cannot access the channel because it is busy.
   候选：So, what we knew so far is that in this case, we cannot ... right? Because the channel is busy.
   理由：恢复So、in this case、right及重复名词；末句分开遵循两ASR，非合并简写
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
10. 原：who is already talking
   候选：who is talking already
   理由：旧Qwen和新medium一致，恢复词序
   来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
11. 原：（空）
   候选：case/phase、两个okay、node/transmitter、a/the冠词及末尾okay/right待听辨标记
   理由：来源冲突不能通过猜测消除；明确范围，候选不冒称准确逐字稿
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json

### 逐单元证据

1. So, we need to recontend for the channel and transmit the packet again, right?
所以，我们需要重新竞争信道，并且再次传送这个数据包，对吧？
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 580–587s
2. This is the [case/phase unclear] that we have considered so far, under which we need to perform the backoff.
这就是我们到目前为止考虑过的这个〔case/phase，情况/阶段，待听辨〕，在这种情况下，我们需要执行这个退避。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 586.66–601.58s
   限制：原飞书及旧Qwen均case，新三路短窗及全文medium均phase；不能以新ASR多数机械推翻旧来源，保留词级待听辨
3. However, there are two more situations under which we need to perform a backoff procedure, [okay? unclear]
不过，还有另外两种情况，在这些情况下，我们需要执行一个退避过程，〔okay?，好吗？待听辨〕
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 592.8–610s
   限制：末尾okay只见原飞书，旧Qwen与新无提示medium未转出，暂显式标记而不无痕删除或确认
4. Exactly as we explained, [okay? unclear]
正如我们解释过的那样，〔okay?，好吗？待听辨〕
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 601.58–610s
   限制：从句三方支持；末尾okay只见原飞书，待听辨
5. The same procedure that we just explained.
就是我们刚刚解释过的同一个过程。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en 09:10–11:50 sample raw；new unprompted base.en/small.en 09:10–11:50 sample raw
   限制：全文medium此处just this way误识；F、Qwen及新独立短窗支持just explained，因此保留完整从句
6. This procedure indeed needs to be performed also when a node, a transmitter [wording unclear], has got a packet to transmit.
这个过程确实也需要在一个节点、一个发送方〔此处措辞待听辨〕有了一个要传送的数据包时执行。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 610–633.44s；new unprompted medium.en 09:10–11:50 sample raw
   限制：新medium两种窗均支持a node, a transmitter；原飞书one and node transmitter、Qwen a known transmitter不清。保留候选结构并明确标注，不能改写成a transmitting node
7. It senses the channel, but the channel is busy, right?
它侦听信道，但是信道是忙的，对吧？
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 624.38–644.71s
   限制：senses由原飞书与新medium支持；Qwen sends是近音。新全文medium漏第二个channel，原飞书、Qwen及新small短窗保留，故补回
8. So, we already know that in this case, we cannot access the channel right away because of the carrier sensing multiple access principle, right?
所以，我们已经知道，在这种情况下，因为载波侦听多址接入的原则，我们不能马上接入信道，对吧？
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 634.03–652.13s
9. So, if we sense the channel, we got [a/the unclear] packet from the higher layers.
所以，如果我们侦听信道，我们从更高层拿到了〔a/the，冠词待听辨〕数据包。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 644.71–659.23s
   限制：got三方明确；原飞书及新全文medium是the，旧Qwen为a。保留got及条件开头，不改成get；冠词显式待听辨
10. At the MAC layer, we sense the channel for DIFS, but the channel is busy, [okay/right unclear]
在MAC层，我们侦听信道一个DIFS的时间，但是信道是忙的，〔okay/right，好吗/对吧，待听辨〕
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00005.json 550–670s；new unprompted medium.en full-run chunk-004.raw.json 652.13–669.69s
   限制：MAC/DIFS是明确Wi-Fi术语近音归一：旧mark/for this，新max/for this。未据此改句式；尾问原Feishu、旧Qwen、新medium短窗及全文为okay，但small短窗655.94–668.02s为right，base未保留，故显式[okay/right unclear]
11. So, what we knew so far is that in this case, we cannot access the channel, right?
所以，我们到目前为止知道的是，在这种情况下，我们不能接入信道，对吧？
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L72；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 659.23–677.39s
12. Because the channel is busy.
因为信道是忙的。
   来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 670.67–677.39s
13. We are like polite people.
我们就像有礼貌的人。
   来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 670.67–677.39s
14. We don't want to interrupt someone who is talking already.
我们不想打断一个已经在讲话的人。
   来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 677.39–687.43s

## 10 · 00:11:21 · 忙信道情况下等待的具体含义

稳定块ID：doxcnPqzDaGsf13GV71CGVfXjmh
原块SHA256：a7fec0aef2159d772f72c52411a6fd17caecacf4fe4ea7403d9e0f1fff5e544e
候选SHA256：3327651ea66e24e68295bd0c074a4c0248460af3595abad9bac41d15e241bbc2

### 具体修改

1. 原：So we wait.
   候选：So, we wait. We wait.
   理由：恢复旧Qwen与新medium单窗内共有的第二次We wait；不是上下文窗拼接重复
   来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
2. 原：what exactly do we mean by waiting, and for how long?
   候选：What do we mean exactly that we need to wait? [question wording unclear] For how long?
   理由：恢复原有问句词序和两个问句，保留措辞冲突而不润色为by waiting
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
3. 原：In reality, also in this case we need to apply
   候选：Well, in reality, also in this case, what we need to do is to apply
   理由：恢复Well、what we need to do is以及重复解释结构
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json
4. 原：We wait for the backoff time according to this procedure.
   候选：So, how long do we wait for? We will wait for the backoff time, according to this procedure.
   理由：恢复被删的完整问句和will，不把再次提问压掉
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json；new unprompted medium.en full-run chunk-005.raw.json
5. 原：This is the rule again also in this first case, when a Wi-Fi node gets a new packet
   候选：So, this is the rule again. Also in this first case, when we have that the node, Wi-Fi node, gets a new packet
   理由：恢复So、分句和when we have that/the node, Wi-Fi node口语；不改成语法更流畅的简写
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json
6. 原：and the MAC needs to apply the protocol to transmit it
   候选：And the MAC needs to apply the protocol in order to transmit that packet
   理由：恢复in order to、that packet及讲者的And开句；MAC技术近音按Qwen及上下文校正
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json

### 逐单元证据

1. So, we wait.
所以，我们等着。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 677.39–687.43s
2. We wait.
我们等着。
   来源：Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 677.39–687.43s
   限制：原飞书只一次；旧Qwen与新medium在各自同一窗口内部均有两次，不是将重叠窗口拼接形成的重复，恢复第二次；仍未人工听辨
3. That's what we said, but now we need to be more precise.
我们之前就是这么说的，但是现在我们需要更精确一些。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 687.43–695.45s
4. What do we mean exactly that we need to wait? [question wording unclear]
我们说需要等着，到底是什么意思？〔问句的确切措辞待听辨〕
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 687.43–704.87s
   限制：新medium为What do we mean exactly that we need to wait，原飞书do we mean exactly that we need to wait，Qwen为What do we do? We mean exactly that we need to wait；保留较完整候选并显式标疑，不替讲者改写为what exactly do we mean by waiting
5. For how long?
等多久？
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 695.45–704.87s
   限制：F和Qwen为for how long；新medium此窗为or how long，按旧双源保留for，不静默合并上一问句
6. Well, in reality, also in this case, what we need to do is to apply the backoff procedure.
嗯，实际上，在这种情况下也是，我们需要做的就是应用退避过程。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 695.45–714.71s；new unprompted medium.en full-run chunk-005.raw.json 705–715.32s
7. So, how long do we wait for?
那么，我们要等多久呢？
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 704.87–714.71s；new unprompted medium.en full-run chunk-005.raw.json 705–715.32s
8. We will wait for the backoff time, according to this procedure.
我们会按照这个过程，等待这个退避时间。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 714.71–723.27s；new unprompted medium.en full-run chunk-005.raw.json 715.32–723.52s
9. So, this is the rule again.
所以，这又是这个规则。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-004.raw.json 714.71–723.27s；new unprompted medium.en full-run chunk-005.raw.json 715.32–723.52s
10. Also in this first case, when we have that the node, Wi-Fi node, gets a new packet from the higher layers.
在这第一种情况下也是，当这个节点，Wi-Fi节点，从更高层拿到一个新的数据包时。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json 724.58–744.3s
   限制：保留讲者when we have that和node, Wi-Fi node口语结构；不改成流利单句
11. And the MAC needs to apply the protocol in order to transmit that packet.
并且MAC需要应用这个协议，才能传送那个数据包。
   来源：Feishu snapshot commit08e6132759c37f035f9b7e6cf6d2b41541d832c8, originals/20261012-1331.md L77,L82；Qwen recovery commit01aeac5480cfa30a6393b2719f9393cbfdf82553, chunk_00006.json 660–780s；new unprompted medium.en full-run chunk-005.raw.json 733.18–750.02s
   限制：原飞书mark、新medium mask，Qwen明确MAC；依技术近音与旧Qwen归一。that由原飞书、新medium支持，Qwen the

## 11 · 00:12:27 · 退避计数递减、冻结与恢复

稳定块ID：doxcnxO1XrFqJ8vDuFhY9nCToXb
原块SHA256：6d12f435de26c268f0d80fa59f37f32e270fb5895be7391f4e9130ade9cb6303
候选SHA256：98f12e01c7170f0b6abee3f1297cafd4fde3a00d93c7a4fb0443ee9c6a87ca5e

### 具体修改

1. 原：First we need to sense the channel for DIFS.
   候选：So, we know that first of all, we need to sense the channel for DIFS.
   理由：恢复原来的起句与 first of all；只将技术近音 this/dips 规范为 DIFS。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 5–6, relative 39.30–56.42s + offset 705s = absolute 744.30–761.42s
2. 原：If the channel is sensed busy, we apply backoff.
   候选：If the channel is sense busy, then what [we’ll / we unclear] do is apply the backoff.
   理由：撤销语法润色和压缩；原始识别保留 is sense busy；未来/现在式冲突不擅选。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 6–7, relative 45.02–64.58s + offset 705s = absolute 750.02–769.58s
3. 原：First we wait for it to become idle again and sense it as idle for DIFS.
   候选：That is, first of all, we need to wait for the channel to become idle again, and sense the channel idle for DIFS.
   理由：恢复 That is、we need to、the channel 的重复及原句式。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 7–8, relative 56.42–75.90s + offset 705s = absolute 761.42–780.90s
4. 原：Then we draw an integer with equal probability from the range zero to CW_min, set the backoff time to that integer multiplied by the time slot
   候选：Then draw an integer with equal probability out of the range zero, CW_min, set that integer multiplied by the time slot as backoff time
   理由：恢复无主语 draw、out of 和 set that integer ... as 的措辞，不重组计算步骤。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 8–10, relative 64.58–96.12s + offset 705s = absolute 769.58–801.12s
5. 原：If the channel becomes busy while we are decreasing the counter, we need to stop and freeze it; we cannot decrease it.
   候选：If the channel becomes busy at a certain point, while we are still decreasing the backoff counter, we need to stop the counter, right? And freeze it; we cannot decrease it.
   理由：恢复 at a certain point、still、counter 重复及口头 right。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 10–12, relative 86.28–112.24s + offset 705s = absolute 791.28–817.24s
6. 原：When the channel becomes idle again, we sense it for DIFS. If it stays idle for that time, we resume decreasing the counter until it reaches zero.
   候选：And then, when the channel becomes idle again, we will sense the channel for DIFS. If it’s idle, of course, for that time, we will resume decreasing our backoff counter. Till we do that, till the counter reaches zero, right?
   理由：恢复两处 will、our、of course，以及 till ... till 的重复从句；不把未来式改成现在式。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 12–15, relative 102.30–140.68s + offset 705s = absolute 807.30–845.68s
7. 原：As soon as it reaches zero, we can access the channel and transmit our packet. The transmission may be successful, in which case we are done.
   候选：As soon as the counter reaches zero, then we can access the channel and transmit our packet. And then of course it depends. The transmission may be successful; that is fine, we are done.
   理由：恢复 the counter、then、被删的 it depends 及口语 that is fine，不以 in which case 替写。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 15–17, relative 132.30–151.66s + offset 705s = absolute 837.30–856.66s
8. 原：Or the packet may fail, and we must recontend for the channel using backoff.
   候选：Or the packet may fail, and in that case, we have to recontend for the channel by using the backoff [receiver / procedure unclear]. Right?
   理由：恢复 in that case、have to、by using 和句末词；receiver 与技术上可能的 procedure 不经音频不能裁决。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 17–18, relative 144.80–164.66s + offset 705s = absolute 849.80–869.66s
9. 原：Now we know two conditions under which we perform backoff.
   候选：Okay, so now we know that actually there are two conditions, one and two, under which we will perform the backoff.
   理由：恢复 actually、one and two、will 和连接语；Qwen/Whisper均为 and，Feishu误识别为 or。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 18–19, relative 151.90–176.32s + offset 705s = absolute 856.90–881.32s

### 逐单元证据

1. So, we know that first of all, we need to sense the channel for DIFS.
所以，我们知道，首先我们需要侦听信道一个 DIFS 的时间。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 5–6, relative 39.30–56.42s + offset 705s = absolute 744.30–761.42s
2. If the channel is sense busy, then what [we’ll / we unclear] do is apply the backoff.
如果信道被侦听为忙，那么[我们将要／我们，待听辨]做的就是执行退避。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Unprompted Whisper medium.en raw: chunk-005, segments 6–7, relative 45.02–64.58s + offset 705s = absolute 750.02–769.58s
   限制：Feishu and Whisper retain “is sense busy”; no grammatical repair to “is sensed busy”. The future/present wording before “do” differs across sources.
3. That is, first of all, we need to wait for the channel to become idle again, and sense the channel idle for DIFS.
也就是说，首先我们需要等信道再次变为空闲，并侦听信道空闲一个 DIFS 的时间。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 7–8, relative 56.42–75.90s + offset 705s = absolute 761.42–780.90s
4. Then draw an integer with equal probability out of the range zero, CW_min, set that integer multiplied by the time slot as backoff time, and then decrease the backoff counter slot by slot as long as the channel is idle.
然后从零、CW_min 这个范围中等概率地抽取一个整数，把那个整数乘以时隙设为退避时间，然后只要信道空闲，就逐个时隙递减退避计数器。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=6, absolute 660.00–780.00s；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 8–10, relative 64.58–96.12s + offset 705s = absolute 769.58–801.12s
5. If the channel becomes busy at a certain point, while we are still decreasing the backoff counter, we need to stop the counter, right?
如果信道在某个时刻变忙，而我们还在递减退避计数器，我们就需要停止计数器，对吧？
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 10–12, relative 86.28–112.24s + offset 705s = absolute 791.28–817.24s
6. And freeze it; we cannot decrease it.
并把它冻结；我们不能递减它。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 12–12, relative 102.30–112.24s + offset 705s = absolute 807.30–817.24s
7. And then, when the channel becomes idle again, we will sense the channel for DIFS.
然后，当信道再次变为空闲时，我们会侦听信道一个 DIFS 的时间。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 12–13, relative 102.30–121.94s + offset 705s = absolute 807.30–826.94s
8. If it’s idle, of course, for that time, we will resume decreasing our backoff counter.
当然，如果它在那段时间里是空闲的，我们就会恢复递减我们的退避计数器。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 13–14, relative 112.24–131.96s + offset 705s = absolute 817.24–836.96s
9. Till we do that, till the counter reaches zero, right?
直到我们这样做，直到计数器到达零，对吧？
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 14–15, relative 122.46–140.68s + offset 705s = absolute 827.46–845.68s
10. As soon as the counter reaches zero, then we can access the channel and transmit our packet.
计数器一到零，那么我们就可以接入信道并发送我们的数据包。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 15–15, relative 132.30–140.68s + offset 705s = absolute 837.30–845.68s
11. And then of course it depends.
然后，当然，这要看情况。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 16–16, relative 140.68–144.80s + offset 705s = absolute 845.68–849.80s
12. The transmission may be successful; that is fine, we are done.
这次传输可能成功；那很好，我们完成了。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 16–17, relative 140.68–151.66s + offset 705s = absolute 845.68–856.66s
13. Or the packet may fail, and in that case, we have to recontend for the channel by using the backoff [receiver / procedure unclear].
或者这个数据包可能失败，而在那种情况下，我们必须使用退避[接收器／过程，待听辨]来重新竞争信道。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 17–18, relative 144.80–164.66s + offset 705s = absolute 849.80–869.66s
   限制：All three recognitions give receiver or a near spelling; procedure is only a contextually plausible technical alternative, not established by these outputs.
14. Right?
对吧？
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 18–18, relative 151.90–164.66s + offset 705s = absolute 856.90–869.66s
15. Okay, so now we know that actually there are two conditions, one and two, under which we will perform the backoff.
好，所以现在我们知道，实际上有两种情况，第一种和第二种，在这些情况下我们会执行退避。
   来源：Feishu historical snapshot: source_index=14, id=31, section anchor 00:12:27；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Unprompted Whisper medium.en raw: chunk-005, segments 18–19, relative 151.90–176.32s + offset 705s = absolute 856.90–881.32s

## 12 · 00:14:39 · 用例子理解退避及窗口扩大原因

稳定块ID：doxcnWAgzkaE1V9NzLFbhdUxUsh
原块SHA256：4e78dfe8a2b1eabc9184b4eb9bdf50c37de08c5e79a49fee65b9ea54ca0911ff
候选SHA256：be6d1fca0b68a51dc6f73ff65ff71e747b09a5df046bb8b0e481d1af840fae53

### 具体修改

1. 原：Let's leave the third condition for later. Before introducing it, I want to present an example of a situation where we apply backoff.
   候选：Okay, let’s leave the third condition for later. Okay, before introducing the third condition, I want to present an example of a situation when we apply the backoff.
   理由：恢复 Okay、重复的 the third condition 及 when；不以 it 消除重复。
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 19–21, relative 164.66–198.06s + offset 705s = absolute 869.66–903.06s；Unprompted Whisper medium.en raw: chunk-006, segments 1–2, relative 1.46–22.14s + offset 885s = absolute 886.46–907.14s
2. 原：With this example, I want to clarify why we use backoff, why it is actually useful, and why the standard says
   候选：And what I want to do with this example is to clarify why, why we are using the backoff. Why is the backoff actually useful? Okay, and why the standard says
   理由：恢复完整引入从句、why why 重复、are using 进行式及独立问句，不合并列举。
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 21–22, relative 186.66–208.98s + offset 705s = absolute 891.66–913.98s；Unprompted Whisper medium.en raw: chunk-006, segments 2–4, relative 11.28–34.30s + offset 885s = absolute 896.28–919.30s
3. 原：every time we perform backoff for a given packet, we need to double the contention window parameter.
   候选：every time we perform the backoff for a given packet, we need to double the contention window parameter.
   理由：恢复 the；pattern/Bechov/window pattern仅作有来源支持的技术近音校正，不据此增添协议解释。
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 4–6, relative 24.70–49.18s + offset 885s = absolute 909.70–934.18s

### 逐单元证据

1. Okay, let’s leave the third condition for later.
好，我们把第三种情况留到后面。
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 19–20, relative 164.66–186.66s + offset 705s = absolute 869.66–891.66s
2. Okay, before introducing the third condition, I want to present an example of a situation when we apply the backoff.
好，在介绍第三种情况之前，我想给出一个我们执行退避的情况的例子。
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=7, absolute 770.00–890.00s；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 20–21, relative 176.32–198.06s + offset 705s = absolute 881.32–903.06s；Unprompted Whisper medium.en raw: chunk-006, segments 1–2, relative 1.46–22.14s + offset 885s = absolute 886.46–907.14s
3. And what I want to do with this example is to clarify why, why we are using the backoff.
而我想用这个例子做的，是说明为什么，为什么我们在使用退避。
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 21–22, relative 186.66–208.98s + offset 705s = absolute 891.66–913.98s；Unprompted Whisper medium.en raw: chunk-006, segments 2–3, relative 11.28–24.70s + offset 885s = absolute 896.28–909.70s
4. Why is the backoff actually useful?
退避实际上为什么有用？
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-005, segments 22–22, relative 198.06–208.98s + offset 705s = absolute 903.06–913.98s；Unprompted Whisper medium.en raw: chunk-006, segments 4–4, relative 24.70–34.30s + offset 885s = absolute 909.70–919.30s
5. Okay, and why the standard says that every time we perform the backoff for a given packet, we need to double the contention window parameter.
好，还有为什么标准说，每次我们为一个给定的数据包执行退避时，我们都需要把竞争窗口参数加倍。
   来源：Feishu historical snapshot: source_index=15, id=33, section anchor 00:14:39；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 4–6, relative 24.70–49.18s + offset 885s = absolute 909.70–934.18s
   限制：packet follows Feishu and the packet/backoff context; pattern in Qwen/Whisper is treated as a technical near-sound error. parameter is explicit in Feishu and Qwen.

## 13 · 00:15:26 · 学习技术机制背后的设计理由

稳定块ID：doxcnAxAESMqbsUmzgLpNkXu0hB
原块SHA256：dcc622357e0ecd7f79788c133b5f67920fa115c473b6636f0954c7174890f806
候选SHA256：e05e00fa110a7c25b9ac491c6d3628a1256598415facc8a2b189bcfa0fdb5a44

### 具体修改

1. 原：The main thing here, when we study Wi-Fi, is of course to learn how we use a technology that is used every day by almost everyone.
   候选：Okay, because the main thing here, when we study Wi-Fi, okay, is to, of course, learn how we use a technology that is actually used every day, right, by almost everyone.
   理由：恢复 because、actually、okay、right 以及原来插入语次序。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 6–8, relative 39.38–64.94s + offset 885s = absolute 924.38–949.94s
2. 原：It's good to know how things work, but it is also important to understand the rationale. Why do things happen?
   候选：So it’s good to know how things work. But it’s also important to understand the rationale, okay? Why things happen?
   理由：恢复 So/But 和 okay；撤销给原问句补 do 的语法润色。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 8–9, relative 56.78–74.82s + offset 885s = absolute 941.78–959.82s
3. 原：That's the really important thing this class should give you: strengthening your ability to understand why certain things have been decided in a certain manner when designing a system.
   候选：That’s the really important fact that this class should give you, okay? To strengthen your ability to understand why certain things have been decided in certain manner in designing a system.
   理由：恢复 fact、that、To strengthen、in certain manner 和 in designing，不补冠词、不改成分词。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 10–12, relative 74.82–109.66s + offset 885s = absolute 959.82–994.66s
4. 原：There is always a reason, and we need to learn how to reason about things and understand the solutions that have been created.
   候选：Okay, because there is always a reason, and what we need to do is to learn how to reason about things, and understand the solutions that have been created.
   理由：恢复 Okay/because 和 what we need to do is to；Feishu在尾部截断，后续由两个Qwen重叠窗与Whisper共同补足。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 12–14, relative 101.82–126.78s + offset 885s = absolute 986.82–1011.78s

### 逐单元证据

1. Okay, because the main thing here, when we study Wi-Fi, okay, is to, of course, learn how we use a technology that is actually used every day, right, by almost everyone.
好，因为这里主要的事情，当我们学习 Wi-Fi 时，好，当然是去了解我们怎样使用一种实际上每天都在被使用的技术，对吧，几乎每个人都在使用。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 6–8, relative 39.38–64.94s + offset 885s = absolute 924.38–949.94s
2. So it’s good to know how things work.
所以，知道事情怎样运作是好的。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 8–8, relative 56.78–64.94s + offset 885s = absolute 941.78–949.94s
3. But it’s also important to understand the rationale, okay?
但理解其中的道理也很重要，好吗？
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 8–9, relative 56.78–74.82s + offset 885s = absolute 941.78–959.82s
4. Why things happen?
为什么事情会发生？
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 9–9, relative 64.94–74.82s + offset 885s = absolute 949.94–959.82s
5. Why do we make certain choices while developing a technology?
为什么我们在开发一项技术时会作出某些选择？
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 9–10, relative 64.94–88.44s + offset 885s = absolute 949.94–973.44s
6. That’s the really important fact that this class should give you, okay?
那是这门课应该给你们的真正重要的事实，好吗？
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 10–10, relative 74.82–88.44s + offset 885s = absolute 959.82–973.44s
7. To strengthen your ability to understand why certain things have been decided in certain manner in designing a system.
去增强你们的能力，理解为什么在设计一个系统时，某些事情被以某种方式决定下来。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Unprompted Whisper medium.en raw: chunk-006, segments 10–12, relative 74.82–109.66s + offset 885s = absolute 959.82–994.66s
8. Okay, because there is always a reason, and what we need to do is to learn how to reason about things, and understand the solutions that have been created.
好，因为总是有一个原因，而我们需要做的是学会怎样思考事情，并理解已经被创造出来的解决方案。
   来源：Feishu historical snapshot: source_index=16, id=35, section anchor 00:15:26；Qwen recovery rerun raw: chunk_index=8, absolute 880.00–1000.00s；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 12–14, relative 101.82–126.78s + offset 885s = absolute 986.82–1011.78s
   限制：Feishu stops at “to look”; Qwen overlapping chunks 8/9 and Whisper supply the continuation. The overlap is retained once, not twice.

## 14 · 00:16:47 · 引入接入点和A、B、C拓扑

稳定块ID：doxcnusJMQ3VdFmXjsWY3Iw9EOh
原块SHA256：f3580b7ccfccb74a0d0be0bbf140e7d708b60077ad5d19b37f63f934a10af5b5
候选SHA256：58db457a3c5c91d2b9ffc146b8c84db511370b9390a71359d285844af2b0e15d

### 具体修改

1. 原：That's the important attitude we need to develop.
   候选：Okay, [that ... unclear] that’s the important attitude that we need to develop.
   理由：恢复 Okay 和 that；Qwen独有的 that 起头重复保留为待听辨，不直接删掉或认定。
   来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–14, relative 120.56–126.78s + offset 885s = absolute 1005.56–1011.78s
2. 原：Understanding why is a kind of mental exercise that we need to do.
   候选：So, this is understanding [why / Wi-Fi unclear], is a kind of mental exercise, okay, that we need to [to ... unclear] do.
   理由：恢复 So, this is 和第二个 is 的口语句法、okay；why/Wi-Fi不依据语意擅选；可能重复to另标待辨。
   来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–15, relative 120.56–135.06s + offset 885s = absolute 1005.56–1020.06s
3. 原：Good. Let's consider a simple topology where we have an access point and then A, B, and C.
   候选：Okay, good. So, let’s consider a simple topology where we have an access point, and then we have A, B, and C.
   理由：恢复 Okay、So 和第二个 we have，不删除平行从句中的重复。
   来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 16–17, relative 136.18–165.16s + offset 885s = absolute 1021.18–1050.16s

### 逐单元证据

1. Okay, [that ... unclear] that’s the important attitude that we need to develop.
好，[那……待听辨]那是我们需要培养的重要态度。
   来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–14, relative 120.56–126.78s + offset 885s = absolute 1005.56–1011.78s
   限制：Qwen has “that that’s”; Feishu/Whisper have “that’s”. The possible false start is not silently deleted.
2. So, this is understanding [why / Wi-Fi unclear], is a kind of mental exercise, okay, that we need to [to ... unclear] do.
所以，这是理解[为什么／Wi-Fi，待听辨]，是一种思维练习，好，我们需要去[去……待听辨]做的。
   来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 14–15, relative 120.56–135.06s + offset 885s = absolute 1005.56–1020.06s
   限制：Feishu: understanding why; Qwen: understanding why fire; Whisper: understanding Wi-Fi. Qwen alone also repeats “to”. mental is supported by Feishu and Whisper; Qwen’s experimental is not adopted.
3. Okay, good.
好，很好。
   来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 16–16, relative 136.18–149.64s + offset 885s = absolute 1021.18–1034.64s
4. So, let’s consider a simple topology where we have an access point, and then we have A, B, and C.
所以，我们来考虑一个简单的拓扑，其中我们有一个接入点，然后我们有 A、B 和 C。
   来源：Feishu historical snapshot: source_index=17, id=37, section anchor 00:16:47；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 16–17, relative 136.18–165.16s + offset 885s = absolute 1021.18–1050.16s

## 15 · 00:17:18 · 所有节点彼此可听的BSS场景

稳定块ID：doxcnDM0vMtHUpnWdnzpcERTuof
原块SHA256：d4f9e44ff7937c69b05c5abd6e5ff7e64871e1e2ef3a4f14016b5c81c19232d3
候选SHA256：b0a7db4e838ae3f94972763a6a7ccac954079ed8566af60d055c2b9e4ab6ad07

### 具体修改

1. 原：The access point is here. These are our user nodes, and they are part of this BSS, which means they can talk with the access point.
   候选：Okay, the access point is here. These are our user nodes, and [we / they unclear] are of course part of this BSS; that means they can talk with the access point.
   理由：恢复 Okay、of course、that means；we/they确有来源冲突，不能因为指代逻辑通顺便改成they。
   来源：Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 17–18, relative 149.64–175.10s + offset 885s = absolute 1034.64–1060.10s
2. 原：Let's consider the simple case where all nodes can hear each other. Now let's represent their behavior over time.
   候选：And also, let’s consider the simple case where all nodes can hear each other. Okay, now let’s represent the behavior of these nodes over time.
   理由：恢复 And also、Okay 和 the behavior of these nodes；Feishu尾部缺失由Qwen及Whisper两窗补足，同一边界句不重复粘贴。
   来源：Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 18–19, relative 165.16–193.16s + offset 885s = absolute 1050.16–1078.16s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s

### 逐单元证据

1. Okay, the access point is here.
好，接入点在这里。
   来源：Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 17–17, relative 149.64–165.16s + offset 885s = absolute 1034.64–1050.16s
2. These are our user nodes, and [we / they unclear] are of course part of this BSS; that means they can talk with the access point.
这些是我们的用户节点，并且[我们／它们，待听辨]当然是这个 BSS 的一部分；那意味着它们可以和接入点通信。
   来源：Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 17–18, relative 149.64–175.10s + offset 885s = absolute 1034.64–1060.10s
   限制：Feishu and Whisper say we; Qwen says they. Do not repair the pronoun solely on technical semantics.
3. And also, let’s consider the simple case where all nodes can hear each other.
还有，我们来考虑所有节点都能听到彼此的这个简单情况。
   来源：Feishu historical snapshot: source_index=18, id=39, section anchor 00:17:18；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 18–19, relative 165.16–193.16s + offset 885s = absolute 1050.16–1078.16s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s
   限制：Feishu stops after all nodes; Qwen and the Whisper overlap provide can hear each other.
4. Okay, now let’s represent the behavior of these nodes over time.
好，现在我们来表示这些节点随时间的行为。
   来源：Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 19–19, relative 175.10–193.16s + offset 885s = absolute 1060.10–1078.16s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s

## 16 · 00:17:58 · A收到数据包并侦听DIFS

稳定块ID：doxcnGEPwbf7ydvGtRF2lbJtene
原块SHA256：a58950f964e05ce19361b2192af289c552afcb78061a3f79599d821ca4425cb1
候选SHA256：ae806571b11b08c267963e884459d4516059875f6887c0d67edb82bf90521682

### 具体修改

1. 原：This is the timeline. We will draw a timeline for each node: the access point, user A, user B, and user C.
   候选：So, this is the timeline. We will represent it by drawing a timeline for each node: access point, user A, user B, and user C.
   理由：恢复 So 和 represent it by drawing；各节点列表以完整的chunk-007为准补全，不用chunk-006窗口截断遗漏C。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 20–21, relative 193.60–209.74s + offset 885s = absolute 1078.60–1094.74s；Unprompted Whisper medium.en raw: chunk-007, segments 1–2, relative 0.00–33.30s + offset 1065s = absolute 1065.00–1098.30s
2. 原：Assume that when we start looking at the system, we observe that A has received a packet from its higher layers. Its application layer has generated some data.
   候选：Okay, now let’s assume that when we start looking at the system, what we observe is that A has received a packet from its higher layers. Okay, its application layer has generated some data.
   理由：恢复 Okay、now let’s、what we observe is that 的完整口语结构。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 3–5, relative 33.30–66.44s + offset 1065s = absolute 1098.30–1131.44s
3. 原：A gets this packet at its MAC layer and understands that it has to try to transmit it.
   候选：So, A gets this packet at [its / this unclear] MAC layer, and A understands that it has to try and transmit this packet, right?
   理由：恢复 So、重复主语A、try and、重复this packet及right；its/this依来源留疑点。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 5–6, relative 55.68–76.68s + offset 1065s = absolute 1120.68–1141.68s
4. 原：We know that in this case a Wi-Fi node will first sense the channel for DIFS. Let's assume that the channel is idle.
   候选：So, we know that in this case, a Wi-Fi node will first sense the channel for DIFS, right? Let’s assume that the channel is idle.
   理由：恢复 So 与 right；Feishu截断后由Qwen/Whisper补齐，diffs仅作DIFS技术近音校正。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 6–7, relative 66.44–86.10s + offset 1065s = absolute 1131.44–1151.10s

### 逐单元证据

1. So, this is the timeline.
所以，这是时间轴。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 20–20, relative 193.60–204.86s + offset 885s = absolute 1078.60–1089.86s；Unprompted Whisper medium.en raw: chunk-007, segments 1–1, relative 0.00–14.68s + offset 1065s = absolute 1065.00–1079.68s
2. We will represent it by drawing a timeline for each node: access point, user A, user B, and user C.
我们会通过给每个节点画一条时间轴来表示它：接入点、用户 A、用户 B 和用户 C。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Unprompted Whisper medium.en raw: chunk-006, segments 20–21, relative 193.60–209.74s + offset 885s = absolute 1078.60–1094.74s；Unprompted Whisper medium.en raw: chunk-007, segments 2–2, relative 14.68–33.30s + offset 1065s = absolute 1079.68–1098.30s
3. Okay, now let’s assume that when we start looking at the system, what we observe is that A has received a packet from its higher layers.
好，现在我们来假设，当我们开始看这个系统时，我们观察到的是 A 从它的高层收到了一个数据包。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=9, absolute 990.00–1110.00s；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 3–4, relative 33.30–55.68s + offset 1065s = absolute 1098.30–1120.68s
4. Okay, its application layer has generated some data.
好，它的应用层生成了一些数据。
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 4–5, relative 46.72–66.44s + offset 1065s = absolute 1111.72–1131.44s
5. So, A gets this packet at [its / this unclear] MAC layer, and A understands that it has to try and transmit this packet, right?
所以，A 在[它的／这个，待听辨] MAC 层收到这个数据包，而 A 明白它必须尝试去发送这个数据包，对吧？
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 5–6, relative 55.68–76.68s + offset 1065s = absolute 1120.68–1141.68s
   限制：Qwen: at its MAC layer; Whisper: at this MAC layer; Feishu: and this mark layer. MAC is a clear technical near-sound correction; the determiner remains unresolved.
6. So, we know that in this case, a Wi-Fi node will first sense the channel for DIFS, right?
所以，我们知道，在这种情况下，一个 Wi-Fi 节点会首先侦听信道一个 DIFS 的时间，对吧？
   来源：Feishu historical snapshot: source_index=19, id=41, section anchor 00:17:58；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 6–7, relative 66.44–86.10s + offset 1065s = absolute 1131.44–1151.10s
   限制：Feishu truncates after a corrupted “I will find out will first”; the full predicate is supported by Qwen and Whisper.
7. Let’s assume that the channel is idle.
我们来假设信道是空闲的。
   来源：Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 7–7, relative 76.68–86.10s + offset 1065s = absolute 1141.68–1151.10s

## 17 · 00:19:08 · A发送数据并获得SIFS后的ACK

稳定块ID：doxcnlR1VavXUPuMoZJxMqbHYie
原块SHA256：b5c9bca604a195405788560a93d584f8308c4debdb7a63cf6471e3e8c508f66f
候选SHA256：b10ed594a7c27cc2829135c46bff218e9b7fdf93f5342600893dcf22a627447d

### 具体修改

1. 原：In this case, A can access the channel and transmit its data packet. It is a unicast packet intended for the access point.
   候选：So, we know that in this case, A can access the channel and transmit its data packet. That is a unicast data packet, so it is intended for the access point.
   理由：恢复 So, we know that、That is、data 和独立的so从句，不压缩成后置修饰。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 7–9, relative 76.68–100.66s + offset 1065s = absolute 1141.68–1165.66s
2. 原：Let's be optimistic and consider that it is successfully received by the access point.
   候选：And let’s be optimistic, and let’s consider that this data packet is successfully received by the access point.
   理由：恢复两个and、第二个let’s和this data packet，保留讲者重复。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 9–11, relative 91.88–115.74s + offset 1065s = absolute 1156.88–1180.74s
3. 原：Therefore, the access point will send an acknowledgment after SIFS.
   候选：Therefore, we know that the access point will send an acknowledgment after SIFS.
   理由：恢复we know that；Feishu的six按Qwen/Whisper共同支持校为SIFS。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 11–12, relative 109.14–124.28s + offset 1065s = absolute 1174.14–1189.28s

### 逐单元证据

1. So, we know that in this case, A can access the channel and transmit its data packet.
所以，我们知道，在这种情况下，A 可以接入信道并发送它的数据包。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 7–8, relative 76.68–91.88s + offset 1065s = absolute 1141.68–1156.88s
2. That is a unicast data packet, so it is intended for the access point.
那是一个单播数据包，所以它是发给接入点的。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 8–9, relative 86.10–100.66s + offset 1065s = absolute 1151.10–1165.66s
3. And let’s be optimistic, and let’s consider that this data packet is successfully received by the access point.
而且我们来乐观一点，而且我们来认为这个数据包被接入点成功接收了。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 9–11, relative 91.88–115.74s + offset 1065s = absolute 1156.88–1180.74s
4. Therefore, we know that the access point will send an acknowledgment after SIFS.
因此，我们知道，接入点会在 SIFS 之后发送一个确认。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 11–12, relative 109.14–124.28s + offset 1065s = absolute 1174.14–1189.28s
5. This is the usual story that we have told many times.
这是我们已经讲过很多次的通常的故事。
   来源：Feishu historical snapshot: source_index=20, id=43, section anchor 00:19:08；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 12–12, relative 115.74–124.28s + offset 1065s = absolute 1180.74–1189.28s

## 18 · 00:19:49 · B和C读取首部设置NAV

稳定块ID：doxcnm1bGEyxYyL64fY1q3gB9Kg
原块SHA256：8f18bac75f40e1f43892bc2972c3be68246bdaeb48f17473898f792133c9165f
候选SHA256：1e49b4f0b9096f8830fe4ca8357bf4fc41ba1dd367e111bc1e8b10c8888896b1

### 具体修改

1. 原：We also know that under these conditions the other nodes, B and C, demodulate the data packet's header.
   候选：Okay, we also know that under these conditions, the other nodes B and C demodulate the header, right, of the data packet.
   理由：恢复Okay、插入的right和the header ... of the data packet的原顺序；they modulate按Whisper及技术词边界校为demodulate。
   来源：Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 13–13, relative 124.28–139.86s + offset 1065s = absolute 1189.28–1204.86s
2. 原：They read the Duration field so they can set their NAV counter, extending over the expected duration of the dialogue.
   候选：They read the Duration field, so that they can set their NAV counter, and this will extend over the all expected duration of the dialogue.
   理由：恢复so that、and this will和三方一致的the all expected，撤销分词压缩及语法修正；NAV由Qwen下一窗明确支持。
   来源：Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 14–15, relative 139.86–159.18s + offset 1065s = absolute 1204.86–1224.18s

### 逐单元证据

1. Okay, we also know that under these conditions, the other nodes B and C demodulate the header, right, of the data packet.
好，我们还知道，在这些条件下，其他节点 B 和 C 解调首部，对吧，这个数据包的首部。
   来源：Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Unprompted Whisper medium.en raw: chunk-007, segments 13–13, relative 124.28–139.86s + offset 1065s = absolute 1189.28–1204.86s
   限制：Feishu/Qwen split the sound as “they modulate”; Whisper gives demodulate. This is treated as a clear technical word-boundary error rather than adding a second subject.
2. They read the Duration field, so that they can set their NAV counter, and this will extend over the all expected duration of the dialogue.
它们读取 Duration 字段，这样它们就能设置它们的 NAV 计数器，而这将延伸覆盖这次对话的全部预期持续时间。
   来源：Feishu historical snapshot: source_index=21, id=45, section anchor 00:19:49；Qwen recovery rerun raw: chunk_index=10, absolute 1100.00–1220.00s；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 14–15, relative 139.86–159.18s + offset 1065s = absolute 1204.86–1224.18s
   限制：The ungrammatical “the all expected duration” is common to all three sources and intentionally retained. Singular field follows Feishu/Qwen; Whisper has fields.

## 19 · 00:20:25 · B和C在信道忙时收到新数据包

稳定块ID：doxcntMYbHlAQ6Z78lxolPfpwkd
原块SHA256：f4332be8c31b0fc429e7ee3e1c35f9ec9a15b2c90497fa700a72bf15b4a82ced
候选SHA256：6bc80434565d55ca5d7f8725e2525630f5c8a5f1145a38b23dffa1bd56188cca

### 具体修改

1. 原：So far so good; this is exactly what we did in the past. Now let's add some events.
   候选：Okay, so, so far so good; this is exactly what we did in the past. Now, let’s add some events here.
   理由：恢复Okay、前置so与so far的重复以及here；以Feishu/Qwen共同支持保留，不能只跟Whisper省略。
   来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 16–16, relative 160.96–170.66s + offset 1065s = absolute 1225.96–1235.66s
2. 原：Let's say that B and C, while their NAV is set to a positive value, also receive a data packet from their respective upper layers.
   候选：Let’s say B and also C, while they have their NAV set to a positive value, will also receive a data packet from their respective upper layers.
   理由：恢复and also、they have their NAV set和will；不把未来式改成现在式。
   来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 17–18, relative 170.66–196.76s + offset 1065s = absolute 1235.66–1261.76s；Unprompted Whisper medium.en raw: chunk-008, segments 1–2, relative 0.00–22.30s + offset 1245s = absolute 1245.00–1267.30s
3. 原：For example, at this point B gets a packet queued at its MAC layer, and at this other point C also gets a packet from its higher layers.
   候选：So, this means that, for example, at this point in time, B gets a packet that is queued at its MAC layer, and let’s assume that C at this point in time also gets a packet from its higher layers.
   理由：恢复So, this means that、that is、let’s assume以及两次at this point in time；删除旧校订无来源的other，不替讲者标明另一个时刻。
   来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 18–20, relative 185.70–209.98s + offset 1065s = absolute 1250.70–1274.98s；Unprompted Whisper medium.en raw: chunk-008, segments 2–4, relative 13.00–41.72s + offset 1245s = absolute 1258.00–1286.72s

### 逐单元证据

1. Okay, so, so far so good; this is exactly what we did in the past.
好，所以，到目前为止一切顺利；这正是我们过去做过的。
   来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 16–16, relative 160.96–170.66s + offset 1065s = absolute 1225.96–1235.66s
2. Now, let’s add some events here.
现在，我们在这里加一些事件。
   来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 16–16, relative 160.96–170.66s + offset 1065s = absolute 1225.96–1235.66s
3. Let’s say B and also C, while they have their NAV set to a positive value, will also receive a data packet from their respective upper layers.
假设 B，还有 C，在它们把各自的 NAV 设为一个正值的时候，也会从它们各自的高层收到一个数据包。
   来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 17–18, relative 170.66–196.76s + offset 1065s = absolute 1235.66–1261.76s；Unprompted Whisper medium.en raw: chunk-008, segments 1–2, relative 0.00–22.30s + offset 1245s = absolute 1245.00–1267.30s
4. So, this means that, for example, at this point in time, B gets a packet that is queued at its MAC layer, and let’s assume that C at this point in time also gets a packet from its higher layers.
所以，这意味着，例如，在这个时间点，B 收到一个在它的 MAC 层排队的数据包，而我们假设 C 在这个时间点也从它的高层收到一个数据包。
   来源：Feishu historical snapshot: source_index=22, id=47, section anchor 00:20:25；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-007, segments 18–20, relative 185.70–209.98s + offset 1065s = absolute 1250.70–1274.98s；Unprompted Whisper medium.en raw: chunk-008, segments 2–4, relative 13.00–41.72s + offset 1245s = absolute 1258.00–1286.72s

## 20 · 00:21:21 · 依据本地忙状态独立执行退避

稳定块ID：doxcnfJ6YnYDMIM2F7E4sDqTb6M
原块SHA256：09b82fe10df6af07a99fb4aac4136ab0147942a9c4b735d048104ae362382a6e
候选SHA256：44fe300b15e39c0d3adeb2b6d0a4d845899c2892b0480ebb66f6c18e88a10dd0

### 具体修改

1. 原：While the dialogue between A and the access point is going on, B and C now also have a packet to transmit.
   候选：Okay, so now while we have this dialogue between A and the access point going on, we have B and C who have a packet to transmit as well.
   理由：恢复Okay, so now、两次we have和who have从句，不能把原来句法改写得更简洁。
   来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 4–6, relative 30.50–61.80s + offset 1245s = absolute 1275.50–1306.80s
2. 原：Clearly their NAV is set, so they know the channel is busy and cannot access it.
   候选：Now, clearly, they have got their NAV set, so they know the channel is busy, so they cannot access the channel, right?
   理由：恢复Now、have got、重复so和the channel及right；NAV是Qwen明确词，不采用Whisper knobs。
   来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 6–7, relative 50.96–68.94s + offset 1245s = absolute 1295.96–1313.94s
3. 原：That is the principle of carrier sensing. We are essentially in this situation, situation number one: B and C get a new packet but sense that the channel is busy.
   候选：That’s the principle of carrier sensing. We are essentially in this situation, situation number one, right? B and C [get / got unclear] a new packet, but they sense the channel as busy.
   理由：恢复right、they和as busy；Qwen重叠窗get/got冲突保留时态待听辨，不能让旧校订决定。
   来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 7–9, relative 62.56–90.92s + offset 1245s = absolute 1307.56–1335.92s
4. 原：What do we have to do? Apply backoff. Remember that our scheme is distributed, so each node makes decisions for itself based on the state of the system that it observes.
   候选：So, what do we have to do? Apply backoff, right? So, this means that both B and C, remember our scheme is distributed, so everyone makes decisions by itself based on the state of the system that it observes.
   理由：恢复两次So、right以及被删的both B and C残留从句；恢复everyone/by itself，不以each node/for itself润色。
   来源：Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 9–11, relative 79.76–113.80s + offset 1245s = absolute 1324.76–1358.80s
5. 原：B will say: I got a packet, but the channel is busy.
   候选：So, B will say, “[Hmm ... unclear] I got [a / the unclear] packet, but the channel is busy.”
   理由：恢复So；Hmm有无和a/the在两种ASR之间冲突，列为待听辨，不凭旧校订取舍。
   来源：Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 11–12, relative 102.48–123.02s + offset 1245s = absolute 1347.48–1368.02s

### 逐单元证据

1. Okay, so now while we have this dialogue between A and the access point going on, we have B and C who have a packet to transmit as well.
好，所以现在，当我们有 A 和接入点之间的这段对话正在进行时，我们有 B 和 C，它们也有一个数据包要发送。
   来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 4–6, relative 30.50–61.80s + offset 1245s = absolute 1275.50–1306.80s
2. Now, clearly, they have got their NAV set, so they know the channel is busy, so they cannot access the channel, right?
现在，显然，它们已经把 NAV 设置好了，所以它们知道信道忙，所以它们不能接入信道，对吧？
   来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 6–7, relative 50.96–68.94s + offset 1245s = absolute 1295.96–1313.94s
3. That’s the principle of carrier sensing.
那就是载波侦听的原则。
   来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Unprompted Whisper medium.en raw: chunk-008, segments 7–7, relative 62.56–68.94s + offset 1245s = absolute 1307.56–1313.94s
4. We are essentially in this situation, situation number one, right?
我们基本上处在这种情况，第一种情况，对吧？
   来源：Feishu historical snapshot: source_index=23, id=49, section anchor 00:21:21；Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 8–8, relative 70.72–79.76s + offset 1245s = absolute 1315.72–1324.76s
5. B and C [get / got unclear] a new packet, but they sense the channel as busy.
B 和 C [收到／收到了，待听辨]一个新数据包，但是它们侦听到信道忙。
   来源：Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=11, absolute 1210.00–1330.00s；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 8–9, relative 70.72–90.92s + offset 1245s = absolute 1315.72–1335.92s
   限制：Qwen’s two overlapping windows disagree get/got; Feishu/Whisper read get. Both tenses are left for listening because the current task specifically forbids silent tense changes.
6. So, what do we have to do?
所以，我们必须做什么？
   来源：Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 9–9, relative 79.76–90.92s + offset 1245s = absolute 1324.76–1335.92s
7. Apply backoff, right?
执行退避，对吧？
   来源：Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 9–9, relative 79.76–90.92s + offset 1245s = absolute 1324.76–1335.92s
8. So, this means that both B and C, remember our scheme is distributed, so everyone makes decisions by itself based on the state of the system that it observes.
所以，这意味着 B 和 C 两者，记住我们的方案是分布式的，所以每一个都根据它观察到的系统状态自己作出决定。
   来源：Feishu historical snapshot: source_index=24, id=51, section anchor 00:21:21；Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 10–11, relative 91.92–113.80s + offset 1245s = absolute 1336.92–1358.80s
   限制：Retains the interrupted “both B and C” clause and everyone/by itself wording; it is not completed or repaired to “each node”.
9. So, B will say, “[Hmm ... unclear] I got [a / the unclear] packet, but the channel is busy.”
所以，B 会说：“[嗯……待听辨]我收到了[一个／这个，待听辨]数据包，但信道忙。”
   来源：Qwen recovery rerun raw: chunk_index=12, absolute 1320.00–1440.00s；Unprompted Whisper medium.en raw: chunk-008, segments 11–12, relative 102.48–123.02s + offset 1245s = absolute 1347.48–1368.02s
   限制：This continuation is absent from the supplied Feishu fragments. Qwen has “Hmm, I got a packet”; Whisper has “I got the packet”. The later what-I-need sentence belongs to section 21.

## 21 · 00:22:43 · 等待空闲DIFS后随机抽取退避值

稳定块ID：doxcniIJAOk2vByuoHqJLWxuw8g
原块SHA256：ab349323bf8510e556d7f1fc756d4381c67bfb8fa2c4f4e4211cb998b833cfd4
候选SHA256：764772125de7dbed07e5dd914f87487c81c5ecd0ec75020b2ce63ec9796793c4

### 具体修改

1. 原：What I need to do is apply backoff. It waits for the channel to become idle again, senses it as idle for DIFS, and if the channel stays idle for DIFS, it can draw an integer out of the range zero to CW_min. The same applies to C. C says: I got a packet to transmit, but the channel is busy. It knows it has to perform backoff. It waits for the channel to become idle and verifies that it remains idle for DIFS. The channel will be idle because nobody else is doing anything.
   候选：What I need to do is to apply backoff. So what [it will / you will, unclear] do is wait for the channel to become idle again, sense the channel idle for DIFS, and then, if the channel is idle for DIFS, it will be able to draw an integer, right? Out of what? Out of the range zero, CW_min. And the same C, right? C at this point in time says, oh, I got a packet to transmit, but the channel is busy. So again, it knows that it has to perform a backoff. So what it will do? It will wait for the channel to become idle. Then it needs to verify that the channel is idle for DIFS. The channel will be idle because nobody else is doing anything, so the channel is idle.
   理由：Restore the repeated questions Out of what? and So what it will do?, repeated channel-is-idle statement, future forms, right/oh/again, and underived pronoun uncertainty. Qwen 1320–1440 and medium chunk-008 preserve wording compressed in the current paragraph.
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-008,chunk-009

### 逐单元证据

1. What I need to do is to apply backoff.
我需要做的就是执行退避。
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 12, absolute 1358.80–1368.02s; source text retained in review packet
2. So what [it will / you will, unclear] do is wait for the channel to become idle again, sense the channel idle for DIFS, and then, if the channel is idle for DIFS, it will be able to draw an integer, right?
所以，[它将要／你将要，待听辨]做的就是等信道再次变为空闲，侦听信道空闲一个 DIFS 的时间，然后，如果信道空闲了一个 DIFS 的时间，它就能够抽取一个整数，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 13,14, absolute 1368.02–1391.80s; source text retained in review packet
   限制：Qwen says it will; historical Feishu says you will; Whisper says you do. Pronoun and auxiliary remain unresolved.
3. Out of what?
从什么里面抽取？
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 15, absolute 1391.80–1410.30s; source text retained in review packet
4. Out of the range zero, CW_min.
从零、CW_min 这个范围里面。
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 15, absolute 1391.80–1410.30s; source text retained in review packet
5. And the same C, right?
C 也一样，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 15, absolute 1391.80–1410.30s; source text retained in review packet
6. C at this point in time says, oh, I got a packet to transmit, but the channel is busy.
C 在这个时间点说，哦，我拿到了一个要发送的数据包，但是信道是忙的。
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 16, absolute 1410.30–1417.50s; source text retained in review packet
7. So again, it knows that it has to perform a backoff.
所以，再说一次，它知道它必须执行一次退避。
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 17, absolute 1417.50–1426.12s; source text retained in review packet
8. So what it will do?
所以，它会做什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 17, absolute 1417.50–1426.12s; source text retained in review packet
9. It will wait for the channel to become idle.
它会等信道变为空闲。
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 13, absolute 1368.02–1378.96s; source text retained in review packet
10. Then it needs to verify that the channel is idle for DIFS.
然后，它需要确认信道空闲了一个 DIFS 的时间。
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-008, segment(s) 18, absolute 1426.12–1434.56s; source text retained in review packet
11. The channel will be idle because nobody else is doing anything, so the channel is idle.
信道会是空闲的，因为其他谁也没有在做什么，所以信道是空闲的。
   来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 2, absolute 1432.82–1439.82s; source text retained in review packet

## 22 · 00:24:00 · B抽到2而C抽到5的例子

稳定块ID：doxcnMBEVaguqYaqIJaRU0gJaqe
原块SHA256：eed3291e744fc517a6d84ed613814d34e4f8c775a6ed7fdf35dee668436189c4
候选SHA256：1f9253b6fc6ef84dbada2ac75a336d246ca376f6ea843c29e6102ed2b06b45ec

### 具体修改

1. 原：It too draws an integer with equal probability from the same range of values. Let's assume that B draws the integer two and C draws five. This is just an example.
   候选：[And it too will draw / And it will do, will draw, unclear] an integer with equal probability out of this same range of values, okay? So let's assume that the value drawn by B, the integer, is equal to two. And let's assume that the integer drawn by C is equal to five. This is just an example.
   理由：Restore both lets-assume clauses, the apposition the value drawn by B, the integer, and okay. Mark the unstable it too / it will do restart instead of smoothing it to It too draws.
   来源：Feishu historical snapshot mapped source_index_zero_based=26; source block(s) 57; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-008,chunk-009

### 逐单元证据

1. [And it too will draw / And it will do, will draw, unclear] an integer with equal probability out of this same range of values, okay?
[它也会抽取／它会做，会抽取，待听辨]一个整数，从这同一个取值范围中等概率地抽取，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=26; source block(s) 57; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 3, absolute 1440.36–1451.38s; source text retained in review packet
   限制：Feishu has And if we two will draw; Qwen has And you will do will draw; Whisper has and it will do, will draw. The short restart or too is not resolved.
2. So let's assume that the value drawn by B, the integer, is equal to two.
所以，我们假设 B 抽到的值，这个整数，等于二。
   来源：Feishu historical snapshot mapped source_index_zero_based=26; source block(s) 57; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 4, absolute 1451.38–1466.60s; source text retained in review packet
3. And let's assume that the integer drawn by C is equal to five.
再假设 C 抽到的整数等于五。
   来源：Feishu historical snapshot mapped source_index_zero_based=26; source block(s) 57; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 4, absolute 1451.38–1466.60s; source text retained in review packet
4. This is just an example.
这只是一个例子。
   来源：Feishu historical snapshot mapped source_index_zero_based=26; source block(s) 57; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 5, absolute 1466.60–1478.68s; source text retained in review packet

## 23 · 00:24:36 · 两个节点并行倒计时至B先归零

稳定块ID：doxcn77kJlEslDJgMxoerJeZhOd
原块SHA256：b310fd13d2233e2dd9f25c135d7c94fcada732e65f4d878da671488dc4160b6f
候选SHA256：c499b7d5ed715c93ef94486b2ba553831acac26c879f3f7899d254c958f8f901

### 具体修改

1. 原：In that case, B computes a backoff time equal to twice the time-slot duration. Similarly, C computes a backoff time of five time slots. Each of them decreases its own backoff counter slot by slot. B senses the channel for one time slot. The channel is currently idle, so it decreases its counter by one. C does the same, decreasing its own counter by one. In the next time slot, B again senses the channel as idle and decreases its counter by one. C does the same, but now B's backoff counter has reached zero.
   候选：Okay, so if this is the case, then we know that B will compute its backoff time, that will be equal to two times the time-slot duration, right? And similarly C will compute its backoff time, that will be five time slots. And then each of them will have to decrease its own backoff counter, time slot by time slot. So B will start sensing the channel for a time slot. The channel is currently idle, so it will decrease its backoff counter by one. And the same will do C, right? So it will decrease it by, its own counter by one. Then, next time slot, again B senses the channel [is / as, unclear] idle, decreases its backoff counter by one. And C will do the same. But now the backoff counter of B has reached zero.
   理由：Restore will compute, will start sensing, and successive conjunctions; keep the it by, its own counter restart. The C-will-do-the-same / B-reaches-zero ending is supported by Qwen 1540–1660 and medium although missing from Feishu.
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-009

### 逐单元证据

1. Okay, so if this is the case, then we know that B will compute its backoff time, that will be equal to two times the time-slot duration, right?
好，所以，如果是这种情况，那么我们知道 B 会计算它的退避时间，这个时间会等于时隙时长的两倍，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 6, absolute 1478.68–1494.34s; source text retained in review packet
2. And similarly C will compute its backoff time, that will be five time slots.
同样，C 会计算它的退避时间，这个时间会是五个时隙。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 7, absolute 1495.50–1506.00s; source text retained in review packet
3. And then each of them will have to decrease its own backoff counter, time slot by time slot.
然后，它们各自都必须逐个时隙地递减自己的退避计数器。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 8, absolute 1506.00–1517.76s; source text retained in review packet
4. So B will start sensing the channel for a time slot.
所以，B 会开始侦听信道一个时隙的时间。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 9, absolute 1518.94–1530.56s; source text retained in review packet
5. The channel is currently idle, so it will decrease its backoff counter by one.
信道目前是空闲的，所以它会把退避计数器减一。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 9, absolute 1518.94–1530.56s; source text retained in review packet
6. And the same will do C, right?
C 也会这样做，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 10, absolute 1530.56–1544.34s; source text retained in review packet
7. So it will decrease it by, its own counter by one.
所以，它会把它减去，把自己的计数器减一。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 10, absolute 1530.56–1544.34s; source text retained in review packet；Documented disfluency, boundary or notation note: The awkward restart it by, its own counter by one is retained across Feishu, Qwen and Whisper; no grammatical repair is made.
8. Then, next time slot, again B senses the channel [is / as, unclear] idle, decreases its backoff counter by one.
然后，下一个时隙，B 再次侦听信道[是／为，待听辨]空闲，把退避计数器减一。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 11, absolute 1544.88–1555.46s; source text retained in review packet
   限制：Historical Feishu and Qwen say is idle; Whisper says as idle.
9. And C will do the same.
C 也会这样做。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 12, absolute 1555.46–1571.12s; source text retained in review packet
10. But now the backoff counter of B has reached zero.
但是现在，B 的退避计数器已经到零了。
   来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 12, absolute 1555.46–1571.12s; source text retained in review packet

## 24 · 00:26:12 · B获得发送机会并成功收到ACK

稳定块ID：doxcnbsGtRDxk5x9f56gzyigbwd
原块SHA256：df9363ca7a4201805e9c6e249a6ce558bbc34c72813d272cff45431b3d36462e
候选SHA256：05b1b99f973694028a8d5f02d5e7f58115e8e86286ff3d7ecf1968c0531f8eb5

### 具体修改

1. 原：B is entitled to access the channel, so it transmits its data packet. The packet is intended for the access point because we are considering unicast packets, and in this network architecture all Wi-Fi user nodes communicate only with the access point. Again, let's be optimistic: the packet is successfully received, and the access point sends an acknowledgment after SIFS.
   候选：So B is entitled to access the channel [and transmit, unclear]. So it will transmit its data packet. The data packet clearly is intended for the access point because, as we said, we are considering unicast packets. And in this network topology, network architecture, all Wi-Fi user nodes communicate with the access point only. Let's again be optimistic. So this means that this packet is received successfully by the access point, which will send back an acknowledgement after SIFS.
   理由：Restore clearly, as we said, the network topology, network architecture restart, and will send back. Mark the extra and transmit that appears only in new medium rather than deciding silently.
   来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-009,chunk-010

### 逐单元证据

1. So B is entitled to access the channel [and transmit, unclear].
所以，B 有资格接入信道[并发送，待听辨]。
   来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 13, absolute 1572.50–1581.74s; source text retained in review packet
   限制：Whisper adds and transmit; historical Feishu and Qwen end this sentence at channel. Do not silently choose the longer or shorter version.
2. So it will transmit its data packet.
所以，它会发送自己的数据包。
   来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 13, absolute 1572.50–1581.74s; source text retained in review packet
3. The data packet clearly is intended for the access point because, as we said, we are considering unicast packets.
这个数据包显然是发给接入点的，因为，正如我们说过的，我们考虑的是单播数据包。
   来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 14, absolute 1581.74–1588.48s; source text retained in review packet
4. And in this network topology, network architecture, all Wi-Fi user nodes communicate with the access point only.
而在这种网络拓扑，网络架构中，所有 Wi-Fi 用户节点都只与接入点通信。
   来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 15,16, absolute 1588.48–1603.08s; source text retained in review packet
5. Let's again be optimistic.
让我们再乐观一点。
   来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-009, segment(s) 16, absolute 1594.88–1603.08s; source text retained in review packet
6. So this means that this packet is received successfully by the access point, which will send back an acknowledgement after SIFS.
所以，这意味着接入点成功接收到了这个数据包，它会在 SIFS 之后发回一个确认。
   来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 1, absolute 1605.00–1615.22s; source text retained in review packet

## 25 · 00:27:02 · B发送期间A设NAV且C冻结退避

稳定块ID：doxcnjesWjxP2UoK4xKj5IVh7dh
原块SHA256：d857101127ea48fa37212bda3b638ebf8acef5f5e2aa0b77bb6cb087b9568e86
候选SHA256：c51f0cfa60f4e8b8f3837861da15a59d6ed6ed69622ff2d7bfdfae63c36d0a33

### 具体修改

1. 原：Upon B's data transmission, the other nodes can set their NAV. They can read the Duration field in the data packet's header. We also need to highlight that both A and C set their NAV. What does this mean for A? It's fine; it doesn't have anything to do. But for C, it means that it must freeze its backoff counter for this duration.
   候选：Upon the data transmission by B, the other nodes, right, can set their NAV. They can read the Duration field in the header of the data packet. So we need also to highlight this, that both A and also C will set their NAV, right? So what does it mean for A? This is okay, fine, it doesn't have anything to do, so that's [not okay / okay, unclear]. But for C, this means that [it / you, unclear] will have to freeze its backoff counter for this duration, right?
   理由：Restore Upon the data transmission by B, both A and also C, repeated So, will, right, and a source conflict around so thats not okay/okay. NAV is an explicit acronym spelling normalization, not a semantic paraphrase.
   来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-009,chunk-010

### 逐单元证据

1. Upon the data transmission by B, the other nodes, right, can set their NAV.
在 B 发送数据时，其他节点，对吧，可以设置自己的 NAV。
   来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 2, absolute 1615.22–1629.16s; source text retained in review packet
2. They can read the Duration field in the header of the data packet.
它们可以读取数据包首部中的 Duration 字段。
   来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 3, absolute 1629.60–1639.36s; source text retained in review packet
3. So we need also to highlight this, that both A and also C will set their NAV, right?
所以，我们还需要强调这一点，就是 A，还有 C，都会设置自己的 NAV，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 4, absolute 1640.20–1659.38s; source text retained in review packet
4. So what does it mean for A?
所以，这对 A 来说意味着什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 5, absolute 1660.28–1668.90s; source text retained in review packet
5. This is okay, fine, it doesn't have anything to do, so that's [not okay / okay, unclear].
这没问题，很好，它没有什么要做的，所以那是[不行的／没问题的，待听辨]。
   来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 5, absolute 1660.28–1668.90s; source text retained in review packet
   限制：Feishu and Whisper say not okay; Qwen says okay. The contradictory wording is not repaired for logic.
6. But for C, this means that [it / you, unclear] will have to freeze its backoff counter for this duration, right?
但是对 C 来说，这意味着[它／你，待听辨]必须在这段时间内冻结它的退避计数器，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 6, absolute 1668.90–1682.96s; source text retained in review packet
   限制：Qwen says it will; Whisper says you will. Feishu truncates before the predicate. The following right is near the 28:03 boundary.

## 26 · 00:28:03 · C在信道恢复后继续剩余倒计时

稳定块ID：doxcn6Oy9GIVWByK2HSBhV2xtLV
原块SHA256：734bb2325f02782a34d224f4fef74dd9554a7c09888d255776a17052af08991e
候选SHA256：f9e87180fb0d8c61fe4f1e478ac917a963054a5387c556b6d63d5b128d049e21

### 具体修改

1. 原：The channel is now busy, so C cannot decrease its counter; it has to suspend the countdown. During all this time C is essentially blocked and waits for the channel to become idle again. It makes sure the channel is idle for DIFS, then resumes decreasing its backoff counter. It still has three time slots to go. It senses the channel for a time slot: yes, it is idle, so it can decrease the counter by one. It senses the channel again for another time slot; it is idle, so it can decrease the counter by one. Then again, the channel is idle for one more time slot, so it decreases the counter by one.
   候选：Because now the channel is busy, so C cannot decrease its counter, it has to suspend the countdown. Okay, so during all this time C will be essentially blocked, and what it does is to wait for the channel to become idle again. [It / he, unclear] makes sure that the channel is idle for DIFS, and then [it / he, unclear] can resume decreasing its backoff [counter / count, unclear], [right, unclear]? It has still three time slots to go, so [it / he, unclear] will sense the channel for a [time slot, possibly incomplete]. Yes, this is idle, so it can decrease the backoff counter by one. Then it senses the channel again for a time slot. The channel is idle, it can decrease the counter by one, and then again, the channel is idle for one more time slot, it can decrease its counter by one.
   理由：Restore Because now, Okay so, will be essentially blocked, what it does, It has still, and the repeated per-slot description. Leave the possibly unfinished for a... and pronoun/counter-count choices unresolved.
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-010

### 逐单元证据

1. Because now the channel is busy, so C cannot decrease its counter, it has to suspend the countdown.
因为现在信道是忙的，所以 C 不能递减计数器，它必须暂停倒计时。
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 7, absolute 1682.96–1694.54s; source text retained in review packet
2. Okay, so during all this time C will be essentially blocked, and what it does is to wait for the channel to become idle again.
好，所以，在这整个时间里，C 基本上会被阻住，而它做的就是等待信道再次变为空闲。
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 8,9, absolute 1697.04–1711.48s; source text retained in review packet
3. [It / he, unclear] makes sure that the channel is idle for DIFS, and then [it / he, unclear] can resume decreasing its backoff [counter / count, unclear], [right, unclear]?
[它／他，待听辨]确认信道空闲了一个 DIFS 的时间，然后[它／他，待听辨]就可以恢复递减它的退避[计数器／计数，待听辨]，[对吧，待听辨]？
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 10, absolute 1711.48–1725.44s; source text retained in review packet
   限制：Feishu and Qwen use it; Whisper uses he. Feishu has right; both ASR runs omit that filler. Counter/count is left unresolved rather than silently substituted.
4. It has still three time slots to go, so [it / he, unclear] will sense the channel for a [time slot, possibly incomplete].
它还剩三个时隙，所以[它／他，待听辨]会侦听信道一个[时隙，此处可能没说完，待听辨]。
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 11, absolute 1725.44–1738.36s; source text retained in review packet
   限制：Qwen has it will sense the channel for a yes; Whisper has he will change the channel followed by yes. Do not silently supply a complete time-slot phrase.
5. Yes, this is idle, so it can decrease the backoff counter by one.
是的，这是空闲的，所以它可以把退避计数器减一。
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 12, absolute 1738.36–1768.16s; source text retained in review packet
6. Then it senses the channel again for a time slot.
然后，它再次侦听信道一个时隙的时间。
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 12, absolute 1738.36–1768.16s; source text retained in review packet
7. The channel is idle, it can decrease the counter by one, and then again, the channel is idle for one more time slot, it can decrease its counter by one.
信道是空闲的，它可以把计数器减一，然后再一次，信道又空闲了一个时隙，它可以把计数器减一。
   来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 12, absolute 1738.36–1768.16s; source text retained in review packet

## 27 · 00:29:23 · C归零发送成功与退避作用

稳定块ID：doxcnSnQ01WcspkpN5GGhyjECig
原块SHA256：dea5a7b326b64f9381feae119d9e860901856a745ab4d3b62bc90e30805ab3bd
候选SHA256：6c616afd16aa6a22046ca06573f396682e30010dccbcb24d84536c8b742c5e40

### 具体修改

1. 原：Now its backoff counter is down to zero, so it can access the channel and transmit its data packet. Again, being optimistic, we say that this is successful, so it receives the acknowledgment after SIFS. We are all happy because all nodes could transmit their data packets successfully. This is an example of applying the backoff procedure under this condition. It also allows us to understand the importance of backoff. That is the ultimate goal I was aiming for.
   候选：Now its backoff counter is down to zero, so [it / you, unclear] can access the channel and transmit its data packet. And again, being optimistic, we say that this is successful, so [it / we, unclear] will receive the acknowledgement after SIFS. And we are all happy because all nodes could transmit [their data packet successfully, unclear]. Okay, so this is an example of how we apply [in the, unclear] backoff procedure, in particular under this condition, right? But it allows [us, unclear] also to understand the importance of backoff. That's the final goal [that I, unclear], the ultimate goal that I was aiming.
   理由：Restore And again, future receive, okay/right, But, and final goal / ultimate goal restart. Mark corrupted all-nodes-success clause and disfluent apply-in-the words; do not certify the existing smooth wording.
   来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-010,chunk-011

### 逐单元证据

1. Now its backoff counter is down to zero, so [it / you, unclear] can access the channel and transmit its data packet.
现在，它的退避计数器降到了零，所以[它／你，待听辨]可以接入信道并发送它的数据包。
   来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 13, absolute 1768.16–1780.12s; source text retained in review packet
   限制：Feishu and Qwen say it; Whisper says you.
2. And again, being optimistic, we say that this is successful, so [it / we, unclear] will receive the acknowledgement after SIFS.
再一次，乐观地说，我们说这次是成功的，所以[它／我们，待听辨]会在 SIFS 之后收到确认。
   来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-010, segment(s) 13,14, absolute 1768.16–1788.62s; source text retained in review packet
   限制：Qwen says it will receive; Feishu and Whisper say we will receive.
3. And we are all happy because all nodes could transmit [their data packet successfully, unclear].
我们都很高兴，因为所有节点都能够[成功发送各自的数据包，待听辨]。
   来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 1, absolute 1785.00–1794.20s; source text retained in review packet
   限制：The final words are corrupted across all three sources: Feishu data packet.Success; Qwen all nice good transmit that part, success; Whisper all knots go towards making that part successful. The displayed wording is an explicit provisional reading, not a certified restoration.
4. Okay, so this is an example of how we apply [in the, unclear] backoff procedure, in particular under this condition, right?
好，所以，这是一个我们如何应用[此处有不清楚的词]退避过程的例子，特别是在这种情况下，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 2,3, absolute 1798.44–1810.02s; source text retained in review packet
   限制：All three sources retain a disfluent word sequence before backoff; do not silently smooth it into applying the backoff procedure.
5. But it allows [us, unclear] also to understand the importance of backoff.
但是，它也让[我们，待听辨]理解退避的重要性。
   来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 4, absolute 1812.54–1824.50s; source text retained in review packet
   限制：Whisper includes us; Qwen omits it; this continuation is absent in the mapped Feishu paragraph but present in both raw ASR windows.
6. That's the final goal [that I, unclear], the ultimate goal that I was aiming.
这就是最后的目标[我所，待听辨]，我所追求的最终目标。
   来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 4, absolute 1812.54–1824.50s; source text retained in review packet
   限制：Qwen retains that I before the restart; Whisper omits it. Preserve final goal and ultimate goal rather than merging them.

## 28 · 00:30:26 · 通过消融实验考察没有退避的系统

稳定块ID：doxcnflAqqxvBp3Q5Cl2hIhippc
原块SHA256：d777be26bb231b0eee71864fa4ff0315763457e5f8c6eee6d2f79f08420aca9a
候选SHA256：441b006e596555b93e068f22a9f50bd1a7e06c0e6a571659c46cfeb65feb7cc7

### 具体修改

1. 原：How can we understand the importance of backoff? Let's make a little game that, scientifically speaking, is called an ablation study. An ablation study is when you remove a feature of a system and study the behavior of that system without that feature. Our small game is an ablation study of this particular backoff procedure, or Wi-Fi channel access. Let's think: what would happen if backoff were not there?
   候选：How can we understand the importance of backoff? Well, let's make a little game that is, scientifically speaking, is called ablation study, okay? An ablation study is when you remove a feature of a system, and you study the behavior of that system without that feature. So our small game is an ablation study of this particular [um, unclear] backoff procedure, or, or Wi-Fi channel access. So let's make this [a, unclear] small game and think, what would happen if the backoff were not there?
   理由：Restore Well, that is...is, okay, repeated or, or and lets make this small game. Mark um and this a conflicts rather than deleting fillers or grammatically repairing the doubled is.
   来源：Feishu historical snapshot mapped source_index_zero_based=33,34; source block(s) 71,73; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011

### 逐单元证据

1. How can we understand the importance of backoff?
我们怎样才能理解退避的重要性？
   来源：Feishu historical snapshot mapped source_index_zero_based=33,34; source block(s) 71,73; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 5, absolute 1826.42–1830.98s; source text retained in review packet
2. Well, let's make a little game that is, scientifically speaking, is called ablation study, okay?
嗯，让我们做一个小游戏，这就是，从科学上说，是叫作消融研究的东西，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=33,34; source block(s) 71,73; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 6, absolute 1830.98–1843.66s; source text retained in review packet
3. An ablation study is when you remove a feature of a system, and you study the behavior of that system without that feature.
消融研究就是，你去掉一个系统的某个特性，然后研究没有那个特性时这个系统的行为。
   来源：Feishu historical snapshot mapped source_index_zero_based=33,34; source block(s) 71,73; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 7,8, absolute 1843.66–1856.84s; source text retained in review packet
4. So our small game is an ablation study of this particular [um, unclear] backoff procedure, or, or Wi-Fi channel access.
所以，我们这个小游戏是对这个特定的[嗯，待听辨]退避过程，或者，或者 Wi-Fi 信道接入，做一个消融研究。
   来源：Feishu historical snapshot mapped source_index_zero_based=33,34; source block(s) 71,73; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 9, absolute 1856.84–1869.88s; source text retained in review packet
   限制：Qwen records um; Feishu and Whisper omit it. The repeated or, or is present in Feishu and Qwen and is retained.
5. So let's make this [a, unclear] small game and think, what would happen if the backoff were not there?
所以，让我们做这个[这里是否有 a，待听辨]小游戏并想一想，如果没有退避，会发生什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=33,34; source block(s) 71,73; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 10, absolute 1869.88–1882.16s; source text retained in review packet
   限制：Qwen and Whisper say this a small game; Feishu says this small game. No grammatical cleanup is applied.

## 29 · 00:31:22 · 移除退避后重新推演

稳定块ID：doxcnAnl1U8JJCpnEoEzHr9c7lb
原块SHA256：5a5570b2c333bf1e13e6a8e0ba56b30af547581ac6b574eee77ccf52eb120b94
候选SHA256：3137a1a28379ddf8f6f6544efce47f5b68158344fc2804da8dc0a523a5faaa0f

### 具体修改

1. 原：Let's roll back the story and start from the beginning, but this time assume there is no backoff. What would be the behavior of our nodes?
   候选：Okay, so let's roll back the story, let's start from the beginning, but this time let's assume that there is no backoff, okay? So what would be the behavior of our nodes?
   理由：Restore Okay, so, lets start, lets assume and the final okay. Preserve the spoken two lets clauses instead of connecting them with and.
   来源：Feishu historical snapshot mapped source_index_zero_based=35; source block(s) 75; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011

### 逐单元证据

1. Okay, so let's roll back the story, let's start from the beginning, but this time let's assume that there is no backoff, okay?
好，所以，让我们把这个故事倒回去，让我们从头开始，但这次我们假设没有退避，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=35; source block(s) 75; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 11,12, absolute 1882.16–1900.02s; source text retained in review packet
2. So what would be the behavior of our nodes?
那么，我们的节点会有怎样的行为？
   来源：Feishu historical snapshot mapped source_index_zero_based=35; source block(s) 75; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 12,13, absolute 1891.18–1906.84s; source text retained in review packet

## 30 · 00:31:43 · 无退避时A的首次发送不变

稳定块ID：doxcnEeDj97Jx5ls3DFI6r5ApEb
原块SHA256：af41a6baf7de3a805c4c3ef802ec9181f15055ae882ca2c9f6807b7ba36a0024
候选SHA256：21191b912af3e1ef1b7419a139110bd7a936302fb597db1780ddfd7beab8d0bc

### 具体修改

1. 原：At the beginning everything is the same because the only node with a packet to transmit is A. It listens to the channel, the channel is idle for DIFS, and it accesses the channel and transmits the packet.
   候选：Well, at the beginning everything is the same because the only node that has got a packet to transmit is A, right? So it will listen to the channel, the channel is idle for DIFS. It will access the channel and transmit the packet.
   理由：Restore Well, the only node that has got, right, So, and both will clauses. Do not substitute simple-present actions for the spoken future forms.
   来源：Feishu historical snapshot mapped source_index_zero_based=36; source block(s) 77; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011

### 逐单元证据

1. Well, at the beginning everything is the same because the only node that has got a packet to transmit is A, right?
嗯，在一开始，一切都是一样的，因为唯一拿到了一个要发送的数据包的节点是 A，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=36; source block(s) 77; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 13,14, absolute 1900.02–1914.68s; source text retained in review packet
2. So it will listen to the channel, the channel is idle for DIFS.
所以，它会侦听信道，信道空闲了一个 DIFS 的时间。
   来源：Feishu historical snapshot mapped source_index_zero_based=36; source block(s) 77; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 14,15, absolute 1906.84–1921.78s; source text retained in review packet
3. It will access the channel and transmit the packet.
它会接入信道并发送这个数据包。
   来源：Feishu historical snapshot mapped source_index_zero_based=36; source block(s) 77; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 15, absolute 1914.68–1921.78s; source text retained in review packet

## 31 · 00:32:02 · B和C同时发送导致必然碰撞

稳定块ID：doxcnL5doQmZhvSVxCEH7EvQeUc
原块SHA256：e4bc0d7462d7f60eed5f5440f866686f1d6232872b1f364be55b8261ef69fbd4
候选SHA256：c1853acefbc42d11a92d49fbb8942f06b99c6633a678a4e5af42a603a2b9ac43

### 具体修改

1. 原：Again, let's be optimistic: the access point sends back an acknowledgment, and the other nodes B and C both set their NAV. This is exactly as before. Assume that B and C also get a packet to transmit at different points in time. But now we do not have backoff. We have to think what would happen if backoff were not there. What would B and C do? We still have carrier-sense multiple access. Since B and C both sense the channel as busy because their NAV is set, they cannot access the channel while it is busy. They will wait for it to become idle and make sure it is idle. But if there is no backoff, they can then access the channel. They say: the channel is idle, I can access it and transmit. Remember, in this game we assume there is no backoff. Both transmit their data packets after sensing the channel idle. What do we have here? A collision. They both access the channel at the same time with probability one. It is certain they will do that, and they fail because their transmissions overlap. The access point will not be able to demodulate either packet correctly.
   候选：And again, let's be optimistic. The access point sends back [the / an / no article, unclear] acknowledgement, and the other nodes, B and C, both set their NAV, right? This is exactly as before. And again, B and C at different points in time, assume that they [get / got, unclear] also a packet to transmit. But again, now we do not have backoff, okay? So we have to think, what would happen if backoff were not there? So what would B and C do? Well, we still have carrier sensing, right, multiple access. So since both B and C sense the channel as busy because they have their NAV set, they cannot access the channel, right? [Till; usage unclear] the channel is busy, I cannot access the channel. So for sure B and C will again wait for the channel to be idle, make sure that the channel is idle. But then if there is no backoff, they can just access the channel, right? Because now the channel is idle, so they say, oh, channel idle, I can access the channel and transmit. Remember, we are playing this small game assuming that there is no backoff. So what we have is that, no backoff, we have both transmitting their data packet after having sensed the channel idle. So what do we have here? Collision, right? They both access the channel at the same time with probability one. It is sure that they will do that, and of course they will fail because they overlap, their transmissions overlap. And the access point will not be able to demodulate correctly either this packet.
   理由：Restore repeated questions, Okay/So/Well/right, Till...I cannot, no backoff restart, and because they overlap, their transmissions overlap. Preserve the grammatically awkward either this packet. Article and get/got remain flagged. Independent QA adds explicit Till-usage uncertainty in both languages; no protocol-based replacement with while/as long as.
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011,chunk-012

### 逐单元证据

1. And again, let's be optimistic.
再一次，让我们乐观一点。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 16, absolute 1921.78–1928.20s; source text retained in review packet
2. The access point sends back [the / an / no article, unclear] acknowledgement, and the other nodes, B and C, both set their NAV, right?
接入点发回确认，[英文这里的冠词待听辨]，而其他节点 B 和 C 都设置自己的 NAV，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 16,17, absolute 1921.78–1936.66s; source text retained in review packet
   限制：Acknowledgement article differs across sources. NAV is explicit technical normalization of NAF/knobs/now variants; historical Feishu incorrectly has send their packets.
3. This is exactly as before.
这和之前完全一样。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 17, absolute 1928.20–1936.66s; source text retained in review packet
4. And again, B and C at different points in time, assume that they [get / got, unclear] also a packet to transmit.
再一次，B 和 C 在不同的时间点，假设它们也[拿到／拿到了，待听辨]一个要发送的数据包。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 18, absolute 1936.66–1947.46s; source text retained in review packet
   限制：Feishu and Whisper say get; Qwen says got. The loose sentence structure is retained.
5. But again, now we do not have backoff, okay?
但是，再说一次，现在我们没有退避，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 19, absolute 1947.46–1957.10s; source text retained in review packet
6. So we have to think, what would happen if backoff were not there?
所以，我们必须想一想，如果没有退避，会发生什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 20, absolute 1957.10–1966.56s; source text retained in review packet
7. So what would B and C do?
那么，B 和 C 会做什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 20, absolute 1957.10–1966.56s; source text retained in review packet
8. Well, we still have carrier sensing, right, multiple access.
嗯，我们仍然有载波侦听，对吧，多址接入。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-011, segment(s) 21, absolute 1967.94–1977.04s; source text retained in review packet
9. So since both B and C sense the channel as busy because they have their NAV set, they cannot access the channel, right?
所以，由于 B 和 C 都侦听到信道为忙，因为它们设置了 NAV，它们就不能接入信道，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 2, absolute 1977.64–1986.52s; source text retained in review packet
10. [Till; usage unclear] the channel is busy, I cannot access the channel.
〔Till，讲者此处时间条件用法待听辨〕信道忙着时，我不能接入信道。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 3, absolute 1986.52–1996.24s; source text retained in review packet；Documented disfluency, boundary or notation note: Till is retained as heard in Feishu and Whisper, even though while would be standard English here; no silent lexical substitution is made.
   限制：Historical Feishu has Till the channel is busy. Retain Till instead of silently replacing it with while/as long as. Its temporal usage is explicitly flagged in both languages; the Chinese does not resolve the condition by protocol knowledge.
11. So for sure B and C will again wait for the channel to be idle, make sure that the channel is idle.
所以，B 和 C 肯定会再次等待信道变为空闲，确认信道是空闲的。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 3,4, absolute 1986.52–2003.98s; source text retained in review packet
12. But then if there is no backoff, they can just access the channel, right?
但是随后，如果没有退避，它们就可以直接接入信道，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 5, absolute 2005.34–2014.24s; source text retained in review packet
13. Because now the channel is idle, so they say, oh, channel idle, I can access the channel and transmit.
因为现在信道是空闲的，所以它们说，哦，信道空闲，我可以接入信道并发送。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 6, absolute 2014.24–2020.60s; source text retained in review packet
14. Remember, we are playing this small game assuming that there is no backoff.
记住，我们是在玩这个小游戏，假设没有退避。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 7, absolute 2020.60–2026.28s; source text retained in review packet
15. So what we have is that, no backoff, we have both transmitting their data packet after having sensed the channel idle.
所以，我们得到的情况是，没有退避，我们有两个节点都在侦听到信道空闲之后发送自己的数据包。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 8,9, absolute 2026.58–2049.66s; source text retained in review packet
16. So what do we have here?
所以，我们这里有什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 10, absolute 2051.52–2063.28s; source text retained in review packet
17. Collision, right?
碰撞，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 10, absolute 2051.52–2063.28s; source text retained in review packet
18. They both access the channel at the same time with probability one.
它们以概率一同时接入信道。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 10, absolute 2051.52–2063.28s; source text retained in review packet
19. It is sure that they will do that, and of course they will fail because they overlap, their transmissions overlap.
它们肯定会这样做，当然它们会失败，因为它们重叠了，它们的传输重叠了。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 11,12, absolute 2063.28–2078.16s; source text retained in review packet
20. And the access point will not be able to demodulate correctly either this packet.
而接入点将无法正确解调这两个数据包中的任何一个。
   来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 13, absolute 2078.16–2087.28s; source text retained in review packet；Documented disfluency, boundary or notation note: The nonstandard wording either this packet is retained in all three source streams rather than repaired to either packet.

## 32 · 00:34:43 · 退避作为碰撞避免机制

稳定块ID：doxcnH4jHHn6Pl1bEysoXgDtTjo
原块SHA256：ebd6035fb6a2023cc5b0a6b92dfec0d1dfa28ceca54d430b18343c7395f05c2d
候选SHA256：c63cb4b451eef4db7598e58408b7626ca1e54e0edbd03d75280f8d71c1ddc004

### 具体修改

1. 原：The first conclusion is that backoff was introduced in our system to avoid collisions between contending nodes. In this example B and C contend for the channel, and backoff is there to avoid their collision. Remember that we said Wi-Fi is a CSMA scheme with collision avoidance.
   候选：Okay, so what is the first conclusion here? That the backoff procedure has been introduced in our system in order to avoid collisions between contending nodes. Our contending nodes in these examples are B and C, right? They are contending for the channel. And the backoff procedure is there to avoid the collision between them. So again, remember that we said Wi-Fi is a CSMA scheme with collision avoidance, [right, unclear]?
   理由：Restore the question-and-answer opening, our contending nodes in these examples, They are contending..., and So again remember that we said. The Wi-Fi/CSMA continuation is corroborated by both raw ASR windows.
   来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-012

### 逐单元证据

1. Okay, so what is the first conclusion here?
好，所以，这里的第一个结论是什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 13,14, absolute 2078.16–2095.88s; source text retained in review packet
2. That the backoff procedure has been introduced in our system in order to avoid collisions between contending nodes.
就是，在我们的系统中引入退避过程，是为了避免竞争节点之间的碰撞。
   来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 14,15, absolute 2087.28–2108.04s; source text retained in review packet
3. Our contending nodes in these examples are B and C, right?
在这些例子中，我们的竞争节点是 B 和 C，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 16, absolute 2108.04–2116.90s; source text retained in review packet
4. They are contending for the channel.
它们在竞争信道。
   来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 16, absolute 2108.04–2116.90s; source text retained in review packet
5. And the backoff procedure is there to avoid the collision between them.
退避过程就是用来避免它们之间的碰撞的。
   来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 17, absolute 2116.90–2127.72s; source text retained in review packet
6. So again, remember that we said Wi-Fi is a CSMA scheme with collision avoidance, [right, unclear]?
所以，再说一次，记住我们说过，Wi-Fi 是一种带碰撞避免的 CSMA 方案，[对吧，待听辨]？
   来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 17,18, absolute 2116.90–2137.26s; source text retained in review packet
   限制：Qwen includes right; Whisper does not. This continuation is supported by both ASR windows though absent from the mapped Feishu block.

## 33 · 00:35:39 · 错开行动时间减少拥挤

稳定块ID：doxcnaHvvyUzO5ghSRmyafl5mXf
原块SHA256：5261b73e44cc835a2cd13cb6db68c54b9898f83574620949e33eeed209d33873
候选SHA256：6687aa9e3a3cc28d03615181d64afd339feb4219ec8adc4f4e3e1405382fc013

### 具体修改

1. 原：Backoff is a mechanism that helps avoid collisions. The basic idea is very simple: whenever there is a crowded situation, you try to desynchronize from the others so that you find a free road ahead. It is exactly the same thing. If it is peak hour, you don't want to jump into the traffic like everyone else.
   候选：This backoff is a mechanism that helps to avoid collisions. So the basic principle, the basic idea is very simple. Whenever there is a crowded situation, right, you try to desynchronize from the others so that you find a free [route / road, unclear] ahead, and this is exactly the same thing. So if there is peak hour, you don't want to jump into the traffic, right, [as all / as for, unclear] the others.
   理由：Restore the basic principle, the basic idea restart and right. Keep route/road and as all/as for conflicts visible. Desynchronize is supported by both independent model families against Feishu synchronize.
   来源：Feishu historical snapshot mapped source_index_zero_based=40; source block(s) 85; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-012,chunk-013

### 逐单元证据

1. This backoff is a mechanism that helps to avoid collisions.
这个退避是一种帮助避免碰撞的机制。
   来源：Feishu historical snapshot mapped source_index_zero_based=40; source block(s) 85; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-012, segment(s) 19, absolute 2138.04–2152.50s; source text retained in review packet
2. So the basic principle, the basic idea is very simple.
所以，基本原理，基本想法，非常简单。
   来源：Feishu historical snapshot mapped source_index_zero_based=40; source block(s) 85; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 1, absolute 2145.00–2161.26s; source text retained in review packet
3. Whenever there is a crowded situation, right, you try to desynchronize from the others so that you find a free [route / road, unclear] ahead, and this is exactly the same thing.
每当出现拥挤的情况，对吧，你就试着与其他人错开，使你前面有一条空闲的[路线／道路，待听辨]，而这完全是同一回事。
   来源：Feishu historical snapshot mapped source_index_zero_based=40; source block(s) 85; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 2,3, absolute 2161.26–2179.78s; source text retained in review packet
   限制：Qwen and Whisper support desynchronize against the Feishu synchronize error. Route is in Qwen and one Whisper overlap, road in Feishu; keep the lexical conflict.
4. So if there is peak hour, you don't want to jump into the traffic, right, [as all / as for, unclear] the others.
所以，如果是高峰时段，你就不想冲进车流，对吧，[像其他所有人／至于其他人，待听辨]。
   来源：Feishu historical snapshot mapped source_index_zero_based=40; source block(s) 85; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 4, absolute 2179.78–2185.36s; source text retained in review packet
   限制：Feishu has as all the others; Qwen has as for the others; Whisper has or the others. Do not recast this as like everyone else.

## 34 · 00:36:25 · 避开高峰时段的生活类比

稳定块ID：doxcnYoikxJiKfhskkvbqwaXuzb
原块SHA256：e9f9ab5031ab3a93d4063bb4be37d4ee7364d76eec6f302309523c5761e092f9
候选SHA256：9e5bd7d18d9f8fb6b62a9f7a85b0cd4c2a5e238b9c3c7682c2be9d42e7a4dad0

### 具体修改

1. 原：You wait and try to pick a time when not many other people will be there. It is the same principle. You pick a time to desynchronize your action from the others, avoiding collisions with them or finding yourself in a traffic jam. That's exactly the same principle.
   候选：You try to pick, you wait, you try to pick a time at which not many other people will be there. And this is exactly the same principle. You try to pick a time in order to desynchronize your action with respect to the others, and this way you avoid meeting, [unclear words], colliding with the others, or finding yourself in a, in a traffic jam. [Hmm, unclear], that's exactly the same principle.
   理由：Restore You try to pick, you wait, you try to pick, with respect to the others, and in a, in a. Leave corrupted linking words before colliding and possible Hmm unresolved rather than inventing a smooth sentence.
   来源：Feishu historical snapshot mapped source_index_zero_based=41; source block(s) 87; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-013

### 逐单元证据

1. You try to pick, you wait, you try to pick a time at which not many other people will be there.
你试着挑选，你等待，你试着挑选一个没有太多其他人会在那里的时间。
   来源：Feishu historical snapshot mapped source_index_zero_based=41; source block(s) 87; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 5, absolute 2185.36–2193.50s; source text retained in review packet
2. And this is exactly the same principle.
而这完全是同一个原理。
   来源：Feishu historical snapshot mapped source_index_zero_based=41; source block(s) 87; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 6, absolute 2193.50–2201.58s; source text retained in review packet
3. You try to pick a time in order to desynchronize your action with respect to the others, and this way you avoid meeting, [unclear words], colliding with the others, or finding yourself in a, in a traffic jam.
你试着挑选一个时间，让你的行动与其他人的行动错开，这样你就避免遇到，[此处词语不清楚]，与其他人发生碰撞，或者发现自己陷在一个，一个交通堵塞中。
   来源：Feishu historical snapshot mapped source_index_zero_based=41; source block(s) 87; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 6,7,8, absolute 2193.50–2217.24s; source text retained in review packet
   限制：Feishu/Qwen have meeting like they colliding; Whisper has meeting and fake aligning. The connecting words remain unclear. The repeated in a, in a is supported by Feishu and Qwen, not removed for fluency.
4. [Hmm, unclear], that's exactly the same principle.
[嗯，待听辨]，这完全是同一个原理。
   来源：Feishu historical snapshot mapped source_index_zero_based=41; source block(s) 87; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 9, absolute 2218.68–2228.88s; source text retained in review packet
   限制：Hmm occurs in the historical snapshot only.

## 35 · 00:37:02 · 相同退避值仍会导致碰撞

稳定块ID：doxcn5gHcCr2H8OejWkUDf8rjJg
原块SHA256：91eabedfa12ae3a532c8803a8f23b6c6eca2288431034f8a3d12d256196ac0b3
候选SHA256：e3e0498d151dea8b5663b01b35ed1bd516d944ce7d691c4101302e83569e9b75

### 具体修改

1. 原：What I want to underline is that our first observation is that backoff is a collision-avoidance mechanism, but it is still probabilistic. Why? If B and C draw the same backoff value, they are going to collide. If C too drew two as its integer, then they would not be desynchronized from each other. Both decrease their counters during the first time slot and again during the second. Under the assumption that both drew two, their counters reach zero at exactly the same time. They access the channel at exactly the same time and collide.
   候选：Now what I would like to underline is that, so we observe, our first observation is that backoff is a mechanism for avoiding collisions, but it is still probabilistic, okay? Why? Because if, like in our example, both B and C draw the same value of backoff, they are going to collide. Okay, so if, for example, C too drew two as an integer, then they will not be [synchronized / desynchronized, unclear] from each other, okay? Because they will both decrease the [the, unclear] backoff counter during the first time slot, and then again during the second time slot. But under the assumption that they now both drew two as an integer, they will decrease the backoff counter to zero exactly at the same time. That means that they will access the channel exactly at the same time and collide.
   理由：Restore Now what I would like to underline, so we observe, our first observation; restore because/okay/future clauses. Do not silently turn synchronized into technically expected desynchronized; retain both as pending listening.
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-013,chunk-014

### 逐单元证据

1. Now what I would like to underline is that, so we observe, our first observation is that backoff is a mechanism for avoiding collisions, but it is still probabilistic, okay?
现在，我想强调的是，所以我们观察到，我们的第一个观察是，退避是一种避免碰撞的机制，但它仍然是概率性的，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 9,10,11, absolute 2218.68–2244.54s; source text retained in review packet
2. Why?
为什么？
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 11, absolute 2235.60–2244.54s; source text retained in review packet
3. Because if, like in our example, both B and C draw the same value of backoff, they are going to collide.
因为，如果像我们的例子中那样，B 和 C 都抽到同一个退避值，它们就会发生碰撞。
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 12, absolute 2244.54–2272.20s; source text retained in review packet
4. Okay, so if, for example, C too drew two as an integer, then they will not be [synchronized / desynchronized, unclear] from each other, okay?
好，所以，如果，例如，C 也抽到了二这个整数，那么它们彼此就不会[同步／错开，待听辨]，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 13, absolute 2272.20–2302.10s; source text retained in review packet
   限制：Historical Feishu and Qwen say synchronized; Whisper skips the relevant phrase. The expected technical meaning would suggest desynchronized, but that is not authority to replace the spoken word.
5. Because they will both decrease the [the, unclear] backoff counter during the first time slot, and then again during the second time slot.
因为它们都会在第一个时隙内递减这个[英文这里是否重复 the，待听辨]退避计数器，然后在第二个时隙内再递减一次。
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 14, absolute 2302.10–2311.88s; source text retained in review packet
   限制：Qwen has the the; historical Feishu has the once; Whisper drops part of this clause. The potential repetition is not silently either added or removed.
6. But under the assumption that they now both drew two as an integer, they will decrease the backoff counter to zero exactly at the same time.
但是，在假设它们现在都抽到了二这个整数的情况下，它们会在完全相同的时刻把退避计数器减到零。
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 15,16, absolute 2312.98–2330.68s; source text retained in review packet
7. That means that they will access the channel exactly at the same time and collide.
这意味着，它们会在完全相同的时刻接入信道，并发生碰撞。
   来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 17, absolute 2331.32–2336.42s; source text retained in review packet

## 36 · 00:38:58 · 退避只能概率性地避免碰撞

稳定块ID：doxcnMJm7xgchJDesFLgciG9Hwf
原块SHA256：71c127a6633c58e52f40b3c8677b2f579bac4b0c9de171e58f209c4be7c365c9
候选SHA256：3417290cce426a2ddc4a840832931befc4c390deb25bc7a4c19ba7bda64b4bee

### 具体修改

1. 原：Backoff is a way to avoid collisions, but it does not avoid them with probability one. There is still a certain probability that contending nodes may collide. It is a probabilistic collision-avoidance mechanism.
   候选：So backoff is a way to avoid collisions, but it does not avoid collisions with probability one. There is still a certain probability with which the nodes, the contending nodes, may collide, [right / okay, unclear]? So it's a probabilistic collision-avoidance mechanism.
   理由：Restore So, repeated collisions instead of them, and the nodes, the contending nodes restart. Keep the right/okay filler conflict visible.
   来源：Feishu historical snapshot mapped source_index_zero_based=43; source block(s) 91; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-013,chunk-014

### 逐单元证据

1. So backoff is a way to avoid collisions, but it does not avoid collisions with probability one.
所以，退避是一种避免碰撞的方法，但它并不是以概率一避免碰撞。
   来源：Feishu historical snapshot mapped source_index_zero_based=43; source block(s) 91; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-013, segment(s) 18, absolute 2338.64–2347.62s; source text retained in review packet
2. There is still a certain probability with which the nodes, the contending nodes, may collide, [right / okay, unclear]?
仍然存在一定的概率，使这些节点，这些竞争节点，可能发生碰撞，[对吧／好吗，待听辨]？
   来源：Feishu historical snapshot mapped source_index_zero_based=43; source block(s) 91; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 4, absolute 2347.66–2358.02s; source text retained in review packet
   限制：Feishu has right; Qwen has okay; Whisper omits the filler. The nodes, the contending nodes restart is supported by all three.
3. So it's a probabilistic collision-avoidance mechanism.
所以，它是一种概率性的碰撞避免机制。
   来源：Feishu historical snapshot mapped source_index_zero_based=43; source block(s) 91; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 5, absolute 2358.74–2366.68s; source text retained in review packet

## 37 · 00:39:28 · 准备讨论扩大竞争窗口的作用

稳定块ID：doxcnFC44DVHPRPxjnurob5RDFf
原块SHA256：0e4c6a9a7f229a7cd0ff36ebbc85f438bb0134abee16f46332a1225c070df42c
候选SHA256：bfdd8c1a7a773b4254aa429e3e72e4756648a6b40be44814c37aa1d663421480

### 具体修改

1. 原：This is our first observation. Is it clear so far? If so, let me make a second one. Sorry, let me check this, because today is a bit different. We have a second observation to make. We are close to the break, but let me start introducing it, then we will finish after the short break.
   候选：Okay, this is our first observation. Is it clear so far? Okay, now if this is clear, let me make a second, [sorry, check this, because today is a bit different, unclear]. Okay, we have a second observation to make. We are close to the break, but let me start introducing it, and then we will finish after [the / a, unclear] short break.
   理由：Restore Okay, now if this is clear, let me make a second and the repeated second observation. Mark the aside found in Feishu but corrupted/omitted in both models instead of declaring it verified.
   来源：Feishu historical snapshot mapped source_index_zero_based=44; source block(s) 93; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014

### 逐单元证据

1. Okay, this is our first observation.
好，这是我们的第一个观察。
   来源：Feishu historical snapshot mapped source_index_zero_based=44; source block(s) 93; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 6, absolute 2368.46–2375.20s; source text retained in review packet
2. Is it clear so far?
到目前为止清楚吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=44; source block(s) 93; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 6, absolute 2368.46–2375.20s; source text retained in review packet
3. Okay, now if this is clear, let me make a second, [sorry, check this, because today is a bit different, unclear].
好，现在，如果这点清楚了，让我作第二个，[抱歉，检查一下这个，因为今天有点不同，待听辨]。
   来源：Feishu historical snapshot mapped source_index_zero_based=44; source block(s) 93; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 7, absolute 2375.20–2395.72s; source text retained in review packet
   限制：The historical snapshot contains this aside; Qwen corrupts it into Say, check this time. This was the possibility; Whisper drops it. Do not present the fluent existing aside as independently verified.
4. Okay, we have a second observation to make.
好，我们要作第二个观察。
   来源：Feishu historical snapshot mapped source_index_zero_based=44; source block(s) 93; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 7, absolute 2375.20–2395.72s; source text retained in review packet
5. We are close to the break, but let me start introducing it, and then we will finish after [the / a, unclear] short break.
我们快到休息时间了，但让我先开始介绍它，然后我们会在短暂休息之后把它讲完，[英文冠词是 the 还是 a，待听辨]。
   来源：Feishu historical snapshot mapped source_index_zero_based=44; source block(s) 93; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 8, absolute 2395.98–2407.34s; source text retained in review packet
   限制：Feishu and Whisper have the short break; Qwen has a short break.

## 38 · 00:40:13 · CW最小值范围内共有多少整数

稳定块ID：doxcnXhZOazuwIoJDnSvi0fuhad
原块SHA256：d7e6ba545f2843f1bea27e778c0d831602a808006d585e73599c6393f6e06522
候选SHA256：134171ce356aaa96fde72658a99e606089f16fa2da556127bac891b9e89d3992

### 具体修改

1. 原：The second observation concerns the benefit of increasing the contention window every time we need to perform backoff for a given data packet. Consider the same example as before: the access point, A, B, and C. A talks with the access point, then B and C both get a packet while the channel is busy. They need to apply backoff and, after sensing the channel idle for DIFS, draw an integer from this range of values. Since this is the first time they run backoff for this packet, both use zero to CW_min as the range of possible integers. How many values are there? There are CW_min plus one integers.
   候选：So the second observation that I want to make is about the benefit of increasing the contention window parameter every time we need to perform a backoff procedure for a given data packet, okay? So let's consider still the same example as before. So we still have the access point, A, B and C. A talk with the access point, then B and C get the packet, both of them, while the channel is busy. So they need to apply the backoff, and they need to draw [unclear words], after having sensed the channel as idle for DIFS, an integer out of, as we know, out of this range of values, because this is the first time that they run the backoff for the packet. So they both use zero, contention window minimum, as a possible range, as a range of possible integers to be selected. So how many values are [in / in in, unclear] this range? There are CW_min...
   理由：Restore parameter, given, Okay/So, A talk, both of them, the corrupted phrase following draw, out of...out of, as a possible range, as a range. Keep in/in in unresolved. Split the CW_min sentence at the existing 41:48 anchor according to new word times; do not duplicate the continuation.
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014,chunk-015

### 逐单元证据

1. So the second observation that I want to make is about the benefit of increasing the contention window parameter every time we need to perform a backoff procedure for a given data packet, okay?
所以，我想作的第二个观察，是关于每次需要为一个给定数据包执行退避过程时，增大竞争窗口参数的好处，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 9,10, absolute 2413.42–2436.42s; source text retained in review packet
2. So let's consider still the same example as before.
所以，让我们仍然考虑和之前相同的例子。
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 11, absolute 2436.42–2446.76s; source text retained in review packet
3. So we still have the access point, A, B and C.
所以，我们仍然有接入点、A、B 和 C。
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 11,12, absolute 2436.42–2453.36s; source text retained in review packet
4. A talk with the access point, then B and C get the packet, both of them, while the channel is busy.
A 与接入点交谈，然后 B 和 C 拿到数据包，它们两个都是在信道忙的时候拿到的。
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 12,13, absolute 2446.76–2460.72s; source text retained in review packet；Documented disfluency, boundary or notation note: The nonstandard A talk is retained across all three sources; not changed to A talks.
5. So they need to apply the backoff, and they need to draw [unclear words], after having sensed the channel as idle for DIFS, an integer out of, as we know, out of this range of values, because this is the first time that they run the backoff for the packet.
所以，它们需要执行退避，而且它们需要抽取[此处词语不清楚]，在侦听到信道空闲一个 DIFS 的时间之后，抽取一个整数，从，我们知道，从这个取值范围中抽取，因为这是它们第一次为这个数据包执行退避。
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 14,15, absolute 2461.56–2483.90s; source text retained in review packet
   限制：The phrase after draw is corrupted as the forum / the pour / the quorum across sources. It is explicitly left unresolved, not replaced with a connective that makes the sentence smoother.
6. So they both use zero, contention window minimum, as a possible range, as a range of possible integers to be selected.
所以，它们都使用零、最小竞争窗口，作为一个可能的范围，作为可供选择的整数的范围。
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 16,17, absolute 2483.90–2503.56s; source text retained in review packet
7. So how many values are [in / in in, unclear] this range?
那么，这个范围里有多少个值，[英文这里是否重复 in，待听辨]？
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-014, segment(s) 17, absolute 2492.68–2503.56s; source text retained in review packet
   限制：Qwen has in in; Whisper has in once; the question is absent in the mapped Feishu source block.
8. There are CW_min...
有 CW_min……
   来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 1, absolute 2505.00–2511.08s; source text retained in review packet；Documented disfluency, boundary or notation note: This sentence crosses the existing 00:41:48 anchor. Whisper words CW_min end at 41:47.64 and plus starts at 41:48.48; the continuation is retained at the start of paragraph 39 rather than duplicated.

## 39 · 00:41:48 · 计入零使取值数量增加一

稳定块ID：doxcnRO13xWA67GmmCsSSXmP1Dc
原块SHA256：06e9e0fc4190bf0c6c8b2dfd77c55592471ffe4eb0a4dd6c738eb551822cc695
候选SHA256：0bfd60bf2d52590fb8cf938e0b12e4124074eecd5428a17e1f339194fd20f3b4

### 具体修改

1. 原：Including zero makes it plus one. This is the number of integers in that range.
   候选：Plus one integers, right? Because [unclear words], including the zero is plus one. Okay, this is the number of integers in that range.
   理由：Restore Plus one integers, right? at the 41:48 anchor as the continuation of paragraph 38. Mark unclear words before including the zero rather than reducing the whole utterance to Including zero makes it plus one. Boundary adjustment is explicit.
   来源：Feishu historical snapshot mapped source_index_zero_based=47; source block(s) 99; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014,chunk-015

### 逐单元证据

1. Plus one integers, right?
加一这么多个整数，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=47; source block(s) 99; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 1, absolute 2505.00–2511.08s; source text retained in review packet；Documented disfluency, boundary or notation note: Continuation of There are CW_min in paragraph 38; the existing 41:48 anchor falls inside this spoken sentence. The intended count is CW_min+1, not one added integer, but the English fragment is not rewritten.
2. Because [unclear words], including the zero is plus one.
因为[此处词语不清楚]，包括零就是加一。
   来源：Feishu historical snapshot mapped source_index_zero_based=47; source block(s) 99; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 2, absolute 2511.46–2515.36s; source text retained in review packet
   限制：Whisper has Because the subunit; Qwen has We call this minimum; the Feishu source is corrupted. Only including the zero is plus one has stable support.
3. Okay, this is the number of integers in that range.
好，这就是那个范围里的整数个数。
   来源：Feishu historical snapshot mapped source_index_zero_based=47; source block(s) 99; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 3, absolute 2515.82–2518.48s; source text retained in review packet

## 40 · 00:41:59 · 均匀抽取整数的概率

稳定块ID：doxcn28MvP7iScVrFLXjKMXm82e
原块SHA256：620a9647ecc8e06122f56c896e6c0baf51c9a7495bf095c15f86a289c770c526
候选SHA256：5ef7649a7f2e85c7d2709de1211d96e3a5080f785ed4f550894282c10b0fd3ea

### 具体修改

1. 原：What we want to compute, since we said that backoff is a probabilistic collision-avoidance mechanism, is the probability that B and C collide. That's the probability we want to compute. We already know that they will collide if they draw the same integer from this range. Remember that a node draws an integer with uniform probability: the same probability for every value. If we consider the probability that a node draws a generic integer n, it is one over (CW_min + 1), because this is the number of integers in the range. Since each value has equal probability, it is easy to see that the probability that an integer, a generic integer, is drawn from this range by a node is one over (CW_min + 1). This is basic probability theory. Each integer is selected with exactly the same probability. This probability is the same for all of them.
   候选：Okay, so what we want to compute, since we said that backoff is a probabilistic collision-avoidance mechanism, is the probability that B and C collide. Okay, that's the probability that we want to compute. Okay, now we know already that they will collide if they draw the same integer out of this range. And remember that the way a node draws an integer out of this range is with uniform probability, right? So same probability for every value to be selected by the node. So if we consider the probability for a node to draw a generic integer n out of this range, this probability is given by one over CW_min plus one, right? Because this is the number of integers in the range. Since we draw each value with equal probability, uniform probability, it's easy to see that the probability that an integer, a generic integer, is drawn out of this range by a node is given by one over CW_min plus one. This is basic probability theory, okay? So in this way you can see that they are selected exactly, each of them with the same probability. [Okay, unclear], this probability is the same for all of them.
   理由：Restore repeated Okay, now, we know already, And remember, same probability fragment, equal probability, uniform probability, and an integer, a generic integer. Keep spoken formula words and standard Chinese denominator grouping; do not replace them with a cleaner derivation.
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014,chunk-015

### 逐单元证据

1. Okay, so what we want to compute, since we said that backoff is a probabilistic collision-avoidance mechanism, is the probability that B and C collide.
好，所以，我们想计算的，既然我们说过退避是一种概率性的碰撞避免机制，就是 B 和 C 发生碰撞的概率。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 4,5,6, absolute 2519.66–2533.06s; source text retained in review packet
2. Okay, that's the probability that we want to compute.
好，这就是我们想计算的概率。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 4, absolute 2519.66–2522.40s; source text retained in review packet
3. Okay, now we know already that they will collide if they draw the same integer out of this range.
好，现在我们已经知道，如果它们从这个范围里抽到同一个整数，它们就会碰撞。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 8, absolute 2561.74–2576.98s; source text retained in review packet
4. And remember that the way a node draws an integer out of this range is with uniform probability, right?
还要记住，一个节点从这个范围里抽取整数的方式，是采用均匀概率，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 9, absolute 2576.98–2587.36s; source text retained in review packet
5. So same probability for every value to be selected by the node.
所以，每个值被节点选中的概率相同。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 10, absolute 2587.36–2594.72s; source text retained in review packet
6. So if we consider the probability for a node to draw a generic integer n out of this range, this probability is given by one over CW_min plus one, right?
所以，如果我们考虑一个节点从这个范围中抽到任意一个整数 n 的概率，这个概率由一除以（CW_min 加一）给出，对吧？
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 11,12, absolute 2594.72–2623.04s; source text retained in review packet；Documented disfluency, boundary or notation note: Formula grouping is spoken without written parentheses; the surrounding statement establishes the denominator CW_min+1. The English wording is preserved; no equation is silently substituted.
7. Because this is the number of integers in the range.
因为这就是这个范围中的整数个数。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 3, absolute 2515.82–2518.48s; source text retained in review packet
8. Since we draw each value with equal probability, uniform probability, it's easy to see that the probability that an integer, a generic integer, is drawn out of this range by a node is given by one over CW_min plus one.
由于我们以相等的概率，均匀的概率，抽取每个值，很容易看出，一个整数，一个任意的整数，被一个节点从这个范围里抽到的概率，由一除以（CW_min 加一）给出。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 13,14,15, absolute 2623.04–2646.68s; source text retained in review packet
9. This is basic probability theory, okay?
这是基本的概率论，好吗？
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 16, absolute 2646.68–2661.26s; source text retained in review packet
10. So in this way you can see that they are selected exactly, each of them with the same probability.
所以，这样你就可以看到，它们被选择时，恰好，每一个都具有相同的概率。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 17, absolute 2661.26–2667.58s; source text retained in review packet
11. [Okay, unclear], this probability is the same for all of them.
[好，待听辨]，这个概率对它们所有值都是一样的。
   来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted: chunk-015, segment(s) 18, absolute 2667.58–2674.84s; source text retained in review packet
   限制：The final Okay occurs in Qwen but not Feishu or Whisper.

## 41 · 00:44:32 · 课间休息与碰撞概率预告

稳定块ID：doxcnpL38KX3LtqqoQ5CnydBzNd
原块SHA256：f68b0a9977886e1520fc827cf276a6db87da631b00559168ed6739c0668fafcd
候选SHA256：1db4c34e54e82fe3f731f27a0eb69ff2a962b0e7f0ee9e39d1f8c7464ae377dc

### 具体修改

1. 原：Let's stop for five minutes, and then use the short break...
   候选：Okay, now let's stop for five minutes. And then use the [short break / shortcut unclear], if I'm not wrong.
   理由：恢复Okay、now及被省略的if I’m not wrong；break/shortcut各有来源，不沿用现稿省略号遮掉词语。
   来源：Feishu historical snapshot: source_index=51, id=107, section anchor 00:44:32；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s；Unprompted Whisper medium.en raw: chunk-015, segments 18–20, absolute 2667.58–2690.08s
2. 原：Then we will resume and see how the collision probability can be computed.
   候选：Okay, and then we will resume and see how [this probability / these probabilities unclear] of collision can be computed.
   理由：恢复Okay、and及原来的指示词/单复数冲突，不将probability of collision改写为collision probability。
   来源：Feishu historical snapshot: source_index=51, id=107, section anchor 00:44:32；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s；Unprompted Whisper medium.en raw: chunk-015, segments 19–20, absolute 2674.84–2690.08s；Unprompted Whisper medium.en raw: chunk-016, segments 1–1, absolute 2685.00–2690.08s

### 逐单元证据

1. Okay, now let's stop for five minutes.
好，现在我们停五分钟。
   来源：Feishu historical snapshot: source_index=51, id=107, section anchor 00:44:32；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s；Unprompted Whisper medium.en raw: chunk-015, segments 18–20, absolute 2667.58–2690.08s
2. And then use the [short break / shortcut unclear], if I'm not wrong.
然后利用这个[短暂休息／捷径，待听辨]，如果我没有弄错的话。
   来源：Feishu historical snapshot: source_index=51, id=107, section anchor 00:44:32；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s；Unprompted Whisper medium.en raw: chunk-015, segments 18–20, absolute 2667.58–2690.08s
   限制：Feishu: short way, you cannot run; Qwen 24: shortcut if I'm not wrong; medium chunk-015 segment 19: short break if I'm not wrong. The noun remains unresolved; the latter clause has two-ASR support.
3. Okay, and then we will resume and see how [this probability / these probabilities unclear] of collision can be computed.
好，然后我们会继续，看看[这个／这些，单复数待听辨]碰撞的概率如何能够计算出来。
   来源：Feishu historical snapshot: source_index=51, id=107, section anchor 00:44:32；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s；Unprompted Whisper medium.en raw: chunk-015, segments 19–20, absolute 2674.84–2690.08s；Unprompted Whisper medium.en raw: chunk-016, segments 1–1, absolute 2685.00–2690.08s
   限制：Medium chunks 015/016: this probability; Qwen 24: these probabilities; Feishu: these two probability. Feishu also has an interrupted and / let's see; two ASRs instead agree on and see.

## 42 · 00:49:19 · 从条件概率推导两节点碰撞

稳定块ID：doxcnBQOCHSdBhJ0SZfY43litTc
原块SHA256：53e67ab2c0ca169a19ce28e2523db9edf284be8163dbfe45a9b46163c2da2c91
候选SHA256：85aa820d8004ac62f1d4dc5872a8bb3f078ecf923c6deea4afeab3e6205a3ae1

### 具体修改

1. 原：Good. Let's look at our computation.
   候选：Okay, good. [So / Now unclear], let's look at our computation.
   理由：恢复Okay与So；Now/So来源冲突显式标示。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–1, absolute 2958.90–2977.88s
2. 原：The probability that B and C collide is, as we said, very simple, so don't worry; this is a very simple derivation.
   候选：So, the probability that B and C collide is, as we said, very simply, so [don't / do not unclear] worry, this is a very, very simple derivation.
   理由：恢复So、very simply、不顺的起句和very, very重复；do not/don’t保留词形疑点。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–2, absolute 2958.90–3004.72s
3. 原：It is the probability that B and C draw the same value, let's say n, the same integer.
   候选：Is the probability that B and C draw the same value, let's say n, okay? [A / the unclear] same value, [a / the unclear] same integer. That's what we said, all right.
   理由：撤销添加的It，恢复a same value、a same integer及That’s what we said, all right。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–3, absolute 2958.90–3016.02s
4. 原：Let's start by considering that B draws a given integer n, whatever it is.
   候选：Let's start this computation by considering that B draws n, a given integer n, whatever this is.
   理由：恢复this computation、先说n再重述a given integer n及whatever this is。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 2–5, absolute 2977.88–3056.06s
5. 原：What we first compute is the conditional probability that C also draws n, given that B drew n.
   候选：So, what we are first computing is the [conditional / conditioned unclear] probability, so the probability that C draws also n, so n, given that B drew n, okay? So this is the so-called conditioned probability.
   理由：恢复So、are first computing、第二次so n与对conditioned probability的重述，不统一为书面conditional probability。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 4–6, absolute 3020.72–3065.02s；Unprompted Whisper medium.en raw: chunk-018, segments 1–1, absolute 3045.00–3062.64s
6. 原：Remember that our scheme is simple because it is distributed. Every node makes its own decisions according to the protocol rules, independently of the others.
   候选：Now remember, our scheme is actually very simple because it's distributed. And as we said, every node makes its own decisions according to the protocol rules, but it makes its own decisions independently from the others, right?
   理由：恢复Now、actually very、as we said及it makes its own decisions重复，保留from和right。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-017, segments 6–7, absolute 3056.06–3074.66s；Unprompted Whisper medium.en raw: chunk-018, segments 1–4, absolute 3045.00–3091.06s

### 逐单元证据

1. Okay, good.
好，很好。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–1, absolute 2958.90–2977.88s
2. [So / Now unclear], let's look at our computation.
[所以／现在，待听辨]，我们来看我们的计算。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–1, absolute 2958.90–2977.88s
   限制：Feishu says Now; Qwen 26 and medium chunk-017 segment 1 say So.
3. So, the probability that B and C collide is, as we said, very simply, so [don't / do not unclear] worry, this is a very, very simple derivation.
所以，B 和 C 碰撞的概率，正如我们所说，非常简单地，所以[不用／不要，待听辨]担心，这是一个非常、非常简单的推导。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–2, absolute 2958.90–3004.72s
   限制：All three retain very simply and very, very. Feishu: don't worry; medium: do not worry; Qwen: not worrying. No repair to adjectival simple or extra predicate.
4. Is the probability that B and C draw the same value, let's say n, okay?
就是 B 和 C 抽到相同的值，比如说 n，好吗？
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–3, absolute 2958.90–3016.02s
5. [A / the unclear] same value, [a / the unclear] same integer.
[一个／这个，待听辨]相同的值，[一个／这个，待听辨]相同的整数。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–3, absolute 2958.90–3016.02s
   限制：Feishu and Qwen 27: a same value, a same integer (Feishu mishears integer as image); medium: the same value, the same, then drops the noun. The repeated phrase is retained, with article uncertainty.
6. That's what we said, all right.
那就是我们说的，好吧。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–3, absolute 2958.90–3016.02s
7. Let's start this computation by considering that B draws n, a given integer n, whatever this is.
我们开始这个计算，先考虑 B 抽到 n，一个给定的整数 n，不管这个是多少。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 2–5, absolute 2977.88–3056.06s
8. So, what we are first computing is the [conditional / conditioned unclear] probability, so the probability that C draws also n, so n, given that B drew n, okay?
所以，我们首先正在计算的是[conditional／conditioned，待听辨]概率，也就是 C 也抽到 n 的概率，所以是 n，已知 B 抽到了 n，好吗？
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 4–6, absolute 3020.72–3065.02s；Unprompted Whisper medium.en raw: chunk-018, segments 1–1, absolute 3045.00–3062.64s
   限制：Feishu first says conditional; Qwen 27 says conditioned; medium says condition. The later repeated term is conditioned in Feishu/Qwen/medium-017.
9. So this is the so-called conditioned probability.
所以这就是所谓的条件概率。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 4–6, absolute 3020.72–3065.02s；Unprompted Whisper medium.en raw: chunk-018, segments 1–1, absolute 3045.00–3062.64s
10. Now remember, our scheme is actually very simple because it's distributed.
现在记住，我们的方案实际上非常简单，因为它是分布式的。
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-017, segments 6–7, absolute 3056.06–3074.66s；Unprompted Whisper medium.en raw: chunk-018, segments 1–4, absolute 3045.00–3091.06s
11. And as we said, every node makes its own decisions according to the protocol rules, but it makes its own decisions independently from the others, right?
而且，正如我们说的，每个节点按照协议规则作出自己的决定，但它独立于其他节点作出自己的决定，对吧？
   来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-017, segments 6–7, absolute 3056.06–3074.66s；Unprompted Whisper medium.en raw: chunk-018, segments 1–4, absolute 3045.00–3091.06s

## 43 · 00:51:21 · 节点独立选择与条件无关性

稳定块ID：doxcns4CMNfXgAjgRek2xop5aSh
原块SHA256：510301ad435b7b0905a9fcb05c717497e5ec082c153b65603a314cbdd386fc4b
候选SHA256：4cc00e677eadef63d6c9e73c8b7b03f097c6c3ef8db29782a411047a7c7905e4

### 具体修改

1. 原：The fact that B drew n will not affect the probability that C draws n.
   候选：So, the fact that B drew n will not affect the probability that C draws n.
   理由：恢复句首So，保留drew/draws及will not。
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 4–5, absolute 3080.06–3099.36s
2. 原：C does whatever it decides following the protocol, but it is not affected by what other nodes do.
   候选：C does whatever, let's say, [he / it unclear] likes, based on what decisions [he / it unclear] makes following the protocol, right? But it's not affected by what other nodes do.
   理由：恢复whatever、let’s say、likes、based on what decisions；he/it来源不同，不压缩为decides。
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 4–6, absolute 3080.06–3110.18s
3. 原：This is therefore equal to the probability that C draws n, simply that, because it doesn't matter what B does. C does things by itself.
   候选：So, this is actually equal to the probability that C draws n, simply that, because it doesn't matter what B does, right? C will do things by [itself / himself / themselves unclear].
   理由：恢复So、actually、right和will，末尾反身代词冲突短标。
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 6–8, absolute 3099.36–3142.32s

### 逐单元证据

1. So, the fact that B drew n will not affect the probability that C draws n.
所以，B 抽到了 n 这个事实不会影响 C 抽到 n 的概率。
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 4–5, absolute 3080.06–3099.36s
2. C does whatever, let's say, [he / it unclear] likes, based on what decisions [he / it unclear] makes following the protocol, right?
C 做任何，假设说，[他／它，待听辨]喜欢做的事，根据[他／它，待听辨]遵循协议作出的决定，对吧？
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 4–6, absolute 3080.06–3110.18s
   限制：Feishu and Qwen 28 use he; medium-018 segment 5 uses it. Feishu clearly has let's say; Qwen has it say, medium omits it. Repeated spoken structure restored without choosing the pronoun.
3. But it's not affected by what other nodes do.
但它不会受到其他节点所做事情的影响。
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 4–6, absolute 3080.06–3110.18s
4. So, this is actually equal to the probability that C draws n, simply that, because it doesn't matter what B does, right?
所以，这实际上就等于 C 抽到 n 的概率，就是这样，因为 B 做什么并不重要，对吧？
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 6–8, absolute 3099.36–3142.32s
5. C will do things by [itself / himself / themselves unclear].
C 会[自己，反身代词待听辨]做事情。
   来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 6–8, absolute 3099.36–3142.32s
   限制：Feishu: itself; Qwen 28: himself; medium-018 segments 7–8: themselves. All retain will; current present-tense paraphrase is removed.

## 44 · 00:52:17 · 给定B选择n时C碰撞的概率

稳定块ID：doxcndVEHARMqt6UlFaVILYkrob
原块SHA256：38639c215c9b4dfc4c7b3ea5fdb83e9ba6b027ffebb2a5f5f8bed663130d4e98
候选SHA256：bb432a35f74d2979272880da145a5bec1c4be5b47eb7c54b969ba18c7d7ab961

### 具体修改

1. 原：What is the probability that C draws n? What is the probability that an integer is selected from zero to CW_min? We have written it here.
   候选：Okay, so what is the probability that C draws n? So, what is the probability that an integer is selected out of the range zero, CW_min? Well, we have written that here, right? This is the probability.
   理由：恢复Okay so、第二个So、out of the range、Well及This is the probability，不重写为from ... to。
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 8–10, absolute 3133.94–3162.86s
2. 原：Given that B has drawn n, the probability that C also draws n is this one.
   候选：Okay, so now we know that given that B has drawn n, the probability that C will also draw n is this one.
   理由：恢复Okay so now we know that与will also draw，不改未来式。
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 10–11, absolute 3153.40–3174.20s
3. 原：Conditioned on B drawing n, this is the conditional collision probability.
   候选：Okay, so [conditioned / condition unclear] to the fact that B drew n, then this is the collision probability [conditioned / condition unclear] to the fact that B drew n, right?
   理由：恢复两次to the fact that B drew n、then及right；condition/conditioned的词尾不凭语法补。
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 12–13, absolute 3176.26–3197.04s

### 逐单元证据

1. Okay, so what is the probability that C draws n?
好，所以 C 抽到 n 的概率是什么？
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 8–10, absolute 3133.94–3162.86s
2. So, what is the probability that an integer is selected out of the range zero, CW_min?
所以，从零、CW_min 这个范围中选出一个整数的概率是什么？
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 8–10, absolute 3133.94–3162.86s
3. Well, we have written that here, right?
嗯，我们已经把那个写在这里了，对吧？
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 8–10, absolute 3133.94–3162.86s
4. This is the probability.
这就是那个概率。
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 8–10, absolute 3133.94–3162.86s
5. Okay, so now we know that given that B has drawn n, the probability that C will also draw n is this one.
好，所以现在我们知道，已知 B 已经抽到了 n，C 也会抽到 n 的概率就是这个。
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 10–11, absolute 3153.40–3174.20s
6. Okay, so [conditioned / condition unclear] to the fact that B drew n, then this is the collision probability [conditioned / condition unclear] to the fact that B drew n, right?
好，所以[conditioned／condition，词尾待听辨]于 B 抽到了 n 这个事实，那么这就是[conditioned／condition，词尾待听辨]于 B 抽到了 n 这个事实的碰撞概率，对吧？
   来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 12–13, absolute 3176.26–3197.04s
   限制：Qwen 28 reads conditioned twice; Feishu and medium read condition twice. All retain the repeated to the fact that B drew n structure.

## 45 · 00:53:12 · 遍历所有n去掉条件限制

稳定块ID：doxcn1OwmYmonhT50Rlx5H4yd4K
原块SHA256：caad46a30b33865c46e6ce181eede028de19ce725b4fe1be6bbccd2587b1903b
候选SHA256：c03d4b9937bea047f9a671ff8c4d67826f4825a8c30bdb9e6731f53ebebcd744

### 具体修改

1. 原：To compute the original probability, we now need to remove the conditioning and consider any possible n.
   候选：What we need to do is to now to compute the original probability, is to decondition and make the computation for any possible n.
   理由：恢复What we need to do is to now to ... is to的不顺结构，以及decondition、make the computation。
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 13–15, absolute 3185.78–3222.08s
2. 原：We want to compute the probability that B and C collide without conditioning on any event.
   候选：So, what we want to now do is to compute in general the probability that B and C collide without conditioning to any event.
   理由：恢复So、what we want to now do、in general和conditioning to，不换介词。
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 14–16, absolute 3197.04–3233.26s；Unprompted Whisper medium.en raw: chunk-019, segments 1–1, absolute 3225.00–3239.24s
3. 原：We need to consider all possible integer values from zero to CW_min.
   候选：So that is, we need to consider all possible values of integer from zero to CW_min.
   理由：恢复So that is及values of integer的原词序。
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 16–17, absolute 3222.08–3249.94s；Unprompted Whisper medium.en raw: chunk-019, segments 1–1, absolute 3225.00–3239.24s
4. 原：For any n, the collision probability involves the probability that C draws n if B has also drawn n.
   候选：And for any n, we know that the probability of collision is what? The probability that C draws n if also B has drawn n, right?
   理由：撤销解释性involves，恢复And、we know that、is what问答及if also B has drawn n。
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 17–18, absolute 3233.26–3254.22s；Unprompted Whisper medium.en raw: chunk-019, segments 2–3, absolute 3242.04–3264.66s

### 逐单元证据

1. What we need to do is to now to compute the original probability, is to decondition and make the computation for any possible n.
我们需要做的是现在去计算原来的概率，是去掉条件，并对任何可能的 n 进行计算。
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 13–15, absolute 3185.78–3222.08s
2. So, what we want to now do is to compute in general the probability that B and C collide without conditioning to any event.
所以，我们现在想做的是一般地计算 B 和 C 碰撞的概率，不以任何事件为条件。
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 14–16, absolute 3197.04–3233.26s；Unprompted Whisper medium.en raw: chunk-019, segments 1–1, absolute 3225.00–3239.24s
3. So that is, we need to consider all possible values of integer from zero to CW_min.
所以，也就是说，我们需要考虑从零到 CW_min 的所有可能的整数的值。
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 16–17, absolute 3222.08–3249.94s；Unprompted Whisper medium.en raw: chunk-019, segments 1–1, absolute 3225.00–3239.24s
4. And for any n, we know that the probability of collision is what?
而对于任何 n，我们知道碰撞的概率是什么？
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 17–18, absolute 3233.26–3254.22s；Unprompted Whisper medium.en raw: chunk-019, segments 2–3, absolute 3242.04–3264.66s
5. The probability that C draws n if also B has drawn n, right?
如果 B 也已经抽到了 n，C 抽到 n 的概率，对吧？
   来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 17–18, absolute 3233.26–3254.22s；Unprompted Whisper medium.en raw: chunk-019, segments 2–3, absolute 3242.04–3264.66s

## 46 · 00:54:22 · B选中n的概率与碰撞条件

稳定块ID：doxcnflxhsrZ0Q4lhw4fU7eq5xe
原块SHA256：a0691b5a2649896534aac84e43016e89e47e3cc2c2fca364ae4144159b79dbfb
候选SHA256：e56c03da0a728ca24c9059999edca1b3eed3ecdb353ec62b98f109b94b05c3aa

### 具体修改

1. 原：Let's first write the probability that B draws n. It is again one over (CW_min + 1).
   候选：So, let's first write the probability that B draws n. The probability that B draws n is again this one. So we can write one over CW_min plus one. This is the probability that B draws n.
   理由：恢复So与三次the probability that B draws n，以及this one和so we can write；不以公式替掉口述。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 3–5, absolute 3251.88–3289.40s
2. 原：Given that, a collision happens if C also draws n, and that happens with this probability.
   候选：And then given that, we know that [a / the unclear] collision happens if C also draws n. That happens with this probability.
   理由：恢复And then、we know that及独立重复句；不合并that happens。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 5–7, absolute 3275.64–3312.46s

### 逐单元证据

1. So, let's first write the probability that B draws n.
所以，我们先写出 B 抽到 n 的概率。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 3–5, absolute 3251.88–3289.40s
2. The probability that B draws n is again this one.
B 抽到 n 的概率又是这个。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 3–5, absolute 3251.88–3289.40s
3. So we can write one over CW_min plus one.
所以我们可以写一除以（CW_min 加一）。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 3–5, absolute 3251.88–3289.40s
4. This is the probability that B draws n.
这就是 B 抽到 n 的概率。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 3–5, absolute 3251.88–3289.40s
5. And then given that, we know that [a / the unclear] collision happens if C also draws n.
然后，给定那个，我们知道，如果 C 也抽到 n，就会发生[一次／这次，待听辨]碰撞。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 5–7, absolute 3275.64–3312.46s
   限制：Qwen 29: a collision; medium-019 segment 6: the collision; Feishu truncates after a.
6. That happens with this probability.
那件事以这个概率发生。
   来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 5–7, absolute 3275.64–3312.46s

## 47 · 00:54:59 · 求和化简得到碰撞概率

稳定块ID：doxcnpIXR5BhdcEJODa1iMozspe
原块SHA256：e922b1be5b49fcb49d5df4373881b4c5da7d4246ee5048628f27aee994453974
候选SHA256：41d8fbe471b260cfa8332be7637f9df1ea05f732303beb1c680f9b2990ccb560

### 具体修改

1. 原：We multiply by one over (CW_min + 1), the probability that C draws n.
   候选：So we multiply by again one over CW_min plus one, which is the probability that C [draws / grows unclear] n.
   理由：恢复So、again、which is；draws由上下文和邻句定位，近音grows/goes不作为确定原词。
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 7–8, absolute 3296.96–3331.38s
2. 原：We therefore sum over n from zero to CW_min the term 1/(CW_min + 1)^2.
   候选：So what we have is simply sum over n that goes from zero to CW_min of one over CW_min plus one squared, [right / okay unclear]?
   理由：恢复so what we have is simply、that goes及口述one over，不用数学符号替换句子。
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 7–9, absolute 3296.96–3346.32s
3. 原：This is a constant term inside the sum. How many times do we sum it? CW_min + 1 times.
   候选：Now, this is a constant term, we are inside a sum, so we are summing this constant term how many times? CW_min plus one times, right?
   理由：恢复Now、we are inside a sum、so we are summing this constant term以及times/right，保留重复。
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 9–11, absolute 3333.28–3380.72s
4. 原：This gives (CW_min + 1)/(CW_min + 1)^2. We simplify numerator and denominator and get 1/(CW_min + 1).
   候选：So this is equal to CW_min plus one divided by CW_min plus one squared. We simplify numerator and denominator, and we get one over CW_min plus one.
   理由：恢复So this is equal to、and we get及口述算式，不添加gives解释。
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 11–12, absolute 3357.94–3396.18s

### 逐单元证据

1. So we multiply by again one over CW_min plus one, which is the probability that C [draws / grows unclear] n.
所以我们再乘以一除以（CW_min 加一），也就是 C [抽到／grows，待听辨] n 的概率。
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 7–8, absolute 3296.96–3331.38s
   限制：Medium-019 segment 7: grows n; Qwen 30: goes n; Feishu is multilingual corruption. Draws is contextually expected and repeatedly spoken elsewhere, but the local verb is not confirmed by these outputs.
2. So what we have is simply sum over n that goes from zero to CW_min of one over CW_min plus one squared, [right / okay unclear]?
所以，我们得到的就是对从零到 CW_min 的 n 求和，求一除以（CW_min 加一）的平方的和，[对吧／好吗，待听辨]？
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 7–9, absolute 3296.96–3346.32s
   限制：Qwen 30 has okay after square; Feishu has right; medium has no tag. Numerator/denominator grouping is conceptual context, not added spoken parentheses.
3. Now, this is a constant term, we are inside a sum, so we are summing this constant term how many times?
现在，这是一个常数项，我们在一个求和里面，所以我们把这个常数项加多少次？
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 9–11, absolute 3333.28–3380.72s
4. CW_min plus one times, right?
（CW_min 加一）次，对吧？
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 9–11, absolute 3333.28–3380.72s
5. So this is equal to CW_min plus one divided by CW_min plus one squared.
所以这等于（CW_min 加一）除以（CW_min 加一）的平方。
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 11–12, absolute 3357.94–3396.18s
6. We simplify numerator and denominator, and we get one over CW_min plus one.
我们把分子和分母约简，就得到一除以（CW_min 加一）。
   来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 11–12, absolute 3357.94–3396.18s

## 48 · 00:56:35 · 两节点碰撞概率的最终结论

稳定块ID：doxcnnL1HcoGHeu170WeLRQgmwb
原块SHA256：fd99dc39ee42b4dab913b1782f31a2ffde14a63efd1553aef1bfd33733b79733
候选SHA256：f3aeb51c49086b141bb9ceb80a9faa92d261cb07f02399615361859b5ff311d7

### 具体修改

1. 原：The final result is that the probability that B and C collide in our simple example is one over (the contention window plus one).
   候选：So, the final result of all [this computation / these computations unclear] is that the probability that B and C collide in our simple example that we presented earlier is one over the contention window plus one.
   理由：恢复So、of all this computation及that we presented earlier，单复数来源冲突短标。
   来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 12–14, absolute 3380.72–3419.70s；Unprompted Whisper medium.en raw: chunk-020, segments 1–1, absolute 3405.00–3419.66s
2. 原：If you were able to follow the computation, great.
   候选：Okay, now if you [were / are unclear] able to follow the computation, great.
   理由：恢复Okay、Now；were/are来自重叠medium窗的冲突不隐藏。
   来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 14–15, absolute 3404.72–3434.48s；Unprompted Whisper medium.en raw: chunk-020, segments 1–2, absolute 3405.00–3434.98s
3. 原：It is a simple probability calculation, but if your background is different and you have not seen probability in previous courses, do not worry. The important thing is to retain the final message.
   候选：It's a simple probability computation, but if your background is different, and therefore you have not seen probability anywhere in your previous courses, do not worry. The important thing is that you retain the final message.
   理由：恢复It’s、computation、therefore、anywhere、your和that you retain，不改成更短的概述。
   来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 15–16, absolute 3419.70–3434.78s；Unprompted Whisper medium.en raw: chunk-020, segments 2–4, absolute 3419.66–3451.44s

### 逐单元证据

1. So, the final result of all [this computation / these computations unclear] is that the probability that B and C collide in our simple example that we presented earlier is one over the contention window plus one.
所以，所有[这个计算／这些计算，待听辨]的最终结果是，B 和 C 在我们前面展示的这个简单例子里碰撞的概率是一除以（竞争窗口加一）。
   来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 12–14, absolute 3380.72–3419.70s；Unprompted Whisper medium.en raw: chunk-020, segments 1–1, absolute 3405.00–3419.66s
   限制：Qwen 30: all this computation; medium-019 segment 12: all these computations. Feishu beginning is corrupted. Restore the full sentence starting before the approximate 00:56:35 anchor without duplicating it in section 47.
2. Okay, now if you [were / are unclear] able to follow the computation, great.
好，现在，如果你们[之前能够／能够，时态待听辨]跟上这个计算，那很好。
   来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 14–15, absolute 3404.72–3434.48s；Unprompted Whisper medium.en raw: chunk-020, segments 1–2, absolute 3405.00–3434.98s
   限制：Qwen 30/31 and medium-019 say were; overlapping medium-020 says are. Feishu garbles were able as were Evil. Majority support favors were, but the tense conflict remains visible.
3. It's a simple probability computation, but if your background is different, and therefore you have not seen probability anywhere in your previous courses, do not worry.
这是一个简单的概率计算，但是如果你们的背景不同，因此在你们之前的课程里的任何地方都没有见过概率，不要担心。
   来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 15–16, absolute 3419.70–3434.78s；Unprompted Whisper medium.en raw: chunk-020, segments 2–4, absolute 3419.66–3451.44s
4. The important thing is that you retain the final message.
重要的事情是你们记住最后的信息。
   来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 15–16, absolute 3419.70–3434.78s；Unprompted Whisper medium.en raw: chunk-020, segments 2–4, absolute 3419.66–3451.44s

## 49 · 00:57:27 · 竞争窗口越大碰撞概率越低

稳定块ID：doxcnJ5JJMQGLQYI4WCncznRwTb
原块SHA256：186542fe5b9325bceb0f22cde6f3e394d65ae518c60d45eae241c16ee6a7eea5
候选SHA256：ef492408dee70406bea5c52b588bc5af5830abd66e10c894604e6e2e81af74e1

### 具体修改

1. 原：In our simple example, the probability that B and C collide while performing backoff equals this ratio, which decreases as the contention window minimum increases.
   候选：The final message is, in our simple example, right, that we are considering, the probability that B and C [collide / collided unclear] while performing the backoff procedure is equal to this ratio, that clearly will decrease as the value of contention window minimum increases, right?
   理由：恢复The final message is、right、that we are considering、procedure、that clearly will以及value of，不压缩未来式。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-020, segments 4–7, absolute 3444.44–3482.36s
2. 原：The larger the contention window, the lower the ratio and therefore the lower the collision probability. This is something everybody can understand.
   候选：The larger the contention window, the lower this ratio, so the lower the collision probability. This is, I think, something that everybody [can understand / understands unclear].
   理由：恢复this ratio、so和I think，can understand/understands来源不一致短标。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-020, segments 7–9, absolute 3471.76–3501.42s
3. 原：This refers to the simple example, but it expresses a general rule: collision probability in backoff decreases as the contention window increases.
   候选：Okay, now, so this means that, okay, this refers, as I said, to the previous simple example, but it's a general rule. The collision probability in the backoff procedure decreases as the value of contention window increases.
   理由：恢复Okay now so this means that okay、as I said、previous及完整第二次rule说明，不重写expresses。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 9–12, absolute 3490.16–3532.90s
4. 原：What does this tell you? Why am I making this second observation?
   候选：So now, what does this tell you? Why am I marking this, [and making / I'm making unclear] this second observation?
   理由：恢复So now及被删的marking this；连接and/I’m来源冲突短标，保留口头自我重启可能。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 12–13, absolute 3518.78–3539.58s
5. 原：We wanted to understand why in Wi-Fi, every time we perform backoff for a given data packet, we roughly double the contention window. We increase it significantly every time. Why? To reduce the probability of collision among contending nodes.
   候选：Because remember, we wanted to understand the reason why in Wi-Fi we say every time we perform the backoff procedure for a given data packet, we roughly speaking double the contention window. So we increase it very significantly every time. Why do we do that? To reduce the probability of collision among [contending / contend unclear] nodes.
   理由：恢复Because remember、the reason why、we say、procedure、roughly speaking、very及完整问句。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 13–18, absolute 3532.90–3583.12s

### 逐单元证据

1. The final message is, in our simple example, right, that we are considering, the probability that B and C [collide / collided unclear] while performing the backoff procedure is equal to this ratio, that clearly will decrease as the value of contention window minimum increases, right?
最后的信息是，在我们这个简单的例子里，对吧，在我们正在考虑的这个例子里，B 和 C 在执行退避过程时[碰撞／发生了碰撞，时态待听辨]的概率等于这个比值，而这个比值显然会随着最小竞争窗口的值增加而减小，对吧？
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-020, segments 4–7, absolute 3444.44–3482.36s
   限制：Qwen 31 and medium-020 use collide; Feishu uses collided. The future will decrease and clearly are restored from Feishu/Qwen/medium.
2. The larger the contention window, the lower this ratio, so the lower the collision probability.
竞争窗口越大，这个比值越低，所以碰撞概率越低。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-020, segments 7–9, absolute 3471.76–3501.42s
3. This is, I think, something that everybody [can understand / understands unclear].
我觉得，这是每个人都[能够理解／理解，待听辨]的事情。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-020, segments 7–9, absolute 3471.76–3501.42s
   限制：Feishu: I think, ... can understand; Qwen 31: I think, ... understands; medium: can understand, omitting I think. Preserve the qualifier, flag the verb difference.
4. Okay, now, so this means that, okay, this refers, as I said, to the previous simple example, but it's a general rule.
好，现在，所以这意味着，好，正如我说的，这是指前面那个简单的例子，但它是一条一般规律。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 9–12, absolute 3490.16–3532.90s
5. The collision probability in the backoff procedure decreases as the value of contention window increases.
退避过程中的碰撞概率随着竞争窗口的值增加而降低。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 9–12, absolute 3490.16–3532.90s
6. So now, what does this tell you?
那么现在，这告诉你们什么？
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 12–13, absolute 3518.78–3539.58s
7. Why am I marking this, [and making / I'm making unclear] this second observation?
我为什么要标出这一点，[并作出／我在作出，待听辨]这第二个观察？
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 12–13, absolute 3518.78–3539.58s
   限制：Medium-020 segments 12–13: Why am I marking this and making this second observation; Qwen 32: Why am I marking these? I'm making this second observation. Feishu supplied fragments omit this sentence.
8. Because remember, we wanted to understand the reason why in Wi-Fi we say every time we perform the backoff procedure for a given data packet, we roughly speaking double the contention window.
因为记住，我们想理解为什么在 Wi-Fi 中我们说，每次为一个给定的数据包执行退避过程时，我们大致来说把竞争窗口扩大一倍。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 13–18, absolute 3532.90–3583.12s
9. So we increase it very significantly every time.
所以我们每次都非常显著地增加它。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 13–18, absolute 3532.90–3583.12s
10. Why do we do that?
我们为什么这样做？
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 13–18, absolute 3532.90–3583.12s
11. To reduce the probability of collision among [contending / contend unclear] nodes.
为了降低[正在竞争的／contend，词尾待听辨]节点之间的碰撞概率。
   来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 13–18, absolute 3532.90–3583.12s
   限制：Qwen 32: contend nodes; medium-020 segment 17: contented nodes; Feishu truncates at To reduce. Contending is technically plausible, but the local participle ending is not established.

## 50 · 00:59:34 · 重复失败时扩大可选整数范围

稳定块ID：doxcnUwQc9ePMHTxq4Ra0PKvQIf
原块SHA256：5b8c7073c1ccf4ae794d8693fb53f552c1311bec43ac13feef0f1a465a7e7809
候选SHA256：ff02759ccf1d3b7e05394d63fbf57604a7298155f1ff2987c1871dddbbbee994

### 具体修改

1. 原：Backoff is a probabilistic mechanism. Wi-Fi essentially assumes that a transmitter is failing, failing, failing because too many nodes are trying to access the channel. The situation is too crowded.
   候选：[Okay unclear], so, backoff is a probabilistic mechanism, and essentially Wi-Fi assumes that the reason why a transmitter is failing, failing, failing is because there are too many nodes in the network that try to access the channel to transmit a packet. The situation is too crowded.
   理由：恢复So、and essentially、the reason why、in the network、to transmit a packet，保留failing三连。
   来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 17–21, absolute 3564.66–3604.92s；Unprompted Whisper medium.en raw: chunk-021, segments 1–3, absolute 3585.00–3605.86s
2. 原：It assumes that when you fail, fail, fail, other nodes are trying too; you select the same backoff time and keep colliding.
   候选：So what Wi-Fi says is, if you fail, [fail, fail unclear], every time you fail means that there are other nodes trying, and you are selecting the same backoff, you have the same backoff time, and you keep colliding.
   理由：恢复what Wi-Fi says is、every time you fail means及same backoff / same backoff time重述；fail重复有Qwen/Feishu支持保留并说明medium省略。
   来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 21–23, absolute 3597.84–3614.84s；Unprompted Whisper medium.en raw: chunk-021, segments 3–5, absolute 3598.64–3621.94s
3. 原：To reduce the collision probability, each node needs to enlarge the range of possible integer values from which it can choose.
   候选：So in order to reduce the probability of collision, each node needs to enlarge the possible values, so the choice, right, among the integers that can be selected.
   理由：恢复So in order to、the possible values及so the choice right among the integers that can be selected，不补range of。
   来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 6–7, absolute 3623.24–3643.32s

### 逐单元证据

1. [Okay unclear], so, backoff is a probabilistic mechanism, and essentially Wi-Fi assumes that the reason why a transmitter is failing, failing, failing is because there are too many nodes in the network that try to access the channel to transmit a packet.
[好，待听辨]，所以，退避是一种概率性机制，而基本上 Wi-Fi 假定，一个发送方失败、失败、失败的原因，是网络中有太多节点尝试接入信道来发送一个数据包。
   来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 17–21, absolute 3564.66–3604.92s；Unprompted Whisper medium.en raw: chunk-021, segments 1–3, absolute 3585.00–3605.86s
   限制：Qwen 32 has Okay before So backoff; Feishu and medium omit that filler. Three failing repetitions are directly supported by Qwen and both medium windows.
2. The situation is too crowded.
这个情况太拥挤了。
   来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 17–21, absolute 3564.66–3604.92s；Unprompted Whisper medium.en raw: chunk-021, segments 1–3, absolute 3585.00–3605.86s
3. So what Wi-Fi says is, if you fail, [fail, fail unclear], every time you fail means that there are other nodes trying, and you are selecting the same backoff, you have the same backoff time, and you keep colliding.
所以 Wi-Fi 说的是，如果你失败，[失败、失败，重复待听辨]，你每一次失败都意味着还有其他节点在尝试，而你们选择了相同的退避，你们有相同的退避时间，而且你们持续碰撞。
   来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 21–23, absolute 3597.84–3614.84s；Unprompted Whisper medium.en raw: chunk-021, segments 3–5, absolute 3598.64–3621.94s
   限制：Qwen 32 explicitly repeats fail three times; Feishu has a fragmented FL feel. Fe. sequence. Both overlapping medium windows give a single fail before every time you fail. Repetition is plausible and retained as unconfirmed, not silently deleted.
4. So in order to reduce the probability of collision, each node needs to enlarge the possible values, so the choice, right, among the integers that can be selected.
所以，为了降低碰撞的概率，每个节点都需要扩大可能的值，所以是选择，对吧，在那些可以被选中的整数之间。
   来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 6–7, absolute 3623.24–3643.32s

## 51 · 01:00:35 · 扩大窗口的好处与信道差错下的代价

稳定块ID：doxcneECTaGLIYZElqo3ZcJjZPe
原块SHA256：5172a0e1ba6be6eeeaa2f0aa71f3a0f107f5d5116bbbc95e2e0dd1c0c979ef30
候选SHA256：fcaf81be692cde4c8bb1f49377602c8beb9739d97320bfb4e5677d847ee36d8c

### 具体修改

1. 原：It's like a bag of candies. If they are all strawberry flavored, two people picking candies will clearly both pick strawberry. If you fill the bag with banana, strawberry, peach, mint, and so on, the probability that two people pick the same flavor decreases. It's the same principle.
   候选：It's like when you have a bag with candies, if they are all strawberry flavored, if there are two people picking the candy, clearly they will pick strawberry. But if instead you fill the bag with banana, strawberry, peach, mint, and so on, then the probability that two people pick the same candy flavor will reduce. So this is exactly the same [principle / thing unclear].
   理由：恢复when you have、if there are two people、the candy、But if instead、then、same candy flavor will reduce及exactly；保留两层if，不压缩为比喻摘要。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 7–12, absolute 3633.44–3677.48s
2. 原：You may say: nice, Wi-Fi deals with a crowded situation and lets us perform better. True, doubling the contention window works if the reason for failure is repeated collisions.
   候选：Okay, so you may say, well, nice, Wi-Fi really takes care of this crowded situation and allow us to perform better. True, but this is, this works, this is a good idea to double the contention window every time you perform a backoff to transmit [a / the unclear] packet. It works, but it works if the reason why a transmitter is failing is indeed because it [it unclear] keeps colliding with others.
   理由：恢复Okay so、well、really takes care、allow us及this is this works、每次退避发送数据包、it works but it works的重复。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 12–17, absolute 3669.88–3718.78s
3. 原：But remember that in wireless a transmission may also fail because of channel errors. You may be the only node with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate correctly.
   候选：But remember, in wireless, a transmission may fail also because of channel errors. So you may be the only one in the network with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate the signal correctly.
   理由：恢复But remember in wireless、fail also、So、only one in the network及the signal，保留原词序。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 17–20, absolute 3710.16–3741.90s
4. 原：You still have to follow the protocol rules. If you fail repeatedly because of channel errors, these rules mean that every time you have to enlarge the contention window. Statistically, it becomes more likely that you draw a longer and longer and longer backoff time.
   候选：Okay, so in that case, of course, you have to follow the protocol rules anyway. Okay, so if you fail and fail because of channel errors, you have to apply the rules. And this means that every time you have to enlarge the contention window, and statistically it's more likely that you will draw a long and longer and longer backoff time, right?
   理由：恢复Okay so in that case of course、anyway、fail and fail、you have to apply the rules、and this means that、will draw a long and longer and longer，不将原话均改longer。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 20–24, absolute 3733.92–3777.88s；Unprompted Whisper medium.en raw: chunk-022, segments 1–1, absolute 3765.68–3774.42s
5. 原：Is this good in this case? Not really. You are not failing because you collide with other nodes; the reason is poor channel quality. This mechanism does not solve that issue.
   候选：So is this good in this case? [Hmm unclear], not really good, right? Because the reason why you are failing is not because there are others and you are colliding, that's not the reason. The reason is that the channel is poor, of poor quality, and this mechanism does not help to solve the issue, right?
   理由：恢复So、not really good right、because the reason why、that’s not the reason、poor of poor quality和does not help to solve；嗯仅Feishu支持短标。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 24–27, absolute 3768.54–3793.32s；Unprompted Whisper medium.en raw: chunk-022, segments 1–4, absolute 3765.68–3800.62s
6. 原：In this situation it is even harmful, because it delays channel access. It makes you wait longer and longer and longer before you can access the channel and transmit, even though the problem is poor channel quality, not collision. It just increases channel access delay and does not help with that problem.
   候选：Actually, this [method / mechanism unclear] in this situation is even harmful. Why? Because it makes you delay channel access, right? It makes you wait longer and longer and longer before accessing the channel, being able to access the channel and transmit the packet. With no reason, because the problem is not collision, the problem is poor channel quality. So it just increases the channel access delay. It doesn't help with anything.
   理由：恢复Actually、this method、独立Why问句、makes you delay、重复before accessing / being able to access、with no reason及doesn’t help with anything；保留三次longer。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s

### 逐单元证据

1. It's like when you have a bag with candies, if they are all strawberry flavored, if there are two people picking the candy, clearly they will pick strawberry.
这就像当你有一个装着糖果的袋子，如果它们全是草莓味的，如果有两个人在拿糖果，显然他们会拿到草莓味的。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 7–12, absolute 3633.44–3677.48s
2. But if instead you fill the bag with banana, strawberry, peach, mint, and so on, then the probability that two people pick the same candy flavor will reduce.
但是，如果你改为在袋子里装上香蕉味、草莓味、桃子味、薄荷味等等，那么两个人拿到相同糖果口味的概率会降低。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 7–12, absolute 3633.44–3677.48s
3. So this is exactly the same [principle / thing unclear].
所以这完全是相同的[原理／事情，待听辨]。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 7–12, absolute 3633.44–3677.48s
   限制：Feishu and medium-021 segment 11: principle; Qwen 33: thing. Both alternatives retained rather than silently following the more natural one.
4. Okay, so you may say, well, nice, Wi-Fi really takes care of this crowded situation and allow us to perform better.
好，所以你可能会说，嗯，很好，Wi-Fi 确实照顾到了这个拥挤的情况，而且让我们表现得更好。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 12–17, absolute 3669.88–3718.78s
5. True, but this is, this works, this is a good idea to double the contention window every time you perform a backoff to transmit [a / the unclear] packet.
是的，但是这是，这有效，这是个好主意，每次你为了发送[一个／这个，待听辨]数据包而执行退避时，就把竞争窗口扩大一倍。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 12–17, absolute 3669.88–3718.78s
   限制：Feishu/Qwen both retain this is, this works; medium drops the first this is. Qwen 33: a packet; medium-021 segment 15: the packet; Feishu phrase is corrupted. Do not reduce the false start to True, doubling ... works.
6. It works, but it works if the reason why a transmitter is failing is indeed because it [it unclear] keeps colliding with others.
它有效，但它有效的条件是，发送方失败的原因确实是它[它，重复待听辨]持续与其他节点碰撞。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 12–17, absolute 3669.88–3718.78s
   限制：All sources retain it works, but it works. Qwen 33 alone repeats it it before keeps; Feishu/medium have it once. The extra it remains marked rather than declared confirmed.
7. But remember, in wireless, a transmission may fail also because of channel errors.
但是记住，在无线通信中，一次传输也可能因为信道差错而失败。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 17–20, absolute 3710.16–3741.90s
8. So you may be the only one in the network with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate the signal correctly.
所以，你可能是网络中唯一有一个数据包要发送的那个，但仍然失败，因为信道不好，而接收方无法正确地解调信号。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 17–20, absolute 3710.16–3741.90s
9. Okay, so in that case, of course, you have to follow the protocol rules anyway.
好，所以在那种情况下，当然，你无论如何都必须遵守协议规则。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 20–24, absolute 3733.92–3777.88s；Unprompted Whisper medium.en raw: chunk-022, segments 1–1, absolute 3765.68–3774.42s
10. Okay, so if you fail and fail because of channel errors, you have to apply the rules.
好，所以如果你因为信道差错而失败，又失败，你必须应用这些规则。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 20–24, absolute 3733.92–3777.88s；Unprompted Whisper medium.en raw: chunk-022, segments 1–1, absolute 3765.68–3774.42s
11. And this means that every time you have to enlarge the contention window, and statistically it's more likely that you will draw a long and longer and longer backoff time, right?
而这意味着，你每次都必须扩大竞争窗口，而从统计上说，你更有可能会抽到一个长的、又更长、又更长的退避时间，对吧？
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 20–24, absolute 3733.92–3777.88s；Unprompted Whisper medium.en raw: chunk-022, segments 1–1, absolute 3765.68–3774.42s
12. So is this good in this case?
所以，这在这种情况下好吗？
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 24–27, absolute 3768.54–3793.32s；Unprompted Whisper medium.en raw: chunk-022, segments 1–4, absolute 3765.68–3800.62s
13. [Hmm unclear], not really good, right?
[嗯，待听辨]，不太好，对吧？
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 24–27, absolute 3768.54–3793.32s；Unprompted Whisper medium.en raw: chunk-022, segments 1–4, absolute 3765.68–3800.62s
   限制：Feishu includes Hmm; Qwen 34 and both medium windows omit it. The content not really good, right is supported across sources.
14. Because the reason why you are failing is not because there are others and you are colliding, that's not the reason.
因为你失败的原因不是因为有其他节点而你正在碰撞，那不是原因。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 24–27, absolute 3768.54–3793.32s；Unprompted Whisper medium.en raw: chunk-022, segments 1–4, absolute 3765.68–3800.62s
15. The reason is that the channel is poor, of poor quality, and this mechanism does not help to solve the issue, right?
原因是信道差，质量差，而这种机制没有帮助解决这个问题，对吧？
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 24–27, absolute 3768.54–3793.32s；Unprompted Whisper medium.en raw: chunk-022, segments 1–4, absolute 3765.68–3800.62s
16. Actually, this [method / mechanism unclear] in this situation is even harmful.
实际上，这个[方法／机制，待听辨]在这种情况下甚至是有害的。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s
   限制：Feishu and medium-022 segment 4: method; Qwen 34: mechanism. Both are plausible local lexical alternatives, so do not silently substitute one.
17. Why?
为什么？
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s
18. Because it makes you delay channel access, right?
因为它让你延迟信道接入，对吧？
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s
19. It makes you wait longer and longer and longer before accessing the channel, being able to access the channel and transmit the packet.
它让你等得更久、又更久、又更久，然后才能接入信道，能够接入信道并发送数据包。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s
20. With no reason, because the problem is not collision, the problem is poor channel quality.
没有理由，因为问题不是碰撞，问题是信道质量差。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s
21. So it just increases the channel access delay.
所以，它只是增加了信道接入时延。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s
22. It doesn't help with anything.
它对任何事情都没有帮助。
   来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s

## 52 · 01:04:00 · 批判性评估技术方案的适用条件

稳定块ID：doxcn7v1pOcJSqW4rkKPR4G6heb
原块SHA256：2b0e6b11f38cbef6984befee8d3d2b25c9b7ab46261307e26f47aa86c386652e
候选SHA256：374ee56476e968ba47d2754a0dfe5ad88eabb266079e10dde447c71dd018d2de

### 具体修改

1. 原：We need to understand why mechanisms are designed in a certain way, but also look at them critically.
   候选：Okay, so we need to be aware that, well, we need to understand why certain techniques, mechanisms are designed in a certain way. But we need also always to look at these mechanisms or techniques or solutions with a critical eye.
   理由：恢复Okay so we need to be aware that well的自我转折、techniques mechanisms、also always、mechanisms or techniques or solutions与with a critical eye，不合并。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 8–11, absolute 3830.38–3868.20s
2. 原：Is a solution good under all conditions and in every situation?
   候选：That means we need to look at them and ask ourselves, is this really good in under all conditions, under all situations, or not?
   理由：恢复That means we need to look at them and ask ourselves、really、in under、两次under all及or not，保留不顺。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 11–13, absolute 3859.44–3885.44s
3. 原：Some aspects of a technology may not always be good, and we need to be aware of that.
   候选：There may be aspects of technology that are not that good, not always, and we need to be aware of that.
   理由：恢复There may be、not that good、not always的语序和停顿。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 13–14, absolute 3876.96–3891.44s
4. 原：When designing a technological solution, we need to account for possible issues.
   候选：Okay, so whenever we design a system, whenever we design a technological solution, we need to account for possible issues that may arise.
   理由：恢复Okay so、whenever we design a system / whenever we design的重复自我重启及that may arise。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 14–16, absolute 3885.44–3911.72s
5. 原：An idea may solve one problem but make things worse in other situations. We need to look at the big picture when designing a technology, and this is an example.
   候选：So an idea may be good to solve one problem, but it might actually make things worse in other situations. So we need also to look at the big picture when we design a technology. [Okay unclear], and [and unclear] this is indeed an example of [of unclear] that.
   理由：恢复So an idea may be good to solve、might actually、So we need also to、when we design、indeed及Qwen单源and/of重复疑点。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 16–18, absolute 3902.68–3930.28s

### 逐单元证据

1. Okay, so we need to be aware that, well, we need to understand why certain techniques, mechanisms are designed in a certain way.
好，所以我们需要意识到，嗯，我们需要理解为什么某些技术、机制以某种方式来设计。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 8–11, absolute 3830.38–3868.20s
2. But we need also always to look at these mechanisms or techniques or solutions with a critical eye.
但是我们也需要总是以批判的眼光来看这些机制，或者技术，或者解决方案。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 8–11, absolute 3830.38–3868.20s
3. That means we need to look at them and ask ourselves, is this really good in under all conditions, under all situations, or not?
那意味着我们需要看着它们并问自己，这真的在，在所有条件下，在所有情况下都好吗，还是不是呢？
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 11–13, absolute 3859.44–3885.44s
4. There may be aspects of technology that are not that good, not always, and we need to be aware of that.
技术的某些方面可能不是那么好，不是总是好，而我们需要意识到这一点。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 13–14, absolute 3876.96–3891.44s
5. Okay, so whenever we design a system, whenever we design a technological solution, we need to account for possible issues that may arise.
好，所以每当我们设计一个系统，每当我们设计一个技术解决方案时，我们需要考虑可能出现的那些问题。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 14–16, absolute 3885.44–3911.72s
6. So an idea may be good to solve one problem, but it might actually make things worse in other situations.
所以，一个想法可能对解决一个问题很好，但它实际上可能会让其他情况下的事情变得更糟。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 16–18, absolute 3902.68–3930.28s
7. So we need also to look at the big picture when we design a technology.
所以我们在设计一项技术时，也需要看整体情况。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 16–18, absolute 3902.68–3930.28s
8. [Okay unclear], and [and unclear] this is indeed an example of [of unclear] that.
[好，待听辨]，而且[而且，重复待听辨]，这的确就是那个的[的，重复待听辨]一个例子。
   来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 16–18, absolute 3902.68–3930.28s
   限制：Qwen 35: Okay, and and this is indeed an example of of that; medium-022 segment 18: and this is indeed an example of that; supplied Feishu fragment ends before this continuation. Single-source repetitions are retained with short uncertainty markers.

## 53 · 01:05:29 · 广播和多播不期待确认

稳定块ID：doxcn6EVnNwTDOuu398ghwuxGRc
原块SHA256：a9becde292f30ace5bd53b2d7ac231bb07e751591bdbb674c8643967f072f9b9
候选SHA256：4d8963a91da17901a41be6fecebbb3fc3f249aa3f404350e6d48acd53a11c08b

### 具体修改

1. 原：The last thing I want to comment on before moving to the third situation is that we are considering unicast data packets.
   候选：[Um unclear], the last thing that I would like to comment, and then we go to the third situation, is remember that we are considering how to transmit unicast data packets, right? We said that.
   理由：恢复would like、comment and then we go、is remember、how to transmit、right、We said that；不把句法改成before moving。
   来源：Feishu historical snapshot: source_index=65, id=135, section anchor 01:05:29；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 18–21, absolute 3917.84–3957.58s；Unprompted Whisper medium.en raw: chunk-023, segments 1–1, absolute 3945.00–3957.64s
2. 原：Let me mention again that multicast and broadcast data packets are much simpler, because we do not expect acknowledgments.
   候选：Let me just mention again that in the case of multicast or broadcast data packet, things are much, much simpler, because we do not expect any acknowledgement.
   理由：恢复just、in the case of、or、data packet单数、things are much much、any acknowledgement单数。
   来源：Feishu historical snapshot: source_index=65, id=135, section anchor 01:05:29；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-022, segments 21–23, absolute 3945.56–3971.28s；Unprompted Whisper medium.en raw: chunk-023, segments 1–2, absolute 3945.00–3966.04s

### 逐单元证据

1. [Um unclear], the last thing that I would like to comment, and then we go to the third situation, is remember that we are considering how to transmit unicast data packets, right?
[嗯，待听辨]，我最后想评论的事情，然后我们就去第三种情况，是记住我们正在考虑如何发送单播数据包，对吧？
   来源：Feishu historical snapshot: source_index=65, id=135, section anchor 01:05:29；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 18–21, absolute 3917.84–3957.58s；Unprompted Whisper medium.en raw: chunk-023, segments 1–1, absolute 3945.00–3957.64s
   限制：Qwen 35 alone has Um; Feishu and medium omit the filler. Feishu/Qwen retain right and We said that, which medium omits.
2. We said that.
我们说过那个。
   来源：Feishu historical snapshot: source_index=65, id=135, section anchor 01:05:29；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 18–21, absolute 3917.84–3957.58s；Unprompted Whisper medium.en raw: chunk-023, segments 1–1, absolute 3945.00–3957.64s
3. Let me just mention again that in the case of multicast or broadcast data packet, things are much, much simpler, because we do not expect any acknowledgement.
让我再提一下，在多播或广播数据包的情况下，事情要简单得多、得多，因为我们不期待任何确认。
   来源：Feishu historical snapshot: source_index=65, id=135, section anchor 01:05:29；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-022, segments 21–23, absolute 3945.56–3971.28s；Unprompted Whisper medium.en raw: chunk-023, segments 1–2, absolute 3945.00–3966.04s

## 54 · 01:06:05 · 多个接收方同时ACK会碰撞

稳定块ID：doxcnVDHtpDHmdLfVNMU7A5Z1nh
原块SHA256：e199c4096069e9c087ff4aa7563f5cdc1c50adc779864a0729d335bd3eff716d
候选SHA256：7ef755517c709da43b2f0511b428243097a222a1f822b269b5cf779da0fba2b6

### 具体修改

1. 原：Since broadcast and multicast packets are intended for multiple destinations, we cannot have all the receivers sending acknowledgments back. If all those acknowledgments were sent at the same time, they would collide with one another. So that would be no use.
   候选：Indeed, since broadcast and multicast packets are intended for multiple destinations, we cannot have receivers sending back acknowledgments, because all these acknowledgments, if sent at the same time, will collide [with / within unclear] each other. So no use.
   理由：恢复Indeed、receivers无all、sending back、because all these acknowledgments if sent、will collide with each other及So no use，不将will改would。
   来源：Feishu historical snapshot: source_index=66, id=137, section anchor 01:06:05；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-022, segments 23–24, absolute 3963.26–3974.96s；Unprompted Whisper medium.en raw: chunk-023, segments 2–6, absolute 3957.64–3997.68s

### 逐单元证据

1. Indeed, since broadcast and multicast packets are intended for multiple destinations, we cannot have receivers sending back acknowledgments, because all these acknowledgments, if sent at the same time, will collide [with / within unclear] each other.
确实，因为广播和多播数据包面向多个目的地，我们不能让接收方发回确认，因为所有这些确认，如果同时发送，会相互[with／within，介词待听辨]碰撞。
   来源：Feishu historical snapshot: source_index=66, id=137, section anchor 01:06:05；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-022, segments 23–24, absolute 3963.26–3974.96s；Unprompted Whisper medium.en raw: chunk-023, segments 2–6, absolute 3957.64–3997.68s
   限制：Feishu and Qwen 36: with each other; medium-023 segment 5: within each other. All use will; old draft's were/would is an unsupported tense rewrite.
2. So no use.
所以没用。
   来源：Feishu historical snapshot: source_index=66, id=137, section anchor 01:06:05；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-022, segments 23–24, absolute 3963.26–3974.96s；Unprompted Whisper medium.en raw: chunk-023, segments 2–6, absolute 3957.64–3997.68s

## 55 · 01:06:45 · 广播多播一次发送与发送后退避引入

稳定块ID：doxcna5EZSQva8EAx8UH3RzbFKh
原块SHA256：f7a74d5136a0f91b139ea49d68bc34854eb1fd635ef7560a0b173b093c4b1d2f
候选SHA256：a106c831c911524b19423d1b6ec4833768b20db4ec75999f4d9cf32944c3f4e8

### 具体修改

1. 原：If you had to desynchronize the acknowledgment transmissions, that would be very, very complicated and would increase the protocol overhead. So that is not good.
   候选：If you had to desynchronize the acknowledgments transmissions, that would be very, very complicated. And [it / you unclear] would increase the overhead of the protocol. So that's [not good / done unclear].
   理由：恢复acknowledgments transmissions、独立and ... increase及the overhead of the protocol；it/you和not good/done有冲突短标，不强行规范复数。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–7, absolute 3997.68–4007.12s
2. 原：So the choice they made was: if a packet is broadcast or multicast, the transmitter of course needs to sense the channel. If it is idle, transmit. If it is busy, you have to perform backoff because you have to wait.
   候选：So the choice that they made was, well, if a packet is broadcast or multicast, the transmitter of course needs to sense the channel. If the channel is idle, transmit. If the channel is busy, of course, you have to perform the backoff procedure because you have to wait.
   理由：恢复that they made、well、两次the channel、of course、the backoff procedure。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–10, absolute 3997.68–4039.06s
3. 原：But once you access the channel and transmit, that's it; you are done. You don't care whether the packet was received successfully or unsuccessfully.
   候选：But then once you access the channel and transmit, that's it. Okay, you are done, because you don't care if the packet was received successfully or unsuccessfully. [You / we unclear] are done.
   理由：恢复then、Okay、because、if和重复You are done；you/we冲突标出。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 10–12, absolute 4030.16–4058.40s
4. 原：Broadcast and multicast packets are transmitted only once. You may need to run backoff for those data packets, but only if, when you want to access the channel, you sense the channel as busy the first time.
   候选：Okay, so broadcast and multicast packets are transmitted only once. So you may need to run the backoff procedure for those data packets, but just if, when you want to access the channel, you sense the channel as busy the first time, okay?
   理由：恢复Okay so、So you may need、the backoff procedure、but just if及句尾okay，不以only if润色。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 12–15, absolute 4049.74–4083.40s
5. 原：Once you perform backoff, access the channel, and transmit, you are done. If everything is clear so far, let me know if you have questions. No questions? Okay, then we can tackle the last condition.
   候选：Then once you perform the backoff and you access the channel and transmit, you are done. Okay, [um unclear], if everything is clear so far, let me know if you have questions. No questions? Okay, so if we are good, then we can now tackle this last condition.
   理由：恢复Then once、the backoff、and you、Okay、so if we are good、now、this last condition。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 15–18, absolute 4075.84–4117.66s
6. 原：We have one more situation in which we perform backoff. In this third situation the procedure is slightly, slightly different. It is essentially the same except for one thing.
   候选：That is, well, we have one more situation under which we perform the backoff. In this third situation, actually, the procedure is slightly, slightly different, okay? [It is / is, is unclear] essentially the same except for one [thing unclear]. What is this third situation?
   理由：恢复That is well、under which、the backoff、actually、Okay；保留slightly重复与one/one thing疑点、补回被删问句。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 18–21, absolute 4105.50–4143.94s；Unprompted Whisper medium.en raw: chunk-024, segments 1–2, absolute 4125.00–4138.36s
7. 原：In this case the procedure is called post-backoff, to underline that there is a small difference from backoff run in the previous two situations.
   候选：[And it is called unclear], in this case the procedure is called [fast / post unclear] backoff, just to underline that there is a small difference with respect to the backoff run under the previous two situations.
   理由：恢复And it is called的重启、just、with respect to、under；此处各ASR为fast backoff，不能仅据知识确写post-backoff。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 21–22, absolute 4137.62–4154.62s；Unprompted Whisper medium.en raw: chunk-024, segments 3–4, absolute 4138.62–4157.50s

### 逐单元证据

1. If you had to desynchronize the acknowledgments transmissions, that would be very, very complicated.
如果你必须让那些确认的传输错开时间，那会非常、非常复杂。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–7, absolute 3997.68–4007.12s
2. And [it / you unclear] would increase the overhead of the protocol.
而且[它／你，待听辨]会增加协议的开销。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–7, absolute 3997.68–4007.12s
   限制：Qwen 36: it would increase the overhead of the protocol; medium-023 segment 7: you would increase the order of the problem. Feishu supplied section-55 fragment starts later. The technical noun is supported by Qwen; subject is unresolved.
3. So that's [not good / done unclear].
所以那[不好／完了，待听辨]。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–7, absolute 3997.68–4007.12s
   限制：Feishu 67: that's not good; Qwen 36: that's done; medium omits this short sentence. Not silently adopting the fluent interpretation.
4. So the choice that they made was, well, if a packet is broadcast or multicast, the transmitter of course needs to sense the channel.
所以他们作出的选择是，嗯，如果一个数据包是广播或多播数据包，发送方当然需要侦听信道。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–10, absolute 3997.68–4039.06s
5. If the channel is idle, transmit.
如果信道空闲，发送。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–10, absolute 3997.68–4039.06s
6. If the channel is busy, of course, you have to perform the backoff procedure because you have to wait.
如果信道忙，当然，你必须执行退避过程，因为你必须等待。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–10, absolute 3997.68–4039.06s
7. But then once you access the channel and transmit, that's it.
但然后一旦你接入信道并发送，就这样了。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 10–12, absolute 4030.16–4058.40s
8. Okay, you are done, because you don't care if the packet was received successfully or unsuccessfully.
好，你完成了，因为你不在乎数据包是被成功接收了，还是没成功接收。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 10–12, absolute 4030.16–4058.40s
9. [You / we unclear] are done.
[你／我们，待听辨]完成了。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 10–12, absolute 4030.16–4058.40s
   限制：Qwen 36: You are done; medium-023 segment 12: we are done; Feishu here is corrupted as a Spanish phrase. Restore the repeated done sentence but flag its subject.
10. Okay, so broadcast and multicast packets are transmitted only once.
好，所以广播和多播数据包只发送一次。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 12–15, absolute 4049.74–4083.40s
11. So you may need to run the backoff procedure for those data packets, but just if, when you want to access the channel, you sense the channel as busy the first time, okay?
所以，你可能需要为那些数据包运行退避过程，但只是在你想接入信道时，第一次就侦听到信道忙的情况下，好吗？
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 12–15, absolute 4049.74–4083.40s
12. Then once you perform the backoff and you access the channel and transmit, you are done.
然后，一旦你执行退避，而你接入信道并发送，你就完成了。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 15–18, absolute 4075.84–4117.66s
13. Okay, [um unclear], if everything is clear so far, let me know if you have questions.
好，[嗯，待听辨]，如果到目前为止所有事情都清楚了，有问题就告诉我。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 15–18, absolute 4075.84–4117.66s
   限制：Qwen 37 alone includes um; Feishu and medium omit it. Kept as a short unresolved filler.
14. No questions?
没有问题吗？
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 15–18, absolute 4075.84–4117.66s
15. Okay, so if we are good, then we can now tackle this last condition.
好，所以如果我们都没问题，那么我们现在就可以处理这最后一种情况。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 15–18, absolute 4075.84–4117.66s
16. That is, well, we have one more situation under which we perform the backoff.
也就是说，嗯，我们还有一种情况，在这种情况下我们执行退避。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 18–21, absolute 4105.50–4143.94s；Unprompted Whisper medium.en raw: chunk-024, segments 1–2, absolute 4125.00–4138.36s
17. In this third situation, actually, the procedure is slightly, slightly different, okay?
在这第三种情况下，实际上，这个过程稍微、稍微有点不同，好吗？
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 18–21, absolute 4105.50–4143.94s；Unprompted Whisper medium.en raw: chunk-024, segments 1–2, absolute 4125.00–4138.36s
18. [It is / is, is unclear] essentially the same except for one [thing unclear].
[它是／是、是，待听辨]基本上相同的，除了一个[事情，待听辨]。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 18–21, absolute 4105.50–4143.94s；Unprompted Whisper medium.en raw: chunk-024, segments 1–2, absolute 4125.00–4138.36s
   限制：Feishu: is, is essentially the same except for one; Qwen 37: It is essentially the same except for one thing; medium-023/024: It's essentially the same except for one. Do not silently add thing or discard the possible false start.
19. What is this third situation?
这个第三种情况是什么？
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 18–21, absolute 4105.50–4143.94s；Unprompted Whisper medium.en raw: chunk-024, segments 1–2, absolute 4125.00–4138.36s
20. [And it is called unclear], in this case the procedure is called [fast / post unclear] backoff, just to underline that there is a small difference with respect to the backoff run under the previous two situations.
[而且它叫作，待听辨]，在这种情况下，这个过程叫作[fast／post，待听辨]退避，只是为了强调它与前面两种情况下运行的退避有一个小的区别。
   来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 21–22, absolute 4137.62–4154.62s；Unprompted Whisper medium.en raw: chunk-024, segments 3–4, absolute 4138.62–4157.50s
   限制：Feishu: It is called in this case ... fast back off; Qwen 37: And indeed it is called in this case ... fast backoff; medium-023: And it is called ... fast back-off; medium-024 omits the restart and also says fast. Later section 58 has post backoff and medium section 60 has post; technical expectation does not certify the local word.

## 56 · 01:09:19 · 成功传输后仍须执行退避

稳定块ID：doxcnSOlCgY8oM1YQQ6YaPFWmPg
原块SHA256：c752c987c175de53931ff27620c7a00d24c3cdf37f2d5ac8a689d19698d5548f
候选SHA256：1ba85648336ecc6f540df81fef15740add2fa5ce53742b24d89e9466ff594753

### 具体修改

1. 原：What is this third situation? It is when a node transmits a data packet successfully.
   候选：So what is this third situation? [It is / is unclear] when a node transmits a data packet successfully.
   理由：恢复So及is when前It有无的口语疑点；不根据语法自动补。
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-024, segments 5–5, absolute 4159.22–4168.92s
2. 原：You may say: why do I have to perform backoff? I transmitted my packet correctly; I'm done. What do you want from me?
   候选：So you may say, well, why do I have to perform the backoff in this case? [I transmitted / I've transmitted unclear] my packet correctly, [I'm / and unclear] done. What do you want from me?
   理由：恢复So、well、the backoff、in this case及I transmitted/I’ve transmitted时态冲突；保留对话原句。
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 6–7, absolute 4169.94–4186.90s
3. 原：Well, Wi-Fi says: I know you transmitted your packet and you are done with that, but after receiving the ACK from the receiver, you need to perform backoff using zero to CW_min as the range of possible integers. That's what the protocol says.
   候选：Well, the Wi-Fi says, I know you transmitted your packet, you are done with that, but after you receive the ACK from the receiver, you need to perform a backoff using zero, CW_min as range of possible integers. That's [what / why unclear] the protocol says.
   理由：恢复the Wi-Fi、you receive、a backoff、using zero CW_min as range，不重写after receiving或补to/the。
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 7–9, absolute 4178.02–4223.82s

### 逐单元证据

1. So what is this third situation?
所以，这第三种情况是什么？
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-024, segments 5–5, absolute 4159.22–4168.92s
2. [It is / is unclear] when a node transmits a data packet successfully.
[它是／是，待听辨]当一个节点成功发送一个数据包的时候。
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-024, segments 5–5, absolute 4159.22–4168.92s
   限制：Qwen 37 and Feishu start with is when; medium-024 segment 5 has It is when.
3. So you may say, well, why do I have to perform the backoff in this case?
所以，你可能会说，嗯，在这种情况下我为什么必须执行退避？
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 6–7, absolute 4169.94–4186.90s
4. [I transmitted / I've transmitted unclear] my packet correctly, [I'm / and unclear] done.
[我发送了／我已经发送了，时态待听辨]我的数据包，而且发送正确，[我／而且，待听辨]完成了。
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 6–7, absolute 4169.94–4186.90s
   限制：Feishu/Qwen 37: I transmitted my packet correctly and done; medium-024: I've transmitted my packet correctly, I'm done. Both the tense and the short fragment before done remain unresolved.
5. What do you want from me?
你还想让我做什么？
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 6–7, absolute 4169.94–4186.90s
6. Well, the Wi-Fi says, I know you transmitted your packet, you are done with that, but after you receive the ACK from the receiver, you need to perform a backoff using zero, CW_min as range of possible integers.
嗯，Wi-Fi 说，我知道你发送了你的数据包，你已经完成了那个，但在你从接收方收到 ACK 之后，你需要执行一次退避，用零、CW_min 作为可能的整数的范围。
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 7–9, absolute 4178.02–4223.82s
7. That's [what / why unclear] the protocol says.
那就是协议[所说的／为什么说，待听辨]。
   来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 7–9, absolute 4178.02–4223.82s
   限制：Feishu and medium-024: That's what the protocol says; Qwen 38: That's why the protocol says. Most of the preceding clause is supported by medium and Qwen, despite Qwen's transmit in your pocket corruption.

## 57 · 01:10:13 · 发送后退避的公平性目标

稳定块ID：doxcnYKp8xXaOwlMx8lzDMPjmEh
原块SHA256：8fe13c12b77dd97b6d88c4132b96f39d3e5d8c7a8093cd297a4f50ed65588b62
候选SHA256：46afc12edbb215eaab9e783e6435b7591ed5ca8371550b826e031c2f77c0bae6

### 具体修改

1. 原：Again, we want to understand why. This is not enough: okay, I have to do it, I will do it, but tell me why. Why do I have to do that? The reason is fairness. We want to be fair to our nodes.
   候选：So again, we want to understand why, right? [I mean / maybe unclear], this is not enough. Okay, I have to do it, I will do it, but tell me why, why do I have to do that? Well, the reason is fairness. We want to be fair to our nodes.
   理由：恢复So、right、I mean及Well；保留I have to/I will重复，不压缩。
   来源：Feishu historical snapshot: source_index=70, id=145, section anchor 01:10:13；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 9–10, absolute 4194.68–4235.92s

### 逐单元证据

1. So again, we want to understand why, right?
所以，我们还是想理解为什么，对吧？
   来源：Feishu historical snapshot: source_index=70, id=145, section anchor 01:10:13；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 9–10, absolute 4194.68–4235.92s
2. [I mean / maybe unclear], this is not enough.
[我的意思是／也许，待听辨]，这还不够。
   来源：Feishu historical snapshot: source_index=70, id=145, section anchor 01:10:13；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 9–10, absolute 4194.68–4235.92s
   限制：Feishu and Qwen 38: I mean; medium-024 segment 9: maybe. Flag the local phrase without overwriting the broader sentence.
3. Okay, I have to do it, I will do it, but tell me why, why do I have to do that?
好，我必须做，我会做，但告诉我为什么，为什么我必须那样做？
   来源：Feishu historical snapshot: source_index=70, id=145, section anchor 01:10:13；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 9–10, absolute 4194.68–4235.92s
4. Well, the reason is fairness.
嗯，原因是公平性。
   来源：Feishu historical snapshot: source_index=70, id=145, section anchor 01:10:13；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 9–10, absolute 4194.68–4235.92s
5. We want to be fair to our nodes.
我们想公平地对待我们的节点。
   来源：Feishu historical snapshot: source_index=70, id=145, section anchor 01:10:13；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 9–10, absolute 4194.68–4235.92s

## 58 · 01:10:32 · 用A成功发送场景说明发送后退避

稳定块ID：doxcnBdnbpPGhKGwvSK0xHE3Xkf
原块SHA256：08517066cda9b072aeb2f23fea809ed01e86c5988088b6837f224fac8ca8f3cb
候选SHA256：e134a4473d4fa55259f39a869519dd5d2874f2c17a3c4a6b62650327a1baad4d

### 具体修改

1. 原：Let me give an example that will allow us to understand why they tell us to run post-backoff once we transmit successfully.
   候选：Okay, so let me give [you unclear] an example, and that will allow us to indeed understand why they tell us, once you transmit successfully, run this post-backoff.
   理由：恢复Okay So、and that will、indeed、引述once you transmit successfully run this post-backoff；give you有无标示。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 10–12, absolute 4223.82–4263.48s
2. 原：Let's consider the same scenario again: an access point, node A, and our B and C nodes, as before. We already know the story, so it will be easier.
   候选：So let's consider again the same scenario, so that will be easy. Access point, and then node A. And then we can also consider our B and C nodes, right? Same as before. So we know [already / that with unclear] the story, it will be easier.
   理由：恢复So、again the same scenario、so that will be easy、碎片Access point and then node A、And then we can also、right及Same as before；we know already来源冲突短标。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 12–14, absolute 4254.16–4284.52s
3. 原：It starts in the same way. A has a packet, senses the channel for DIFS, finds it idle, and transmits its unicast data packet to the access point. The transmission is successful, so the access point sends back the ACK.
   候选：So the story starts in the same way. A has got a packet, [DIFS unclear], channel idle, transmits the data packet, unicast data packet to the access point. This packet transmission is successful, so the access point [sends / sent unclear] back the ACK.
   理由：恢复So the story starts、has got、DIFS/channel idle碎片与data packet / unicast data packet重复；撤销现稿补出的senses/finds动词，ACK前动词待听辨。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 15–17, absolute 4285.52–4323.38s；Unprompted Whisper medium.en raw: chunk-025, segments 1–1, absolute 4305.00–4316.38s

### 逐单元证据

1. Okay, so let me give [you unclear] an example, and that will allow us to indeed understand why they tell us, once you transmit successfully, run this post-backoff.
好，所以让我[给你们，待听辨]举一个例子，而那会让我们的确理解为什么他们告诉我们，一旦你成功发送，就运行这个发送后退避。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 10–12, absolute 4223.82–4263.48s
   限制：Qwen 38: give you an example; Feishu and medium-024 segments 10–11: give an example. Indeed is Qwen's clear reading, with Feishu in beat / medium in winter near-phonetic corruptions. Post-backoff is clear in Feishu, Qwen has post pickoff, medium hospital.
2. So let's consider again the same scenario, so that will be easy.
所以，我们再考虑同一个场景，那样就容易了。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 12–14, absolute 4254.16–4284.52s
3. Access point, and then node A.
接入点，然后节点 A。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 12–14, absolute 4254.16–4284.52s
4. And then we can also consider our B and C nodes, right?
然后我们也可以考虑我们的 B 和 C 节点，对吧？
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 12–14, absolute 4254.16–4284.52s
5. Same as before.
和之前一样。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 12–14, absolute 4254.16–4284.52s
6. So we know [already / that with unclear] the story, it will be easier.
所以我们[已经／that with，待听辨]知道这个过程，它会更容易。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 12–14, absolute 4254.16–4284.52s
   限制：Qwen 38: we know already the story; Feishu: we know that if the story; medium-024 segment 14: we know that with the story. The current fluent paraphrase cannot settle this local wording.
7. So the story starts in the same way.
所以，这个过程以同样的方式开始。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 15–17, absolute 4285.52–4323.38s；Unprompted Whisper medium.en raw: chunk-025, segments 1–1, absolute 4305.00–4316.38s
8. A has got a packet, [DIFS unclear], channel idle, transmits the data packet, unicast data packet to the access point.
A 有了一个数据包，[DIFS，待听辨]，信道空闲，发送这个数据包，单播数据包给接入点。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 15–17, absolute 4285.52–4323.38s；Unprompted Whisper medium.en raw: chunk-025, segments 1–1, absolute 4305.00–4316.38s
   限制：Feishu/Qwen/medium all render the short item after packet as leaves. DIFS is a strong technical near-phonetic possibility, not locally clear. None supplies the current draft's expanded senses the channel for / finds it / its phrasing.
9. This packet transmission is successful, so the access point [sends / sent unclear] back the ACK.
这次数据包传输是成功的，所以接入点[发回／发回了，时态待听辨] ACK。
   来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 15–17, absolute 4285.52–4323.38s；Unprompted Whisper medium.en raw: chunk-025, segments 1–1, absolute 4305.00–4316.38s
   限制：Qwen 39: access points have back the ACK; medium-024/025: access points have backed the ACK; Feishu fragment ends before this. Sends/sent is a plausible reconstruction of the garbled verb, not audio-certified.

## 59 · 01:11:51 · B和C设NAV并收到待发数据

稳定块ID：doxcnWJukIbTM7WOpJFug42kc4d
原块SHA256：4bcbac7005ec269a6617cac33c4dc000ecba17d80c6e4b2a97b07bf174358e80
候选SHA256：be907002d5068dc29f29b9c504480fe4152f0f6f04cc269473f9f2c50f71346a

### 具体修改

1. 原：As we said before, all nodes are in radio visibility of each other; they can hear each other. B and C therefore set their NAV.
   候选：And as we said before, all nodes are in radio visibility of each other, they can hear each other. So B and C will set their [NAV unclear].
   理由：恢复And、So及will；NAV保留局部听辨标示，不把NAT/noth等粗糙ASR当音频确认。
   来源：Feishu historical snapshot: source_index=72, id=149, section anchor 01:11:51；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 17–18, absolute 4304.78–4334.68s；Unprompted Whisper medium.en raw: chunk-025, segments 1–2, absolute 4305.00–4326.30s
2. 原：As before, at a certain point they get a packet from their respective higher layers, so they will have to transmit their packets.
   候选：And same as before, at a certain point B and C get a packet from their respective higher layers, so they will have to transmit their packet, right?
   理由：恢复And same as before、第二次B and C、their packet单数及right；不以they替换节点名。
   来源：Feishu historical snapshot: source_index=72, id=149, section anchor 01:11:51；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 18–18, absolute 4323.38–4334.68s；Unprompted Whisper medium.en raw: chunk-025, segments 3–4, absolute 4326.30–4349.54s

### 逐单元证据

1. And as we said before, all nodes are in radio visibility of each other, they can hear each other.
而且正如我们之前说的，所有节点都处在彼此的无线可见范围内，它们可以互相听到。
   来源：Feishu historical snapshot: source_index=72, id=149, section anchor 01:11:51；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 17–18, absolute 4304.78–4334.68s；Unprompted Whisper medium.en raw: chunk-025, segments 1–2, absolute 4305.00–4326.30s
2. So B and C will set their [NAV unclear].
所以 B 和 C 会设置它们的[NAV，待听辨]。
   来源：Feishu historical snapshot: source_index=72, id=149, section anchor 01:11:51；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 17–18, absolute 4304.78–4334.68s；Unprompted Whisper medium.en raw: chunk-025, segments 1–2, absolute 4305.00–4326.30s
   限制：Medium-025 segment 2: will set their NAT; Feishu: will send their noth; Qwen 39: will say they are not. NAV is the intended protocol term strongly indicated by earlier exposition, but the local word is garbled in all supplied ASRs.
3. And same as before, at a certain point B and C get a packet from their respective higher layers, so they will have to transmit their packet, right?
而且和之前一样，在某个时刻 B 和 C 从它们各自的高层收到一个数据包，所以它们将必须发送它们的数据包，对吧？
   来源：Feishu historical snapshot: source_index=72, id=149, section anchor 01:11:51；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 18–18, absolute 4323.38–4334.68s；Unprompted Whisper medium.en raw: chunk-025, segments 3–4, absolute 4326.30–4349.54s

## 60 · 01:12:20 · A成功后退避与B、C常规退避

稳定块ID：doxcnJy0CfZy89ROVTTTAPVxpFe
原块SHA256：0b33636abf529312c9af57d6bcaaa5e31e32cfd0b5dc7232b24e4207415e2c62
候选SHA256：bb4e4268c44a6b29fd808acfae1ee9b9ecfbde84a79b8443eaffdd90f39a7a18

### 具体修改

1. 原：We already know how things work, but now our attention is on A. Let's focus on A. A is the one that performed its transmission successfully, so it is done.
   候选：And we know already how things work, fine, but now our attention is on A, okay? Let's focus on A. A is the one that performs its transmission successfully, so it's done.
   理由：恢复And we know already、fine、okay与performs现在式，不能沿现稿performed。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 4–6, absolute 4336.56–4375.04s
2. 原：According to the protocol, once A has finished transmitting the packet and received the ACK, it needs to perform post-backoff.
   候选：And according to the protocol, now we know that A actually, once it has finished transmitting the packet and [received / receive unclear] the ACK, needs to perform this [post / past / fast unclear] backoff procedure, right?
   理由：恢复And、now we know that、A actually、this ... procedure、right及received/receive词尾冲突。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 6–8, absolute 4366.02–4394.90s
3. 原：It has to sense the channel for DIFS and then draw an integer from zero to CW_min.
   候选：So [it / I unclear] will have to sense the channel for [DIFS unclear], and then [it / you / we unclear] will have to draw an integer out of the range zero, CW_min.
   理由：恢复So、will have to两次与out of the range，主语it/I/you/we来源分歧标示，不把未来式改现在式。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 8–9, absolute 4384.48–4406.84s
4. 原：B and C behave as before; we know that already. They have to run a regular backoff procedure.
   候选：And of course for B and C we'll have the same behavior as before. We know [that already / that's ready unclear]. So B and [and unclear] C will have to run a, let's say, regular backoff procedure.
   理由：恢复And of course for B and C we’ll have、So B and C will have to、a let’s say regular及that already疑点；保留源中and and重复可能。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 9–11, absolute 4394.90–4432.24s

### 逐单元证据

1. And we know already how things work, fine, but now our attention is on A, okay?
而且我们已经知道事情如何进行，很好，但现在我们的注意力在 A 上，好吗？
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 4–6, absolute 4336.56–4375.04s
2. Let's focus on A.
我们把注意力放在 A 上。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 4–6, absolute 4336.56–4375.04s
3. A is the one that performs its transmission successfully, so it's done.
A 是那个成功进行它的传输的节点，所以它完成了。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 4–6, absolute 4336.56–4375.04s
4. And according to the protocol, now we know that A actually, once it has finished transmitting the packet and [received / receive unclear] the ACK, needs to perform this [post / past / fast unclear] backoff procedure, right?
而根据协议，现在我们知道，A 实际上，一旦它已经发送完数据包并且[收到了／收到，时态待听辨] ACK，就需要执行这个[post／past／fast，待听辨]退避过程，对吧？
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 6–8, absolute 4366.02–4394.90s
   限制：Qwen 39: received ... past backoff; Feishu: receive ... fast bake off; medium-025: receive ... post bake-off. The post prefix has local medium support and section-58 context, but source disagreement is explicit. Received/receive is not silently grammatically corrected.
5. So [it / I unclear] will have to sense the channel for [DIFS unclear], and then [it / you / we unclear] will have to draw an integer out of the range zero, CW_min.
所以[它／我，待听辨]将必须侦听信道一个[DIFS，待听辨]的时间，然后[它／你／我们，待听辨]将必须从零、CW_min 这个范围中抽取一个整数。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 8–9, absolute 4384.48–4406.84s
   限制：Qwen 39: it will ... it will; medium-025: I will ... you will; Feishu: I will ... we will. All give leaves for the timing term; DIFS is the technical reconstruction, marked rather than certified. All retain future will have to.
6. And of course for B and C we'll have the same behavior as before.
而且当然，对于 B 和 C，我们会有和之前相同的行为。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 9–11, absolute 4394.90–4432.24s
7. We know [that already / that's ready unclear].
我们知道[那个已经／that's ready，待听辨]。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 9–11, absolute 4394.90–4432.24s
   限制：Feishu, Qwen 40 and medium-025 all approximate that's ready. That already is plausible from the lecturer's meaning but not established locally.
8. So B and [and unclear] C will have to run a, let's say, regular backoff procedure.
所以 B 和[和，重复待听辨] C 将必须运行一个，我们说，常规的退避过程。
   来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 9–11, absolute 4394.90–4432.24s
   限制：Feishu repeats and and; Qwen 40 and medium-025 have and once and both retain let's say, omitted from the current draft. The local technical word is go/cough/kickoff in the rough ASRs, normalized as backoff with context.

## 61 · 01:13:44 · 移除发送后退避的消融实验

稳定块ID：doxcnOafaFDOATqssKwhE22BQ4g
原块SHA256：fa9d0b1d6f6f221baa386dfa659474b58064007c3673983255c2b025d0163768
候选SHA256：e8e0d1023cbf1cf85cf9923055d888f6fa024c864e97072ff07e17951b7de553

### 具体修改

1. 原：Again, to understand how useful a mechanism or solution is, let's play our little game of ablation.
   候选：So again, in order to understand how useful [a / the unclear] mechanism is, or solution is, let's play our little game of ablation, right?
   理由：恢复So、in order to、两次is及right，撤销原校订的合并；a/the保持冲突。
   来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 11–12, absolute 4421.20–4441.52s
2. 原：Let's remove post-backoff and see what happens. What if A does not have to run any post-backoff?
   候选：So let's remove the post-backoff and see what happens. So what if A does not have to run any, [any unclear] post-backoff?
   理由：恢复两次So与the，Qwen独有any重复明确标待听辨，不机械吸收上下段。
   来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 12–13, absolute 4432.24–4455.72s；Unprompted Whisper medium.en raw: chunk-025, segments 13–13, absolute 4441.60–4455.72s
3. 原：Let's add an event here to understand what would happen, considering all possible cases.
   候选：Well, let's add an event here to better understand what would happen considering all possible cases.
   理由：恢复三类证据均保留的Well及better。
   来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 14–15, absolute 4458.16–4482.56s

### 逐单元证据

1. So again, in order to understand how useful [a / the unclear] mechanism is, or solution is, let's play our little game of ablation, right?
所以，再一次，为了理解[一种／这一个，待听辨]机制有多有用，或者解决方案有多有用，让我们玩一下我们的小小消融游戏，对吧？
   来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 11–12, absolute 4421.20–4441.52s
   限制：历史Feishu为a mechanism、Our solution；Qwen与medium为the mechanism、or solution。恢复口语重复is，不改成精炼的a mechanism or solution；冠词待听辨。right由历史Feishu与Qwen保留。
2. So let's remove the post-backoff and see what happens.
所以，让我们去掉发送后退避，看看会发生什么。
   来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 12–13, absolute 4432.24–4455.72s
   限制：post-backoff按历史post back off及medium pass back off近音作技术术语规范；Qwen为post go。
3. So what if A does not have to run any, [any unclear] post-backoff?
所以，如果A不必执行任何、[任何，重复待听辨]发送后退避，会怎么样？
   来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 13–13, absolute 4441.60–4455.72s
   限制：Qwen同一窗口保留any any；Feishu与medium仅一次，不把第二个any写成已确认。
4. Well, let's add an event here to better understand what would happen considering all possible cases.
嗯，让我们在这里加一个事件，考虑所有可能的情况，来更好地理解会发生什么。
   来源：Feishu historical snapshot: source_index=74, id=153, section anchor 01:13:44；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 14–15, absolute 4458.16–4482.56s

## 62 · 01:14:31 · A队列中还有另一个待发包

稳定块ID：doxcniDom3MTYG6SdyGg8uIbLqh
原块SHA256：acfbe892156f61001dad4a05a8b5fe3b3ca7ec182b47e16e5991168ca9a0458a
候选SHA256：3f664546c4f622fb5dab2130bf6982d49dbfec596dd3c498b2077762116bb21e

### 具体修改

1. 原：Let's consider that A has another packet in its MAC queue. Remember that we said the MAC layer can be modeled as a queue with a server.
   候选：Let's consider that A has got another packet in [a unclear] its MAC queue. Remember that we said the MAC layer can be modeled, right, as a queue with a server.
   理由：恢复has got及right，并明确标出Feishu独有in a its口语残片。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 15–15, absolute 4468.46–4482.56s；Unprompted Whisper medium.en raw: chunk-025, segments 15–16, absolute 4468.46–4492.98s；Unprompted Whisper medium.en raw: chunk-026, segments 1–1, absolute 4485.00–4494.78s
2. 原：A has transmitted the packet here successfully, but let's assume it has another packet in the queue waiting to be transmitted.
   候选：So let's consider that A has transmitted the packet here successfully, but let's assume that A has [got / put unclear] another packet in the queue waiting to be transmitted.
   理由：恢复So let's consider that、重复主语A及has got/put词冲突；不以代词压缩原话。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 16–17, absolute 4482.56–4503.40s；Unprompted Whisper medium.en raw: chunk-026, segments 1–2, absolute 4485.00–4503.42s
3. 原：This first packet goes through successfully; that's what we represented here. But now A has another packet right here.
   候选：So this first packet goes through, right, successfully. This is what we [represented / represent unclear] here. But now A has got another packet right here, right?
   理由：恢复So、right、This is、has got及尾部right，保留represent/represented时态冲突；两组重叠窗口只保留一次句子。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 18–18, absolute 4505.12–4514.78s；Unprompted Whisper medium.en raw: chunk-026, segments 3–3, absolute 4503.42–4518.58s；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 3–4, absolute 4503.42–4529.80s

### 逐单元证据

1. Let's consider that A has got another packet in [a unclear] its MAC queue.
让我们考虑A在[一个，待听辨]它的MAC队列里又有了一个数据包。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 15–15, absolute 4468.46–4482.56s
   限制：历史Feishu为in a its，Qwen和medium为in its；a可能是口误或识别插入，保留待听辨。MAC由medium明确识别，历史/Qwen的mark为技术近音。
2. Remember that we said the MAC layer can be modeled, right, as a queue with a server.
记住，我们说过，MAC层可以被建模，对吧，建模成一个带有服务台的队列。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 15–16, absolute 4468.46–4492.98s；Unprompted Whisper medium.en raw: chunk-026, segments 1–1, absolute 4485.00–4494.78s
   限制：right由历史Feishu及Qwen保留；modeled由medium明确识别，历史modern/Qwen modded为近音。
3. So let's consider that A has transmitted the packet here successfully, but let's assume that A has [got / put unclear] another packet in the queue waiting to be transmitted.
所以，让我们考虑A已经在这里成功地发送了这个数据包，但让我们假设A在队列里[还有／放入了，待听辨]另一个等待发送的数据包。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 16–17, absolute 4482.56–4503.40s；Unprompted Whisper medium.en raw: chunk-026, segments 1–2, absolute 4485.00–4503.42s
   限制：历史Feishu及medium为has got；Qwen为has put。两者含义不同，不强选。
4. So this first packet goes through, right, successfully.
所以，这第一个数据包通过了，对吧，成功地通过了。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 18–18, absolute 4505.12–4514.78s；Unprompted Whisper medium.en raw: chunk-026, segments 3–3, absolute 4503.42–4518.58s
5. This is what we [represented / represent unclear] here.
这就是我们在这里[已经表示出的／所表示的，时态待听辨]内容。
   来源：Feishu historical snapshot: source_index=75, id=155, section anchor 01:14:31；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-025, segments 18–18, absolute 4505.12–4514.78s；Unprompted Whisper medium.en raw: chunk-026, segments 3–3, absolute 4503.42–4518.58s
   限制：medium chunk-025句尾为represent，重叠chunk-026为represented；历史Feishu和Qwen为represented。重叠只对应一句，时态待听辨。
6. But now A has got another packet right here, right?
但现在A在这里又有了一个数据包，对吧？
   来源：Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 3–4, absolute 4503.42–4529.80s
   限制：此尾句在Qwen41及medium26中完整出现；Qwen40只到But now A is going，不能将截断另作新句。历史Feishu本段未收该句，按现有段边界保留于62。

## 63 · 01:15:22 · 没有发送后退避时A立即再发

稳定块ID：doxcnfJ7kuePp8OBvwoAxXJk1sc
原块SHA256：7087863a79c0033c8c9f39969cc86ca00dc44319e77b888911aaddb161d060cf
候选SHA256：d28ad77ade955c38b40d055688fe3c5b6629fc1de8601e53b9e41de730d18f3c

### 具体修改

1. 原：When it is done with this dialogue, it has another packet to deal with. What if A didn't have any post-backoff to run?
   候选：So when [it's / he's unclear] done with this dialogue, [we'll / we unclear] have another packet to deal with. So what if A didn't have any post-backoff to run?
   理由：恢复两个So与we'll/we have，撤销无依据改成it has；保留he/it、时态冲突。
   来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 4–5, absolute 4518.58–4540.46s；Unprompted Whisper medium.en raw: chunk-026, segments 5–5, absolute 4529.80–4540.46s
2. 原：It would sense the channel for DIFS, find it idle, and be able to access it and transmit its other data packet.
   候选：Well, [it / he / you unclear] will have to sense the channel for DIFS. The channel is idle, and [it / you unclear] will be able to access the channel [and transmit / trust me unclear]. So [it / you unclear] will have to transmit its [other / own unclear] data.
   理由：撤销合句压缩及would/find；恢复Well、will have to、The channel is idle、重复the channel、So，移除无原始支持的packet；缺失尾部与代词、other/own分别待听辨。
   来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 5–6, absolute 4529.80–4550.44s；Unprompted Whisper medium.en raw: chunk-026, segments 6–7, absolute 4540.46–4562.60s；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s
3. 原：This may be successful. Would that be fair with respect to B and C?
   候选：This may be successful. And what would be that? Would that be fair with respect to B and C?
   理由：保留原有两句并恢复Qwen及medium均显示但旧校订删去的And what would be that?。
   来源：Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s；Unprompted Whisper medium.en raw: chunk-026, segments 8–8, absolute 4564.02–4571.70s

### 逐单元证据

1. So when [it's / he's unclear] done with this dialogue, [we'll / we unclear] have another packet to deal with.
所以，当[它／他，待听辨]完成这轮对话时，我们[将会有／有，待听辨]另一个数据包要处理。
   来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 4–5, absolute 4518.58–4540.46s
   限制：历史Feishu为he's、we'll；Qwen为it's、we'll；medium为it's、we。不能按技术叙述习惯改为it has。
2. So what if A didn't have any post-backoff to run?
所以，如果A没有任何发送后退避要执行，会怎么样？
   来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 5–5, absolute 4529.80–4540.46s
   限制：post-backoff为同一机制的术语规范：历史cost、Qwen possible cost、medium phospho-cov均为近音输出。
3. Well, [it / he / you unclear] will have to sense the channel for DIFS.
嗯，[它／他／你，待听辨]将必须侦听信道一个DIFS的时间。
   来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 5–6, absolute 4529.80–4550.44s
   限制：保留will have to，不改为would；Qwen it、Feishu he、medium you冲突。sense与DIFS是技术近音规范（Since/Sends、B's/this），不改成find idle。
4. The channel is idle, and [it / you unclear] will be able to access the channel [and transmit / trust me unclear].
信道是空闲的，而[它／你，待听辨]将能够接入信道[并发送／相信我，待听辨]。
   来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 6–7, absolute 4540.46–4562.60s
   限制：Feishu尾部独立Trust me，medium为and trust me，Qwen未保留此尾部；不能凭技术语义直接补transmit，也不删除残片。
5. So [it / you unclear] will have to transmit its [other / own unclear] data.
所以，[它／你，待听辨]将必须发送它的[其他／自己的，待听辨]数据。
   来源：Feishu historical snapshot: source_index=76, id=157, section anchor 01:15:22；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s
   限制：Qwen为it、own；Feishu为you、other；medium为you、other但transmit误成ask me。未擅加packet。
6. This may be successful.
这可能会成功。
   来源：Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 7–7, absolute 4550.72–4562.60s
7. And what would be that?
那这会是什么情况？
   来源：Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–8, absolute 4564.02–4571.70s
8. Would that be fair with respect to B and C?
这对B和C来说会公平吗？
   来源：Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–8, absolute 4564.02–4571.70s
   限制：两份ASR均为fear；与后文unfair/fairness构成同一讨论，作fair技术语境近音规范，不改原疑问句结构。

## 64 · 01:16:10 · 连续占用信道造成不公平

稳定块ID：doxcnOX3I4DDVfFDghwN2D719Lf
原块SHA256：143a3e8651c731052c2c8e6589ff598ed433e5fc310d72bc7cf2a7373cc0c291
候选SHA256：1138beded9b50ae36010f94bda8285a6d96caf106bb441f5e6da51b6c8891fd6

### 具体修改

1. 原：Poor B and C are waiting for their backoff time, and A just gets the next packet and goes ahead with its transmission. This is unfair.
   候选：The poor B and C are waiting [right there unclear], their backoff time, and A just gets the next packet and go ahead with its transmission. So this is unfair.
   理由：恢复The、right there残片、So和讲者原有go语法；撤销替补介词for，不伪装为完整顺畅句。
   来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–10, absolute 4564.02–4592.18s；Unprompted Whisper medium.en raw: chunk-026, segments 10–10, absolute 4580.36–4592.18s
2. 原：If a Wi-Fi card like A has several packets to transmit, in this situation without post-backoff it will just continue accessing the channel and transmitting its packets.
   候选：And indeed, if a Wi-Fi card like A has got several packets to transmit, under this situation without post-backoff, we just continue accessing the channel and transmitting its packets.
   理由：恢复And indeed、has got、under this situation及原始we just continue，不把主语语法整理成it will。
   来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 10–12, absolute 4580.36–4609.86s
3. 原：With very high probability it will seize the channel for a very long time and transmit, transmit, transmit, while the others have to wait, wait, and wait, because the channel will become busy continuously.
   候选：With very high probability, [it / you unclear] will actually seize the channel for a very long time and transmit, transmit, transmit, while the others [will have / we have / we had unclear] to wait, wait, [and unclear] wait, because the channel [will / would unclear] become busy [confused unclear].
   理由：恢复actually并标代词、时态及and冲突；continuously无三类原始文本支持，回退为busy之后的待听辨残片。
   来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 12–13, absolute 4601.40–4620.60s
4. 原：This was indeed observed experimentally. Years ago, some researchers experimented with different Wi-Fi cards that were commercial products.
   候选：And this was indeed observed, also experimentally. Years ago, some researchers made experiments with different Wi-Fi cards. [They / which unclear] were commercial products.
   理由：恢复And、also、made experiments和they/which were，不用experimented/that were润色替换。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 14–14, absolute 4622.54–4632.44s；Unprompted Whisper medium.en raw: chunk-026, segments 14–15, absolute 4622.54–4642.06s；Unprompted Whisper medium.en raw: chunk-026, segments 15–15, absolute 4632.44–4642.06s
5. 原：All these cards claimed to follow the standard; products must follow the standard. They claimed to do that, but one card was applying everything specified by the standard except post-backoff.
   候选：They claimed, all these cards [claimed / claim unclear] to follow the standard. [Of course / for unclear] products must follow the standard. They [claimed / claim unclear] to do that. But actually, one of these cards was applying everything, okay, as specified by the standard, but the post-backoff.
   理由：恢复They claimed起句、all these cards重复、Of course/for、But actually、one of these cards、okay、as和句尾but；两处claim时态保留冲突。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 15–16, absolute 4632.44–4648.32s；Unprompted Whisper medium.en raw: chunk-026, segments 16–16, absolute 4642.06–4648.32s；Unprompted Whisper medium.en raw: chunk-026, segments 16–18, absolute 4642.06–4669.06s

### 逐单元证据

1. The poor B and C are waiting [right there unclear], their backoff time, and A just gets the next packet and go ahead with its transmission.
可怜的B和C[就在那儿，待听辨]等着，等它们的退避时间，而A只是拿到下一个数据包，就继续它的发送。
   来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 8–10, absolute 4564.02–4592.18s
   限制：历史为right there, their back off time；Qwen为right there because time；medium为very good, their pick-off time。保留历史残句和go语法，right there标待听辨；backoff为术语近音规范。
2. So this is unfair.
所以，这是不公平的。
   来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 10–10, absolute 4580.36–4592.18s
3. And indeed, if a Wi-Fi card like A has got several packets to transmit, under this situation without post-backoff, we just continue accessing the channel and transmitting its packets.
而且确实，如果像A这样的Wi-Fi网卡有好几个数据包要发送，在这种没有发送后退避的情况下，我们就一直接入信道，并发送它的数据包。
   来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 10–12, absolute 4580.36–4609.86s
   限制：三类文本均呈现we just continue，保持讲者主语漂移，不改成it will；to transmit见历史及Qwen，medium略去。post-backoff为pass the cost/possible cost/cost because近音规范。
4. With very high probability, [it / you unclear] will actually seize the channel for a very long time and transmit, transmit, transmit, while the others [will have / we have / we had unclear] to wait, wait, [and unclear] wait, because the channel [will / would unclear] become busy [confused unclear].
以非常高的概率，[它／你，待听辨]实际上会占据信道很长时间，并且发送、发送、发送，而其他那些[将必须／我们必须／我们过去必须，待听辨]等、等、[并且，待听辨]等，因为信道[将会／会，待听辨]变忙[后词疑似confused，待听辨]。
   来源：Feishu historical snapshot: source_index=77, id=159, section anchor 01:16:10；Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 12–13, absolute 4601.40–4620.60s
   限制：历史it、will have、and wait、will；Qwen you、we have、无and、will；medium you、we had、无and、would。seize由历史明确，其余size为近音；transmit由历史/Qwen明确。busy后的confused三类均不可靠，不采纳旧校订补出的continuously。
5. And this was indeed observed, also experimentally.
而且，这也确实在实验中被观察到了。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=41, absolute 4510.00–4630.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 14–14, absolute 4622.54–4632.44s
   限制：observed有历史及Qwen明确词形；medium absurd属近音。
6. Years ago, some researchers made experiments with different Wi-Fi cards.
几年前，一些研究人员用不同的Wi-Fi网卡做了实验。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 14–15, absolute 4622.54–4642.06s
7. [They / which unclear] were commercial products.
[它们／这些，连接形式待听辨]是商业产品。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 15–15, absolute 4632.44–4642.06s
   限制：历史与medium为独立they were，Qwen为which were；保留冲突，不顺写从句。
8. They claimed, all these cards [claimed / claim unclear] to follow the standard.
它们声称，所有这些网卡都[声称过／声称，时态待听辨]遵循标准。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 15–16, absolute 4632.44–4648.32s
   限制：恢复They claimed起句和重复cards主语；Qwen第二处claim，历史及medium claimed。
9. [Of course / for unclear] products must follow the standard.
[当然／因为，待听辨]产品必须遵循标准。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 16–16, absolute 4642.06–4648.32s
   限制：medium明确of course，历史/Qwen为for；不能靠语句流畅度决定。
10. They [claimed / claim unclear] to do that.
它们[声称过／声称，时态待听辨]自己这样做。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 16–16, absolute 4642.06–4648.32s
11. But actually, one of these cards was applying everything, okay, as specified by the standard, but the post-backoff.
但实际上，这些网卡中的一张实施了标准所规定的所有内容，好吧，唯独发送后退避除外。
   来源：Feishu historical snapshot: source_index=78, id=161, section anchor 01:16:10；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 16–18, absolute 4642.06–4669.06s
   限制：保留but的except义及okay口语插入；post-backoff由Qwen post pickoff和medium post the cop近音规范。历史the cost became off不另增句。

## 65 · 01:17:42 · 未实施发送后退避的商用网卡实验

稳定块ID：doxcn1cpQfGyubHhKy2AGOYZv2e
原块SHA256：dcfb30afb26fdc0c88910a467b8a625b5f56f83d09151b32566410aac740f5fd
候选SHA256：823f48af0e3e1242487e3b30c113ed58186a54e42e567c47fc04f0be5dcb2875

### 具体修改

1. 原：The researchers observed that this Wi-Fi card obtained very, very high throughput, meaning it could transmit a lot of data, while the other cards were starving: they could not get access to the channel.
   候选：And what these researchers observed was that this Wi-Fi card was [obtaining / obtained unclear] a very, very high throughput; that means the ability to transmit a lot of data, while the other Wi-Fi cards were starving, so they could not get access to the channel.
   理由：恢复And what、was that、a、was obtaining/obtained冲突、that means the ability、完整other Wi-Fi cards及so；撤销meaning it could解释式改写。
   来源：Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 18–21, absolute 4660.40–4692.22s；Unprompted Whisper medium.en raw: chunk-027, segments 1–3, absolute 4665.00–4690.20s
2. 原：It was a very unfair service because that commercial Wi-Fi card did not implement post-backoff.
   候选：A very unfair service, and this is because, this was because that commercial Wi-Fi card at that time did not implement the post-backoff procedure.
   理由：撤销补写It was，恢复不完整名词句、is because/was because自修、at that time、the及procedure。
   来源：Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 21–22, absolute 4683.38–4694.20s；Unprompted Whisper medium.en raw: chunk-027, segments 3–5, absolute 4681.32–4708.56s

### 逐单元证据

1. And what these researchers observed was that this Wi-Fi card was [obtaining / obtained unclear] a very, very high throughput; that means the ability to transmit a lot of data, while the other Wi-Fi cards were starving, so they could not get access to the channel.
而这些研究人员观察到的是，这张Wi-Fi网卡当时[正在获得／obtained形式，待听辨]非常、非常高的吞吐量；那意味着发送大量数据的能力，而其他Wi-Fi网卡则处于饥饿状态，所以它们无法接入信道。
   来源：Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 18–21, absolute 4660.40–4692.22s；Unprompted Whisper medium.en raw: chunk-027, segments 1–3, absolute 4665.00–4690.20s
   限制：was obtaining保留历史、Qwen及medium27的进行时；medium26重叠为was obtained，登记待听辨但不把同一内容重复写两遍。
2. A very unfair service, and this is because, this was because that commercial Wi-Fi card at that time did not implement the post-backoff procedure.
一种非常不公平的服务，而这是因为，当时这是因为，那张商业Wi-Fi网卡在那个时候没有实现发送后退避程序。
   来源：Feishu historical snapshot: source_index=79, id=163, section anchor 01:17:42；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-026, segments 21–22, absolute 4683.38–4694.20s；Unprompted Whisper medium.en raw: chunk-027, segments 3–5, absolute 4681.32–4708.56s
   限制：保留is because → was because自我修正与at that time限定；post-backoff procedure据post pickoff/prospect of近音规范。

## 66 · 01:18:22 · 发送后退避的强制性与开销示例

稳定块ID：doxcn61liWTicB4PpLe3q93NYVc
原块SHA256：e0013ddf3419b4abf5ddc0ddd76209a149bd663b9dbfd6c500fc84ba3e673193
候选SHA256：400ce9ec4d9803ac47d5e77965eb2848289805f0ffc7e351e283b75ed1bb8c75

### 具体修改

1. 原：This seems like a detail, or one more thing that a node has to do, but it is extremely important for fairness. In Wi-Fi we want to be fair and give everyone the same probability of channel access. It is a very important feature.
   候选：So this seems to be, you know, a detail or one more thing that a node has to do, but it's actually extremely important to ensure fairness. In Wi-Fi, we want to be fair, we want to give the same probability to everyone in channel access. So it is a very important feature,
   理由：恢复So、seems to be、you know、actually、ensure、we want重复及to everyone in channel access；不精炼改写。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 5–6, absolute 4699.64–4716.60s；Unprompted Whisper medium.en raw: chunk-027, segments 6–7, absolute 4708.56–4725.66s；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 7–9, absolute 4716.60–4751.78s
2. 原：Notice that the same would happen without post-backoff even if A had no packet immediately after successfully completing its dialogue. Even if it got a packet a few microseconds later, it would still have an advantage over B and C, who must run backoff.
   候选：and notice that the same would happen if we didn't have the post-backoff procedure. Even if A, right after its, [its unclear] completion, successful completion of, [of unclear] its dialogue, didn't have any packet. But even in the case where it gets a packet right after, [a unclear] few microseconds after, [it / you unclear] will still get an advantage [with unclear] respect to B and C, who must run the backoff.
   理由：恢复if we didn't have、procedure、Even if A原停顿与completion自修、right after/few microseconds after重复、gets/will still get原时态、the backoff；标记its/of、代词及with冲突。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 7–9, absolute 4716.60–4751.78s；Unprompted Whisper medium.en raw: chunk-027, segments 9–10, absolute 4738.30–4759.68s；Unprompted Whisper medium.en raw: chunk-027, segments 10–12, absolute 4752.58–4781.04s
3. 原：That's why the standard says: no matter what the state of your MAC queue is, once you complete a transmission successfully, you must run post-backoff. It is mandatory; we cannot do otherwise.
   候选：So that's why the standard says, no matter what your MAC queue state is, we don't care. Once you complete a transmission successfully, you must run the post-backoff procedure, [right / okay unclear]? So that's, [it's unclear] that's mandatory. We cannot do [anything otherwise / any, any number one unclear].
   理由：恢复So、原词序your MAC queue state、删去的we don't care、procedure、So that's自修、句尾right/okay和anything otherwise残片；明确medium这里大段漏识别，不拿压缩旧稿补证。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 12–13, absolute 4771.14–4810.36s；Unprompted Whisper medium.en raw: chunk-027, segments 13–13, absolute 4781.04–4810.36s
4. 原：Help me out here. Do we have the long break now? No, sorry. Our time... [number unclear]. Okay, thanks.
   候选：Help me out here. We, [we unclear] have the long break now? [No / oh unclear], sorry. Our time [three five, five plus three; numbers unclear]. Okay, thanks.
   理由：恢复We have原词序与可能重复，记录No/oh冲突，保留原ASR数字碎片但不解释成课间安排；原稿省略号此处是existing_english真实字符。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 14–14, absolute 4810.36–4815.20s；Unprompted Whisper medium.en raw: chunk-027, segments 15–15, absolute 4816.52–4817.22s
5. 原：We still have about fifteen minutes. Let me know if I get it wrong, please; I need to adjust the schedule.
   候选：Okay, so we still have about fifteen minutes before. Let me know if I [get it wrong / get this one wrong / did something wrong unclear], please. I need to adjust the, [the unclear] schedule, of course.
   理由：恢复Okay so、before、of course及可能的the重复；if I后的三种措辞逐处待听辨，不省略限定。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 16–16, absolute 4817.80–4822.84s；Unprompted Whisper medium.en raw: chunk-027, segments 17–17, absolute 4823.14–4825.50s；Unprompted Whisper medium.en raw: chunk-027, segments 18–18, absolute 4826.36–4830.72s
6. 原：We have essentially gone through all these slides, using the whiteboard for greater clarity, but the essential information is also in the slides. What I would like to show now is another example presented here. Don't get scared by the many figures in these slides.
   候选：Okay, so we run essentially through all these slides, using the whiteboard for greater clarity, but you have the essential information also in, [in unclear] the slides. Okay, so what I would like to show now is another example that is here presented in [the / these unclear] slides. Don't get scared by the many figures that are used in these, [in these unclear] slides.
   理由：撤销have gone、the information is改写，恢复we run、you have、Okay so、that is here presented及in these重复；the/these不强选。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 19–21, absolute 4832.70–4847.90s；Unprompted Whisper medium.en raw: chunk-028, segments 1–1, absolute 4845.00–4854.86s；Unprompted Whisper medium.en raw: chunk-027, segments 22–23, absolute 4849.10–4858.34s；Unprompted Whisper medium.en raw: chunk-028, segments 1–2, absolute 4845.00–4861.34s；Unprompted Whisper medium.en raw: chunk-027, segments 24–24, absolute 4858.56–4865.64s；Unprompted Whisper medium.en raw: chunk-028, segments 2–3, absolute 4854.86–4869.20s
7. 原：They just highlight something we already know, but here you have a concrete example to emphasize it further. We now know more or less how the basic version of Wi-Fi works.
   候选：It's just to highlight something that we already know, but here you have indeed concrete example to further emphasize this. That is, we now know more or less how the basic version of Wi-Fi works.
   理由：恢复It's just to、that、indeed及That is，去掉原校订补出的a，并保留this指代和原句词序。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 25–25, absolute 4867.20–4874.92s；Unprompted Whisper medium.en raw: chunk-028, segments 3–5, absolute 4861.34–4886.14s；Unprompted Whisper medium.en raw: chunk-028, segments 5–6, absolute 4878.50–4893.94s
8. 原：We already said Wi-Fi is so successful because it works quite well for our needs, but it has a big problem in general: overhead. We already commented on that. Now that we know how the channel is used in Wi-Fi, this practical example gives evidence of it.
   候选：We already said that Wi-Fi is so successful because it works quite well for our needs. But it has got a big problem in general, that is overhead, right? We already commented on that. So now that we know how channel is used in Wi-Fi, this is a practical example that gives evidence to that.
   理由：恢复that、has got、that is、right、So、this is a practical example that gives evidence to that；不补how channel中的冠词。
   来源：Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 6–7, absolute 4886.14–4897.34s；Unprompted Whisper medium.en raw: chunk-028, segments 8–9, absolute 4897.98–4904.22s；Unprompted Whisper medium.en raw: chunk-028, segments 10–10, absolute 4904.28–4906.22s；Unprompted Whisper medium.en raw: chunk-028, segments 11–12, absolute 4906.62–4917.88s

### 逐单元证据

1. So this seems to be, you know, a detail or one more thing that a node has to do, but it's actually extremely important to ensure fairness.
所以，这似乎是，你知道，一个细节，或者一个节点必须多做的一件事，但它实际上对于保证公平性极其重要。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 5–6, absolute 4699.64–4716.60s
   限制：a node由medium明确识别；Feishu I know that、Qwen and no that为近音残片。保留you know、actually及ensure，不压缩成for fairness。
2. In Wi-Fi, we want to be fair, we want to give the same probability to everyone in channel access.
在Wi-Fi中，我们想要公平，我们想在信道接入方面给予每个人相同的概率。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 6–7, absolute 4708.56–4725.66s
3. So it is a very important feature, and notice that the same would happen if we didn't have the post-backoff procedure.
所以，这是一个非常重要的特性，而且注意，如果我们没有发送后退避程序，同样的情况就会发生。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=42, absolute 4620.00–4740.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 7–9, absolute 4716.60–4751.78s
   限制：历史now is that由Qwen与medium完整notice that支持作近音规范。post-backoff规范自post pickoff/postback/post-bacov。
4. Even if A, right after its, [its unclear] completion, successful completion of, [of unclear] its dialogue, didn't have any packet.
即便A，恰好在它的、[它的，重复待听辨]完成之后，成功完成了、[了，of重复待听辨]它的对话之后，没有任何数据包。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 9–10, absolute 4738.30–4759.68s
   限制：completion → successful completion三类文本均见；第二个its、of只见历史Feishu，不能认证为口语重复，也不直接删去。此处保留even if不完整句。
5. But even in the case where it gets a packet right after, [a unclear] few microseconds after, [it / you unclear] will still get an advantage [with unclear] respect to B and C, who must run the backoff.
但即便在它随即收到一个数据包的情况下，几微秒之后，[few前的a待听辨]，[它／你，待听辨]相对于B和C仍会得到一个优势，[with是否存在待听辨]，而B和C必须执行退避。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 10–12, absolute 4752.58–4781.04s
   限制：保留right after、few microseconds after重复及must；medium有a、you、with，历史/Qwen无a、it、respect to。backoff规范自vehicle/record近音，不把优势改写成抽象summary。
6. So that's why the standard says, no matter what your MAC queue state is, we don't care.
所以，这就是为什么标准说，不管你的MAC队列处于什么状态，我们不在乎。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 12–13, absolute 4771.14–4810.36s
   限制：MAC queue state规范自mark/max queue/max Q-step the state；medium在此有长段遗漏，不据其分段把we don't care延伸至后面。
7. Once you complete a transmission successfully, you must run the post-backoff procedure, [right / okay unclear]?
一旦你成功完成一次发送，你就必须执行发送后退避程序，[对吧／好吧，待听辨]？
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 13–13, absolute 4781.04–4810.36s
   限制：历史Feishu完整transmission successfully ... right，Qwen为permission successfully ... Okay；medium仅到once you complete a，后续遗漏到4810.36秒。transmission及post-backoff为技术近音规范，句尾词冲突待听辨；后半句不能声称由新medium确认。
8. So that's, [it's unclear] that's mandatory.
所以，那是，[它是，待听辨]，那是强制的。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   限制：Qwen为So that's that's mandatory；历史为So that's it's that's manual。mandatory由Qwen支持并对应历史manual近音；it's仅历史，保留待听辨。新medium漏掉。
9. We cannot do [anything otherwise / any, any number one unclear].
我们不能[用其他方式做任何事／any, any number one残片，待听辨]。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   限制：历史We cannot do anything otherwise；QwenWe cannot do any any number one；medium整句遗漏。不能强选或把残片润色成标准英语。
10. Help me out here.
在这里帮我一下。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   限制：历史与Qwen完整支持；medium在4781.04–4810.36秒漏掉本句及相邻课间问句。
11. We, [we unclear] have the long break now?
我们，[我们，重复待听辨]现在要放长课间了吗？
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output
   限制：Qwen为We we have，历史为We have；新medium遗漏。保留陈述词序作提问，不补旧校订的Do。
12. [No / oh unclear], sorry.
[不／哦，待听辨]，抱歉。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 14–14, absolute 4810.36–4815.20s
   限制：历史/Qwen No sorry；medium Oh sorry。
13. Our time [three five, five plus three; numbers unclear].
我们的时间[three five, five plus three；数字及其含义待听辨]。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 14–14, absolute 4810.36–4815.20s
   限制：三类来源均仅转出three five, five plus three一类碎片。不得据此推断13:55、15:35、五分钟加三分钟或任何课间安排。
14. Okay, thanks.
好，谢谢。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 15–15, absolute 4816.52–4817.22s
15. Okay, so we still have about fifteen minutes before.
好，所以在那之前我们还有大约十五分钟。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 16–16, absolute 4817.80–4822.84s
   限制：三类来源均保留fifteen minutes及before；before的参照对象未说清，不补课间具体起止时间。
16. Let me know if I [get it wrong / get this one wrong / did something wrong unclear], please.
如果我[弄错了／把这一次弄错了／做错了什么，待听辨]，请告诉我。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 17–17, absolute 4823.14–4825.50s
   限制：历史get it wrong，Qwen did something wrong，medium get this one wrong；未用旧稿覆盖冲突。
17. I need to adjust the, [the unclear] schedule, of course.
当然，我需要调整这个、[这个，重复待听辨]时间安排。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 18–18, absolute 4826.36–4830.72s
   限制：I由Qwen及medium保留，历史开头省略；第二个the仅Qwen。
18. Okay, so we run essentially through all these slides, using the whiteboard for greater clarity, but you have the essential information also in, [in unclear] the slides.
好，所以我们基本上讲过了所有这些幻灯片，为了更清楚而使用了白板，但你们在、[在，重复待听辨]幻灯片中也有这些基本信息。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=43, absolute 4730.00–4850.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 19–21, absolute 4832.70–4847.90s；Unprompted Whisper medium.en raw: chunk-028, segments 1–1, absolute 4845.00–4854.86s
   限制：保留we run现在形式、you have及also词位，不改have gone；第二个in只见Qwen43，44为重叠窗口，不重复拼接。
19. Okay, so what I would like to show now is another example that is here presented in [the / these unclear] slides.
好，所以我现在想展示的是在这里的[这些／该组，指示词待听辨]幻灯片中呈现的另一个例子。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 22–23, absolute 4849.10–4858.34s；Unprompted Whisper medium.en raw: chunk-028, segments 1–2, absolute 4845.00–4861.34s
   限制：历史/Qwen为the slides，medium两窗为these slides；恢复完整what I would like及that is here presented。
20. Don't get scared by the many figures that are used in these, [in these unclear] slides.
不要被这些、[这些，in these重复待听辨]幻灯片中使用的许多图示吓到。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 24–24, absolute 4858.56–4865.64s；Unprompted Whisper medium.en raw: chunk-028, segments 2–3, absolute 4854.86–4869.20s
   限制：历史及Qwen有in these in these，medium仅一次；标出重复而不平滑删去。figures不在无图的情况下限定为数字。
21. It's just to highlight something that we already know, but here you have indeed concrete example to further emphasize this.
这只是为了突出我们已经知道的某件事，但在这里，你们确实有一个具体的例子，来进一步强调这一点。
   来源：Feishu historical snapshot: source_index=80, id=165, section anchor 01:18:22；Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-027, segments 25–25, absolute 4867.20–4874.92s；Unprompted Whisper medium.en raw: chunk-028, segments 3–5, absolute 4861.34–4886.14s
   限制：恢复just、indeed、further，保留concrete example前缺冠词的口语语法；历史165/167跨段实际同一句，不额外重复here you have indeed。
22. That is, we now know more or less how the basic version of Wi-Fi works.
也就是说，我们现在或多或少知道Wi-Fi的基本版本是如何工作的。
   来源：Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 5–6, absolute 4878.50–4893.94s
23. We already said that Wi-Fi is so successful because it works quite well for our needs.
我们已经说过，Wi-Fi如此成功，是因为它能相当好地满足我们的需求。
   来源：Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 6–7, absolute 4886.14–4897.34s
24. But it has got a big problem in general, that is overhead, right?
但总的来说，它有一个大问题，那就是开销，对吧？
   来源：Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 8–9, absolute 4897.98–4904.22s
25. We already commented on that.
我们已经就此作过评论。
   来源：Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 10–10, absolute 4904.28–4906.22s
26. So now that we know how channel is used in Wi-Fi, this is a practical example that gives evidence to that.
所以，既然我们现在知道在Wi-Fi中信道是怎样被使用的，这就是为这一点提供证据的一个实际例子。
   来源：Feishu historical snapshot: source_index=81, id=167, section anchor 01:18:22；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 11–12, absolute 4906.62–4917.88s
   限制：保留how channel的口语缺冠词，不补the；止于4917.88秒，不吞入下一段So we know that。

## 67 · 01:21:58 · DIFS、物理前导码与各层首部开销

稳定块ID：doxcnZ562lYsPjFnhaKLUa6k3pf
原块SHA256：a0d2961fffd810c43a87db58b23ef582d1e3694d4f638989fa738150e3567cf0
候选SHA256：bb31e5b725fdcf0ac152efed21d7f4d9f50f5022912750ec556cf7ae5e10e518

### 具体修改

1. 原：When we need to transmit a data packet, first we sense the channel for DIFS. We can consider DIFS to be fifty microseconds long. That is certainly time we need to wait.
   候选：So we know that in the case where we need to transmit [the / a unclear] data packet, first of all we need to sense the channel for DIFS. We can consider [DIFS / this unclear] to be fifty microseconds long. So that's for sure something that we need to wait for.
   理由：恢复So we know that in the case where、first of all we need to、So that's for sure something ... for；冠词及DIFS/this不强选。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 13–15, absolute 4918.14–4931.74s；Unprompted Whisper medium.en raw: chunk-028, segments 15–16, absolute 4923.16–4938.60s；Unprompted Whisper medium.en raw: chunk-028, segments 16–16, absolute 4931.74–4938.60s
2. 原：If we are lucky, if we are lucky, the channel is idle and we can transmit our packet right away. But the packet has headers.
   候选：Then if we are lucky, if we are lucky, the channel is idle, and we can transmit our packet right away. But the packet that we transmit, we [know already / already know unclear] that [it unclear] has got some headers, right?
   理由：恢复Then及But the packet that we transmit整句、we know already、has got some和right，不摘要替代句子；know/already词序和it待听辨。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 16–18, absolute 4931.74–4953.50s；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 18–19, absolute 4946.42–4958.94s
3. 原：We already said it has a physical-layer preamble used by transmitter and receiver to synchronize, so the receiver can start demodulating what the transmitter sends. At the electronics level, they need this preamble to start the communication.
   候选：Actually, we already said it has got a physical layer preamble that is used by the transmitter and receiver to essentially synchronize, and so that the receiver can start [to unclear] demodulating what the transmitter is sending. So at the electronics level, they need this preamble to start the, [the, let's see unclear] communication.
   理由：恢复Actually、has got、that is used、essentially、and so that、is sending进行时、So；标出历史start to demodulating和Qwen独有the the let's see。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 19–22, absolute 4953.50–4982.90s；Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Unprompted Whisper medium.en raw: chunk-028, segments 22–22, absolute 4971.46–4982.90s
4. 原：Then there is the physical-layer header, and then the physical—sorry, the MAC-layer header, where, for example, we have the Duration field. All these headers are just control information. They are not the payload.
   候选：And then there is the physical layer header, and then there is the physical, sorry, the MAC layer header, where we have, for example, the duration field. So all these headers are just control information. It's not [a / the unclear] payload.
   理由：恢复And、第二次there is、原where we have for example词序、So及It's单数；a/the payload冲突不按标准英语选择。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 23–24, absolute 4983.80–4995.74s；Unprompted Whisper medium.en raw: chunk-028, segments 25–25, absolute 4996.94–5004.04s
5. 原：It's not something useful at the MAC layer. It is useful for the protocol, but these are not application-layer bits. They are there, fine, but from the application's perspective they are not useful or interesting.
   候选：It's not something useful at the MAC layer. It is something that is there. It is useful for the protocol, but not, they are not application layer bits, right? So [they are / you're unclear] there, fine, but from the application, from what would be the application layer perspective, that's something that is not useful, it's not interesting.
   理由：补回完全删掉的It is something that is there，恢复but not、they are、right、So及from the application自修长结构；保留MAC layer原技术说法，代词冲突待听辨。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–26, absolute 4996.94–5012.44s；Unprompted Whisper medium.en raw: chunk-028, segments 26–26, absolute 5004.04–5012.44s；Unprompted Whisper medium.en raw: chunk-028, segments 26–27, absolute 5004.04–5020.40s；Unprompted Whisper medium.en raw: chunk-028, segments 27–29, absolute 5012.44–5033.84s；Unprompted Whisper medium.en raw: chunk-029, segments 1–1, absolute 5025.00–5033.86s

### 逐单元证据

1. So we know that in the case where we need to transmit [the / a unclear] data packet, first of all we need to sense the channel for DIFS.
所以，我们知道，在我们需要发送[这个／一个，待听辨]数据包的情况下，首先我们需要侦听信道一个DIFS的时间。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 13–15, absolute 4918.14–4931.74s
   限制：历史及medium为the data packet，Qwen为a data packet；DIFS据历史dips及其他this近音规范，不压缩成When we need。
2. We can consider [DIFS / this unclear] to be fifty microseconds long.
我们可以认为[DIFS／这个，待听辨]持续五十微秒。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 15–16, absolute 4923.16–4938.60s
   限制：数字50三类均有，不引入其他制式数值；历史为dips，Qwen/medium为this，可能术语亦可能代词，保持词冲突。
3. So that's for sure something that we need to wait for.
所以，那肯定是我们需要等待的一段时间。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 16–16, absolute 4931.74–4938.60s
4. Then if we are lucky, if we are lucky, the channel is idle, and we can transmit our packet right away.
然后，如果我们幸运，如果我们幸运，信道是空闲的，我们就可以立即发送我们的数据包。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 16–18, absolute 4931.74–4953.50s
5. But the packet that we transmit, we [know already / already know unclear] that [it unclear] has got some headers, right?
但是，我们发送的这个数据包，我们[已经知道，know与already词序待听辨]，[it是否存在待听辨]它有一些首部，对吧？
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=44, absolute 4840.00–4960.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 18–19, absolute 4946.42–4958.94s
   限制：历史we already know；Qwen44与medium we know already that has；Qwen45重叠为we know already that it has。不把两个重叠窗口拼接成重复发言。
6. Actually, we already said it has got a physical layer preamble that is used by the transmitter and receiver to essentially synchronize, and so that the receiver can start [to unclear] demodulating what the transmitter is sending.
实际上，我们已经说过，它有一个物理层前导码，由发送方和接收方用来基本上实现同步，并使接收方能够开始[to是否存在待听辨]解调发送方正在发送的内容。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 19–22, absolute 4953.50–4982.90s
   限制：恢复Actually、has got、essentially及and so that；历史start to demodulating，Qwen与medium start demodulating。transmitter is sending由Qwen明确识别，历史/medium尾部近音破碎，保留此候选并注明不是听音认证。
7. So at the electronics level, they need this preamble to start the, [the, let's see unclear] communication.
所以，在电子电路层面，它们需要这个前导码来开始这、[这，让我们看看，待听辨]通信。
   来源：Feishu historical snapshot: source_index=82, id=169, section anchor 01:21:58；Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 22–22, absolute 4971.46–4982.90s
   限制：Qwen独有the the let's see，历史及medium只一次the且无let's see；不将Qwen单源口头填充当已确认。
8. And then there is the physical layer header, and then there is the physical, sorry, the MAC layer header, where we have, for example, the duration field.
然后有物理层首部，接着有物理，抱歉，MAC层首部，其中我们有，例如，时长字段。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 23–24, absolute 4983.80–4995.74s
   限制：保留physical → sorry → MAC自修及两次and then there is；field在Qwen及medium明确，历史至duration。
9. So all these headers are just control information.
所以，所有这些首部都只是控制信息。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–25, absolute 4996.94–5004.04s
10. It's not [a / the unclear] payload.
它不是[一个／该，冠词待听辨]有效载荷。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–25, absolute 4996.94–5004.04s
   限制：历史the payload；Qwen与medium a payload。保留单数It's，不改成They。
11. It's not something useful at the MAC layer.
它不是在MAC层有用的东西。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 25–26, absolute 4996.94–5012.44s
   限制：讲者原话的MAC layer保留；不因其下一句讨论application layer而代改。
12. It is something that is there.
它是存在在那里的某种东西。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 26–26, absolute 5004.04–5012.44s
13. It is useful for the protocol, but not, they are not application layer bits, right?
它对协议是有用的，但不是，它们不是应用层的比特，对吧？
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 26–27, absolute 5004.04–5020.40s
   限制：保留but not口语转折残片与right；没有补造主语these或删掉自修。
14. So [they are / you're unclear] there, fine, but from the application, from what would be the application layer perspective, that's something that is not useful, it's not interesting.
所以，[它们／你，待听辨]在那里，好吧，但从应用，从所谓的应用层角度来看，那是没有用的东西，是没有意思的东西。
   来源：Feishu historical snapshot: source_index=83, id=171, section anchor 01:21:58；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 27–29, absolute 5012.44–5033.84s；Unprompted Whisper medium.en raw: chunk-029, segments 1–1, absolute 5025.00–5033.86s
   限制：历史they're there、Qwenthey are there，medium28 you're there；保留from the application → from what would be the application layer perspective自修和重复not，不压成application's perspective。medium29只是跨窗尾部，不额外拼接。

## 68 · 01:23:51 · 基本速率发送前导码和首部

稳定块ID：doxcnBiFI1L4BIG5iB170r9SIdd
原块SHA256：60eac5cf731d29b7215135bd8514d1e99aaff9df0aa9f04d543360bc750c844f
候选SHA256：2eb18a64a2e8cd6026fc110f6e72f1b4695a1d3b3a21c410c48b0fd41c3c3b02

### 具体修改

1. 原：We spend time transmitting this physical-layer preamble and header, and they are transmitted at the basic rate.
   候选：Okay. So, [but / when unclear] we spend time to transmit [this / these unclear] physical layer preamble, physical layer header, and they are transmitted at the basic rate.
   理由：恢复Okay、So but/when、spend time to transmit、physical layer header重复全称；this/these不强选。
   来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 29–31, absolute 5025.18–5047.42s；Unprompted Whisper medium.en raw: chunk-029, segments 1–3, absolute 5025.00–5047.80s
2. 原：As we already commented, the basic rate is a low speed, so they are transmitted slowly.
   候选：So as we commented already, the basic rate is a low speed. So they are transmitted slowly at low speed.
   理由：恢复两次So、as we commented already原词序及被删除的at low speed，保留口语重复。
   来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 31–32, absolute 5040.56–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 3–4, absolute 5041.36–5057.02s；Unprompted Whisper medium.en raw: chunk-028, segments 32–32, absolute 5047.42–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 4–4, absolute 5047.80–5057.02s
3. 原：If, as in this example, the basic rate is one megabit per second, you have to wait; this takes time. Then we have the MAC header.
   候选：And if you consider the basic rate, like in this example, to be one megabit per second, well then you have to wait; it takes time to do that. And then we have the MAC header.
   理由：恢复And if you consider、like in this example、to be、well then、it takes time to do that和And then，不压成客观陈述。
   来源：Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 4–6, absolute 5047.80–5074.76s；Unprompted Whisper medium.en raw: chunk-029, segments 6–6, absolute 5064.78–5074.76s

### 逐单元证据

1. Okay.
好。
   来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output
   限制：Okay在历史Feishu及Qwen45出现，新medium两窗均未转出。
2. So, [but / when unclear] we spend time to transmit [this / these unclear] physical layer preamble, physical layer header, and they are transmitted at the basic rate.
所以，[但是／当，待听辨]我们花时间来发送[这个／这些，待听辨]物理层前导码、物理层首部，而它们是以基本速率发送的。
   来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 29–31, absolute 5025.18–5047.42s；Unprompted Whisper medium.en raw: chunk-029, segments 1–3, absolute 5025.00–5047.80s
   限制：历史/Qwen So but，medium两窗So when；历史these，Qwen/mediumthis。保留spend time to transmit及重复physical layer，不用流畅性强选。
3. So as we commented already, the basic rate is a low speed.
所以，正如我们已经评论过的，基本速率是一个低速率。
   来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 31–32, absolute 5040.56–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 3–4, absolute 5041.36–5057.02s
4. So they are transmitted slowly at low speed.
所以，它们被慢慢地以低速率发送。
   来源：Feishu historical snapshot: source_index=84, id=173, section anchor 01:23:51；Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-028, segments 32–32, absolute 5047.42–5053.46s；Unprompted Whisper medium.en raw: chunk-029, segments 4–4, absolute 5047.80–5057.02s
   限制：恢复slowly及at low speed同义重复；at有历史及medium29明确支持，Qwen/medium28为a low speed近音，不当成重复发言。
5. And if you consider the basic rate, like in this example, to be one megabit per second, well then you have to wait; it takes time to do that.
而且，如果你认为基本速率，像这个例子中一样，是每秒一兆比特，那么，嗯，你就必须等待；做这件事需要时间。
   来源：Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 4–6, absolute 5047.80–5074.76s
   限制：历史Feishu本段止于low speed；此例及one megabit per second由Qwen45、46重叠及medium29支持，不把Qwen46截断A bit per second另算新句。
6. And then we have the MAC header.
然后我们还有MAC首部。
   来源：Qwen recovery rerun raw: window_index=45, absolute 4950.00–5070.00s; recovery rerun, not lost first output；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 6–6, absolute 5064.78–5074.76s
   限制：本句结束本段；其后The MAC header again are属于69段开头，避免Qwen45尾部或medium6跨段造成机械重复。

## 69 · 01:24:28 · MAC首部长度随地址需求变化

稳定块ID：doxcnaPSN6RL8HcSamaAISyuJqf
原块SHA256：47c0214dc5c65b426abe8c2f9335c70f9f329bb9bff182ee2009e7157e463002
候选SHA256：1046d723397bc083fefd51fac250f356e6c2ed0e591c4b10f0fa17bfef2a4af7

### 具体修改

1. 原：Again, the MAC header consists of uninteresting bits from the application's point of view.
   候选：The MAC header again are, [I would say / we say / it's a unclear] non-interesting bits from the point of view of the application.
   理由：撤销consists of语法修补及uninteresting同义替换，恢复The MAC header again are、non-interesting、from the point of view of the application；口头插入词三源冲突逐字保留。
   来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 6–7, absolute 5064.78–5079.76s
2. 原：Its size in Wi-Fi may vary, depending, for example, on how many addresses you need.
   候选：The size of the MAC header in Wi-Fi may actually vary, depending on, for example, how many addresses you need.
   理由：恢复The size of the MAC header全称、actually及depending on, for example原词序。
   来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 7–9, absolute 5074.76–5094.32s
3. 原：If you are in an isolated BSS, like the one in your apartment, the only addresses you need are the transmitter and receiver addresses.
   候选：So if you are in a BSS, isolated BSS, as the one that you have got in your apartment, the only addresses that you need are the transmitter address and [a unclear] receiver address.
   理由：恢复So、a BSS, isolated BSS重复、as the one that you have got、that及重复address；接收方地址前a待听辨，不改讲者两地址简化。
   来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 9–11, absolute 5086.80–5109.56s

### 逐单元证据

1. The MAC header again are, [I would say / we say / it's a unclear] non-interesting bits from the point of view of the application.
MAC首部又是，[我会说／我们说／它是一个，待听辨]，从应用的角度来看没有意思的比特。
   来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 6–7, absolute 5064.78–5079.76s
   限制：保留header are的讲者语法；历史we say，Qwenit's a，mediumI would say，均不可据语义强选；不润色成consists of uninteresting。
2. The size of the MAC header in Wi-Fi may actually vary, depending on, for example, how many addresses you need.
Wi-Fi中的MAC首部大小实际上可能会变化，这取决于，例如，你需要多少个地址。
   来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 7–9, absolute 5074.76–5094.32s
   限制：MAC由历史/Qwen明确，mediummount为近音；保留actually、完整The size of the MAC header及on。
3. So if you are in a BSS, isolated BSS, as the one that you have got in your apartment, the only addresses that you need are the transmitter address and [a unclear] receiver address.
所以，如果你处在一个BSS中，一个孤立的BSS，就像你公寓里有的那一个，你需要的地址就只有发送方地址和[一个，a是否存在待听辨]接收方地址。
   来源：Feishu historical snapshot: source_index=85, id=175, section anchor 01:24:28；Qwen recovery rerun raw: window_index=46, absolute 5060.00–5180.00s; recovery rerun, not lost first output；Unprompted Whisper medium.en raw: chunk-029, segments 9–11, absolute 5086.80–5109.56s
   限制：三类原始文本均写VSS，此处按既有稿BSS及basic/extended service set语境作B/V技术近音规范，不能视为音频确认。保留a BSS, isolated BSS重复和as the one；a receiver在历史及medium有，Qwen无，留待听辨。you've got/you have got仅缩合差异，以展开词形显示。讲者关于孤立BSS只需两地址的简化原样保留，不能暗改为规范地址数量。

## 70 · 01:25:04 · 扩展服务集中的四地址需求

稳定块ID：doxcne0VOVXpSN5fpm81zBk9gpc
原块SHA256：f8dcca481b3309a1847f05ff47868face47e35e768a11c7b046fb7e399786de0
候选SHA256：64e220bca3a0f2aef084ca84fc1a1d69c485abd4e4882e07f6e9d651063deab4

### 具体修改

1. 原：like on the Tongji campus
   候选：like here on Tongji campus [place-introduction wording unclear]
   理由：恢复地点引入词的可能措辞，不用现稿流畅表达替代；差异标疑。
   来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5100–5121.72s
2. 原：with many access points connected through the wired network
   候选：where we have many access points connected through, you know, the, the wired network
   理由：恢复where we have、you know和the,the重复。
   来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46
3. 原：The reason is that, in an extended service set, we may have access points connected to each other.
   候选：and the reason for that is that, in an extended service set, you may have, as we know, access points that are connected to each other, right?
   理由：恢复for that、you、as we know、that are、right及原长句结构。
   来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5121.72–5150.32s

### 逐单元证据

1. If you are in an extended service set, like here on Tongji campus [place-introduction wording unclear], where we have many access points connected through, you know, the, the wired network.
如果你处在一个扩展服务集里，就像这里的同济校园〔引出地点的措辞待听辨〕，这里我们有许多接入点，通过，你知道的，这个、这个有线网络连接起来。
   来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5100.02–5121.72s
   限制：Tongji由Feishu与新medium支持；here on是新medium，Feishu your on、Qwen your Monton G近音不清。you know/the,the由Feishu与Qwen保留，新medium省略。
2. Then you may need four different addresses, and the reason for that is that, in an extended service set, you may have, as we know, access points that are connected to each other, right?
那么你可能需要四个不同的地址，而其原因是，在一个扩展服务集中，你可能有，正如我们所知道的，彼此连接的接入点，对吧？
   来源：Feishu historical snapshot 08e6132, original source paragraph 87；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5121.72–5150.32s
   限制：保留讲者关于四地址的解释；不在正文把它改写为标准适用范围说明。
3. We already explained the architecture of the network.
我们已经解释过这个网络的架构。
   来源：Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5142.28–5150.32s

## 71 · 01:25:52 · 数据包经两个接入点交付

稳定块ID：doxcnq3VlLHsxPBYm8fqFaxRdCf
原块SHA256：ddfb6ba20961124445fa6aeda3f62f07121fdd3f880b7b8e5855c7d551c352d9
候选SHA256：fec0735a490289837920c1866ed733dc46ca350ddc56a4e8387139a4722d0b0d

### 具体修改

1. 原：You are A, and you want to send a packet to B. You send it to the access point you are connected to.
   候选：And so, if you are A and you want to send a packet to B, well, then you have to send your packet to the access point you are connected with.
   理由：恢复And so if条件、well/then、have to、your packet和with，不用简写send it。
   来源：Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5142–5167s
2. 原：Access point one sends it to access point two, and access point two delivers it to B.
   候选：This access point one will send the packet to access point two, and then access point two will deliver the packet to B.
   理由：恢复This、两次will、then及重复the packet。
   来源：Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5160–5183s

### 逐单元证据

1. And so, if you are A and you want to send a packet to B, well, then you have to send your packet to the access point you are connected with.
所以，如果你是A，并且你想把一个数据包发送给B，嗯，那么你必须把你的数据包发送给与你连接的那个接入点。
   来源：Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；new unprompted medium.en chunk-029, absolute 5142.28–5167.44s
2. This access point one will send the packet to access point two, and then access point two will deliver the packet to B.
这个接入点一会把这个数据包发送给接入点二，然后接入点二会把这个数据包递送给B。
   来源：Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5160.84–5183.18s
3. This happens in an extended service set.
这发生在一个扩展服务集中。
   来源：Feishu historical snapshot 08e6132, original source paragraph 88；Qwen recovery raw commit2887ed5, window 46；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5173.86–5183.18s

## 72 · 01:26:20 · 源、发送方、接收方与目的地址

稳定块ID：doxcn57rutxrKFZjcBVeZsksgmf
原块SHA256：f930152bb48a96a38cb4b9b0ca850264d7101660ffe323f3fcd5e407f2706a38
候选SHA256：57311a6dfcdde5d77f743a698ebd6a4189abcc0e8c44187bd5d464ee77754188

### 具体修改

1. 原：In this case A is the sender, the transmitter, so it is the original source and also the transmitter of the packet.
   候选：Okay, now in this case, A is the sender, okay, the transmitter
   理由：恢复Okay/now及原口语插语，the/your原始限定词冲突标疑。
   来源：Feishu historical snapshot 08e6132, original source paragraph 89；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5173–5200s
2. 原：It has access point one's address as the receiver address, and B's address as the destination address.
   候选：You will have access point one address as a receiver, and then you will have the destination address, the B's address as destination address.
   理由：恢复You will have、then、重复destination address和原语法，不压成It has。
   来源：Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5219–5241s
3. 原：Once the packet is received at access point one, that access point has to send it to access point two so that it eventually can be delivered to the final destination.
   候选：Once the packet is received at access point one, [and unclear] access point one has to send the packet to access point two, so that the packet eventually can be delivered to the final destination.
   理由：补句由旧Qwen和新medium支持；恢复重复名词，不替换为that access point/it；and异文标疑。
   来源：Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5241–5266s
4. 原：Here the packet needs four addresses in the header.
   候选：This packet, when the packet is here, it [needs/means/names unclear] four addresses in the [MAC unclear] header.
   理由：恢复重复主语和when从句；动词及MAC冲突不靠标准表述裁定。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5259–5276s
5. 原：The transmitter now is access point one, the receiver is access point two, and the final destination is B.
   候选：The transmitter now is access point one. The receiver now is access point two. And the final destination where this packet has to go is B, right?
   理由：恢复第二个now、where this packet has to go及尾问。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5276–5308s
6. 原：Anyway, you already have to account for DIFS, the physical preamble, physical header, and MAC header.
   候选：Anyway, [um unclear], so you already have to account for [DIFS/SIFS unclear], physical preamble, physical header, MAC header.
   理由：恢复so与单源um疑点；DIFS/SIFS来源冲突不能按技术预期强选。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5327–5344s
7. 原：The payload is the useful, interesting part, so it is not overhead.
   候选：The payload is the useful, interesting part. [Okay, so that's not overhead; wording unclear]
   理由：保留已支持的payload句，not overhead只有旧Qwen近音孤证，改为待听辨而非确认事实。
   来源：Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5337–5355s

### 逐单元证据

1. Okay, now in this case, A is the sender, okay, the transmitter, so it's [the/your unclear] original source and also transmitter of the packet.
好，现在在这种情况下，A是发送方，好，发送机，所以它是〔the/your，限定词待听辨〕最初的源，同时也是这个数据包的发送方。
   来源：Feishu historical snapshot 08e6132, original source paragraph 89；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5173.86–5200.4s
   限制：Feishu your original source，Qwen与medium the original source；保留词级冲突，不因your不自然而去掉。Okay由原Feishu支持。
2. And access point one is the receiver, but the final destination is B.
而接入点一是接收方，但是最终目的地是B。
   来源：Feishu historical snapshot 08e6132, original source paragraph 89；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5191.68–5211.96s
3. So, this packet that travels from A to access point one will have A as the transmitter address, which is also the source's address.
所以，这个从A传到接入点一的数据包，会把A作为发送方地址，这同时也是源的地址。
   来源：Feishu historical snapshot 08e6132, original source paragraph 89；Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-029, absolute 5200.4–5234.82s；new unprompted medium.en chunk-030, absolute 5205–5229.84s
4. You will have access point one address as a receiver, and then you will have the destination address, the B's address as destination address.
你会把接入点一的地址作为接收方地址，然后你会有目的地址，B的地址作为目的地址。
   来源：Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5219.4–5241.22s
   限制：保留as a receiver及the B’s的口语形式，不改成receiver address语法润色。
5. So it needs to have three addresses in the MAC header.
所以它需要在MAC首部中有三个地址。
   来源：Feishu historical snapshot 08e6132, original source paragraph 90；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5231.72–5252.1s
6. Once the packet is received at access point one, [and unclear] access point one has to send the packet to access point two, so that the packet eventually can be delivered to the final destination.
一旦这个数据包在接入点一被接收，〔and，连接词有无待听辨〕接入点一就必须把这个数据包发送给接入点二，这样这个数据包最终才能被递送到最终目的地。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5241.22–5266.76s
   限制：原Feishu前半句漏录；Qwen与medium补回，但medium有and、Qwen无，标疑。
7. This packet, when the packet is here, it [needs/means/names unclear] four addresses in the [MAC unclear] header.
这个数据包，当这个数据包在这里时，它〔needs/means/names，需要/意味着/说出，待听辨〕四个地址，在〔MAC有无待听辨〕首部里。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5259.4–5276.64s
   限制：Feishu it means four addresses in the header；Qwen it needs four addresses in the MAC header；medium it names four addresses in the MAC header。动词保留待听辨，MAC也记录F省略。
8. Why? Because we need to [specify/specifying unclear] that this packet originally came from source A.
为什么？因为我们需要〔specify/specifying，词形待听辨〕说明这个数据包最初来自源A。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；new unprompted medium.en chunk-030, absolute 5266.76–5287.6s
   限制：Feishu和Qwen specify，新medium specifying，不能仅为语法修掉来源词形差异。
9. The transmitter now is access point one. The receiver now is access point two. And the final destination where this packet has to go is B, right?
现在的发送方是接入点一。现在的接收方是接入点二。而这个数据包必须到达的最终目的地是B，对吧？
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 47；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5276.64–5308.94s
10. So, in extended service sets, when the Wi-Fi packets travel from one access point to another, they need four addresses.
所以，在扩展服务集中，当Wi-Fi数据包从一个接入点传到另一个接入点时，它们需要四个地址。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5298.78–5318.12s
   限制：这是讲者说法，适用范围的技术简化不在讲稿正文中悄悄改正。
11. So this is just to say that the size of the MAC header may vary, okay, may be shorter or longer.
所以这只是要说明，MAC首部的大小可能变化，好，可能更短或者更长。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5318.12–5337.26s
12. Anyway, [um unclear], so you already have to account for [DIFS/SIFS unclear], physical preamble, physical header, MAC header.
总之，〔um，语气词有无待听辨〕，所以你已经必须把〔DIFS/SIFS待听辨〕、物理层前导码、物理层首部、MAC首部计算在内。
   来源：Feishu historical snapshot 08e6132, original source paragraph 91；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5327.7–5344.82s
   限制：Feishu与medium for this可近音DIFS，Qwen明确SIFS；不能仅凭协议正确值把讲者原话裁定为DIFS。um仅Qwen有。
13. The payload is the useful, interesting part. [Okay, so that's not overhead; wording unclear]
有效载荷是有用的、有意思的部分。〔好，所以那不是开销；此句措辞待听辨〕
   来源：Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5337.26–5355.3s
   限制：payload句Qwen+medium支持；not overhead只Qwen字面not over it，原Feishu缺、medium未出。旧稿将它当确定句，现保留疑句不能声称已确认。

## 73 · 01:29:08 · 成功传输后的SIFS与确认开销

稳定块ID：doxcnoz4iNyPcVFzBZa9v02rNAb
原块SHA256：80040f79599fd97482d5f6ec76f1878712397936a08962c1a96b8700b96b41c7
候选SHA256：4ac32962394d1a46cb9c15df21e2405ba479086fbdb795fe70c8aa812cbaed18

### 具体修改

1. 原：Then, if the packet is hopefully delivered successfully, in the best case, there is SIFS, another interval you have to wait for.
   候选：But then, if the packet is hopefully, so in the best case, delivered successfully, you have SIFS.
   理由：恢复But、so、you have和原词序；另一个时间间隔的潜在重说列为独立待听辨句。
   来源：Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5344–5367s
2. 原：Then comes the acknowledgment, a control packet, so it is not interesting from the application's point of view.
   候选：And then acknowledgment, that is a control packet, so not interesting from the application point of view.
   理由：恢复原口语无主语结构及that is；不增comes/it is或所有格。
   来源：Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5360–5372s

### 逐单元证据

1. But then, if the packet is hopefully, so in the best case, delivered successfully, you have SIFS.
但是然后，如果这个数据包，希望如此，所以是在最好的情况下，被成功递送了，你会有SIFS。
   来源：Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5344.82–5360.9s
   限制：SIFS由Qwen明确、F sips与medium sieves近音共同支持；保留hopefully/so在句中的位置。
2. That is [another time interval / another time you have ... interval; wording unclear] you have to wait for.
那是〔another time interval / another time you have ... interval，另一段时间间隔及可能的起句重说，待听辨〕，你必须等过的。
   来源：Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5355.3–5367.04s
   限制：Feishu another time you have interval you have to wait for；Qwen another time you are involved. You have to wait for；medium another time interval you have to wait for，不能靠顺语法把可能的重说删除。
3. And then acknowledgment, that is a control packet, so not interesting from the application point of view.
然后是确认，那是一个控制包，所以从应用的角度看并不有意思。
   来源：Feishu historical snapshot 08e6132, original source paragraph 92；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5360.9–5372.52s

## 74 · 01:29:30 · ACK结构与一次传输的总开销

稳定块ID：doxcnjlEVlqixKzyDteKtNUUyQb
原块SHA256：54af5b9fc922f707d762a3f7d55d006c65d0151c2ff1ef500eb2fcd7ea1f4d7d
候选SHA256：4dd6bb0a7e390e65fb0eb808dbe4b601fe56d3ad22f63bd0fea577b3d4255715

### 具体修改

1. 原：The acknowledgment again is made of a physical preamble, physical header, and MAC header, so there are lots of things to transmit. That is the best case.
   候选：And the acknowledgment again is made of physical preamble, physical header, MAC header, so lots of things to be transmitted. And that's the best case.
   理由：恢复And、原列表无额外冠词/and、无主语lots of things、被动to be transmitted和缩写that’s。
   来源：Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5367–5387s
2. 原：To transmit the payload, you have to wait for DIFS, transmission of the physical-layer preamble, physical-layer header, and MAC header, then SIFS and then ACK.
   候选：So, you, to transmit the payload, you have to wait [DIFS/SIFS unclear], transmission of physical layer preamble, physical layer header, MAC header, and then SIFS, and then ACK.
   理由：恢复So you假起句及反复and then；不把DIFS按知识直接定词。
   来源：Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5380–5405s；new unprompted medium.en chunk-031, absolute 5385–5407s
3. 原：Lots of time just to transmit the payload.
   候选：[Okay unclear], lots of time to just transmit [a/the/zero-article unclear] payload.
   理由：恢复to just词序；Okay和冠词来源不一，留明确标记。
   来源：Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395–5405s；new unprompted medium.en chunk-031, absolute 5400–5407s

### 逐单元证据

1. And the acknowledgment again is made of physical preamble, physical header, MAC header, so lots of things to be transmitted. And that's the best case.
并且这个确认又由物理层前导码、物理层首部、MAC首部构成，所以有许多东西要传输。而且那还是最好的情况。
   来源：Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；new unprompted medium.en chunk-030, absolute 5367.04–5387.66s
2. So, you, to transmit the payload, you have to wait [DIFS/SIFS unclear], transmission of physical layer preamble, physical layer header, MAC header, and then SIFS, and then ACK.
所以，你，为了传输有效载荷，你必须等待〔DIFS/SIFS待听辨〕、物理层前导码的传输、物理层首部、MAC首部，然后是SIFS，然后是ACK。
   来源：Feishu historical snapshot 08e6132, original source paragraph 93；Qwen recovery raw commit2887ed5, window 48；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5380.66–5405.34s；new unprompted medium.en chunk-031, absolute 5385–5407.16s
   限制：保留So you to transmit...you have to口语起句，不删除第一个you。发送前间隔F dewes、W dips/this，Q SIFS冲突；发送后SIFS/ACK由Qwen与新medium近音支持。
3. [Okay unclear], lots of time to just transmit [a/the/zero-article unclear] payload.
〔Okay有无待听辨〕，要用很多时间，就为了传输〔a/the/无冠词待听辨〕有效载荷。
   来源：Qwen recovery raw commit2887ed5, window 48；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395.66–5405.34s；new unprompted medium.en chunk-031, absolute 5400.72–5407.16s
   限制：Qwen有Okay和零冠词payload；medium chunk30为a payload、chunk31为the payload；Feishu尾部漏录。

## 75 · 01:30:04 · 长载荷效率与失败重传额外开销

稳定块ID：doxcnVIlMbRLnNFqo5tFGAYyaqh
原块SHA256：91b39d35bd0816ca0459ad5c6becf456b03d98747b825e55d292c29172a20fb6
候选SHA256：2f6f2cb96d3d620ce285e049357fd2bf5c733a2449b9366f4378affdf5331f6f

### 具体修改

1. 原：You had better have a long payload, because otherwise your protocol is very, very inefficient.
   候选：So you better have a long payload because otherwise your protocol is very, very inefficient, [okay unclear].
   理由：去掉旧编辑补的had，恢复So和来源中存在的Okay疑点。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395–5414s；new unprompted medium.en chunk-031, absolute 5400–5419s
2. 原：If transmission fails and you have to perform backoff and retransmit the packet, you must wait for the channel to become idle:
   候选：If your transmission fails and you have to perform backoff and retransmit the packet, then you have to wait for the channel to become idle.
   理由：恢复your、then、have to，不以must替换原话。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5413–5424s
3. 原：and hope the channel remains idle so that you can keep decreasing the backoff counter until it reaches zero.
   候选：Hope that the channel remains idle and you can decrease the backoff counter continuously and over time reach zero
   理由：恢复原祈愿开句及continuously and over time，不概括为keep/until。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5424–5437s
4. 原：Lots of things, right, just to transmit a single payload again.
   候选：Lots of things, right? Just again to transmit a single [payload/failure unclear].
   理由：恢复原again词序；payload/failure是实质异文，不能凭语义选payload。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5437–5452s

### 逐单元证据

1. So you better have a long payload because otherwise your protocol is very, very inefficient, [okay unclear].
所以你最好有一个长的有效载荷，因为否则你的协议就非常、非常低效，〔okay有无待听辨〕。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-030, absolute 5395.66–5414.82s；new unprompted medium.en chunk-031, absolute 5400.72–5419.92s
   限制：保留you better，不补had。Okay在Qwen与medium chunk31有，Feishu与chunk30无；口头语暂标疑。
2. And this is the best case. If your transmission fails and you have to perform backoff and retransmit the packet, then you have to wait for the channel to become idle.
而且这是最好的情况。如果你的传输失败了，并且你必须执行退避并重传这个数据包，那么你必须等待信道变为空闲。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5407.16–5424.14s
3. [DIFS/SIFS unclear], backoff time. Hope that the channel remains idle and you can decrease the backoff counter continuously and over time reach zero, and then transmit your packet, and then SIFS and ACK.
〔DIFS/SIFS待听辨〕，退避时间。希望信道保持空闲，而且你能够持续地递减退避计数器，并随着时间推移到达零，然后传输你的数据包，然后是SIFS和ACK。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5424.6–5445.16s
   限制：F Dips、medium This、Qwen SIFS；仍标疑，不按流程强改。其后continuously and over time三方有对应，恢复原措辞。
4. Lots of things, right? Just again to transmit a single [payload/failure unclear].
很多东西，对吧？仅仅又是为了传输一个〔payload/failure，有效载荷/失败，待听辨〕。
   来源：Feishu historical snapshot 08e6132, original source paragraph 94；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5437.66–5452.78s
   限制：Qwen payload，Feishu failure、新medium failure；不能单凭技术合理性把failure悄悄改为payload。

## 76 · 01:30:46 · Wi-Fi协议效率总结

稳定块ID：doxcnhiEoLg0Ehnqpu87QIE85Mf
原块SHA256：1ffb56b0ccf5487489937b8c6b5f6bd1c80efcb6ba8cac2069e2ae7715e8e5db
候选SHA256：4223e330f0b6c2d7c15c995b13ef05d7576c2a8d7691762a3330d8c2fb562fa2

### 具体修改

1. 原：We realize that Wi-Fi's efficiency is actually pretty low.
   候选：So, we [realize/realized unclear] that the efficiency of Wi-Fi is actually pretty low.
   理由：恢复So与the efficiency of Wi-Fi词序，不把ASR时态差异统一成现在时。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5445–5452s
2. 原：Unfortunately this holds for all versions of Wi-Fi.
   候选：And this holds, unfortunately, for all versions of Wi-Fi.
   理由：恢复And及unfortunately原位置。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453–5461s
3. 原：We looked at the basic version, but it is a curse for all versions.
   候选：Okay, we [looked / are looking / have looked unclear] at the basic version, but it's actually a curse for all versions.
   理由：恢复Okay、actually和it’s；三种时态不靠语法判断强选。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453–5470s
4. 原：On average, you can consider this scheme's efficiency to be about fifty to fifty-five percent, which is definitely low.
   候选：And on average, you can consider that the efficiency of this scheme is about fifty, fifty-five percent, which is definitely low, right?
   理由：恢复And、that从句、of结构、原数字表达及尾问；不借听校修正讲者效率估计。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5461–5481s
5. 原：Maximum efficiency would be one hundred percent. So, yeah, hopefully.
   候选：The maximum efficiency [would/will unclear] be one hundred percent. [So, yeah, hopefully / so, we are halfway; unclear]
   理由：恢复The，明确would/will与hopefully/halfway两处来源冲突。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5470–5490s

### 逐单元证据

1. So, we [realize/realized unclear] that the efficiency of Wi-Fi is actually pretty low.
所以，我们〔realize/realized，时态待听辨〕认识到，Wi-Fi的效率实际上相当低。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5445.16–5452.78s
   限制：F与Qwen realize，新medium realized，保留时态冲突。
2. And this holds, unfortunately, for all versions of Wi-Fi.
而且不幸的是，这对所有版本的Wi-Fi都成立。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453.5–5461.3s
   限制：这是讲者泛化说法，未替换为技术上更严谨的范围表述。
3. Okay, we [looked / are looking / have looked unclear] at the basic version, but it's actually a curse for all versions.
好，我们〔looked/are looking/have looked，时态待听辨〕看的是基础版本，但是它实际上是所有版本的一个诅咒。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5453.5–5470.46s
   限制：F looked；Q are looking；W have looked，不能任意统一时态。
4. And on average, you can consider that the efficiency of this scheme is about fifty, fifty-five percent, which is definitely low, right?
而且平均来看，你可以认为这个方案的效率大约是百分之五十、五十五，这确实很低，对吧？
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5461.3–5481.06s
   限制：保留讲者百分数估计；来源没有可靠独立to词，按原相邻数字记录，不添加更高精度或适用性结论。
5. The maximum efficiency [would/will unclear] be one hundred percent.
最高效率〔would/will，情态或时态待听辨〕是百分之百。
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5470.46–5490.18s
   限制：F would，Qwen与W will，词级待听辨。
6. [So, yeah, hopefully / so, we are halfway; unclear]
〔So, yeah, hopefully / so, we are halfway，所以，是的，希望如此／所以，我们到了一半；待听辨〕
   来源：Feishu historical snapshot 08e6132, original source paragraph 95；Qwen recovery raw commit2887ed5, window 49；new unprompted medium.en chunk-031, absolute 5481.06–5490.18s
   限制：旧两源yeah hopefully，新medium we are halfway；语义不同，不能因50%上下文而强行选halfway，也不能把旧稿hopefully当已证原话。

## 77 · 01:31:25 · 引出最后一个机制扩展IFS

稳定块ID：doxcnwoEYTymZ16TQtbNWfHjjff
原块SHA256：329e1098915d700ccac9cb1d5a5147c606804f6c3f83d6e66b731a1944c0d704
候选SHA256：eed6e406d19e97137aabddff9b988343534c26ba59f21f859951d038926fcc7c

### 具体修改

1. 原：That said, we are missing just one last mechanism in Wi-Fi channel access,
   候选：Okay, that said, we are just missing one last mechanism in the Wi-Fi channel access,
   理由：恢复Okay、are just missing词序和the；不改为更顺的叙述。
   来源：Feishu historical snapshot 08e6132, original source paragraph 96；Qwen recovery raw commit2887ed5, window 49；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5481–5509s
2. 原：We just need to introduce it, and we will do that after the break: this last piece of the protocol, related to something we already know about, the famous four interframe spaces, the extended IFS.
   候选：Okay, so we just [need/needed unclear] to introduce, and we do that after the break, this last piece [for ... unclear] of the protocol that is related to what, actually, something that we know already about, the famous [four/for/form unclear] interframe space, the extended IFS.
   理由：恢复Okay/so、原省略宾语、do时态、what actually、know already词序与space单数；不保留编辑增补it/will。need/needed及起句介词冲突标疑。 famous后原Feishu for、Qwen50 four、medium031 segment18 form近音不稳，补显式待听辨；不定译四个。
   来源：Feishu historical snapshot 08e6132, original source paragraph 96；Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5500–5528s
3. 原：Remember the extended IFS and the priority ladder: SIFS, PIFS, DIFS, and extended IFS.
   候选：Remember the extended IFS. Remember the priority ladder, we have SIFS, PIFS, [DIFS/PIFS unclear], and extended IFS.
   理由：恢复两次Remember与we have；列表部分漏识/近音冲突不按标准顺序无标记补齐。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5528–5551s
4. 原：We said we would first focus on SIFS and DIFS and understand how they are used, then return to the other timing intervals.
   候选：So, we [said/start unclear], let's first focus on SIFS and [DIFS/PIFS unclear], understand how they are used, and then we'll go back to the other [time/timing unclear] intervals.
   理由：恢复So、let’s命令结构、we’ll go back原措辞，不改would/return；源词冲突保留。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5537–5555s
5. 原：Now it is time to talk about the longest of these intervals, the extended IFS.
   候选：So, now it's time to talk about the longest among these [time/timing unclear] intervals. That was indeed the extended IFS.
   理由：恢复So、among、完整That was indeed句及过去式，非同位语压缩。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5556–5566s
6. 原：To give you an idea, it can be as long as about three hundred microseconds, so it is definitely longer than the others we have considered.
   候选：And just to give you an idea, this extended IFS, [so/or unclear] this [time/timing unclear] interval, can be as long as about three hundred microseconds, so definitely longer than the others that we have considered so far.
   理由：恢复And/just、重复this extended IFS/time interval、that与so far；不补it is；so/or待听辨。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5566–5594s；new unprompted medium.en chunk-032, absolute 5565–5594s

### 逐单元证据

1. Okay, that said, we are just missing one last mechanism in the Wi-Fi channel access, and then we are done with the basic version of Wi-Fi, that is the most important one.
好，说到这里，我们在Wi-Fi信道接入中就只剩最后一个机制还没有讲，然后我们就讲完Wi-Fi的基础版本了，那是最重要的一个版本。
   来源：Feishu historical snapshot 08e6132, original source paragraph 96；Qwen recovery raw commit2887ed5, window 49；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5481.06–5509.24s
   限制：Qwen49尾部but it is，Qwen50/F/medium that is；此候选按相邻更完整窗口及F保留that is，不新增which从句。
2. Okay, so we just [need/needed unclear] to introduce, and we do that after the break, this last piece [for ... unclear] of the protocol that is related to what, actually, something that we know already about, the famous [four/for/form unclear] interframe space, the extended IFS.
好，所以我们只是〔need/needed，时态待听辨〕需要介绍，而且我们在休息之后来做这件事，这最后一部分〔for，起句词有无待听辨〕协议，它关联到什么，实际上，关联到我们已经知道的一些东西，那著名的〔four/for/form，确切措辞待听辨〕帧间间隔，扩展IFS。
   来源：Feishu historical snapshot 08e6132, original source paragraph 96；Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 49；Qwen recovery raw commit2887ed5, window 50；new unprompted medium.en chunk-031, absolute 5500.96–5528.54s
   限制：保留introduce后缺宾语、what actually与singular space；F last piece for.Of，Q/W last piece of，介词可能是假起句，标疑；W needed，F/Q need。 原Feishu为for、Qwen50为four、medium031 segment18为form；不按协议知识强定four或fourth，正文显式待听辨。
3. Remember the extended IFS. Remember the priority ladder, we have SIFS, PIFS, [DIFS/PIFS unclear], and extended IFS.
记住扩展IFS。记住这个优先级阶梯，我们有SIFS、PIFS、〔DIFS/PIFS待听辨〕，还有扩展IFS。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5528.54–5551.26s
   限制：F sieves/peeves/diffs/extended，Q50 SIFS/PIFS/PIFS/extended，Qtail漏一项，新medium此列表漏录。可恢复四项框架，但第三项必须暴露来源差异。
4. So, we [said/start unclear], let's first focus on SIFS and [DIFS/PIFS unclear], understand how they are used, and then we'll go back to the other [time/timing unclear] intervals.
所以，我们〔said/start，确切措辞待听辨〕，我们先关注SIFS和〔DIFS/PIFS待听辨〕，理解它们是怎样使用的，然后我们再回到其他的〔time/timing，时间修饰词待听辨〕间隔。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5537.1–5555.02s
   限制：F said let’s first focus on sieves/diffs，Q50 start last first ...SIFS/PIFS，Qtail start let’s first ...SIFS/PIFS；medium we said let’s first...sieves/dieves。句首和第二种IFS均标疑，不按优先级知识强定。
5. So, now it's time to talk about the longest among these [time/timing unclear] intervals. That was indeed the extended IFS.
所以，现在到了讨论这些〔time/timing，时间修饰词待听辨〕间隔中最长的那个的时候了。那确实就是扩展IFS。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5556.04–5566.22s；new unprompted medium.en chunk-032, absolute 5565–5576.72s
   限制：保留原that was indeed过去式，不改is或同位语；time/timing因Q主窗与tail/新ASR不同保留。
6. And just to give you an idea, this extended IFS, [so/or unclear] this [time/timing unclear] interval, can be as long as about three hundred microseconds, so definitely longer than the others that we have considered so far.
而且，只是为了让你有个概念，这个扩展IFS，〔so/or，所以/或者，待听辨〕这个〔time/timing，时间修饰词待听辨〕间隔，可以长到大约三百微秒，所以肯定比我们到目前为止考虑过的其他那些更长。
   来源：Feishu historical snapshot 08e6132, original source paragraph 97；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-031, absolute 5566.22–5594.98s；new unprompted medium.en chunk-032, absolute 5565–5594.28s
   限制：so为F和Q50，or为Qtail及medium两窗；保留this extended IFS重复，不压成it；300微秒三方明确，适用版本限定在下段。

## 78 · 01:33:12 · EIFS近似时长与长课间休息

稳定块ID：doxcnH3EBc16mt3kuRZNdO8FJpe
原块SHA256：9f2eab41bdab1b95b846093fbb6d2e0a73378114bd71708b947a6c20878088c1
候选SHA256：53e6737b0e3048fe6b148c85c67ff45e3c4a8d13160ab949319fd984dc764ddf

### 具体修改

1. 原：It depends on the version of Wi-Fi we consider, but to keep an approximate figure in mind, you can consider it equal to three hundred microseconds.
   候选：Okay, it depends on the version of Wi-Fi that we consider, but just [yeah / you know / no filler; unclear], to keep in mind, again, [you can be considered; subject/construction unclear] equal to three hundred microseconds.
   理由：恢复Okay/that/just/again及三方原口语you can be considered；删去旧稿无来源的approximate figure和主语语法改写；语气词冲突标疑。 多源相同仍不能排除共同ASR误识，主语/句式补正文显式待听辨，不擅改it。
   来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5586–5616s
2. 原：Just to have an idea.
   候选：[Okay unclear], so just to [have an idea / verify / evaluate; unclear].
   理由：恢复可能Okay/so；have an idea并非一致结果，全文保留精确片语冲突。
   来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603–5616s
3. 原：If I'm not wrong, we now stop for twenty-five minutes. Okay.
   候选：So if I'm not wrong, now we stop for twenty-five minutes. Okay.
   理由：恢复So及now原词序；不改动三源共同的25分钟。
   来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603–5616s

### 逐单元证据

1. Okay, it depends on the version of Wi-Fi that we consider, but just [yeah / you know / no filler; unclear], to keep in mind, again, [you can be considered; subject/construction unclear] equal to three hundred microseconds.
好，这取决于我们考虑的是Wi-Fi的哪个版本，但是只是〔yeah / you know / 无语气词；待听辨〕，为了记在心里，再说一次，〔你可以被认为；主语/句式待听辨〕等于三百微秒。
   来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5586.7–5616.34s
   限制：原Feishu justyeah，Qwen just you know，新medium just to keep in mind；保留you can be considered这一三方共有但不自然的口语，不改成you can consider it。中文逐字保留主语以免替讲者修理；其意思或转写仍需回听。 即使多源表面一致，you can be considered主语/句式仍可能共同识别错误；正文英中同步标疑，不擅自改为it。
2. [Okay unclear], so just to [have an idea / verify / evaluate; unclear].
〔Okay有无待听辨〕，所以只是为了〔have an idea / verify / evaluate，有个概念/核实/评估，待听辨〕。
   来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603.2–5616.34s
   限制：F So just to后残缺；Q50 verify、Q51及tail have an idea、W evaluate。旧稿选have an idea不应当作已确认。
3. So if I'm not wrong, now we stop for twenty-five minutes. Okay.
所以，如果我没有记错，现在我们停二十五分钟。好。
   来源：Feishu historical snapshot 08e6132, original source paragraph 98；Qwen recovery raw commit2887ed5, window 50；Qwen recovery raw commit2887ed5, window 51；Qwen recovery raw commit2887ed5, window tail；new unprompted medium.en chunk-032, absolute 5603.2–5616.34s
   限制：twenty-five三源对应一致；尾Okay来自F及Q50/tail，新medium未转出。不用前文其他课间安排猜测替换25。

