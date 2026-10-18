# 20261012-1331 · 第01–20段忠实恢复候选

仅本地候选，未写回飞书，未逐句人工听辨。方括号为待听辨；讲者重复、时态、口语语法与限定语保留。中文逐句对应，正文每段英文下紧接中文。

来源：原飞书历史快照、校订前Qwen恢复输出、新无提示medium.en及09段独立短窗；来源分歧不以模型票数裁定。原飞书可能已人工编辑，Qwen不是丢失首次输出；旧、新M4A哈希不同，尚未取得旧音轨作等同性验证。

## 01 · 00:00:03

And we said that whenever [a/the unclear] Wi-Fi node needs to recontend for the channel, because this node has to retransmit [a/the unclear] packet that failed, then this node will perform the backoff procedure.
而且我们说过，每当[一个/这个待听辨] Wi-Fi 节点需要重新竞争信道，因为这个节点必须重新发送[一个/这个待听辨]发送失败的数据包，那么这个节点就会执行退避过程。

## 02 · 00:00:29

And we explained how the backoff procedure works. Okay? Now, we [said/send unclear] that first a node needs to wait for the channel to be idle for DIFS. Then [it/you unclear] will draw an integer out of a range of possible values with equal probability, selecting each of them with equal probability. And this range of values goes from zero to the contention window parameter, okay? The first time that we use the backoff procedure to transmit a packet, we set this contention window parameter to its minimum value. And then, if we need to perform the backoff procedure again in order to transmit this packet, because, for example, we fail and fail and fail, every time we will increase the value of contention window. And we said, roughly speaking, this value of contention window doubles every time, right? Now, to be more precise, the relation according to which the CW parameter increases is the following. So, CW value is actually expressed as a power of two minus one, where this exponent is called backoff exponent.
而且我们解释过退避过程是怎样工作的。好吗？现在，我们[“说过/发送”待听辨]，首先一个节点需要等待信道空闲一个 DIFS。然后[它/你待听辨]会以相等的概率从一组可能的值中抽取一个整数，以相等的概率选择其中的每一个。而且这个取值范围从零到竞争窗口参数，好吗？第一次我们使用退避过程来发送一个数据包时，我们把这个竞争窗口参数设为它的最小值。然后，如果我们需要再次执行退避过程来发送这个数据包，因为，例如，我们失败、失败、再失败，每一次我们都会增大竞争窗口的值。而且我们说过，粗略地说，竞争窗口的这个值每次都会翻倍，对吧？现在，更准确地说，CW 参数据以增大的关系是下面这个。所以，CW 的值实际上表示为二的一个幂减一，其中这个指数叫作退避指数。

## 03 · 00:02:48

Okay? So, for example, the first time that we use the backoff procedure for a data packet, we set the, so the first time, we set the backoff exponent to the backoff exponent minimum, okay? Now, by default, in the early versions of Wi-Fi, this is equal to five, okay? This is an example that refers to the early versions of Wi-Fi, okay? Now, so, if we take this example here, this example value here, we see that, as we said last time, the first time that we use this contention window minimum, the value will be two to the power of the minimum exponent minus one. Since this is five, right, this will be two to the five minus one, which is 31, right? So that's why, yes, on Saturday, when we [introduce/produce tense unclear] this procedure, we said, well, let's consider the minimum contention window 31, okay? Then, the second time that we use the backoff procedure for the same packet, we are going to increase the backoff exponent. So, if this was our first value, the second time, [sorry unclear], we'll have second value, right, that is equal to what, is equal to the previous one plus one.
好吗？所以，例如，第一次我们对一个数据包使用退避过程时，我们设置这，所以第一次，我们把退避指数设为退避指数最小值，好吗？现在，默认地，在早期版本的 Wi-Fi 中，这等于五，好吗？这是一个指的是早期版本的 Wi-Fi 的例子，好吗？现在，所以，如果我们采用这里的这个例子，这里的这个示例值，我们看到，正如我们上次说过的，第一次我们使用这个竞争窗口最小值时，这个值会是二的最小指数次方减一。因为这是五，对吧，这会是二的五次方减一，也就是 31，对吧？所以这就是为什么，是的，在星期六，当我们[“介绍/产生”及其时态待听辨]这个过程时，我们说，嗯，让我们考虑最小竞争窗口 31，好吗？然后，第二次我们对同一个数据包使用退避过程时，我们要增大退避指数。所以，如果这是我们的第一个值，第二次，[“抱歉”待听辨]，我们会有第二个值，对吧，它等于什么，等于前一个值加一。

## 04 · 00:05:24

Okay? So this means that the second time that we have to compute the contention window, this will be equal to two to the power of the, the backoff exponent [on/at unclear] the second step minus one, which is two to the backoff exponent [on/at unclear] the first step increased by one minus one, right?
好吗？所以这意味着，第二次我们必须计算竞争窗口时，这会等于二的这个、这个[on/at 介词待听辨]第二步的退避指数次方减一，这就是二的“[on/at 介词待听辨]第一步的退避指数加一”次方减一，对吧？

## 05 · 00:06:01

So now this is two to the power, in our example, to the power of six minus one, which is 63, okay? So this is the way we increase the contention window minimum value every time till, as we said, we reach this value, CW max. After we reach this value, we do not increase [the/this unclear] CW value any longer [beyond/behind unclear] this value, even if we need to still perform the backoff procedure for the same time.
所以现在这是二的次方，在我们的例子中，是六次方减一，也就是 63，好吗？所以这就是我们每次增大竞争窗口最小值的方式，直到，正如我们说过的，我们达到这个值，CW max。在我们达到这个值之后，我们不再把[限定词待听辨] CW 值增大到这个值的[以上/后面待听辨]，即使我们还需要为同一次执行退避过程。

## 06 · 00:06:57

So, the general, [ah unclear] the general rule is that at step i, the generic step i, we set the backoff exponent [at/as unclear] step i equal to the backoff exponent [at/and unclear] the previous step increased by one, right?
所以，一般的，[语气词待听辨]一般规则是，在第 i 步，任意的第 i 步，我们把[在/作为待听辨]第 i 步的退避指数设为[在/以及待听辨]前一步的退避指数增加一，对吧？

## 07 · 00:07:28

And at the generic step i, the contention window will be computed as two to the power of the backoff exponent at step i minus one. Okay, this is the general expression that we use to compute the, the backoff exponent and the corresponding contention window at each step. Okay, that said, therefore we understand that [every time/at every time unclear] that we need to perform the backoff for a given data packet, we roughly double the contention window, as we said. Okay, so we are going to [enlarge/launch unclear] the possible values, integer values, that we can draw to compute [backoff repetition unclear] time. Okay, so before explaining why we do that, okay, why the [standard said/standards say unclear] let's double the contention window every time we need to perform a backoff to transmit [a/the unclear] packet. So before explaining the reason because we do that, let me mention what was reported in one of the earlier slides.
而且在任意的第 i 步，竞争窗口将被计算为二的第 i 步的退避指数次方减一。好，这就是我们用来计算每一步的这个、这个退避指数和相应竞争窗口的一般表达式。好，说到这里，因此我们明白，[“每一次”前介词待听辨]我们需要对一个给定的数据包执行退避时，我们大致把竞争窗口翻倍，正如我们说过的。好，所以我们要[“扩大/发起”待听辨]那些可能的值，整数值，我们可以抽取它们来计算[“退避”的重复待听辨]时间。好，所以在解释我们为什么这样做之前，好，为什么[“标准说”的单复数和时态待听辨]让我们每次需要执行一次退避来发送[一个/这个待听辨]数据包时把竞争窗口翻倍。所以在解释因为我们这样做的原因之前，让我提一下前面一张幻灯片中报告过的内容。

## 08 · 00:09:04

But I didn't comment on that because I didn't want to put too many things at the same time. But one more thing that we need to say important about the backoff is that the backoff procedure, of course, it is performed, as we said, when we have essentially a packet, right, that has been transmitted and it failed.
但我没有对此作解释，因为我不想同时放入太多事情。但还有一件我们需要说的重要的关于退避的事情，是退避过程，当然，它会被执行，正如我们说过的，当我们基本上有一个数据包，对吧，它已经被发送了，而且它失败了。

## 09 · 00:09:40

So, we need to recontend for the channel and transmit the packet again, right? This is the [case/phase unclear] that we have considered so far, under which we need to perform the backoff. However, there are two more situations under which we need to perform a backoff procedure, [okay? unclear] Exactly as we explained, [okay? unclear] The same procedure that we just explained. This procedure indeed needs to be performed also when a node, a transmitter [wording unclear], has got a packet to transmit. It senses the channel, but the channel is busy, right? So, we already know that in this case, we cannot access the channel right away because of the carrier sensing multiple access principle, right? So, if we sense the channel, we got [a/the unclear] packet from the higher layers. At the MAC layer, we sense the channel for DIFS, but the channel is busy, [okay/right unclear] So, what we knew so far is that in this case, we cannot access the channel, right? Because the channel is busy. We are like polite people. We don't want to interrupt someone who is talking already.
所以，我们需要重新竞争信道，并且再次传送这个数据包，对吧？这就是我们到目前为止考虑过的这个〔case/phase，情况/阶段，待听辨〕，在这种情况下，我们需要执行这个退避。不过，还有另外两种情况，在这些情况下，我们需要执行一个退避过程，〔okay?，好吗？待听辨〕正如我们解释过的那样，〔okay?，好吗？待听辨〕就是我们刚刚解释过的同一个过程。这个过程确实也需要在一个节点、一个发送方〔此处措辞待听辨〕有了一个要传送的数据包时执行。它侦听信道，但是信道是忙的，对吧？所以，我们已经知道，在这种情况下，因为载波侦听多址接入的原则，我们不能马上接入信道，对吧？所以，如果我们侦听信道，我们从更高层拿到了〔a/the，冠词待听辨〕数据包。在MAC层，我们侦听信道一个DIFS的时间，但是信道是忙的，〔okay/right，好吗/对吧，待听辨〕所以，我们到目前为止知道的是，在这种情况下，我们不能接入信道，对吧？因为信道是忙的。我们就像有礼貌的人。我们不想打断一个已经在讲话的人。

## 10 · 00:11:21

So, we wait. We wait. That's what we said, but now we need to be more precise. What do we mean exactly that we need to wait? [question wording unclear] For how long? Well, in reality, also in this case, what we need to do is to apply the backoff procedure. So, how long do we wait for? We will wait for the backoff time, according to this procedure. So, this is the rule again. Also in this first case, when we have that the node, Wi-Fi node, gets a new packet from the higher layers. And the MAC needs to apply the protocol in order to transmit that packet.
所以，我们等着。我们等着。我们之前就是这么说的，但是现在我们需要更精确一些。我们说需要等着，到底是什么意思？〔问句的确切措辞待听辨〕等多久？嗯，实际上，在这种情况下也是，我们需要做的就是应用退避过程。那么，我们要等多久呢？我们会按照这个过程，等待这个退避时间。所以，这又是这个规则。在这第一种情况下也是，当这个节点，Wi-Fi节点，从更高层拿到一个新的数据包时。并且MAC需要应用这个协议，才能传送那个数据包。

## 11 · 00:12:27

So, we know that first of all, we need to sense the channel for DIFS. If the channel is sense busy, then what [we’ll / we unclear] do is apply the backoff. That is, first of all, we need to wait for the channel to become idle again, and sense the channel idle for DIFS. Then draw an integer with equal probability out of the range zero, CW_min, set that integer multiplied by the time slot as backoff time, and then decrease the backoff counter slot by slot as long as the channel is idle. If the channel becomes busy at a certain point, while we are still decreasing the backoff counter, we need to stop the counter, right? And freeze it; we cannot decrease it. And then, when the channel becomes idle again, we will sense the channel for DIFS. If it’s idle, of course, for that time, we will resume decreasing our backoff counter. Till we do that, till the counter reaches zero, right? As soon as the counter reaches zero, then we can access the channel and transmit our packet. And then of course it depends. The transmission may be successful; that is fine, we are done. Or the packet may fail, and in that case, we have to recontend for the channel by using the backoff [receiver / procedure unclear]. Right? Okay, so now we know that actually there are two conditions, one and two, under which we will perform the backoff.
所以，我们知道，首先我们需要侦听信道一个 DIFS 的时间。如果信道被侦听为忙，那么[我们将要／我们，待听辨]做的就是执行退避。也就是说，首先我们需要等信道再次变为空闲，并侦听信道空闲一个 DIFS 的时间。然后从零、CW_min 这个范围中等概率地抽取一个整数，把那个整数乘以时隙设为退避时间，然后只要信道空闲，就逐个时隙递减退避计数器。如果信道在某个时刻变忙，而我们还在递减退避计数器，我们就需要停止计数器，对吧？并把它冻结；我们不能递减它。然后，当信道再次变为空闲时，我们会侦听信道一个 DIFS 的时间。当然，如果它在那段时间里是空闲的，我们就会恢复递减我们的退避计数器。直到我们这样做，直到计数器到达零，对吧？计数器一到零，那么我们就可以接入信道并发送我们的数据包。然后，当然，这要看情况。这次传输可能成功；那很好，我们完成了。或者这个数据包可能失败，而在那种情况下，我们必须使用退避[接收器／过程，待听辨]来重新竞争信道。对吧？好，所以现在我们知道，实际上有两种情况，第一种和第二种，在这些情况下我们会执行退避。

## 12 · 00:14:39

Okay, let’s leave the third condition for later. Okay, before introducing the third condition, I want to present an example of a situation when we apply the backoff. And what I want to do with this example is to clarify why, why we are using the backoff. Why is the backoff actually useful? Okay, and why the standard says that every time we perform the backoff for a given packet, we need to double the contention window parameter.
好，我们把第三种情况留到后面。好，在介绍第三种情况之前，我想给出一个我们执行退避的情况的例子。而我想用这个例子做的，是说明为什么，为什么我们在使用退避。退避实际上为什么有用？好，还有为什么标准说，每次我们为一个给定的数据包执行退避时，我们都需要把竞争窗口参数加倍。

## 13 · 00:15:26

Okay, because the main thing here, when we study Wi-Fi, okay, is to, of course, learn how we use a technology that is actually used every day, right, by almost everyone. So it’s good to know how things work. But it’s also important to understand the rationale, okay? Why things happen? Why do we make certain choices while developing a technology? That’s the really important fact that this class should give you, okay? To strengthen your ability to understand why certain things have been decided in certain manner in designing a system. Okay, because there is always a reason, and what we need to do is to learn how to reason about things, and understand the solutions that have been created.
好，因为这里主要的事情，当我们学习 Wi-Fi 时，好，当然是去了解我们怎样使用一种实际上每天都在被使用的技术，对吧，几乎每个人都在使用。所以，知道事情怎样运作是好的。但理解其中的道理也很重要，好吗？为什么事情会发生？为什么我们在开发一项技术时会作出某些选择？那是这门课应该给你们的真正重要的事实，好吗？去增强你们的能力，理解为什么在设计一个系统时，某些事情被以某种方式决定下来。好，因为总是有一个原因，而我们需要做的是学会怎样思考事情，并理解已经被创造出来的解决方案。

## 14 · 00:16:47

Okay, [that ... unclear] that’s the important attitude that we need to develop. So, this is understanding [why / Wi-Fi unclear], is a kind of mental exercise, okay, that we need to [to ... unclear] do. Okay, good. So, let’s consider a simple topology where we have an access point, and then we have A, B, and C.
好，[那……待听辨]那是我们需要培养的重要态度。所以，这是理解[为什么／Wi-Fi，待听辨]，是一种思维练习，好，我们需要去[去……待听辨]做的。好，很好。所以，我们来考虑一个简单的拓扑，其中我们有一个接入点，然后我们有 A、B 和 C。

## 15 · 00:17:18

Okay, the access point is here. These are our user nodes, and [we / they unclear] are of course part of this BSS; that means they can talk with the access point. And also, let’s consider the simple case where all nodes can hear each other. Okay, now let’s represent the behavior of these nodes over time.
好，接入点在这里。这些是我们的用户节点，并且[我们／它们，待听辨]当然是这个 BSS 的一部分；那意味着它们可以和接入点通信。还有，我们来考虑所有节点都能听到彼此的这个简单情况。好，现在我们来表示这些节点随时间的行为。

## 16 · 00:17:58

So, this is the timeline. We will represent it by drawing a timeline for each node: access point, user A, user B, and user C. Okay, now let’s assume that when we start looking at the system, what we observe is that A has received a packet from its higher layers. Okay, its application layer has generated some data. So, A gets this packet at [its / this unclear] MAC layer, and A understands that it has to try and transmit this packet, right? So, we know that in this case, a Wi-Fi node will first sense the channel for DIFS, right? Let’s assume that the channel is idle.
所以，这是时间轴。我们会通过给每个节点画一条时间轴来表示它：接入点、用户 A、用户 B 和用户 C。好，现在我们来假设，当我们开始看这个系统时，我们观察到的是 A 从它的高层收到了一个数据包。好，它的应用层生成了一些数据。所以，A 在[它的／这个，待听辨] MAC 层收到这个数据包，而 A 明白它必须尝试去发送这个数据包，对吧？所以，我们知道，在这种情况下，一个 Wi-Fi 节点会首先侦听信道一个 DIFS 的时间，对吧？我们来假设信道是空闲的。

## 17 · 00:19:08

So, we know that in this case, A can access the channel and transmit its data packet. That is a unicast data packet, so it is intended for the access point. And let’s be optimistic, and let’s consider that this data packet is successfully received by the access point. Therefore, we know that the access point will send an acknowledgment after SIFS. This is the usual story that we have told many times.
所以，我们知道，在这种情况下，A 可以接入信道并发送它的数据包。那是一个单播数据包，所以它是发给接入点的。而且我们来乐观一点，而且我们来认为这个数据包被接入点成功接收了。因此，我们知道，接入点会在 SIFS 之后发送一个确认。这是我们已经讲过很多次的通常的故事。

## 18 · 00:19:49

Okay, we also know that under these conditions, the other nodes B and C demodulate the header, right, of the data packet. They read the Duration field, so that they can set their NAV counter, and this will extend over the all expected duration of the dialogue.
好，我们还知道，在这些条件下，其他节点 B 和 C 解调首部，对吧，这个数据包的首部。它们读取 Duration 字段，这样它们就能设置它们的 NAV 计数器，而这将延伸覆盖这次对话的全部预期持续时间。

## 19 · 00:20:25

Okay, so, so far so good; this is exactly what we did in the past. Now, let’s add some events here. Let’s say B and also C, while they have their NAV set to a positive value, will also receive a data packet from their respective upper layers. So, this means that, for example, at this point in time, B gets a packet that is queued at its MAC layer, and let’s assume that C at this point in time also gets a packet from its higher layers.
好，所以，到目前为止一切顺利；这正是我们过去做过的。现在，我们在这里加一些事件。假设 B，还有 C，在它们把各自的 NAV 设为一个正值的时候，也会从它们各自的高层收到一个数据包。所以，这意味着，例如，在这个时间点，B 收到一个在它的 MAC 层排队的数据包，而我们假设 C 在这个时间点也从它的高层收到一个数据包。

## 20 · 00:21:21

Okay, so now while we have this dialogue between A and the access point going on, we have B and C who have a packet to transmit as well. Now, clearly, they have got their NAV set, so they know the channel is busy, so they cannot access the channel, right? That’s the principle of carrier sensing. We are essentially in this situation, situation number one, right? B and C [get / got unclear] a new packet, but they sense the channel as busy. So, what do we have to do? Apply backoff, right? So, this means that both B and C, remember our scheme is distributed, so everyone makes decisions by itself based on the state of the system that it observes. So, B will say, “[Hmm ... unclear] I got [a / the unclear] packet, but the channel is busy.”
好，所以现在，当我们有 A 和接入点之间的这段对话正在进行时，我们有 B 和 C，它们也有一个数据包要发送。现在，显然，它们已经把 NAV 设置好了，所以它们知道信道忙，所以它们不能接入信道，对吧？那就是载波侦听的原则。我们基本上处在这种情况，第一种情况，对吧？B 和 C [收到／收到了，待听辨]一个新数据包，但是它们侦听到信道忙。所以，我们必须做什么？执行退避，对吧？所以，这意味着 B 和 C 两者，记住我们的方案是分布式的，所以每一个都根据它观察到的系统状态自己作出决定。所以，B 会说：“[嗯……待听辨]我收到了[一个／这个，待听辨]数据包，但信道忙。”

