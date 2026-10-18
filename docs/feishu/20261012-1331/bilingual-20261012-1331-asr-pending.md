# 双语对照：录音机-20261012-1331

会议主题：录音机-20261012-1331
课程：移动与传感器网络 / Mobile Sensor Networks
上传时间：2026年10月14日（周三） 09:55 （GMT+08）
音频时长：约 01:33:42
整理日期：2026年10月18日
版本：完整忠实双语稿 · 913cf98f5b3c
状态：双语正文已完成（78 对）；课件图共8张（保留原6张，补充2张）；78个分段标题与9个主题标题已加入原生目录

[飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf) · [原始文字记录](https://lcn6dqn3m0yr.feishu.cn/docx/NwvUdszghonyiIxRXpfc5zYpnsg) · [原始录音与播放](https://lcn6dqn3m0yr.feishu.cn/minutes/obcnl1r6fl65o45lkj3o1zq9)

录音文件：20261012-1331.m4a（播放请使用原始录音链接）
课件：[02-WiFi_1-7.pdf](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf)

注意：第9段（00:09:40–00:11:21）英文与原音是否一致，用户已提出异议，正在等待原音ASR复核。本包仅证明正文相对编辑前快照未改动，不能据此证明忠实原音。原始版本行中“完整忠实”是历史稿自带标签，不是本次审计认证。

完整保留78对编辑前双语文字、6张原PNG；新增78个分段标题与9个主题标题，补入固定PDF图46和52，共8张课件图。

来源说明：AP/A/B/C多节点退避、消融和公平性时间线，以及碰撞概率条件推导，没有在固定PDF中找到同一原图。第66段明确提到主要使用白板；这些课堂视觉资料的截图来源仍待确认，未自行重绘或以其他章节图片替代。

原图45第3条只写成功后仍有排队数据时退避，图50及第66段则说明不论队列状态都要执行。此源内差异按原稿保留；本整理不改写技术内容。

说话人、时间戳和段内换行逐字保留；图号是PDF讲义顺序，不是文档图片流水号，也不是图内的小页脚编号。

# 一、退避指数与竞争窗口

## 01 · 00:00:03 · 重传失败数据包需要退避

原标说话人 1  00:00:03
And we said that whenever a Wi-Fi node needs to recontend for the channel because it has to retransmit a packet that failed, this node will perform the backoff procedure.
我们之前说过，当一个 Wi-Fi 节点需要重传发送失败的数据包，因而必须重新竞争信道时，这个节点就会执行退避过程。

## 02 · 00:00:29 · 退避过程与竞争窗口指数表达式

原标说话人 1  00:00:29
We explained how the backoff procedure works. First, a node needs to wait for the channel to be idle for DIFS. Then it will draw an integer out of a range of possible values, selecting each of them with equal probability. This range goes from zero to the contention window parameter. The first time that we use the backoff procedure to transmit a packet, we set this parameter to its minimum value. If we need to perform backoff again to transmit this packet, because, for example, we fail and fail and fail, every time we increase the contention window. We said that, roughly speaking, this value doubles every time. To be more precise, the relation according to which CW increases is the following. The CW value is expressed as a power of two minus one, where this exponent is called the backoff exponent.
我们已经解释过退避过程是如何工作的。首先，节点需要等待信道连续空闲一个 DIFS 的时间。然后，它会从一个取值范围中随机抽取一个整数，每个整数被选中的概率都相同。这个范围从零到竞争窗口参数 CW。第一次通过退避过程发送某个数据包时，我们把这个参数设为最小值。如果为了发送同一个数据包，还需要再次退避，因为，例如，我们失败、失败、再失败，那么每次都要增大竞争窗口。我们说过，粗略地讲，这个值每次都会翻倍。更准确地说，CW 按照下面这个关系增大。CW 的值表示为二的某个指数次方减一，这个指数称为退避指数。

[02-WiFi_1-7.pdf 图47：Backoff Value: Binary Exponential Backoff · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcnxfTo4JUVDPN3hf2lJuS3gd)

课件：02-WiFi_1-7.pdf · PDF第24页上半页 · 图47（按PDF顺序）

## 03 · 00:02:48 · 最小退避指数与CW为31的例子

原标说话人 1  00:02:48
For example, the first time we use the backoff procedure for a data packet, we set the backoff exponent to its minimum. By default, in the early versions of Wi-Fi, this is equal to five. This example refers to the early versions of Wi-Fi. If we take this example value, we see that, as we said last time, the first time we use this contention window minimum, the value will be two to the power of the minimum exponent minus one. Since this is five, it will be two to the five minus one, which is 31. That is why on Saturday, when we introduced this procedure, we said: let's consider the minimum contention window 31. The second time we use backoff for the same packet, we are going to increase the backoff exponent. If this was our first value, the second time we will have a second value equal to the previous one plus one.
例如，第一次对某个数据包执行退避过程时，我们把退避指数设为最小值。在早期版本的 Wi-Fi 中，这个值默认为五。这里的例子指的是早期版本的 Wi-Fi。如果采用这个示例值，就会看到，正如上次所说，第一次使用最小竞争窗口时，它的值等于二的最小指数次方减一。由于这个指数是五，所以结果就是二的五次方减一，也就是 31。这就是为什么周六介绍这个过程时，我们说，假设最小竞争窗口为 31。第二次为同一个数据包执行退避时，我们要增大退避指数。如果这是第一次的取值，那么第二次的取值就等于前一次的值加一。

[02-WiFi_1-7.pdf 图48：Example: CW Growth (802.11b, CWmin = 31, CWmax = 1023) · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcnXPHO3jBPy2cpA3xE0Bh9Vc)

课件：02-WiFi_1-7.pdf · PDF第24页下半页 · 图48（按PDF顺序）

## 04 · 00:05:24 · 第二次退避的竞争窗口计算

原标说话人 1  00:05:24
This means that the second time we compute the contention window, it will equal two to the power of the backoff exponent at the second step, minus one. This is two to the power of the exponent at the first step increased by one, minus one.
这意味着，第二次计算竞争窗口时，它等于二的第二步退避指数次方减一。这也就是二的“第一步的指数加一”次方减一。

## 05 · 00:06:01 · 窗口增至63并受CW最大值限制

原标说话人 1  00:06:01
In our example this is two to the power of six minus one, which is 63. This is the way we increase the contention window minimum value every time until we reach CW_max. After reaching this value, we do not increase CW beyond it, even if we still need to perform backoff for the same packet.
在我们的例子中，就是二的六次方减一，结果为 63。我们就是这样每次增大竞争窗口的最小值，直到达到 CW_max。达到这个值以后，即使仍然需要为同一个数据包执行退避，我们也不会再把 CW 增大到这个值以上。

## 06 · 00:06:57 · 退避指数逐次加一的规则

原标说话人 1  00:06:57
The general rule is that at step i, the generic step i, we set the backoff exponent equal to the exponent at the previous step increased by one.
一般规则是：在第 i 步，也就是任意的第 i 步，我们把退避指数设为前一步的退避指数加一。

## 07 · 00:07:28 · 竞争窗口扩大与随机取值范围

原标说话人 1  00:07:28
At the generic step i, the contention window is computed as two to the power of the backoff exponent at step i, minus one. This is the general expression used to compute the backoff exponent and the corresponding contention window at each step. Every time we need to perform backoff for a given data packet, we roughly double the contention window. We enlarge the possible integer values that we can draw to compute the backoff time. Before explaining why the standard says to double the contention window every time we need to perform backoff to transmit a packet, let me mention something reported in one of the earlier slides.
在任意的第 i 步，竞争窗口等于二的第 i 步退避指数次方减一。这就是计算每一步的退避指数及相应竞争窗口所用的一般表达式。每次需要为某个数据包执行退避时，我们都会把竞争窗口大致翻倍，也就是扩大随机抽取整数的取值范围，以此计算退避时间。在解释为什么标准规定每次为发送同一个数据包而退避时都要把竞争窗口翻倍之前，我先补充一下前面某页幻灯片中提到的一点。

# 二、退避触发条件与计数规则

## 08 · 00:09:04 · 发送失败时的退避回顾

原标说话人 1  00:09:04
I didn't comment on that because I didn't want to put too many things together at the same time. One more important thing to say about backoff is that, of course, it is performed, as we said, when we have a packet that has been transmitted and failed.
我当时没有解释这一点，因为不想一下子把太多内容放在一起讲。关于退避，还有一个重要的地方需要说明。当然，正如我们已经说过的，如果一个数据包已经发送过，但发送失败了，就需要执行退避。

## 09 · 00:09:40 · 新包到达但侦听到忙信道

原标说话人 1  00:09:40
So we need to recontend for the channel and transmit the packet again. This is the case we have considered so far in which we need to perform backoff. However, there are two more situations in which we need to perform exactly the same backoff procedure. It also needs to be performed when a transmitting node has a packet to transmit, senses the channel, and finds it busy. We already know that we cannot access the channel right away because of the carrier-sense multiple-access principle. We get a packet from the higher layers, and at the MAC layer we sense the channel for DIFS, but it is busy. What we knew so far is that we cannot access the channel because it is busy. We are like polite people; we don't want to interrupt someone who is already talking.
因此，我们需要重新竞争信道，再次发送这个数据包。这就是到目前为止我们讨论过的需要退避的情况。不过，还有另外两种情况也需要执行完全相同的退避过程。其中一种情况是，发送节点有一个数据包要发送，但侦听信道时发现信道忙。根据载波侦听多路访问的原则，我们已经知道，这时不能立即接入信道。我们从高层收到一个数据包，在 MAC 层侦听信道一个 DIFS 的时间，却发现信道忙。到目前为止，我们知道的是，由于信道忙，所以不能接入。就像有礼貌的人一样，我们不想打断已经在说话的人。

[02-WiFi_1-7.pdf 图45：When Does a Station (Re)contend? — the Backoff Cases · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcnc7j1Yu1VqrAZpgPfPUc4le)

课件：02-WiFi_1-7.pdf · PDF第23页上半页 · 图45（按PDF顺序）

## 10 · 00:11:21 · 忙信道情况下等待的具体含义

原标说话人 1  00:11:21
So we wait. That's what we said, but now we need to be more precise: what exactly do we mean by waiting, and for how long? In reality, also in this case we need to apply the backoff procedure. We wait for the backoff time according to this procedure. This is the rule again also in this first case, when a Wi-Fi node gets a new packet from the higher layers and the MAC needs to apply the protocol to transmit it.
所以，我们就等待。之前我们是这样说的，但现在需要说得更准确一些：这里的等待究竟是什么意思，又要等多久？实际上，这种情况下也需要采用退避过程。我们按照这个过程等待相应的退避时间。这条规则同样适用于这里的第一种情况，也就是 Wi-Fi 节点从高层收到一个新数据包，需要由 MAC 按照协议将它发送出去的情况。

## 11 · 00:12:27 · 退避计数递减、冻结与恢复

[02-WiFi_1-7.pdf 图46：Backoff Procedure (Collision Avoidance) · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcnWTFsquj2iIzhTunL0hhLyd)

课件：02-WiFi_1-7.pdf · PDF第23页下半页 · 图46

原标说话人 1  00:12:27
First we need to sense the channel for DIFS. If the channel is sensed busy, we apply backoff. First we wait for it to become idle again and sense it as idle for DIFS. Then we draw an integer with equal probability from the range zero to CW_min, set the backoff time to that integer multiplied by the time slot, and decrease the backoff counter slot by slot as long as the channel is idle. If the channel becomes busy while we are decreasing the counter, we need to stop and freeze it; we cannot decrease it. When the channel becomes idle again, we sense it for DIFS. If it stays idle for that time, we resume decreasing the counter until it reaches zero. As soon as it reaches zero, we can access the channel and transmit our packet. The transmission may be successful, in which case we are done. Or the packet may fail, and we must recontend for the channel using backoff. Now we know two conditions under which we perform backoff.
首先，我们需要侦听信道一个 DIFS 的时间。如果侦听到信道忙，就执行退避。我们先等待信道重新变为空闲，并确认它连续空闲一个 DIFS 的时间。然后，从零到 CW_min 的范围中等概率地随机抽取一个整数，把退避时间设为这个整数乘以时隙长度。只要信道空闲，就逐个时隙递减退避计数器。如果递减过程中信道变忙，就必须停止并冻结计数器，不能继续递减。信道再次空闲后，我们再侦听一个 DIFS 的时间。如果信道在这段时间内一直空闲，就继续递减计数器，直到它变为零。一旦计数器变为零，我们就可以接入信道并发送数据包。发送可能成功，这样就完成了；也可能失败，这时就必须通过退避重新竞争信道。现在，我们已经知道两种需要退避的情况。

## 12 · 00:14:39 · 用例子理解退避及窗口扩大原因

原标说话人 1  00:14:39
Let's leave the third condition for later. Before introducing it, I want to present an example of a situation where we apply backoff. With this example, I want to clarify why we use backoff, why it is actually useful, and why the standard says that every time we perform backoff for a given packet, we need to double the contention window parameter.
第三种情况留到后面再说。在介绍它之前，我想先举一个需要退避的例子。通过这个例子，我想说明为什么要使用退避，退避究竟有什么用，以及为什么标准规定，每次为同一个数据包执行退避时，都需要把竞争窗口参数翻倍。

# 三、多节点退避时序示例

## 13 · 00:15:26 · 学习技术机制背后的设计理由

原标说话人 1  00:15:26
The main thing here, when we study Wi-Fi, is of course to learn how we use a technology that is used every day by almost everyone. It's good to know how things work, but it is also important to understand the rationale. Why do things happen? Why do we make certain choices while developing a technology? That's the really important thing this class should give you: strengthening your ability to understand why certain things have been decided in a certain manner when designing a system. There is always a reason, and we need to learn how to reason about things and understand the solutions that have been created.
我们学习 Wi-Fi，当然主要是为了了解如何使用一种几乎人人每天都在使用的技术。知道事物如何运作很好，但理解背后的道理同样重要。为什么会这样？为什么在开发一项技术时，我们会作出某些选择？这才是这门课真正应该带给大家的东西：提高你们的能力，让你们理解，在设计一个系统时，为什么某些事情会以某种方式确定下来。这背后总有原因，我们需要学会分析问题，理解人们提出的解决方案。

## 14 · 00:16:47 · 引入接入点和A、B、C拓扑

原标说话人 1  00:16:47
That's the important attitude we need to develop. Understanding why is a kind of mental exercise that we need to do. Good. Let's consider a simple topology where we have an access point and then A, B, and C.
这就是我们需要培养的重要态度。理解“为什么”，是我们需要进行的一种思维训练。好，我们来看一个简单的拓扑，其中有一个接入点，以及 A、B、C 三个节点。

## 15 · 00:17:18 · 所有节点彼此可听的BSS场景

原标说话人 1  00:17:18
The access point is here. These are our user nodes, and they are part of this BSS, which means they can talk with the access point. Let's consider the simple case where all nodes can hear each other. Now let's represent their behavior over time.
接入点在这里。这些是我们的用户节点，它们属于这个 BSS，也就是说，它们都可以与接入点通信。我们先考虑一种简单情况：所有节点都能听到彼此的信号。现在来表示它们随时间变化的行为。

## 16 · 00:17:58 · A收到数据包并侦听DIFS

原标说话人 1  00:17:58
This is the timeline. We will draw a timeline for each node: the access point, user A, user B, and user C. Assume that when we start looking at the system, we observe that A has received a packet from its higher layers. Its application layer has generated some data. A gets this packet at its MAC layer and understands that it has to try to transmit it. We know that in this case a Wi-Fi node will first sense the channel for DIFS. Let's assume that the channel is idle.
这是时间轴。我们给每个节点都画一条时间轴，分别对应接入点、用户 A、用户 B 和用户 C。假设开始观察系统时，我们发现 A 从它的高层收到了一个数据包。它的应用层生成了一些数据。A 在 MAC 层收到这个数据包，知道自己需要尝试发送。我们知道，这种情况下，Wi-Fi 节点首先会侦听信道一个 DIFS 的时间。假设信道是空闲的。

## 17 · 00:19:08 · A发送数据并获得SIFS后的ACK

原标说话人 1  00:19:08
In this case, A can access the channel and transmit its data packet. It is a unicast packet intended for the access point. Let's be optimistic and consider that it is successfully received by the access point. Therefore, the access point will send an acknowledgment after SIFS. This is the usual story that we have told many times.
这时，A 就可以接入信道并发送它的数据包。这是一个发给接入点的单播数据包。我们乐观一点，假设接入点成功接收了它。因此，接入点会在 SIFS 之后发送一个确认。这就是我们已经讲过很多次的常规过程。

## 18 · 00:19:49 · B和C读取首部设置NAV

原标说话人 1  00:19:49
We also know that under these conditions the other nodes, B and C, demodulate the data packet's header. They read the Duration field so they can set their NAV counter, extending over the expected duration of the dialogue.
我们还知道，在这种情况下，其他节点 B 和 C 会解调这个数据包的首部。它们读取 Duration（持续时间）字段，从而设置各自的 NAV 计数器，使其覆盖这次交互预计持续的时间。

## 19 · 00:20:25 · B和C在信道忙时收到新数据包

原标说话人 1  00:20:25
So far so good; this is exactly what we did in the past. Now let's add some events. Let's say that B and C, while their NAV is set to a positive value, also receive a data packet from their respective upper layers. For example, at this point B gets a packet queued at its MAC layer, and at this other point C also gets a packet from its higher layers.
到这里一切都很顺利，和我们之前讲的完全一样。现在再加入一些事件。假设 B 和 C 的 NAV 值仍为正数时，也分别从各自的高层收到了一个数据包。例如，在这个时刻，B 的 MAC 层有一个数据包进入队列；在另一个时刻，C 也从高层收到了一个数据包。

## 20 · 00:21:21 · 依据本地忙状态独立执行退避

原标说话人 1  00:21:21
While the dialogue between A and the access point is going on, B and C now also have a packet to transmit. Clearly their NAV is set, so they know the channel is busy and cannot access it. That is the principle of carrier sensing. We are essentially in this situation, situation number one: B and C get a new packet but sense that the channel is busy. What do we have to do? Apply backoff. Remember that our scheme is distributed, so each node makes decisions for itself based on the state of the system that it observes. B will say: I got a packet, but the channel is busy.
在 A 和接入点进行交互期间，B 和 C 现在也各有一个数据包要发送。显然，它们的 NAV 已经设置，所以它们知道信道忙，不能接入。这就是载波侦听的原则。我们实际上处于这里的这种情况，也就是第一种情况：B 和 C 收到了新数据包，但侦听到信道忙。我们该怎么办？执行退避。记住，我们采用的是分布式方案，所以每个节点都根据自己观察到的系统状态独立作出决定。B 会说：我收到了一个数据包，但信道忙。

## 21 · 00:22:43 · 等待空闲DIFS后随机抽取退避值

原标说话人 1  00:22:43
What I need to do is apply backoff. It waits for the channel to become idle again, senses it as idle for DIFS, and if the channel stays idle for DIFS, it can draw an integer out of the range zero to CW_min. The same applies to C. C says: I got a packet to transmit, but the channel is busy. It knows it has to perform backoff. It waits for the channel to become idle and verifies that it remains idle for DIFS. The channel will be idle because nobody else is doing anything.
我需要做的就是执行退避。它等待信道重新空闲，再侦听一个 DIFS 的时间。如果信道连续空闲了一个 DIFS，它就可以随机抽取一个整数，取值范围是零到 CW_min。C 也是一样。C 会说：我有一个数据包要发送，但信道忙。它知道自己需要执行退避，于是等待信道空闲，并确认信道连续空闲一个 DIFS 的时间。由于没有其他节点在做什么，所以信道会保持空闲。

## 22 · 00:24:00 · B抽到2而C抽到5的例子

原标说话人 1  00:24:00
It too draws an integer with equal probability from the same range of values. Let's assume that B draws the integer two and C draws five. This is just an example.
它也从同一个取值范围中等概率地随机抽取一个整数。假设 B 抽到的是二，而 C 抽到的是五。这只是一个例子。

## 23 · 00:24:36 · 两个节点并行倒计时至B先归零

原标说话人 1  00:24:36
In that case, B computes a backoff time equal to twice the time-slot duration. Similarly, C computes a backoff time of five time slots. Each of them decreases its own backoff counter slot by slot. B senses the channel for one time slot. The channel is currently idle, so it decreases its counter by one. C does the same, decreasing its own counter by one. In the next time slot, B again senses the channel as idle and decreases its counter by one. C does the same, but now B's backoff counter has reached zero.
在这种情况下，B 计算出的退避时间等于两个时隙的长度。类似地，C 计算出的退避时间是五个时隙。它们各自逐个时隙递减自己的退避计数器。B 侦听信道一个时隙，当前信道是空闲的，因此把计数器减一。C 也做同样的事，把自己的计数器减一。下一个时隙中，B 再次侦听到信道空闲，于是再把计数器减一。C 也一样，但这时 B 的退避计数器已经变为零。

## 24 · 00:26:12 · B获得发送机会并成功收到ACK

原标说话人 1  00:26:12
B is entitled to access the channel, so it transmits its data packet. The packet is intended for the access point because we are considering unicast packets, and in this network architecture all Wi-Fi user nodes communicate only with the access point. Again, let's be optimistic: the packet is successfully received, and the access point sends an acknowledgment after SIFS.
B 获得了接入信道的资格，于是发送它的数据包。这个数据包的目的地是接入点，因为我们考虑的是单播数据包，而且在这种网络架构中，所有 Wi-Fi 用户节点都只与接入点通信。我们还是乐观一点：数据包成功接收，接入点在 SIFS 之后发送确认。

## 25 · 00:27:02 · B发送期间A设NAV且C冻结退避

原标说话人 1  00:27:02
Upon B's data transmission, the other nodes can set their NAV. They can read the Duration field in the data packet's header. We also need to highlight that both A and C set their NAV. What does this mean for A? It's fine; it doesn't have anything to do. But for C, it means that it must freeze its backoff counter for this duration.
B 发送数据包时，其他节点可以设置各自的 NAV。它们可以读取数据包首部中的Duration 字段。还需要强调的是，A 和 C 都会设置自己的 NAV。这对 A 意味着什么？没有关系，它没有什么事情要做。但对 C 而言，这意味着在这段时间内，它必须冻结自己的退避计数器。

## 26 · 00:28:03 · C在信道恢复后继续剩余倒计时

原标说话人 1  00:28:03
The channel is now busy, so C cannot decrease its counter; it has to suspend the countdown. During all this time C is essentially blocked and waits for the channel to become idle again. It makes sure the channel is idle for DIFS, then resumes decreasing its backoff counter. It still has three time slots to go. It senses the channel for a time slot: yes, it is idle, so it can decrease the counter by one. It senses the channel again for another time slot; it is idle, so it can decrease the counter by one. Then again, the channel is idle for one more time slot, so it decreases the counter by one.
现在信道忙，所以 C 不能递减计数器，必须暂停倒计时。在这整段时间内，C 基本上被阻塞了，只能等待信道再次空闲。它确认信道连续空闲一个 DIFS 的时间，然后继续递减退避计数器。它还剩下三个时隙。它侦听信道一个时隙：是的，它是空闲的，所以可以把计数器减一。它再侦听一个时隙，信道空闲，因此又可以把计数器减一。然后，信道又空闲了一个时隙，它再把计数器减一。

## 27 · 00:29:23 · C归零发送成功与退避作用

原标说话人 1  00:29:23
Now its backoff counter is down to zero, so it can access the channel and transmit its data packet. Again, being optimistic, we say that this is successful, so it receives the acknowledgment after SIFS. We are all happy because all nodes could transmit their data packets successfully. This is an example of applying the backoff procedure under this condition. It also allows us to understand the importance of backoff. That is the ultimate goal I was aiming for.
现在，它的退避计数器已经变为零，因此可以接入信道并发送数据包。我们还是乐观地假设发送成功，于是它在 SIFS 之后收到了确认。大家都很高兴，因为所有节点都成功发送了各自的数据包。这就是在这种情况下执行退避过程的一个例子。它也让我们能够理解退避的重要性，这才是我最终想要说明的。

# 四、消融实验与概率性碰撞避免

## 28 · 00:30:26 · 通过消融实验考察没有退避的系统

原标说话人 1  00:30:26
How can we understand the importance of backoff? Let's make a little game that, scientifically speaking, is called an ablation study. An ablation study is when you remove a feature of a system and study the behavior of that system without that feature. Our small game is an ablation study of this particular backoff procedure, or Wi-Fi channel access. Let's think: what would happen if backoff were not there?
怎样理解退避的重要性呢？我们来做一个小游戏，用科研中的说法，这叫消融实验。所谓消融实验，就是从系统中去掉某个功能，再研究系统在缺少这一功能时的行为。我们这个小游戏，就是针对这一退避过程，也就是 Wi-Fi 信道接入过程，进行一次消融实验。想一想，如果没有退避，会发生什么？

## 29 · 00:31:22 · 移除退避后重新推演

原标说话人 1  00:31:22
Let's roll back the story and start from the beginning, but this time assume there is no backoff. What would be the behavior of our nodes?
我们把整个过程倒回去，从头再来一次，但这次假设没有退避。我们的节点会怎样行动呢？

## 30 · 00:31:43 · 无退避时A的首次发送不变

原标说话人 1  00:31:43
At the beginning everything is the same because the only node with a packet to transmit is A. It listens to the channel, the channel is idle for DIFS, and it accesses the channel and transmits the packet.
最开始，一切都一样，因为只有 A 有数据包要发送。它侦听信道，信道连续空闲一个 DIFS 的时间，于是它接入信道并发送数据包。

## 31 · 00:32:02 · B和C同时发送导致必然碰撞

原标说话人 1  00:32:02
Again, let's be optimistic: the access point sends back an acknowledgment, and the other nodes B and C both set their NAV. This is exactly as before. Assume that B and C also get a packet to transmit at different points in time. But now we do not have backoff. We have to think what would happen if backoff were not there. What would B and C do? We still have carrier-sense multiple access. Since B and C both sense the channel as busy because their NAV is set, they cannot access the channel while it is busy. They will wait for it to become idle and make sure it is idle. But if there is no backoff, they can then access the channel. They say: the channel is idle, I can access it and transmit. Remember, in this game we assume there is no backoff. Both transmit their data packets after sensing the channel idle. What do we have here? A collision. They both access the channel at the same time with probability one. It is certain they will do that, and they fail because their transmissions overlap. The access point will not be able to demodulate either packet correctly.
我们还是乐观一点：接入点返回一个确认，其他两个节点 B 和 C 都设置了各自的 NAV。这与之前完全一样。假设 B 和 C 也在不同的时刻各自收到了一个要发送的数据包。但现在没有退避了。我们需要想一想，没有退避会怎么样。B 和 C 会怎么做？我们仍然采用载波侦听多路访问机制。由于 B 和 C 都设置了 NAV，因此它们都认为信道忙，不能在信道忙时接入。它们会等待信道空闲，并确认信道确实空闲。但是，如果没有退避，随后它们就可以接入信道了。它们会说：信道空闲，我可以接入并发送。记住，在这个小游戏里，我们假设没有退避。两者在侦听到信道空闲后，都会发送各自的数据包。这时会发生什么？碰撞。它们同时接入信道的概率为一，也就是说，它们一定会同时接入，而且会因为发送过程重叠而失败。接入点无法正确解调其中任何一个数据包。

## 32 · 00:34:43 · 退避作为碰撞避免机制

原标说话人 1  00:34:43
The first conclusion is that backoff was introduced in our system to avoid collisions between contending nodes. In this example B and C contend for the channel, and backoff is there to avoid their collision. Remember that we said Wi-Fi is a CSMA scheme with collision avoidance.
第一个结论是，我们在系统中引入退避，是为了避免竞争节点之间发生碰撞。在这个例子里，B 和 C 竞争信道，而退避就是为了避免它们相互碰撞。记得我们说过，Wi-Fi 采用的是带碰撞避免的 CSMA 方案。

## 33 · 00:35:39 · 错开行动时间减少拥挤

原标说话人 1  00:35:39
Backoff is a mechanism that helps avoid collisions. The basic idea is very simple: whenever there is a crowded situation, you try to desynchronize from the others so that you find a free road ahead. It is exactly the same thing. If it is peak hour, you don't want to jump into the traffic like everyone else.
退避是一种有助于避免碰撞的机制。它的基本思想很简单：在拥挤的情况下，尽量与其他人错开行动时间，这样前面的路就可能是畅通的。道理完全一样。如果正值高峰时段，你不会想和所有人一起挤进车流。

## 34 · 00:36:25 · 避开高峰时段的生活类比

原标说话人 1  00:36:25
You wait and try to pick a time when not many other people will be there. It is the same principle. You pick a time to desynchronize your action from the others, avoiding collisions with them or finding yourself in a traffic jam. That's exactly the same principle.
你会等一等，尝试选择一个其他人比较少的时间。这里也是同样的原理。你选一个时间，让自己的行动与其他人错开，从而避免与他们碰撞，或避免让自己陷入交通拥堵。这是完全相同的道理。

## 35 · 00:37:02 · 相同退避值仍会导致碰撞

原标说话人 1  00:37:02
What I want to underline is that our first observation is that backoff is a collision-avoidance mechanism, but it is still probabilistic. Why? If B and C draw the same backoff value, they are going to collide. If C too drew two as its integer, then they would not be desynchronized from each other. Both decrease their counters during the first time slot and again during the second. Under the assumption that both drew two, their counters reach zero at exactly the same time. They access the channel at exactly the same time and collide.
我想强调的是，我们的第一个观察是：退避是一种避免碰撞的机制，但它仍然是概率性的。为什么？如果 B 和 C 抽到了相同的退避值，它们就会发生碰撞。如果 C 抽到的整数也是二，那么两者的行动时间就没有错开。它们都在第一个时隙把计数器减一，又在第二个时隙再减一。假设两者都抽到了二，那么它们的计数器就会在完全相同的时刻变为零。它们会在完全相同的时刻接入信道，从而发生碰撞。

## 36 · 00:38:58 · 退避只能概率性地避免碰撞

原标说话人 1  00:38:58
Backoff is a way to avoid collisions, but it does not avoid them with probability one. There is still a certain probability that contending nodes may collide. It is a probabilistic collision-avoidance mechanism.
退避是一种避免碰撞的方法，但它不能以百分之百的概率避免碰撞。竞争节点之间仍然有一定概率发生碰撞。因此，它是一种概率性的碰撞避免机制。

## 37 · 00:39:28 · 准备讨论扩大竞争窗口的作用

原标说话人 1  00:39:28
This is our first observation. Is it clear so far? If so, let me make a second one. Sorry, let me check this, because today is a bit different. We have a second observation to make. We are close to the break, but let me start introducing it, then we will finish after the short break.
这就是我们的第一个观察。到这里清楚吗？如果清楚，我再讲第二个。不好意思，我先确认一下这个，因为今天的情况有点不一样。我们还有第二个观察要讨论。快到休息时间了，不过我先开个头，短暂休息之后再讲完。

# 五、碰撞概率与竞争窗口

## 38 · 00:40:13 · CW最小值范围内共有多少整数

原标说话人 1  00:40:13
The second observation concerns the benefit of increasing the contention window every time we need to perform backoff for a given data packet. Consider the same example as before: the access point, A, B, and C. A talks with the access point, then B and C both get a packet while the channel is busy. They need to apply backoff and, after sensing the channel idle for DIFS, draw an integer from this range of values. Since this is the first time they run backoff for this packet, both use zero to CW_min as the range of possible integers. How many values are there? There are CW_min plus one integers.
第二个观察涉及这样做的好处：每次需要为同一个数据包执行退避时，都增大竞争窗口。还是考虑之前那个例子，有接入点、A、B 和 C。A 与接入点通信，然后 B 和 C 都在信道忙的时候收到了数据包。它们需要执行退避，在确认信道连续空闲一个 DIFS 的时间后，随机抽取一个整数，取值就在这个范围内。由于这是它们第一次为这个数据包执行退避，所以两者采用的整数取值范围都是零到 CW_min。这个范围里有多少个值？一共有 CW_min + 1 个整数。

## 39 · 00:41:48 · 计入零使取值数量增加一

原标说话人 1  00:41:48
Including zero makes it plus one. This is the number of integers in that range.
因为还要算上零，所以要加一。这就是这个范围内整数的个数。

## 40 · 00:41:59 · 均匀抽取整数的概率

原标说话人 1  00:41:59
What we want to compute, since we said that backoff is a probabilistic collision-avoidance mechanism, is the probability that B and C collide. That's the probability we want to compute. We already know that they will collide if they draw the same integer from this range. Remember that a node draws an integer with uniform probability: the same probability for every value. If we consider the probability that a node draws a generic integer n, it is one over (CW_min + 1), because this is the number of integers in the range. Since each value has equal probability, it is easy to see that the probability that an integer, a generic integer, is drawn from this range by a node is one over (CW_min + 1). This is basic probability theory. Each integer is selected with exactly the same probability. This probability is the same for all of them.
既然我们说退避是一种概率性的碰撞避免机制，那么我们想要计算的就是B 和 C 发生碰撞的概率。这就是我们要计算的概率。我们已经知道，如果它们从这个范围内抽取了相同的整数，就会发生碰撞。记住，节点是以均匀概率抽取整数的，也就是说，每个值被抽中的概率都一样。如果考虑节点抽中某个一般的整数 n 的概率，那么它就是 1/(CW_min + 1)，因为这个范围内一共有 CW_min + 1 个整数。由于每个值的概率都相等，很容易看出，某个整数，也就是某个一般的整数，被节点从这个范围内抽中的概率是 1/(CW_min + 1)。这是基本的概率论知识。每个整数被选中的概率完全相同。对所有整数来说，这个概率都一样。

## 41 · 00:44:32 · 课间休息与碰撞概率预告

原标说话人 1  00:44:32
Let's stop for five minutes, and then use the short break... Then we will resume and see how the collision probability can be computed.
我们先停五分钟，利用这个短暂的休息……然后我们再继续，看看如何计算碰撞概率。

## 42 · 00:49:19 · 从条件概率推导两节点碰撞

原标说话人 1  00:49:19
Good. Let's look at our computation. The probability that B and C collide is, as we said, very simple, so don't worry; this is a very simple derivation. It is the probability that B and C draw the same value, let's say n, the same integer. Let's start by considering that B draws a given integer n, whatever it is. What we first compute is the conditional probability that C also draws n, given that B drew n. Remember that our scheme is simple because it is distributed. Every node makes its own decisions according to the protocol rules, independently of the others.
好。我们来看看这个计算。正如刚才所说，B 和 C 发生碰撞的概率很容易计算，所以不用担心，这个推导非常简单。它就是 B 和 C 抽中同一个值，也就是同一个整数，比如 n 的概率。我们先考虑 B 抽中了某个给定的整数 n，不管它具体是多少。首先要计算的是：在已知 B 抽中 n 的条件下，C 也抽中 n 的条件概率。记住，我们的方案之所以简单，是因为它是分布式的。每个节点都按照协议规则独立作出自己的决定，不受其他节点影响。

## 43 · 00:51:21 · 节点独立选择与条件无关性

原标说话人 1  00:51:21
The fact that B drew n will not affect the probability that C draws n. C does whatever it decides following the protocol, but it is not affected by what other nodes do. This is therefore equal to the probability that C draws n, simply that, because it doesn't matter what B does. C does things by itself.
B 抽中了 n 这个事实，不会影响 C 抽中 n 的概率。C 按照协议自行决定怎么做，不会受到其他节点行为的影响。因此，这就等于 C 抽中 n 的概率，仅此而已，因为 B 做了什么并不重要。C 是独立行事的。

## 44 · 00:52:17 · 给定B选择n时C碰撞的概率

原标说话人 1  00:52:17
What is the probability that C draws n? What is the probability that an integer is selected from zero to CW_min? We have written it here. Given that B has drawn n, the probability that C also draws n is this one. Conditioned on B drawing n, this is the conditional collision probability.
C 抽中 n 的概率是多少？从零到 CW_min 之间选中某个整数的概率是多少？我们已经写在这里了。已知 B 抽中了 n，C 也抽中 n 的概率就是这个。在 B 抽中 n 的条件下，这就是发生碰撞的条件概率。

## 45 · 00:53:12 · 遍历所有n去掉条件限制

原标说话人 1  00:53:12
To compute the original probability, we now need to remove the conditioning and consider any possible n. We want to compute the probability that B and C collide without conditioning on any event. We need to consider all possible integer values from zero to CW_min. For any n, the collision probability involves the probability that C draws n if B has also drawn n.
为了计算最初要求的概率，我们现在需要去掉这个条件，把所有可能的 n 都考虑进去。我们要计算的是不附加任何事件条件时，B 和 C 发生碰撞的概率。我们需要考虑从零到 CW_min 的所有可能整数值。对于任意 n，碰撞概率都涉及这样一个概率：在 B 也抽中了 n 的情况下，C 抽中 n 的概率。

## 46 · 00:54:22 · B选中n的概率与碰撞条件

原标说话人 1  00:54:22
Let's first write the probability that B draws n. It is again one over (CW_min + 1). Given that, a collision happens if C also draws n, and that happens with this probability.
先写出 B 抽中 n 的概率。它仍然是 1/(CW_min + 1)。在这个条件下，如果 C 也抽中了 n，就会发生碰撞，而这件事发生的概率就是这个。

## 47 · 00:54:59 · 求和化简得到碰撞概率

原标说话人 1  00:54:59
We multiply by one over (CW_min + 1), the probability that C draws n. We therefore sum over n from zero to CW_min the term 1/(CW_min + 1)^2. This is a constant term inside the sum. How many times do we sum it? CW_min + 1 times. This gives (CW_min + 1)/(CW_min + 1)^2. We simplify numerator and denominator and get 1/(CW_min + 1).
我们再乘上 1/(CW_min + 1)，也就是 C 抽中 n 的概率。因此，我们对 n 从零到 CW_min 求和，求和项为 1/(CW_min + 1)^2。这个求和项是常数。我们要把它加多少次？CW_min + 1 次。这样就得到 (CW_min + 1)/(CW_min + 1)^2。把分子和分母约分，得到 1/(CW_min + 1)。

## 48 · 00:56:35 · 两节点碰撞概率的最终结论

原标说话人 1  00:56:35
The final result is that the probability that B and C collide in our simple example is one over (the contention window plus one). If you were able to follow the computation, great. It is a simple probability calculation, but if your background is different and you have not seen probability in previous courses, do not worry. The important thing is to retain the final message.
最终结果是，在这个简单的例子中，B 和 C 发生碰撞的概率等于竞争窗口加一的倒数。如果你们跟上了这个计算过程，那很好。这只是一个简单的概率计算，但如果你们的知识背景不同，以前的课程里没有学过概率，也不用担心。重要的是记住最后的结论。

## 49 · 00:57:27 · 竞争窗口越大碰撞概率越低

原标说话人 1  00:57:27
In our simple example, the probability that B and C collide while performing backoff equals this ratio, which decreases as the contention window minimum increases. The larger the contention window, the lower the ratio and therefore the lower the collision probability. This is something everybody can understand. This refers to the simple example, but it expresses a general rule: collision probability in backoff decreases as the contention window increases. What does this tell you? Why am I making this second observation? We wanted to understand why in Wi-Fi, every time we perform backoff for a given data packet, we roughly double the contention window. We increase it significantly every time. Why? To reduce the probability of collision among contending nodes.
在这个简单的例子里，B 和 C 在执行退避时发生碰撞的概率等于这个比值，它会随着最小竞争窗口的增大而减小。竞争窗口越大，这个比值就越小，因此碰撞概率也越低。这一点大家都能理解。虽然我们说的是一个简单的例子，但它体现了一条普遍规律：退避过程中的碰撞概率会随着竞争窗口的增大而降低。这说明了什么？我为什么要提出第二点观察？我们想弄清楚，为什么在 Wi-Fi 中，每次为某个给定的数据包执行退避时，都要把竞争窗口大致扩大一倍。每次都要显著增大它。为什么？为了降低竞争节点之间发生碰撞的概率。

# 六、机制局限与广播多播

## 50 · 00:59:34 · 重复失败时扩大可选整数范围

原标说话人 1  00:59:34
Backoff is a probabilistic mechanism. Wi-Fi essentially assumes that a transmitter is failing, failing, failing because too many nodes are trying to access the channel. The situation is too crowded. It assumes that when you fail, fail, fail, other nodes are trying too; you select the same backoff time and keep colliding. To reduce the collision probability, each node needs to enlarge the range of possible integer values from which it can choose.
退避是一种概率性机制。Wi-Fi 实际上是假定，发送方之所以失败、失败、再失败，是因为有太多节点在尝试接入信道，竞争太拥挤。它假定，当你失败、失败、再失败时，其他节点也在尝试发送；你们选择了相同的退避时间，因此不断发生碰撞。为了降低碰撞概率，每个节点都需要扩大可供抽取的整数值范围。

## 51 · 01:00:35 · 扩大窗口的好处与信道差错下的代价

原标说话人 1  01:00:35
It's like a bag of candies. If they are all strawberry flavored, two people picking candies will clearly both pick strawberry. If you fill the bag with banana, strawberry, peach, mint, and so on, the probability that two people pick the same flavor decreases. It's the same principle. You may say: nice, Wi-Fi deals with a crowded situation and lets us perform better. True, doubling the contention window works if the reason for failure is repeated collisions. But remember that in wireless a transmission may also fail because of channel errors. You may be the only node with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate correctly. You still have to follow the protocol rules. If you fail repeatedly because of channel errors, these rules mean that every time you have to enlarge the contention window. Statistically, it becomes more likely that you draw a longer and longer and longer backoff time. Is this good in this case? Not really. You are not failing because you collide with other nodes; the reason is poor channel quality. This mechanism does not solve that issue. In this situation it is even harmful, because it delays channel access. It makes you wait longer and longer and longer before you can access the channel and transmit, even though the problem is poor channel quality, not collision. It just increases channel access delay and does not help with that problem.
这就像一袋糖果。如果全是草莓味的，那么两个人各拿一颗，显然都会拿到草莓味。如果袋子里装着香蕉味、草莓味、桃子味、薄荷味等各种糖果，那么两个人拿到相同口味的概率就会降低。原理是一样的。你可能会说：很好，Wi-Fi 能应对拥挤的情况，让我们的性能更好。没错，如果失败的原因是反复发生碰撞，那么把竞争窗口扩大一倍确实有效。但要记住，在无线通信中，传输也可能因为信道差错而失败。即使只有你这一个节点有数据包要发送，也可能因为信道状况不好、接收方无法正确解调而失败。你仍然必须遵守协议规则。如果你因为信道差错而反复失败，那么按照这些规则，每次你都必须扩大竞争窗口。从统计上说，你抽到越来越长、越来越长、越来越长的退避时间的可能性会增大。这在这种情况下是好事吗？并不是。你失败的原因并不是与其他节点发生了碰撞，而是信道质量差。这种机制解决不了这个问题。在这种情况下，它甚至是有害的，因为它延迟了信道接入。它让你等得越来越久、越来越久、越来越久，才能接入信道并发送，尽管问题出在信道质量差，而不是碰撞。它只是增加了信道接入时延，对这个问题并没有帮助。

[02-WiFi_1-7.pdf 图49：Remarks on Backoff · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcnYA2YIgLfiTLfyHxySIUeed)

课件：02-WiFi_1-7.pdf · PDF第25页上半页 · 图49（按PDF顺序）

## 52 · 01:04:00 · 批判性评估技术方案的适用条件

原标说话人 1  01:04:00
We need to understand why mechanisms are designed in a certain way, but also look at them critically. Is a solution good under all conditions and in every situation? Some aspects of a technology may not always be good, and we need to be aware of that. When designing a technological solution, we need to account for possible issues. An idea may solve one problem but make things worse in other situations. We need to look at the big picture when designing a technology, and this is an example.
我们需要理解各种机制为什么要这样设计，同时也要批判性地看待它们。一种解决方案在所有条件下、所有情形中都好吗？一项技术的某些方面未必总是好的，我们需要意识到这一点。在设计技术方案时，必须考虑可能出现的问题。某个想法也许能解决一个问题，却会让其他情况下的表现变得更糟。设计技术时，我们需要从整体上考虑问题，这就是一个例子。

## 53 · 01:05:29 · 广播和多播不期待确认

原标说话人 1  01:05:29
The last thing I want to comment on before moving to the third situation is that we are considering unicast data packets. Let me mention again that multicast and broadcast data packets are much simpler, because we do not expect acknowledgments.
在进入第三种情况之前，我最后还想说明一点：我们现在讨论的是单播数据包。我再提一下，多播和广播数据包要简单得多，因为我们不期待收到确认。

## 54 · 01:06:05 · 多个接收方同时ACK会碰撞

原标说话人 1  01:06:05
Since broadcast and multicast packets are intended for multiple destinations, we cannot have all the receivers sending acknowledgments back. If all those acknowledgments were sent at the same time, they would collide with one another. So that would be no use.
广播和多播数据包是发给多个目的节点的，因此我们不能让所有接收方都发回确认。如果所有确认同时发出，它们就会相互碰撞。因此，这样做没有用。

## 55 · 01:06:45 · 广播多播一次发送与发送后退避引入

原标说话人 1  01:06:45
If you had to desynchronize the acknowledgment transmissions, that would be very, very complicated and would increase the protocol overhead. So that is not good. So the choice they made was: if a packet is broadcast or multicast, the transmitter of course needs to sense the channel. If it is idle, transmit. If it is busy, you have to perform backoff because you have to wait. But once you access the channel and transmit, that's it; you are done. You don't care whether the packet was received successfully or unsuccessfully. Broadcast and multicast packets are transmitted only once. You may need to run backoff for those data packets, but only if, when you want to access the channel, you sense the channel as busy the first time. Once you perform backoff, access the channel, and transmit, you are done. If everything is clear so far, let me know if you have questions. No questions? Okay, then we can tackle the last condition. We have one more situation in which we perform backoff. In this third situation the procedure is slightly, slightly different. It is essentially the same except for one thing. In this case the procedure is called post-backoff, to underline that there is a small difference from backoff run in the previous two situations.
如果要让这些确认错开时间发送，那会非常、非常复杂，而且会增加协议开销。所以这样不好。因此，协议采取的做法是：如果一个数据包是广播或多播数据包，发送方当然仍然需要侦听信道。如果信道空闲，就发送。如果信道忙，就必须执行退避，因为你需要等待。但一旦接入信道并完成发送，就到此为止，任务完成。你不再关心数据包是否被成功接收。广播和多播数据包只发送一次。你可能需要为这些数据包执行退避，但只有在想要接入信道时，第一次侦听就发现信道忙的情况下才需要。一旦执行退避、接入信道并发送完毕，任务就完成了。如果到这里都清楚了，有问题就告诉我。没有问题吗？好，那我们就来讨论最后一种情况。还有一种情况下需要执行退避。在第三种情况下，过程会略有、略有不同。除了一个地方以外，基本上是一样的。在这种情况下，这个过程叫作发送后退避，用来强调它与前两种情况下执行的退避有一点区别。

[02-WiFi_1-7.pdf 图51：Remark: Broadcast and Multicast Traffic · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcn02sGtGH4i7wCWx46feJRs4)

课件：02-WiFi_1-7.pdf · PDF第26页上半页 · 图51（按PDF顺序）

# 七、发送后退避与公平性

## 56 · 01:09:19 · 成功传输后仍须执行退避

原标说话人 1  01:09:19
What is this third situation? It is when a node transmits a data packet successfully. You may say: why do I have to perform backoff? I transmitted my packet correctly; I'm done. What do you want from me? Well, Wi-Fi says: I know you transmitted your packet and you are done with that, but after receiving the ACK from the receiver, you need to perform backoff using zero to CW_min as the range of possible integers. That's what the protocol says.
第三种情况是什么？就是节点成功发送了一个数据包之后。你可能会说：为什么还要执行退避？我的数据包已经正确发送出去了，事情已经做完了。还要我做什么？那么，Wi-Fi 会说：我知道你已经发送了数据包，这件事已经完成，但收到接收方返回的 ACK 之后，你还需要执行退避，抽取整数的范围是从零到 CW_min。协议就是这样规定的。

## 57 · 01:10:13 · 发送后退避的公平性目标

原标说话人 1  01:10:13
Again, we want to understand why. This is not enough: okay, I have to do it, I will do it, but tell me why. Why do I have to do that? The reason is fairness. We want to be fair to our nodes.
我们还是想弄明白为什么。仅仅说“好吧，既然必须做，那我就做”还不够，还要告诉我为什么。为什么我必须这样做？原因是公平性。我们希望公平地对待各个节点。

## 58 · 01:10:32 · 用A成功发送场景说明发送后退避

原标说话人 1  01:10:32
Let me give an example that will allow us to understand why they tell us to run post-backoff once we transmit successfully. Let's consider the same scenario again: an access point, node A, and our B and C nodes, as before. We already know the story, so it will be easier. It starts in the same way. A has a packet, senses the channel for DIFS, finds it idle, and transmits its unicast data packet to the access point. The transmission is successful, so the access point sends back the ACK.
我来举个例子，帮助大家理解为什么在成功发送之后，协议要求我们执行发送后退避。我们再来看同一个场景：一个接入点、节点 A，以及刚才的节点 B 和 C。这个过程我们已经熟悉了，所以理解起来会更容易。开头是一样的。A 有一个数据包，它侦听信道一个 DIFS 的时间，发现信道空闲，就把自己的单播数据包发送给接入点。传输成功了，因此接入点返回 ACK。

## 59 · 01:11:51 · B和C设NAV并收到待发数据

原标说话人 1  01:11:51
As we said before, all nodes are in radio visibility of each other; they can hear each other. B and C therefore set their NAV. As before, at a certain point they get a packet from their respective higher layers, so they will have to transmit their packets.
正如前面所说，所有节点都在彼此的无线可见范围内，能够相互听到。因此，B 和 C 会设置各自的 NAV。和之前一样，它们在某个时刻从各自的上层收到一个数据包，因此也需要发送这些数据包。

## 60 · 01:12:20 · A成功后退避与B、C常规退避

原标说话人 1  01:12:20
We already know how things work, but now our attention is on A. Let's focus on A. A is the one that performed its transmission successfully, so it is done. According to the protocol, once A has finished transmitting the packet and received the ACK, it needs to perform post-backoff. It has to sense the channel for DIFS and then draw an integer from zero to CW_min. B and C behave as before; we know that already. They have to run a regular backoff procedure.
我们已经知道整个过程是如何进行的，但现在要关注的是 A。我们把注意力放到 A 上。A 已经成功完成了传输，因此它的任务完成了。根据协议，A 发送完数据包并收到 ACK 之后，就需要执行发送后退避。它必须先侦听信道一个 DIFS 的时间，然后从零到 CW_min 之间抽取一个整数。B 和 C 的行为与之前一样，这一点我们已经知道了。它们必须执行常规的退避过程。

## 61 · 01:13:44 · 移除发送后退避的消融实验

原标说话人 1  01:13:44
Again, to understand how useful a mechanism or solution is, let's play our little game of ablation. Let's remove post-backoff and see what happens. What if A does not have to run any post-backoff? Let's add an event here to understand what would happen, considering all possible cases.
同样，为了理解一种机制或解决方案究竟有多大用处，我们再玩一下这个小小的消融游戏。把发送后退避去掉，看看会发生什么。如果 A 不需要执行任何发送后退避，会怎么样？我们在这里加一个事件，考虑所有可能的情况，来理解接下来会发生什么。

## 62 · 01:14:31 · A队列中还有另一个待发包

原标说话人 1  01:14:31
Let's consider that A has another packet in its MAC queue. Remember that we said the MAC layer can be modeled as a queue with a server. A has transmitted the packet here successfully, but let's assume it has another packet in the queue waiting to be transmitted. This first packet goes through successfully; that's what we represented here. But now A has another packet right here.
假设 A 的 MAC 队列中还有另一个数据包。记住，我们说过，可以把 MAC 层建模为一个带有服务台的队列。A 已经在这里成功发送了这个数据包，但假设队列中还有另一个数据包等待发送。第一个数据包成功传送了出去，这就是我们在这里画出来的情况。但现在，A 在这里还有另一个数据包。

## 63 · 01:15:22 · 没有发送后退避时A立即再发

原标说话人 1  01:15:22
When it is done with this dialogue, it has another packet to deal with. What if A didn't have any post-backoff to run? It would sense the channel for DIFS, find it idle, and be able to access it and transmit its other data packet. This may be successful. Would that be fair with respect to B and C?
当它完成这轮交互时，还有另一个数据包需要处理。如果 A 不需要执行任何发送后退避，会怎么样？它会侦听信道一个 DIFS 的时间，发现信道空闲，然后就可以接入信道，发送另一个数据包。这次传输也可能成功。这样对 B 和 C 公平吗？

## 64 · 01:16:10 · 连续占用信道造成不公平

原标说话人 1  01:16:10
Poor B and C are waiting for their backoff time, and A just gets the next packet and goes ahead with its transmission. This is unfair. If a Wi-Fi card like A has several packets to transmit, in this situation without post-backoff it will just continue accessing the channel and transmitting its packets. With very high probability it will seize the channel for a very long time and transmit, transmit, transmit, while the others have to wait, wait, and wait, because the channel will become busy continuously. This was indeed observed experimentally. Years ago, some researchers experimented with different Wi-Fi cards that were commercial products. All these cards claimed to follow the standard; products must follow the standard. They claimed to do that, but one card was applying everything specified by the standard except post-backoff.
可怜的 B 和 C 还在等待退避时间结束，A 却直接拿到下一个数据包，继续发送。这是不公平的。如果像 A 这样的 Wi-Fi 网卡有多个数据包要发送，在没有发送后退避的情况下，它就会不停地接入信道、发送数据包。它很有可能长时间占用信道，发送、发送、再发送，而其他节点只能等、等、再等，因为信道会变得忙碌，而且会持续如此。实验中确实观察到了这种情况。很多年前，一些研究人员用不同的商用 Wi-Fi 网卡做过实验。所有这些网卡都声称遵循标准，产品必须遵循标准。它们虽然这样声称，但其中有一块网卡实现了标准规定的所有内容，唯独没有实现发送后退避。

## 65 · 01:17:42 · 未实施发送后退避的商用网卡实验

原标说话人 1  01:17:42
The researchers observed that this Wi-Fi card obtained very, very high throughput, meaning it could transmit a lot of data, while the other cards were starving: they could not get access to the channel. It was a very unfair service because that commercial Wi-Fi card did not implement post-backoff.
研究人员观察到，这块 Wi-Fi 网卡获得了非常、非常高的吞吐量，也就是能够传输大量数据，而其他网卡则陷入了饥饿状态，根本无法接入信道。这种服务非常不公平，原因就在于那块商用 Wi-Fi 网卡没有实现发送后退避。

## 66 · 01:18:22 · 发送后退避的强制性与开销示例

原标说话人 1  01:18:22
This seems like a detail, or one more thing that a node has to do, but it is extremely important for fairness. In Wi-Fi we want to be fair and give everyone the same probability of channel access. It is a very important feature. Notice that the same would happen without post-backoff even if A had no packet immediately after successfully completing its dialogue. Even if it got a packet a few microseconds later, it would still have an advantage over B and C, who must run backoff. That's why the standard says: no matter what the state of your MAC queue is, once you complete a transmission successfully, you must run post-backoff. It is mandatory; we cannot do otherwise. Help me out here. Do we have the long break now? No, sorry. Our time... [number unclear]. Okay, thanks. We still have about fifteen minutes. Let me know if I get it wrong, please; I need to adjust the schedule. We have essentially gone through all these slides, using the whiteboard for greater clarity, but the essential information is also in the slides. What I would like to show now is another example presented here. Don't get scared by the many figures in these slides. They just highlight something we already know, but here you have a concrete example to emphasize it further. We now know more or less how the basic version of Wi-Fi works. We already said Wi-Fi is so successful because it works quite well for our needs, but it has a big problem in general: overhead. We already commented on that. Now that we know how the channel is used in Wi-Fi, this practical example gives evidence of it.
这看起来像是一个细节，或者只是节点又多了一件要做的事，但它对于公平性极其重要。在 Wi-Fi 中，我们希望做到公平，让每个节点都有相同的信道接入概率。这是一个非常重要的特性。请注意，即使 A 在成功完成这轮交互后没有立即拿到新的数据包，如果没有发送后退避，也会发生同样的情况。即使它在几微秒之后才收到一个数据包，相比于必须执行退避的 B 和 C，它仍然占有优势。因此，标准规定：无论你的 MAC 队列处于什么状态，一旦成功完成一次传输，就必须执行发送后退避。这是强制要求，不能不做。帮我确认一下，现在是长休息时间了吗？不是，抱歉。我们的时间……数字不清。好，谢谢。我们还有大约十五分钟。如果我弄错了，请告诉我，我需要调整一下时间安排。我们基本上已经讲完了这些幻灯片的内容，为了讲得更清楚，主要用了白板，但关键的信息也都在幻灯片上。现在我想给大家看这里的另一个例子。不要被这些幻灯片上众多的图吓到。它们只是突出一些我们已经知道的内容，不过这里给出了一个具体的例子，进一步加以强调。现在，我们大致已经知道 Wi-Fi 基础版本是如何工作的。我们已经说过，Wi-Fi 之所以如此成功，是因为它能够很好地满足我们的需求，但总体上它有一个大问题：开销。对此我们之前已经讨论过。现在我们知道了 Wi-Fi 如何使用信道，这个实际例子就能说明这个问题。

[02-WiFi_1-7.pdf 图50：Post-Backoff · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcnETwbqqjz80GK8xGqUWwMKc)

课件：02-WiFi_1-7.pdf · PDF第25页下半页 · 图50（按PDF顺序）

# 八、协议开销与传输效率

## 67 · 01:21:58 · DIFS、物理前导码与各层首部开销

原标说话人 1  01:21:58
When we need to transmit a data packet, first we sense the channel for DIFS. We can consider DIFS to be fifty microseconds long. That is certainly time we need to wait. If we are lucky, if we are lucky, the channel is idle and we can transmit our packet right away. But the packet has headers. We already said it has a physical-layer preamble used by transmitter and receiver to synchronize, so the receiver can start demodulating what the transmitter sends. At the electronics level, they need this preamble to start the communication. Then there is the physical-layer header, and then the physical—sorry, the MAC-layer header, where, for example, we have the Duration field. All these headers are just control information. They are not the payload. It's not something useful at the MAC layer. It is useful for the protocol, but these are not application-layer bits. They are there, fine, but from the application's perspective they are not useful or interesting.
当我们需要发送一个数据包时，首先要侦听信道一个 DIFS 的时间。我们可以把 DIFS 看作长五十微秒。这显然是必须等待的时间。如果运气好，如果运气好，信道处于空闲状态，我们就可以立即发送数据包。但数据包带有首部。我们已经说过，它有一个物理层前导码，用于发送方和接收方之间的同步，这样接收方就能开始对发送方发来的信号进行解调。在电子电路层面，它们需要这个前导码，才能开始通信。接下来是物理层首部，然后是物理层……抱歉，是 MAC 层首部，比如 Duration 字段就在这里。所有这些首部都只是控制信息，并不是有效载荷。它们不是在 MAC 层有用的东西。它们对协议有用，但这些并不是应用层的比特。它们在这里，没有问题，但从应用的角度看，它们既没有用，也不是应用所关心的内容。

## 68 · 01:23:51 · 基本速率发送前导码和首部

原标说话人 1  01:23:51
We spend time transmitting this physical-layer preamble and header, and they are transmitted at the basic rate. As we already commented, the basic rate is a low speed, so they are transmitted slowly. If, as in this example, the basic rate is one megabit per second, you have to wait; this takes time. Then we have the MAC header.
我们需要花时间发送物理层前导码和首部，而且它们是以基本速率发送的。正如前面所说，基本速率是一种较低的速率，所以它们发送得很慢。如果像这个例子一样，基本速率是一兆比特每秒，那么你就必须等待，这需要时间。然后还有 MAC 首部。

## 69 · 01:24:28 · MAC首部长度随地址需求变化

原标说话人 1  01:24:28
Again, the MAC header consists of uninteresting bits from the application's point of view. Its size in Wi-Fi may vary, depending, for example, on how many addresses you need. If you are in an isolated BSS, like the one in your apartment, the only addresses you need are the transmitter and receiver addresses.
同样，从应用的角度看，MAC 首部也由应用并不关心的比特组成。Wi-Fi 中 MAC 首部的长度可能变化，例如会取决于需要多少个地址。如果处在一个独立的 BSS 中，比如你公寓里的那种，那么只需要发送方地址和接收方地址。

## 70 · 01:25:04 · 扩展服务集中的四地址需求

原标说话人 1  01:25:04
If you are in an extended service set, like on the Tongji campus, with many access points connected through the wired network, you may need four different addresses. The reason is that, in an extended service set, we may have access points connected to each other. We already explained the network architecture.
如果处在一个扩展服务集中，比如同济大学校园里，许多接入点通过有线网络连接在一起，那么可能需要四个不同的地址。原因是，在扩展服务集中，接入点之间可能相互连接。这个网络架构我们已经解释过了。

## 71 · 01:25:52 · 数据包经两个接入点交付

原标说话人 1  01:25:52
You are A, and you want to send a packet to B. You send it to the access point you are connected to. Access point one sends it to access point two, and access point two delivers it to B. This happens in an extended service set.
假设你是 A，想要给 B 发送一个数据包。你先把它发送给自己所连接的接入点。接入点一将它发送给接入点二，再由接入点二交给 B。这就是扩展服务集中发生的过程。

## 72 · 01:26:20 · 源、发送方、接收方与目的地址

原标说话人 1  01:26:20
In this case A is the sender, the transmitter, so it is the original source and also the transmitter of the packet. Access point one is the receiver, but the final destination is B. The packet traveling from A to access point one has A as the transmitter address, which is also the source address. It has access point one's address as the receiver address, and B's address as the destination address. So it needs three addresses in the MAC header. Once the packet is received at access point one, that access point has to send it to access point two so that it eventually can be delivered to the final destination. Here the packet needs four addresses in the header. Why? We need to specify that it originally came from source A. The transmitter now is access point one, the receiver is access point two, and the final destination is B. In extended service sets, when Wi-Fi packets travel from one access point to another, they need four addresses. This is just to say that the MAC header's size may vary; it can be shorter or longer. Anyway, you already have to account for DIFS, the physical preamble, physical header, and MAC header. The payload is the useful, interesting part, so it is not overhead.
在这种情况下，A 是发送方，也就是发射方，因此它既是数据包的最初源节点，也是当前发送数据包的节点。接入点一是接收方，但最终目的节点是 B。数据包从 A 传到接入点一时，A 的地址是发送方地址，同时也是源地址。接入点一的地址是接收方地址，而 B 的地址是目的地址。因此，MAC 首部中需要三个地址。接入点一收到这个数据包之后，必须把它发送给接入点二，这样数据包最终才能交付给最终目的节点。此时，数据包的首部中需要四个地址。为什么？我们需要指明，它最初来自源节点 A。现在的发送方是接入点一，接收方是接入点二，最终目的节点是 B。在扩展服务集中，当 Wi-Fi 数据包从一个接入点传到另一个接入点时，需要四个地址。说这些只是为了说明，MAC 首部的长度可能变化，可以短一些，也可以长一些。总之，到这里你已经需要计入 DIFS、物理层前导码、物理层首部和 MAC 首部。有效载荷才是有用的、我们关心的部分，因此它不属于开销。

## 73 · 01:29:08 · 成功传输后的SIFS与确认开销

原标说话人 1  01:29:08
Then, if the packet is hopefully delivered successfully, in the best case, there is SIFS, another interval you have to wait for. Then comes the acknowledgment, a control packet, so it is not interesting from the application's point of view.
接下来，在最理想的情况下，希望数据包能够成功送达，然后还有 SIFS，又一个必须等待的时间间隔。再之后是确认，它是一个控制包，因此从应用的角度看，也不是应用所关心的内容。

## 74 · 01:29:30 · ACK结构与一次传输的总开销

原标说话人 1  01:29:30
The acknowledgment again is made of a physical preamble, physical header, and MAC header, so there are lots of things to transmit. That is the best case. To transmit the payload, you have to wait for DIFS, transmission of the physical-layer preamble, physical-layer header, and MAC header, then SIFS and then ACK. Lots of time just to transmit the payload.
确认同样由物理层前导码、物理层首部和 MAC 首部组成，因此需要传输的东西很多。这还是最理想的情况。为了传输有效载荷，你必须等待 DIFS，传输物理层前导码、物理层首部和 MAC 首部，然后还有 SIFS，再然后才是 ACK。仅仅为了传输有效载荷，就需要花费大量时间。

## 75 · 01:30:04 · 长载荷效率与失败重传额外开销

原标说话人 1  01:30:04
You had better have a long payload, because otherwise your protocol is very, very inefficient. This is the best case. If transmission fails and you have to perform backoff and retransmit the packet, you must wait for the channel to become idle: DIFS, backoff time, and hope the channel remains idle so that you can keep decreasing the backoff counter until it reaches zero. Then transmit your packet, then SIFS and ACK. Lots of things, right, just to transmit a single payload again.
最好让有效载荷长一些，否则协议的效率就会非常、非常低。这还是最理想的情况。如果传输失败，需要执行退避并重传数据包，那么你必须等待信道空闲，等待 DIFS、退避时间，并且希望信道一直保持空闲，这样才能持续减少退避计数器，直到它减到零。然后发送数据包，再等待 SIFS 和 ACK。要做很多事情，对吧，而目的只是再次传输这一份有效载荷。

## 76 · 01:30:46 · Wi-Fi协议效率总结

[02-WiFi_1-7.pdf 图52：Worked Example: Why 11 Mb/s Never Feels Like 11 Mb/s · 在飞书查看原图](https://lcn6dqn3m0yr.feishu.cn/docx/BSkQdCu5LoOPopxZWPGcbeJhnhf#doxcnQS6J19jan879PbrFimceGh)

课件：02-WiFi_1-7.pdf · PDF第26页下半页 · 图52

原标说话人 1  01:30:46
We realize that Wi-Fi's efficiency is actually pretty low. Unfortunately this holds for all versions of Wi-Fi. We looked at the basic version, but it is a curse for all versions. On average, you can consider this scheme's efficiency to be about fifty to fifty-five percent, which is definitely low. Maximum efficiency would be one hundred percent. So, yeah, hopefully.
由此可见，Wi-Fi 的效率实际上相当低。遗憾的是，所有版本的 Wi-Fi 都存在这个问题。我们看的是基础版本，但它是所有版本的诅咒。平均而言，可以认为这个方案的效率大约是百分之五十到百分之五十五，这确实很低。最高效率应该是百分之百。所以，是的，希望如此。

# 九、扩展IFS预告

## 77 · 01:31:25 · 引出最后一个机制扩展IFS

原标说话人 1  01:31:25
That said, we are missing just one last mechanism in Wi-Fi channel access, and then we are done with the basic version of Wi-Fi, which is the most important one. We just need to introduce it, and we will do that after the break: this last piece of the protocol, related to something we already know about, the famous four interframe spaces, the extended IFS. Remember the extended IFS and the priority ladder: SIFS, PIFS, DIFS, and extended IFS. We said we would first focus on SIFS and DIFS and understand how they are used, then return to the other timing intervals. Now it is time to talk about the longest of these intervals, the extended IFS. To give you an idea, it can be as long as about three hundred microseconds, so it is definitely longer than the others we have considered.
话虽如此，Wi-Fi 的信道接入机制现在只剩最后一个还没介绍，然后我们就讲完 Wi-Fi 的基础版本了，而这也是最重要的版本。我们只需要介绍一下这个机制，我们会在休息之后来讲：协议的最后这一部分，与我们已经了解的内容有关，也就是那四种著名的帧间间隔中的扩展 IFS。还记得扩展 IFS 以及优先级顺序吗：SIFS、PIFS、DIFS 和扩展 IFS。我们说过，先重点介绍 SIFS 和 DIFS，理解它们如何使用，然后再回头讨论其他时间间隔。现在该讲这些间隔中最长的一个，也就是扩展 IFS 了。为了给大家一个概念，它可以长达大约三百微秒，因此明显比前面讨论过的其他间隔更长。

## 78 · 01:33:12 · EIFS近似时长与长课间休息

原标说话人 1  01:33:12
It depends on the version of Wi-Fi we consider, but to keep an approximate figure in mind, you can consider it equal to three hundred microseconds. Just to have an idea. If I'm not wrong, we now stop for twenty-five minutes. Okay.
具体数值取决于我们考虑的是哪个 Wi-Fi 版本，但为了记住一个大致的数字，可以把它看作三百微秒。只是有个概念。如果我没弄错，现在我们休息二十五分钟。好。
