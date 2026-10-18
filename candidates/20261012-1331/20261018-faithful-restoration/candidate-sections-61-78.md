# 20261012-1331 · 第61–78段忠实恢复候选

仅本地候选，未写回飞书，未逐句人工听辨。方括号为待听辨；讲者重复、时态、口语语法与限定语保留。中文逐句对应，正文每段英文下紧接中文。

来源：原飞书历史快照、校订前Qwen恢复输出、新无提示medium.en；来源分歧不以模型票数裁定。原飞书可能已人工编辑，Qwen不是丢失首次输出；旧、新M4A哈希不同，尚未取得旧音轨作等同性验证。

## 61 · 01:13:44

So again, in order to understand how useful [a / the unclear] mechanism is, or solution is, let's play our little game of ablation, right? So let's remove the post-backoff and see what happens. So what if A does not have to run any, [any unclear] post-backoff? Well, let's add an event here to better understand what would happen considering all possible cases.
所以，再一次，为了理解[一种／这一个，待听辨]机制有多有用，或者解决方案有多有用，让我们玩一下我们的小小消融游戏，对吧？所以，让我们去掉发送后退避，看看会发生什么。所以，如果A不必执行任何、[任何，重复待听辨]发送后退避，会怎么样？嗯，让我们在这里加一个事件，考虑所有可能的情况，来更好地理解会发生什么。

## 62 · 01:14:31

Let's consider that A has got another packet in [a unclear] its MAC queue. Remember that we said the MAC layer can be modeled, right, as a queue with a server. So let's consider that A has transmitted the packet here successfully, but let's assume that A has [got / put unclear] another packet in the queue waiting to be transmitted. So this first packet goes through, right, successfully. This is what we [represented / represent unclear] here. But now A has got another packet right here, right?
让我们考虑A在[一个，待听辨]它的MAC队列里又有了一个数据包。记住，我们说过，MAC层可以被建模，对吧，建模成一个带有服务台的队列。所以，让我们考虑A已经在这里成功地发送了这个数据包，但让我们假设A在队列里[还有／放入了，待听辨]另一个等待发送的数据包。所以，这第一个数据包通过了，对吧，成功地通过了。这就是我们在这里[已经表示出的／所表示的，时态待听辨]内容。但现在A在这里又有了一个数据包，对吧？

## 63 · 01:15:22

So when [it's / he's unclear] done with this dialogue, [we'll / we unclear] have another packet to deal with. So what if A didn't have any post-backoff to run? Well, [it / he / you unclear] will have to sense the channel for DIFS. The channel is idle, and [it / you unclear] will be able to access the channel [and transmit / trust me unclear]. So [it / you unclear] will have to transmit its [other / own unclear] data. This may be successful. And what would be that? Would that be fair with respect to B and C?
所以，当[它／他，待听辨]完成这轮对话时，我们[将会有／有，待听辨]另一个数据包要处理。所以，如果A没有任何发送后退避要执行，会怎么样？嗯，[它／他／你，待听辨]将必须侦听信道一个DIFS的时间。信道是空闲的，而[它／你，待听辨]将能够接入信道[并发送／相信我，待听辨]。所以，[它／你，待听辨]将必须发送它的[其他／自己的，待听辨]数据。这可能会成功。那这会是什么情况？这对B和C来说会公平吗？

## 64 · 01:16:10

The poor B and C are waiting [right there unclear], their backoff time, and A just gets the next packet and go ahead with its transmission. So this is unfair. And indeed, if a Wi-Fi card like A has got several packets to transmit, under this situation without post-backoff, we just continue accessing the channel and transmitting its packets. With very high probability, [it / you unclear] will actually seize the channel for a very long time and transmit, transmit, transmit, while the others [will have / we have / we had unclear] to wait, wait, [and unclear] wait, because the channel [will / would unclear] become busy [confused unclear]. And this was indeed observed, also experimentally. Years ago, some researchers made experiments with different Wi-Fi cards. [They / which unclear] were commercial products. They claimed, all these cards [claimed / claim unclear] to follow the standard. [Of course / for unclear] products must follow the standard. They [claimed / claim unclear] to do that. But actually, one of these cards was applying everything, okay, as specified by the standard, but the post-backoff.
可怜的B和C[就在那儿，待听辨]等着，等它们的退避时间，而A只是拿到下一个数据包，就继续它的发送。所以，这是不公平的。而且确实，如果像A这样的Wi-Fi网卡有好几个数据包要发送，在这种没有发送后退避的情况下，我们就一直接入信道，并发送它的数据包。以非常高的概率，[它／你，待听辨]实际上会占据信道很长时间，并且发送、发送、发送，而其他那些[将必须／我们必须／我们过去必须，待听辨]等、等、[并且，待听辨]等，因为信道[将会／会，待听辨]变忙[后词疑似confused，待听辨]。而且，这也确实在实验中被观察到了。几年前，一些研究人员用不同的Wi-Fi网卡做了实验。[它们／这些，连接形式待听辨]是商业产品。它们声称，所有这些网卡都[声称过／声称，时态待听辨]遵循标准。[当然／因为，待听辨]产品必须遵循标准。它们[声称过／声称，时态待听辨]自己这样做。但实际上，这些网卡中的一张实施了标准所规定的所有内容，好吧，唯独发送后退避除外。

## 65 · 01:17:42

And what these researchers observed was that this Wi-Fi card was [obtaining / obtained unclear] a very, very high throughput; that means the ability to transmit a lot of data, while the other Wi-Fi cards were starving, so they could not get access to the channel. A very unfair service, and this is because, this was because that commercial Wi-Fi card at that time did not implement the post-backoff procedure.
而这些研究人员观察到的是，这张Wi-Fi网卡当时[正在获得／obtained形式，待听辨]非常、非常高的吞吐量；那意味着发送大量数据的能力，而其他Wi-Fi网卡则处于饥饿状态，所以它们无法接入信道。一种非常不公平的服务，而这是因为，当时这是因为，那张商业Wi-Fi网卡在那个时候没有实现发送后退避程序。

## 66 · 01:18:22

So this seems to be, you know, a detail or one more thing that a node has to do, but it's actually extremely important to ensure fairness. In Wi-Fi, we want to be fair, we want to give the same probability to everyone in channel access. So it is a very important feature, and notice that the same would happen if we didn't have the post-backoff procedure. Even if A, right after its, [its unclear] completion, successful completion of, [of unclear] its dialogue, didn't have any packet. But even in the case where it gets a packet right after, [a unclear] few microseconds after, [it / you unclear] will still get an advantage [with unclear] respect to B and C, who must run the backoff. So that's why the standard says, no matter what your MAC queue state is, we don't care. Once you complete a transmission successfully, you must run the post-backoff procedure, [right / okay unclear]? So that's, [it's unclear] that's mandatory. We cannot do [anything otherwise / any, any number one unclear]. Help me out here. We, [we unclear] have the long break now? [No / oh unclear], sorry. Our time [three five, five plus three; numbers unclear]. Okay, thanks. Okay, so we still have about fifteen minutes before. Let me know if I [get it wrong / get this one wrong / did something wrong unclear], please. I need to adjust the, [the unclear] schedule, of course. Okay, so we run essentially through all these slides, using the whiteboard for greater clarity, but you have the essential information also in, [in unclear] the slides. Okay, so what I would like to show now is another example that is here presented in [the / these unclear] slides. Don't get scared by the many figures that are used in these, [in these unclear] slides. It's just to highlight something that we already know, but here you have indeed concrete example to further emphasize this. That is, we now know more or less how the basic version of Wi-Fi works. We already said that Wi-Fi is so successful because it works quite well for our needs. But it has got a big problem in general, that is overhead, right? We already commented on that. So now that we know how channel is used in Wi-Fi, this is a practical example that gives evidence to that.
所以，这似乎是，你知道，一个细节，或者一个节点必须多做的一件事，但它实际上对于保证公平性极其重要。在Wi-Fi中，我们想要公平，我们想在信道接入方面给予每个人相同的概率。所以，这是一个非常重要的特性，而且注意，如果我们没有发送后退避程序，同样的情况就会发生。即便A，恰好在它的、[它的，重复待听辨]完成之后，成功完成了、[了，of重复待听辨]它的对话之后，没有任何数据包。但即便在它随即收到一个数据包的情况下，几微秒之后，[few前的a待听辨]，[它／你，待听辨]相对于B和C仍会得到一个优势，[with是否存在待听辨]，而B和C必须执行退避。所以，这就是为什么标准说，不管你的MAC队列处于什么状态，我们不在乎。一旦你成功完成一次发送，你就必须执行发送后退避程序，[对吧／好吧，待听辨]？所以，那是，[它是，待听辨]，那是强制的。我们不能[用其他方式做任何事／any, any number one残片，待听辨]。在这里帮我一下。我们，[我们，重复待听辨]现在要放长课间了吗？[不／哦，待听辨]，抱歉。我们的时间[three five, five plus three；数字及其含义待听辨]。好，谢谢。好，所以在那之前我们还有大约十五分钟。如果我[弄错了／把这一次弄错了／做错了什么，待听辨]，请告诉我。当然，我需要调整这个、[这个，重复待听辨]时间安排。好，所以我们基本上讲过了所有这些幻灯片，为了更清楚而使用了白板，但你们在、[在，重复待听辨]幻灯片中也有这些基本信息。好，所以我现在想展示的是在这里的[这些／该组，指示词待听辨]幻灯片中呈现的另一个例子。不要被这些、[这些，in these重复待听辨]幻灯片中使用的许多图示吓到。这只是为了突出我们已经知道的某件事，但在这里，你们确实有一个具体的例子，来进一步强调这一点。也就是说，我们现在或多或少知道Wi-Fi的基本版本是如何工作的。我们已经说过，Wi-Fi如此成功，是因为它能相当好地满足我们的需求。但总的来说，它有一个大问题，那就是开销，对吧？我们已经就此作过评论。所以，既然我们现在知道在Wi-Fi中信道是怎样被使用的，这就是为这一点提供证据的一个实际例子。

## 67 · 01:21:58

So we know that in the case where we need to transmit [the / a unclear] data packet, first of all we need to sense the channel for DIFS. We can consider [DIFS / this unclear] to be fifty microseconds long. So that's for sure something that we need to wait for. Then if we are lucky, if we are lucky, the channel is idle, and we can transmit our packet right away. But the packet that we transmit, we [know already / already know unclear] that [it unclear] has got some headers, right? Actually, we already said it has got a physical layer preamble that is used by the transmitter and receiver to essentially synchronize, and so that the receiver can start [to unclear] demodulating what the transmitter is sending. So at the electronics level, they need this preamble to start the, [the, let's see unclear] communication. And then there is the physical layer header, and then there is the physical, sorry, the MAC layer header, where we have, for example, the duration field. So all these headers are just control information. It's not [a / the unclear] payload. It's not something useful at the MAC layer. It is something that is there. It is useful for the protocol, but not, they are not application layer bits, right? So [they are / you're unclear] there, fine, but from the application, from what would be the application layer perspective, that's something that is not useful, it's not interesting.
所以，我们知道，在我们需要发送[这个／一个，待听辨]数据包的情况下，首先我们需要侦听信道一个DIFS的时间。我们可以认为[DIFS／这个，待听辨]持续五十微秒。所以，那肯定是我们需要等待的一段时间。然后，如果我们幸运，如果我们幸运，信道是空闲的，我们就可以立即发送我们的数据包。但是，我们发送的这个数据包，我们[已经知道，know与already词序待听辨]，[it是否存在待听辨]它有一些首部，对吧？实际上，我们已经说过，它有一个物理层前导码，由发送方和接收方用来基本上实现同步，并使接收方能够开始[to是否存在待听辨]解调发送方正在发送的内容。所以，在电子电路层面，它们需要这个前导码来开始这、[这，让我们看看，待听辨]通信。然后有物理层首部，接着有物理，抱歉，MAC层首部，其中我们有，例如，时长字段。所以，所有这些首部都只是控制信息。它不是[一个／该，冠词待听辨]有效载荷。它不是在MAC层有用的东西。它是存在在那里的某种东西。它对协议是有用的，但不是，它们不是应用层的比特，对吧？所以，[它们／你，待听辨]在那里，好吧，但从应用，从所谓的应用层角度来看，那是没有用的东西，是没有意思的东西。

## 68 · 01:23:51

Okay. So, [but / when unclear] we spend time to transmit [this / these unclear] physical layer preamble, physical layer header, and they are transmitted at the basic rate. So as we commented already, the basic rate is a low speed. So they are transmitted slowly at low speed. And if you consider the basic rate, like in this example, to be one megabit per second, well then you have to wait; it takes time to do that. And then we have the MAC header.
好。所以，[但是／当，待听辨]我们花时间来发送[这个／这些，待听辨]物理层前导码、物理层首部，而它们是以基本速率发送的。所以，正如我们已经评论过的，基本速率是一个低速率。所以，它们被慢慢地以低速率发送。而且，如果你认为基本速率，像这个例子中一样，是每秒一兆比特，那么，嗯，你就必须等待；做这件事需要时间。然后我们还有MAC首部。

## 69 · 01:24:28

The MAC header again are, [I would say / we say / it's a unclear] non-interesting bits from the point of view of the application. The size of the MAC header in Wi-Fi may actually vary, depending on, for example, how many addresses you need. So if you are in a BSS, isolated BSS, as the one that you have got in your apartment, the only addresses that you need are the transmitter address and [a unclear] receiver address.
MAC首部又是，[我会说／我们说／它是一个，待听辨]，从应用的角度来看没有意思的比特。Wi-Fi中的MAC首部大小实际上可能会变化，这取决于，例如，你需要多少个地址。所以，如果你处在一个BSS中，一个孤立的BSS，就像你公寓里有的那一个，你需要的地址就只有发送方地址和[一个，a是否存在待听辨]接收方地址。

## 70 · 01:25:04

If you are in an extended service set, like here on Tongji campus [place-introduction wording unclear], where we have many access points connected through, you know, the, the wired network. Then you may need four different addresses, and the reason for that is that, in an extended service set, you may have, as we know, access points that are connected to each other, right? We already explained the architecture of the network.
如果你处在一个扩展服务集里，就像这里的同济校园〔引出地点的措辞待听辨〕，这里我们有许多接入点，通过，你知道的，这个、这个有线网络连接起来。那么你可能需要四个不同的地址，而其原因是，在一个扩展服务集中，你可能有，正如我们所知道的，彼此连接的接入点，对吧？我们已经解释过这个网络的架构。

## 71 · 01:25:52

And so, if you are A and you want to send a packet to B, well, then you have to send your packet to the access point you are connected with. This access point one will send the packet to access point two, and then access point two will deliver the packet to B. This happens in an extended service set.
所以，如果你是A，并且你想把一个数据包发送给B，嗯，那么你必须把你的数据包发送给与你连接的那个接入点。这个接入点一会把这个数据包发送给接入点二，然后接入点二会把这个数据包递送给B。这发生在一个扩展服务集中。

## 72 · 01:26:20

Okay, now in this case, A is the sender, okay, the transmitter, so it's [the/your unclear] original source and also transmitter of the packet. And access point one is the receiver, but the final destination is B. So, this packet that travels from A to access point one will have A as the transmitter address, which is also the source's address. You will have access point one address as a receiver, and then you will have the destination address, the B's address as destination address. So it needs to have three addresses in the MAC header. Once the packet is received at access point one, [and unclear] access point one has to send the packet to access point two, so that the packet eventually can be delivered to the final destination. This packet, when the packet is here, it [needs/means/names unclear] four addresses in the [MAC unclear] header. Why? Because we need to [specify/specifying unclear] that this packet originally came from source A. The transmitter now is access point one. The receiver now is access point two. And the final destination where this packet has to go is B, right? So, in extended service sets, when the Wi-Fi packets travel from one access point to another, they need four addresses. So this is just to say that the size of the MAC header may vary, okay, may be shorter or longer. Anyway, [um unclear], so you already have to account for [DIFS/SIFS unclear], physical preamble, physical header, MAC header. The payload is the useful, interesting part. [Okay, so that's not overhead; wording unclear]
好，现在在这种情况下，A是发送方，好，发送机，所以它是〔the/your，限定词待听辨〕最初的源，同时也是这个数据包的发送方。而接入点一是接收方，但是最终目的地是B。所以，这个从A传到接入点一的数据包，会把A作为发送方地址，这同时也是源的地址。你会把接入点一的地址作为接收方地址，然后你会有目的地址，B的地址作为目的地址。所以它需要在MAC首部中有三个地址。一旦这个数据包在接入点一被接收，〔and，连接词有无待听辨〕接入点一就必须把这个数据包发送给接入点二，这样这个数据包最终才能被递送到最终目的地。这个数据包，当这个数据包在这里时，它〔needs/means/names，需要/意味着/说出，待听辨〕四个地址，在〔MAC有无待听辨〕首部里。为什么？因为我们需要〔specify/specifying，词形待听辨〕说明这个数据包最初来自源A。现在的发送方是接入点一。现在的接收方是接入点二。而这个数据包必须到达的最终目的地是B，对吧？所以，在扩展服务集中，当Wi-Fi数据包从一个接入点传到另一个接入点时，它们需要四个地址。所以这只是要说明，MAC首部的大小可能变化，好，可能更短或者更长。总之，〔um，语气词有无待听辨〕，所以你已经必须把〔DIFS/SIFS待听辨〕、物理层前导码、物理层首部、MAC首部计算在内。有效载荷是有用的、有意思的部分。〔好，所以那不是开销；此句措辞待听辨〕

## 73 · 01:29:08

But then, if the packet is hopefully, so in the best case, delivered successfully, you have SIFS. That is [another time interval / another time you have ... interval; wording unclear] you have to wait for. And then acknowledgment, that is a control packet, so not interesting from the application point of view.
但是然后，如果这个数据包，希望如此，所以是在最好的情况下，被成功递送了，你会有SIFS。那是〔another time interval / another time you have ... interval，另一段时间间隔及可能的起句重说，待听辨〕，你必须等过的。然后是确认，那是一个控制包，所以从应用的角度看并不有意思。

## 74 · 01:29:30

And the acknowledgment again is made of physical preamble, physical header, MAC header, so lots of things to be transmitted. And that's the best case. So, you, to transmit the payload, you have to wait [DIFS/SIFS unclear], transmission of physical layer preamble, physical layer header, MAC header, and then SIFS, and then ACK. [Okay unclear], lots of time to just transmit [a/the/zero-article unclear] payload.
并且这个确认又由物理层前导码、物理层首部、MAC首部构成，所以有许多东西要传输。而且那还是最好的情况。所以，你，为了传输有效载荷，你必须等待〔DIFS/SIFS待听辨〕、物理层前导码的传输、物理层首部、MAC首部，然后是SIFS，然后是ACK。〔Okay有无待听辨〕，要用很多时间，就为了传输〔a/the/无冠词待听辨〕有效载荷。

## 75 · 01:30:04

So you better have a long payload because otherwise your protocol is very, very inefficient, [okay unclear]. And this is the best case. If your transmission fails and you have to perform backoff and retransmit the packet, then you have to wait for the channel to become idle. [DIFS/SIFS unclear], backoff time. Hope that the channel remains idle and you can decrease the backoff counter continuously and over time reach zero, and then transmit your packet, and then SIFS and ACK. Lots of things, right? Just again to transmit a single [payload/failure unclear].
所以你最好有一个长的有效载荷，因为否则你的协议就非常、非常低效，〔okay有无待听辨〕。而且这是最好的情况。如果你的传输失败了，并且你必须执行退避并重传这个数据包，那么你必须等待信道变为空闲。〔DIFS/SIFS待听辨〕，退避时间。希望信道保持空闲，而且你能够持续地递减退避计数器，并随着时间推移到达零，然后传输你的数据包，然后是SIFS和ACK。很多东西，对吧？仅仅又是为了传输一个〔payload/failure，有效载荷/失败，待听辨〕。

## 76 · 01:30:46

So, we [realize/realized unclear] that the efficiency of Wi-Fi is actually pretty low. And this holds, unfortunately, for all versions of Wi-Fi. Okay, we [looked / are looking / have looked unclear] at the basic version, but it's actually a curse for all versions. And on average, you can consider that the efficiency of this scheme is about fifty, fifty-five percent, which is definitely low, right? The maximum efficiency [would/will unclear] be one hundred percent. [So, yeah, hopefully / so, we are halfway; unclear]
所以，我们〔realize/realized，时态待听辨〕认识到，Wi-Fi的效率实际上相当低。而且不幸的是，这对所有版本的Wi-Fi都成立。好，我们〔looked/are looking/have looked，时态待听辨〕看的是基础版本，但是它实际上是所有版本的一个诅咒。而且平均来看，你可以认为这个方案的效率大约是百分之五十、五十五，这确实很低，对吧？最高效率〔would/will，情态或时态待听辨〕是百分之百。〔So, yeah, hopefully / so, we are halfway，所以，是的，希望如此／所以，我们到了一半；待听辨〕

## 77 · 01:31:25

Okay, that said, we are just missing one last mechanism in the Wi-Fi channel access, and then we are done with the basic version of Wi-Fi, that is the most important one. Okay, so we just [need/needed unclear] to introduce, and we do that after the break, this last piece [for ... unclear] of the protocol that is related to what, actually, something that we know already about, the famous [four/for/form unclear] interframe space, the extended IFS. Remember the extended IFS. Remember the priority ladder, we have SIFS, PIFS, [DIFS/PIFS unclear], and extended IFS. So, we [said/start unclear], let's first focus on SIFS and [DIFS/PIFS unclear], understand how they are used, and then we'll go back to the other [time/timing unclear] intervals. So, now it's time to talk about the longest among these [time/timing unclear] intervals. That was indeed the extended IFS. And just to give you an idea, this extended IFS, [so/or unclear] this [time/timing unclear] interval, can be as long as about three hundred microseconds, so definitely longer than the others that we have considered so far.
好，说到这里，我们在Wi-Fi信道接入中就只剩最后一个机制还没有讲，然后我们就讲完Wi-Fi的基础版本了，那是最重要的一个版本。好，所以我们只是〔need/needed，时态待听辨〕需要介绍，而且我们在休息之后来做这件事，这最后一部分〔for，起句词有无待听辨〕协议，它关联到什么，实际上，关联到我们已经知道的一些东西，那著名的〔four/for/form，确切措辞待听辨〕帧间间隔，扩展IFS。记住扩展IFS。记住这个优先级阶梯，我们有SIFS、PIFS、〔DIFS/PIFS待听辨〕，还有扩展IFS。所以，我们〔said/start，确切措辞待听辨〕，我们先关注SIFS和〔DIFS/PIFS待听辨〕，理解它们是怎样使用的，然后我们再回到其他的〔time/timing，时间修饰词待听辨〕间隔。所以，现在到了讨论这些〔time/timing，时间修饰词待听辨〕间隔中最长的那个的时候了。那确实就是扩展IFS。而且，只是为了让你有个概念，这个扩展IFS，〔so/or，所以/或者，待听辨〕这个〔time/timing，时间修饰词待听辨〕间隔，可以长到大约三百微秒，所以肯定比我们到目前为止考虑过的其他那些更长。

## 78 · 01:33:12

Okay, it depends on the version of Wi-Fi that we consider, but just [yeah / you know / no filler; unclear], to keep in mind, again, [you can be considered; subject/construction unclear] equal to three hundred microseconds. [Okay unclear], so just to [have an idea / verify / evaluate; unclear]. So if I'm not wrong, now we stop for twenty-five minutes. Okay.
好，这取决于我们考虑的是Wi-Fi的哪个版本，但是只是〔yeah / you know / 无语气词；待听辨〕，为了记在心里，再说一次，〔你可以被认为；主语/句式待听辨〕等于三百微秒。〔Okay有无待听辨〕，所以只是为了〔have an idea / verify / evaluate，有个概念/核实/评估，待听辨〕。所以，如果我没有记错，现在我们停二十五分钟。好。

