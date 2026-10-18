说明：Git文本检查点不含图片二进制；图像见飞书原文或完整ZIP。

# 双语对照：录音机-20261013-0803

https://lcn6dqn3m0yr.feishu.cn/docx/QX16d9bfUoakAHxlKBCcnf2qnPg

课件审计检查点：69段原正文与导航保留，16张图已逐张核验；2项课堂图来源缺口；未作原音转写认证。

会议主题：录音机-20261013-0803
课程：移动与传感器网络 / Mobile Sensor Networks
上传时间：2026年10月14日（周三） 09:13 （GMT+08）
音频时长：约 01:39:00
整理日期：2026年10月18日
版本：完整忠实双语稿 · 913cf98f5b3c
状态：双语正文已完成（69 对）；已匹配插入16张课件图

[原录音附件块保留，音频二进制未打包]

录音文件：点击打开原始录音并播放

原资源链接：https://lcn6dqn3m0yr.feishu.cn/minutes/obcnl12yu9u7o55896nnv47b

文字来源：原始文字记录

原资源链接：https://lcn6dqn3m0yr.feishu.cn/docx/L8gmdNLPOoXIC3xBERncdyClnUg

课件来源：02-WiFi_1-7.pdf

原资源链接：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf

# 一、Block Ack块确认与协议效率

## 01 · 00:00:02 · 发送结束后请求Block Ack并以SIFS间隔回应

原标说话人 1  00:00:02
He will send a short control packet that essentially says, “I’m done,” okay? And implicitly, he requests acknowledgments from the receiver. So after that, the receiver can send this so-called Block Ack, spaced by SIFS, because we are within the same dialogue.
它会发送一个很短的控制分组，基本上就是在说：“我发完了。”好吧？同时，它也隐含地向接收方请求确认。接着，接收方就可以间隔一个 SIFS，发送这个所谓的块确认，也就是 Block Ack，因为我们仍然处于同一次交互中。

![图75：EDCA Bursting with Block ACK](../slide-images/slide-075.png)

课件：02-WiFi_1-7.pdf · PDF第38页上半页 · 图75（按PDF顺序）

## 02 · 00:00:40 · 块确认位图如何标记各分组接收结果

原标说话人 1  00:00:40
The Block Ack is a control packet that has a bitmap in the MAC header. I guess you know what a bitmap is. It’s a sequence of bits. Each bit represents a possible acknowledgment for one of the packets that have been sent. So, for example, if this bit is set to one, it means that, it means that the first packet was received successfully by the receiver. If the second bit is also set to one, it means that the second packet was also received successfully. And then perhaps, if there were a third packet, if this bit is set to zero, it means that that packet has not been received successfully. Okay?
Block Ack 是一个控制分组，其 MAC 首部里有一个位图。我想你们知道位图是什么，就是一串比特。每个比特都可以表示对一个已发送分组的确认。比如，如果这个比特设为 1，就表示，就表示接收方已经成功收到了第一个分组。如果第二个比特也设为 1，就表示第二个分组也成功收到了。然后，假如还有第三个分组，如果它对应的比特设为 0，就说明这个分组没有成功收到。好吧？

![图76：Block ACK: How it works](../slide-images/slide-076.png)

课件：02-WiFi_1-7.pdf · PDF第38页下半页 · 图76（按PDF顺序）

## 03 · 00:01:54 · Block Ack减少逐包确认开销并提高效率

原标说话人 1  00:01:54
So by sending this bitmap at the end, so this is the Block Ack packet, we avoid spending time sending an acknowledgment for each of the packets that are sent while they are transmitted within the transmission opportunity. And we make the protocol more efficient, right? So this is a significant improvement in the efficiency of the Wi-Fi protocol, and indeed, the use of Block Ack has become mandatory in the more recent versions of Wi-Fi. So now, in the more recent versions of Wi-Fi, we always use the enhanced distributed coordination function, as we said. And within that, Block Ack is an essential feature of our scheme. This is just essentially what, what I said now. There are some small drawbacks in using Block Acks, but they are very, very minor. Do you know what delay jitter is? Okay, then forget about it. It’s very minor; it’s not worth explaining.
所以，通过在最后发送这个位图，也就是这个Block Ack数据包，我们就避免了在传输机会内发送各个数据包时，花时间为每一个已发送的数据包单独发送确认。而且，我们让协议变得更高效，对吧？所以，这是对Wi-Fi协议效率的一项显著改进，而且实际上，在较新的Wi-Fi版本中，使用Block Ack已经成为强制要求。所以现在，在较新的Wi-Fi版本中，正如我们说过的，我们总是使用增强型分布式协调功能。而在其中，Block Ack是我们方案的一个必要功能。这基本上就是我、我刚才说的内容。使用Block Ack有一些小缺点，但它们非常、非常轻微。你们知道时延抖动是什么吗？好，那么就忘掉它吧。它非常轻微，不值得解释。

![图77：EDCA Bursting: Pros and Cons](../slide-images/slide-077.png)

课件：02-WiFi_1-7.pdf · PDF第39页上半页 · 图77（按PDF顺序）

# 二、DCF逐分组公平与吞吐量

## 04 · 00:03:39 · 从一次接入只能发送一个分组说起

原标说话人 1  00:03:39
What instead is important to underline at the end of this scheme is not one additional feature. We are essentially done with the main features of this scheme. But this is an observation, a reflection on this enhanced distributed channel access scheme, which is indeed important. So remember what we said: previously, a transmitter that had the opportunity to transmit had the chance to transmit only one packet, right? And then, if it had more packets, it had to recontend for the channel and try to access the channel again.
不过，在讲完这个机制时，还有一点值得强调，它并不是又一个新功能。这个机制的主要功能，我们基本上已经讲完了。接下来是对增强型分布式信道接入机制的一个观察、一点思考，而且确实很重要。还记得我们说过，以前一个发送方获得发送机会时，只能发送一个分组，对吧？如果它还有更多分组，就必须重新竞争信道，再次设法获得信道接入机会。

## 05 · 00:04:34 · TXOP使逐分组公平转向时间公平

原标说话人 1  00:04:34
So that was per-packet channel access. Now, we already said that thanks to this transmission-opportunity innovation, what a transmitter wins is the possibility to transmit for a certain period of time. So we have a temporal channel-access scheme, a temporal-opportunity channel-access scheme. As a consequence, the fairness of our distributed channel-access scheme changes from so-called per-packet fairness to so-called temporal fairness. Now, you know what fairness means. To be fair, to be fair in English means to give the same possibilities, chances, to everyone, right? As we said, Wi-Fi, in the distributed channel-access scheme, aims to be fair. And indeed, while, for example, looking at DCF, the distributed coordination function, we said that the post-backoff mechanism is there to ensure that we provide fairness, fair treatment to all Wi-Fi cards, right? That was the reason why we have post-backoff in the DCF scheme.
所以，那是按数据包接入信道。现在，我们已经说过，多亏了这项传输机会的创新，发送端赢得的是在某个时间段内发送的机会。所以，我们有一个基于时间的信道接入方案，一个基于时间机会的信道接入方案。结果是，我们的分布式信道接入方案的公平性，从所谓的逐包公平，变成所谓的时间公平。现在，你们知道公平是什么意思。公平，英语中的公平，意思是给每个人相同的可能性、机会，对吧？正如我们说过的，Wi-Fi在分布式信道接入方案中以公平为目标。而且，确实，比如说，在看DCF，也就是分布式协调功能时，我们说过，发送后退避机制是为了确保我们提供公平性、公平地对待所有Wi-Fi网卡，对吧？那就是我们在DCF方案中有发送后退避的原因。

## 06 · 00:06:20 · DCF相同接入规则带来平均分组数公平

原标说话人 1  00:06:20
Okay, so we want to be fair, right? And that’s one of the goals of Wi-Fi. But clearly, since in the previous version, in DCF, each transmitter had a chance to transmit one packet per channel access, the fairness that we were providing was per-packet fairness, meaning that we were fair in giving the different Wi-Fi nodes the possibility to transmit packets. So that was per-packet fairness. So, as you may remember, in DCF every node, every node follows the same rules in order to access the channel. So it has to sense the channel as idle for DIFS. If the channel is busy, it has to perform the backoff procedure, using, the first time, zero to CWmin, then doubling the contention window, et cetera, et cetera, right? All of them follow the same rules. So this means that if we look at the average behavior, when we consider DCF, we have that, on average, on average, the nodes will access the channel the same number of times. And each time they will transmit one packet, right? So they will have the chance to transmit the same number of packets.
好，所以我们希望公平，对吧？这也是 Wi-Fi 的目标之一。不过，在以前的版本里，在 DCF 中，每个发送方每次接入信道都只能发送一个分组。因此，我们提供的是逐分组公平，也就是说，我们公平地给不同的 Wi-Fi 节点提供发送分组的机会。这就是逐分组公平。你们可能还记得，在 DCF 中，每个节点，每个节点在接入信道时都遵循相同的规则。它必须侦听到信道空闲了一个 DIFS。如果信道忙，就必须执行退避过程，第一次从 0 到 CWmin 的范围中取值，随后把竞争窗口加倍，等等、等等，对吧？所有节点遵循相同的规则。所以，如果看平均行为，在 DCF 中，平均而言，平均而言，各节点接入信道的次数相同。每次接入时，它们都发送一个分组，对吧？因此，它们获得发送相同数量分组的机会。

## 07 · 00:08:32 · 两个站点始终有包可发的饱和场景

原标说话人 1  00:08:32
So if we make some simplifying assumptions, let’s consider that we have the access point here, and then two stations, A and B, connected to the access point. And let’s consider that both A and B have a MAC queue that is full of packets. Okay, assume that there are always packets coming in. So they always have traffic to transmit, packets to transmit, okay? This kind of assumption is called saturated Wi-Fi stations, meaning that their queues are indeed saturated. They have, they are always full. Okay?
我们先作一些简化假设。假设这里有一个接入点，还有连接到它的两个站点 A 和 B。再假设 A 和 B 的 MAC 队列里都装满了分组。也就是说，假设一直有分组到来，因此它们始终有业务要发送，始终有分组要发送，好吧？这种假设称为 Wi-Fi 站点处于饱和状态，也就是说，它们的队列确实是饱和的。队列里有分组，始终是满的。好吧？

## 08 · 00:09:45 · 长期观察下的相同发送次数与吞吐量定义

原标说话人 1  00:09:45
That’s the meaning. So if we assume this kind of scenario, where of course A and B can hear each other, a very simple network scenario, and we consider using DCF, then this is, on average, on average, the kind of traffic pattern that we will observe on the channel. That means we look at the channel, and on average, statistically, what we will see is that A and B get the same chances to access the channel and transmit a packet, because, as we said, DCF is fair. So, on average, if you observe the system for quite a long time, on average you would see that our two nodes, A and B, will be able to transmit exactly the same number of packets during this time period. And we denote this number of packets by n. Okay, so let’s denote this number of packets transmitted by each node with n. Now, what is the throughput, so the ability of A and B to transmit traffic in bits per second? Remember that throughput is an average performance metric. We have already introduced this metric. It is the number of useful bits, bits of interest to the application, from the point of view of the application, interesting bits, that a node is able to transmit over a period of time T. Okay, considering that this T is quite long, we need to observe the system for quite some time.
就是这个意思。假设是这样一个场景，当然，A 和 B 能够听到彼此，这是一个非常简单的网络场景。再假设我们使用 DCF，那么，平均而言，平均而言，信道上会出现这样的业务发送模式。也就是说，如果观察信道，平均而言，从统计上看，我们会看到 A 和 B 获得相同的机会来接入信道、发送一个分组，因为，正如我们说过，DCF 是公平的。因此，平均而言，如果观察系统足够长的时间，平均而言，就会看到 A 和 B 这两个节点在这段时间里能够发送完全相同数量的分组。我们把这个分组数记为 n。好，就把每个节点发送的分组数记为 n。那么，吞吐量是多少？也就是 A 和 B 以比特每秒计的业务发送能力是多少？记住，吞吐量是一个平均性能指标。我们已经介绍过这个指标。它关注的是一个节点在一段时间 T 内能够发送的有效比特数，也就是应用关心的比特，从应用的角度看有意义的比特。当然，这个 T 应当足够长，我们需要观察系统相当长一段时间。

## 09 · 00:12:32 · 节点A吞吐量计算中的分组数和载荷长度

原标说话人 1  00:12:32
So what is the throughput? So Th means throughput. What is the throughput of A, of node A? Well, we need to consider the number of packets that A is able to transmit over the time period T. And then we need to consider the size, the length. So L stands for the length of the payload, right, sent by A when it transmits a packet.
那么，吞吐量是多少？这里用 Th 表示吞吐量。节点 A 的吞吐量是多少？我们需要考虑 A 在时间段 T 内能够发送多少个分组，还需要考虑分组的大小、长度。所以，L 表示 A 发送一个分组时，其中有效载荷的长度，对吧？

## 10 · 00:13:11 · 用n、L_A与T计算吞吐量并引入节点B

原标说话人 1  00:13:11
So let’s assume that all the packets that A has in its queue have length L_A, okay? So they are of the same size, all of them. So the throughput can be computed as the number of packets that are transmitted over T, considering that each packet includes L_A useful bits, right? Very simple. Okay, what about B? Similarly, B will be able to transmit n packets over the time period T, and let’s consider that each packet has a size, a length, equal to L_B.
假设 A 队列里的所有分组长度都是 L_A，好吧？也就是说，这些分组大小相同，全部都一样。所以，计算吞吐量时，要考虑在 T 内发送的分组数，并且每个分组都包含L_A 个有效比特，对吧？很简单。那么，B 呢？同样，B 在时间段 T 内能够发送 n 个分组，我们假设每个分组的大小、长度都等于 L_B。

## 11 · 00:14:17 · 节点B的分组长度与吞吐量表达式

原标说话人 1  00:14:17
Okay, so all these packets here in B’s queue have length L_B. So what is the throughput of B, then? Again, it’s the number of packets that it will be able to transmit over the time period, and each packet will include, right, L_B useful bits. So this is the expression for the throughput of B.
好，所以 B 队列里的所有这些分组，长度都是 L_B。那么，B 的吞吐量是多少？还是看它在这段时间里能够发送多少个分组，而每个分组里都包含，对吧，L_B 个有效比特。这就是 B 的吞吐量表达式。

## 12 · 00:14:50 · 相同接入机会是否意味着相同吞吐量

原标说话人 1  00:14:50
So now remember, our DCF, because we are considering DCF here, wants to be fair to our Wi-Fi cards. So, fine, it provides the same chances to everyone to access the channel. But our question here is: what about the throughput performance? The fact that DCF gives all nodes the same possibility to access the channel, does this mean that the nodes, the Wi-Fi cards, will achieve the same throughput? Because this is what matters in the end. Okay, the amount of useful bits that you are able to transmit on average, so that’s what matters. It’s okay to be fair in terms of channel access, but in the end I would like to be fair in terms of throughput.
现在记住，我们这里讨论的是 DCF，而 DCF 希望公平地对待 Wi-Fi 网卡。好，它给每个节点相同的信道接入机会。但我们的问题是：吞吐量性能怎么样？DCF 给所有节点相同的信道接入机会，这是否意味着这些节点、这些 Wi-Fi 网卡就会获得相同的吞吐量？因为，最终重要的是这个，也就是平均能够发送多少有效比特，这才是重要的。信道接入公平当然可以，但最终，我希望吞吐量也公平。

## 13 · 00:16:05 · DCF在载荷长度相同时实现吞吐量公平

原标说话人 1  00:16:05
So our question is: when are these two expressions the same, equal, okay? When can A and B enjoy the same throughput? So if we look at these expressions, it is easy to see that they are equal when L_A is equal to L_B, right? So what we can say is that the per-packet fairness provided by DCF will also lead to throughput fairness when our nodes, our Wi-Fi cards, transmit packets of the same size, with the same number of bits in their payloads. Then per-packet fairness also means throughput fairness at the MAC layer. Okay, that was essentially what we had in DCF.
所以，我们的问题是：这两个表达式什么时候相同、相等？A 和 B 什么时候可以获得相同的吞吐量？看这两个表达式，很容易发现，当L_A 等于 L_B 时，它们就相等，对吧？因此，我们可以说，当各节点、各 Wi-Fi 网卡发送大小相同的分组，也就是有效载荷中比特数相同时，DCF 提供的逐分组公平也会带来吞吐量公平。这时，逐分组公平也就意味着 MAC 层的吞吐量公平。这基本上就是 DCF 的情况。

# 三、EDCA时间公平与吞吐量

## 14 · 00:17:27 · 同优先级队列之间的时间公平

原标说话人 1  00:17:27
Now we have a different, slightly enhanced, different scheme, right, where we have the transmission-opportunity concept. So as we already said, our scheme will provide what is called temporal fairness, considering two queues of the same priority in two different nodes.
现在，我们有一个不同的、稍微增强的、不同的方案，对吧，其中有传输机会的概念。所以，正如我们已经说过的，考虑两个不同节点中优先级相同的两个队列，我们的方案会提供所谓的时间公平。

## 15 · 00:18:00 · EDCA同接入类别获得相同TXOP时长

原标说话人 1  00:18:00
Okay, so now let’s consider our enhanced distributed channel-access scheme, and let’s consider the same scenario as before. But let’s now consider, for example, that this is access category zero for both these Wi-Fi cards, okay? We need to look at the same queues, types of queues. So access category zero in A and access category zero in B. And what do we have here? Well, again, the scheme is distributed. All Wi-Fi cards will follow the same rules, so we are still fair. But as we said, when they access the channel, and they will access the channel with the same probability, because we are still fair, what they will be able to do is transmit for a transmission-opportunity-limit time interval corresponding to access category zero.
好，现在考虑增强型分布式信道接入机制，场景仍然和刚才一样。不过，我们现在假设这两块 Wi-Fi 网卡上比较的都是零号接入类别。我们必须比较相同的队列、相同类型的队列，也就是 A 的零号接入类别和 B 的零号接入类别。那么，这里会出现什么情况？同样，这是一个分布式机制，所有 Wi-Fi 网卡都遵循相同的规则，因此仍然是公平的。不过，正如我们说过，当它们接入信道时，由于我们仍然保持公平，它们接入信道的概率相同，它们获得的是在零号接入类别所对应的传输机会限额这段时间内进行发送的机会。

## 16 · 00:19:30 · 零优先级队列赢得的发送时间限额

原标说话人 1  00:19:30
Okay? So what they will win is the possibility to transmit for the transmission opportunity limit. We are considering the queues of priority zero, so they will be able to transmit for this amount of time.
好吧？所以，它们赢得的是在传输机会限额规定的时间内发送的机会。这里考虑的是零优先级队列，因此它们能够在这么长的时间内进行发送。

## 17 · 00:19:53 · 重新计算EDCA下的节点吞吐量

原标说话人 1  00:19:53
Okay. Now we want to compute again the throughput that they will enjoy, because, again, it’s fine to have the same probability of accessing the channel, but what matters is the throughput.
好。现在，我们再次计算它们能获得的吞吐量，因为，还是那句话，相同的信道接入概率固然很好，但重要的是吞吐量。

## 18 · 00:20:15 · 用TXOP时间线比较EDCA与DCF

原标说话人 1  00:20:15
So again, we look at the system, our system, for an extended period of time T. And we can consider that this is essentially the pattern we will have, where we simplify things a little bit and represent the duration of the transmission opportunity that each node will gain. Okay? So, for example, they access the channel, again as before, the same number of times. But now every time they access the channel, they will transmit for exactly the same duration. Of course, I said we simplify things a little here because we are not looking at the individual packets, right, transmitted within a transmission opportunity limit. We know that to fill the transmission opportunity with packets, we have packet, SIFS, packet, SIFS, packet, SIFS, and then Block Ack. Okay? We simplify that; we just represent the whole transmission opportunity with a rectangle. Okay, it’s a simplified view. Okay, so this is what we can see now. Hmm. And I think it’s easy to see immediately, visually, by comparing these two temporal lines, timelines here, the difference. Here, in DCF, A and B could transmit packets of different sizes, right? L_A and L_B.
所以，我们再次观察这个系统、我们的系统，观察一段较长的时间 T。基本上，会出现这样的模式。这里稍微作了一点简化，图中画出的是每个节点获得的传输机会的持续时间。好吧？比如，它们仍然像以前一样，接入信道的次数相同。不过，现在每次接入信道时，它们发送的时间都完全相同。当然，我说过，这里作了一点简化，因为我们没有逐个查看一次传输机会限额内发送的各个分组，对吧？我们知道，用分组填满一次传输机会时，发送顺序是分组、SIFS、分组、SIFS、分组、SIFS，然后是 Block Ack。好吧？我们把它简化了，只用一个矩形表示整个传输机会。这是一种简化的画法。好，这就是我们现在看到的情况。嗯。我想，直接比较这两条时间线，就很容易看出区别。在这里，在 DCF 中，A 和 B 可以发送大小不同的分组，对吧？长度分别是 L_A 和 L_B。

![图79：Temporal Fairness vs. Per-Packet Fairness（双时间线与公式）](../slide-images/slide-079.png)

课件：02-WiFi_1-7.pdf · PDF第40页上半页 · 图79（按PDF顺序）

## 19 · 00:22:28 · EDCA吞吐量计算中的接入次数与TXOP

原标说话人 1  00:22:28
In this second case, it doesn’t really matter what size packets they transmit, right? Because what matters is actually the speed at which they transmit, because the time allocated to each of them is the same. And indeed, if we now compute the throughput that A can achieve, we need to consider the number of times that A will be able to access the channel. This is still n. Now we have to multiply this n by the transmission opportunity, because what a node wins when accessing the channel is not a packet transmission; it is a transmission opportunity.
在第二种情况中，它们发送的分组有多大并不重要，对吧？因为真正重要的是发送速度，每个节点获得的时间是相同的。如果现在计算 A 能够达到的吞吐量，就要考虑 A 接入信道的次数，这里仍然是 n。现在需要把 n 乘上传输机会的时长，因为节点接入信道时赢得的不是发送一个分组的机会，而是一次传输机会。

## 20 · 00:23:31 · 节点A的数据速率决定每次TXOP发送比特数

原标说话人 1  00:23:31
And then, in order to compute the number of bits transmitted during a transmission opportunity, we need to consider the data rate used by A, the speed at which A transmits. That is denoted by R_A, okay? So R_A is the speed at which A transmits over the radio channel. And that, of course, is divided by T, our observation time, in order to compute the throughput.
然后，要计算一次传输机会中发送了多少比特，就必须考虑 A 使用的数据速率，也就是 A 的发送速度。我们用 R_A 表示它，好吧？所以，R_A 就是 A 在无线信道上的发送速度。当然，还要除以观察时间 T，才能得到吞吐量。

## 21 · 00:24:27 · 节点B的TXOP、数据速率与吞吐量计算

原标说话人 1  00:24:27
For B, similarly, the numerator contains the number of times that B can access the channel. Every time it can transmit for a duration equal to the transmission opportunity. And how many bits fit there? Well, it clearly depends on how fast, right, on the speed at which B transmits during the transmission opportunity. So this is the speed, the bits-per-second speed at which B transmits. And clearly, this time interval, the transmission opportunity, multiplied by R_B gives you the number of bits that B is able to transmit during the transmission opportunity. It gets n transmission opportunities over a period T. So the numerator indeed represents the number of bits that B is able to transmit over T. So the throughput can be simply written in this way.
对于 B，同样，分子中包含 B 能够接入信道的次数。每次接入时，它都可以发送一段与传输机会时长相等的时间。那么，这段时间里能够放入多少比特？显然，这取决于它有多快，对吧？也就是 B 在传输机会期间的发送速度。这里就是 B 的速度，以比特每秒为单位。显然，传输机会这段时间乘以 R_B，就得到了 B 在一次传输机会中能够发送的比特数。在时间 T 内，它获得 n 次传输机会。因此，分子确实表示 B 在 T 内能够发送的比特总数。吞吐量就可以这样写出来。

## 22 · 00:25:42 · 时间公平下吞吐量取决于节点发送速率

原标说话人 1  00:25:42
So again, the question is the same as before: when will A and B achieve the same throughput at the MAC layer? Well, the two expressions are now equal when the speed at which A transmits is the same as the speed at which B transmits, right? So this means that they will enjoy the same throughput if they are equally fast at transmitting. So the throughput that you enjoy at the MAC layer depends on how fast you can transmit. If you are very close to the access point, and, as we know, your transmission speed can be very high because you are a lucky user with a very good channel, then you also enjoy very high throughput. But if you are an unlucky user, far away, or there are obstacles between you and the access point, the channel is bad, then you will be a slow transmitter, and in this case your throughput will be much lower. Okay? So our conclusion is that Wi-Fi, newer versions of Wi-Fi, provide temporal fairness because everyone, let’s say, given that the priority of their queues is the same, gets the possibility to transmit for the same amount of time. That’s temporal fairness. However, the actual number of bits that you will be able to transmit at the MAC layer depends on how fast you can be. Hmm. So that’s why at the very beginning we said the newest version of Wi-Fi allows you to transmit at a physical-layer data speed of 46 gigabits per second. Okay, that’s the data speed at the physical layer, which is very, very high. Excuse me, but not all users are able to transmit at that speed.
所以，问题仍然和刚才一样：A 和 B 什么时候能够在 MAC 层获得相同的吞吐量？现在，当 A 的发送速度与 B 的发送速度相同时，这两个表达式就相等，对吧？也就是说，如果它们发送得一样快，就能获得相同的吞吐量。因此，你在 MAC 层获得的吞吐量取决于你的发送速度。如果你离接入点很近，正如我们所知，你的发送速度可以很高，因为你是一个很幸运的用户，信道非常好，那么你也会获得很高的吞吐量。但如果你不太幸运，距离很远，或者你和接入点之间有障碍物，信道很差，那么你的发送就会很慢，这时吞吐量也会低得多。好吧？所以，我们的结论是，Wi-Fi，较新的 Wi-Fi 版本，提供时间公平，因为大家，假设各自队列的优先级相同，都获得相同的发送时长。这就是时间公平。然而，你在 MAC 层实际能够发送多少比特，取决于你的速度有多快。嗯。所以，我们一开始才说，最新版本的 Wi-Fi 在物理层可以达到每秒 46 吉比特的数据速率。好，这是物理层的数据速率，非常、非常高。不过，并不是所有用户都能够以这个速度发送。

![图78：Temporal Fairness vs. Per-Packet Fairness（文字公式）](../slide-images/slide-078.png)

课件：02-WiFi_1-7.pdf · PDF第39页下半页 · 图78（按PDF顺序）

# 四、HCCA轮询、TXOP与服务质量

## 23 · 00:28:37 · 结束EDCA并转向增强集中式接入机制

原标说话人 1  00:28:37
So your throughput in that case will be high, but only if you are a lucky user, okay? So that accounts for the actual performance that we have. Okay, that said, we are done with enhanced distributed channel access, and now we move to the new centralized access scheme that we have in Wi-Fi 4. So, as you may remember, we said that in this Wi-Fi 4 we do not have PCF anymore, because it didn’t work, right? So they introduced a new version, an enhanced new version of the centralized scheme. And this centralized scheme now works, so that’s the good news.
因此，在这种情况下，你的吞吐量会很高，不过前提是你是一个幸运的用户，好吧？这就是我们实际性能的情况。好，增强型分布式信道接入就讲完了，现在转到 Wi-Fi 4 中新的集中式接入机制。你们可能还记得，我们说过，在这个 Wi-Fi 4 中不再使用 PCF，因为它效果不好，对吧？于是，他们引入了一个新版本，一个经过增强的集中式机制。这个集中式机制现在能起作用了，这是个好消息。

## 24 · 00:29:44 · 信标启动超帧与集中式无竞争期

原标说话人 1  00:29:44
How does it work? Well, let me stress the important things here through a graphical representation of our, of our protocol. So again, let’s consider a superframe. We already know what a superframe is. The superframe, remember, starts with a beacon. And then we have two different phases. The first phase is the contention-free period, during which we use the centralized access scheme.
它怎样工作呢？嗯，让我通过我们、我们协议的一个图示，强调这里的重要内容。所以，同样，让我们考虑一个超帧。我们已经知道超帧是什么。记住，超帧从一个信标开始。然后，我们有两个不同阶段。第一个阶段是无竞争期，在这期间，我们使用集中式接入方案。

![图82：The 802.11e Superframe](../slide-images/slide-082.png)

课件：02-WiFi_1-7.pdf · PDF第41页下半页 · 图82（按PDF顺序）

## 25 · 00:30:28 · HCCA依据队列状态动态轮询站点

原标说话人 1  00:30:28
And the second phase is the contention period, during which we use the distributed channel-access scheme. Okay, this is exactly the same as what we discussed already. Okay, so let’s first focus on the contention-free period, the contention-free period where we use this new centralized access scheme called HCCA. Now, if you observe this representation, you can see that it is essentially more or less the same as PCF, right? Because we still have a polling, polling scheme, where the access point polls the stations, and every time a station is polled, it gets the right, it is entitled to access the channel, right? So from that point of view, it is very similar to PCF. But what are the differences? Well, first of all, the way the access point polls the station is different, because we no longer have a static polling list. Instead, the access point now has an idea of the status of the queues of the different Wi-Fi cards, and therefore it can poll a station only if it knows that that station has data to transmit. Why? Well, remember what we said yesterday about the MAC header, right? We said, “Oh, there is a new subfield there, the QoS Control subfield.”
第二个阶段是竞争期，在这段时间里使用分布式信道接入机制。好，这和我们前面讨论过的完全一样。先看无竞争期，也就是使用这个新的集中式接入机制 HCCA 的阶段。观察这张图，可以发现它基本上与 PCF 差不多，对吧？因为它仍然是一种轮询、轮询机制，由接入点轮询各站点。每当一个站点被轮询到，它就获得权利，被允许接入信道。从这个角度看，它与 PCF 非常相似。那么，区别是什么呢？首先，接入点轮询站点的方式不同，因为现在不再使用一个静态轮询列表。接入点知道各 Wi-Fi 网卡队列的大致状态，因此只有在知道某个站点有数据需要发送时，才会轮询它。为什么？还记得昨天讲 MAC 首部时说过什么吗？我们说：“哦，这里新增了一个子字段，叫作 QoS Control 子字段。”

![图80：HCCA: Crucial Features](../slide-images/slide-080.png)

课件：02-WiFi_1-7.pdf · PDF第40页下半页 · 图80（按PDF顺序）

## 26 · 00:33:13 · QoS控制字段报告队列状态并减少无效轮询

原标说话人 1  00:33:13
And we said, well, this can be used to signal the type of traffic that we are transmitting, but it is also used to include information on the state of the queue of a Wi-Fi card. So through this subfield in the packet header, Wi-Fi cards can notify the access point about their queue status. So this means that the access point now has a real-time view of the queues at each station, whether they have traffic to transmit or not, right, and how much traffic they have. So now we solve one of the, one of the PCF issues. That was the overhead we had due to possible poll, null, poll exchanges [exchange wording uncertain] that were totally useless and harmful, right? They introduced lots of overhead, and we said that was one major issue in PCF.
而且，我们说过，嗯，这可以用来指示我们正在传输的流量类型，但它也用来包含Wi-Fi网卡队列状态的信息。所以，通过数据包首部中的这个子字段，Wi-Fi网卡能够通知接入点自己的队列状态。所以，这意味着，接入点现在能实时查看每一个站点的队列，它们是否有流量要发送，对吧，以及有多少流量。所以，现在我们解决了PCF的一个、一个问题。那就是由于可能出现的轮询、空包、轮询交换［交换措辞不确定］而产生的开销，这些交换完全无用，而且有害，对吧？它们引入了大量开销，而我们说过，这是PCF的一个主要问题。

![图84：Polling and Scheduling in HCCA](../slide-images/slide-084.png)

课件：02-WiFi_1-7.pdf · PDF第42页下半页 · 图84（按PDF顺序）

## 27 · 00:34:59 · 仅轮询有待发流量的站点

原标说话人 1  00:34:59
Now we do not have that anymore; we solve that issue. Because the access point has knowledge, an idea, of the status of the queues of the different Wi-Fi cards, it will poll a station only if that station has traffic to transmit.
现在就不再有这个问题了，我们解决了它。因为接入点知道各 Wi-Fi 网卡队列的大致状态，所以只有当某个站点有业务需要发送时，才会轮询它。

## 28 · 00:35:25 · 以TXOP授权解决PCF发送时长不可控问题

原标说话人 1  00:35:25
Okay, so one problem solved. There is also another, another problem that is solved here. That is, remember in PCF, every time the access point was polling a station, we didn’t know how long that transmission would go on, because it depended on the transmission speed of that station and on the payload size of the packet that that station had. So we didn’t have any control over the time taken by a Wi-Fi station to transmit its packet, right? Now this issue is also solved. Why? Because every time we poll a station, what we grant is not the possibility to transmit a packet. It is the possibility to transmit for a transmission opportunity.
好，一个问题解决了。这里还解决了另一个、另一个问题。记得在 PCF 中，每当接入点轮询一个站点时，我们不知道这次发送会持续多久，因为这取决于该站点的发送速度，也取决于它那个分组的有效载荷大小。因此，我们无法控制一个 Wi-Fi 站点发送一个分组所需的时间，对吧？现在这个问题也解决了。为什么？因为每次轮询一个站点时，我们授予的不是发送一个分组的机会，而是在一个传输机会时段内进行发送的机会。

## 29 · 00:36:52 · 接入点通过TXOP上限规划发送与接入时延

原标说话人 1  00:36:52
So the access point can poll the station and tell that station, “Look, you are entitled to transmit now, but for this transmission opportunity limit, no more than that.” Okay, so the second issue that we had in PCF is solved, because now we have control over how long each polled station will transmit. So the access point can plan ahead very well who is going to transmit and for how long. So now the access point can have full control of these transmissions. Okay, so we have full control of the channel-access delay of the Wi-Fi nodes during the contention period [possibly “contention-free period”; phase name uncertain]. So this scheme works very well: full control. That is what we wanted to provide quality of service. Is this clear?
接入点可以轮询某个站点，并告诉它：“你现在可以发送了，但只能发送这个传输机会限额所规定的时间，不能再多。”好，PCF 的第二个问题也解决了，因为现在我们可以控制每个被轮询站点发送多长时间。接入点能够很好地提前规划谁来发送、发送多久，因此可以完全控制这些发送。也就是说，我们可以完全控制 Wi-Fi 节点在竞争期中的信道接入时延；这里也可能说的是无竞争期，阶段名称不确定。所以，这个机制效果很好，可以完全控制，而这正是我们为了提供服务质量所希望做到的。明白了吗？

## 30 · 00:38:20 · 竞争期发送仍可能推迟下一个信标

原标说话人 1  00:38:20
Okay, now you may remember that there was a third issue with PCF, which was the fact that the beacon could get delayed. Because in the second phase we have a contention period, we use contention-based distributed channel access, and if a station gets the channel at the end, it will be entitled to transmit, and this may go beyond the target ending time of the superframe. Okay, so it may delay the beacon. Now, unfortunately, we still have that. Why? Because this phase is based on contention. We apply the enhanced distributed channel-access scheme here. If a queue gets access to the channel, it can transmit for its transmission opportunity limit. Okay, so nobody can interrupt that. So also in this case, the beacon of the subsequent superframe may be delayed. That issue is still there.
好，你们可能还记得，PCF 还有第三个问题，就是信标可能被延迟。因为第二阶段是竞争期，使用基于竞争的分布式信道接入。如果一个站点在这个阶段快结束时获得信道，它就有权进行发送，而发送可能越过超帧原定的结束时刻，从而造成信标延迟。很遗憾，这个问题仍然存在。为什么？因为这个阶段仍然基于竞争，使用的是增强型分布式信道接入机制。如果一个队列获得信道接入机会，它就可以发送到传输机会限额结束，没有人能打断它。因此，在这种情况下，下一个超帧的信标仍然可能被延迟。这个问题依然存在。

## 31 · 00:39:55 · 接入点等待PIFS后可在竞争期发起轮询

原标说话人 1  00:39:55
But, in this new version, there is actually a change to the contention-period phase. It is still true that during this phase we are using distributed channel access. However, we give the access point the possibility to seize the channel and poll stations if needed. So even if we are in a contention-period phase, the access point may want to poll stations during this phase as well. And it can do that: it just needs to sense the channel as idle for PIFS. Remember PIFS, which was also used to transmit the beacon. So it is enough for the access point to sense the channel as idle for PIFS. If the channel is idle, it can actually also send a poll. And after the poll, after SIFS [interval name uncertain], the polled station can access the channel and transmit. So this allows, allows the access point essentially to recover the channel for urgent traffic transmissions if needed.
但是，在这个新版本中，竞争期阶段实际上有所改变。在这个阶段，我们仍然使用分布式信道接入，这一点仍然成立。不过，我们给接入点提供了在必要时占据信道并轮询站点的可能。所以，即使我们处于竞争期阶段，接入点也可能想在这个阶段轮询站点。而且，它可以这样做：它只需要侦听到信道空闲一个PIFS。记住PIFS，发送信标时也用到它。所以，接入点只要侦听到信道空闲一个PIFS就够了。如果信道空闲，它实际上也可以发送一次轮询。而在轮询之后，在SIFS之后［间隔名称不确定］，被轮询的站点能够接入信道并发送。因此，这允许、允许接入点在必要时，基本上为紧急流量传输重新取得信道。

![图81：HC and QSTA Behavior in HCCA](../slide-images/slide-081.png)

课件：02-WiFi_1-7.pdf · PDF第41页上半页 · 图81（按PDF顺序）

![图85：Did HCCA Actually Fix PCF's Problems?](../slide-images/slide-085.png)

课件：02-WiFi_1-7.pdf · PDF第43页上半页 · 图85（按PDF顺序）

## 32 · 00:41:45 · 竞争期轮询支持紧急流量与课间安排

原标说话人 1  00:41:45
So if there are stations that really need to transmit, or the access point really needs to transmit traffic towards some stations as soon as possible, we give the access point this advantage by allowing it to use polls even during the contention-period phase. So all these things together make this new version of Wi-Fi really, really good at supporting quality of service. Okay. There is only one, one thing left, but we’ll of course discuss that in five minutes. So let’s take a five-minute break.
所以，如果有站点确实需要发送，或者接入点确实需要尽快向某些站点发送流量，我们就通过允许接入点即使在竞争期阶段也使用轮询，给它这个优势。所以，所有这些东西合在一起，使得这个新版本的Wi-Fi在支持服务质量方面真的、真的很好。好。只剩一件、一件事，但是我们当然会在五分钟后讨论。所以，我们休息五分钟。

## 33 · 00:43:35 · 休息后继续讲解与提问安排

原标说话人 1  00:43:35
Okay, we’ll go through that again, no worries. After the break, yes, you can ask the question after the break, okay?
好，我们会再讲一遍，别担心。休息之后，对，你可以在休息之后再提这个问题，好吗？

# 五、公平性与吞吐量计算的复习答疑

## 34 · 00:49:23 · 统一吞吐量公式中的字母记号

原标说话人 1  00:49:23
Perfect. So let me go back to this slide for clarity. Let me just change the alphabet here, or, for clarity, let me do this a little better in terms of the alphabet. Otherwise it might be confusing, using lowercase and uppercase versions of the letters. So let me use exactly the same way for the quantities that relate to the users. [The precise letter changes and some wording are unclear.] So, yeah, yeah, yeah. Okay. So let me just write [symbol unclear], and also here, and here. So it’s a little clearer. I’m not changing the formulas [word uncertain], just presenting them differently.
好。所以，让我回到这张幻灯片，让它更清楚一点。我来调整一下这里使用的字母，或者说，为了说清楚，我把字母的用法再调整一下。否则，一会儿用小写、一会儿用大写，可能会让人困惑。因此，与用户相关的量，我就用完全相同的方式来表示。这里具体改了哪些字母，以及部分措辞，都不清楚。对，对，对。好。所以，我在这里写上这个符号，符号不清楚，这里也一样，还有这里。这样就更清楚一点。我没有改变公式，这个词不确定，只是换一种呈现方式。

## 35 · 00:51:51 · 复习DCF接入次数与不同分组长度的吞吐量

原标说话人 1  00:51:51
Hopefully it’s a bit more, more clear. Okay, so this, this was what we had, right, in DCF. This means “multiplied by,” okay? This symbol means “multiplied by.” So as we said, in DCF our two stations A and B, I mean, this example refers to that scenario, okay, where nodes A and B always have packets to transmit. Their queues are saturated. They get the same chances to access the channel, right, because the protocol is fair. So we denote by n, n is the number of times that a node gets a chance to access the channel. And since they get the same chance to access the channel over a period T, each of them will access the channel n times. Exactly, okay, so n times. And through this representation, this graphical representation, we represented graphically what happens on average, what we expect to see on average. That is, A transmits, then B transmits, then A transmits, then B transmits, and so on and so forth, because they both access the channel n times during this observation time T. And what we have represented here is also the fact that, since we are using DCF, okay, each node, each station may transmit a packet, one packet each time, but the packets may be of different sizes, right? So in this example, we may indeed have that the length of the packets transmitted by A, denoted by L_A, is shorter than the length of the packets transmitted by B, denoted by L_B. Okay, so, for example, if this is true, if, if in this case L_A is less than L_B, then based on our computation, what we will see is that the throughput of A will be less than the throughput of B, right? Hmm.
希望现在更清楚一点，更清楚一点。好，这就是我们在 DCF 中的情况，对吧？这里表示“乘以”，好吧？这个符号表示“乘以”。所以，正如我们说过，在 DCF 中，我们有两个站点 A 和 B，我是说，这个例子指的就是那个场景：A 和 B 始终有分组需要发送，它们的队列是饱和的。它们获得相同的信道接入机会，对吧？因为这个协议是公平的。我们用 n 表示，n 就是一个节点获得信道接入机会的次数。由于在一段时间 T 内，它们获得相同的接入机会，因此每个站点都会接入信道 n 次。对，好，就是 n 次。通过这张图，这个图形表示，我们画出了平均情况下会发生什么，也就是平均而言我们预期会看到什么：A 发送，然后 B 发送，再是 A 发送，再是 B 发送，如此反复。因为在观察时间 T 内，它们都接入信道 n 次。图中还表示了另一点，就是由于我们使用的是 DCF，每个节点、每个站点每次可以发送一个分组，一次一个，但分组的大小可能不同，对吧？在这个例子里，A 发送的分组长度，用 L_A 表示，确实可能小于 B 发送的分组长度，用 L_B 表示。好，比如，如果是这样，如果，如果这里 L_A 小于 L_B，那么根据我们的计算，A 的吞吐量就会小于 B 的吞吐量，对吧？嗯。

## 36 · 00:55:13 · 相同分组长度使DCF吞吐量相等

原标说话人 1  00:55:13
Instead, if they have packets of the same size, so now let’s consider that L_A is equal to L_B, then in this case they will enjoy the same throughput. Is it clear? Okay, that was in DCF.
反过来，如果它们的分组大小相同，现在假设 L_A 等于 L_B，那么这种情况下，它们就会获得相同的吞吐量。清楚了吗？好，这是 DCF 的情况。

## 37 · 00:55:39 · 比较EDCA与DCF的平均发送时间线

原标说话人 1  00:55:39
The bottom representation is what we have on average when we use EDCA instead. Okay? What is the difference between EDCA and DCF? Don’t be shy. What is the difference?
下方这张图表示的是改用 EDCA 时的平均情况。好吧？EDCA 相比 DCF 有什么区别？别害羞，有什么区别？

## 38 · 00:56:22 · EDCA同优先级队列获得相同发送时长

原标说话人 1  00:56:22
“The same duration” [reply wording uncertain]. Excellent, thank you. So, since we are considering queues at each station having the same priority, every time they transmit, they get access to the channel, they do so for the same duration. And this is indeed what we have represented here, right? So this is as long as this. And so they have exactly the same duration, right? That’s a fact, because EDCA works this way.
“时长相同”，这里回答的具体措辞不确定。很好，谢谢。因此，由于我们考虑的是各站点上优先级相同的队列，每次它们发送、接入信道时，获得的发送时长相同。图中画的正是这个，对吧？这一段和那一段一样长，所以持续时间完全相同，对吧？这是确定的，因为 EDCA 就是这样工作的。

## 39 · 00:57:10 · 以跑步速度类比TXOP内的数据发送速率

原标说话人 1  00:57:10
We have the same transmission opportunity limit because we are considering two queues of the same priority within A and within B, presumably. Okay, so now what is the throughput enjoyed by A? Again, EDCA is also fair to all Wi-Fi cards in terms of their chances of accessing the channel, right? So we can say, okay, during this time period T, say A gets access to the channel n times, okay? Every time it gets access to the channel, it will be able to transmit for the transmission opportunity limit. And how many bits do we fit into that time? It depends on the bit rate, on the speed used by A, right? So it’s like when you run on a, on a field, right? You have, for example, let’s say, how many meters are you able to run if you run for one minute? It depends on how fast you are. If you are very fast, in one minute you run many meters. If you are slow, if you walk, then in one minute you are able to cover a smaller number of meters, right? And it’s exactly the same thing.
它们有相同的传输机会限额，因为我们比较的是 A 内部和应该是 B 内部两个优先级相同的队列。好，那么 A 的吞吐量是多少？同样，在信道接入机会方面，EDCA 也公平地对待所有 Wi-Fi 网卡，对吧？所以，我们可以说，在时间段 T 内，假设 A 接入信道 n 次。每次接入信道，它都可以发送传输机会限额所规定的时间。那么，这段时间里能放入多少比特？这取决于比特率，取决于A 使用的速度，对吧？这就像你在场地上跑步，对吧？比如说，如果跑一分钟，你能跑多少米？这取决于你跑得有多快。如果你很快，一分钟就能跑很多米。如果你很慢，如果是在走路，那么一分钟只能走较少的米数，对吧？这里完全一样。

## 40 · 00:59:13 · 固定TXOP内发送速度越快可传比特越多

原标说话人 1  00:59:13
So this is the time, okay? Let’s say our transmission opportunity limit is one minute, and this is how fast A runs, okay, how fast A is at transmitting bits. If A is very fast, then within the transmission opportunity limit it will be able to transmit many, many bits.
所以，这里是时间，好吧？假设我们的传输机会限额是一分钟，这里是 A 跑得有多快，也就是 A 发送比特有多快。如果 A 很快，就能够在传输机会限额内发送很多、很多比特。

## 41 · 00:59:41 · 总发送比特数等于每次发送量乘以接入次数

原标说话人 1  00:59:41
Okay, what is the total number of bits A will be able to transmit over T? Well, clearly, the number of bits it can transmit during one transmission opportunity, multiplied by the times, the number of times it can access the channel, right, so it can run, okay? Same for B. So B will get n channel accesses, because we, again, we are fair in that respect. Every time it accesses the channel, it will be able to transmit, so to run for one minute.
好，A 在 T 内一共能够发送多少比特？显然，就是它在一次传输机会中能够发送的比特数，乘以次数，也就是它接入信道的次数，对吧？也就是它能够跑的次数，好吧？B 也是一样。B 会获得 n 次信道接入机会，因为在这一点上，我们同样保持公平。每次接入信道，它都能发送，也就是跑一分钟。

## 42 · 01:00:25 · 节点B的发送速率决定TXOP容量

原标说话人 1  01:00:25
Okay? To transmit for one transmission opportunity limit. And how many bits will it be able to fit into that transmission opportunity limit? It depends on how fast it is. Okay, so this is the speed of our transmitter.
好吧？也就是发送一个传输机会限额所规定的时间。那么，它能够在这个传输机会限额内放入多少比特？这取决于它有多快。好，这就是发送方的速度。

## 43 · 01:00:46 · 用观察期内的总比特数除以时间计算吞吐量

原标说话人 1  01:00:46
So the numerator in both cases, again, represents the number of bits that a node is able to transmit over a period T. Dividing by T gives the throughput. Okay, is the throughput computation clear?
因此，两种情况下的分子，仍然都表示一个节点在时间 T 内能够发送的比特数。再除以 T，就得到吞吐量。好，吞吐量的计算清楚了吗？

## 44 · 01:01:14 · 吞吐量计算是可能出现的考试内容

原标说话人 1  01:01:14
Okay, this is very important. Okay, it might appear in the test. So if it’s not clear, let me know. Okay, don’t complain then if you find a question on this in the test. You’re positive that it’s clear?
好，这非常重要。好，它可能出现在考试里。所以，如果不清楚，告诉我。好，如果你们之后在考试里发现了关于这个的问题，可不要抱怨。你们确定这已经清楚了吗？

## 45 · 01:01:40 · EDCA中相同发送速率带来相同吞吐量

原标说话人 1  01:01:40
Okay, back. So again, we ask ourselves: when do A and B achieve the same throughput? If we look at these two expressions, we can see that if they have the same speed, so they are able to transmit bits at the same speed, then they will also achieve the same throughput.
好，回到这里。我们再次问：A 和 B 什么时候能获得相同的吞吐量？看这两个表达式就能发现，如果它们速度相同，也就是能够以相同的速度发送比特，那么它们也会获得相同的吞吐量。

## 46 · 01:02:16 · 时间公平与应用实际传输性能的关系

原标说话人 1  01:02:16
Okay, so in Wi-Fi, thanks to the standard [word uncertain], we now have temporal fairness, not per-packet fairness anymore. Okay, we have temporal fairness. Then nodes that are equally fast at transmitting will also be able to achieve the same throughput, and throughput is what matters in terms of performance. Because it tells you how many bits, application-layer bits essentially, bits that are of interest to the application, may be transmitted or received over a time period. So it really tells you, if you have to upload or download a video or whatever, essentially how long it takes. Okay? So throughput is what matters. Is it clear? Okay, better. Then, just to be even clearer.
好，所以在 Wi-Fi 中，由于这个标准，这里“标准”一词不确定，我们现在有了时间公平，而不再是逐分组公平。好，我们有了时间公平。因此，发送速度相同的节点，也能够获得相同的吞吐量，而吞吐量才是衡量性能时重要的指标。因为它告诉我们，在一段时间里能够发送或接收多少比特，基本上就是应用层比特，也就是应用关心的比特。所以，如果你要上传或者下载一个视频，或者别的什么，它实际告诉你的就是大概要花多长时间。好吧？因此，吞吐量才是重要的。清楚了吗？好，这样更清楚了。接下来，再说得更清楚一点。

# 六、流量信令与呼叫接纳控制

## 47 · 01:03:51 · 流量信令进一步帮助接入点控制BSS流量

原标说话人 1  01:03:51
Hmm. Okay. Okay. So, that said, let’s move to essentially the last few slides for this version of Wi-Fi. We already know how both the centralized and the distributed channel-access schemes work. And we said one important thing is that the access point now gets informed, notified, about the traffic that each Wi-Fi card has in its queues, right? And that allows the access point to plan, to schedule traffic efficiently, so that we can meet the quality-of-service requirements. Okay, that said, let me add that there is one more thing that helps the access point control the traffic of the BSS. Okay, what is this additional feature? It is called traffic signaling.
嗯。好。好。所以，说完这些，我们转到这个Wi-Fi版本基本上最后的几张幻灯片。我们已经知道集中式和分布式信道接入方案是怎样工作的。而且我们说过，一件重要的事情是，接入点现在会获知、会收到通知，知道每一块Wi-Fi网卡队列里的流量，对吧？而这使接入点能够有效地规划、调度流量，从而让我们满足服务质量要求。好，说完这些，让我补充一下，还有一件事能够帮助接入点控制BSS中的流量。好，这个额外的功能是什么？它叫作流量信令。

## 48 · 01:05:30 · 通过显式握手协商吞吐量、时延和丢包需求

原标说话人 1  01:05:30
So traffic signaling may happen through the Quality of Service Control subfield in the MAC header, as we said before. But it can also happen through an explicit handshake between the access point and a Wi-Fi station. When a Wi-Fi card, so a user, wants to start a new traffic flow, for example wants to upload a new video or a new photo, it can contact the access point in advance and say, “Look, I’d like to start this traffic flow, but I, I need this throughput for this traffic flow. I need to achieve this throughput, and, for example, this maximum delay and this maximum packet-loss probability.” Okay. So the access point can reply to this Wi-Fi card, saying, “Look, that’s fine. I have enough radio resources, enough space, let’s say, in the BSS to accommodate your traffic flow and allow you to achieve the quality of service that you want.”
所以，正如我们之前说过的，流量信令可以通过MAC首部中的服务质量控制子字段来进行。但是，它也可以通过接入点与Wi-Fi站点之间的显式握手来进行。当一块Wi-Fi网卡，也就是一个用户，想要启动一个新的流量流，比如想上传一个新视频或者一张新照片时，它可以事先联系接入点，说：‘听着，我想启动这个流量流，但是我，我需要这个流量流具有这样的吞吐量。我需要达到这个吞吐量，以及，比如说，这个最大时延和这个最大丢包概率。’好。所以，接入点可以回复这块Wi-Fi网卡，说：‘听着，这没问题。我有足够的无线资源，足够的空间，可以说，在BSS中有足够空间容纳你的流量流，让你达到想要的服务质量。’

![图83：Traffic Signaling](../slide-images/slide-083.png)

课件：02-WiFi_1-7.pdf · PDF第42页上半页 · 图83（按PDF顺序）

## 49 · 01:07:21 · 呼叫接纳控制限制业务量并减少竞争碰撞

原标说话人 1  01:07:21
And at that point the user can start the traffic flow. Or the access point may say, “I don’t have so much room in the BSS right now. So if you want to start this new traffic flow, fine, but look, I can give you this much throughput. It is not what you are asking for; it is a bit lower, but this is what I can offer.” And the Wi-Fi card would say, “Okay, I take it, fine, I’ll start my traffic flow.” Or it can say, “No, no, no, this does not work for me. I will wait. There is no way to send the traffic flow efficiently enough for me. I give up, or I will do it later.” Okay? Or the access point can just say, “Look, there is no room at all. Forget about starting a new traffic flow.” So there is a sort of so-called call admission control. It’s a call-admission-control mechanism through which the access point can control up front the amount of traffic handled within its BSS. So it can avoid having too many traffic flows, too many stations transmitting or trying to transmit in the BSS. So it can reduce the level of contention in the BSS, so that during the contention period there will be fewer stations contending and therefore a lower collision probability. Okay, so this helps control the amount of traffic that we need to handle within the BSS, and it is very effective.
这时，用户就可以开始这个业务流。或者，接入点可能会说：“现在 BSS 中没有那么多空间。如果你想启动这个新业务流，也可以，但我只能提供这么多吞吐量。这不是你要求的数值，会低一点，不过我只能给这么多。”Wi-Fi 网卡可以说：“好，我接受，那我开始发送这个业务流。”也可以说：“不，不，不，这对我不行。我先等等。这种条件下，我没法以自己需要的效率发送这个业务流。我放弃，或者以后再做。”好吧？接入点也可以直接说：“现在一点空间都没有，别启动新的业务流了。”因此，这里有一种所谓的呼叫接纳控制。它是一种呼叫接纳控制机制，通过它，接入点可以事先控制 BSS 内所处理的业务量，从而避免出现过多业务流，避免太多站点同时发送或者试图发送。因此，它能够降低BSS 中的竞争程度，使竞争期内参与竞争的站点更少，从而降低碰撞概率。好，这有助于控制 BSS 内需要处理的业务量，而且非常有效。

## 50 · 01:10:16 · 流量与时延控制小结及802.11n内容导入

原标说话人 1  01:10:16
Okay, it’s one more tool we have in Wi-Fi to keep the traffic, and therefore the traffic load, and therefore the delay, under, under control. Okay, so in the slides you will also find several things that we mentioned. Before moving to the numerical problems, right, the examples I promised we would look at together this morning, let’s also look at the very last things related to this Wi-Fi 4. As an amendment, this part is labeled 802.11n.
好，这是Wi-Fi中我们拥有的另一个工具，用来让流量，因此也让流量负载，因此也让时延，处于、处于控制之下。好，所以在幻灯片里，你们也能找到我们提到的几件事情。在转到数值问题之前，对，就是我承诺今天上午会一起看的那些例子，让我们也看看与这个Wi-Fi 4有关的最后几个内容。作为一项修订，这一部分标为802.11n。

![图86：Wi-Fi 4 (802.11n) — PHY/MAC Enhancements](../slide-images/slide-086.png)

课件：02-WiFi_1-7.pdf · PDF第43页下半页 · 图86（按PDF顺序）

# 七、物理层增强与波束成形

## 51 · 01:11:16 · 额外增强主要在物理层且细节仅供了解

原标说话人 1  01:11:16
And there are, let’s say, additional features that we find in Wi-Fi 4, okay? They are not really related to the way nodes access the channel; these additional features are more related to the physical layer. Okay, related to the MAC layer, there are very few things to add. You don’t need to remember what relates to the physical layer; it is just for your information.
而且，可以说，在Wi-Fi 4中，我们还有额外的功能，好吗？它们实际上不涉及节点接入信道的方式；这些额外功能更多地涉及物理层。好，关于MAC层，需要补充的东西很少。你们不需要记住涉及物理层的内容；它只是供你们了解。

## 52 · 01:12:00 · OFDM、MIMO与喊话类比引入波束成形

原标说话人 1  01:12:00
So, for example, in this new version of Wi-Fi, Wi-Fi 4, there is this particular amendment, 802.11n, which relates to the physical layer and tries to improve the physical, the physical layer. This is something we already said when commenting on the table that gave you the big picture of Wi-Fi evolution. Remember the initial table with all the different versions of Wi-Fi and the summary of the evolution. So if you remember that table, for example, we already mentioned that newer versions of Wi-Fi use not just OFDM at the physical layer; they also use MIMO. Remember what MIMO is? We mentioned it already. And there is one more thing they use: beamforming, still at the physical layer. What is beamforming? It’s a very simple concept. I don’t know if you do this in China, but in Europe, when you want to call someone, right, you are in a street, you see your friend, and your friend hasn’t seen you, so you want to attract your friend’s attention. And you shout at your friend, right? For example, your friend is called John. So you want to shout “John!” to attract his attention, right? So what we do is put our hands here and shout “John!” Why do we do that? I don’t know if you do the same. To direct our voice towards that person. So our voice, if I don’t do that, just gets spread, right, everywhere. But if I put my hands here, I direct my voice better towards that person, and it is more likely that the person receives my voice loudly enough, right? So they are more likely to hear it. That’s exactly what beamforming does.
比如，在这个较新的 Wi-Fi 版本，也就是 Wi-Fi 4 中，有一个具体的修订 802.11n，它涉及物理层，试图改进物理层，物理层。这一点在之前讲 Wi-Fi 演进总览表时，我们已经提到过。还记得最初那张表吗？它列出了不同的 Wi-Fi 版本，并总结了演进过程。比如，我们已经说过，较新的 Wi-Fi 版本在物理层不仅使用 OFDM，还使用 MIMO。还记得 MIMO 是什么吗？我们已经提过。另外，它们还使用一个功能，也在物理层，叫作波束成形。波束成形是什么？概念非常简单。我不知道你们在中国是不是也这样做，但在欧洲，当你想喊一个人的时候，比如说，你走在街上，看见一个朋友，但他还没看见你，所以你想引起他的注意。你就朝他喊，对吧？比如，你的朋友叫 John，你就喊“John！”来引起他的注意。我们会把手拢在这里，喊“John！”为什么这样做？我不知道你们是不是也一样。这样是为了把声音朝着那个人的方向传过去。如果不这样做，声音就会向四面八方散开。但如果把手拢在这里，就能更好地把声音朝向那个人，让他更有可能听到足够响的声音，对吧？于是，他听到的可能性就更大。这正是波束成形所做的事情。

## 53 · 01:15:00 · 节点与接入点形成指向接收方的波束

原标说话人 1  01:15:00
So if you have an access point and a user, for example A here, the antenna you use to transmit to the access point will have this radiation pattern, so that the power emitted at the physical layer from the node towards the access point will be directed. So instead of having an omnidirectional antenna that spreads power everywhere, this is the omnidirectional antenna, when you do beamforming, you form a beam, right? Beamforming means forming a beam. This is a beam. And you form a beam directed towards the access point. And the same, when the access point wants to transmit towards this node, it will form a beam pointing to this node. If instead the access point wants to transmit towards this other node, B, it will form a beam directed towards B, presumably.
假设这里有一个接入点，还有一个用户，比如 A。你用来向接入点发送的天线，会有这样的辐射方向图，使节点在物理层发出的功率朝向接入点。因此，不再像全向天线那样把功率向各个方向散开，这里画的是全向天线；进行波束成形时，你形成一个波束，对吧？波束成形就是形成波束。这就是一个波束，你形成一个指向接入点的波束。同样，当接入点想向这个节点发送时，就会形成一个指向这个节点的波束。如果接入点想向另一个节点 B 发送，就会形成一个应该是朝向 B 的波束。

## 54 · 01:16:48 · 集中发射功率提升接收信号质量

原标说话人 1  01:16:48
Okay, so this is the general concept of beamforming. When transmitters, instead of just transmitting everywhere, try to direct their power, their transmission power, along a certain direction where they know the intended receiver is, the power will be mainly concentrated around that direction. And the result is the same as I was saying before in my example: the signal transmitted by the node will be received with higher power at the receiver, right? So the receiver will understand better what we have transmitted. That’s the key point of beamforming. Okay. So in more recent versions of Wi-Fi, we indeed have the possibility to create beams with our antennas at the physical layer, and therefore improve the quality of transmission because the received power will be higher.
好，这就是波束成形的一般概念。发送方不再简单地向所有方向发送，而是把功率、发射功率，集中朝向某个方向，因为它知道目标接收方就在那个方向。因此，功率主要集中在这个方向附近。结果就像我前面的例子一样：节点发出的信号，到达接收方时具有更高的接收功率，对吧？于是，接收方就能更好地理解我们发送的内容。这就是波束成形的关键。因此，在较新的 Wi-Fi 版本中，我们确实能够在物理层通过天线形成波束，从而提高传输质量，因为接收功率会更高。

![图90：Beamforming](../slide-images/slide-090.png)

课件：02-WiFi_1-7.pdf · PDF第45页下半页 · 图90（按PDF顺序）

## 55 · 01:18:13 · 波束成形随Wi-Fi版本演进而改进

原标说话人 1  01:18:13
Now, as we know, Wi-Fi 4 is an intermediate version in Wi-Fi evolution, right? We are now at Wi-Fi 7, and Wi-Fi 8 is under standardization. So in this intermediate version of Wi-Fi, beamforming is not working very well. It has been introduced, but it is not working very well. But in even more recent versions of Wi-Fi, 5, 6, 7, beamforming works very well. So now, when our phone, for example, communicates through Wi-Fi with our home access point, there is actually a beam between the Wi-Fi card in the phone and the access point at home. Okay. Transmission and reception happen over this beam. Okay, so that’s something useful at the physical layer.
现在，正如我们所知，Wi-Fi 4 是 Wi-Fi 演进中的一个中间版本，对吧？现在已经发展到 Wi-Fi 7，而 Wi-Fi 8 正在标准化。所以，在 Wi-Fi 4 这个中间版本中，波束成形还不是很好用。它已经引入了，但效果还不是很好。不过，在更新的 Wi-Fi 5、6、7 中，波束成形就很好用了。因此，比如我们的手机通过 Wi-Fi 与家里的接入点通信时，手机中的 Wi-Fi 网卡和家中接入点之间，实际上就有一个波束，发送和接收沿着这个波束进行。这就是物理层中一个有用的功能。

# 八、信道聚合、MCS与MIMO速率提升

## 56 · 01:19:30 · Wi-Fi工作频段与可用信道回顾

原标说话人 1  01:19:30
The other, the other thing we have in Wi-Fi 4, and even more in subsequent versions, is, remember what we said about spectrum use, right? Wi-Fi may work at 2.4 gigahertz, 5 gigahertz, or 6 gigahertz. And when it works at 2.4 gigahertz, there are three possible channels available.
另外，另外一个在 Wi-Fi 4 以及后续版本中更加突出的功能，还记得我们讲过频谱的使用吗？Wi-Fi 可以工作在 2.4 GHz、5 GHz 或 6 GHz。当它工作在 2.4 GHz 时，有三个可用信道。

## 57 · 01:20:07 · 不同频段的不重叠信道与约20MHz带宽

原标说话人 1  01:20:07
We represented them this way, if you remember the figure. When we work at 5 gigahertz, there are actually 12 [channel count uncertain] that do not overlap. When we work at 6 gigahertz, there are even more that do not overlap. And each of these frequency bands, we said, just to give a rough number, is 20 megahertz wide, okay? So the width of each channel is more or less 20 megahertz.
如果还记得那张图，我们把它们画成了这样。当工作在 5 GHz 时，实际上有 12 个互不重叠的信道，这个信道数量不确定。工作在 6 GHz 时，互不重叠的信道还会更多。我们说过，这些频带每个大约有 20 MHz 宽，只是给一个粗略数值，好吧？所以，每个信道的宽度大约是 20 MHz。

## 58 · 01:20:50 · 聚合两个信道扩大带宽并提升发送速率

原标说话人 1  01:20:50
Okay, so what they tried to do in Wi-Fi was to increase the transmission speed of the nodes, right? We want to be as fast as possible. So, to give Wi-Fi nodes the possibility of increasing their speed, they allowed the BSS, and therefore the access point and stations, to use not just one channel but, for example, two channels at the same time, to aggregate two channels. And this means that instead of transmitting only on this portion of the spectrum, you now have double the bandwidth. So you can essentially double your transmission speed by doing that, okay? So essentially, instead of 20, you can use 40 megahertz of bandwidth, which makes your transmissions faster, as I was saying.
好，Wi-Fi 希望做的就是提高节点的发送速度，对吧？我们希望越快越好。因此，为了让 Wi-Fi 节点能够提高速度，允许一个 BSS，也就是其中的接入点和站点，不仅使用一个信道，而是例如同时使用两个信道，把两个信道聚合起来。这意味着，你不再只在这部分频谱上发送，而是拥有了两倍的带宽。这样，发送速度基本上也能翻倍，好吧？因此，你可以使用 40 MHz 的带宽，而不只是 20 MHz，正如我说过的，这会让发送更快。

![图87：802.11n Physical Layer: Overview](../slide-images/slide-087.png)

课件：02-WiFi_1-7.pdf · PDF第44页上半页 · 图87（按PDF顺序）

## 59 · 01:22:19 · 更高阶调制让每个信号携带更多比特

原标说话人 1  01:22:19
Also, if you remember what we said about modulation, we now accommodate more efficient modulations. This means essentially that you have 16 signals in your constellation. This means that you have 64 signals in your constellation. So in this case, you may remember, with one signal we can transmit four bits, right? [Which constellation “this case” indicates is unclear.] So by increasing this number here, and in more recent versions of Wi-Fi it is even larger, you are able to transmit more bits with one signal, and that also helps increase the bit rate.
另外，如果还记得前面讲过调制，现在可以使用效率更高的调制方式。这里表示星座中有 16 个信号点，这里表示星座中有 64 个信号点。因此，在这种情况下，你们可能记得，一个信号就能传输 4 个比特，对吧？这里“这种情况”具体指哪一个星座并不清楚。通过增大这里的数值，而且较新 Wi-Fi 版本中的数值还更大，每个信号就能够携带更多比特，这也有助于提高比特率。

## 60 · 01:23:17 · 信道质量、编码率与调制编码方案MCS

原标说话人 1  01:23:17
Of course, this is possible only if your channel is good enough. Okay. The coding rates also vary. Remember what we said about channel coding, and we defined the coding rate. So this essentially tells you how many redundant bits you are sending for each block, if you remember what we said at the beginning. So you have multiple options. And essentially this means that depending on the coding rate you use, and depending on the modulation you use, you will be able to achieve a different bit rate, a different speed. So the coding rate and the type of modulation you use are essentially referred to as a modulation and coding scheme.
当然，只有信道足够好时，才可能这样做。好，编码率也有不同选择。还记得我们讲过信道编码，并定义了编码率吗？如果记得最初讲的内容，它基本上反映了每个块中发送多少冗余比特。所以，你有多种选择。这意味着，所用的编码率不同、调制方式不同，能够达到的比特率、速度也不同。所使用的编码率和调制类型，合起来基本上就叫作调制与编码方案。

![图88：802.11n: Data Rates](../slide-images/slide-088.png)

课件：02-WiFi_1-7.pdf · PDF第44页下半页 · 图88（按PDF顺序）

## 61 · 01:24:26 · MCS与MIMO并行空间流共同提高速率

原标说话人 1  01:24:26
We have different possibilities, different modulation and coding schemes that the transmitter can apply. And depending on the selected modulation and coding scheme, it will be able to transmit at different bit rates, okay, faster, more fast, or, or less fast. Also, as you can see here, we have MIMO. In particular, you may have two antennas at the transmitter and two at the receiver, or three antennas at the transmitter and three at the receiver, or four antennas at the transmitter and four at the receiver. The more antennas you have, the more parallel streams you can transmit, and, as we said, the greater, again, the ability to transmit bits. So, as I was saying, all these improvements allow a Wi-Fi card to be faster and faster. That’s the goal, and they are all enhancements made at the physical, physical layer.
我们有不同的可能性，发送端可以采用不同的调制与编码方案。而且，根据所选的调制与编码方案，它能够以不同的比特率发送，好，更快、更快，或者、或者不那么快。另外，正如这里能看到的，我们有MIMO。特别是，发送端可以有两根天线，接收端有两根；或者发送端三根天线，接收端三根；或者发送端四根天线，接收端四根。天线越多，你能够发送的并行流就越多，而且，正如我们说过的，发送比特的能力也会再次更强。所以，正如我刚才所说，所有这些改进使Wi-Fi网卡能够越来越快。这就是目标，而且它们全都是在物理、物理层作出的增强。

## 62 · 01:25:45 · Wi-Fi 4可用比特率与信道质量的关系

原标说话人 1  01:25:45
Here you have a summary of the possible bit rates at which, in this version, Wi-Fi 4, we can transmit. Depending on the quality of the channel, you can use a different modulation and coding scheme and therefore achieve different speeds, okay, varying from essentially 6.5 megabits per second up to, in the best possible case, 600 megabits per second.
这里总结了 Wi-Fi 4 这个版本中可能达到的发送比特率。根据信道质量，可以使用不同的调制与编码方案，从而达到不同速度，基本上从每秒 6.5 兆比特，一直到最佳情况下的每秒 600 兆比特。

![图89：802.11n Example Data Rates](../slide-images/slide-089.png)

课件：02-WiFi_1-7.pdf · PDF第45页上半页 · 图89（按PDF顺序）

# 九、物理层发送速率的含义与课堂讨论

## 63 · 01:26:25 · 物理层细节的学习范围与性能启示

原标说话人 1  01:26:25
Okay, this is Wi-Fi 4. Okay, so you can skip these slides because they are again about, this slide is essentially about beamforming. As I said, this is something we just need to know, to understand as a concept, but it is not important for us now. What is important instead is the following that I’m going to explain. So, before introducing what is essentially interesting to us in this case, in this amendment of Wi-Fi 4, let’s reflect on the consequences of what we said about the physical layer.
好，这是 Wi-Fi 4。所以，这些幻灯片可以跳过，因为它们还是在讲，这一页基本上是在讲波束成形。正如我说过，我们只需要知道、理解这个概念，现在它对我们不是重点。真正重要的，是接下来我要解释的内容。在介绍这个 Wi-Fi 4 修订中真正值得我们关注的内容之前，先思考一下刚才那些物理层改进意味着什么。

## 64 · 01:27:31 · Wi-Fi演进不断提高可达最高发送速率

原标说话人 1  01:27:31
Okay, so don’t worry about the details of the physical layer. But what is the major observation we can make here? The basic observation is that as we evolve with Wi-Fi, we have the possibility of increasing, more and more, the maximum speed that can be achieved.
好，不用担心物理层的细节。不过，从这里能够得到的主要观察是什么？最基本的一点是，随着 Wi-Fi 的演进，能够达到的最高速度可以越来越高。

## 65 · 01:28:08 · 比较11Mbps、600Mbps与46Gbps速率

原标说话人 1  01:28:08
Okay. Now, in the very initial version of Wi-Fi, remember, it was 11 megabits per second. We know from the summary table we looked at, probably the first time, that nowadays we can achieve 46 gigabits per second, right, as the maximum speed. This, as I said, is an intermediate version in the evolution, so its maximum is 600 megabits per second. So, if you look at these values, 11 megabits per second, this intermediate one, 600 megabits per second, and now 46 gigabits per second.
好。记得，在非常早期的 Wi-Fi 版本中，速度是每秒 11 兆比特。从最初可能就看过的那张总结表中，我们知道，如今最高可以达到每秒 46 吉比特，对吧？而这里，正如我说过，是演进中的一个中间版本，最高速度是每秒 600 兆比特。因此，看这几个数值：每秒 11 兆比特，中间这个每秒 600 兆比特，再到现在的每秒 46 吉比特。

## 66 · 01:29:00 · 物理层提供的高发送速率究竟如何使用

原标说话人 1  01:29:00
Okay, these are the maximum speeds that can be achieved, but they are increasing, increasing. So even though unlucky users still have relatively low speeds, okay, on average, what can we say? On average, we can say that the more recent the Wi-Fi card we use, the faster we can be in transmission. That’s easy to observe. But let’s think about it a little more. What is this speed used for in Wi-Fi? And now you answer. What does it mean, 600 megabits per second, if you are a lucky user? How do you use this speed? So this is a kind of power the physical layer gives you, right? What do you do with this ability, this powerfulness of the physical layer, this high performance of the physical layer? What do you do with that?
好，这些是能够达到的最高速度，而且还在不断提高、不断提高。虽然不太幸运的用户仍然只有相对较低的速度，不过，平均而言，我们能说什么？平均而言，我们可以说，使用的 Wi-Fi 网卡越新，发送速度就可以越快。这很容易看出来。但再仔细想一想：在 Wi-Fi 中，这个速度用来做什么？现在你们回答。如果你是一个幸运的用户，每秒 600 兆比特意味着什么？你怎么使用这个速度？这是物理层赋予你的一种能力，对吧？有了这种能力，有了这么强大的物理层、这么高性能的物理层，你用它来做什么？你会拿它做什么？

## 67 · 01:30:50 · 鼓励回答物理层速率含义的问题

原标说话人 1  01:30:50
Even if you answer wrong, don’t worry. But we’re going to stay here until someone answers. So it’s almost 35; please say something.
即使你回答错了，也不用担心。但是，我们会一直待在这里，直到有人回答。所以，已经快35了；请说点什么。

## 68 · 01:31:20 · 再次追问600Mbps意味着什么

原标说话人 1  01:31:20
What does it mean to have a speed of 600 megabits per second?
拥有每秒 600 兆比特的速度，到底意味着什么？

## 69 · 01:31:40 · 明确速率概念后再继续与休息安排

原标说话人 1  01:31:40
Okay, so you may want to think about it, but unless we go over this, we cannot continue, because it is useless to go on. Okay, so unless someone answers, whatever, otherwise there is no point in going on. If you cannot get this concept, what transmitting at 600 megabits per second, or 46 gigabits per second, or 11 megabits per second in Wi-Fi means, I’m afraid we have to go backwards, not forwards, with our slides. Okay? So let’s have a 25-minute break, and then let’s reconvene after the break and see if we can figure it out. Okay? Good. I’ll see you then. [Final brief phrase unclear.] Okay, good, thanks.
好，你们可以想一想，但如果这个问题没有讲明白，我们就无法继续，因为继续下去也没有用。所以，至少得有人回答，随便说点什么，否则继续讲就没有意义。如果你们还理解不了这个概念，不知道在 Wi-Fi 中以每秒 600 兆比特、每秒 46 吉比特或者每秒 11 兆比特发送意味着什么，那恐怕我们的幻灯片就得往回看，而不是继续往前讲。好吧？我们先休息 25 分钟，休息之后再回来，看看能不能把它弄清楚。好吧？好，待会儿见。最后一句简短的话不清楚。好，很好，谢谢。

