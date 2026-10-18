# 20261012-1331 四处候选边界 QA

生成时间：2026-10-18T15:36:27.682005+00:00

## 结论

四处边界的恢复语句均连续覆盖，未检出整句漏失或ASR重叠造成的重复；真实复说及潜在重复仍保留或显式待听辨。发现4项边界相关元数据/不确定性说明问题，已单列补充而未修改候选。

只读核对原候选、三来源review packet与medium原始词级时间；未回听、未改候选、未对外写入。PASS不等于音频逐字认证。

## 20/21 — PASS_TEXT_CONTINUITY_WITH_METADATA_CAVEAT

左段尾：So, B will say, “[Hmm ... unclear] I got [a / the unclear] packet, but the channel is busy.”
右段首：What I need to do is to apply backoff.

### 逐条证据
1. 候选20以 B will say ... I got [a / the unclear] packet, but the channel is busy 结束；候选21从 What I need to do is to apply backoff 开始。两个意义单元各保留一次，顺序与Qwen window12及medium chunk-008 segment12一致。
2. medium chunk-008 segment12（1358.80–1368.02s）同时含20末句及21首句。它被两个review packet重复收录，是同一个segment的归段上下文，不是两次讲述。原始词级时标：busy结束1362.78s，What从1363.78s开始；21的旧锚点1363s位于两者之间。
3. Feishu block53（source_index_zero_based=24，00:22:43）恰从What I need to do开头；20对应Feishu块49/51缺末尾B自述，因此末尾恢复依赖Qwen与medium，不可误判为凭空增补。
4. Qwen window11/12在1320–1330s重叠，B and C get/got a new packet是同一事件的双窗口输出，候选20只保留一次；21没有再次复制。

漏失：未检出边界整句或可确认单词漏失；21第二句的So what开头仍在正文，虽其medium索引漏了segment12。
重叠重复：未检出ASR窗口或review-packet重叠引起的正文重复。

保留的讲者重复或待听辨重复：
- 20内部 situation, situation number one 被保留
- B自述channel is busy之后，21中C再述channel is busy属于不同节点的连续例子；Qwen window12和medium的不同时间段分别支持，不能按相似句去重
- 21句末channel will be idle ... so the channel is idle的重复保留；两个medium窗口的同一结尾仅写一次

不能排除／未决：
- 20末尾Hmm有无和a/the冠词未听辨
- 21第二句it will / you will / medium you do分歧仍未解决
- 机器词时标不是人工音频边界认证

证据定位：
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-01-20.json
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-21-40.json
- /workspace/shared/course-1012-1331/asr-full-20261018/chunk-008.raw.json

## 38/39 — PASS_TEXT_CONTINUITY_WITH_METADATA_CAVEAT

左段尾：There are CW_min...
右段首：Plus one integers, right?

### 逐条证据
1. 候选38尾There are CW_min...与39首Plus one integers, right?合并后正好是There are CW_min plus one integers, right?；CW_min、plus one、integers、right均未因拆段遗漏或复制。
2. medium chunk-014 segment18（2505.02–2515.34s）和chunk-015 segment1（2505.00–2511.08s）给出同一句的重叠识别；两者起始相差0.02s，不能当成讲者讲了两遍。候选只保留一个计数句。
3. Qwen window22（2420–2540s）仅含一次There are CWmin plus one integers, right?；随后另有including the zero is plus one。这后一个plus one是讲者解释零计入计数的独立短语，候选39保留，不能与前一个plus one合并。
4. Feishu block99（41:48）以损坏的Flashwanna interjurbrive开头，支持旧段39从plus one附近起；旧锚点2508s不是已认证逐词切点。chunk-014词对齐为min结束2507.64s、plus开始2508.48s；chunk-015则mean结束/plus开始2507.66s，存在0.82s窗口间对齐差异。

漏失：未检出边界计数句漏词；拆段省略号是编辑性衔接标记，不能解读为已证实的讲者停顿或省略语。
重叠重复：未检出ASR窗口重叠引起的正文重复；完整计数句仅保留一次。

保留的讲者重复或待听辨重复：
- 候选38保留as a possible range, as a range of possible integers的复说
- 候选38将in / in in显式待听辨，没有因机器去重删除可能的讲者重复
- plus one计数与including the zero is plus one解释均保留，整对候选中plus one共2次，属于不同时间位置

不能排除／未决：
- Because / We call this minimum / We call this a unit等分歧未能排除；39只将Because之后标为unclear，不能把Because本身视作已证实
- in重复次数仍需回听
- chunk-014/015词对齐不一致，不能声称2508s精确落在词间；不影响按旧ID保留完整句子

证据定位：
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-21-40.json
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-21-40.json
- /workspace/shared/course-1012-1331/asr-full-20261018/chunk-014.raw.json
- /workspace/shared/course-1012-1331/asr-full-20261018/chunk-015.raw.json

## 54/55 — PASS_TEXT_CONTINUITY_WITH_METADATA_CAVEAT

左段尾：So no use.
右段首：If you had to desynchronize the acknowledgments transmissions, that would be very, very complicated.

### 逐条证据
1. 候选54在So no use结束；候选55从If you had to desynchronize the acknowledgments transmissions, that would be very, very complicated起。Qwen window36连续包含这两句，候选没有丢掉早于55旧锚点的首句。
2. medium chunk-023 segment6（3988.92–3997.68s）横跨no use和If you had to desynchronize ... that would；segment7（3997.68–4007.12s）续be very very complicated and ...。按raw词级时标，use结束3990.12s，If开始3990.82s，complicated结束3999.20s。
3. 55旧锚点01:06:45=4005s晚于这整个desynchronize句；以旧锚点硬裁会漏句。现候选遵循旧段落归属把句子只放55，连续性正确。
4. Feishu block137（54来源）以So no use结束，block139（55来源）从So that's not good开始，中间desynchronize/overhead两句在Feishu映射中缺失；Qwen36与medium6–7提供恢复依据。
5. chunk-022/023在54开头Indeed since broadcast...有重叠，候选54只保留一次；54/55实际转接点位于同一chunk-023中，不存在第二次desynchronize。

漏失：未检出正文边界漏句；55提前于其旧锚点的desynchronize和overhead内容均保留。
重叠重复：未检出窗口重叠造成的正文重复；desynchronize句在54/55合并中仅一次。

保留的讲者重复或待听辨重复：
- very, very complicated在Qwen36与medium segment7均为双very，候选55确实保留两个very；这是同一窗口内的词级重复，不是相邻窗口重复
- 55后文you are done / [You / we unclear] are done / you are done位于不同语句和不同时间位置，均保留

不能排除／未决：
- 54 with / within仍未听辨
- 55 it / you、overhead of the protocol / medium order of the problem以及not good / done存在来源分歧；归段无漏不等于这些词已认证
- 54的unresolved证据把segment6起点3988.92s近似作为desynchronize句起点；词级If实际3990.82s，须表述为大致窗口而非精确句始

证据定位：
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-41-60.json
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-41-60.json
- /workspace/shared/course-1012-1331/asr-full-20261018/chunk-023.raw.json

## 60/61 — PASS_TEXT_CONTINUITY

左段尾：So B and [and unclear] C will have to run a, let's say, regular backoff procedure.
右段首：So again, in order to understand how useful [a / the unclear] mechanism is, or solution is, let's play our little game of ablation, right?

### 逐条证据
1. 候选60尾regular backoff procedure后，候选61接So again, in order to understand how useful ...。Qwen window40和medium chunk-025 segment11均按此顺序连续出现，没有需要额外补入的中间句。
2. medium chunk-025 segment11（4421.20–4432.24s）同时覆盖60末尾与61开头，两个review packet复用的是同一segment；60未复制So again，61未重复制procedure。词级procedure结束4422.92s，So开始4424.70s；61旧锚点4424s位于该间隔内。
3. Feishu block151以regular kickoff procedure结尾，block153从So again开头，与候选归属吻合；Qwen window39/40在4400–4410s重叠的zero CW_min / same behavior as before只在60保留一次。

漏失：未检出边界整句或可确认单词漏失；let's say仍在60末句，61保留mechanism is, or solution is的复说。
重叠重复：未检出窗口或review-packet重叠引起的正文重复。

保留的讲者重复或待听辨重复：
- 60中and [and unclear] C保留潜在重复并标记不确定
- 61中mechanism is, or solution is保留两次is与自我补说结构
- 61中any, [any unclear]保留Qwen的可能双any；没有因单词重复擅自去重

不能排除／未决：
- 60的and重复、61的a/the冠词与any重复仍待听辨
- 技术词backoff由跨源/上下文恢复，medium末尾the cough procedure不是逐字认证

证据定位：
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-41-60.json
- /workspace/shared/course-1012-1331/asr-full-20261018/review-packets/sections-61-78.json
- /workspace/shared/course-1012-1331/asr-full-20261018/chunk-025.raw.json

## 元数据 QA 补充（不改正文）

### M21-START-END — INCOMPLETE_MEDIUM_SENTENCE_REFERENCE
- 位置：第21段，第2句
- 发现：句2的medium引用只列chunk-008 segments13,14（1368.02–1391.80s）；So what you在segment12尾（1367.50–1368.02s），draw an在14末但integer在15首。正文完整，引用范围不覆盖整句。
- 补充证据：chunk-008 segment12–15，1358.80–1410.30s；按词对齐句首So=1367.50s。right在Qwen/Feishu有支持，medium segment15不含right。

### M38-TIMING-SOURCE — SOURCE_LABEL_MISMATCH_FOR_WORD_TIMING
- 位置：第38段，第8句
- 发现：候选注释说CW_min结束41:47.64、plus开始41:48.48，但只列chunk-015 segment1。上述精确数值实际来自chunk-014 segment18。chunk-015给mean结束与plus开始均2507.66s。
- 补充证据：精确数值应指向chunk-014.raw.json segment18（offset2325s），并同时注明chunk-015 segment1对齐不同；原锚点仅作旧段落定位，不声称人工验证词间停顿。

### M39-BECAUSE-SOURCE — ALTERNATE_SOURCE_NOT_IN_SENTENCE_REFERENCE
- 位置：第39段，第2句
- 发现：候选Because [unclear words]的medium引用只列chunk-015 segment2，但该段原文是We call this a unit ...。Because the subunit来自同时间的chunk-014 segment18，候选uncertainty描述Whisper但未区分两个窗口。
- 补充证据：补列chunk-014 segment18；把Because / We call本身也作为未决读法，不可将Because视作稳定跨源词。此问题不构成边界漏句或窗口重复。

### M55-MISSING-SEG6 — INCOMPLETE_MEDIUM_SENTENCE_REFERENCE
- 位置：第55段，第1句
- 发现：首句只列chunk-023 segment7（3997.68–4007.12s）；If you had to desynchronize ... that would实际在segment6（3988.92–3997.68s），该段仅被收在54的review packet。Feishu块139/141不包含该首句，不能单凭它们验证。
- 补充证据：该句应补指向54来源包内chunk-023 segment6，再接segment7；完整segment级证据3988.92–4007.12s。词级If=3990.82s，complicated结束3999.20s。Qwen36提供独立连续句支持。

## 适用限制

- 仅能判断已提供ASR/历史文本覆盖与归段，不能证明音频中不存在所有ASR共同漏掉的口语、停顿或单词。
- 历史Feishu可能已有编辑和识别错误；Qwen是恢复重跑，不是遗失首次输出的逐字重放。
- review packets报告新旧输入m4a SHA256不同，内容和时间有上下文支持但字节相同未建立；不能称PCM哈希一致。
- medium词级时标来自ASR对齐，不是人工听辨认证；尤其38/39邻窗词边界存在0.82s差异。
- PASS仅针对指定边界的文本覆盖/去重，不代表78段逐字忠实度通过或可以作为最终听辨版发布。

输入SHA256、原始时间戳词证据和可机器核验计数见同名JSON。
