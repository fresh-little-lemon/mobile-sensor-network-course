# 20261012-1331 第09段（00:09:40）原音ASR复核

## 结论

现稿主题与这段录音的机器转写基本一致，但不能作为逐字稿：它合并了完整的重复解释，改写了句式、时态和词序，并删掉了多个口语连接词、限定语和问句尾词。该结论来自真实原音推理；不是把现稿重新润色。尚未做人工听辨，不能宣布候选改稿已经完全准确。

三份主结果分别使用faster-whisper base.en、small.en、medium.en，在同一09:10–11:50（160秒）窗口上独立运行，language=en，无initial_prompt，无前段文本条件，无VAD，beam_size=5、temperature=0、word_timestamps=true、CPU int8。它们同属Whisper体系，可能有共同错误。另保存两份只给术语短表的重跑及一份疑点短窗重跑，均未输入现稿全文或句子。

原音：20261012-1331.m4a，5622.281333秒，139451685字节，AAC/48kHz/双声道。SHA256：b710201745efeb5071757d4e3b086ce30937f038bbe1bbe6ae18bd74aa7239ff。用于主跑的16kHz单声道PCM裁片SHA256：2c0c982ddba76c71f2c87caace541949afe560e69f05c799dedbc2c4b70232cf。

## 逐句差异证据

以下为原音绝对时间，边界由模型估计，不是人工校准。

1. 09:40.6–09:53.3
   - 现稿：So we need to recontend for the channel and transmit the packet again. This is the case we have considered so far in which we need to perform backoff.
   - 主ASR共同支持的结构：So we need to recontend for the channel and transmit the packet again, right? This is the phase that we have considered so far under which we need to perform the ...
   - 差异：right、that、the被省略；under which改成in which。三模型均输出phase，现稿写case，但模型一致不能排除共同误识别，phase/case仍待听辨。backoff在无提示跑被错成become等，术语表重跑恢复backoff。

2. 09:54.2–10:10.7
   - 现稿：However, there are two more situations in which we need to perform exactly the same backoff procedure.
   - 三份主ASR均保留：However, there are two more situations under which we need to perform a ... procedure, exactly as we explained, the same procedure that we just explained.
   - 差异：现稿把两个完整重复从句exactly as we explained和the same procedure that we just explained压成exactly the same。这是最清楚的非逐字证据。

3. 10:13.0–10:36.0
   - 现稿：It also needs to be performed when a transmitting node has a packet to transmit, senses the channel, and finds it busy.
   - medium.en无提示：This procedure indeed needs to be performed also when a node, a transmitter, has got a packet to transmit, it senses the channel but the ... is busy right.
   - small.en保留the channel is busy，medium.en术语表跑也完整保留该词组。
   - 差异：This procedure indeed改成It；a node, a transmitter压成a transmitting node；has got改成has；but the channel is busy改成and finds it busy。中间when a node的识别在小模型中不稳定；medium两次支持此读法。senses前代词：medium两次it，小模型he，暂不定稿。

4. 10:36.4–10:49.5
   - 现稿：We already know that we cannot access the channel right away because of the carrier-sense multiple-access principle.
   - 三份主ASR支持：So we already know that in this case we cannot access the channel right away because of the carrier sensing multiple access principle, right?
   - 差异：So、in this case、right被删；sensing被规范化成sense。意义大体保留，口述形式改变。

5. 10:50.1–11:04.9
   - 现稿：We get a packet from the higher layers, and at the MAC layer we sense the channel for DIFS, but it is busy.
   - 三份主ASR支持的非术语部分：So if we sense the channel, we got the packet from the higher layers. At the ... layer we sense the channel for ..., but the channel is busy.
   - 差异：So if we sense the channel被删除；we got the packet被改成We get a packet；补了and；the channel被改成it。原口语的停顿/接续不顺，不能因不顺而默默重写。
   - MAC在模型中出现map/monthly/max/math/matte；DIFS出现this/dibs。MAC、DIFS可列为课程语境下的术语规范化候选，但这些拼写没有获得无歧义的ASR验证。末尾right/okay各模型不一致、分数低，待听辨。

6. 11:05.1–11:21.3
   - 现稿：What we knew so far is that we cannot access the channel because it is busy. We are like polite people; we don't want to interrupt someone who is already talking.
   - 三份主ASR支持：So what we knew so far is that in this case we cannot access the channel, right? Because the channel is busy. We are like polite people. We don't want to ... someone who is talking already.
   - 差异：So、in this case、right被删；because the channel is busy改成because it is busy；talking already改成already talking。medium无提示与两份术语表跑支持interrupt；base/small主跑误识别或候选为interact with，仍需复听后确认。

## 相邻段边界

第09段最后的talking already约到11:21.3。So we wait约在11:21.3–11:22.7，属于第10段00:11:21起点。约11:25再次We wait，三份主ASR均支持，现稿第10段只保留了一次。不要把第二次We wait追加到第09段。建议第10段开头候选为：So we wait. We wait. That's what we said, but now we need to be more precise...

另：small.en术语表跑在11:17.66产生了零时长的第二个We，其他主结果不支持；该重复没有加入候选稿。

## 候选稿使用规则

revision-candidate.txt和revision-candidate.json给出完整第09段英语候选和对应直译。保留口语重复和不顺的接续，不按书面语补出未被模型支持的意思。方括号明确标出仍有冲突的词。backoff、MAC、DIFS属于显式术语规范化，原始JSON保持不变。

该稿是待听辨草稿，不能称作最终逐字稿，不应自动覆盖飞书或现有双语正文。需要先核验：09:46.8的phase/case、10:20–10:31的when a node及it/he、10:55–11:05的MAC/DIFS和尾词、11:18的interrupt/interact with。

已准备4个12–15秒复听片段，仅保存在本地，不在文本备份中包含音频：09:44–09:56、10:17–10:32、10:53–11:05、11:14–11:29。
