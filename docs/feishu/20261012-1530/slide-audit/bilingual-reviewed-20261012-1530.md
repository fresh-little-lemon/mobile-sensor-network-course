说明：Git文本检查点不含图片二进制；图像见飞书原文或完整ZIP。

# 双语对照：录音机-20261012-1530

https://lcn6dqn3m0yr.feishu.cn/docx/EsHBd3OOCo6ODAxhlMKc6JxNn9d

课件审计检查点：44段原正文与导航保留，9张图已逐张核验；2项课堂图来源缺口；未作原音转写认证。

会议主题：录音机-20261012-1530
课程：移动与传感器网络 / Mobile Sensor Networks
上传时间：2026年10月14日（周三） 09:55 （GMT+08）
音频时长：约 00:45:19
整理日期：2026年10月18日
版本：完整忠实双语稿 · 913cf98f5b3c
状态：双语正文已完成（44 对）；已匹配插入9张课件图

[原录音附件块保留，音频二进制未打包]

录音文件：点击打开原始录音并播放

原资源链接：https://lcn6dqn3m0yr.feishu.cn/minutes/obcnl1j5hh4391672s5qxi1r

文字来源：原始文字记录

原资源链接：https://lcn6dqn3m0yr.feishu.cn/docx/Cp7Pd07RQobgCFx4iiucXKiunCb

课件来源：02-WiFi_1-7.pdf

原资源链接：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf

# 一、扩展IFS与侦听不一致

## 01 · 00:00:02 · 扩展IFS的使用条件

原标说话人 1  00:00:02
As we said, now we need this last piece to understand this basic scheme, that is, the use of extended IFS. So, the definition is actually simple, although I can understand that it might be a bit obscure at the beginning, meaning that this extended IFS is used whenever a network node senses the channel as busy at the physical layer, but at the MAC layer you cannot set its NAV. Essentially, at the MAC layer the channel is still sensed as idle, although the node actually senses that the channel, in a way, is busy at the physical layer. So, clearly, it is used in the case of an error.
正如我们刚才所说，现在还需要最后这一块拼图，才能理解这个基本方案，也就是扩展帧间间隔的使用。所以，定义其实很简单，虽然我能理解，一开始它可能有点难懂。意思是，只要一个网络节点在物理层感知到信道忙，但在 MAC 层却无法设置它的 NAV，就会使用这个扩展帧间间隔。实际上，虽然这个节点在物理层确实感知到信道在某种意义上是忙的，但在 MAC 层，信道仍被感知为空闲。所以很明显，它是在发生错误的情况下使用的。

![图53：EIFS: Extended Interframe Space](../slide-images/slide-053.png)

课件：02-WiFi_1-7.pdf · PDF第27页上半页 · 图53（按PDF顺序）

## 02 · 00:01:13 · 双重侦听不一致与三节点示例

原标说话人 1  00:01:13
Something is wrong, right? Because we get different feedback from the physical layer and from the MAC layer about the state of the channel. So, there is a mismatch between physical and virtual sensing. That is when we use the extended IFS. Now, if you think about it, again, it is what we do as human beings when someone is talking. So, we know that someone is talking, but we do not understand what this guy is saying. Clearly, we do not answer, right? We do not say anything. We wait and try to figure out how things are and what actually is the message for us. So, if we do not understand, we just wait a little bit in order to figure out what to do. And this is essentially what our Wi-Fi nodes will also do. If they do not exactly understand what is going on, because there is a mismatch between physical-layer and MAC-layer sensing, then they wait. Okay, so this is the basic principle. We are going to explain, hopefully a little bit better, how this is used. Then we will see other examples. But for today, let us refer to this situation. So, in this case, we have three nodes, A, B, and C. Again, you can read B as an access point if you wish. So, B is our data source. It has got a packet toward C. So, C is the destination of this packet. And we are currently observing our system, and currently what we see is that B is indeed transmitting the packet to C. Okay. So, let us assume that C can receive correctly from B. Indeed, B and C are within the same radio range.
有地方不对劲，对吧？因为物理层和 MAC 层对信道状态给出了不同的反馈。所以，物理载波侦听和虚拟载波侦听之间出现了不一致。这就是使用扩展帧间间隔的时候。现在，如果你再想一想，这和我们人在听别人说话时的做法一样。我们知道有人在说话，却听不懂这个人在说什么。显然，我们不会回答，对吧？我们什么也不说。我们会等一等，试着弄清楚情况，以及对方究竟想向我们传达什么。所以，如果我们没听懂，就会稍等片刻，好弄清楚该怎么办。我们的 Wi-Fi 节点实际上也会这样做。如果它们不完全清楚正在发生什么，因为物理层和 MAC 层的侦听结果不一致，那么它们就会等待。好，这就是基本原理。接下来我们会争取更清楚地解释它的用法，之后还会看其他例子。不过今天，我们先来看这种情况。这里有三个节点，A、B 和 C。还是一样，如果你愿意，可以把 B 看作一个接入点。B 是我们的数据源，它有一个要发往 C 的分组，所以 C 是这个分组的目的节点。现在我们正在观察这个系统，看到的情况是 B 确实正在把分组发给 C。好，假设 C 能正确接收 B 的信号。事实上，B 和 C 处在彼此的无线覆盖范围内。

## 03 · 00:03:43 · B向C成功传输并收到ACK

原标说话人 1  00:03:43
And let us assume that this data-packet transmission, in principle, is successful. So, C can demodulate everything correctly and is also, therefore, transmitting back an acknowledgment after a SIFS. So, so far, so good. We know this is the, let us say, usual way of behavior, the usual way our nodes behave in Wi-Fi.
而且，让我们假设这次数据包传输原则上是成功的。所以，C能正确解调所有内容，因此也会在一个SIFS之后发回确认。所以，到目前为止，一切都很好。我们知道，这就是，可以说，通常的行为方式，我们的节点在Wi-Fi中通常的行为方式。

## 04 · 00:04:15 · A能听见B却无法解调C

原标说话人 1  00:04:15
Now A, as you can see from the top-right figure there, can hear B but is outside the radio range of C. So, it means that, in this case, what it means is that A can correctly receive from B, but it cannot correctly demodulate the signal, any signal coming from C. Okay.
现在A，正如你们能从那里右上方的图看到的，能够听到B，但是处在C的无线电覆盖范围之外。所以，这意味着，在这种情况下，它的意思是，A能够正确接收来自B的信号，但是无法正确解调信号，来自C的任何信号。好。

## 05 · 00:04:48 · 随机信道错误导致首部解调失败

原标说话人 1  00:04:48
Now, however, we are in a particular, let us say, unlucky situation where, although typically A can demodulate correctly what B transmits, in this specific case, because remember that channel conditions are always random, right? They are determined by the presence of obstacles, how these obstacles move, where they are. So, the quality of the wireless channel actually can be represented as stochastic. So, what A actually does is hear a signal from B, but it cannot, because of a channel error, demodulate correctly what B is transmitting. So, we are in an unlucky case where suddenly the wireless channel between A and B deteriorates due to multipath fading, for example. So, as marked here, A, in this unfortunate situation, will sense the channel as busy because it can hear B, of course. But, as I said, we have an error in the demodulation stage, and A cannot extract the value of the duration field correctly.
不过，现在我们遇到了一种特别的、可以说是不走运的情况。虽然通常 A 能正确解调 B 发出的内容，但在这一次，记住，信道条件总是随机的，对吧？它们取决于障碍物是否存在、这些障碍物如何移动、位于哪里。所以，无线信道的质量实际上可以看作是随机的。A 实际上听到了 B 的信号，但由于信道错误，无法正确解调 B 正在发送的内容。因此，我们遇到了一种不走运的情况：A 和 B 之间的无线信道突然恶化，例如由于多径衰落。正如这里标出的，在这种不幸的情况下，A 会感知到信道忙，因为它当然能听到 B。但正如我所说，解调阶段出了错，A 无法正确提取持续时间字段的值。

![图54：EIFS in Action](../slide-images/slide-054.png)

课件：02-WiFi_1-7.pdf · PDF第27页下半页 · 图54（按PDF顺序）

## 06 · 00:06:36 · 无法读取Duration就不能设置NAV

原标说话人 1  00:06:36
So, if I cannot read the duration field, clearly I cannot set the NAV, right?
所以，如果我读不出持续时间字段，显然就无法设置 NAV，对吧？

## 07 · 00:06:42 · 物理忙与虚拟空闲的侦听不一致

原标说话人 1  00:06:42
So, what A will do during this time is have the physical sensing, the physical-layer sensing function, saying the channel is busy. But at the MAC layer, A cannot set the NAV, so the virtual sensing function at the MAC layer will say, "Channel idle." So, we have a mismatch between what the physical-layer sensing function says and what the MAC-layer function says. So, in this case, A is like us when we hear something but we cannot make any sense of it. So, semantically, we do not understand. We hear the voice, but semantically we do not understand what they are telling us. So, what we do is, of course, finish hearing what the other person has to say, and then what we do unconsciously is wait, right? And this is what indeed A will do.
因此，在这段时间里，A 的物理侦听，也就是物理层侦听功能，会说信道忙。但在 MAC 层，A 无法设置 NAV，所以 MAC 层的虚拟侦听功能会说：“信道空闲。”这样，物理层侦听功能和 MAC 层功能给出的结果就不一致了。在这种情况下，A 就像我们听到了声音，却完全不明白它的意思。从语义上说，我们没有理解。我们听到了声音，但从语义上说，我们不知道对方在告诉我们什么。所以，我们当然会先听完对方要说的话，然后下意识地等一等，对吧？这正是 A 要做的。

## 08 · 00:07:58 · 等待EIFS以保护正在进行的对话

原标说话人 1  00:07:58
It will wait for this extended IFS time. And then, after having sensed the channel as idle for this extended IFS time interval, A will resume the normal behavior. Now, again, why do we have this in the protocol? Well, because Wi-Fi, as we know already, has a goal to always try and preserve ongoing dialogues, right? That is one of the goals of Wi-Fi. Now, if we look at this case here, we have indeed this ongoing dialogue, right, between B and C, and this dialogue is actually taking place successfully.
它会等待这段扩展帧间间隔。然后，在感知到信道持续空闲达一个扩展帧间间隔后，A 就会恢复正常行为。那么，再问一次，协议里为什么要有这个机制？因为我们已经知道，Wi-Fi 的一个目标就是始终尽量保护正在进行的对话，对吧？这是 Wi-Fi 的目标之一。现在看这里的情况，B 和 C 之间确实有这样一段正在进行的对话，而且这段对话本来是在顺利进行的。

# 二、保护对话与恢复正常接入

## 09 · 00:09:02 · 通过反例理解EIFS保护作用

原标说话人 1  00:09:02
So, what Wi-Fi wants to avoid is that others may access the channel and disrupt ongoing dialogues, and the use of extended IFS will serve that purpose. Why? Because, again, let us study our little game.
所以，Wi-Fi想避免的是，其他节点可能接入信道并破坏正在进行的对话，而使用扩展IFS就是为了实现这个目的。为什么？因为，同样，我们来研究一下我们这个小游戏。

## 10 · 00:09:33 · 没有EIFS时A可能干扰C的确认

原标说话人 1  00:09:33
If we did not have this extended IFS, what could happen is that A, during this time, okay, the channel is busy at the physical layer. But then, after that, here the channel for A is idle both at the physical layer and at the MAC layer because A could not set its NAV. So, if A gets a packet, it can sense the channel as idle for DIFS here and potentially access the channel and transmit. In that case, if A did that, then we would have at the receiver, essentially, the possibility of... So, the receiver of the acknowledgment is B, right? So, we will have at B the possibility that these two transmissions collide, because during this time B will receive the acknowledgment. If A started transmitting, the signal from A would collide with the acknowledgment sent by C. And our B, that is now supposed to receive, will have two signals overlapping and will not be able to demodulate them correctly.
如果没有扩展帧间间隔，会发生什么？对于 A 来说，在这一段时间里，物理层上的信道是忙的。但在这之后，这里的信道对 A 而言，无论在物理层还是 MAC 层都是空闲的，因为 A 没能设置 NAV。所以，如果 A 有了一个分组，它可以在这里感知信道空闲达一个 DIFS，然后就有可能接入信道并发送。如果 A 真的这样做，那么在接收端，就可能出现……确认分组的接收端是 B，对吧？因此，在 B 这里，两次传输就有可能发生碰撞。因为在这段时间里，B 要接收确认。如果 A 开始发送，A 的信号就会和 C 发出的确认相碰撞。而此时本应进行接收的 B 会遇到两个重叠的信号，无法正确解调它们。

## 11 · 00:11:24 · 侦听不一致后必须额外等待

原标说话人 1  00:11:24
So, even if, in principle, this dialogue could have been successful, it would fail [wording uncertain], and Wi-Fi does not want that. So, what the protocol says is, if you are a node and you are not understanding what is going on on the channel because your physical-layer and MAC-layer sensing functions do not match, then, as soon as the channel becomes idle again, do nothing, just wait. And this waiting extends for this IFS time period. Okay?
所以，即使原则上这段对话本来可以成功，它也会失败［此处措辞不确定］，而 Wi-Fi 不希望发生这种情况。因此，协议的意思是：如果你是一个节点，却不明白信道上正在发生什么，因为你的物理层和 MAC 层侦听功能给出的结果不一致，那么一旦信道再次变为空闲，就什么也别做，只要等待。而这次等待会持续这段帧间间隔的时间。好吗？

![图35：DCF Basic Rules](../slide-images/slide-035.png)

课件：02-WiFi_1-7.pdf · PDF第18页上半页 · 图35（按PDF顺序）

## 12 · 00:12:10 · 正确收到首部后提前结束EIFS

原标说话人 1  00:12:10
Now, however, if, while a node is waiting for this extended IFS to be completed, if during this time it receives a packet header and is able to read that header and the duration field in that header, then it resumes the normal behavior immediately, because it means that, at that point, it is again understanding what is going on on the channel. So, its physical-layer and MAC-layer sensing functions match again. So, no need to keep running this extended IFS.
现在，不过，如果一个节点正在等待这个扩展IFS结束时，如果在这段时间里，它收到一个数据包首部，而且能够读取这个首部以及首部中的Duration字段，那么它就会立即恢复正常行为，因为这意味着，在那个时候，它又理解信道上正在发生什么了。所以，它的物理层和MAC层侦听功能再次一致。因此，没有必要继续运行这个扩展IFS。

![图55：EIFS: the Recovery Rule](../slide-images/slide-055.png)

课件：02-WiFi_1-7.pdf · PDF第28页上半页 · 图55（按PDF顺序）

## 13 · 00:13:04 · 重新理解信道状态便恢复正常

原标说话人 1  00:13:04
Now you are understanding what is going on again on the channel, so just forget about the extended IFS and resume the normal behavior. So, as I said, this may be a little bit difficult to understand now, or to think of how it is actually applied.
现在你又知道信道上正在发生什么了，所以就不用再管扩展帧间间隔，恢复正常行为即可。正如我所说，现在要理解这一点，或者想象它在实际中如何应用，可能还有些困难。

# 三、DCF总结与练习安排

## 14 · 00:13:28 · 后续实例帮助理解EIFS

原标说话人 1  00:13:28
Tomorrow we will look at some examples, okay? So, do not worry too much. I mean that, for now, it is okay if you grasp the idea of why we have this extended IFS, and then tomorrow we will see more examples, more situations, and it will become, hopefully, clearer, more clear how this is used in Wi-Fi.
明天我们会看一些例子，好吗？所以，不必太担心。我的意思是，目前只要你理解了为什么需要扩展帧间间隔，就可以了。明天我们会看更多例子、更多情况，希望到时会更清楚，更清楚它在 Wi-Fi 中是如何使用的。

## 15 · 00:13:58 · 通过实例整合DCF机制

原标说话人 1  00:13:58
Okay, so let us keep it on hold for now, a little bit. So, tomorrow we will devote some time to indeed see how our scheme is applied. So, that will help us to put all things together, all pieces together, and have a better understanding of the overall DCF scheme.
好，那么，我们暂时把它稍微搁置一下。所以，明天我们会花一些时间，真正看看我们的方案是怎样应用的。因此，这会帮助我们把所有东西放在一起，把所有部分放在一起，更好地理解整个DCF方案。

## 16 · 00:14:27 · 次日数值练习安排

原标说话人 1  00:14:27
Okay. So, that will be tomorrow, because tomorrow we will indeed present some numerical problems. I will give you some time to look at the problem, try to understand what the problem is about, and, if possible, sketch some solution.
好。所以，那是明天的内容，因为明天我们确实会给出一些数值问题。我会给你们一些时间看看题目，尝试理解题目是关于什么的，而且，如果可能，勾勒出一些解法。

## 17 · 00:14:49 · 准备绘制节点行为并结束基础DCF

原标说话人 1  00:14:49
So, make sure you have a tablet or a piece of paper, whatever you like, in order to be able to try and draw the behavior of the nodes based on the situations that we will present, so that you can train yourself a little bit in using this protocol. But this evening we will just close here the basic DCF, as promised.
所以，请准备好平板电脑或一张纸，随你喜欢，以便根据我们给出的情况，试着画出节点的行为。这样你就能练习一下如何运用这个协议。不过今天晚上，我们会按照之前的计划，在这里结束基本 DCF 的介绍。

# 四、PCF与DCF的超帧共存

## 18 · 00:15:23 · 引入集中式点协调功能PCF

原标说话人 1  00:15:23
The extended IFS was the last thing to specify, and what we will do instead is present briefly the second access scheme in Wi-Fi, right? The centralized one. Remember, it was called point coordination function. It is centralized, so it could have been applied. It is specified by the standard, but in practice it is not implemented in commercial products. So, we will be fast about it. It could be applied if we have an access point, because it is a centralized scheme, so we need a central node that actually runs this protocol.
扩展帧间间隔是最后一个需要说明的内容。接下来，我们会简要介绍 Wi-Fi 中的第二种接入方案，对，就是集中式方案。记得吗，它叫点协调功能。它是集中式的，所以原本可以采用。标准中规定了它，但实际商用产品中并没有实现它，所以我们会快速讲一下。如果有接入点，就可以采用它，因为这是一个集中式方案，我们需要一个真正运行该协议的中心节点。

## 19 · 00:16:14 · DCF与PCF如何共存

原标说话人 1  00:16:14
Now, the first important thing that we need to say is how DCF, so the scheme that we learned so far, and this second type of channel access could coexist if they were both implemented. Why is this important? Well, we will find out probably tomorrow or the day after. I would say tomorrow. So, it is something important to understand.
现在，首先要说明的重要事情是：DCF，也就是我们目前学过的方案，与第二种信道接入方式，如果两者都实现了，会怎样共存。为什么这很重要？我们大概明天或后天就会知道，我想应该是明天。所以，这是一个需要理解的重要问题。

## 20 · 00:16:48 · 连续信标之间的超帧

原标说话人 1  00:16:48
Excuse me. So, we know already that whenever we have a BSS with an access point, our access point almost periodically transmits the beacon packet. And we said, consider that the beacon is broadcast every 100 milliseconds. Okay, the time between two consecutive beacons is called a superframe.
不好意思。我们已经知道，只要一个 BSS 中有接入点，这个接入点就会近似周期性地发送信标分组。我们说过，假设信标每 100 毫秒广播一次。好，两个连续信标之间的时间称为一个超帧。

![图58：PCF Superframe Structure](../slide-images/slide-058.png)

课件：02-WiFi_1-7.pdf · PDF第29页下半页 · 图58（按PDF顺序）

## 21 · 00:17:23 · PCF阶段与无竞争期

原标说话人 1  00:17:23
The standard says that when, in our Wi-Fi BSS, we have implemented both DCF and PCF, things work, should work, in this way. We have the beacon transmitted by the access point, and then we have a first time interval, first phase, time phase, during which we would use PCF. That is also referred to as the contention-free period, because PCF, as we said, is centralized. There is no distributed protocol, no contention for the channel, right? We already said there would be the access point saying, "You transmit, you transmit, you transmit." So, there is no contention. It is the access point that makes decisions about who is going to transmit.
标准说，当我们的Wi-Fi BSS实现了DCF和PCF两者时，事情会、应该会按照这种方式运行。我们有接入点发送的信标，然后有第一个时间区间、第一个阶段、时间阶段，在这期间我们使用PCF。它也称为无竞争期，因为，正如我们说过的，PCF是集中式的。没有分布式协议，没有对信道的竞争，对吧？我们已经说过，会由接入点说：‘你发送，你发送，你发送。’所以，没有竞争。是接入点决定谁将发送。

## 22 · 00:18:29 · DCF阶段与竞争期

原标说话人 1  00:18:29
So, there is first this phase. And then, when this phase, first phase, ends, we have a second phase within the superframe where, instead, we apply the DCF scheme. That is, as we know, a contention-based protocol, right? It is distributed, so nodes will contend for the channel, and indeed this second phase is called the contention period. Okay, and then things repeat over and over.
所以，先是这个阶段。等这个第一阶段结束后，在同一个超帧中还有第二个阶段，这一阶段则使用 DCF 方案。我们知道，它是一个基于竞争的协议，对吧？它是分布式的，所以各节点会竞争信道，而这第二阶段确实就叫竞争期。好，然后整个过程不断重复。

## 23 · 00:19:08 · 两种接入方案在超帧内时分共存

原标说话人 1  00:19:08
So, essentially, if we had both PCF and DCF implemented in our Wi-Fi cards, the two schemes, PCF and DCF, would coexist within the same superframe, and they would be essentially divided, separated, only on a time-division basis. Okay, so that is it. This is important, as I was saying.
所以，基本上，如果我们的Wi-Fi网卡同时实现了PCF和DCF，那么这两个方案，PCF和DCF，会在同一个超帧中共存，而它们基本上只是按照时分方式被划分、被分隔。好，就是这样。正如我刚才所说，这很重要。

![图59：PCF and DCF Coexistence](../slide-images/slide-059.png)

课件：02-WiFi_1-7.pdf · PDF第30页上半页 · 图59（按PDF顺序）

# 五、轮询、数据与快速确认

## 24 · 00:19:46 · PCF参与站点列表与关联阶段

原标说话人 1  00:19:46
We know already what to do in the second phase of the superframe when we use DCF. What we need to explain now, [aside unclear], is what happens when we use PCF. So, for clarity, let me draw here an example. Remember, we are focusing on PCF. So, let us consider one superframe. The superframe starts with a beacon that is transmitted by the access point. And then what happens is that the access point has got a list of user stations that are connected to that access point. We said that already. During association, these nodes told the access point if they intend to participate in the PCF phase, that, as we said, is also called the contention-free period, or not. Okay? So, the access point has this list of stations.
我们已经知道，在使用 DCF 的超帧第二阶段该做什么。现在需要解释的，［插话不清］，是使用 PCF 时会发生什么。为了说清楚，我在这里画一个例子。记住，我们现在关注的是 PCF。来看一个超帧，它以接入点发送的信标开始。然后，接入点有一张与它相连的用户站点列表。我们已经说过，在关联过程中，这些节点会告诉接入点，它们是否打算参与 PCF 阶段，也就是我们所说的无竞争期。好，所以接入点有这样一张站点列表。

![图57：PCF: Basic Characteristics](../slide-images/slide-057.png)

课件：02-WiFi_1-7.pdf · PDF第29页上半页 · 图57（按PDF顺序）

## 25 · 00:21:23 · 接入点按列表轮询各站点

原标说话人 1  00:21:23
Let us say A wants to participate, B does not, C wants to participate, D wants to participate, E does not, F wants, and so on. Okay, it has got this list. Now, remember, this list, according to the standard, has been compiled during the association phase, so at the very beginning, when these nodes joined. Okay. Now, at every superframe, after the beacon, the access point will go through this list using the so-called polling scheme.
假设A想参与，B不想，C想参与，D想参与，E不想，F想，等等。好，它有这张列表。现在，记住，按照标准，这张列表是在关联阶段编制的，所以是在最开始，这些节点加入的时候。好。现在，在每一个超帧中，信标之后，接入点会使用所谓的轮询方案遍历这张列表。

## 26 · 00:22:08 · 轮询A并授权发送

原标说话人 1  00:22:08
The polling scheme is very simple. Let us assume that the first station to poll is A. This means that, after SIFS since the beacon, our access point will send a poll packet, and this poll is intended for A. And this poll packet from the access point, let us say to A, essentially means, "A, now you can transmit." Okay? So, upon receiving this poll message, A will send its data packet if it has got a data packet to transmit.
轮询机制非常简单。假设第一个要轮询的站点是 A。这意味着，在信标结束后经过一个 SIFS，接入点会发送一个轮询分组，这次轮询针对的是 A。这个从接入点发给 A 的轮询分组，意思基本上就是：“A，现在你可以发送了。”好？所以，A 收到轮询消息后，如果有数据分组要发送，就会发送它的数据分组。

## 27 · 00:23:00 · 发送时长取决于载荷与速率

原标说话人 1  00:23:00
Okay, now we do not know, notice that we do not know, how long this transmission will be, right? Because it depends on the payload of this data packet, and it depends on the speed at which A will transmit toward the access point. But anyway, it will go on.
好，现在我们不知道，注意，我们不知道这次传输会持续多久，对吧？因为这取决于这个数据分组的载荷，也取决于 A 向接入点发送时采用的速率。不过，无论如何，传输会进行下去。

## 28 · 00:23:29 · 轮询C时合并下行数据

原标说话人 1  00:23:29
When A finishes, after SIFS the access point will poll the next station in the list, that, in our example, is C. Now, let us consider in this case that the access point has got some data to send to C. So, in this case, it will of course send a poll. But it will also send a payload with data, right? Because it wants to poll C, but it has also got some data to send to that node. So, it will send a poll, that is control information, plus data. And notice that, in this case, after SIFS we will have that C is entitled to transmit, access the channel and transmit a data packet.
A 发送结束后，再经过一个 SIFS，接入点就会轮询列表中的下一个站点，在我们的例子中就是 C。现在，假设接入点也有一些数据要发给 C。那么，它当然会发送轮询，但还会附带一个装有数据的载荷，对吧？因为它想轮询 C，同时又有数据要发给这个节点。所以，它会发送轮询，也就是控制信息，加上数据。注意，在这种情况下，经过一个 SIFS 后，C 就有权发送，也就是接入信道，发送一个数据分组。

## 29 · 00:24:47 · 快速ACK与头部捎带确认

原标说话人 1  00:24:47
Again, assuming that C has something to send. Okay? So, the polling scheme is very simple. The access point tells each station when it can access the channel. Okay. So, one important observation that we made already is that, whenever a station is entitled to access the channel, it accesses the channel and transmits one packet. For how long, we do not know a priori, right? It depends on the payload size and the data speed at which that node transmits. Okay, that is the first thing that we already said. The other thing that we need to say is how acknowledgments take place in this case, right? Because, so far, we have not highlighted any acknowledgment here. So, where is the acknowledgment? Well, when a station that has been polled by the access point transmits a data packet, if this data packet is correctly received by the access point, then, when the access point polls the next station, in the header it will also include a bit that represents the acknowledgment for the station that transmitted earlier. This is called fast ACK. That means we do not wait for the access point to poll that station, A in our example, again in order to send the ACK to A. Even if here the access point is polling a new station, C, the ACK bit in the header of this packet will refer to the previous transmission, so that, upon reading the header of this new packet sent by the access point, the previous station can see if its packet was successful or not. Okay? And if the access point transmits a data packet to a station, the station can include an ACK packet in the header of its own packet in order to ACK what the access point sent, if received successfully. Okay, so the way data are ACKed in this case is a bit different. We do not have a specific acknowledgment packet. We have acknowledgment bits in the header of the packets that are exchanged in order to notify whether the previous transmission has occurred successfully or not.
同样，这里假设 C 有东西要发送。好？所以，轮询机制很简单，接入点会告诉每个站点何时可以接入信道。我们已经提到过一个重要的观察：只要某个站点获得接入信道的权利，它就会接入信道并发送一个分组。发送多久，我们事先并不知道，对吧？这取决于载荷的大小，以及该节点发送时采用的数据速率。好，这是我们已经说过的第一点。另外还需要说明，在这种情况下是如何确认的，对吧？因为到目前为止，我们还没有在图中突出任何确认。那么，确认在哪里？当被接入点轮询的站点发送了一个数据分组，而且接入点正确收到了这个数据分组时，接入点在轮询下一个站点时，还会在头部中加入一个比特，表示对之前发送的那个站点的确认。这叫作快速 ACK。也就是说，我们不必等到接入点再次轮询那个站点，也就是例子中的 A，才给 A 发送 ACK。即使接入点在这里轮询的是一个新站点 C，这个分组头部中的 ACK 比特也会对应前一次传输。因此，前一个站点读到接入点发出的这个新分组的头部时，就能知道自己的分组是否发送成功。好？如果接入点向一个站点发送了数据分组，那么该站点可以在自己分组的头部中加入一个 ACK 分组，以便在成功收到接入点发送的内容后，对它进行确认。所以，这里确认数据的方式略有不同。我们没有一个专门的确认分组，而是在双方交换的分组头部中放入确认比特，以通知前一次传输是否成功。

## 30 · 00:28:38 · PCF用SIFS减少接入开销

原标说话人 1  00:28:38
The last thing we need to highlight here, so far, is that, as you may have noticed, during PCF all packets are spaced by SIFS, right? We do not have DIFS. We have just a short time spacing. Why? To increase the efficiency of the protocol and reduce the sensing time. Why can we do that? Because it is a contention-free period. There is no contention, right? So, there is no need for the nodes to actually sense the channel. It is the access point that makes decisions on who should access the channel. So, nodes do not need to sense the channel. There is no DIFS. There is only SIFS. Okay, good.
到这里，最后还需要强调的是，你们可能已经注意到了，在 PCF 期间，所有分组之间都间隔一个 SIFS，对吧？我们没有 DIFS，只有很短的时间间隔。为什么？为了提高协议的效率，减少侦听时间。为什么能这么做？因为这是无竞争期，没有竞争，对吧？所以，各节点实际上不需要侦听信道，而是由接入点决定谁应该接入信道。因此，节点不需要侦听信道。没有 DIFS，只有 SIFS。好，很好。

## 31 · 00:29:48 · 按列表继续轮询站点D

原标说话人 1  00:29:48
So, that said, let me just make one more case. So, now let us assume that, in the polling list, we have D. Okay? So, after having polled A and then C, now our access point will poll D. It just follows the list. So, it sends, let us say, in this case it does not have any data for D, so the access point just sends the D poll.
好，那么，说完这些，让我再举一种情况。所以，现在假设，在轮询列表中，我们有D。好吗？那么，轮询了A，然后轮询了C之后，现在接入点会轮询D。它只是遵循列表。所以，它发送，假设，在这种情况下，它没有任何给D的数据，所以接入点只发送D的轮询。

## 32 · 00:30:29 · 空分组与无竞争期结束

原标说话人 1  00:30:29
Okay, now D understands that it can access the channel and transmit, but D does not have anything to transmit. So, what can D do? Well, D can transmit a null packet. That is just nothing, right? It is a control packet that says, "I do not have any data in my queue. I do not have anything to transmit." Okay, why can this happen? Because, remember, this list has been compiled at the very beginning, upon association. So, in the following, at every superframe the access point uses PCF and polls the stations. They might have packets to transmit at that time or not. We do not know. At the beginning, during association, they just declared their interest in participating in PCF. But in real time, we do not know if they have got packets to transmit or not. So, this situation may happen. Okay? Now, when the access point wants to finish, terminate this contention-free period, it will send a packet, a control packet that is called contention-free period end. Essentially, it broadcasts to everyone that this phase is finished. Okay, so it is over, and this means that, in our previous representation, we are essentially here. The contention-free period is finished, and this means that everyone can start the subsequent phase, that is the contention period, during which we just use the DCF function that we know about.
好，现在 D 知道自己可以接入信道并发送，但 D 没有什么要发送。那么 D 能做什么？它可以发送一个空分组，也就是什么都没有，对吧？这是一个控制分组，意思是：“我的队列里没有数据，我没有东西要发送。”为什么会发生这种情况？记住，这张列表最初是在关联时建立的。之后，接入点在每个超帧中使用 PCF，轮询各个站点。到了那个时刻，它们可能有分组要发送，也可能没有，我们不知道。最开始关联时，它们只是表示有兴趣参与 PCF，但在实时运行中，我们不知道它们到底有没有分组要发送。因此，这种情况是可能发生的。好？现在，当接入点想结束、终止这个无竞争期时，它会发送一个分组，一个称为无竞争期结束的控制分组。它实际上是在向所有节点广播：这个阶段已经结束了。好，这一阶段结束了，在前面的图示中，我们基本上就到了这里。无竞争期结束，意味着所有节点都可以进入接下来的阶段，也就是竞争期。在这个阶段中，我们就使用已经学过的 DCF 功能。

# 六、信标延迟与PIFS优先权

## 33 · 00:33:05 · 超帧末尾与新信标

原标说话人 1  00:33:05
Okay, is this clear so far? Okay, so now we are here, right? We are at the end of the superframe. As we know, we will have the beacon and a new superframe will start, and everything will repeat again and again. But let us think for a moment about what happens at the end of this contention period, when we apply DCF.
好，到目前为止清楚吗？好，那么，现在我们在这里，对吧？我们在超帧的末尾。正如我们知道的，我们会有信标，一个新的超帧将开始，而且所有过程将一遍又一遍地重复。但是，让我们想一会儿，在这个应用DCF的竞争期结束时会发生什么。

## 34 · 00:33:43 · 目标信标发送时间TBTT

原标说话人 1  00:33:43
Okay? Why? Because we know that the beacon is a packet that the access point should broadcast periodically. But what if a station seizes the channel right before the beacon time? TBTT means target beacon transmission time. So, this is the time at which, in theory, the beacon should be transmitted, every 100 milliseconds.
好？为什么要考虑这个？因为我们知道，信标是接入点应当周期性广播的一个分组。但如果某个站点恰好在信标发送时刻之前占用了信道，怎么办？TBTT 指目标信标发送时间。因此，理论上信标就应该在这个时刻发送，每 100 毫秒一次。

## 35 · 00:34:20 · DCF传输可能跨越信标时刻

原标说话人 1  00:34:20
But the beacon can be transmitted when we finish DCF, right? And during DCF, our nodes contend for the channel according to the rules that we already know. So, assume that a node here has got a packet to transmit, senses the channel as idle for DIFS, and then it can access the channel and transmit the packet. And the packet transmission, of course, will run. And if the packet is transmitted successfully, it will have to receive the acknowledgment.
但是，信标要等 DCF 结束后才能发送，对吧？在 DCF 期间，各节点按照我们已经知道的规则竞争信道。因此，假设这里某个节点有分组要发送，它感知到信道空闲达一个 DIFS，然后就可以接入信道并发送分组。分组传输当然会持续一段时间，如果分组发送成功，它还得接收确认。

## 36 · 00:35:05 · 保护现有对话使信标延迟

原标说话人 1  00:35:05
So, what may happen is that this beacon may be delayed, because if we are finishing with this phase, we are not done yet. The access point has no way to interrupt an ongoing dialogue. So, this beacon transmission might be delayed. That is why I always said, more or less, the beacon is transmitted periodically. Why was I saying more or less?
因此，可能出现的情况是，信标被推迟了。因为这个阶段虽然快结束了，却还没有真正结束，接入点无法中断正在进行的对话，所以信标传输可能会延迟。这就是为什么我一直说，信标是差不多周期性地发送的。为什么说“差不多”呢？

## 37 · 00:35:39 · PIFS为接入点发送信标提供优先权

原标说话人 1  00:35:39
Because, in theory, the beacon transmission should be periodic, every 100 milliseconds. But if the access point finds the channel as busy, it cannot interrupt an ongoing dialogue to transmit the beacon. It has to wait, okay? So, this means that the beginning, the time at which a superframe can begin, is not deterministically predictable. It may be shifted. Okay. That said, however, the protocol wants to be, let us say, good to the access point. When the access point has to transmit the beacon, the protocol gives the access point an advantage, a small advantage. That is, the access point needs to sense the channel as idle only for PIFS. And PIFS is longer than SIFS, so we cannot interrupt an ongoing dialogue, but is shorter than the other interval, apparently DIFS, so we get priority with respect to any other data packet.
因为，理论上，信标传输应该是周期性的，每100毫秒一次。但是，如果接入点发现信道忙，它就不能中断正在进行的对话来发送信标。它必须等待，好吗？所以，这意味着，开始的时刻、一个超帧能够开始的时刻，不是可以确定性预测的。它可能会移动。好。不过，说完这些，协议想要，可以说，对接入点好一点。当接入点必须发送信标时，协议会给接入点一个优势，一个小优势。也就是，接入点只需要侦听到信道空闲一个PIFS。而PIFS比SIFS长，所以我们不能中断正在进行的对话，但是它比另一个间隔短，显然是DIFS，所以相对于任何其他数据包，我们获得了优先权。

![图34：The Four Interframe Spaces](../slide-images/slide-034.png)

课件：02-WiFi_1-7.pdf · PDF第17页下半页 · 图34（按PDF顺序）

## 38 · 00:37:01 · PIFS作用与PCF实践问题

原标说话人 1  00:37:01
And now we understand why we also have PIFS in the priority ladder of IFS. Okay, it is to give a small advantage to the access point to access the channel when it has to transmit the beacon. Okay, that said, we are done with PCF. As promised, this was indeed, let us say, fast. But what we need to just highlight are the issues. So, as I said, while looking at these techniques, we need to have a critical eye. We need to understand what is working, what does not work. And by doing that, in this case, we also understand why PCF is in the standard, is still in the standard, but it is not being implemented in practice. So, why?
现在，我们明白为什么在IFS的优先级阶梯中也有PIFS了。好，它是为了在接入点必须发送信标时，给它接入信道的一点小优势。好，说完这些，我们讲完PCF了。正如承诺的，这确实，可以说，讲得很快。但是，我们需要强调的就是这些问题。所以，正如我说过的，在看这些技术时，我们需要有批判的眼光。我们需要理解什么有效，什么无效。而通过这样做，在这个例子中，我们也理解了，为什么PCF在标准中，仍然在标准中，却没有在实践中实现。所以，为什么？

# 七、PCF服务质量目标与局限

## 39 · 00:38:07 · 低时延应用与确定性接入目标

原标说话人 1  00:38:07
Well, because PCF was introduced initially to provide some deterministic access in Wi-Fi, so that you could support quality of service. That means, when you have voice traffic, voice over IP, or you have video, video conferencing, video streaming, well, as we already said, these are types of applications that require low latency, okay? Otherwise, the quality of the service for the user is not good enough. If you have delays when you talk over Zoom or WeChat or other applications that you may use, well, you get annoyed, right? Because you start talking and the other person actually is overlapping with his voice. It is a mess. So, these kinds of applications really need low latency, low delay. If you think about how DCF works, based on contention, if Wi-Fi nodes have got packets to transmit, well, who knows when they get a chance to transmit? Okay? It is kind of random. It depends on how many nodes are there, how much traffic we have to transmit. It depends on the wireless channel conditions. There are many things that may go wrong.
因为最初引入 PCF，是为了在 Wi-Fi 中提供一定的确定性接入，从而支持服务质量。也就是说，当你有语音流量、IP 语音，或者有视频、视频会议、视频流时，正如我们已经说过的，这些都是要求低时延的应用。否则，对用户而言，服务质量就不够好。如果你在通过 Zoom、微信或其他应用交谈时出现延迟，你会感到烦躁，对吧？因为你开始说话时，对方的声音实际上会与你重叠，乱成一团。因此，这类应用确实需要低时延、低延迟。想想 DCF 基于竞争的工作方式：如果 Wi-Fi 节点有分组要发送，谁知道它们什么时候才能获得发送机会呢？这有一定的随机性，取决于有多少节点、有多少流量要发送，也取决于无线信道的条件。很多因素都可能出问题。

## 40 · 00:39:49 · PCF支持服务质量的初衷

原标说话人 1  00:39:49
So, the standard said, well, we need to introduce a different access scheme whenever we have traffic that needs to be transmitted with low delay. And that is why they initially specified PCF, because, as we said, in this case there is no randomness in access, right, in channel access. It is the access point that says, "You can transmit, you can transmit, you can transmit." So, it is more deterministic. So, you may wonder again, anyway, it is a good thing. It could help to support quality of service, reduce the delay that a node may experience when it needs to access the channel and transmit a packet. Why did they not implement it? So, what do you think? Why, why did they not implement this scheme? What is wrong with that?
所以，标准制定者说，如果有些流量需要以低时延发送，我们就需要引入另一种接入方案。这就是最初规定 PCF 的原因。因为正如我们所说，在这种情况下，接入没有随机性，对吧，我是说信道接入。接入点会说：“你可以发送，你可以发送，你可以发送。”所以，它更具有确定性。于是，你可能又会想，这毕竟是件好事。它可以帮助支持服务质量，减少节点在需要接入信道发送分组时可能经历的延迟。那为什么没有实现呢？你们觉得呢？为什么，为什么没有实现这个方案？它有什么问题？

## 41 · 00:41:02 · 轮询空包交换没有有效数据

原标说话人 1  00:41:02
One thing, a hint that I want to give you is, for example, focus on this possibility. Is this exchange useful? Is this efficient? No, right? It is poll, null. Where are the data there? No data. So, we waste time for really nothing.
嗯，有一点，我想给你们的一个提示是，比如说，关注这个可能性。这次交换有用吗？这高效吗？不，对吧？它是轮询、空包。那里的数据在哪里？没有数据。所以，我们确实是在为什么也没有的事情浪费时间。

## 42 · 00:41:36 · 静态轮询列表缺少实时队列信息

原标说话人 1  00:41:36
Because this may happen: the access point may poll a station that does not have any data. The access point does not have any data for that station, and still, according to PCF, if D is in the list, I have to poll it, the access point has to poll it. This is not good, right? There is the possibility of having a significant inefficiency there because of the fact that the polling list has been compiled at the beginning, and we do not have real-time information on the status of the queues, how many packets each node actually has to transmit. So, we just follow this initial list. That is not efficient. So, that is the first problem: kind of stale information in the polling list, because we just follow the expression of interest of the nodes, but not their actual need to transmit a packet at a certain point in time. So, this is the first problem that we have.
因为这种情况是可能发生的：接入点轮询了一个没有任何数据的站点，而接入点自己也没有数据要发给这个站点。可是按照 PCF，只要 D 在列表里，我就得轮询它，接入点就得轮询它。这不好，对吧？这里可能存在很明显的低效，因为轮询列表是在最开始建立的，我们没有关于队列状态的实时信息，不知道每个节点实际上有多少分组需要发送。所以，我们只是照着最初的这张列表走，这没有效率。这就是第一个问题：轮询列表中的信息有些陈旧。我们只是依据节点曾经表达过的参与意愿，而不是它们在某个具体时刻是否真的需要发送分组。这就是我们的第一个问题。

![图60：Why PCF Never Really Happened](../slide-images/slide-060.png)

课件：02-WiFi_1-7.pdf · PDF第30页下半页 · 图60（按PDF顺序）

## 43 · 00:42:58 · 信标推迟导致不可预测的服务延迟

原标说话人 1  00:42:58
Another, another problem that we have is that, as mentioned, right, sorry, here we have, at the end of PCF, we have the DCF phase, like shown in that picture. And after DCF, then we have again the beacon, but, as discussed already, the beacon may need to be shifted. So, whatever traffic should have been polled here in this new superframe will be delayed, and we do not know in advance if that will be delayed or for how long. That is another problem because, again, your goal in PCF was to provide deterministic channel access and control the delay. You do not want unpredictable delay in accessing the channel. You want to control the delay. So, if you are not sure about when a superframe can actually start, well, that is not a good start at all to control the delay.
另外，另一个问题是，正如刚才提到的，对，抱歉，在 PCF 结束后还有一个 DCF 阶段，就像图中所示。DCF 之后又会有信标。但我们已经讨论过，信标可能需要推迟。因此，这个新超帧中原本应当通过轮询得到服务的任何流量都会被延迟，而且我们事先不知道是否会延迟，也不知道会延迟多久。这又是一个问题，因为 PCF 的目标本来就是提供确定性的信道接入并控制延迟。你不希望接入信道时遇到不可预测的延迟，而是希望控制延迟。所以，如果连一个超帧究竟什么时候能开始都不确定，那么对于控制延迟来说，这实在算不上一个好的开端。

## 44 · 00:44:31 · PCF第二项局限与第三项问题预告

原标说话人 1  00:44:31
So, this is the second major issue with PCF. Okay, no ability to control when actually the PCF phase, the superframe and, of course, the next PCF phase can start. And there is a third issue that we are going to explain in five minutes. That is the last one. If you want to think about it while we have a short break, you can look at that picture and try to think what could be this third issue.
所以，这就是PCF的第二个主要问题。好，无法控制PCF阶段、超帧，当然还有下一个PCF阶段，实际上什么时候能够开始。而且还有第三个问题，我们五分钟后会解释。那是最后一个。如果你们想在短暂休息时思考一下，可以看看那张图，试着想想，这第三个问题可能是什么。

