# 双语对照：录音机-20261012-1331 — English wording restoration

Status: faithful restoration with unresolved words; manual_listening=false. Brackets remain unresolved.

## 一、退避指数与竞争窗口

### 01 · 00:00:03 · 重传失败数据包需要退避

原标说话人 1  00:00:03
And we said that whenever [a/the unclear] Wi-Fi node needs to recontend for the channel, because this node has to retransmit [a/the unclear] packet that failed, then this node will perform the backoff procedure.

### 02 · 00:00:29 · 退避过程与竞争窗口指数表达式

原标说话人 1  00:00:29
And we explained how the backoff procedure works. Okay? Now, we [said/send unclear] that first a node needs to wait for the channel to be idle for DIFS. Then [it/you unclear] will draw an integer out of a range of possible values with equal probability, selecting each of them with equal probability. And this range of values goes from zero to the contention window parameter, okay? The first time that we use the backoff procedure to transmit a packet, we set this contention window parameter to its minimum value. And then, if we need to perform the backoff procedure again in order to transmit this packet, because, for example, we fail and fail and fail, every time we will increase the value of contention window. And we said, roughly speaking, this value of contention window doubles every time, right? Now, to be more precise, the relation according to which the CW parameter increases is the following. So, CW value is actually expressed as a power of two minus one, where this exponent is called backoff exponent.

### 03 · 00:02:48 · 最小退避指数与CW为31的例子

原标说话人 1  00:02:48
Okay? So, for example, the first time that we use the backoff procedure for a data packet, we set the, so the first time, we set the backoff exponent to the backoff exponent minimum, okay? Now, by default, in the early versions of Wi-Fi, this is equal to five, okay? This is an example that refers to the early versions of Wi-Fi, okay? Now, so, if we take this example here, this example value here, we see that, as we said last time, the first time that we use this contention window minimum, the value will be two to the power of the minimum exponent minus one. Since this is five, right, this will be two to the five minus one, which is 31, right? So that's why, yes, on Saturday, when we [introduce/produce tense unclear] this procedure, we said, well, let's consider the minimum contention window 31, okay? Then, the second time that we use the backoff procedure for the same packet, we are going to increase the backoff exponent. So, if this was our first value, the second time, [sorry unclear], we'll have second value, right, that is equal to what, is equal to the previous one plus one.

### 04 · 00:05:24 · 第二次退避的竞争窗口计算

原标说话人 1  00:05:24
Okay? So this means that the second time that we have to compute the contention window, this will be equal to two to the power of the, the backoff exponent [on/at unclear] the second step minus one, which is two to the backoff exponent [on/at unclear] the first step increased by one minus one, right?

### 05 · 00:06:01 · 窗口增至63并受CW最大值限制

原标说话人 1  00:06:01
So now this is two to the power, in our example, to the power of six minus one, which is 63, okay? So this is the way we increase the contention window minimum value every time till, as we said, we reach this value, CW max. After we reach this value, we do not increase [the/this unclear] CW value any longer [beyond/behind unclear] this value, even if we need to still perform the backoff procedure for the same time.

### 06 · 00:06:57 · 退避指数逐次加一的规则

原标说话人 1  00:06:57
So, the general, [ah unclear] the general rule is that at step i, the generic step i, we set the backoff exponent [at/as unclear] step i equal to the backoff exponent [at/and unclear] the previous step increased by one, right?

### 07 · 00:07:28 · 竞争窗口扩大与随机取值范围

原标说话人 1  00:07:28
And at the generic step i, the contention window will be computed as two to the power of the backoff exponent at step i minus one. Okay, this is the general expression that we use to compute the, the backoff exponent and the corresponding contention window at each step. Okay, that said, therefore we understand that [every time/at every time unclear] that we need to perform the backoff for a given data packet, we roughly double the contention window, as we said. Okay, so we are going to [enlarge/launch unclear] the possible values, integer values, that we can draw to compute [backoff repetition unclear] time. Okay, so before explaining why we do that, okay, why the [standard said/standards say unclear] let's double the contention window every time we need to perform a backoff to transmit [a/the unclear] packet. So before explaining the reason because we do that, let me mention what was reported in one of the earlier slides.

## 二、退避触发条件与计数规则

### 08 · 00:09:04 · 发送失败时的退避回顾

原标说话人 1  00:09:04
But I didn't comment on that because I didn't want to put too many things at the same time. But one more thing that we need to say important about the backoff is that the backoff procedure, of course, it is performed, as we said, when we have essentially a packet, right, that has been transmitted and it failed.

### 09 · 00:09:40 · 新包到达但侦听到忙信道

原标说话人 1  00:09:40
So, we need to recontend for the channel and transmit the packet again, right? This is the [case/phase unclear] that we have considered so far, under which we need to perform the backoff. However, there are two more situations under which we need to perform a backoff procedure, [okay? unclear] Exactly as we explained, [okay? unclear] The same procedure that we just explained. This procedure indeed needs to be performed also when a node, a transmitter [wording unclear], has got a packet to transmit. It senses the channel, but the channel is busy, right? So, we already know that in this case, we cannot access the channel right away because of the carrier sensing multiple access principle, right? So, if we sense the channel, we got [a/the unclear] packet from the higher layers. At the MAC layer, we sense the channel for DIFS, but the channel is busy, [okay/right unclear] So, what we knew so far is that in this case, we cannot access the channel, right? Because the channel is busy. We are like polite people. We don't want to interrupt someone who is talking already.

### 10 · 00:11:21 · 忙信道情况下等待的具体含义

原标说话人 1  00:11:21
So, we wait. We wait. That's what we said, but now we need to be more precise. What do we mean exactly that we need to wait? [question wording unclear] For how long? Well, in reality, also in this case, what we need to do is to apply the backoff procedure. So, how long do we wait for? We will wait for the backoff time, according to this procedure. So, this is the rule again. Also in this first case, when we have that the node, Wi-Fi node, gets a new packet from the higher layers. And the MAC needs to apply the protocol in order to transmit that packet.

### 11 · 00:12:27 · 退避计数递减、冻结与恢复

原标说话人 1  00:12:27
So, we know that first of all, we need to sense the channel for DIFS. If the channel is sense busy, then what [we’ll / we unclear] do is apply the backoff. That is, first of all, we need to wait for the channel to become idle again, and sense the channel idle for DIFS. Then draw an integer with equal probability out of the range zero, CW_min, set that integer multiplied by the time slot as backoff time, and then decrease the backoff counter slot by slot as long as the channel is idle. If the channel becomes busy at a certain point, while we are still decreasing the backoff counter, we need to stop the counter, right? And freeze it; we cannot decrease it. And then, when the channel becomes idle again, we will sense the channel for DIFS. If it’s idle, of course, for that time, we will resume decreasing our backoff counter. Till we do that, till the counter reaches zero, right? As soon as the counter reaches zero, then we can access the channel and transmit our packet. And then of course it depends. The transmission may be successful; that is fine, we are done. Or the packet may fail, and in that case, we have to recontend for the channel by using the backoff [receiver / procedure unclear]. Right? Okay, so now we know that actually there are two conditions, one and two, under which we will perform the backoff.

### 12 · 00:14:39 · 用例子理解退避及窗口扩大原因

原标说话人 1  00:14:39
Okay, let’s leave the third condition for later. Okay, before introducing the third condition, I want to present an example of a situation when we apply the backoff. And what I want to do with this example is to clarify why, why we are using the backoff. Why is the backoff actually useful? Okay, and why the standard says that every time we perform the backoff for a given packet, we need to double the contention window parameter.

## 三、多节点退避时序示例

### 13 · 00:15:26 · 学习技术机制背后的设计理由

原标说话人 1  00:15:26
Okay, because the main thing here, when we study Wi-Fi, okay, is to, of course, learn how we use a technology that is actually used every day, right, by almost everyone. So it’s good to know how things work. But it’s also important to understand the rationale, okay? Why things happen? Why do we make certain choices while developing a technology? That’s the really important fact that this class should give you, okay? To strengthen your ability to understand why certain things have been decided in certain manner in designing a system. Okay, because there is always a reason, and what we need to do is to learn how to reason about things, and understand the solutions that have been created.

### 14 · 00:16:47 · 引入接入点和A、B、C拓扑

原标说话人 1  00:16:47
Okay, [that ... unclear] that’s the important attitude that we need to develop. So, this is understanding [why / Wi-Fi unclear], is a kind of mental exercise, okay, that we need to [to ... unclear] do. Okay, good. So, let’s consider a simple topology where we have an access point, and then we have A, B, and C.

### 15 · 00:17:18 · 所有节点彼此可听的BSS场景

原标说话人 1  00:17:18
Okay, the access point is here. These are our user nodes, and [we / they unclear] are of course part of this BSS; that means they can talk with the access point. And also, let’s consider the simple case where all nodes can hear each other. Okay, now let’s represent the behavior of these nodes over time.

### 16 · 00:17:58 · A收到数据包并侦听DIFS

原标说话人 1  00:17:58
So, this is the timeline. We will represent it by drawing a timeline for each node: access point, user A, user B, and user C. Okay, now let’s assume that when we start looking at the system, what we observe is that A has received a packet from its higher layers. Okay, its application layer has generated some data. So, A gets this packet at [its / this unclear] MAC layer, and A understands that it has to try and transmit this packet, right? So, we know that in this case, a Wi-Fi node will first sense the channel for DIFS, right? Let’s assume that the channel is idle.

### 17 · 00:19:08 · A发送数据并获得SIFS后的ACK

原标说话人 1  00:19:08
So, we know that in this case, A can access the channel and transmit its data packet. That is a unicast data packet, so it is intended for the access point. And let’s be optimistic, and let’s consider that this data packet is successfully received by the access point. Therefore, we know that the access point will send an acknowledgment after SIFS. This is the usual story that we have told many times.

### 18 · 00:19:49 · B和C读取首部设置NAV

原标说话人 1  00:19:49
Okay, we also know that under these conditions, the other nodes B and C demodulate the header, right, of the data packet. They read the Duration field, so that they can set their NAV counter, and this will extend over the all expected duration of the dialogue.

### 19 · 00:20:25 · B和C在信道忙时收到新数据包

原标说话人 1  00:20:25
Okay, so, so far so good; this is exactly what we did in the past. Now, let’s add some events here. Let’s say B and also C, while they have their NAV set to a positive value, will also receive a data packet from their respective upper layers. So, this means that, for example, at this point in time, B gets a packet that is queued at its MAC layer, and let’s assume that C at this point in time also gets a packet from its higher layers.

### 20 · 00:21:21 · 依据本地忙状态独立执行退避

原标说话人 1  00:21:21
Okay, so now while we have this dialogue between A and the access point going on, we have B and C who have a packet to transmit as well. Now, clearly, they have got their NAV set, so they know the channel is busy, so they cannot access the channel, right? That’s the principle of carrier sensing. We are essentially in this situation, situation number one, right? B and C [get / got unclear] a new packet, but they sense the channel as busy. So, what do we have to do? Apply backoff, right? So, this means that both B and C, remember our scheme is distributed, so everyone makes decisions by itself based on the state of the system that it observes. So, B will say, “[Hmm ... unclear] I got [a / the unclear] packet, but the channel is busy.”

### 21 · 00:22:43 · 等待空闲DIFS后随机抽取退避值

原标说话人 1  00:22:43
What I need to do is to apply backoff. So what [it will / you will, unclear] do is wait for the channel to become idle again, sense the channel idle for DIFS, and then, if the channel is idle for DIFS, it will be able to draw an integer, right? Out of what? Out of the range zero, CW_min. And the same C, right? C at this point in time says, oh, I got a packet to transmit, but the channel is busy. So again, it knows that it has to perform a backoff. So what it will do? It will wait for the channel to become idle. Then it needs to verify that the channel is idle for DIFS. The channel will be idle because nobody else is doing anything, so the channel is idle.

### 22 · 00:24:00 · B抽到2而C抽到5的例子

原标说话人 1  00:24:00
[And it too will draw / And it will do, will draw, unclear] an integer with equal probability out of this same range of values, okay? So let's assume that the value drawn by B, the integer, is equal to two. And let's assume that the integer drawn by C is equal to five. This is just an example.

### 23 · 00:24:36 · 两个节点并行倒计时至B先归零

原标说话人 1  00:24:36
Okay, so if this is the case, then we know that B will compute its backoff time, that will be equal to two times the time-slot duration, right? And similarly C will compute its backoff time, that will be five time slots. And then each of them will have to decrease its own backoff counter, time slot by time slot. So B will start sensing the channel for a time slot. The channel is currently idle, so it will decrease its backoff counter by one. And the same will do C, right? So it will decrease it by, its own counter by one. Then, next time slot, again B senses the channel [is / as, unclear] idle, decreases its backoff counter by one. And C will do the same. But now the backoff counter of B has reached zero.

### 24 · 00:26:12 · B获得发送机会并成功收到ACK

原标说话人 1  00:26:12
So B is entitled to access the channel [and transmit, unclear]. So it will transmit its data packet. The data packet clearly is intended for the access point because, as we said, we are considering unicast packets. And in this network topology, network architecture, all Wi-Fi user nodes communicate with the access point only. Let's again be optimistic. So this means that this packet is received successfully by the access point, which will send back an acknowledgement after SIFS.

### 25 · 00:27:02 · B发送期间A设NAV且C冻结退避

原标说话人 1  00:27:02
Upon the data transmission by B, the other nodes, right, can set their NAV. They can read the Duration field in the header of the data packet. So we need also to highlight this, that both A and also C will set their NAV, right? So what does it mean for A? This is okay, fine, it doesn't have anything to do, so that's [not okay / okay, unclear]. But for C, this means that [it / you, unclear] will have to freeze its backoff counter for this duration, right?

### 26 · 00:28:03 · C在信道恢复后继续剩余倒计时

原标说话人 1  00:28:03
Because now the channel is busy, so C cannot decrease its counter, it has to suspend the countdown. Okay, so during all this time C will be essentially blocked, and what it does is to wait for the channel to become idle again. [It / he, unclear] makes sure that the channel is idle for DIFS, and then [it / he, unclear] can resume decreasing its backoff [counter / count, unclear], [right, unclear]? It has still three time slots to go, so [it / he, unclear] will sense the channel for a [time slot, possibly incomplete]. Yes, this is idle, so it can decrease the backoff counter by one. Then it senses the channel again for a time slot. The channel is idle, it can decrease the counter by one, and then again, the channel is idle for one more time slot, it can decrease its counter by one.

### 27 · 00:29:23 · C归零发送成功与退避作用

原标说话人 1  00:29:23
Now its backoff counter is down to zero, so [it / you, unclear] can access the channel and transmit its data packet. And again, being optimistic, we say that this is successful, so [it / we, unclear] will receive the acknowledgement after SIFS. And we are all happy because all nodes could transmit [their data packet successfully, unclear]. Okay, so this is an example of how we apply [in the, unclear] backoff procedure, in particular under this condition, right? But it allows [us, unclear] also to understand the importance of backoff. That's the final goal [that I, unclear], the ultimate goal that I was aiming.

## 四、消融实验与概率性碰撞避免

### 28 · 00:30:26 · 通过消融实验考察没有退避的系统

原标说话人 1  00:30:26
How can we understand the importance of backoff? Well, let's make a little game that is, scientifically speaking, is called ablation study, okay? An ablation study is when you remove a feature of a system, and you study the behavior of that system without that feature. So our small game is an ablation study of this particular [um, unclear] backoff procedure, or, or Wi-Fi channel access. So let's make this [a, unclear] small game and think, what would happen if the backoff were not there?

### 29 · 00:31:22 · 移除退避后重新推演

原标说话人 1  00:31:22
Okay, so let's roll back the story, let's start from the beginning, but this time let's assume that there is no backoff, okay? So what would be the behavior of our nodes?

### 30 · 00:31:43 · 无退避时A的首次发送不变

原标说话人 1  00:31:43
Well, at the beginning everything is the same because the only node that has got a packet to transmit is A, right? So it will listen to the channel, the channel is idle for DIFS. It will access the channel and transmit the packet.

### 31 · 00:32:02 · B和C同时发送导致必然碰撞

原标说话人 1  00:32:02
And again, let's be optimistic. The access point sends back [the / an / no article, unclear] acknowledgement, and the other nodes, B and C, both set their NAV, right? This is exactly as before. And again, B and C at different points in time, assume that they [get / got, unclear] also a packet to transmit. But again, now we do not have backoff, okay? So we have to think, what would happen if backoff were not there? So what would B and C do? Well, we still have carrier sensing, right, multiple access. So since both B and C sense the channel as busy because they have their NAV set, they cannot access the channel, right? [Till; usage unclear] the channel is busy, I cannot access the channel. So for sure B and C will again wait for the channel to be idle, make sure that the channel is idle. But then if there is no backoff, they can just access the channel, right? Because now the channel is idle, so they say, oh, channel idle, I can access the channel and transmit. Remember, we are playing this small game assuming that there is no backoff. So what we have is that, no backoff, we have both transmitting their data packet after having sensed the channel idle. So what do we have here? Collision, right? They both access the channel at the same time with probability one. It is sure that they will do that, and of course they will fail because they overlap, their transmissions overlap. And the access point will not be able to demodulate correctly either this packet.

### 32 · 00:34:43 · 退避作为碰撞避免机制

原标说话人 1  00:34:43
Okay, so what is the first conclusion here? That the backoff procedure has been introduced in our system in order to avoid collisions between contending nodes. Our contending nodes in these examples are B and C, right? They are contending for the channel. And the backoff procedure is there to avoid the collision between them. So again, remember that we said Wi-Fi is a CSMA scheme with collision avoidance, [right, unclear]?

### 33 · 00:35:39 · 错开行动时间减少拥挤

原标说话人 1  00:35:39
This backoff is a mechanism that helps to avoid collisions. So the basic principle, the basic idea is very simple. Whenever there is a crowded situation, right, you try to desynchronize from the others so that you find a free [route / road, unclear] ahead, and this is exactly the same thing. So if there is peak hour, you don't want to jump into the traffic, right, [as all / as for, unclear] the others.

### 34 · 00:36:25 · 避开高峰时段的生活类比

原标说话人 1  00:36:25
You try to pick, you wait, you try to pick a time at which not many other people will be there. And this is exactly the same principle. You try to pick a time in order to desynchronize your action with respect to the others, and this way you avoid meeting, [unclear words], colliding with the others, or finding yourself in a, in a traffic jam. [Hmm, unclear], that's exactly the same principle.

### 35 · 00:37:02 · 相同退避值仍会导致碰撞

原标说话人 1  00:37:02
Now what I would like to underline is that, so we observe, our first observation is that backoff is a mechanism for avoiding collisions, but it is still probabilistic, okay? Why? Because if, like in our example, both B and C draw the same value of backoff, they are going to collide. Okay, so if, for example, C too drew two as an integer, then they will not be [synchronized / desynchronized, unclear] from each other, okay? Because they will both decrease the [the, unclear] backoff counter during the first time slot, and then again during the second time slot. But under the assumption that they now both drew two as an integer, they will decrease the backoff counter to zero exactly at the same time. That means that they will access the channel exactly at the same time and collide.

### 36 · 00:38:58 · 退避只能概率性地避免碰撞

原标说话人 1  00:38:58
So backoff is a way to avoid collisions, but it does not avoid collisions with probability one. There is still a certain probability with which the nodes, the contending nodes, may collide, [right / okay, unclear]? So it's a probabilistic collision-avoidance mechanism.

### 37 · 00:39:28 · 准备讨论扩大竞争窗口的作用

原标说话人 1  00:39:28
Okay, this is our first observation. Is it clear so far? Okay, now if this is clear, let me make a second, [sorry, check this, because today is a bit different, unclear]. Okay, we have a second observation to make. We are close to the break, but let me start introducing it, and then we will finish after [the / a, unclear] short break.

## 五、碰撞概率与竞争窗口

### 38 · 00:40:13 · CW最小值范围内共有多少整数

原标说话人 1  00:40:13
So the second observation that I want to make is about the benefit of increasing the contention window parameter every time we need to perform a backoff procedure for a given data packet, okay? So let's consider still the same example as before. So we still have the access point, A, B and C. A talk with the access point, then B and C get the packet, both of them, while the channel is busy. So they need to apply the backoff, and they need to draw [unclear words], after having sensed the channel as idle for DIFS, an integer out of, as we know, out of this range of values, because this is the first time that they run the backoff for the packet. So they both use zero, contention window minimum, as a possible range, as a range of possible integers to be selected. So how many values are [in / in in, unclear] this range? There are CW_min...

### 39 · 00:41:48 · 计入零使取值数量增加一

原标说话人 1  00:41:48
Plus one integers, right? Because [unclear words], including the zero is plus one. Okay, this is the number of integers in that range.

### 40 · 00:41:59 · 均匀抽取整数的概率

原标说话人 1  00:41:59
Okay, so what we want to compute, since we said that backoff is a probabilistic collision-avoidance mechanism, is the probability that B and C collide. Okay, that's the probability that we want to compute. Okay, now we know already that they will collide if they draw the same integer out of this range. And remember that the way a node draws an integer out of this range is with uniform probability, right? So same probability for every value to be selected by the node. So if we consider the probability for a node to draw a generic integer n out of this range, this probability is given by one over CW_min plus one, right? Because this is the number of integers in the range. Since we draw each value with equal probability, uniform probability, it's easy to see that the probability that an integer, a generic integer, is drawn out of this range by a node is given by one over CW_min plus one. This is basic probability theory, okay? So in this way you can see that they are selected exactly, each of them with the same probability. [Okay, unclear], this probability is the same for all of them.

### 41 · 00:44:32 · 课间休息与碰撞概率预告

原标说话人 1  00:44:32
Okay, now let's stop for five minutes. And then use the [short break / shortcut unclear], if I'm not wrong. Okay, and then we will resume and see how [this probability / these probabilities unclear] of collision can be computed.

### 42 · 00:49:19 · 从条件概率推导两节点碰撞

原标说话人 1  00:49:19
Okay, good. [So / Now unclear], let's look at our computation. So, the probability that B and C collide is, as we said, very simply, so [don't / do not unclear] worry, this is a very, very simple derivation. Is the probability that B and C draw the same value, let's say n, okay? [A / the unclear] same value, [a / the unclear] same integer. That's what we said, all right. Let's start this computation by considering that B draws n, a given integer n, whatever this is. So, what we are first computing is the [conditional / conditioned unclear] probability, so the probability that C draws also n, so n, given that B drew n, okay? So this is the so-called conditioned probability. Now remember, our scheme is actually very simple because it's distributed. And as we said, every node makes its own decisions according to the protocol rules, but it makes its own decisions independently from the others, right?

### 43 · 00:51:21 · 节点独立选择与条件无关性

原标说话人 1  00:51:21
So, the fact that B drew n will not affect the probability that C draws n. C does whatever, let's say, [he / it unclear] likes, based on what decisions [he / it unclear] makes following the protocol, right? But it's not affected by what other nodes do. So, this is actually equal to the probability that C draws n, simply that, because it doesn't matter what B does, right? C will do things by [itself / himself / themselves unclear].

### 44 · 00:52:17 · 给定B选择n时C碰撞的概率

原标说话人 1  00:52:17
Okay, so what is the probability that C draws n? So, what is the probability that an integer is selected out of the range zero, CW_min? Well, we have written that here, right? This is the probability. Okay, so now we know that given that B has drawn n, the probability that C will also draw n is this one. Okay, so [conditioned / condition unclear] to the fact that B drew n, then this is the collision probability [conditioned / condition unclear] to the fact that B drew n, right?

### 45 · 00:53:12 · 遍历所有n去掉条件限制

原标说话人 1  00:53:12
What we need to do is to now to compute the original probability, is to decondition and make the computation for any possible n. So, what we want to now do is to compute in general the probability that B and C collide without conditioning to any event. So that is, we need to consider all possible values of integer from zero to CW_min. And for any n, we know that the probability of collision is what? The probability that C draws n if also B has drawn n, right?

### 46 · 00:54:22 · B选中n的概率与碰撞条件

原标说话人 1  00:54:22
So, let's first write the probability that B draws n. The probability that B draws n is again this one. So we can write one over CW_min plus one. This is the probability that B draws n. And then given that, we know that [a / the unclear] collision happens if C also draws n. That happens with this probability.

### 47 · 00:54:59 · 求和化简得到碰撞概率

原标说话人 1  00:54:59
So we multiply by again one over CW_min plus one, which is the probability that C [draws / grows unclear] n. So what we have is simply sum over n that goes from zero to CW_min of one over CW_min plus one squared, [right / okay unclear]? Now, this is a constant term, we are inside a sum, so we are summing this constant term how many times? CW_min plus one times, right? So this is equal to CW_min plus one divided by CW_min plus one squared. We simplify numerator and denominator, and we get one over CW_min plus one.

### 48 · 00:56:35 · 两节点碰撞概率的最终结论

原标说话人 1  00:56:35
So, the final result of all [this computation / these computations unclear] is that the probability that B and C collide in our simple example that we presented earlier is one over the contention window plus one. Okay, now if you [were / are unclear] able to follow the computation, great. It's a simple probability computation, but if your background is different, and therefore you have not seen probability anywhere in your previous courses, do not worry. The important thing is that you retain the final message.

### 49 · 00:57:27 · 竞争窗口越大碰撞概率越低

原标说话人 1  00:57:27
The final message is, in our simple example, right, that we are considering, the probability that B and C [collide / collided unclear] while performing the backoff procedure is equal to this ratio, that clearly will decrease as the value of contention window minimum increases, right? The larger the contention window, the lower this ratio, so the lower the collision probability. This is, I think, something that everybody [can understand / understands unclear]. Okay, now, so this means that, okay, this refers, as I said, to the previous simple example, but it's a general rule. The collision probability in the backoff procedure decreases as the value of contention window increases. So now, what does this tell you? Why am I marking this, [and making / I'm making unclear] this second observation? Because remember, we wanted to understand the reason why in Wi-Fi we say every time we perform the backoff procedure for a given data packet, we roughly speaking double the contention window. So we increase it very significantly every time. Why do we do that? To reduce the probability of collision among [contending / contend unclear] nodes.

## 六、机制局限与广播多播

### 50 · 00:59:34 · 重复失败时扩大可选整数范围

原标说话人 1  00:59:34
[Okay unclear], so, backoff is a probabilistic mechanism, and essentially Wi-Fi assumes that the reason why a transmitter is failing, failing, failing is because there are too many nodes in the network that try to access the channel to transmit a packet. The situation is too crowded. So what Wi-Fi says is, if you fail, [fail, fail unclear], every time you fail means that there are other nodes trying, and you are selecting the same backoff, you have the same backoff time, and you keep colliding. So in order to reduce the probability of collision, each node needs to enlarge the possible values, so the choice, right, among the integers that can be selected.

### 51 · 01:00:35 · 扩大窗口的好处与信道差错下的代价

原标说话人 1  01:00:35
It's like when you have a bag with candies, if they are all strawberry flavored, if there are two people picking the candy, clearly they will pick strawberry. But if instead you fill the bag with banana, strawberry, peach, mint, and so on, then the probability that two people pick the same candy flavor will reduce. So this is exactly the same [principle / thing unclear]. Okay, so you may say, well, nice, Wi-Fi really takes care of this crowded situation and allow us to perform better. True, but this is, this works, this is a good idea to double the contention window every time you perform a backoff to transmit [a / the unclear] packet. It works, but it works if the reason why a transmitter is failing is indeed because it [it unclear] keeps colliding with others. But remember, in wireless, a transmission may fail also because of channel errors. So you may be the only one in the network with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate the signal correctly. Okay, so in that case, of course, you have to follow the protocol rules anyway. Okay, so if you fail and fail because of channel errors, you have to apply the rules. And this means that every time you have to enlarge the contention window, and statistically it's more likely that you will draw a long and longer and longer backoff time, right? So is this good in this case? [Hmm unclear], not really good, right? Because the reason why you are failing is not because there are others and you are colliding, that's not the reason. The reason is that the channel is poor, of poor quality, and this mechanism does not help to solve the issue, right? Actually, this [method / mechanism unclear] in this situation is even harmful. Why? Because it makes you delay channel access, right? It makes you wait longer and longer and longer before accessing the channel, being able to access the channel and transmit the packet. With no reason, because the problem is not collision, the problem is poor channel quality. So it just increases the channel access delay. It doesn't help with anything.

### 52 · 01:04:00 · 批判性评估技术方案的适用条件

原标说话人 1  01:04:00
Okay, so we need to be aware that, well, we need to understand why certain techniques, mechanisms are designed in a certain way. But we need also always to look at these mechanisms or techniques or solutions with a critical eye. That means we need to look at them and ask ourselves, is this really good in under all conditions, under all situations, or not? There may be aspects of technology that are not that good, not always, and we need to be aware of that. Okay, so whenever we design a system, whenever we design a technological solution, we need to account for possible issues that may arise. So an idea may be good to solve one problem, but it might actually make things worse in other situations. So we need also to look at the big picture when we design a technology. [Okay unclear], and [and unclear] this is indeed an example of [of unclear] that.

### 53 · 01:05:29 · 广播和多播不期待确认

原标说话人 1  01:05:29
[Um unclear], the last thing that I would like to comment, and then we go to the third situation, is remember that we are considering how to transmit unicast data packets, right? We said that. Let me just mention again that in the case of multicast or broadcast data packet, things are much, much simpler, because we do not expect any acknowledgement.

### 54 · 01:06:05 · 多个接收方同时ACK会碰撞

原标说话人 1  01:06:05
Indeed, since broadcast and multicast packets are intended for multiple destinations, we cannot have receivers sending back acknowledgments, because all these acknowledgments, if sent at the same time, will collide [with / within unclear] each other. So no use.

### 55 · 01:06:45 · 广播多播一次发送与发送后退避引入

原标说话人 1  01:06:45
If you had to desynchronize the acknowledgments transmissions, that would be very, very complicated. And [it / you unclear] would increase the overhead of the protocol. So that's [not good / done unclear]. So the choice that they made was, well, if a packet is broadcast or multicast, the transmitter of course needs to sense the channel. If the channel is idle, transmit. If the channel is busy, of course, you have to perform the backoff procedure because you have to wait. But then once you access the channel and transmit, that's it. Okay, you are done, because you don't care if the packet was received successfully or unsuccessfully. [You / we unclear] are done. Okay, so broadcast and multicast packets are transmitted only once. So you may need to run the backoff procedure for those data packets, but just if, when you want to access the channel, you sense the channel as busy the first time, okay? Then once you perform the backoff and you access the channel and transmit, you are done. Okay, [um unclear], if everything is clear so far, let me know if you have questions. No questions? Okay, so if we are good, then we can now tackle this last condition. That is, well, we have one more situation under which we perform the backoff. In this third situation, actually, the procedure is slightly, slightly different, okay? [It is / is, is unclear] essentially the same except for one [thing unclear]. What is this third situation? [And it is called unclear], in this case the procedure is called [fast / post unclear] backoff, just to underline that there is a small difference with respect to the backoff run under the previous two situations.

## 七、发送后退避与公平性

### 56 · 01:09:19 · 成功传输后仍须执行退避

原标说话人 1  01:09:19
So what is this third situation? [It is / is unclear] when a node transmits a data packet successfully. So you may say, well, why do I have to perform the backoff in this case? [I transmitted / I've transmitted unclear] my packet correctly, [I'm / and unclear] done. What do you want from me? Well, the Wi-Fi says, I know you transmitted your packet, you are done with that, but after you receive the ACK from the receiver, you need to perform a backoff using zero, CW_min as range of possible integers. That's [what / why unclear] the protocol says.

### 57 · 01:10:13 · 发送后退避的公平性目标

原标说话人 1  01:10:13
So again, we want to understand why, right? [I mean / maybe unclear], this is not enough. Okay, I have to do it, I will do it, but tell me why, why do I have to do that? Well, the reason is fairness. We want to be fair to our nodes.

### 58 · 01:10:32 · 用A成功发送场景说明发送后退避

原标说话人 1  01:10:32
Okay, so let me give [you unclear] an example, and that will allow us to indeed understand why they tell us, once you transmit successfully, run this post-backoff. So let's consider again the same scenario, so that will be easy. Access point, and then node A. And then we can also consider our B and C nodes, right? Same as before. So we know [already / that with unclear] the story, it will be easier. So the story starts in the same way. A has got a packet, [DIFS unclear], channel idle, transmits the data packet, unicast data packet to the access point. This packet transmission is successful, so the access point [sends / sent unclear] back the ACK.

### 59 · 01:11:51 · B和C设NAV并收到待发数据

原标说话人 1  01:11:51
And as we said before, all nodes are in radio visibility of each other, they can hear each other. So B and C will set their [NAV unclear]. And same as before, at a certain point B and C get a packet from their respective higher layers, so they will have to transmit their packet, right?

### 60 · 01:12:20 · A成功后退避与B、C常规退避

原标说话人 1  01:12:20
And we know already how things work, fine, but now our attention is on A, okay? Let's focus on A. A is the one that performs its transmission successfully, so it's done. And according to the protocol, now we know that A actually, once it has finished transmitting the packet and [received / receive unclear] the ACK, needs to perform this [post / past / fast unclear] backoff procedure, right? So [it / I unclear] will have to sense the channel for [DIFS unclear], and then [it / you / we unclear] will have to draw an integer out of the range zero, CW_min. And of course for B and C we'll have the same behavior as before. We know [that already / that's ready unclear]. So B and [and unclear] C will have to run a, let's say, regular backoff procedure.

### 61 · 01:13:44 · 移除发送后退避的消融实验

原标说话人 1  01:13:44
So again, in order to understand how useful [a / the unclear] mechanism is, or solution is, let's play our little game of ablation, right? So let's remove the post-backoff and see what happens. So what if A does not have to run any, [any unclear] post-backoff? Well, let's add an event here to better understand what would happen considering all possible cases.

### 62 · 01:14:31 · A队列中还有另一个待发包

原标说话人 1  01:14:31
Let's consider that A has got another packet in [a unclear] its MAC queue. Remember that we said the MAC layer can be modeled, right, as a queue with a server. So let's consider that A has transmitted the packet here successfully, but let's assume that A has [got / put unclear] another packet in the queue waiting to be transmitted. So this first packet goes through, right, successfully. This is what we [represented / represent unclear] here. But now A has got another packet right here, right?

### 63 · 01:15:22 · 没有发送后退避时A立即再发

原标说话人 1  01:15:22
So when [it's / he's unclear] done with this dialogue, [we'll / we unclear] have another packet to deal with. So what if A didn't have any post-backoff to run? Well, [it / he / you unclear] will have to sense the channel for DIFS. The channel is idle, and [it / you unclear] will be able to access the channel [and transmit / trust me unclear]. So [it / you unclear] will have to transmit its [other / own unclear] data. This may be successful. And what would be that? Would that be fair with respect to B and C?

### 64 · 01:16:10 · 连续占用信道造成不公平

原标说话人 1  01:16:10
The poor B and C are waiting [right there unclear], their backoff time, and A just gets the next packet and go ahead with its transmission. So this is unfair. And indeed, if a Wi-Fi card like A has got several packets to transmit, under this situation without post-backoff, we just continue accessing the channel and transmitting its packets. With very high probability, [it / you unclear] will actually seize the channel for a very long time and transmit, transmit, transmit, while the others [will have / we have / we had unclear] to wait, wait, [and unclear] wait, because the channel [will / would unclear] become busy [confused unclear]. And this was indeed observed, also experimentally. Years ago, some researchers made experiments with different Wi-Fi cards. [They / which unclear] were commercial products. They claimed, all these cards [claimed / claim unclear] to follow the standard. [Of course / for unclear] products must follow the standard. They [claimed / claim unclear] to do that. But actually, one of these cards was applying everything, okay, as specified by the standard, but the post-backoff.

### 65 · 01:17:42 · 未实施发送后退避的商用网卡实验

原标说话人 1  01:17:42
And what these researchers observed was that this Wi-Fi card was [obtaining / obtained unclear] a very, very high throughput; that means the ability to transmit a lot of data, while the other Wi-Fi cards were starving, so they could not get access to the channel. A very unfair service, and this is because, this was because that commercial Wi-Fi card at that time did not implement the post-backoff procedure.

### 66 · 01:18:22 · 发送后退避的强制性与开销示例

原标说话人 1  01:18:22
So this seems to be, you know, a detail or one more thing that a node has to do, but it's actually extremely important to ensure fairness. In Wi-Fi, we want to be fair, we want to give the same probability to everyone in channel access. So it is a very important feature, and notice that the same would happen if we didn't have the post-backoff procedure. Even if A, right after its, [its unclear] completion, successful completion of, [of unclear] its dialogue, didn't have any packet. But even in the case where it gets a packet right after, [a unclear] few microseconds after, [it / you unclear] will still get an advantage [with unclear] respect to B and C, who must run the backoff. So that's why the standard says, no matter what your MAC queue state is, we don't care. Once you complete a transmission successfully, you must run the post-backoff procedure, [right / okay unclear]? So that's, [it's unclear] that's mandatory. We cannot do [anything otherwise / any, any number one unclear]. Help me out here. We, [we unclear] have the long break now? [No / oh unclear], sorry. Our time [three five, five plus three; numbers unclear]. Okay, thanks. Okay, so we still have about fifteen minutes before. Let me know if I [get it wrong / get this one wrong / did something wrong unclear], please. I need to adjust the, [the unclear] schedule, of course. Okay, so we run essentially through all these slides, using the whiteboard for greater clarity, but you have the essential information also in, [in unclear] the slides. Okay, so what I would like to show now is another example that is here presented in [the / these unclear] slides. Don't get scared by the many figures that are used in these, [in these unclear] slides. It's just to highlight something that we already know, but here you have indeed concrete example to further emphasize this. That is, we now know more or less how the basic version of Wi-Fi works. We already said that Wi-Fi is so successful because it works quite well for our needs. But it has got a big problem in general, that is overhead, right? We already commented on that. So now that we know how channel is used in Wi-Fi, this is a practical example that gives evidence to that.

## 八、协议开销与传输效率

### 67 · 01:21:58 · DIFS、物理前导码与各层首部开销

原标说话人 1  01:21:58
So we know that in the case where we need to transmit [the / a unclear] data packet, first of all we need to sense the channel for DIFS. We can consider [DIFS / this unclear] to be fifty microseconds long. So that's for sure something that we need to wait for. Then if we are lucky, if we are lucky, the channel is idle, and we can transmit our packet right away. But the packet that we transmit, we [know already / already know unclear] that [it unclear] has got some headers, right? Actually, we already said it has got a physical layer preamble that is used by the transmitter and receiver to essentially synchronize, and so that the receiver can start [to unclear] demodulating what the transmitter is sending. So at the electronics level, they need this preamble to start the, [the, let's see unclear] communication. And then there is the physical layer header, and then there is the physical, sorry, the MAC layer header, where we have, for example, the duration field. So all these headers are just control information. It's not [a / the unclear] payload. It's not something useful at the MAC layer. It is something that is there. It is useful for the protocol, but not, they are not application layer bits, right? So [they are / you're unclear] there, fine, but from the application, from what would be the application layer perspective, that's something that is not useful, it's not interesting.

### 68 · 01:23:51 · 基本速率发送前导码和首部

原标说话人 1  01:23:51
Okay. So, [but / when unclear] we spend time to transmit [this / these unclear] physical layer preamble, physical layer header, and they are transmitted at the basic rate. So as we commented already, the basic rate is a low speed. So they are transmitted slowly at low speed. And if you consider the basic rate, like in this example, to be one megabit per second, well then you have to wait; it takes time to do that. And then we have the MAC header.

### 69 · 01:24:28 · MAC首部长度随地址需求变化

原标说话人 1  01:24:28
The MAC header again are, [I would say / we say / it's a unclear] non-interesting bits from the point of view of the application. The size of the MAC header in Wi-Fi may actually vary, depending on, for example, how many addresses you need. So if you are in a BSS, isolated BSS, as the one that you have got in your apartment, the only addresses that you need are the transmitter address and [a unclear] receiver address.

### 70 · 01:25:04 · 扩展服务集中的四地址需求

原标说话人 1  01:25:04
If you are in an extended service set, like here on Tongji campus [place-introduction wording unclear], where we have many access points connected through, you know, the, the wired network. Then you may need four different addresses, and the reason for that is that, in an extended service set, you may have, as we know, access points that are connected to each other, right? We already explained the architecture of the network.

### 71 · 01:25:52 · 数据包经两个接入点交付

原标说话人 1  01:25:52
And so, if you are A and you want to send a packet to B, well, then you have to send your packet to the access point you are connected with. This access point one will send the packet to access point two, and then access point two will deliver the packet to B. This happens in an extended service set.

### 72 · 01:26:20 · 源、发送方、接收方与目的地址

原标说话人 1  01:26:20
Okay, now in this case, A is the sender, okay, the transmitter, so it's [the/your unclear] original source and also transmitter of the packet. And access point one is the receiver, but the final destination is B. So, this packet that travels from A to access point one will have A as the transmitter address, which is also the source's address. You will have access point one address as a receiver, and then you will have the destination address, the B's address as destination address. So it needs to have three addresses in the MAC header. Once the packet is received at access point one, [and unclear] access point one has to send the packet to access point two, so that the packet eventually can be delivered to the final destination. This packet, when the packet is here, it [needs/means/names unclear] four addresses in the [MAC unclear] header. Why? Because we need to [specify/specifying unclear] that this packet originally came from source A. The transmitter now is access point one. The receiver now is access point two. And the final destination where this packet has to go is B, right? So, in extended service sets, when the Wi-Fi packets travel from one access point to another, they need four addresses. So this is just to say that the size of the MAC header may vary, okay, may be shorter or longer. Anyway, [um unclear], so you already have to account for [DIFS/SIFS unclear], physical preamble, physical header, MAC header. The payload is the useful, interesting part. [Okay, so that's not overhead; wording unclear]

### 73 · 01:29:08 · 成功传输后的SIFS与确认开销

原标说话人 1  01:29:08
But then, if the packet is hopefully, so in the best case, delivered successfully, you have SIFS. That is [another time interval / another time you have ... interval; wording unclear] you have to wait for. And then acknowledgment, that is a control packet, so not interesting from the application point of view.

### 74 · 01:29:30 · ACK结构与一次传输的总开销

原标说话人 1  01:29:30
And the acknowledgment again is made of physical preamble, physical header, MAC header, so lots of things to be transmitted. And that's the best case. So, you, to transmit the payload, you have to wait [DIFS/SIFS unclear], transmission of physical layer preamble, physical layer header, MAC header, and then SIFS, and then ACK. [Okay unclear], lots of time to just transmit [a/the/zero-article unclear] payload.

### 75 · 01:30:04 · 长载荷效率与失败重传额外开销

原标说话人 1  01:30:04
So you better have a long payload because otherwise your protocol is very, very inefficient, [okay unclear]. And this is the best case. If your transmission fails and you have to perform backoff and retransmit the packet, then you have to wait for the channel to become idle. [DIFS/SIFS unclear], backoff time. Hope that the channel remains idle and you can decrease the backoff counter continuously and over time reach zero, and then transmit your packet, and then SIFS and ACK. Lots of things, right? Just again to transmit a single [payload/failure unclear].

### 76 · 01:30:46 · Wi-Fi协议效率总结

原标说话人 1  01:30:46
So, we [realize/realized unclear] that the efficiency of Wi-Fi is actually pretty low. And this holds, unfortunately, for all versions of Wi-Fi. Okay, we [looked / are looking / have looked unclear] at the basic version, but it's actually a curse for all versions. And on average, you can consider that the efficiency of this scheme is about fifty, fifty-five percent, which is definitely low, right? The maximum efficiency [would/will unclear] be one hundred percent. [So, yeah, hopefully / so, we are halfway; unclear]

## 九、扩展IFS预告

### 77 · 01:31:25 · 引出最后一个机制扩展IFS

原标说话人 1  01:31:25
Okay, that said, we are just missing one last mechanism in the Wi-Fi channel access, and then we are done with the basic version of Wi-Fi, that is the most important one. Okay, so we just [need/needed unclear] to introduce, and we do that after the break, this last piece [for ... unclear] of the protocol that is related to what, actually, something that we know already about, the famous [four/for/form unclear] interframe space, the extended IFS. Remember the extended IFS. Remember the priority ladder, we have SIFS, PIFS, [DIFS/PIFS unclear], and extended IFS. So, we [said/start unclear], let's first focus on SIFS and [DIFS/PIFS unclear], understand how they are used, and then we'll go back to the other [time/timing unclear] intervals. So, now it's time to talk about the longest among these [time/timing unclear] intervals. That was indeed the extended IFS. And just to give you an idea, this extended IFS, [so/or unclear] this [time/timing unclear] interval, can be as long as about three hundred microseconds, so definitely longer than the others that we have considered so far.

### 78 · 01:33:12 · EIFS近似时长与长课间休息

原标说话人 1  01:33:12
Okay, it depends on the version of Wi-Fi that we consider, but just [yeah / you know / no filler; unclear], to keep in mind, again, [you can be considered; subject/construction unclear] equal to three hundred microseconds. [Okay unclear], so just to [have an idea / verify / evaluate; unclear]. So if I'm not wrong, now we stop for twenty-five minutes. Okay.
