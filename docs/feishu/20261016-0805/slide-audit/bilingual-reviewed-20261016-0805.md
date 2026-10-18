说明：Git文本检查点不含图片二进制；图像见飞书原文或完整ZIP。

# 双语对照：录音机-20261016-0805

https://lcn6dqn3m0yr.feishu.cn/docx/H8UxdBbx7owjVmxCeMbcnihengg

课件审计检查点：87段原正文与导航保留，24张图已逐张核验；4项课堂图来源缺口；未作原音转写认证。

会议主题：录音机-20261016-0805
课程：移动与传感器网络 / Mobile Sensor Networks
上传时间：2026年10月16日（周五） 09:36 （GMT+08）
音频时长：约 01:30:43
整理日期：2026年10月18日
版本：完整忠实双语稿 · 913cf98f5b3c
状态：双语正文已完成（87 对）；已匹配插入24张课件图

[原录音附件块保留，音频二进制未打包]

录音文件：点击打开原始录音并播放

原资源链接：https://lcn6dqn3m0yr.feishu.cn/minutes/obcnneupacaz461n7m32skxv

文字来源：原始文字记录

原资源链接：https://lcn6dqn3m0yr.feishu.cn/docx/CmfWdCMtWocccHxBB1IcaDH4n1d

课件来源：04-Sensors-MAC.pdf

原资源链接：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/04-Sensors-MAC.pdf

# 一、物理层带宽与小型分组

## 01 · 00:00:00 · 信道带宽与可达比特率

原标说话人 1  00:00:00
We actually are able to achieve lower bit rates, lower speeds, because the available bandwidth is narrower. You can see that for each channel, indeed, we have one megahertz of width. When instead we work at 2.4 gigahertz, each channel is larger, so we have essentially a larger bandwidth, more frequencies in the frequency channel that we consider. And this means that we can send essentially more signals per second, and therefore achieve higher bit rates.
我们实际上能够达到的是更低的比特率、更低的速度，因为可用带宽更窄。你们可以看到，确实，每个信道的宽度是1兆赫。而当我们工作在2.4吉赫时，每个信道更宽，所以基本上，我们有更大的带宽，在我们所考虑的频率信道中有更多频率。这意味着，我们基本上每秒能够发送更多信号，从而达到更高的比特率。

![图31：Operating Frequency Bands](../slide-images/slide-031.png)

课件：04-Sensors-MAC.pdf · PDF第16页上半页 · 图31（按PDF顺序）

## 02 · 00:00:48 · 物理层调制提示与分组格式

原标说话人 1  00:00:48
You don't need to memorize this slide, but just to say that, in terms of transmission, we are using a particular type of modulation that is called [the modulation/spreading term is unclear in both transcripts]. You don't need to learn what that is. What is instead interesting is to look at the size of the packets. This is the size of a packet at the physical layer.
你们不需要记住这张幻灯片，不过这里只是想说，在传输方面，我们使用一种特定类型的调制，叫作[调制／扩频术语在两份转写中均不清楚]。你们不需要学习那是什么。相反，有意思的是看看分组的大小。这就是物理层一个分组的大小。

![图32：PHY Layer](../slide-images/slide-032.png)

课件：04-Sensors-MAC.pdf · PDF第16页下半页 · 图32（按PDF顺序）

## 03 · 00:01:23 · 短首部与小型有效载荷

原标说话人 1  00:01:23
And we can see that of course we need a header, for sure, a header. But this is a short header; it's six bytes, it's quite short. And then, of course, if it is a control packet, then the payload will be zero. Control packets have got zero payload. If it's a data packet, the payload can be up to 127 bytes, which is very small, very small.
而且我们可以看到，当然，我们需要一个首部，肯定需要，一个首部。不过，这是一个很短的首部；它是6字节，相当短。然后，当然，如果这是一个控制分组，那么有效载荷就是零。控制分组的有效载荷为零。如果这是一个数据分组，有效载荷最多可以达到127字节，这非常小，非常小。

## 04 · 00:01:57 · 低速率设计与转入MAC层

原标说话人 1  00:01:57
So this is to say, this confirms the fact that this kind of sensors have been designed to work at a low bit rate. We don't need high throughput, and indeed each packet has also got a small payload. Now let's move to the MAC layer. In the MAC, remember when we talked yesterday about the network topologies, and we said that there is going to be a coordinator?
所以，这是想说，这证实了这样一个事实：这类传感器被设计为以低比特率工作。我们不需要高吞吐量，而且确实，每个分组的有效载荷也很小。现在我们转到MAC层。在MAC中，还记得昨天我们谈到网络拓扑时，说过将会有一个协调器吗？

![图33：MAC LAYER](../slide-images/slide-033.png)

课件：04-Sensors-MAC.pdf · PDF第17页上半页 · 图33（按PDF顺序）

# 二、信标、超帧与协调器休眠管理

## 05 · 00:02:43 · PAN协调器管理网络并发送信标

原标说话人 1  00:02:43
Right? We call it the PAN coordinator. Now we briefly mentioned the fact that this coordinator is there in order to manage the network, record the nodes that are part of the network, those that leave, stop functioning, those that join in. But also it can provide, we said, synchronization—a synchronization, sorry, a time reference to all the other nodes. And indeed, in our network, the coordinator at the MAC layer can periodically send beacons, exactly like in Wi-Fi.
对吧？我们把它叫作PAN协调器。刚才我们简单提到，这个协调器是用来管理网络的，记录属于网络的节点、那些离开的节点、停止工作的节点、那些加入的节点。不过，它还能够提供我们说过的同步——一个同步，抱歉，是给所有其他节点提供时间参考。而且确实，在我们的网络中，协调器能够在MAC层周期性地发送信标，完全和Wi-Fi中一样。

![图34：MAC Layer: beacon-enabled mode](../slide-images/slide-034.png)

课件：04-Sensors-MAC.pdf · PDF第17页下半页 · 图34（按PDF顺序）

## 06 · 00:03:34 · 信标为超帧和节点提供时间参考

原标说话人 1  00:03:34
So we have a superframe that starts with, with a beacon, and this beacon is indeed a way to provide a time reference for all the other nodes of the network, so that they can be considered synchronized.
所以，我们有一个超帧，它由、由一个信标开始，而这个信标确实是一种给网络中所有其他节点提供时间参考的方式，这样就可以认为它们是同步的。

## 07 · 00:03:56 · 信标使能模式与节点活动组织

原标说话人 1  00:03:56
If the coordinator does that, then we say that our network works in beacon-enabled mode. Okay, so let's first look indeed at this case where we have beacons that are periodically transmitted by the coordinator. And it's easier to understand the organization of the nodes' activity in the network by looking at this picture.
如果协调器这样做，那么我们就说，我们的网络工作在信标使能模式。好，所以我们先来看看这种情况，也就是由协调器周期性地发送信标的情况。而且，看这张图，就更容易理解网络中节点活动的组织方式。

## 08 · 00:04:34 · 超帧内先竞争再无竞争接入

原标说话人 1  00:04:34
So, as I said, in this case, when the beacon is enabled, we have superframes. The superframe is again the time between two subsequent beacons, like in Wi-Fi. And then within a superframe we have two phases: one in which we use contention-based access, and the other in which we use contention-free access. So, very similar to what we had again in Wi-Fi, but the two are swapped. So we have this contention-based access first, and then the contention-free period afterwards.
所以，正如我所说，在这种情况下，当信标使能时，我们有超帧。超帧同样是两个相继的信标之间的时间，和Wi-Fi中一样。然后，在一个超帧内，我们有两个阶段：一个阶段采用基于竞争的接入，另一个阶段采用无竞争接入。所以，这又和我们在Wi-Fi中看到的情况非常相似，不过这两个阶段交换了顺序。因此，我们先有这个基于竞争的接入，然后才是无竞争期。

![图35：Optional Superframe Structure](../slide-images/slide-035.png)

课件：04-Sensors-MAC.pdf · PDF第18页上半页 · 图35（按PDF顺序）

## 09 · 00:05:31 · 同步时隙与标准术语差异

原标说话人 1  00:05:31
Now, if we look into each of these phases, we can see here that we have essentially a sort of time slots, right? So the time within these two phases, since the whole system is considered synchronized, is divided indeed into time slots. Now, the terminology used by this standard is a bit different, and as we will see, it's also a bit confusing with respect to the terminology used in Wi-Fi. This is just a heads-up.
现在，如果我们看看这两个阶段中的每一个，就可以看到，这里基本上有某种时隙，对吧？所以，由于整个系统被认为是同步的，这两个阶段内的时间确实被划分成时隙。现在，这个标准使用的术语有些不同，而且，正如我们将会看到的，与Wi-Fi中使用的术语相比，它也有些容易混淆。这只是提前提醒一下。

## 10 · 00:06:26 · 无竞争期时隙分配与节点休眠

原标说话人 1  00:06:26
We will detail how the contention-based access works under this beacon-enabled mode, but let me just say something about this contention-free period first. That is essentially very little, because the standard does not specify how the nodes should behave in this period in such a detailed manner. What the standard says is that during the contention-free period, as we expect, the PAN coordinator can give sensors access by assigning them a given time slot. So we have time-division multiple access, exactly like in LEACH. Remember LEACH that we discussed yesterday, and we said that within a cluster we are using time-division multiple access? So we have periods of time that are divided into slots, and then the cluster head, which now would be our coordinator, assigns slots to the sensors. Okay? So if we have this contention-free period, then essentially this is all we need to know about how the nodes will access the channel during that period. So it's not complicated. The interesting part here is that we may have nodes going to sleep very often, because remember, we need to save energy. So we may also have cases where the whole network goes to sleep. We may have, as represented here, superframes during which nobody is up, not even the coordinator. Okay? So everyone goes to sleep. This is a kind of extreme case, but it is possible. In other cases the coordinator remains awake, and sensors may go to sleep. Okay, so in that case, clearly they will not be able to transmit or receive traffic.
我们会详细说明在这种信标使能模式下，基于竞争的接入是怎样工作的，不过，先让我说说这个无竞争期。基本上，要说的内容非常少，因为标准并没有那么详细地规定节点在这一时期应该如何行动。标准所说的是，在无竞争期内，正如我们预期的那样，PAN协调器可以通过给传感器分配一个指定的时隙，让它们获得接入机会。所以，我们采用时分多址，完全和LEACH中一样。还记得我们昨天讨论过的LEACH吗？我们说，在一个簇内，我们使用时分多址，对吧？所以，我们有一些时间段，把它们划分成时隙，然后由簇首，也就是现在这里的协调器，给传感器分配时隙。好吗？所以，如果我们有这个无竞争期，那么，关于节点在这个时期将如何接入信道，基本上我们需要知道的就是这些。因此，它并不复杂。有意思的地方在于，我们可能会有一些节点非常频繁地进入休眠，因为要记住，我们需要节省能量。所以，我们也可能遇到整个网络都进入休眠的情况。我们可能会有这里所画出的这种超帧，在这些超帧期间，没有任何节点醒着，连协调器也不醒着。好吗？所以，所有节点都进入休眠。这算是一种极端情况，但它是可能的。在其他情况下，协调器保持唤醒，而传感器可能进入休眠。好，所以在这种情况下，显然，它们将无法发送或接收业务。

![图36：Energy Saving: whole-network idle](../slide-images/slide-036.png)

课件：04-Sensors-MAC.pdf · PDF第18页下半页 · 图36（按PDF顺序）

## 11 · 00:09:30 · 协调器缓存负担及时隙CSMA/CA导入

原标说话人 1  00:09:30
Clearly, during these time intervals in which sensors are asleep, if the coordinator gets some traffic to be delivered to them, the coordinator needs to store, cache these packets, wait for the sensors to wake up, and then it will be able to deliver the packets to the sensors. So from that we understand that the role of the coordinator is quite heavy. First of all, because sometimes it can go to sleep as well, but that means that the whole network will go to sleep. Otherwise the coordinator needs to remain awake. And then if the sensors, the single sensors, go to sleep, the coordinator needs to store packets for them. So if the sensors go to sleep for a long time, well, that's also something challenging, because the coordinator is still a sensor with reduced capabilities. So if it has to store many packets, then that's an issue, okay? After a while it may actually need to drop some packets because there is no room anymore for all the packets. Okay, that said, we are now going to look at the contention-based time interval still in the case where we have beacon-enabled mode, okay? So we are still considering beacon-enabled mode, when we have beacons, superframes, the two phases, and what we're going to focus on now is this phase. Okay? And detail how our sensors can access the channel during this time period. Okay, so this is called slotted CSMA/CA. So let's say that the good news is that we still have carrier-sense multiple access with collision avoidance.
显然，在传感器处于休眠状态的这些时间区间内，如果协调器收到一些要交给它们的业务，协调器就需要存储、缓存这些分组，等待传感器醒来，然后它才能把这些分组交给传感器。所以，由此我们可以理解，协调器承担的任务相当繁重。首先，因为有时候它也能够进入休眠，不过那意味着整个网络都会进入休眠。否则，协调器就需要保持唤醒。然后，如果传感器，单个的传感器，进入休眠，协调器就需要为它们存储分组。所以，如果传感器休眠很长时间，嗯，那也是一件有挑战的事，因为协调器仍然是一个能力有限的传感器。所以，如果它必须存储很多分组，那就是个问题，对吧？过一段时间，它实际上可能需要丢弃一些分组，因为再也没有空间容纳所有分组了。好，说完这些，现在我们要看看基于竞争的时间区间仍然是在我们采用信标使能模式的情况下，好吗？所以，我们仍然在考虑信标使能模式，这时我们有信标、超帧、两个阶段，而我们现在要重点关注的是这个阶段。好吗？并且详细说明，在这段时间内，我们的传感器如何能够接入信道。好，所以，这叫作时隙CSMA/CA。因此，可以说，好消息是，我们仍然采用带冲突避免的载波侦听多路访问。

![图37：Energy Saving: individual nodes](../slide-images/slide-037.png)

课件：04-Sensors-MAC.pdf · PDF第19页上半页 · 图37（按PDF顺序）

![图38：Slotted CSMA-CA overview](../slide-images/slide-038.png)

课件：04-Sensors-MAC.pdf · PDF第19页下半页 · 图38（按PDF顺序）

## 12 · 00:12:25 · 同步时隙中仍采用分布式竞争

原标说话人 1  00:12:25
So we know the main principles of this scheme, because these principles were also applied, used by Wi-Fi, right? This is good news. It is called slotted because, as we just said, time is considered divided into time intervals. Right? We are beacon-enabled, all the nodes are synchronized, so all of them can actually apply this time division into slots. But even if we have this division into time slots, during the contention-based access phase we have a distributed scheme.
所以，我们知道这个方案的主要原理，因为这些原理也被Wi-Fi应用过、使用过，对吧？这是好消息。它被称为时隙式，是因为，正如我们刚才所说，时间被认为是划分成时间区间的。对吧？我们采用信标使能模式，所有节点都是同步的，所以它们实际上都能够采用这种把时间划分成时隙的方式。不过，即使有这种时隙划分，在基于竞争的接入阶段，我们采用的仍然是一个分布式方案。

## 13 · 00:13:23 · 与Wi-Fi共用CSMA/CA原理

原标说话人 1  00:13:23
In this contention-based phase, it is contention-based, so it's, it's distributed, clearly. And indeed, as we said, we are applying the principles of CSMA/CA. The bad news is that the scheme is similar but not exactly the same as in Wi-Fi.
在这个基于竞争的阶段，它是基于竞争的，所以它是、它是分布式的，显然如此。而且确实，正如我们所说，我们应用的是CSMA/CA的原理。坏消息是，这个方案与Wi-Fi中的方案相似，但并不完全一样。

## 14 · 00:13:49 · 不同需求产生不同接入细节

原标说话人 1  00:13:49
So that's why I was saying it's a bit confusing, because both the terminology and the scheme may be similar. But we have to be a bit careful, because it is not exactly as in Wi-Fi. This is a different system with different requirements, so they designed a different channel access scheme.
所以我才说它有些容易混淆，因为术语和方案可能都相似。不过需要稍微小心，因为它与Wi-Fi并不完全一样。这是一个需求不同的系统，因此设计了不同的信道接入方案。

# 三、时隙CSMA/CA外层停止等待

## 15 · 00:14:16 · 内外模块与发送尝试计数初始化

原标说话人 1  00:14:16
Now the channel access scheme defined as slotted CSMA/CA is defined through an algorithm, and the algorithm includes an inner block and an outer block. So this is the representation, sorry, of the, of the overall, of the overall algorithm. We have some parameters and variables, and here essentially what we represent is the outer block, okay? Now we start by considering a sensor that has got a packet to transmit. So it wants to transmit the packet, access the channel and transmit the packet. Then our sensor first of all needs to initialize this variable called N_f to zero. Okay? Now what is this variable? This variable counts the number of times that a packet is transmitted, because we still have a sort of stop-and-wait mechanism also in this case. So if the packet eventually is transmitted on the channel, but the transmission fails, then our node should again try to access the channel and retransmit the packet, okay? So this variable N_f helps us keep track of how many times we have transmitted the packet. And we already know, according to stop-and-wait, that we have a maximum number of attempts available, okay? After that, the packet has to be discarded. So indeed, if we look at the bottom here, we can already see that this N_f cannot exceed a maximum value.
现在，被称为时隙CSMA/CA的信道接入方案是通过一个算法来定义的，而这个算法包括一个内层模块和一个外层模块。所以，这是这个、这个整体、这个整体算法的表示，抱歉。我们有一些参数和变量，而这里我们所表示的基本上是外层模块，好吗？现在，我们先考虑一个有分组要发送的传感器。所以，它想发送这个分组，接入信道并发送这个分组。那么，我们的传感器首先需要把这个叫作N_f的变量初始化为零。好吗？现在，这个变量是什么？这个变量统计一个分组被发送的次数，因为在这种情况下，我们也仍然采用某种停止等待机制。所以，如果分组最终在信道上发出去了，但发送失败，那么我们的节点就应该再次尝试接入信道并重传这个分组，好吗？所以，这个变量N_f帮助我们记录我们已经发送了这个分组多少次。而且，根据停止等待机制，我们已经知道，我们可用的尝试次数有一个最大值，好吗？超过这个次数，就必须丢弃分组。所以，确实，如果我们看看这里的底部，就已经可以看到，这个N_f不能超过一个最大值。

![图40：Slotted CSMA-CA Procedure: Outer Block](../slide-images/slide-040.png)

课件：04-Sensors-MAC.pdf · PDF第20页下半页 · 图40（按PDF顺序）

## 16 · 00:17:00 · 内层允许发送后等待ACK

原标说话人 1  00:17:00
Okay, this is our maximum number of attempts to transmit a packet. So, so far, nothing new. This is stop-and-wait, right? Okay, now after initializing this variable that counts the number of times a packet has been transmitted over the channel, we enter this inner block. For now let's look at the inner block just as a black box, okay? For now that's enough. And let's focus instead on what outcome we may get from this inner block. Okay? So the possible outcomes are a positive one that says transmit, access the channel and transmit the packet. Okay, good. If we get that outcome, it means that the node can transmit the packet, and then it has to wait for an acknowledgment. If the packet is correctly received, then success. If instead the packet transmission fails, of course we will not get any acknowledgment.
好，这就是我们尝试发送一个分组的最大次数。所以，到目前为止，没有什么新东西。这就是停止等待，对吧？好，现在，在初始化这个统计一个分组已经在信道上发送了多少次的变量之后，我们进入这个内层模块。目前，先让我们只把内层模块看成一个黑盒，好吗？目前，这样就够了。相反，我们来重点看看，我们可能从这个内层模块得到什么结果。好吗？所以，可能的结果包括一个肯定的结果，它说：发送，接入信道并发送这个分组。好，很好。如果我们得到这个结果，那就意味着节点可以发送这个分组，然后它必须等待一个确认。如果这个分组被正确接收，那就是成功。相反，如果分组发送失败，当然，我们就不会得到任何确认。

## 17 · 00:18:35 · 失败后累计尝试次数或丢包

原标说话人 1  00:18:35
We need to try again, right? So we increase the number represented by this variable N_f and check, because if we have reached the maximum number of possible attempts, we need to stop, of course. In that case that's it: we just discard the packet, failure. But if we have not exceeded the maximum number of attempts according to stop-and-wait, we go back, essentially, enter the inner block again and try again. Okay?
我们需要再试一次，对吧？所以，我们增加这个变量N_f所表示的数值，并作检查，因为如果我们已经达到可能的最大尝试次数，当然，我们就需要停止。在那种情况下，就到此为止：我们直接丢弃分组，失败。但是，如果我们尚未超过停止等待机制所规定的最大尝试次数，我们基本上就返回，再次进入内层模块，再试一次。好吗？

## 18 · 00:19:16 · 内层也可能直接返回接入失败

原标说话人 1  00:19:16
So I guess this is relatively easy because in the end it's just a representation of stop-and-wait. Okay, but now let's consider a second possible outcome that we can get from the inner block. Unfortunately, the inner block may also say, ‘Sorry, you cannot, you cannot access the channel. Actually, you have to discard your packet.’ So that's a failure, that's it. Okay? So if we look at the possible outcomes of the inner block, we may have, let's say, a positive outcome, as we said: transmit the packet, access the channel and transmit the packet. Or a total failure: no, just discard the packet, that's it. Okay?
所以，我想这相对容易，因为归根到底，它只是停止等待的一种表示。好，不过现在，我们来考虑能够从内层模块得到的第二种可能结果。不幸的是，内层模块也可能说：“抱歉，你不能，你不能接入信道。实际上，你必须丢弃你的分组。”所以，那就是失败，就这样。好吗？所以，如果我们看看内层模块的可能结果，我们可能会得到，可以说，一个肯定的结果，正如我们所说的：发送分组，接入信道并发送分组。或者，彻底失败：不，直接丢弃分组，就这样。好吗？

## 19 · 00:20:19 · 外层流程总结与深入内层算法

原标说话人 1  00:20:19
So even if at first sight this outer block may seem complicated, it is actually very simple, because if you get permission, let's say, to access the channel and transmit at the output of the inner block, then this representation, this algorithmic representation, is exactly [the phrase is unclear: the original resembles ‘stop-and-wait’, while the independent ASR reads ‘correct’]. If instead you get a negative outcome from the inner block, that's a failure; you discard the packet, okay? So I would say the outer block is very easy. What is a little more complicated instead is the inner block. Okay, so now we need to zoom in, into the inner block, and understand why in certain cases we get as an outcome—let me actually show you the diagram—why in certain cases we get a positive outcome: transmit, access the channel and transmit, send your packet; while in other cases we essentially get a failure, a packet discard.
所以，即使乍一看，这个外层模块可能显得很复杂，它实际上也非常简单，因为如果你在内层模块的输出处得到，可以说，接入信道并发送的许可，那么这种表示，这种算法表示，恰好就是[这句话不清楚：原转写近似“停止等待”，而独立ASR转写为“正确的”]。相反，如果你从内层模块得到一个否定结果，那就是失败；你丢弃分组，好吗？所以，我会说，外层模块非常容易。相对而言，稍微复杂一些的是内层模块。好，所以现在我们需要放大，深入到内层模块中，并且理解为什么在某些情况下，我们得到的结果是——实际上，让我给你们看看这张图——为什么在某些情况下，我们得到一个肯定结果：发送，接入信道并发送，发送你的分组；而在其他情况下，我们基本上得到的是失败，是丢弃分组。

# 四、内层随机退避与信道侦听

## 20 · 00:21:59 · 初始化NB与两时隙侦听窗口

原标说话人 1  00:21:59
So let's look at the algorithm that regulates the inner block. Also in this case we have some parameters and variables that we need to—so variables need to be initialized to some parameters. In particular, we have here a variable that is the number of backoff procedures that we are performing in order to transmit the data. Initially this is set to zero. Then we have—and this is confusing, I know, but unfortunately this is the terminology this is actually a sensing time, okay? A time during which our sensor will have to sense the channel. It's called the contention window, unfortunately, because the meaning is different from the contention window in Wi-Fi. And it's set to two time slots.
所以，我们来看看控制内层模块的算法。在这种情况下，我们也有一些参数和变量，需要把它们——所以，需要用一些参数来初始化变量。具体来说，我们这里有一个变量，它表示我们为了发送数据而执行的退避过程的次数。最初，它被设为零。然后，我们还有——而且这很容易混淆，我知道，不过，不幸的是，术语就是这样这实际上是一段侦听时间，好吗？一段我们的传感器必须侦听信道的时间。不幸的是，它被称为竞争窗口，因为它的含义与Wi-Fi中的竞争窗口不同。而且，它被设为两个时隙。

![图39：Slotted CSMA-CA Algorithm: Variables](../slide-images/slide-039.png)

课件：04-Sensors-MAC.pdf · PDF第20页上半页 · 图39（按PDF顺序）

![图41：Slotted CSMA-CA Procedure: Inner Block](../slide-images/slide-041.png)

课件：04-Sensors-MAC.pdf · PDF第21页上半页 · 图41（按PDF顺序）

## 21 · 00:23:16 · 初始化退避指数BE

原标说话人 1  00:23:16
Okay. And then we have the backoff exponent, which is essentially the same as in Wi-Fi, so that's good news. And it is initialized to the minimum value of the backoff exponent.
好。然后，我们有退避指数，它基本上与Wi-Fi中一样，所以这是好消息。而且，它被初始化为退避指数的最小值。

## 22 · 00:23:36 · 同步系统在时隙边界采取动作

原标说话人 1  00:23:36
Okay, now remember we are in a synchronized system, right? And we act on the basis of this time division. So what we need to do is, first of all, remember we have the node that has got a packet to transmit; it has entered the inner block. After initializing, initializing these variables, it will wait for the beginning of a time slot. Any action that is taken is taken at the beginning of a time slot, because the system is synchronized.
好，现在记住，我们处在一个同步系统中，对吧？而且，我们依据这种时间划分来行动。所以，我们需要做的是，首先，记住，我们有一个节点，它有分组要发送；它已经进入了内层模块。在初始化、初始化这些变量之后，它会等待一个时隙的开始。所采取的任何动作，都是在一个时隙的开始时采取的，因为系统是同步的。

## 23 · 00:24:26 · 等待下一个时隙开始

原标说话人 1  00:24:26
So we don't do anything asynchronously. We say, if we do something, we always do it at the beginning of a time slot. Okay, so first of all, wait for the beginning of a time slot.
所以，我们不会异步地做任何事情。我们说，如果我们做什么，我们总是在一个时隙的开始时做。好，所以，首先，等待一个时隙的开始。

## 24 · 00:24:44 · 退避周期术语与随机退避计算

原标说话人 1  00:24:44
The problem here in terms of terminology, again, is not a conceptual problem; it's in terms of terminology. The time slot in this kind of system is called the backoff period. Sorry, but this is how it is called. So forget about what the backoff period was in Wi-Fi, okay? This is essentially—you have to read this as ‘time slots’, okay? So first of all, what you do once you identify the beginning of the next time slot, you draw a random integer between zero and two to the power of the backoff exponent, minus one. Then you multiply this random integer, drawn with equal probability as in Wi-Fi, by the time-slot duration, which, as I said, is now called the backoff period. But it is the time-slot duration. So this step essentially corresponds to drawing a random backoff time in Wi-Fi. It's exactly the same thing.
再说一次，这里在术语方面的问题，不是一个概念问题；它是一个术语方面的问题。这类系统中的时隙被称为退避周期。抱歉，不过，它就是这么叫的。所以，忘掉Wi-Fi中的退避周期原来是什么，好吗？这基本上是——你们必须把这里理解为“时隙”，好吗？所以，首先，一旦你确定了下一个时隙的开始，你所做的就是，在零和二的退避指数次方、减一之间，抽取一个随机整数。然后，你把这个像Wi-Fi中一样以相等概率抽取的随机整数，乘以时隙时长，而正如我所说，时隙时长现在被称为退避周期。不过，它就是时隙时长。所以，这一步基本上对应于在Wi-Fi中抽取一个随机退避时间。这是完全相同的事情。

## 25 · 00:26:08 · 先连续退避再执行信道侦听

原标说话人 1  00:26:08
Notice that this is the very, very first thing that we do. So in sensor networks, if you get a packet, the first thing you have to do is to draw a backoff. Okay, now we have our backoff set, and what we are going to do is decrease this backoff counter continuously. So it's simpler than in Wi-Fi, because we don't mind about the state of the channel. If the channel is idle, if the channel is busy, we don't care. We just decrease the backoff counter continuously. When the backoff counter reaches zero, however, in this case we cannot access the channel and transmit; we need to sense the channel. So again, at the beginning of the time slot, here called the backoff period, we start sensing the channel.
注意，这是我们所做的最、最先的一件事。所以，在传感器网络中，如果你有了一个分组，你必须做的第一件事，就是抽取一个退避值。好，现在我们已经设好了退避值，而我们接下来要做的，是连续地递减这个退避计数器。所以，它比Wi-Fi中更简单，因为我们不在意信道的状态。如果信道空闲，如果信道忙，我们都不在意。我们只是连续地递减退避计数器。不过，当退避计数器到零时，在这种情况下，我们不能接入信道并发送；我们需要侦听信道。所以，同样，在一个时隙的开始，也就是这里所说的退避周期的开始，我们开始侦听信道。

## 26 · 00:27:22 · 两次空闲侦听及忙时重设变量

原标说话人 1  00:27:22
If the channel is idle, fine; we keep sensing the channel for how many time slots? Two time slots, right? Because CW is set to two. If the channel is idle for this time, this sensing time, then we can access the channel. After this time of two time slots, if the channel was idle, we can just access the channel and transmit the packet. If instead, while sensing the channel—and notice that this is physical-layer sensing, okay, a clear channel assessment function implemented by the physical layer, it's physical-layer sensing—if the channel while sensing is detected as busy, so not idle, then we need to reset the sensing time to two increase NB, the number of backoff procedures, and then also increase the backoff exponent, and go back to the backoff procedure if possible, because we cannot run the backoff for a packet more than a given maximum number of times. [Editorial note: Resetting the value to two is inferred from the CW setting; this short phrase is unclear in the ASR.]
如果信道空闲，很好；我们继续侦听信道，要侦听多少个时隙？两个时隙，对吧？因为CW被设为二。如果信道在这段时间、这段侦听时间内空闲，那么我们就可以接入信道。在这两个时隙的时间之后，如果信道一直空闲，我们就可以直接接入信道并发送分组。相反，如果在侦听信道的时候——而且要注意，这是物理层侦听，好吗，是一个由物理层实现的空闲信道评估功能，它是物理层侦听——如果在侦听时，检测到信道忙，也就是不空闲，那么我们就需要把侦听时间重新设为二增加NB，也就是退避过程的次数，然后还要增加退避指数，并且，如果可能的话，就返回退避过程，因为对于一个分组，我们运行退避过程的次数不能超过一个给定的最大次数。[校对说明：将数值重新设为二是依据CW设置作出的推定；这段短语在ASR中不清楚。]

## 27 · 00:29:13 · 内层重试次数耗尽导致丢包

原标说话人 1  00:29:13
Okay? So if we still have the possibility to run another backoff procedure, we go back and draw a new random number, essentially. When we hit the maximum number of backoff procedures that we have performed within this inner loop, inner block, we cannot do anything else. We get out of the inner block with outcome failure, and the packet is discarded. So within the inner block, essentially, to summarize, first of all we perform the backoff. That's the very first thing we do. Perform the backoff, decrease it continuously. When you reach zero, sense the channel. If the channel is idle, transmit. If the channel is sensed as busy, then you cannot transmit. Of course you have to defer your transmission. How do we do that? By going back and running the backoff again. This is, in a nutshell, okay? As we said, we can also get out of this inner block with a failure outcome, and that happens when we have tried, tried, tried to sense the channel as idle. But unfortunately every time we have performed this procedure, we have found the channel busy, and we do not have any more backoff procedures essentially available. So at that point we exit this block with a failure outcome. [Editorial note: “In a nutshell” is a contextual inference; the exact short phrase is unclear.]
好吗？所以，如果我们仍然有可能再运行一次退避过程，我们就返回，基本上，抽取一个新的随机数。当我们已经执行的退避过程次数达到最大值时在这个内层循环、内层模块中，我们就不能再做任何别的事情了。我们以失败的结果退出内层模块，而这个分组被丢弃。所以，在内层模块中，基本上，总结一下，首先我们执行退避。这是我们做的第一件事。执行退避，连续地递减它。当你到达零时，侦听信道。如果信道空闲，就发送。如果侦听到信道忙，那么你就不能发送。当然，你必须推迟你的发送。我们怎么做呢？通过返回并再次运行退避。这就是简而言之的情况，好吗？正如我们所说，我们也可能以失败的结果退出这个内层模块，而那发生在我们尝试过、尝试过、尝试过，想要侦听到信道空闲的时候。不过，不幸的是，每次我们执行这个过程，都发现信道忙，而且我们基本上已经没有更多可用的退避过程次数了。所以，在那一点上，我们以失败的结果退出这个模块。[校对说明：“简而言之”是根据上下文作出的推定；这段短语的确切措辞不清楚。]

![图42：Slotted CSMA-CA Algorithm: Inner Block summary](../slide-images/slide-042.png)

课件：04-Sensors-MAC.pdf · PDF第21页下半页 · 图42（按PDF顺序）

## 28 · 00:31:29 · 内外层串联后的成功发送流程

原标说话人 1  00:31:29
So, going back to our inner—sorry, outer—block here, we can now see that whenever a node has got a packet to transmit, it will essentially enter the inner block. Inside the inner block, now we know that first of all we have to perform the backoff, then sense the channel. If the channel is idle, the outcome is transmit. Okay? Then we have an acknowledgment if the packet is correctly received, and success.
所以，回到我们这里的内层——抱歉，外层——模块，现在我们可以看到，每当一个节点有分组要发送时，它基本上就会进入内层模块。在内层模块内部，现在我们知道，首先我们必须执行退避，然后侦听信道。如果信道空闲，结果就是发送。好吗？然后，如果这个分组被正确接收，我们就有一个确认，并且成功。

## 29 · 00:32:13 · 区分发送重试与接入退避重试

原标说话人 1  00:32:13
If the packet is not received correctly, then according to the maximum number of stop-and-wait attempts, we may have the possibility to try again. If not, of course we have to discard it. If we try again, we go again into the inner block, and here again we start with the backoff, we sense the channel. Unfortunately we may, you know, loop, cycle inside this inner block many times if we cannot find the channel idle, right? So if we find the channel busy inside the inner block, we will run, we need to run several backoff procedures. And if eventually we find the channel idle, then okay, we can get out and transmit. But otherwise, if we hit the maximum number of backoff procedures allowed and have not been able to access the channel, that's a failure.
如果这个分组没有被正确接收，那么，根据停止等待的最大尝试次数，我们可能还有机会再试一次。如果没有，当然，我们就必须丢弃它。如果我们再试一次，我们就再次进入内层模块，而且在这里，我们又从退避开始，再侦听信道。不幸的是，如果我们找不到空闲信道，我们可能，你们知道，在这个内层模块中循环、循环很多次，对吧？所以，如果我们在内层模块中发现信道忙，我们就会运行，我们需要运行好几次退避过程。而如果最终我们发现信道空闲，那么，好，我们就可以退出并发送。不过，反过来，如果我们达到允许的最大退避过程次数，而且还未能接入信道，那就是失败。

## 30 · 00:33:30 · 每次重入内层重新初始化NB

原标说话人 1  00:33:30
So it is not actually difficult. The only thing I would like to, to remark about the inner block, one more thing, is this: notice that every time we enter the inner block again, we reset the number of backoff procedures performed to zero. So every time we enter the inner block, we reset the counter of the backoff procedures. That means that we will have this maximum number of backoff procedures available, okay? Every time we enter the inner block. And as we already said, but let me remark that we re-enter the inner block every time we actually transmit a packet on the channel. So if we actually transmit the packet on the channel and do not receive any ACK, we get into the inner block again, and we are allowed to reset the number of available backoff procedures. Okay.
所以，它实际上并不难。我想要、想要就内层模块强调的唯一一点，还有一点，就是这个：注意，每次我们再次进入内层模块时，我们都会把已执行的退避过程次数重新设为零。所以，每次我们进入内层模块，我们都会重设退避过程的计数器。这意味着，我们将有这个最大次数的退避过程可用，好吗？每次我们进入内层模块的时候。而且，正如我们已经说过的，不过，让我再强调一下，每次我们实际在信道上发送一个分组时，我们都会重新进入内层模块。所以，如果我们实际在信道上发送了分组，却没有收到任何ACK，我们就再次进入内层模块，并且允许我们重新设置可用的退避过程次数。好。

![图44：Remarks: Failure Handling](../slide-images/slide-044.png)

课件：04-Sensors-MAC.pdf · PDF第22页下半页 · 图44（按PDF顺序）

## 31 · 00:35:11 · 建议结合流程图反复复习

原标说话人 1  00:35:11
Now this may seem complicated, but trust me, it is not. So once you review it a couple of times, you will see that it is actually a simple, simple algorithm, and usually students do not have any difficulty with, with this one. So it is not as bad as it looks at first sight.
现在，这可能看起来很复杂，不过相信我，它并不复杂。所以，一旦你们复习过几遍，就会看到，它实际上是一个简单、简单的算法，而且通常，同学们对、对这一个算法都没有什么困难。所以，它并没有乍看之下那么糟。

## 32 · 00:35:43 · 关于RTS和CTS扩展的课堂补充

原标说话人 1  00:35:43
Let me also mention that in this kind of access we may also have RTS and CTS. So we presented the, the algorithm, let's say, in the easiest version without RTS and CTS, but potentially you can also use RTS and CTS.
也让我提一下，在这种接入方式中，我们也可能有RTS和CTS。所以，我们介绍的是这个、这个算法，可以说，最简单的版本，没有RTS和CTS，不过，也有可能使用RTS和CTS。

# 五、ACK与半双工收发切换

## 33 · 00:36:09 · 以汇聚节点和传感器说明竞争期

原标说话人 1  00:36:09
The other, the other thing I would like to mention is to consider, for example, a sink and a sensor. So you can think of the sink also as our PAN coordinator, the one that provides this synchronization. Now we are inside the contention period. So when the coordinator works in beacon-enabled mode, during the contention period we are applying this kind of slotted CSMA/CA.
另外、另外一件我想提到的事，是考虑一下，例如，一个汇聚节点和一个传感器。所以，你们也可以把汇聚节点看作我们的PAN协调器，就是提供这种同步的那个节点。现在，我们处在竞争期内。所以，当协调器工作在信标使能模式时，在竞争期内，我们应用的是这种时隙CSMA/CA。

## 34 · 00:37:04 · 取得接入机会后执行停止等待

原标说话人 1  00:37:04
So let me just consider the case where—okay, we know that a sensor with a packet has to run all these steps of the algorithms of the inner and outer blocks. But let me just consider that at a certain point in time our sensor can transmit its data packet on the channel. Okay, and we said, well, in this case we are applying stop-and-wait, right?
所以，让我只考虑这样一种情况——好，我们知道，一个有分组的传感器必须执行内层和外层模块算法的所有这些步骤。不过，让我只考虑，在某个时刻，我们的传感器能够在信道上发送它的数据分组。好，而且我们说过，嗯，在这种情况下，我们采用的是停止等待，对吧？

## 35 · 00:37:37 · 正确接收后经SIFS发送ACK

原标说话人 1  00:37:37
And if the sink receives the data correctly, it will send back the acknowledgment. Otherwise the acknowledgment clearly is not there. Okay. One thing we need to say is that this acknowledgment will be sent back by the access point after a time that is again called SIFS, okay?
而如果汇聚节点正确收到数据，它就会发回确认。否则，显然就不会有确认。好。我们需要说的一点是，这个确认将由接入点在一段同样被称为SIFS的时间之后发回，好吗？

## 36 · 00:38:15 · SIFS用于半双工收发切换

原标说话人 1  00:38:15
And during this SIFS, the—sorry, access point—the sink, the sink, during this SIFS performs the turnaround of its transceiver. Also in this case our nodes are half-duplex. They cannot transmit and receive at the same time.
而在这个SIFS期间，这个——抱歉，接入点——汇聚节点，汇聚节点，在这个SIFS期间执行其收发器的模式切换。在这种情况下，我们的节点同样是半双工的。它们不能同时发送和接收。

## 37 · 00:38:35 · 单收发器从接收转向发送

原标说话人 1  00:38:35
They are very simple nodes with only one transceiver, and therefore, after receiving this data packet, the sink will turn around its transceiver from receive mode to transmit mode and then transmit the ACK.
这些节点很简单，只有一个收发器。因此收到数据分组后，汇聚节点会把收发器从接收模式切换到发送模式，然后发送ACK。

## 38 · 00:38:58 · 简单设备较长SIFS及ACK后等待

原标说话人 1  00:38:58
The peculiarity is that since these are very simple devices, okay, less sophisticated than Wi-Fi cards, much less sophisticated, they take much longer to perform this turnaround of the transceiver. So as we will see from numerical examples, this SIFS is now, for example, 192 microseconds, okay? It was ten microseconds in the—sorry, it was twenty microseconds in Wi-Fi. So you can see that it's much, much longer. And the last thing I would like to mention is that after the sink has transmitted an acknowledgment, it will be able to receive signals only after SIFS.
这里的特点是，由于这些都是非常简单的设备，好吗，比Wi-Fi网卡更简单，简单得多，所以它们执行这种收发器切换所花费的时间要长得多。因此，正如我们将从数值例子中看到的，现在这个SIFS，例如，是192微秒，好吗？它原来是10微秒，在——抱歉，在Wi-Fi中，它是20微秒。所以，你们可以看到，它长得多、长得多。而我想提到的最后一点是，在汇聚节点发送完一个确认之后，它只有在经过SIFS之后才能接收信号。

![图43：Remarks: Backoff and Timings](../slide-images/slide-043.png)

课件：04-Sensors-MAC.pdf · PDF第22页上半页 · 图43（按PDF顺序）

## 39 · 00:40:03 · ACK后切换期间汇聚节点无法接收

原标说话人 1  00:40:03
Because again, here it is transmitting, right? If we want the sink to be able to receive something else, we have to wait again for this SIFS, because it again has to turn around its transceiver from receive mode—sorry, from transmit mode, where it transmits the ACK—to receive mode. So during this time, SIFS after the acknowledgment, the sink cannot receive anything. If any sensor tries to transmit something during this time, it will not be received correctly, okay? Because during this time the sink cannot do anything; it is just again performing the turnaround of its transceiver. Okay, good. So let's stop for five minutes, and then we are going to see the last scheme. Ah, the last scheme.
因为，同样，这里它正在发送，对吧？如果我们想让汇聚节点能够接收别的东西，我们就必须再次等待这个SIFS，因为它又必须把收发器从接收模式——抱歉，是从发送模式，也就是它发送ACK时的模式——切换到接收模式。所以，在这段时间内，也就是确认之后的SIFS期间，汇聚节点不能接收任何东西。如果任何传感器试图在这段时间内发送什么，这些内容就不会被正确接收，好吗？因为在这段时间内，汇聚节点不能做任何事情；它只是在再次执行收发器的切换。好，很好。所以，我们休息五分钟，然后我们将看看最后一种方案。啊，最后一种方案。

# 六、非时隙CSMA/CA及丢包条件

## 40 · 00:47:14 · 无信标模式与相同的外层流程

原标说话人 1  00:47:14
Okay, so let's resume our class. Now the very last thing we need to look at is the case where we have no beacons. In this possibility the coordinator, the PAN coordinator, will still be there, but it will not issue beacons. So in this case we do not have superframes. The only way for our sensors to access the channel is to use so-called unslotted CSMA/CA. ‘Unslotted’ emphasizes that now we may not have synchronization among the nodes as we had previously when beacons were enabled. The result is a slightly different scheme, indeed unslotted CSMA/CA, which is essentially simpler than the one we saw before. So very, very similar; it's just simpler. So this is, I think, easy to explain. Again we have the outer block and inner block, the same structure of the algorithm. And again the good news is that the outer block is exactly the same as before, exactly the same. Consider a sensor that has got a packet to transmit. First, in the outer block, it initializes the number of transmissions performed for a packet to zero. It will enter the inner block. Again, as the outcome of the inner block, we have a possible positive outcome that says ‘access the channel and transmit’, or a negative, very negative outcome: ‘failure, discard the packet’. If the outcome is ‘access the channel and transmit’, then if the packet is received correctly, we have an acknowledgment, success, we are done and happy. If instead the packet is not successfully transmitted, the ACK of course is not there. If we still have attempts available to access the channel according to stop-and-wait, we can do that by going back to the inner block. If instead we have reached the maximum number of transmission attempts allowed by stop-and-wait, failure: discard the packet. Okay, this is exactly as before. So we may now take the opportunity to emphasize that there are two situations under which we may fail, two causes that may determine packet discard.
好，所以我们继续上课。现在，我们需要看的最后一件事，就是没有信标的情况。在这种可能的情况下，协调器，PAN协调器，仍然会存在，但它不会发出信标。所以，在这种情况下，我们没有超帧。我们的传感器接入信道的唯一方式，是使用所谓的非时隙CSMA/CA。“非时隙”强调的是，现在节点之间可能没有像之前信标使能时那样的同步。结果是一种略有不同的方案，确实就是非时隙CSMA/CA，它基本上比我们之前看到的方案更简单。所以，非常、非常相似；它只是更简单。所以，我认为，这很容易解释。同样，我们有外层模块和内层模块，算法的结构相同。而且，同样，好消息是，外层模块与之前完全一样，完全一样。考虑一个有分组要发送的传感器。首先，在外层模块中，它把为一个分组执行的发送次数初始化为零。它将进入内层模块。同样，作为内层模块的结果，我们可能得到一个肯定的结果，它说“接入信道并发送”，或者一个否定的、非常否定的结果：“失败，丢弃分组”。如果结果是“接入信道并发送”，那么，如果分组被正确接收，我们就有一个确认，成功，我们完成了，也很高兴。相反，如果分组没有成功发送，当然就没有ACK。如果根据停止等待机制，我们仍然有可用的接入信道尝试次数，我们就可以返回内层模块来进行尝试。相反，如果我们已经达到停止等待机制允许的最大发送尝试次数，那就是失败：丢弃分组。好，这和之前完全一样。所以，我们现在可以借此机会强调，有两种情况下我们可能失败，有两个可能导致分组丢弃的原因。

![图45：No Beacon-enabled Mode](../slide-images/slide-045.png)

课件：04-Sensors-MAC.pdf · PDF第23页上半页 · 图45（按PDF顺序）

![图47：Unslotted CSMA-CA: Outer Block](../slide-images/slide-047.png)

课件：04-Sensors-MAC.pdf · PDF第24页上半页 · 图47（按PDF顺序）

## 41 · 00:51:11 · 接入失败和重传耗尽两类丢包

原标说话人 1  00:51:11
One is when we exit the inner block with a negative outcome; that's a possible cause of packet discard. The second is the, let's say, standard one, traditional one: when we exceed the maximum number of transmission attempts fixed by stop-and-wait, we know that we have to discard the packet. Okay, this is the usual cause why we need to discard a packet. But as we said, there is also this additional reason why we may need to discard the packet in this case: the negative outcome of the inner block. So this is a further observation that clearly also holds for slotted CSMA/CA, because the outer block is exactly the same in both cases, slotted and unslotted. What changes a bit instead is the inner block, as you—
一种情况是，我们以否定的结果退出内层模块；那是可能导致分组丢弃的一个原因。第二种是，可以说，标准的、传统的那一种：当我们超过停止等待所规定的最大发送尝试次数时，我们知道，我们必须丢弃分组。好，这就是我们通常需要丢弃一个分组的原因。不过，正如我们所说，在这种情况下，我们可能需要丢弃分组，还有这个额外的原因：内层模块的否定结果。所以，这是一个进一步的观察，显然，它也适用于时隙CSMA/CA，因为在时隙和非时隙这两种情况下，外层模块是完全一样的。相反，稍有变化的是内层模块，就像你们——

![图52：Remarks: Failure Handling (unslotted)](../slide-images/slide-052.png)

课件：04-Sensors-MAC.pdf · PDF第26页下半页 · 图52（按PDF顺序）

## 42 · 00:52:33 · 非时隙内层无需等待时隙边界

原标说话人 1  00:52:33
So what changes in the inner block? You can immediately see that it is actually much simpler, right? There are fewer blocks, fewer arrows in the flow diagram. At the beginning we have the initialization step; we just initialize the variables we need to use in the algorithm. And again the first thing we do is run the backoff, again the very first thing when we enter the inner block. However, in this case the backoff is run in an easier way, meaning that the nodes are not synchronized, right? So we don't need to perform actions at the beginning of a time slot, which we called a backoff period. We can take action at any time, okay? Whenever we start contending for the channel, it's fine. We don't have to wait and act only at the beginning of a time slot. As soon as we enter this inner block, we run the backoff. No waiting for the start of a time slot now.
所以，内层模块有什么变化？你们马上就能看到，它实际上简单得多，对吧？流程图中的模块更少，箭头也更少。开始时，我们有初始化步骤；我们只是初始化在算法中需要使用的变量。而且，同样，我们做的第一件事是运行退避，同样，是我们进入内层模块时做的第一件事。不过，在这种情况下，退避以一种更简单的方式运行，意思是，节点没有同步，对吧？所以，我们不需要在一个时隙，也就是我们称为退避周期的开始时执行动作。我们可以在任何时候采取动作，好吗？无论什么时候开始竞争信道，都可以。我们不必等待，也不必只在时隙开始时行动。一旦我们进入这个内层模块，我们就运行退避。现在不用等待时隙的开始。

![图46：Unslotted CSMA-CA Algorithm: Variables](../slide-images/slide-046.png)

课件：04-Sensors-MAC.pdf · PDF第23页下半页 · 图46（按PDF顺序）

![图48：Unslotted CSMA-CA: Inner Block flow](../slide-images/slide-048.png)

课件：04-Sensors-MAC.pdf · PDF第24页下半页 · 图48（按PDF顺序）

## 43 · 00:54:05 · 连续退避结束后进行CCA

原标说话人 1  00:54:05
We decrease the backoff, which is computed essentially in the same way as before. We draw the random integer, multiply it by the backoff period, which is now our time-slot duration, and get our backoff time. And then we continuously decrease the backoff counter. No matter what the status of the channel is, we don't care. We decrease it. When the backoff counter reaches zero, we perform sensing at the physical layer for a time that is called CCA; it's the sensing time.
我们递减退避值，它的计算方式基本上与之前相同。我们抽取这个随机整数，把它乘以退避周期，也就是现在我们的时隙时长，然后得到我们的退避时间。然后我们连续地递减退避计数器。不管信道的状态是什么，我们都不在意。我们递减它。当退避计数器到零时，我们在物理层执行侦听，持续一段被称为CCA的时间；这就是侦听时间。

## 44 · 00:54:52 · 侦听结果、重试限制与双向SIFS

原标说话人 1  00:54:52
If the channel is idle, transmit. If the channel is busy and we have not exceeded the maximum number of backoff procedures for that packet, try again by running the backoff. Of course if we always find the channel busy and have run out of available backoff procedures, then we have a negative outcome from this block, and that's a failure; we need to discard the packet. Also in this case, when we have an acknowledgment, the data packet and the acknowledgment will be spaced by SIFS. Again this SIFS is the same as before, so quite long, because, as we said, these are simple devices. They are slow, so performing the turnaround of the transceiver takes time, okay? As before, after the acknowledgment the sink again needs some time to turn around its transceiver before being able to receive another packet. Because here it was transmitting the acknowledgment, before it can receive, it needs to perform this turnaround, and that will again take SIFS.
如果信道空闲，就发送。如果信道忙，而且我们没有超过针对这个分组的最大退避过程次数，就通过运行退避再试一次。当然，如果我们总是发现信道忙，而且已经用尽了可用的退避过程次数，那么我们从这个模块得到的就是一个否定结果，而那就是失败；我们需要丢弃分组。同样，在这种情况下，当我们有一个确认时，数据分组和确认之间将相隔SIFS。同样，这个SIFS与之前一样，所以相当长，因为，正如我们所说，这些是简单的设备。它们速度慢，所以执行收发器切换需要时间，好吗？和之前一样，在确认之后，汇聚节点还需要一些时间来切换其收发器，然后才能接收另一个分组。因为这里它原本在发送确认，在能够接收之前，它需要执行这种切换，而那又将需要SIFS。

![图49：Unslotted CSMA-CA: Inner Block summary](../slide-images/slide-049.png)

课件：04-Sensors-MAC.pdf · PDF第25页上半页 · 图49（按PDF顺序）

![图50：Remarks: same observations](../slide-images/slide-050.png)

课件：04-Sensors-MAC.pdf · PDF第25页下半页 · 图50（按PDF顺序）

![图51：Remarks: Backoff and Timings (unslotted)](../slide-images/slide-051.png)

课件：04-Sensors-MAC.pdf · PDF第26页上半页 · 图51（按PDF顺序）

## 45 · 00:56:39 · ACK后的SIFS内发送会失败

原标说话人 1  00:56:39
If anything is sent to the sink during this SIFS time after the ACK, it will be lost, it will not be received correctly, because the sink is not essentially available yet, ready yet, to receive. That's it with that. Okay, good.
如果在ACK之后的这段SIFS时间内，有任何东西发送到汇聚节点，它就会丢失，它不会被正确接收，因为汇聚节点基本上还不可用，还没有准备好接收。这个就讲到这里。好，很好。

# 七、答疑：CSMA/CA、DCF与退避

## 46 · 00:57:03 · 结束传感器MAC并进入复习答疑

原标说话人 1  00:57:03
So now, since we are done with channel access for sensor networks, let's move to, let's say, the review session. If you have any questions or any points that are unclear, let's review them. Then we go back again to the sensors for some numerical examples. But first let's make sure we clarify the doubts and questions we have so far. Okay? So now—
所以现在，既然我们已经讲完了传感器网络的信道接入，我们就转到，可以说，复习环节。如果你们有任何问题，或者任何不清楚的地方，我们就来回顾一下。然后，我们再回到传感器，做一些数值例子。不过，首先，我们要确保澄清到目前为止的疑惑和问题。好吗？所以现在——

## 47 · 00:57:46 · 同学说明已收集问题

原标说话人 2  00:57:46
We have collected [the rest of this fragment is unclear].
我们已经收集了[这个片段的其余部分不清楚]。

## 48 · 00:57:50 · 邀请课堂提问

原标说话人 1  00:57:50
Sure, please. The questions from the classroom. Yeah, thanks, please.
当然，请。来自课堂的问题。好的，谢谢，请。

## 49 · 00:58:04 · 准备从第一个问题开始

原标说话人 1  00:58:04
Starting from—okay, shall we start from the first one? Okay, so you can read the questions, so, or essentially—
从——好，我们从第一个开始吗？好，所以，你们可以读一下这些问题，所以，或者，基本上——

## 50 · 00:58:18 · 关于DCF加退避的提问

原标说话人 2  00:58:18
DCF plus backoff?
DCF加上退避？

## 51 · 00:58:21 · CSMA/CA作为一般接入原理

原标说话人 1  00:58:21
Okay, so let me—thanks—let me clarify that. CSMA/CA is a general principle, okay? That means carrier-sense multiple access plus collision avoidance. So what do I mean by a general principle? Meaning that it's an approach, a type of approach to access the channel at the MAC layer. That means we are using carrier-sense multiple access as an approach: whenever we have something to transmit, we need to sense the channel as idle. That's the approach, right? If the channel is idle, we transmit. If the channel is busy, we need to defer the transmission. That is carrier-sense multiple access. Okay, it's a type of approach.
好，所以，让我——谢谢——让我澄清一下。CSMA/CA是一种一般原理，好吗？它的意思是载波侦听多路访问加上冲突避免。所以，我说“一般原理”是什么意思呢？意思是，它是一种方法，一种在MAC层接入信道的方法。那意味着，我们采用载波侦听多路访问作为一种方法：每当我们有东西要发送时，我们需要侦听到信道空闲。这就是这种方法，对吧？如果信道空闲，我们就发送。如果信道忙，我们就需要推迟发送。这就是载波侦听多路访问。好，它是一种方法。

## 52 · 00:59:28 · 空闲发送与忙时推迟的基本原则

原标说话人 1  00:59:28
That is exactly what I said now. When you have a packet to transmit, first sense the channel. If the channel is idle, you can transmit. If the channel is busy, you need to defer your transmission.
这正是我刚才所说的。当你有一个分组要发送时，首先侦听信道。如果信道空闲，你就可以发送。如果信道忙，你就需要推迟你的发送。

## 53 · 00:59:44 · 引导比较CSMA和DCF

原标说话人 1  00:59:44
Okay. Now what do you think? Is this DCF? Is it exactly DCF? But if you think of DCF, what do you think about? What comes to your mind? If I say DCF, what are you thinking about immediately? ‘For exercise examples.’ Sorry? ‘For exercise examples.’
好。现在，你们怎么看？这是DCF吗？它恰好就是DCF吗？不过，如果你们想到DCF，你们会想到什么？脑海里会浮现什么？如果我说DCF，你们会立刻想到什么？“练习例子。”抱歉，什么？“练习例子。”

## 54 · 01:00:13 · 回顾节点拿到分组后的首个动作

原标说话人 1  01:00:13
Exactly, where—it's good—where we had the nodes doing what? ‘Backoff.’ Not really. I mean, also backoff, but later. That was probably not the very first thing they did. What was the first thing they were doing?
没错，那里——很好——在那里，我们有节点在做什么？“退避。”不完全是。我的意思是，也有退避，不过是在后面。那很可能不是它们所做的第一件事。它们所做的第一件事是什么？

## 55 · 01:00:38 · CSMA原则与DCF的DIFS细节

原标说话人 1  01:00:38
[A short answer is unclear.] No, that's collision avoidance. So backoff and so forth is collision avoidance, but now we are focusing on CSMA, right? Carrier-sense multiple access. Think of the numerical problems, examples. What was a node doing when it got a packet from the higher layers? The first thing was to sense, carrier sensing; we need to sense the channel. Okay, but what you think about is this action of sensing, and you may actually visualize that the sensing was for how long? DIFS, right? So DCF is a particular channel access scheme that uses the CSMA approach, meaning that CSMA is a general way of behaving: sense the channel; if idle, transmit; if busy, defer transmission. Am I telling you to sense the channel for DIFS? No. If I explain what CSMA is, I just say, sense the channel; if idle, transmit; if busy, defer transmission. That's it.
[一个简短的回答不清楚。]不，那是冲突避免。所以，退避等等属于冲突避免，不过现在，我们重点看的是CSMA，对吧？载波侦听多路访问。想想那些数值题、例子。当一个节点从高层收到一个分组时，它在做什么？第一件事是侦听，载波侦听；我们需要侦听信道。好，不过，你们想到的是这个侦听动作，而且你们实际上可能会在脑海中想象，侦听持续了多长时间？DIFS，对吧？所以，DCF是一个采用CSMA方法的特定信道接入方案，意思是，CSMA是一种一般的行为方式：侦听信道；如果空闲，就发送；如果忙，就推迟发送。我有没有告诉你们，要侦听信道DIFS这么长时间？没有。如果我解释什么是CSMA，我只是说，侦听信道；如果空闲，就发送；如果忙，就推迟发送。就这样。

## 56 · 01:02:28 · 一般原则不规定完整DCF步骤

原标说话人 1  01:02:28
I'm not saying that a node receiving a packet from the higher layers has to sense the channel for DIFS. If the channel is idle for DIFS, then it can access the channel; otherwise it has to perform blah, blah, blah, blah, blah. Okay, see the difference? [Editorial note: The original transcription has five repetitions of “blah”, while the independent ASR has four; the actual number of spoken repetitions is unconfirmed.]
我并没有说，一个从高层收到分组的节点必须侦听信道DIFS这么长时间。如果信道空闲了DIFS这么长时间，那么它就可以接入信道；否则，它就必须执行这个、这个、这个、这个、这个。好，看出区别了吗？[校对说明：原转写有五次“blah”，独立ASR有四次；这里保留原转写中的五次，实际口头重复次数尚未确认。]

## 57 · 01:02:50 · DCF是CSMA原则的具体实现

原标说话人 1  01:02:50
In one case, I'm not just describing the general approach, the general principle of carrier-sense multiple access. In the other case, I'm specifying exactly what a node does, essentially how we apply the general principle of carrier-sense multiple access in Wi-Fi technology. Do you see the difference? So DCF is a specific channel access scheme that makes use of the carrier-sense multiple access approach.
一种情况下，我并不只是在描述一般的方法，载波侦听多路访问的一般原理。在另一种情况下，我在准确规定一个节点做什么，基本上就是，我们如何在Wi-Fi技术中应用载波侦听多路访问的一般原理。你们看出区别了吗？所以，DCF是一个采用载波侦听多路访问方法的具体信道接入方案。

## 58 · 01:03:33 · DCF已包含退避且不同于传感器方案

原标说话人 1  01:03:33
But it's a specific technology. That means you specify exactly what the Wi-Fi cards do, okay? For example, when we said that the access point, in order to transmit the beacon, will have to sense the channel as idle for PIFS, right? It's still carrier-sense multiple access, an application of the general principle. But DCF specifies that if you need to transmit a data packet, you have to sense the channel for DIFS. If instead you are the access point and need to transmit the beacon, you need to sense the channel as idle for PIFS, right? So that's a very detailed specification of how to apply the general principle. Saying that CSMA/CA, for example, is DCF plus backoff is not accurate, okay? CSMA and also CA, collision avoidance, are general approaches. DCF is the specific channel access scheme that details how nodes behave in different situations. It applies the general principle, but it's a specific channel access scheme. Indeed, with sensors, for example here, we said we're also applying carrier-sense multiple access with collision avoidance, right? But is this the same as DCF? No, it's different. Okay, see the difference? The other thing: DCF is indeed a channel access scheme that includes the backoff mechanism. So saying ‘DCF plus backoff’ does not make sense. The backoff is a mechanism that is part of DCF.
不过，它是一种具体的技术。那意味着，你要准确规定Wi-Fi网卡做什么，好吗？例如，我们说过，接入点为了发送信标，必须侦听到信道空闲了PIFS这么长时间，对吧？这仍然是载波侦听多路访问，是一般原理的一种应用。不过，DCF规定，如果你需要发送一个数据分组，你必须侦听信道DIFS这么长时间。相反，如果你是接入点，而且需要发送信标，你就需要侦听到信道空闲了PIFS这么长时间，对吧？所以，这是对如何应用一般原理的一个非常详细的规定。比如说，说CSMA/CA就是DCF加上退避，这是不准确的，好吗？CSMA以及CA，也就是冲突避免，都是一般的方法。DCF是一个具体的信道接入方案，它详细规定节点在不同情况下如何行动。它应用一般原理，不过，它是一个具体的信道接入方案。确实，以传感器为例，比如这里，我们说过，我们同样应用带冲突避免的载波侦听多路访问，对吧？不过，这和DCF一样吗？不，它不一样。好，看出区别了吗？另一件事：DCF确实是一个包括退避机制的信道接入方案。所以，说“DCF加上退避”是没有意义的。退避是一个机制，是DCF的一部分。

## 59 · 01:05:59 · 冲突避免目标与具体退避步骤

原标说话人 1  01:05:59
The backoff is there as a mechanism, as a procedure, in order to avoid collisions. But again, collision avoidance is a general approach. As the name says, you try to avoid collisions. Very vague, okay? The backoff procedure tells you: sense the channel for DIFS, then draw a random integer with equal probability out of this range of values, then multiply the integer by the time-slot duration.
退避作为一种机制、作为一个过程而存在，是为了避免冲突。不过，同样，冲突避免是一种一般的方法。正如这个名字所说，你试图避免冲突。很模糊，好吗？退避过程会告诉你：侦听信道DIFS这么长时间，然后从这个取值范围内以相等概率抽取一个随机整数，然后把这个整数乘以时隙时长。

## 60 · 01:06:39 · Wi-Fi退避递减、冻结和恢复规则

原标说话人 1  01:06:39
Then set the counter to that value, then decrease the counter to zero as long as the channel is idle. If the channel gets busy, you have to freeze the counter. Then you can resume decreasing the counter after you sense the channel as idle for DIFS. When the counter reaches zero, you can transmit the data packet.
然后把计数器设为那个值，然后，只要信道空闲，就递减计数器直到零。如果信道变忙，你必须冻结计数器。然后，在你侦听到信道空闲了DIFS这么长时间之后，你就可以恢复递减计数器。当计数器到零时，你就可以发送数据分组。

## 61 · 01:07:00 · 不同系统用不同退避机制避免碰撞

原标说话人 1  01:07:00
So if I say ‘collision avoidance’ like that, do you understand all this? I don't think so, right? So collision avoidance is a general principle. Backoff is specific. It's a specific mechanism; in particular, in Wi-Fi, the Wi-Fi backoff is a specific mechanism that works according to certain rules, whose goal is to avoid collisions. But it's a specific mechanism that is part of the DCF channel access scheme. And indeed, again, also in this case, we do have backoff, right? And backoff is there for the same reason: try and avoid collisions, try to desynchronize contending sensors that need to access the channel. But is this collision-avoidance procedure the same as in Wi-Fi? No. Similar, but it's not the same. Okay, good. If it's clear, we can move to the next. [Editorial note: “Desynchronize” is inferred from context; the independent ASR reads “synchronize”.]
所以，如果我就这样说“冲突避免”，你们能理解所有这些吗？我想不能，对吧？所以，冲突避免是一个一般原理。退避是具体的。它是一个具体的机制；尤其是在Wi-Fi中，Wi-Fi退避是一个按照某些规则工作的具体机制，它的目标是避免冲突。不过，它是一个具体的机制，是DCF信道接入方案的一部分。而且确实，同样，在这种情况下，我们也确实有退避，对吧？而退避存在的理由也是一样的：尝试避免冲突，尝试让需要接入信道、彼此竞争的传感器不再同步行动。不过，这个冲突避免过程与Wi-Fi中的相同吗？不。相似，但不相同。好，很好。如果已经清楚了，我们就可以转到下一个。[校对说明：“使其不再同步”是根据上下文作出的推定；独立ASR转写为“使其同步”。]

# 八、答疑：NAV、冻结与推迟

## 62 · 01:08:08 · 提问NAV、退避冻结与推迟的区别

原标说话人 2  01:08:08
[Opening wording unclear.] In DCF, what is the difference between NAV, backoff freezing, and deferral? Can these concepts be used interchangeably in the exercises?
[开头措辞不清楚。]在DCF中，NAV、退避冻结和推迟之间有什么区别？在练习中，这些概念可以互换使用吗？

## 63 · 01:08:24 · 三者不可互换且推迟不是机制

原标说话人 1  01:08:24
Okay, in DCF, what is the difference between NAV, backoff freezing, and deferral? Can these concepts be used interchangeably in the exercises? No. So the answer is no. Or should they be treated as distinct mechanisms? Yes, they should be treated as distinct mechanisms. But deferral is not a mechanism.
好，在DCF中，NAV、退避冻结和推迟之间有什么区别？在练习中，这些概念可以互换使用吗？不能。所以，答案是不能。还是应该把它们作为不同的机制来对待？是的，应该把它们作为不同的机制来对待。不过，推迟不是一种机制。

## 64 · 01:08:52 · 推迟的含义及与具体机制的区别

原标说话人 1  01:08:52
Okay, deferral in English means to postpone. A mechanism is something more; it's a specific behavior. Deferral is something general, means to postpone. A mechanism is when you specify the behavior of a node. So a node will defer an action; it will postpone, right, that action. But deferral per se is not a mechanism. So deferral, I hope we clarified that. NAV and backoff freezing, they are very different things. Okay.
好，deferral在英语中的意思是推迟。一个机制所包含的东西更多；它是一种具体的行为。推迟是一种一般性的说法，意思是延后。一个机制，是指你具体规定一个节点的行为。所以，一个节点会推迟某个动作；它会延后，对吧，那个动作。不过，推迟本身不是一种机制。所以，对于推迟，我希望我们已经澄清了这一点。NAV和退避冻结，它们是非常不同的事情。好。

## 65 · 01:09:42 · 设置NAV可能伴随退避冻结

原标说话人 1  01:09:42
Actually, the short answer—then we're going to clarify—but the short answer is: backoff freezing may happen, may happen, when you set the NAV, right? But NAV is totally different. So let's explain better.
实际上，简短的回答——然后我们会澄清——不过，简短的回答是：退避冻结可能发生，可能发生，在你设置NAV的时候，对吧？不过，NAV是完全不同的。所以，让我们解释得更清楚一点。

## 66 · 01:10:05 · 借简单DCF时序重新解释NAV

![图36：DCF Basic Access: Unicast DATA + ACK](../slide-images/slide-wifi-036.png)

课件：02-WiFi_1-7.pdf · PDF第18页下半页 · 图36（按PDF顺序）

原标说话人 1  01:10:05
So remember what we said at the very beginning, when we were giving the overview of how DCF works. In this simple case where we had an access point and then, for example, A and B—[a reference to another node is unclear]—that can all hear each other, right? So we said, let's consider the time diagram. It was one of the initial ones that we showed. So we said, let's consider that A has got a packet to transmit.
所以，记住我们在最开始概述DCF如何工作时所说的。在这个简单的情况下，我们有一个接入点，然后还有，例如，A和B——[这里提到另一个节点的措辞不清楚]——它们都能够听到彼此，对吧？所以，我们说，来考虑一下时间图。它是我们最开始展示的那些图之一。所以，我们说，来考虑A有一个分组要发送的情况。

## 67 · 01:11:05 · 读取Duration并设置NAV计数器

原标说话人 1  01:11:05
What DCF says is that in this case, A gets the packet from its higher layers. At that point, as we already said this morning, it needs to sense the channel for DIFS. If the channel is idle, then it can transmit its data packet. If this data packet is received successfully After SIFS, the access point will send back the ACK. And then we said, what do the other nodes do in this case? They demodulate the header of the data packet, read the Duration field, and at the MAC layer they set a counter to the value that represents the expected duration of the dialogue, right? So this is the NAV; the NAV is a counter. First of all, setting the NAV means that you are reading the Duration field in the header of a packet. This packet could also be RTS or CTS, or the data packet. Even the acknowledgment Has got a Duration field here, okay? You read the Duration field and you set your NAV counter to the value that you read in that field of the header. That's the usage of NAV. Okay, so is there any backoff here?
DCF所说的是，在这种情况下，A从它的高层收到这个分组。在那一刻，正如我们今天早上已经说过的，它需要侦听信道DIFS这么长时间。如果信道空闲，那么它就可以发送它的数据分组。如果这个数据分组被成功接收经过SIFS之后，接入点将发回ACK。然后，我们说，在这种情况下，其他节点做什么？它们解调数据分组的首部，读取Duration字段，并且在MAC层，把一个计数器设置为表示这轮对话预期持续时间的数值，对吧？所以，这就是NAV；NAV是一个计数器。首先，设置NAV意味着，你在读取一个分组首部中的Duration字段。这个分组也可以是RTS或CTS，或者数据分组。甚至确认这里也有一个Duration字段，好吗？你读取Duration字段，然后把你的NAV计数器设置为你从首部的那个字段中读到的值。这就是NAV的用法。好，所以，这里有任何退避吗？

## 68 · 01:12:59 · NAV虚拟侦听与物理CCA联合判断

原标说话人 1  01:12:59
Indeed. So the NAV, as we explained, is a counter whose usage at the MAC layer essentially represents the sensing, virtual sensing function at the MAC layer. So it tells you whether the channel is idle or busy. And it's done through a counter at the MAC layer. So it's not a physical function; it's a virtual function. And we said a node will consider the channel as idle only if both the sensing function at the physical layer That is called CCA; I recall that because we also mentioned it this morning for the sensors—and the virtual sensing function at the MAC layer, represented by the NAV, say the channel is idle. Okay?
确实如此。所以，正如我们解释过的，NAV是一个计数器，它在MAC层的用途基本上代表了MAC层的侦听、虚拟侦听功能。所以，它告诉你，信道是空闲还是忙。而这是通过MAC层的一个计数器来完成的。所以，它不是一个物理功能；它是一个虚拟功能。而且，我们说过，一个节点要把信道视为空闲，必须同时满足：物理层的侦听功能这个功能叫作CCA；我提醒一下这一点，因为今天早上讲传感器时，我们也提到过它——以及由NAV代表的MAC层虚拟侦听功能，两者都说信道空闲。好吗？

## 69 · 01:14:02 · 退避冻结取决于信道是否忙

原标说话人 1  01:14:02
Now, when a node is—[unclear fragment]. Okay, that's about the NAV. Now, when a node has got the backoff counter set to a positive value, we know that you can decrease the backoff counter as long as the channel is idle. But as soon as the channel becomes busy, it has to freeze the counter. Okay. When does a node say that the channel is busy? So if I am a Wi-Fi card When do I say, ‘Well, for me the channel is busy’? When do I say that?
现在，当一个节点处于——[片段不清楚]。好，关于NAV就是这些。现在，当一个节点的退避计数器被设为一个正值时，我们知道，只要信道空闲，你就可以递减退避计数器。不过，一旦信道变忙，它就必须冻结计数器。好。一个节点什么时候会说信道忙呢？所以，如果我是一块Wi-Fi网卡我什么时候会说：“嗯，对我来说，信道忙”？我什么时候会这样说？

## 70 · 01:15:01 · CCA或NAV任一忙都冻结退避

原标说话人 1  01:15:01
When, first of all, if at the physical layer my CCA function senses power above the threshold, right? That's physical sensing. Or, and if at the MAC layer I've got the NAV set, right? We just said that the channel is considered busy if at least one of these functions says the channel is busy. It might be only the CCA at the physical layer; it may be the NAV only; or they both can say the channel is busy. But when the channel is busy, I have to freeze the backoff counter. Okay? So the backoff counter is not NAV. Okay? They're completely different. And by the way, I can freeze the backoff counter even if the NAV is zero.
什么时候呢，首先，如果在物理层，我的CCA功能侦听到超过阈值的功率，对吧？那就是物理侦听。或者，而且，如果在MAC层，我已经设置了NAV，对吧？我们刚才说过，只要这些功能中至少有一个说信道忙，就认为信道忙。可能只有物理层的CCA这样说；可能只有NAV这样说；或者它们两个都可能说信道忙。不过，当信道忙时，我必须冻结退避计数器。好吗？所以，退避计数器不是NAV。好吗？它们是完全不同的。而且，顺便说一下，即使NAV为零，我也可以冻结退避计数器。

## 71 · 01:16:07 · NAV为零也可因物理忙而冻结

原标说话人 1  01:16:07
Because if my CCA function at the physical layer says the channel is busy, the channel is busy whatever the NAV is. And if the channel is busy, I have to freeze the backoff counter, if I've got a backoff counter set to a value that is greater than zero. Okay, good. Next. Just check the time. [A short transition is unclear.] You can start reading the question.
因为，如果我在物理层的CCA功能说信道忙，那么，不管NAV是什么值，信道就是忙的。而如果信道忙，我就必须冻结退避计数器，前提是我有一个被设为大于零的数值的退避计数器。好，很好。下一个。看一下时间。[一小段过渡话语不清楚。]你可以开始读问题了。

# 九、答疑：扩展IFS及碰撞实例

## 72 · 01:16:41 · 各机制使用条件与三类退避场景

![图45：When Does a Station (Re)contend? — the Backoff Cases](../slide-images/slide-wifi-045.png)

课件：02-WiFi_1-7.pdf · PDF第23页上半页 · 图45（按PDF顺序）

原标说话人 1  01:16:41
Okay, thanks. Under what circumstances should backoff, extended IFS, backoff freezing, and NAV each be used, respectively? [A brief aside after the question is unclear.] So backoff is used whenever we have the three—so the short answer is, you go back to the slide and you check that. The backoff procedure, we have a slide on that, is performed under three possible situations, right? We have a slide. Go there and read the slide.
好，谢谢。在什么情况下，应该分别使用退避、扩展IFS、退避冻结和NAV？[问题之后的一句简短插话不清楚。]所以，每当我们有那三种——所以，简短的回答是，你回到那张幻灯片，查看一下。退避过程，我们有一张关于它的幻灯片，是在三种可能的情况下执行的，对吧？我们有一张幻灯片。到那里去，读一读那张幻灯片。

## 73 · 01:17:25 · 扩展IFS及两层侦听不一致

原标说话人 1  01:17:25
Extended IFS, backoff freezing, and NAV. Now, backoff freezing, we just said that, right? Whenever the channel is sensed as busy. NAV, we just said that: NAV starts whenever I read the Duration field in the packet header and I set the NAV. So let's focus on extended IFS, okay? Extended IFS is indeed a little bit more tricky. Why? Because—thanks—because the definition is simple, but then one has to think about the examples that we presented to probably really grasp the concept. So the definition is simple, meaning that extended IFS is used whenever we have a mismatch between what the physical layer says and what the MAC layer says within a communication node. And we have a Wi-Fi card: its physical layer, for example, senses the channel is busy, and the MAC layer reports, senses that the channel is idle. Or vice versa, for example. But anyway, whenever we have a mismatch. Okay?
扩展IFS、退避冻结和NAV。现在，退避冻结，我们刚才说过了，对吧？每当侦听到信道忙的时候。NAV，我们刚才也说过了：每当我读取分组首部中的Duration字段并设置NAV时，NAV就开始了。所以，我们重点看扩展IFS，好吗？扩展IFS确实稍微更棘手一些。为什么？因为——谢谢——因为定义很简单，不过，然后你必须想一想我们介绍过的例子，才可能真正理解这个概念。所以，定义很简单，意思是，每当一个通信节点内部物理层所说的与MAC层所说的出现不一致时，就使用扩展IFS。而我们有一块Wi-Fi网卡：例如，它的物理层侦听到信道忙，而MAC层报告、侦听到信道空闲。或者，例如，反过来。不过，总之，每当我们出现不一致的时候。好吗？

## 74 · 01:19:03 · 用两个例子复习EIFS

原标说话人 1  01:19:03
So the examples that we made probably clarify better this usage of extended IFS. You may remember that we presented, in particular, two examples, two situations under which we use extended IFS. That is, one situation was the following.
所以，我们举过的例子可能会更好地说明扩展IFS的这种用法。你们可能记得，我们特别介绍过两个例子，两种我们会使用扩展IFS的情况。也就是说，其中一种情况如下。

## 75 · 01:19:36 · A、B同时发送造成信号重叠

原标说话人 1  01:19:36
We have, for example, A and B that are hidden with respect to each other, or they are in radio visibility. It doesn't really matter here. But anyway, they transmit a data packet at the same time. Okay, they access the channel at the same time and transmit.
例如，我们有A和B，它们相对于彼此是隐藏的，或者它们处在彼此的无线电可见范围内。这里，这实际上并不重要。不过，总之，它们同时发送一个数据分组。好，它们同时接入信道并发送。

## 76 · 01:20:01 · C无法解调首部却感知信道忙

原标说话人 1  01:20:01
Now clearly, these packets at the access point cannot be successfully received because we have a collision, right? Let's consider that C also is exposed to both signals, so it can hear both signals. C is another node there in the BSS. But in this case, will C be able to demodulate the header of these packets? No, right? It cannot, because they overlap, right? So the SINR at C will be too low; it cannot demodulate correctly the header of these data packets. So can C set its NAV? No. No, right? But at the physical layer, C senses power; the channel is busy. So we have: the physical layer says channel busy; the MAC layer, meaning the NAV, says channel idle. Right?
现在，显然，在接入点，这些分组无法被成功接收，因为我们发生了冲突，对吧？我们考虑一下，C也同时处在这两个信号的覆盖下，所以它能听到这两个信号。C是那个BSS中的另一个节点。不过，在这种情况下，C能够解调这些分组的首部吗？不能，对吧？它不能，因为它们重叠了，对吧？所以，C处的SINR会太低；它无法正确解调这些数据分组的首部。那么，C能设置它的NAV吗？不能。不能，对吧？不过，在物理层，C侦听到功率；信道忙。所以，我们的情况是：物理层说信道忙；MAC层，也就是NAV，说信道空闲。对吧？

## 77 · 01:21:32 · 信道重新空闲后C等待EIFS

原标说话人 1  01:21:32
This is a mismatch between physical and MAC. So this means that as soon as the channel becomes idle again, then C has to wait for the extended IFS before taking action.
这就是物理层和MAC层之间的不一致。所以，这意味着，一旦信道再次变为空闲，那么C就必须在采取动作之前等待扩展IFS。

## 78 · 01:21:53 · 接入点同样等待及新发送示例

原标说话人 1  01:21:53
Okay? Then we said also, by the way, also the access point, okay? Same behavior. Also for the access point, we have the same behavior. So here we have the extended IFS. Also we said, well, a node can stop waiting for the extended IFS only if during this time another node accesses the channel. And, for example, if there is another node D here that could hear only A, for example, it can set the NAV, and then it has got a packet to transmit and it accesses the channel, for example, at this point in time.
好吗？然后我们还说过，顺便说一下，接入点也是这样，好吗？同样的行为。对于接入点，我们也有同样的行为。所以这里是扩展帧间间隔。我们还说过，嗯，一个节点只有在这段时间内有另一个节点接入信道，才可以停止等待扩展帧间间隔。比如说，如果这里有另一个节点D，例如，它只能听见A，那么它可以设置NAV，然后它有一个分组要发送，于是它接入信道，比如说，在这个时刻。

## 79 · 01:22:44 · 正确接收D的首部后恢复正常

原标说话人 1  01:22:44
Okay. If C can hear D, then it can hear this header of the packet. And in this case it can resume its normal behavior, because it's now able to set its NAV, and everything is back to normal. [Editorial note: “Set its NAV” is inferred from context; the two transcriptions disagree.]
好。如果C能够听见D，那么它就能够听到这个分组的这个头部。而在这种情况下，它可以恢复正常行为，因为它现在能够设置自己的NAV了，一切都恢复正常。[校对说明：“设置自己的NAV”是根据上下文推定的；两份转写对此不一致。]

## 80 · 01:23:04 · 中断EIFS与不同包长碰撞示例

原标说话人 1  01:23:04
So the extended IFS can be, let's say, interrupted if during the IFS I can hear something, I understand what that is, and then I can resume my normal behavior. So that was One situation under which a node, for example, has to use extended IFS, right, because we have this mismatch. The second, a second example where we said that our node, our node is going to use the extended IFS, was, if you remember that example where we had two packets of different duration, right? So we still had a collision, as before. C also could not understand the header of the packets. So here for C we have exactly the same situation as before. The physical layer of C says channel busy, while the MAC layer of C says channel idle. Okay, exactly as before.
因此，可以说，如果在扩展帧间间隔期间我能听到某个东西，我理解了那是什么，那么我就能恢复正常行为，扩展帧间间隔就可以被中断。所以，那是例如，节点必须使用扩展帧间间隔的一种情况，对吧，因为我们有这种不一致。第二个，第二个我们说节点、我们的节点将会使用扩展帧间间隔的例子，是，如果你们还记得那个两个分组持续时间不同的例子，对吧？所以我们仍然发生了冲突，和之前一样。C也无法理解这些分组的头部。所以这里对于C来说，情况与之前完全一样。C的物理层说信道忙，而C的MAC层说信道空闲。好，和之前完全一样。

## 81 · 01:24:32 · 不同包长碰撞中A的特殊处境

原标说话人 1  01:24:32
So we have to wait for the channel to become idle, and then use extended IFS for C. It's the same as before. But we added one more situation here, if you remember, that was about A. Why? Because A transmitted its packet. It failed because it was overlapping with B's transmission.
所以，我们必须等待信道变为空闲，然后让C使用扩展帧间间隔。这和之前一样。但是，如果你们还记得，我们在这里又加了一种情况，那是关于A的。为什么？因为A发送了它的分组。它失败了，因为它与B的传输重叠了。

## 82 · 01:25:04 · A只听到包尾时使用EIFS

原标说话人 1  01:25:04
And then, after stopping because its packet was shorter, it would turn into receive mode, hoping to receive the acknowledgment, right? But what it could hear is the ending of this transmission. That is nothing—I mean, it's a signal at the physical layer, but clearly it's not going to demodulate anything. It's not a header; it's the ending of the packet. So again, here we have: the physical layer of A says channel busy, because there is the signal on the channel, but its MAC has got the NAV set to zero. So for the MAC, the channel is idle. Again, mismatch. Okay, physical layer says busy, MAC layer says idle, so mismatch. So at that point A has to wait for the channel to become idle again and use extended IFS. Okay? So if we want a simple rule, okay, to simplify things: whenever, in a node, its physical layer senses the channel as busy—[a short repeated fragment is unclear]—but the NAV is set to zero, so the MAC layer says channel idle, then we have a mismatch, and that means that we need to use the extended IFS as soon as the channel becomes idle.
然后，由于它的分组比较短，在停止发送之后，它会转入接收模式，希望收到确认，对吧？但是它能够听见的是这次传输的末尾。那什么也不是——我是说，在物理层它是一个信号，但显然它不会解调出任何东西。那不是头部；那是分组的末尾。所以，这里我们又有这样的情况：A的物理层说信道忙，因为信道上有信号，但是它的MAC的NAV设为零。所以，对于MAC来说，信道是空闲的。又是不一致。好，物理层说忙，MAC层说空闲，所以不一致。因此，在那个时刻，A必须等待信道再次变为空闲，并使用扩展帧间间隔。好吗？所以，如果我们想要一条简单的规则，好，来把事情简化一下：只要在一个节点中，它的物理层感知信道为忙——[一小段重复片段不清楚]——但是NAV设为零，所以MAC层说信道空闲，那么我们就有不一致，而这意味着，一旦信道变为空闲，我们就需要使用扩展帧间间隔。

## 83 · 01:26:56 · 转向下一个答疑问题

原标说话人 1  01:26:56
Okay, good. Next.
好，很好。下一个。

# 十、答疑：DIFS、EIFS与RTS阈值

## 84 · 01:27:11 · 退避开始与恢复前的DIFS要求

原标说话人 1  01:27:11
Is DIFS always required before backoff? Yes, unless we use extended IFS, right? If the backoff countdown is interrupted by the channel becoming busy and is later resumed, does the station still need to wait for DIFS before continuing?
退避之前是否总是需要DIFS？是的，除非我们使用扩展帧间间隔，对吧？如果退避倒计时因信道变忙而中断，后来又恢复，那么站点在继续之前是否仍然需要等待DIFS？

## 85 · 01:27:30 · 等待EIFS本身不必然触发退避

原标说话人 1  01:27:30
Yes. If a station has waited extended IFS and then finds the channel busy, does it enter backoff directly, or does it still need to wait for DIFS first? What do you mean? Because a station that does not have any packet to transmit, it will wait extended IFS, but then it will not need to perform any backoff. So, no. I mean, in general, let's say that the question is not well posed, because the fact that I have to wait for extended IFS doesn't mean that I have to run a backoff.
是的。如果一个站点已经等待了扩展帧间间隔，随后发现信道忙，它是直接进入退避，还是仍然需要先等待DIFS？你是什么意思？因为一个没有任何分组要发送的站点，它会等待扩展帧间间隔，但随后它不需要执行任何退避。所以，不是。我是说，一般来说，可以说，这个问题提得不够恰当，因为我必须等待扩展帧间间隔这一事实，并不意味着我必须执行退避。

## 86 · 01:28:16 · 适用时EIFS替代DIFS及转写疑点

原标说话人 1  01:28:16
I have to run a backoff if I have something to transmit. If I don't have anything to transmit, I have to run a backoff. If a node has got something to transmit, then of course, as we said, in the case it needs to use extended IFS, it will wait for extended IFS and then draw the integer for the backoff in order to transmit its packet. So in this case, extended IFS essentially replaces DIFS, if that's the question. Okay, good. [Editorial note: Both transcriptions contain the positive “I have to” in the second sentence, which conflicts with the preceding explanation; a missing negative or spoken slip is possible, and this wording is unconfirmed.]
如果我有东西要发送，我就必须执行退避。如果我没有任何东西要发送，我就必须执行退避。如果一个节点有东西要发送，那么当然，正如我们说过的，在它需要使用扩展帧间间隔的情况下，它会等待扩展帧间间隔，然后抽取用于退避的整数，以便发送它的分组。所以，在这种情况下，扩展帧间间隔实际上替代了DIFS，如果问题问的是这个的话。好，很好。[校对说明：两份转写的第二句都包含肯定的“我必须”，这与前面的解释矛盾；可能漏了否定词，也可能是口误，这一措辞尚未确认。]

## 87 · 01:29:10 · RTS阈值由包长决定而非隐藏节点

原标说话人 1  01:29:10
So we can stop probably now. Let me just read the next question and then we will answer—[the wording about the longer break is unclear]. Why do exercises three and four involve hidden terminals but do not require RTS/CTS? Now, as we said, RTS and CTS are not used when the nodes are hidden. That's not the criterion under which we decide whether to use RTS/CTS. RTS/CTS is useful in the case when there are hidden nodes. It's useful when there are hidden nodes, but the criterion that is used to trigger a transmission with RTS and CTS is the packet size. If the packet size is above the RTS threshold, so it means a large packet, then you will use RTS and CTS to transmit it. If the packet is shorter, so below the RTS threshold, you use the simple basic DCF to transmit. Okay, so that was—okay, thanks a lot. We will continue [after the break?]. [Editorial note: “Basic DCF to transmit” is inferred from context and is not confirmed word for word.]
所以，我们现在大概可以停下来了。让我先读一下下一个问题，然后我们会回答——[关于较长休息的措辞不清楚]。为什么练习三和四涉及隐藏终端，却不要求RTS/CTS？现在，正如我们说过的，当节点是隐藏的时，不使用RTS和CTS。那不是我们决定是否使用RTS/CTS所依据的判据。在存在隐藏节点的情况下，RTS/CTS是有用的。存在隐藏节点时它是有用的，但是，用来触发采用RTS和CTS进行传输的判据是分组大小。如果分组大小超过RTS阈值，也就是说，这是一个大分组，那么你就会使用RTS和CTS来传输它。如果分组比较短，也就是低于RTS阈值，那么你使用简单的基本DCF来传输。好，所以刚才那是——好，非常感谢。我们会[在休息之后？]继续。[校对说明：“基本DCF来传输”是根据上下文推定的，尚未逐词确认。]

