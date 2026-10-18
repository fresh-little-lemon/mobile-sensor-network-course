# 第41–60段独立变更对照

状态：candidate_not_audio_certified；每个 before 均逐字校验为现稿子串。after 为恢复候选，非听辨认证。中文按每句英文重译，不替讲者补逻辑。


## 第41段 00:44:32
段 ID：doxcnpL38KX3LtqqoQ5CnydBzNd


### 变更 1

Before: Let's stop for five minutes, and then use the short break...

After: Okay, now let's stop for five minutes. And then use the [short break / shortcut unclear], if I'm not wrong.

理由：恢复Okay、now及被省略的if I’m not wrong；break/shortcut各有来源，不沿用现稿省略号遮掉词语。

来源：Feishu historical snapshot: source_index=51, id=107, section anchor 00:44:32；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s；Unprompted Whisper medium.en raw: chunk-015, segments 18–20, absolute 2667.58–2690.08s


### 变更 2

Before: Then we will resume and see how the collision probability can be computed.

After: Okay, and then we will resume and see how [this probability / these probabilities unclear] of collision can be computed.

理由：恢复Okay、and及原来的指示词/单复数冲突，不将probability of collision改写为collision probability。

来源：Feishu historical snapshot: source_index=51, id=107, section anchor 00:44:32；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s；Unprompted Whisper medium.en raw: chunk-015, segments 19–20, absolute 2674.84–2690.08s；Unprompted Whisper medium.en raw: chunk-016, segments 1–1, absolute 2685.00–2690.08s


### 待听辨与来源限制

- And then use the [short break / shortcut unclear], if I'm not wrong.
  依据：Feishu: short way, you cannot run; Qwen 24: shortcut if I'm not wrong; medium chunk-015 segment 19: short break if I'm not wrong. The noun remains unresolved; the latter clause has two-ASR support.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- Okay, and then we will resume and see how [this probability / these probabilities unclear] of collision can be computed.
  依据：Medium chunks 015/016: this probability; Qwen 24: these probabilities; Feishu: these two probability. Feishu also has an interrupted and / let's see; two ASRs instead agree on and see.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- Break-region isolated and repetitive ASR output
  依据：At 2714.36–2714.84s medium alone gives Thank you with no_speech_prob 0.6267; not corroborated by Feishu/Qwen. At 2840.94–2864.98s medium repeats I’m sorry eight times. anomalies/4720-repetition-review.json records empty small.en and Qwen 25 outputs, high compression and repeated zero-duration word anchors.
  处理：不把这两处插入已确认讲者台词；保留原始输出与疑点。47:20重复疑似幻觉，不是已证实口语重复。


## 第42段 00:49:19
段 ID：doxcnBQOCHSdBhJ0SZfY43litTc


### 变更 1

Before: Good. Let's look at our computation.

After: Okay, good. [So / Now unclear], let's look at our computation.

理由：恢复Okay与So；Now/So来源冲突显式标示。

来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–1, absolute 2958.90–2977.88s


### 变更 2

Before: The probability that B and C collide is, as we said, very simple, so don't worry; this is a very simple derivation.

After: So, the probability that B and C collide is, as we said, very simply, so [don't / do not unclear] worry, this is a very, very simple derivation.

理由：恢复So、very simply、不顺的起句和very, very重复；do not/don’t保留词形疑点。

来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–2, absolute 2958.90–3004.72s


### 变更 3

Before: It is the probability that B and C draw the same value, let's say n, the same integer.

After: Is the probability that B and C draw the same value, let's say n, okay? [A / the unclear] same value, [a / the unclear] same integer. That's what we said, all right.

理由：撤销添加的It，恢复a same value、a same integer及That’s what we said, all right。

来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=26, absolute 2860.00–2980.00s；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 1–3, absolute 2958.90–3016.02s


### 变更 4

Before: Let's start by considering that B draws a given integer n, whatever it is.

After: Let's start this computation by considering that B draws n, a given integer n, whatever this is.

理由：恢复this computation、先说n再重述a given integer n及whatever this is。

来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 2–5, absolute 2977.88–3056.06s


### 变更 5

Before: What we first compute is the conditional probability that C also draws n, given that B drew n.

After: So, what we are first computing is the [conditional / conditioned unclear] probability, so the probability that C draws also n, so n, given that B drew n, okay? So this is the so-called conditioned probability.

理由：恢复So、are first computing、第二次so n与对conditioned probability的重述，不统一为书面conditional probability。

来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Unprompted Whisper medium.en raw: chunk-017, segments 4–6, absolute 3020.72–3065.02s；Unprompted Whisper medium.en raw: chunk-018, segments 1–1, absolute 3045.00–3062.64s


### 变更 6

Before: Remember that our scheme is simple because it is distributed. Every node makes its own decisions according to the protocol rules, independently of the others.

After: Now remember, our scheme is actually very simple because it's distributed. And as we said, every node makes its own decisions according to the protocol rules, but it makes its own decisions independently from the others, right?

理由：恢复Now、actually very、as we said及it makes its own decisions重复，保留from和right。

来源：Feishu historical snapshot: source_index=52, id=109, section anchor 00:49:19；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-017, segments 6–7, absolute 3056.06–3074.66s；Unprompted Whisper medium.en raw: chunk-018, segments 1–4, absolute 3045.00–3091.06s


### 待听辨与来源限制

- [So / Now unclear], let's look at our computation.
  依据：Feishu says Now; Qwen 26 and medium chunk-017 segment 1 say So.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So, the probability that B and C collide is, as we said, very simply, so [don't / do not unclear] worry, this is a very, very simple derivation.
  依据：All three retain very simply and very, very. Feishu: don't worry; medium: do not worry; Qwen: not worrying. No repair to adjectival simple or extra predicate.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- [A / the unclear] same value, [a / the unclear] same integer.
  依据：Feishu and Qwen 27: a same value, a same integer (Feishu mishears integer as image); medium: the same value, the same, then drops the noun. The repeated phrase is retained, with article uncertainty.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So, what we are first computing is the [conditional / conditioned unclear] probability, so the probability that C draws also n, so n, given that B drew n, okay?
  依据：Feishu first says conditional; Qwen 27 says conditioned; medium says condition. The later repeated term is conditioned in Feishu/Qwen/medium-017.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第43段 00:51:21
段 ID：doxcns4CMNfXgAjgRek2xop5aSh


### 变更 1

Before: The fact that B drew n will not affect the probability that C draws n.

After: So, the fact that B drew n will not affect the probability that C draws n.

理由：恢复句首So，保留drew/draws及will not。

来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=27, absolute 2970.00–3090.00s；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 4–5, absolute 3080.06–3099.36s


### 变更 2

Before: C does whatever it decides following the protocol, but it is not affected by what other nodes do.

After: C does whatever, let's say, [he / it unclear] likes, based on what decisions [he / it unclear] makes following the protocol, right? But it's not affected by what other nodes do.

理由：恢复whatever、let’s say、likes、based on what decisions；he/it来源不同，不压缩为decides。

来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 4–6, absolute 3080.06–3110.18s


### 变更 3

Before: This is therefore equal to the probability that C draws n, simply that, because it doesn't matter what B does. C does things by itself.

After: So, this is actually equal to the probability that C draws n, simply that, because it doesn't matter what B does, right? C will do things by [itself / himself / themselves unclear].

理由：恢复So、actually、right和will，末尾反身代词冲突短标。

来源：Feishu historical snapshot: source_index=53, id=111, section anchor 00:51:21；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 6–8, absolute 3099.36–3142.32s


### 待听辨与来源限制

- C does whatever, let's say, [he / it unclear] likes, based on what decisions [he / it unclear] makes following the protocol, right?
  依据：Feishu and Qwen 28 use he; medium-018 segment 5 uses it. Feishu clearly has let's say; Qwen has it say, medium omits it. Repeated spoken structure restored without choosing the pronoun.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- C will do things by [itself / himself / themselves unclear].
  依据：Feishu: itself; Qwen 28: himself; medium-018 segments 7–8: themselves. All retain will; current present-tense paraphrase is removed.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第44段 00:52:17
段 ID：doxcndVEHARMqt6UlFaVILYkrob


### 变更 1

Before: What is the probability that C draws n? What is the probability that an integer is selected from zero to CW_min? We have written it here.

After: Okay, so what is the probability that C draws n? So, what is the probability that an integer is selected out of the range zero, CW_min? Well, we have written that here, right? This is the probability.

理由：恢复Okay so、第二个So、out of the range、Well及This is the probability，不重写为from ... to。

来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 8–10, absolute 3133.94–3162.86s


### 变更 2

Before: Given that B has drawn n, the probability that C also draws n is this one.

After: Okay, so now we know that given that B has drawn n, the probability that C will also draw n is this one.

理由：恢复Okay so now we know that与will also draw，不改未来式。

来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Unprompted Whisper medium.en raw: chunk-018, segments 10–11, absolute 3153.40–3174.20s


### 变更 3

Before: Conditioned on B drawing n, this is the conditional collision probability.

After: Okay, so [conditioned / condition unclear] to the fact that B drew n, then this is the collision probability [conditioned / condition unclear] to the fact that B drew n, right?

理由：恢复两次to the fact that B drew n、then及right；condition/conditioned的词尾不凭语法补。

来源：Feishu historical snapshot: source_index=54, id=113, section anchor 00:52:17；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 12–13, absolute 3176.26–3197.04s


### 待听辨与来源限制

- Okay, so [conditioned / condition unclear] to the fact that B drew n, then this is the collision probability [conditioned / condition unclear] to the fact that B drew n, right?
  依据：Qwen 28 reads conditioned twice; Feishu and medium read condition twice. All retain the repeated to the fact that B drew n structure.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第45段 00:53:12
段 ID：doxcn1OwmYmonhT50Rlx5H4yd4K


### 变更 1

Before: To compute the original probability, we now need to remove the conditioning and consider any possible n.

After: What we need to do is to now to compute the original probability, is to decondition and make the computation for any possible n.

理由：恢复What we need to do is to now to ... is to的不顺结构，以及decondition、make the computation。

来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=28, absolute 3080.00–3200.00s；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 13–15, absolute 3185.78–3222.08s


### 变更 2

Before: We want to compute the probability that B and C collide without conditioning on any event.

After: So, what we want to now do is to compute in general the probability that B and C collide without conditioning to any event.

理由：恢复So、what we want to now do、in general和conditioning to，不换介词。

来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 14–16, absolute 3197.04–3233.26s；Unprompted Whisper medium.en raw: chunk-019, segments 1–1, absolute 3225.00–3239.24s


### 变更 3

Before: We need to consider all possible integer values from zero to CW_min.

After: So that is, we need to consider all possible values of integer from zero to CW_min.

理由：恢复So that is及values of integer的原词序。

来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 16–17, absolute 3222.08–3249.94s；Unprompted Whisper medium.en raw: chunk-019, segments 1–1, absolute 3225.00–3239.24s


### 变更 4

Before: For any n, the collision probability involves the probability that C draws n if B has also drawn n.

After: And for any n, we know that the probability of collision is what? The probability that C draws n if also B has drawn n, right?

理由：撤销解释性involves，恢复And、we know that、is what问答及if also B has drawn n。

来源：Feishu historical snapshot: source_index=55, id=115, section anchor 00:53:12；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-018, segments 17–18, absolute 3233.26–3254.22s；Unprompted Whisper medium.en raw: chunk-019, segments 2–3, absolute 3242.04–3264.66s


## 第46段 00:54:22
段 ID：doxcnflxhsrZ0Q4lhw4fU7eq5xe


### 变更 1

Before: Let's first write the probability that B draws n. It is again one over (CW_min + 1).

After: So, let's first write the probability that B draws n. The probability that B draws n is again this one. So we can write one over CW_min plus one. This is the probability that B draws n.

理由：恢复So与三次the probability that B draws n，以及this one和so we can write；不以公式替掉口述。

来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 3–5, absolute 3251.88–3289.40s


### 变更 2

Before: Given that, a collision happens if C also draws n, and that happens with this probability.

After: And then given that, we know that [a / the unclear] collision happens if C also draws n. That happens with this probability.

理由：恢复And then、we know that及独立重复句；不合并that happens。

来源：Feishu historical snapshot: source_index=56, id=117, section anchor 00:54:22；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Unprompted Whisper medium.en raw: chunk-019, segments 5–7, absolute 3275.64–3312.46s


### 待听辨与来源限制

- And then given that, we know that [a / the unclear] collision happens if C also draws n.
  依据：Qwen 29: a collision; medium-019 segment 6: the collision; Feishu truncates after a.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第47段 00:54:59
段 ID：doxcnpIXR5BhdcEJODa1iMozspe


### 变更 1

Before: We multiply by one over (CW_min + 1), the probability that C draws n.

After: So we multiply by again one over CW_min plus one, which is the probability that C [draws / grows unclear] n.

理由：恢复So、again、which is；draws由上下文和邻句定位，近音grows/goes不作为确定原词。

来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=29, absolute 3190.00–3310.00s；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 7–8, absolute 3296.96–3331.38s


### 变更 2

Before: We therefore sum over n from zero to CW_min the term 1/(CW_min + 1)^2.

After: So what we have is simply sum over n that goes from zero to CW_min of one over CW_min plus one squared, [right / okay unclear]?

理由：恢复so what we have is simply、that goes及口述one over，不用数学符号替换句子。

来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 7–9, absolute 3296.96–3346.32s


### 变更 3

Before: This is a constant term inside the sum. How many times do we sum it? CW_min + 1 times.

After: Now, this is a constant term, we are inside a sum, so we are summing this constant term how many times? CW_min plus one times, right?

理由：恢复Now、we are inside a sum、so we are summing this constant term以及times/right，保留重复。

来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 9–11, absolute 3333.28–3380.72s


### 变更 4

Before: This gives (CW_min + 1)/(CW_min + 1)^2. We simplify numerator and denominator and get 1/(CW_min + 1).

After: So this is equal to CW_min plus one divided by CW_min plus one squared. We simplify numerator and denominator, and we get one over CW_min plus one.

理由：恢复So this is equal to、and we get及口述算式，不添加gives解释。

来源：Feishu historical snapshot: source_index=57, id=119, section anchor 00:54:59；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Unprompted Whisper medium.en raw: chunk-019, segments 11–12, absolute 3357.94–3396.18s


### 待听辨与来源限制

- So we multiply by again one over CW_min plus one, which is the probability that C [draws / grows unclear] n.
  依据：Medium-019 segment 7: grows n; Qwen 30: goes n; Feishu is multilingual corruption. Draws is contextually expected and repeatedly spoken elsewhere, but the local verb is not confirmed by these outputs.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So what we have is simply sum over n that goes from zero to CW_min of one over CW_min plus one squared, [right / okay unclear]?
  依据：Qwen 30 has okay after square; Feishu has right; medium has no tag. Numerator/denominator grouping is conceptual context, not added spoken parentheses.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第48段 00:56:35
段 ID：doxcnnL1HcoGHeu170WeLRQgmwb


### 变更 1

Before: The final result is that the probability that B and C collide in our simple example is one over (the contention window plus one).

After: So, the final result of all [this computation / these computations unclear] is that the probability that B and C collide in our simple example that we presented earlier is one over the contention window plus one.

理由：恢复So、of all this computation及that we presented earlier，单复数来源冲突短标。

来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 12–14, absolute 3380.72–3419.70s；Unprompted Whisper medium.en raw: chunk-020, segments 1–1, absolute 3405.00–3419.66s


### 变更 2

Before: If you were able to follow the computation, great.

After: Okay, now if you [were / are unclear] able to follow the computation, great.

理由：恢复Okay、Now；were/are来自重叠medium窗的冲突不隐藏。

来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=30, absolute 3300.00–3420.00s；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 14–15, absolute 3404.72–3434.48s；Unprompted Whisper medium.en raw: chunk-020, segments 1–2, absolute 3405.00–3434.98s


### 变更 3

Before: It is a simple probability calculation, but if your background is different and you have not seen probability in previous courses, do not worry. The important thing is to retain the final message.

After: It's a simple probability computation, but if your background is different, and therefore you have not seen probability anywhere in your previous courses, do not worry. The important thing is that you retain the final message.

理由：恢复It’s、computation、therefore、anywhere、your和that you retain，不改成更短的概述。

来源：Feishu historical snapshot: source_index=58, id=121, section anchor 00:56:35；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-019, segments 15–16, absolute 3419.70–3434.78s；Unprompted Whisper medium.en raw: chunk-020, segments 2–4, absolute 3419.66–3451.44s


### 待听辨与来源限制

- So, the final result of all [this computation / these computations unclear] is that the probability that B and C collide in our simple example that we presented earlier is one over the contention window plus one.
  依据：Qwen 30: all this computation; medium-019 segment 12: all these computations. Feishu beginning is corrupted. Restore the full sentence starting before the approximate 00:56:35 anchor without duplicating it in section 47.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- Okay, now if you [were / are unclear] able to follow the computation, great.
  依据：Qwen 30/31 and medium-019 say were; overlapping medium-020 says are. Feishu garbles were able as were Evil. Majority support favors were, but the tense conflict remains visible.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第49段 00:57:27
段 ID：doxcnJ5JJMQGLQYI4WCncznRwTb


### 变更 1

Before: In our simple example, the probability that B and C collide while performing backoff equals this ratio, which decreases as the contention window minimum increases.

After: The final message is, in our simple example, right, that we are considering, the probability that B and C [collide / collided unclear] while performing the backoff procedure is equal to this ratio, that clearly will decrease as the value of contention window minimum increases, right?

理由：恢复The final message is、right、that we are considering、procedure、that clearly will以及value of，不压缩未来式。

来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-020, segments 4–7, absolute 3444.44–3482.36s


### 变更 2

Before: The larger the contention window, the lower the ratio and therefore the lower the collision probability. This is something everybody can understand.

After: The larger the contention window, the lower this ratio, so the lower the collision probability. This is, I think, something that everybody [can understand / understands unclear].

理由：恢复this ratio、so和I think，can understand/understands来源不一致短标。

来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Unprompted Whisper medium.en raw: chunk-020, segments 7–9, absolute 3471.76–3501.42s


### 变更 3

Before: This refers to the simple example, but it expresses a general rule: collision probability in backoff decreases as the contention window increases.

After: Okay, now, so this means that, okay, this refers, as I said, to the previous simple example, but it's a general rule. The collision probability in the backoff procedure decreases as the value of contention window increases.

理由：恢复Okay now so this means that okay、as I said、previous及完整第二次rule说明，不重写expresses。

来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 9–12, absolute 3490.16–3532.90s


### 变更 4

Before: What does this tell you? Why am I making this second observation?

After: So now, what does this tell you? Why am I marking this, [and making / I'm making unclear] this second observation?

理由：恢复So now及被删的marking this；连接and/I’m来源冲突短标，保留口头自我重启可能。

来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=31, absolute 3410.00–3530.00s；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 12–13, absolute 3518.78–3539.58s


### 变更 5

Before: We wanted to understand why in Wi-Fi, every time we perform backoff for a given data packet, we roughly double the contention window. We increase it significantly every time. Why? To reduce the probability of collision among contending nodes.

After: Because remember, we wanted to understand the reason why in Wi-Fi we say every time we perform the backoff procedure for a given data packet, we roughly speaking double the contention window. So we increase it very significantly every time. Why do we do that? To reduce the probability of collision among [contending / contend unclear] nodes.

理由：恢复Because remember、the reason why、we say、procedure、roughly speaking、very及完整问句。

来源：Feishu historical snapshot: source_index=59, id=123, section anchor 00:57:27；Feishu historical snapshot: source_index=60, id=125, section anchor 00:57:27；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 13–18, absolute 3532.90–3583.12s


### 待听辨与来源限制

- The final message is, in our simple example, right, that we are considering, the probability that B and C [collide / collided unclear] while performing the backoff procedure is equal to this ratio, that clearly will decrease as the value of contention window minimum increases, right?
  依据：Qwen 31 and medium-020 use collide; Feishu uses collided. The future will decrease and clearly are restored from Feishu/Qwen/medium.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- This is, I think, something that everybody [can understand / understands unclear].
  依据：Feishu: I think, ... can understand; Qwen 31: I think, ... understands; medium: can understand, omitting I think. Preserve the qualifier, flag the verb difference.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- Why am I marking this, [and making / I'm making unclear] this second observation?
  依据：Medium-020 segments 12–13: Why am I marking this and making this second observation; Qwen 32: Why am I marking these? I'm making this second observation. Feishu supplied fragments omit this sentence.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- To reduce the probability of collision among [contending / contend unclear] nodes.
  依据：Qwen 32: contend nodes; medium-020 segment 17: contented nodes; Feishu truncates at To reduce. Contending is technically plausible, but the local participle ending is not established.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第50段 00:59:34
段 ID：doxcnUwQc9ePMHTxq4Ra0PKvQIf


### 变更 1

Before: Backoff is a probabilistic mechanism. Wi-Fi essentially assumes that a transmitter is failing, failing, failing because too many nodes are trying to access the channel. The situation is too crowded.

After: [Okay unclear], so, backoff is a probabilistic mechanism, and essentially Wi-Fi assumes that the reason why a transmitter is failing, failing, failing is because there are too many nodes in the network that try to access the channel to transmit a packet. The situation is too crowded.

理由：恢复So、and essentially、the reason why、in the network、to transmit a packet，保留failing三连。

来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 17–21, absolute 3564.66–3604.92s；Unprompted Whisper medium.en raw: chunk-021, segments 1–3, absolute 3585.00–3605.86s


### 变更 2

Before: It assumes that when you fail, fail, fail, other nodes are trying too; you select the same backoff time and keep colliding.

After: So what Wi-Fi says is, if you fail, [fail, fail unclear], every time you fail means that there are other nodes trying, and you are selecting the same backoff, you have the same backoff time, and you keep colliding.

理由：恢复what Wi-Fi says is、every time you fail means及same backoff / same backoff time重述；fail重复有Qwen/Feishu支持保留并说明medium省略。

来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Unprompted Whisper medium.en raw: chunk-020, segments 21–23, absolute 3597.84–3614.84s；Unprompted Whisper medium.en raw: chunk-021, segments 3–5, absolute 3598.64–3621.94s


### 变更 3

Before: To reduce the collision probability, each node needs to enlarge the range of possible integer values from which it can choose.

After: So in order to reduce the probability of collision, each node needs to enlarge the possible values, so the choice, right, among the integers that can be selected.

理由：恢复So in order to、the possible values及so the choice right among the integers that can be selected，不补range of。

来源：Feishu historical snapshot: source_index=61, id=127, section anchor 00:59:34；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 6–7, absolute 3623.24–3643.32s


### 待听辨与来源限制

- [Okay unclear], so, backoff is a probabilistic mechanism, and essentially Wi-Fi assumes that the reason why a transmitter is failing, failing, failing is because there are too many nodes in the network that try to access the channel to transmit a packet.
  依据：Qwen 32 has Okay before So backoff; Feishu and medium omit that filler. Three failing repetitions are directly supported by Qwen and both medium windows.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So what Wi-Fi says is, if you fail, [fail, fail unclear], every time you fail means that there are other nodes trying, and you are selecting the same backoff, you have the same backoff time, and you keep colliding.
  依据：Qwen 32 explicitly repeats fail three times; Feishu has a fragmented FL feel. Fe. sequence. Both overlapping medium windows give a single fail before every time you fail. Repetition is plausible and retained as unconfirmed, not silently deleted.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第51段 01:00:35
段 ID：doxcneECTaGLIYZElqo3ZcJjZPe


### 变更 1

Before: It's like a bag of candies. If they are all strawberry flavored, two people picking candies will clearly both pick strawberry. If you fill the bag with banana, strawberry, peach, mint, and so on, the probability that two people pick the same flavor decreases. It's the same principle.

After: It's like when you have a bag with candies, if they are all strawberry flavored, if there are two people picking the candy, clearly they will pick strawberry. But if instead you fill the bag with banana, strawberry, peach, mint, and so on, then the probability that two people pick the same candy flavor will reduce. So this is exactly the same [principle / thing unclear].

理由：恢复when you have、if there are two people、the candy、But if instead、then、same candy flavor will reduce及exactly；保留两层if，不压缩为比喻摘要。

来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=32, absolute 3520.00–3640.00s；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 7–12, absolute 3633.44–3677.48s


### 变更 2

Before: You may say: nice, Wi-Fi deals with a crowded situation and lets us perform better. True, doubling the contention window works if the reason for failure is repeated collisions.

After: Okay, so you may say, well, nice, Wi-Fi really takes care of this crowded situation and allow us to perform better. True, but this is, this works, this is a good idea to double the contention window every time you perform a backoff to transmit [a / the unclear] packet. It works, but it works if the reason why a transmitter is failing is indeed because it [it unclear] keeps colliding with others.

理由：恢复Okay so、well、really takes care、allow us及this is this works、每次退避发送数据包、it works but it works的重复。

来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 12–17, absolute 3669.88–3718.78s


### 变更 3

Before: But remember that in wireless a transmission may also fail because of channel errors. You may be the only node with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate correctly.

After: But remember, in wireless, a transmission may fail also because of channel errors. So you may be the only one in the network with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate the signal correctly.

理由：恢复But remember in wireless、fail also、So、only one in the network及the signal，保留原词序。

来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Unprompted Whisper medium.en raw: chunk-021, segments 17–20, absolute 3710.16–3741.90s


### 变更 4

Before: You still have to follow the protocol rules. If you fail repeatedly because of channel errors, these rules mean that every time you have to enlarge the contention window. Statistically, it becomes more likely that you draw a longer and longer and longer backoff time.

After: Okay, so in that case, of course, you have to follow the protocol rules anyway. Okay, so if you fail and fail because of channel errors, you have to apply the rules. And this means that every time you have to enlarge the contention window, and statistically it's more likely that you will draw a long and longer and longer backoff time, right?

理由：恢复Okay so in that case of course、anyway、fail and fail、you have to apply the rules、and this means that、will draw a long and longer and longer，不将原话均改longer。

来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=33, absolute 3630.00–3750.00s；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 20–24, absolute 3733.92–3777.88s；Unprompted Whisper medium.en raw: chunk-022, segments 1–1, absolute 3765.68–3774.42s


### 变更 5

Before: Is this good in this case? Not really. You are not failing because you collide with other nodes; the reason is poor channel quality. This mechanism does not solve that issue.

After: So is this good in this case? [Hmm unclear], not really good, right? Because the reason why you are failing is not because there are others and you are colliding, that's not the reason. The reason is that the channel is poor, of poor quality, and this mechanism does not help to solve the issue, right?

理由：恢复So、not really good right、because the reason why、that’s not the reason、poor of poor quality和does not help to solve；嗯仅Feishu支持短标。

来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 24–27, absolute 3768.54–3793.32s；Unprompted Whisper medium.en raw: chunk-022, segments 1–4, absolute 3765.68–3800.62s


### 变更 6

Before: In this situation it is even harmful, because it delays channel access. It makes you wait longer and longer and longer before you can access the channel and transmit, even though the problem is poor channel quality, not collision. It just increases channel access delay and does not help with that problem.

After: Actually, this [method / mechanism unclear] in this situation is even harmful. Why? Because it makes you delay channel access, right? It makes you wait longer and longer and longer before accessing the channel, being able to access the channel and transmit the packet. With no reason, because the problem is not collision, the problem is poor channel quality. So it just increases the channel access delay. It doesn't help with anything.

理由：恢复Actually、this method、独立Why问句、makes you delay、重复before accessing / being able to access、with no reason及doesn’t help with anything；保留三次longer。

来源：Feishu historical snapshot: source_index=62, id=129, section anchor 01:00:35；Feishu historical snapshot: source_index=63, id=131, section anchor 01:00:35；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Unprompted Whisper medium.en raw: chunk-021, segments 28–28, absolute 3794.28–3794.70s；Unprompted Whisper medium.en raw: chunk-022, segments 4–8, absolute 3789.72–3840.14s


### 待听辨与来源限制

- So this is exactly the same [principle / thing unclear].
  依据：Feishu and medium-021 segment 11: principle; Qwen 33: thing. Both alternatives retained rather than silently following the more natural one.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- True, but this is, this works, this is a good idea to double the contention window every time you perform a backoff to transmit [a / the unclear] packet.
  依据：Feishu/Qwen both retain this is, this works; medium drops the first this is. Qwen 33: a packet; medium-021 segment 15: the packet; Feishu phrase is corrupted. Do not reduce the false start to True, doubling ... works.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- It works, but it works if the reason why a transmitter is failing is indeed because it [it unclear] keeps colliding with others.
  依据：All sources retain it works, but it works. Qwen 33 alone repeats it it before keeps; Feishu/medium have it once. The extra it remains marked rather than declared confirmed.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- [Hmm unclear], not really good, right?
  依据：Feishu includes Hmm; Qwen 34 and both medium windows omit it. The content not really good, right is supported across sources.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- Actually, this [method / mechanism unclear] in this situation is even harmful.
  依据：Feishu and medium-022 segment 4: method; Qwen 34: mechanism. Both are plausible local lexical alternatives, so do not silently substitute one.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第52段 01:04:00
段 ID：doxcn7v1pOcJSqW4rkKPR4G6heb


### 变更 1

Before: We need to understand why mechanisms are designed in a certain way, but also look at them critically.

After: Okay, so we need to be aware that, well, we need to understand why certain techniques, mechanisms are designed in a certain way. But we need also always to look at these mechanisms or techniques or solutions with a critical eye.

理由：恢复Okay so we need to be aware that well的自我转折、techniques mechanisms、also always、mechanisms or techniques or solutions与with a critical eye，不合并。

来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=34, absolute 3740.00–3860.00s；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 8–11, absolute 3830.38–3868.20s


### 变更 2

Before: Is a solution good under all conditions and in every situation?

After: That means we need to look at them and ask ourselves, is this really good in under all conditions, under all situations, or not?

理由：恢复That means we need to look at them and ask ourselves、really、in under、两次under all及or not，保留不顺。

来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 11–13, absolute 3859.44–3885.44s


### 变更 3

Before: Some aspects of a technology may not always be good, and we need to be aware of that.

After: There may be aspects of technology that are not that good, not always, and we need to be aware of that.

理由：恢复There may be、not that good、not always的语序和停顿。

来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 13–14, absolute 3876.96–3891.44s


### 变更 4

Before: When designing a technological solution, we need to account for possible issues.

After: Okay, so whenever we design a system, whenever we design a technological solution, we need to account for possible issues that may arise.

理由：恢复Okay so、whenever we design a system / whenever we design的重复自我重启及that may arise。

来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 14–16, absolute 3885.44–3911.72s


### 变更 5

Before: An idea may solve one problem but make things worse in other situations. We need to look at the big picture when designing a technology, and this is an example.

After: So an idea may be good to solve one problem, but it might actually make things worse in other situations. So we need also to look at the big picture when we design a technology. [Okay unclear], and [and unclear] this is indeed an example of [of unclear] that.

理由：恢复So an idea may be good to solve、might actually、So we need also to、when we design、indeed及Qwen单源and/of重复疑点。

来源：Feishu historical snapshot: source_index=64, id=133, section anchor 01:04:00；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 16–18, absolute 3902.68–3930.28s


### 待听辨与来源限制

- [Okay unclear], and [and unclear] this is indeed an example of [of unclear] that.
  依据：Qwen 35: Okay, and and this is indeed an example of of that; medium-022 segment 18: and this is indeed an example of that; supplied Feishu fragment ends before this continuation. Single-source repetitions are retained with short uncertainty markers.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第53段 01:05:29
段 ID：doxcn6EVnNwTDOuu398ghwuxGRc


### 变更 1

Before: The last thing I want to comment on before moving to the third situation is that we are considering unicast data packets.

After: [Um unclear], the last thing that I would like to comment, and then we go to the third situation, is remember that we are considering how to transmit unicast data packets, right? We said that.

理由：恢复would like、comment and then we go、is remember、how to transmit、right、We said that；不把句法改成before moving。

来源：Feishu historical snapshot: source_index=65, id=135, section anchor 01:05:29；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Unprompted Whisper medium.en raw: chunk-022, segments 18–21, absolute 3917.84–3957.58s；Unprompted Whisper medium.en raw: chunk-023, segments 1–1, absolute 3945.00–3957.64s


### 变更 2

Before: Let me mention again that multicast and broadcast data packets are much simpler, because we do not expect acknowledgments.

After: Let me just mention again that in the case of multicast or broadcast data packet, things are much, much simpler, because we do not expect any acknowledgement.

理由：恢复just、in the case of、or、data packet单数、things are much much、any acknowledgement单数。

来源：Feishu historical snapshot: source_index=65, id=135, section anchor 01:05:29；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-022, segments 21–23, absolute 3945.56–3971.28s；Unprompted Whisper medium.en raw: chunk-023, segments 1–2, absolute 3945.00–3966.04s


### 待听辨与来源限制

- [Um unclear], the last thing that I would like to comment, and then we go to the third situation, is remember that we are considering how to transmit unicast data packets, right?
  依据：Qwen 35 alone has Um; Feishu and medium omit the filler. Feishu/Qwen retain right and We said that, which medium omits.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第54段 01:06:05
段 ID：doxcnVDHtpDHmdLfVNMU7A5Z1nh


### 变更 1

Before: Since broadcast and multicast packets are intended for multiple destinations, we cannot have all the receivers sending acknowledgments back. If all those acknowledgments were sent at the same time, they would collide with one another. So that would be no use.

After: Indeed, since broadcast and multicast packets are intended for multiple destinations, we cannot have receivers sending back acknowledgments, because all these acknowledgments, if sent at the same time, will collide [with / within unclear] each other. So no use.

理由：恢复Indeed、receivers无all、sending back、because all these acknowledgments if sent、will collide with each other及So no use，不将will改would。

来源：Feishu historical snapshot: source_index=66, id=137, section anchor 01:06:05；Qwen recovery rerun raw: window_index=35, absolute 3850.00–3970.00s；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-022, segments 23–24, absolute 3963.26–3974.96s；Unprompted Whisper medium.en raw: chunk-023, segments 2–6, absolute 3957.64–3997.68s


### 待听辨与来源限制

- Indeed, since broadcast and multicast packets are intended for multiple destinations, we cannot have receivers sending back acknowledgments, because all these acknowledgments, if sent at the same time, will collide [with / within unclear] each other.
  依据：Feishu and Qwen 36: with each other; medium-023 segment 5: within each other. All use will; old draft's were/would is an unsupported tense rewrite.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- Section 54/55 boundary
  依据：The desynchronize sentence begins around 3988.92s, before the existing section-55 timestamp label 01:06:45 (4005s). The existing draft assigns this sentence to section 55.
  处理：保留现有段ID及时间标签；desynchronize句只放第55段，不根据粗略时间锚重复或挪动。


## 第55段 01:06:45
段 ID：doxcna5EZSQva8EAx8UH3RzbFKh


### 变更 1

Before: If you had to desynchronize the acknowledgment transmissions, that would be very, very complicated and would increase the protocol overhead. So that is not good.

After: If you had to desynchronize the acknowledgments transmissions, that would be very, very complicated. And [it / you unclear] would increase the overhead of the protocol. So that's [not good / done unclear].

理由：恢复acknowledgments transmissions、独立and ... increase及the overhead of the protocol；it/you和not good/done有冲突短标，不强行规范复数。

来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–7, absolute 3997.68–4007.12s


### 变更 2

Before: So the choice they made was: if a packet is broadcast or multicast, the transmitter of course needs to sense the channel. If it is idle, transmit. If it is busy, you have to perform backoff because you have to wait.

After: So the choice that they made was, well, if a packet is broadcast or multicast, the transmitter of course needs to sense the channel. If the channel is idle, transmit. If the channel is busy, of course, you have to perform the backoff procedure because you have to wait.

理由：恢复that they made、well、两次the channel、of course、the backoff procedure。

来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 7–10, absolute 3997.68–4039.06s


### 变更 3

Before: But once you access the channel and transmit, that's it; you are done. You don't care whether the packet was received successfully or unsuccessfully.

After: But then once you access the channel and transmit, that's it. Okay, you are done, because you don't care if the packet was received successfully or unsuccessfully. [You / we unclear] are done.

理由：恢复then、Okay、because、if和重复You are done；you/we冲突标出。

来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Unprompted Whisper medium.en raw: chunk-023, segments 10–12, absolute 4030.16–4058.40s


### 变更 4

Before: Broadcast and multicast packets are transmitted only once. You may need to run backoff for those data packets, but only if, when you want to access the channel, you sense the channel as busy the first time.

After: Okay, so broadcast and multicast packets are transmitted only once. So you may need to run the backoff procedure for those data packets, but just if, when you want to access the channel, you sense the channel as busy the first time, okay?

理由：恢复Okay so、So you may need、the backoff procedure、but just if及句尾okay，不以only if润色。

来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=36, absolute 3960.00–4080.00s；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 12–15, absolute 4049.74–4083.40s


### 变更 5

Before: Once you perform backoff, access the channel, and transmit, you are done. If everything is clear so far, let me know if you have questions. No questions? Okay, then we can tackle the last condition.

After: Then once you perform the backoff and you access the channel and transmit, you are done. Okay, [um unclear], if everything is clear so far, let me know if you have questions. No questions? Okay, so if we are good, then we can now tackle this last condition.

理由：恢复Then once、the backoff、and you、Okay、so if we are good、now、this last condition。

来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 15–18, absolute 4075.84–4117.66s


### 变更 6

Before: We have one more situation in which we perform backoff. In this third situation the procedure is slightly, slightly different. It is essentially the same except for one thing.

After: That is, well, we have one more situation under which we perform the backoff. In this third situation, actually, the procedure is slightly, slightly different, okay? [It is / is, is unclear] essentially the same except for one [thing unclear]. What is this third situation?

理由：恢复That is well、under which、the backoff、actually、Okay；保留slightly重复与one/one thing疑点、补回被删问句。

来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 18–21, absolute 4105.50–4143.94s；Unprompted Whisper medium.en raw: chunk-024, segments 1–2, absolute 4125.00–4138.36s


### 变更 7

Before: In this case the procedure is called post-backoff, to underline that there is a small difference from backoff run in the previous two situations.

After: [And it is called unclear], in this case the procedure is called [fast / post unclear] backoff, just to underline that there is a small difference with respect to the backoff run under the previous two situations.

理由：恢复And it is called的重启、just、with respect to、under；此处各ASR为fast backoff，不能仅据知识确写post-backoff。

来源：Feishu historical snapshot: source_index=67, id=139, section anchor 01:06:45；Feishu historical snapshot: source_index=68, id=141, section anchor 01:06:45；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-023, segments 21–22, absolute 4137.62–4154.62s；Unprompted Whisper medium.en raw: chunk-024, segments 3–4, absolute 4138.62–4157.50s


### 待听辨与来源限制

- And [it / you unclear] would increase the overhead of the protocol.
  依据：Qwen 36: it would increase the overhead of the protocol; medium-023 segment 7: you would increase the order of the problem. Feishu supplied section-55 fragment starts later. The technical noun is supported by Qwen; subject is unresolved.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So that's [not good / done unclear].
  依据：Feishu 67: that's not good; Qwen 36: that's done; medium omits this short sentence. Not silently adopting the fluent interpretation.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- [You / we unclear] are done.
  依据：Qwen 36: You are done; medium-023 segment 12: we are done; Feishu here is corrupted as a Spanish phrase. Restore the repeated done sentence but flag its subject.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- Okay, [um unclear], if everything is clear so far, let me know if you have questions.
  依据：Qwen 37 alone includes um; Feishu and medium omit it. Kept as a short unresolved filler.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- [It is / is, is unclear] essentially the same except for one [thing unclear].
  依据：Feishu: is, is essentially the same except for one; Qwen 37: It is essentially the same except for one thing; medium-023/024: It's essentially the same except for one. Do not silently add thing or discard the possible false start.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- [And it is called unclear], in this case the procedure is called [fast / post unclear] backoff, just to underline that there is a small difference with respect to the backoff run under the previous two situations.
  依据：Feishu: It is called in this case ... fast back off; Qwen 37: And indeed it is called in this case ... fast backoff; medium-023: And it is called ... fast back-off; medium-024 omits the restart and also says fast. Later section 58 has post backoff and medium section 60 has post; technical expectation does not certify the local word.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第56段 01:09:19
段 ID：doxcnSOlCgY8oM1YQQ6YaPFWmPg


### 变更 1

Before: What is this third situation? It is when a node transmits a data packet successfully.

After: So what is this third situation? [It is / is unclear] when a node transmits a data packet successfully.

理由：恢复So及is when前It有无的口语疑点；不根据语法自动补。

来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Unprompted Whisper medium.en raw: chunk-024, segments 5–5, absolute 4159.22–4168.92s


### 变更 2

Before: You may say: why do I have to perform backoff? I transmitted my packet correctly; I'm done. What do you want from me?

After: So you may say, well, why do I have to perform the backoff in this case? [I transmitted / I've transmitted unclear] my packet correctly, [I'm / and unclear] done. What do you want from me?

理由：恢复So、well、the backoff、in this case及I transmitted/I’ve transmitted时态冲突；保留对话原句。

来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 6–7, absolute 4169.94–4186.90s


### 变更 3

Before: Well, Wi-Fi says: I know you transmitted your packet and you are done with that, but after receiving the ACK from the receiver, you need to perform backoff using zero to CW_min as the range of possible integers. That's what the protocol says.

After: Well, the Wi-Fi says, I know you transmitted your packet, you are done with that, but after you receive the ACK from the receiver, you need to perform a backoff using zero, CW_min as range of possible integers. That's [what / why unclear] the protocol says.

理由：恢复the Wi-Fi、you receive、a backoff、using zero CW_min as range，不重写after receiving或补to/the。

来源：Feishu historical snapshot: source_index=69, id=143, section anchor 01:09:19；Qwen recovery rerun raw: window_index=37, absolute 4070.00–4190.00s；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 7–9, absolute 4178.02–4223.82s


### 待听辨与来源限制

- [It is / is unclear] when a node transmits a data packet successfully.
  依据：Qwen 37 and Feishu start with is when; medium-024 segment 5 has It is when.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- [I transmitted / I've transmitted unclear] my packet correctly, [I'm / and unclear] done.
  依据：Feishu/Qwen 37: I transmitted my packet correctly and done; medium-024: I've transmitted my packet correctly, I'm done. Both the tense and the short fragment before done remain unresolved.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- That's [what / why unclear] the protocol says.
  依据：Feishu and medium-024: That's what the protocol says; Qwen 38: That's why the protocol says. Most of the preceding clause is supported by medium and Qwen, despite Qwen's transmit in your pocket corruption.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第57段 01:10:13
段 ID：doxcnYKp8xXaOwlMx8lzDMPjmEh


### 变更 1

Before: Again, we want to understand why. This is not enough: okay, I have to do it, I will do it, but tell me why. Why do I have to do that? The reason is fairness. We want to be fair to our nodes.

After: So again, we want to understand why, right? [I mean / maybe unclear], this is not enough. Okay, I have to do it, I will do it, but tell me why, why do I have to do that? Well, the reason is fairness. We want to be fair to our nodes.

理由：恢复So、right、I mean及Well；保留I have to/I will重复，不压缩。

来源：Feishu historical snapshot: source_index=70, id=145, section anchor 01:10:13；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 9–10, absolute 4194.68–4235.92s


### 待听辨与来源限制

- [I mean / maybe unclear], this is not enough.
  依据：Feishu and Qwen 38: I mean; medium-024 segment 9: maybe. Flag the local phrase without overwriting the broader sentence.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第58段 01:10:32
段 ID：doxcnBdnbpPGhKGwvSK0xHE3Xkf


### 变更 1

Before: Let me give an example that will allow us to understand why they tell us to run post-backoff once we transmit successfully.

After: Okay, so let me give [you unclear] an example, and that will allow us to indeed understand why they tell us, once you transmit successfully, run this post-backoff.

理由：恢复Okay So、and that will、indeed、引述once you transmit successfully run this post-backoff；give you有无标示。

来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 10–12, absolute 4223.82–4263.48s


### 变更 2

Before: Let's consider the same scenario again: an access point, node A, and our B and C nodes, as before. We already know the story, so it will be easier.

After: So let's consider again the same scenario, so that will be easy. Access point, and then node A. And then we can also consider our B and C nodes, right? Same as before. So we know [already / that with unclear] the story, it will be easier.

理由：恢复So、again the same scenario、so that will be easy、碎片Access point and then node A、And then we can also、right及Same as before；we know already来源冲突短标。

来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Unprompted Whisper medium.en raw: chunk-024, segments 12–14, absolute 4254.16–4284.52s


### 变更 3

Before: It starts in the same way. A has a packet, senses the channel for DIFS, finds it idle, and transmits its unicast data packet to the access point. The transmission is successful, so the access point sends back the ACK.

After: So the story starts in the same way. A has got a packet, [DIFS unclear], channel idle, transmits the data packet, unicast data packet to the access point. This packet transmission is successful, so the access point [sends / sent unclear] back the ACK.

理由：恢复So the story starts、has got、DIFS/channel idle碎片与data packet / unicast data packet重复；撤销现稿补出的senses/finds动词，ACK前动词待听辨。

来源：Feishu historical snapshot: source_index=71, id=147, section anchor 01:10:32；Qwen recovery rerun raw: window_index=38, absolute 4180.00–4300.00s；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 15–17, absolute 4285.52–4323.38s；Unprompted Whisper medium.en raw: chunk-025, segments 1–1, absolute 4305.00–4316.38s


### 待听辨与来源限制

- Okay, so let me give [you unclear] an example, and that will allow us to indeed understand why they tell us, once you transmit successfully, run this post-backoff.
  依据：Qwen 38: give you an example; Feishu and medium-024 segments 10–11: give an example. Indeed is Qwen's clear reading, with Feishu in beat / medium in winter near-phonetic corruptions. Post-backoff is clear in Feishu, Qwen has post pickoff, medium hospital.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So we know [already / that with unclear] the story, it will be easier.
  依据：Qwen 38: we know already the story; Feishu: we know that if the story; medium-024 segment 14: we know that with the story. The current fluent paraphrase cannot settle this local wording.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- A has got a packet, [DIFS unclear], channel idle, transmits the data packet, unicast data packet to the access point.
  依据：Feishu/Qwen/medium all render the short item after packet as leaves. DIFS is a strong technical near-phonetic possibility, not locally clear. None supplies the current draft's expanded senses the channel for / finds it / its phrasing.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- This packet transmission is successful, so the access point [sends / sent unclear] back the ACK.
  依据：Qwen 39: access points have back the ACK; medium-024/025: access points have backed the ACK; Feishu fragment ends before this. Sends/sent is a plausible reconstruction of the garbled verb, not audio-certified.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第59段 01:11:51
段 ID：doxcnWJukIbTM7WOpJFug42kc4d


### 变更 1

Before: As we said before, all nodes are in radio visibility of each other; they can hear each other. B and C therefore set their NAV.

After: And as we said before, all nodes are in radio visibility of each other, they can hear each other. So B and C will set their [NAV unclear].

理由：恢复And、So及will；NAV保留局部听辨标示，不把NAT/noth等粗糙ASR当音频确认。

来源：Feishu historical snapshot: source_index=72, id=149, section anchor 01:11:51；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 17–18, absolute 4304.78–4334.68s；Unprompted Whisper medium.en raw: chunk-025, segments 1–2, absolute 4305.00–4326.30s


### 变更 2

Before: As before, at a certain point they get a packet from their respective higher layers, so they will have to transmit their packets.

After: And same as before, at a certain point B and C get a packet from their respective higher layers, so they will have to transmit their packet, right?

理由：恢复And same as before、第二次B and C、their packet单数及right；不以they替换节点名。

来源：Feishu historical snapshot: source_index=72, id=149, section anchor 01:11:51；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-024, segments 18–18, absolute 4323.38–4334.68s；Unprompted Whisper medium.en raw: chunk-025, segments 3–4, absolute 4326.30–4349.54s


### 待听辨与来源限制

- So B and C will set their [NAV unclear].
  依据：Medium-025 segment 2: will set their NAT; Feishu: will send their noth; Qwen 39: will say they are not. NAV is the intended protocol term strongly indicated by earlier exposition, but the local word is garbled in all supplied ASRs.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。


## 第60段 01:12:20
段 ID：doxcnJy0CfZy89ROVTTTAPVxpFe


### 变更 1

Before: We already know how things work, but now our attention is on A. Let's focus on A. A is the one that performed its transmission successfully, so it is done.

After: And we know already how things work, fine, but now our attention is on A, okay? Let's focus on A. A is the one that performs its transmission successfully, so it's done.

理由：恢复And we know already、fine、okay与performs现在式，不能沿现稿performed。

来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 4–6, absolute 4336.56–4375.04s


### 变更 2

Before: According to the protocol, once A has finished transmitting the packet and received the ACK, it needs to perform post-backoff.

After: And according to the protocol, now we know that A actually, once it has finished transmitting the packet and [received / receive unclear] the ACK, needs to perform this [post / past / fast unclear] backoff procedure, right?

理由：恢复And、now we know that、A actually、this ... procedure、right及received/receive词尾冲突。

来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Unprompted Whisper medium.en raw: chunk-025, segments 6–8, absolute 4366.02–4394.90s


### 变更 3

Before: It has to sense the channel for DIFS and then draw an integer from zero to CW_min.

After: So [it / I unclear] will have to sense the channel for [DIFS unclear], and then [it / you / we unclear] will have to draw an integer out of the range zero, CW_min.

理由：恢复So、will have to两次与out of the range，主语it/I/you/we来源分歧标示，不把未来式改现在式。

来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 8–9, absolute 4384.48–4406.84s


### 变更 4

Before: B and C behave as before; we know that already. They have to run a regular backoff procedure.

After: And of course for B and C we'll have the same behavior as before. We know [that already / that's ready unclear]. So B and [and unclear] C will have to run a, let's say, regular backoff procedure.

理由：恢复And of course for B and C we’ll have、So B and C will have to、a let’s say regular及that already疑点；保留源中and and重复可能。

来源：Feishu historical snapshot: source_index=73, id=151, section anchor 01:12:20；Qwen recovery rerun raw: window_index=39, absolute 4290.00–4410.00s；Qwen recovery rerun raw: window_index=40, absolute 4400.00–4520.00s；Unprompted Whisper medium.en raw: chunk-025, segments 9–11, absolute 4394.90–4432.24s


### 待听辨与来源限制

- And according to the protocol, now we know that A actually, once it has finished transmitting the packet and [received / receive unclear] the ACK, needs to perform this [post / past / fast unclear] backoff procedure, right?
  依据：Qwen 39: received ... past backoff; Feishu: receive ... fast bake off; medium-025: receive ... post bake-off. The post prefix has local medium support and section-58 context, but source disagreement is explicit. Received/receive is not silently grammatically corrected.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So [it / I unclear] will have to sense the channel for [DIFS unclear], and then [it / you / we unclear] will have to draw an integer out of the range zero, CW_min.
  依据：Qwen 39: it will ... it will; medium-025: I will ... you will; Feishu: I will ... we will. All give leaves for the timing term; DIFS is the technical reconstruction, marked rather than certified. All retain future will have to.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- We know [that already / that's ready unclear].
  依据：Feishu, Qwen 40 and medium-025 all approximate that's ready. That already is plausible from the lecturer's meaning but not established locally.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。

- So B and [and unclear] C will have to run a, let's say, regular backoff procedure.
  依据：Feishu repeats and and; Qwen 40 and medium-025 have and once and both retain let's say, omitted from the current draft. The local technical word is go/cough/kickoff in the rough ASRs, normalized as backoff with context.
  处理：保留短标与中文待听辨；来源比较候选，未作亲耳听辨。
