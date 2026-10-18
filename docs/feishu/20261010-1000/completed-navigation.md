<!-- Generated from completed live Feishu blocks; original bilingual repository files are not replaced. -->

会议主题：录音机-20261010-1000  
课程：移动与传感器网络 / Mobile Sensor Networks  
上传时间：2026年10月14日（周三） 09:30 （GMT+08）  
音频时长：约 01:37:19  
整理日期：2026年10月18日  
版本：完整忠实双语稿 · 913cf98f5b3c  
状态：双语正文已完成（76 对）；已匹配插入9张课件图；76个分段标题与9个主题标题已加入原生目录

[原录音附件：20261010-1000.m4a](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcngX1q9Xf5ibGfDprymE00Ef)

录音文件：[点击打开原始录音并播放](https://lcn6dqn3m0yr.feishu.cn/minutes/obcnl1lg3zib7324wh4f2i69)

文字来源：[原始文字记录](https://lcn6dqn3m0yr.feishu.cn/docx/NGDxdSPFdor3LixorLVcWE91n6f)

课件来源：[02-WiFi_1-7.pdf](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf)

# 隐藏终端与基本DCF的碰撞

## 01 · 00:00:00 · 更新课件中的节点标号

原标说话人 1  00:00:00  
Resume. As mentioned, I changed the label of these nodes in order to make it easier for you, so that we are always assuming Wi-Fi working with an access point. Just to stress that in your slides, in the copy of the slides that you've got, there are the old labels. OK, so you need to update the labels according to what we are showing here. OK.  
继续。正如提到过的，我改变了这些节点的标号，为的是让你们更容易理解，这样我们就始终假设Wi-Fi是在有接入点的情况下工作。只是要强调一下，你们的幻灯片，也就是你们拿到的那份幻灯片里，还是旧标号。好，所以你们需要按照这里显示的内容更新标号。好。

## 02 · 00:00:44 · 引入隐藏终端场景

[课件图片：课件：02-WiFi_1-7.pdf · PDF第20页下半页 · 图40（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcn8wHpcCeDj9ms7e2Vt1rw8b)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

原课件保留旧标号；根据课堂00:00:00–00:01:59，从左到右原图A、B、C分别对应课堂A、接入点、B。两端用户节点相互隐藏，均可与中间接入点通信。

原标说话人 1  00:00:44  
Now, as mentioned, we now move from the simple scenario, the simple scenario that we considered earlier, where we had an access point and all user nodes that were able to hear each other, to a scenario where instead we have the access point, and now let's consider, for simplicity, just two user nodes A and B. Both A and B can hear the access point, and the access point can of course hear the user nodes. OK, so each user node is connected with the access point, but the two user nodes A and B cannot hear each other. So this is a scenario that often happens in practice, and it's called a hidden terminals scenario, where the terminals are the user nodes.  
现在，正如提到过的，我们从比较简单的场景，也就是前面考虑过的那个简单场景，转向另一个场景。在之前的场景中，我们有一个接入点，而且所有用户节点都能听到彼此；而在这个场景里，我们有接入点，现在为了简单起见，只考虑两个用户节点A和B。A和B都能听到接入点，而且接入点当然也能听到用户节点。好，所以，每个用户节点都连接着接入点，但是两个用户节点A和B不能听到彼此。所以，这是一种实践中经常出现的场景，它叫作隐藏终端场景，其中终端就是用户节点。

## 03 · 00:01:59 · 无线覆盖范围与相互隐藏

原标说话人 1  00:01:59  
And they are hidden with respect to each other because they cannot, let's say, see, electromagnetically speaking, each other. They cannot hear each other. OK, so let's try and apply the previous scheme that we saw can be used to this scenario. In this figure, you may notice that these circles represent the radio range of A and of B. OK? So this essentially highlights the fact that both A and B can hear the access point, because the access point is within the radio range of A and also within the radio range of B, while instead A and B are hidden with respect to each other. Indeed, if you look at the radio range of A, B is outside, and if you look at the radio range of B, A is outside. And the radio range is the area where, if there are other nodes, I can hear from them and I can transmit potentially to them. If they are outside my radio range, it means that they are outside my reach.  
而且，它们相对于彼此是隐藏的，因为它们不能，可以说，从电磁的角度，看到彼此。它们不能听到彼此。好，所以我们试着把前面见过的、可以使用的那个方案应用到这个场景中。在这张图里，你们可能注意到，这些圆代表A和B的无线电覆盖范围。好吗？所以，这基本上突出了这样一个事实：A和B都能听到接入点，因为接入点位于A的无线电覆盖范围内，也位于B的无线电覆盖范围内；相反，A和B相对于彼此是隐藏的。确实，如果你看A的无线电覆盖范围，B在外面；如果你看B的无线电覆盖范围，A在外面。而无线电覆盖范围就是这样一个区域，如果有其他节点在那里，我就能听到它们，也可能向它们发送。如果它们在我的无线电覆盖范围之外，就意味着它们超出了我的可达范围。

## 04 · 00:03:50 · A先发送、B随后侦听

原标说话人 1  00:03:50  
OK, now, is this scenario clear? OK, so let's assume that both A and B now have got a packet to transmit. Actually, A gets this packet, data packet, from its higher layers first. It senses the channel; the channel currently is idle. A listens to the channel for DIFS, right, for DIFS. The channel is idle, so A says, well, I can transmit my packet, and starts transmitting the packet to the access point. While this is going on, also B gets a packet from its higher layers. The packet reaches, right, the MAC server at B. So this MAC function on B starts listening to the channel and listens to the channel for DIFS.  
好，现在，这个场景清楚了吗？好，那么，假设A和B现在都有一个数据包要发送。实际上，A先从它的高层收到这个包、数据包。它侦听信道；信道目前是空闲的。A监听信道一个DIFS，对，一个DIFS。信道空闲，所以A说，嗯，我可以发送我的数据包，于是开始向接入点发送数据包。当这个过程正在进行时，B也从它的高层得到一个数据包。这个包到达，对，到达B的MAC服务模块。所以，B上的这个MAC功能开始监听信道，并监听信道一个DIFS。

## 05 · 00:05:23 · 隐藏终端碰撞与ACK缺失

原标说话人 1  00:05:23  
Remember, A and B cannot hear each other, right? So even if A is already transmitting to the access point, B senses the channel as, as idle. Thank you, as idle. OK, good. So this means that B too will start transmitting toward the access point after a DIFS time. Now we have a partial overlap of the two transmissions at the access point. That means that part of these packets cannot be demodulated correctly by the access point, right? So that part that overlaps is wasted. The access point will not acknowledge any of these packets, because both of them will report errors. Partially, for both of them, the SNR, the SINR will be too low. And the access point, experiencing this collision because the two signals at the access point collide, will not be able to demodulate either packet correctly. So, as I said, there is no acknowledgment for anybody here. Both transmissions fail. Do you agree?  
记住，A和B不能听到彼此，对吧？所以，即使A已经在向接入点发送，B侦听到的信道仍然是、是空闲的。谢谢，是空闲的。好，很好。所以，这意味着B在一个DIFS时间之后，也会开始向接入点发送。现在，两次传输在接入点处发生部分重叠。这意味着，这些数据包的一部分不能被接入点正确解调，对吧？所以，重叠的那部分就浪费了。接入点不会确认这些数据包中的任何一个，因为两者都会报告错误。在一部分时间内，对于两者来说，SNR、SINR都会太低。而接入点，由于两个信号在接入点处碰撞，经历了这个碰撞，就无法正确解调任何一个数据包。所以，正如我说的，这里没有任何一方能得到确认。两次传输都失败。你们同意吗？

# RTS/CTS握手与NAV

## 06 · 00:07:25 · 引入带握手的DCF

[课件图片：课件：02-WiFi_1-7.pdf · PDF第21页上半页 · 图41（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcnyMzsPsZq3LyTArSo1HiWsc)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

原标说话人 1  00:07:25  
OK, so this is bad, because we just wasted radio resources, right? The two nodes try to transmit, both of them fail, total failure. This means that the basic scheme that we looked at earlier is not working really good when there are hidden nodes. So what the standard says is, well, let's introduce a slightly different version of the basic scheme that can be used to make channel access more efficient. This is the scheme with the so-called explicit channel reservation, or it is also called DCF with handshake. OK? Why? Why? Let me show you a figure that is easier to understand. In this second version of the DCF, what we have is the possibility to have a handshake before the actual data packet transmission. A handshake is when you shake hands, right, with someone. So it is an initial phase during which transmitter and receiver essentially meet each other, and then the transmitter actually transmits the packet. So the transmitter starts saying something important, right?  
好，所以，这不好，因为我们只是浪费了无线资源，对吧？两个节点尝试发送，两者都失败了，完全失败。这意味着，当有隐藏节点时，我们前面看的基本方案工作得并不是很好。所以，标准说，嗯，让我们引入一个与基本方案稍有不同的版本，可以用来让信道接入更高效。这就是带有所谓显式信道预留的方案，也叫作带握手的DCF。好吗？为什么？为什么？让我给你们看一张更容易理解的图。在DCF的这第二个版本中，我们可以在真正发送数据包之前进行一次握手。握手就是你和某个人握手，对吧。所以，它是一个初始阶段，在这个阶段，发送端和接收端基本上先见面，然后发送端才真正发送数据包。所以，发送端开始说一些重要的事情，对吧？

## 07 · 00:09:31 · RTS请求与CTS许可

原标说话人 1  00:09:31  
So here it is like if node A in the previous example first of all greets the access point, says, hi, access point, nice to meet you, and the access point says, ah, very nice to meet you, node A. And then now A starts talking to the access point. OK? Why do they do that? Because by doing that, they essentially agree on talking, right, on starting a dialogue, and they do that by exchanging these two control packets that are called Request to Send. This is what the transmitter will send. And if the intended receiver is available to receive, to be engaged in this dialogue, it will reply with another control packet called Clear to Send. Request to Send means, may I send you something, and Clear to Send means, you are clear, go ahead. OK?  
所以，这就像前面那个例子里的节点A，首先向接入点打招呼，说：‘嗨，接入点，很高兴见到你。’接入点说：‘啊，很高兴见到你，节点A。’然后，现在A开始与接入点交谈。好吗？它们为什么这样做？因为，通过这样做，它们基本上就交谈、就开始一段对话达成一致，对吧，而且它们通过交换这两个控制数据包来这样做，其中一个叫作请求发送。这是发送端将发送的包。而如果预期接收端可以接收、可以参与这段对话，它就会用另一个称为允许发送的控制数据包回复。请求发送的意思是：‘我能给你发点东西吗？’允许发送的意思是：‘你可以发了，开始吧。’好吗？

## 08 · 00:10:56 · DIFS侦听与RTS/CTS交换

原标说话人 1  00:10:56  
So the way now the dialogue happens is the following. Our transmitter, as before, first of all needs to sense the channel. Now we know that this sensing is both on the physical layer and the MAC layer. If both sensing functions say the channel is idle, and the channel is declared as idle for DIFS, then our transmitter can access the channel. But as we said, instead of transmitting the data packet right away, it will first transmit its control packet: the Request to Send packet. The control packet is a control packet, so there is no payload, right? It is only header. So remember, everyone demodulates packet headers. They do not demodulate the payload unless they are the intended receiver, but everyone demodulates the header. Everyone will demodulate the Request to Send control packet. The Request to Send, however, is of course intended for the access point. The access point, if it is available to receive, will reply with this other control packet, the CTS, Clear to Send. Notice, after SIFS. Why? Because they are packets belonging to the same dialogue. OK, perfect, so Clear to Send.  
所以，现在对话的发生方式如下。我们的发送端和之前一样，首先需要侦听信道。现在我们知道，这种侦听既在物理层，也在MAC层。如果两个侦听功能都说信道空闲，而且信道被判定为空闲的状态持续一个DIFS，那么发送端就可以接入信道。但是，正如我们说过的，它不会马上发送数据包，而会先发送自己的控制数据包：请求发送包。控制数据包就是控制数据包，所以没有有效载荷，对吧？它只有首部。所以，记住，每个人都会解调数据包首部。除非自己是预期接收端，否则不会解调有效载荷，但是每个人都会解调首部。每个人都会解调请求发送这个控制数据包。不过，请求发送当然是发给接入点的。如果接入点可以接收，它就会回复另一个控制数据包，CTS，允许发送。注意，在SIFS之后。为什么？因为它们是属于同一段对话的数据包。好，很好，那么，允许发送。

[课件图片：课件：02-WiFi_1-7.pdf · PDF第21页下半页 · 图42（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcnpCIDolzjAKZSRkFhwT6K2m)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

## 09 · 00:12:45 · SIFS间隔、数据与ACK

原标说话人 1  00:12:45  
Now A understands, OK, I can start transmitting my data. Here I didn't mark it, but there is another SIFS, OK? Between a CTS and data there is another SIFS. Why? Because all these are part of the same dialogue. All these packets are part of the same dialogue, so they are spaced by SIFS. After SIFS, node A starts transmitting the data packet. Assume that the data packet is correctly received by the access point. After SIFS, the access point will send back the ACK control packet. So as you see, we have the handshake first, and then the actual transmission.  
现在A明白了，好，我可以开始发送我的数据了。这里我没有标出来，但是还有另一个SIFS，好吗？在CTS和数据之间，还有另一个SIFS。为什么？因为所有这些都属于同一段对话。所有这些数据包都属于同一段对话，所以它们间隔SIFS。SIFS之后，节点A开始发送数据包。假设接入点正确接收了数据包。在SIFS之后，接入点会发回ACK控制数据包。所以，正如你们看到的，我们先有握手，然后才是真正的传输。

## 10 · 00:13:42 · 隐藏节点通过CTS获知通信

原标说话人 1  00:13:42  
Now, what do the other nodes do? For example, in our example, B. Well, when the RTS is transmitted by A, remember what we said: everyone can demodulate it if they hear it. In our example, however, B, if you remember, cannot hear A, right? So far our other node B will do actually nothing in our example, because it cannot hear A. So consider that this part, referring to our previous example, is not there, because B cannot hear A. However, when the access point transmits the CTS back to A, B can hear the access point, right? So it will be able to demodulate the CTS. And these are control packets, only headers, but remember, in the header there is the Duration field.  
现在，其他节点会做什么？比如，在我们的例子里，B。嗯，当A发送RTS时，记住我们说过的：每个人只要听得到，就都能解调它。不过，在我们的例子中，如果你还记得，B听不到A，对吧？所以，到目前为止，我们另一个节点B在这个例子中实际上什么也不会做，因为它听不到A。所以，考虑到我们之前的例子，这一部分不存在，因为B听不到A。但是，当接入点把CTS发回给A时，B能听到接入点，对吧？因此它能够解调CTS。而这些是控制数据包，只有首部，但是，记住，首部里有Duration字段。

## 11 · 00:15:20 · CTS设置NAV与虚拟侦听

原标说话人 1  00:15:20  
So when B hears the CTS, it demodulates the CTS, reads the Duration field, and sets its NAV to the expected remaining, at this point, expected duration of the dialogue. So the NAV of B will be set to a value that covers all this time interval. OK? What does it mean? It means that even if B gets a packet from its higher layers, now assume that it gets this packet from its higher layers at this point in time, OK, now if B senses the channel at the physical layer, the channel is idle. Why? Because B cannot hear A, so the channel is idle for B. But at the MAC layer, B has set the NAV in correspondence with the CTS. So at the MAC layer, B would say the channel for my MAC layer is busy. B must say the channel is busy. Therefore, even if it receives a packet from its higher layers at this point in time, and even if its physical layer says the channel is idle, it will have to consider the channel as busy. So it cannot access till when? Till the NAV expires, and the channel becomes actually idle, both at the physical and at the MAC layer.  
所以，当B听到CTS时，它解调CTS，读取Duration字段，并把自己的NAV设置为这段对话在此时预计剩余的、预计的持续时间。因此，B的NAV会被设为一个覆盖整个这段时间区间的值。好吗？这意味着什么？它意味着，即使B从高层得到一个数据包，现在假设它在这个时刻从高层得到了这个包，好，现在，如果B在物理层侦听信道，信道是空闲的。为什么？因为B听不到A，所以对B来说信道空闲。但是在MAC层，B已经对应着CTS设置了NAV。因此，在MAC层，B会说，对于我的MAC层来说，信道是忙的。B必须说信道是忙的。因此，即使它在这个时刻从高层收到一个数据包，即使它的物理层说信道是空闲的，它也必须认为信道是忙的。所以，它不能接入，要到什么时候呢？直到NAV到期，信道在物理层和MAC层都真正变为空闲。

## 12 · 00:17:51 · RTS/CTS预留无线资源

原标说话人 1  00:17:51  
OK, so this means that using RTS and CTS, we may avoid collisions. This is one of the mechanisms that we can apply in order to avoid collisions. As we will see also later, what the use of RTS and CTS does is, as I was saying, to reserve radio resources. Why? Because through RTS and CTS, the transmitter and the receiver will announce to their neighbors, respective neighbors, that they are going to be engaged in a dialogue. So everybody will know that. It is like saying, OK, now everyone, shut up, because I need to talk with this person.  
好，所以，这意味着，通过使用RTS和CTS，我们可能避免碰撞。这是我们可以用来避免碰撞的机制之一。正如我们后面也会看到的，RTS和CTS的使用所起的作用，就是我刚才说的，预留无线资源。为什么？因为通过RTS和CTS，发送端和接收端会向它们的邻居、各自的邻居宣布，它们将要参与一段对话。所以，每个人都会知道这一点。这就像在说，好，现在所有人都闭嘴，因为我需要和这个人谈话。

## 13 · 00:19:08 · 双方邻居如何保持静默

原标说话人 1  00:19:08  
OK, and everyone who can hear—the transmitter will say that by sending the RTS; the receiver will say that by sending the CTS. So whoever can hear the transmitter, upon receiving an RTS, if it is not the intended destination, this RTS actually says that A wants to talk to someone. And the CTS says, I am available to talk to someone. Whoever is around A will demodulate the RTS and be informed that A wants to talk. So it needs to shut up. Whoever can hear the CTS sent by the intended destination will know that that node wants to receive, right? It wants to talk with someone else, so it needs to shut up. All the neighbors of the transmitter, of the source, and all the neighbors of the intended destination will be informed that the dialogue is going to start, and they need to be silent. So that's why.  
好，而所有能听到的人——发送端会通过发送RTS来这样说，接收端会通过发送CTS来这样说。所以，任何能听到发送端的节点，在收到RTS时，如果它不是预期目的节点，这个RTS实际上就在说A想和某个人交谈。而CTS在说，我可以和某个人交谈。A周围的任何节点都会解调RTS，并得知A想要讲话。所以，它需要闭嘴。任何能够听到预期目的节点发送的CTS的节点，都会知道那个节点想要接收，对吧？它想和另一个节点交谈，所以这个旁听节点需要闭嘴。发送端、源节点的所有邻居，以及预期目的节点的所有邻居，都会被告知对话即将开始，它们需要保持安静。所以，原因就是这样。

# 同频接入点中的显式信道预留

## 14 · 00:20:58 · 同频接入点与信道预留示例

原标说话人 1  00:20:58  
RTS and CTS, as I was saying, is called DCF with handshake, but it is also referred to as explicit channel reservation, because it's like if the transmitter, the source, and the intended destination were reserving the channel for their dialogue by exchanging these control packets, RTS and CTS. OK? So the typical scenario that allows us to fully understand this explicit channel reservation is this one, where, as you can see, we have two access points. Let's assume that the two access points are operating on the same frequency channel. This may indeed happen. A is a user connected with access point one, and B is a user connected with access point two.  
正如我说过的，RTS和CTS被称为带握手的DCF，但它也被称为显式信道预留，因为这就像发送端、源节点，以及预期目的节点，通过交换这些控制数据包RTS和CTS，为自己的对话预留信道。好吗？所以，能够让我们充分理解这种显式信道预留的典型场景，就是这个，正如你们看到的，这里有两个接入点。假设这两个接入点工作在同一个频率信道上。这确实可能发生。A是连接到接入点一的用户，而B是连接到接入点二的用户。

## 15 · 00:22:05 · 识别示例中的无线覆盖范围

原标说话人 1  00:22:05  
Now, as reported here again, the radio ranges highlight, in particular, the radio range of access point one and the radio range of B. So we can see that A can hear access point one, access point one can hear both A and B, and B is connected with access point two.  
现在，正如这里再次显示的，无线电覆盖范围特别突出了接入点一的无线电覆盖范围，以及B的无线电覆盖范围。所以，我们可以看到，A能够听到接入点一，接入点一能够听到A和B，而B连接到接入点二。

## 16 · 00:22:37 · 更正拓扑：A和B均连接AP1

原标说话人 1  00:22:37  
OK, now what we have is that, essentially, we are using the scheme with RTS and CTS. Sorry, just because I changed it earlier, so I just need to check if I changed it correctly. OK, so sorry now, the scenario that I consider here is the following, where we have an access point one, and both A and B are connected with access point one, and access point two is a nearby access point.  
好，现在，我们这里基本上使用的是RTS和CTS方案。抱歉，只是因为我先前改了它，所以我只需要检查一下自己有没有改对。好，所以，抱歉，现在，我在这里考虑的场景如下：我们有一个接入点一，而且A和B都连接到接入点一，而接入点二是附近的一个接入点。

## 17 · 00:23:36 · 两个接入点使用同一信道

原标说话人 1  00:23:36  
As I said before, access point one and access point two, they both use the same frequencies, right, the same frequency channel. So if they both transmit, they transmit exactly on the same frequency band.  
正如我之前说的，接入点一和接入点二，它们都使用相同的频率，对，相同的频率信道。所以，如果它们都发送，它们就在完全相同的频带上发送。

## 18 · 00:23:56 · AP1向B发送的场景设定

[课件图片：课件：02-WiFi_1-7.pdf · PDF第22页上半页 · 图43（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcn2LoDNUYJsvRXXC86JIBnZb)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

原课件图保留旧标号；按课堂00:22:37及00:52:16的更正，从左到右对应A、接入点1、B、接入点2。A和B均关联接入点1；接入点2是附近的同频接入点。原图未包含01:06:17之后临时加入的节点C。

原标说话人 1  00:23:56  
OK, now in this example, access point one wants to transmit a packet to the user node B. So the two nodes who want to start the dialogue are these central nodes, access point one and B. Let's assume that they use the DCF with handshake.  
好，现在，在这个例子中，接入点一想要向用户节点B发送一个数据包。所以，想要开始对话的两个节点，就是中间这两个节点，接入点一和B。假设它们使用带握手的DCF。

## 19 · 00:24:30 · AP1发送RTS并通知邻居

原标说话人 1  00:24:30  
So initially assume that the channel is idle for everyone. Access point one will sense the channel for DIFS. The channel is idle both at the physical and MAC layer, so the channel is idle. Access point one can access the channel. But we're using the scheme with handshake, right? So what access point one starts with is by sending the RTS. The RTS is intended for B. Now what is the consequence of the fact that access point one sends the RTS? The consequence is that B first of all understands that access point one wants to send a packet to it. If B is available, so it's doing nothing, it will reply with a CTS, right? Essentially, the first consequence is that access point one, by sending the RTS, is like asking for permission to transmit to B. But the other important effect that we want to highlight with this example is that, by sending the RTS, access point one notifies A that it will be engaged in a dialogue with B.  
所以，一开始假设信道对所有节点都是空闲的。接入点一会侦听信道一个DIFS。信道在物理层和MAC层都空闲，所以信道空闲。接入点一可以接入信道。但是，我们使用的是带握手的方案，对吧？所以，接入点一首先做的，就是发送RTS。RTS是发给B的。现在，接入点一发送RTS这个事实，会有什么结果？结果是，B首先明白，接入点一想向它发送一个数据包。如果B可以接收，也就是说它没在做什么，它就会回复一个CTS，对吧？基本上，第一个结果就是，接入点一通过发送RTS，就像是在请求向B发送的许可。但是，我们想通过这个例子强调的另一个重要作用是，通过发送RTS，接入点一通知A，自己将会与B进行一段对话。

## 20 · 00:26:21 · A根据RTS设置NAV

原标说话人 1  00:26:21  
So A, who is a neighbor of access point one, right, A is connected with access point one, will be informed that there will be a dialogue going on, happening, and therefore it must be silent. How do we make sure that A is silent? Because, as we said, the RTS is a control packet, it has got the Duration field. So when A, that can hear access point one's RTS, demodulates the RTS, it will set its NAV to the Duration field reported in this RTS. So all the nodes that are neighbors of access point one will demodulate the RTS and understand that they cannot speak. Because access point one wants to speak to someone, and they cannot interfere, they cannot disrupt the dialogue. So we do that by imposing that they set their NAV to the Duration field included in the RTS.  
所以，A是接入点一的邻居，对，A连接着接入点一，它会被告知将会有一段对话正在进行、正在发生，因此它必须保持安静。我们怎样确保A保持安静呢？因为，正如我们说过的，RTS是一个控制数据包，它有Duration字段。所以，当能够听到接入点一的RTS的A解调这个RTS时，它会把自己的NAV设置为这个RTS中给出的Duration字段的值。因此，接入点一的所有邻居节点都会解调RTS，并知道它们不能讲话。因为接入点一想和某个人讲话，而它们不能干扰，不能打断这段对话。所以，我们通过强制它们按照RTS中包含的Duration字段来设置NAV，实现这一点。

## 21 · 00:27:50 · B发送CTS并通知邻居

原标说话人 1  00:27:50  
Now, if B is available for reception, then it will send back the CTS, right? Again, the CTS is a way to inform all the neighbors of B that it is going to be engaged in a dialogue. Of course, the CTS is also used to tell access point one, I'm available, I'm free, please go ahead, start your data packet transmission. But it is also a way to say to all the other nodes, look, I'm going to be engaged in a dialogue, so shut up, don't say anything, because otherwise you are going to disturb my reception.  
现在，如果B可以接收，那么它就会发回CTS，对吧？同样，CTS是一种通知B的所有邻居，它即将参与一段对话的方式。当然，CTS也用来告诉接入点一，我可以接收，我有空，请继续，开始发送你的数据包。但是，它也是一种对其他所有节点说话的方式：听着，我将要参与一段对话，所以闭嘴，不要说任何话，因为否则你们就会干扰我的接收。

## 22 · 00:28:44 · CTS的Duration字段与NAV

原标说话人 1  00:28:44  
So how do we do that? Because the protocol says all the nodes that can hear the CTS, it's a control packet, demodulate the header, and they are going to read the Duration field in the CTS, and set their NAV based on the value that they read. So everyone who receives the CTS will set its NAV to the Duration field included in the CTS. This means that at the MAC layer, they will consider the channel as busy for all that time.  
所以，我们怎样做到这一点呢？因为协议规定，所有能听到CTS的节点，它是一个控制数据包，都解调首部，然后读取CTS中的Duration字段，并根据读到的值设置NAV。所以，每个接收到CTS的节点，都会把自己的NAV设置为CTS中包含的Duration字段的值。这意味着，在MAC层，它们会在所有那段时间内都认为信道是忙的。

## 23 · 00:29:31 · 显式信道预留的作用

原标说话人 1  00:29:31  
So now I hope we better understand why RTS and CTS represent an explicit channel reservation, because whoever sends RTS informs all its neighbors that they need to be silent for a certain time corresponding to the expected duration of the dialogue. And whoever sends the CTS informs its neighbors that the channel is going to be busy because of its dialogue. So they reserve radio resources for their own dialogue by sending RTS and CTS.  
所以，现在我希望我们能够更好地理解，为什么RTS和CTS代表显式信道预留，因为发送RTS的节点会通知它的所有邻居，它们需要保持安静一段时间，这段时间对应于对话的预计持续时间。而发送CTS的节点会通知它的邻居，信道将因为它的对话而变忙。所以，它们通过发送RTS和CTS，为自己的对话预留无线资源。

# 握手开销、失败风险与RTS阈值

## 24 · 00:30:25 · 控制帧基本速率与时间开销

原标说话人 1  00:30:25  
OK, so you may think, well, RTS and CTS is great, solves all our problems, right? Well, there are some drawbacks here. What are the drawbacks? First of all, RTS and CTS are control packets. They do not carry any application-level information, right? So they do not carry any useful information from the application-layer point of view. They are just control packets. They are short, but control packets, except for acknowledgments, in Wi-Fi are always transmitted at the basic rate. What does it mean? That they are transmitted slowly, at a low speed. The reason is that everyone should be able to demodulate the control packets correctly. So in order to make sure that everyone understands the control packet, everyone in the network understands the control packet, we transmit at the lowest possible data rate, so very robust modulation. We make sure that our signal is received correctly by everyone that is in the area. What is the consequence? It takes time. It takes time to transmit the RTS, it takes time to transmit the CTS, so what we are doing is actually to occupy the channel with something that is not useful from the application point of view. So in a way it's a waste of radio resources. Remember, radio resources are precious, right? We would like to use them to transmit as much application data as possible. By doing that, we're just using the channel to transmit this control information.  
好，所以，你们可能会想，嗯，RTS和CTS很棒，解决了我们所有的问题，对吧？嗯，这里有一些缺点。缺点是什么？首先，RTS和CTS是控制数据包。它们不携带任何应用层信息，对吧？所以，从应用层角度看，它们不携带任何有用的信息。它们只是控制数据包。它们很短，但是，在Wi-Fi中，除了确认包之外，控制数据包总是以基本速率发送。这是什么意思？意味着它们发送得很慢，以低速发送。原因是，每个人都应该能够正确解调控制数据包。所以，为了确保每个人都理解控制数据包，网络中的每个人都理解控制数据包，我们以尽可能低的数据速率发送，因此使用非常稳健的调制。我们确保自己的信号能被区域内的每个人正确接收。后果是什么？它需要时间。发送RTS需要时间，发送CTS需要时间，所以，我们实际做的，就是用一些从应用角度看没有用的东西占据信道。所以，在某种程度上，这是对无线资源的浪费。记住，无线资源是宝贵的，对吧？我们希望利用它们发送尽可能多的应用数据。这样做时，我们只是在使用信道发送这些控制信息。

## 25 · 00:32:48 · 协议开销降低效率

原标说话人 1  00:32:48  
So the overhead associated with the Wi-Fi protocol increases, and that's bad. Overhead is bad. Overhead is something that you don't want. It reduces your efficiency. So that's the first problem.  
所以，Wi-Fi协议所带来的开销增加了，而这不好。开销不好。开销是你不想要的东西。它会降低你的效率。所以，这是第一个问题。

## 26 · 00:33:09 · 邻居漏收RTS的干扰风险

原标说话人 1  00:33:09  
The other one, the second problem, is that unfortunately things do not go so well always in practice. Why? Because, for example, an RTS that is transmitted by a transmitter may not be received correctly by other nodes because of channel errors. This still may happen even if I transmit the RTS at the basic rate, slowly, and so on. It might happen that there is a channel error. In that case, the neighbors of the transmitter will not receive the RTS correctly, so they will not understand that the channel is reserved for a dialogue. They might actually access the channel if they sense it idle, and disrupt the dialogue, first of all.  
另一个问题，第二个问题是，不幸的是，实践中事情并不总是那么顺利。为什么？因为，比如说，一个发送端发出的RTS，可能由于信道错误而无法被其他节点正确接收。即使我以基本速率慢慢地发送RTS，等等，这仍然可能发生。可能出现一个信道错误。在这种情况下，发送端的邻居就不会正确收到RTS，所以它们就不知道信道已经为一段对话预留了。如果它们侦听到信道空闲，实际上可能会接入信道，并破坏这段对话，这是第一点。

## 27 · 00:34:23 · 目的节点漏收RTS与无效等待

原标说话人 1  00:34:23  
The RTS transmission may also fail because, again, channel errors at the intended destination. So A may transmit the RTS, all other neighbors of A may receive it correctly, so they block their NAV, that's fine. But unfortunately the intended destination does not receive the RTS correctly. In that case, clearly, the intended destination will not send back any CTS. So there is no dialogue. What is the consequence? All the neighbors of A are blocked. They must be silent, because upon receiving the RTS they set the NAV; they know that they must be silent for a certain time. But there is no dialogue, no dialogue going on. That's bad as well, because we block some nodes when there is no need to do that, and this may lead again to a waste of resources. Someone could have transmitted, and instead they are blocked, they cannot. Same thing with CTS, right? Again, the CTS may not be received correctly by the neighbors of the receiver. In that case, they do not get blocked and may interfere with the dialogue.  
RTS传输也可能失败，因为，同样，在预期目的节点处出现信道错误。所以，A可能发送RTS，A的所有其他邻居都可能正确收到它，因此它们设置NAV，把自己阻止住，这没有问题。但是，不幸的是，预期目的节点没有正确收到RTS。在这种情况下，显然，预期目的节点不会发回任何CTS。所以，没有对话。后果是什么？A的所有邻居都被阻止了。它们必须保持安静，因为它们一收到RTS就设置了NAV；它们知道，自己必须保持安静一段时间。但是，没有对话，没有对话正在进行。这也不好，因为我们在没有必要这样做时，阻止了一些节点，而这同样可能导致资源浪费。有些节点本来可以发送，但是它们却被阻止了，不能发送。CTS也是同样的事情，对吧？同样，接收端的邻居可能没有正确收到CTS。在这种情况下，它们不会被阻止，可能干扰这段对话。

[课件图片：课件：02-WiFi_1-7.pdf · PDF第22页下半页 · 图44（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcnhfEUG2di0RQCr3bnR3ExHc)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

## 28 · 00:36:26 · CTS漏收、信道变化与握手局限

原标说话人 1  00:36:26  
Or the CTS may not be demodulated correctly by the source. In this case, the neighbors of the intended destination will be blocked if they receive the CTS correctly, but there is not going to be any data. Unfortunately, the wireless channel quality, due to diffraction, reflection, and therefore multipath fading, may be varying. These are stochastic phenomena; it is a stochastic process. You really don't know how good or bad your channel is going to be. There is still the possibility of channel errors. Even if you use robust modulations, there is still the risk of channel errors. So these RTS and CTS may work or may not. Summing up these drawbacks, the overhead induced by RTS and CTS and the fact that they may not work because of channel errors, let's say that in practice this handshake is not so often used.  
或者，源节点可能没有正确解调CTS。在这种情况下，如果预期目的节点的邻居正确收到CTS，它们就会被阻止，但是接下来不会有任何数据。不幸的是，无线信道质量由于衍射、反射，以及由此产生的多径衰落，可能不断变化。这些是随机现象；它是一个随机过程。你真的不知道自己的信道将会有多好或者多差。信道错误的可能性仍然存在。即使你使用稳健的调制，信道错误的风险仍然存在。所以，这些RTS和CTS可能起作用，也可能不起作用。把这些缺点加在一起，即RTS和CTS带来的开销，以及它们可能因信道错误而不起作用这一事实，可以说，在实践中，这种握手并没有那么经常被使用。

## 29 · 00:38:12 · 按数据包大小选择RTS阈值

原标说话人 1  00:38:12  
The idea is good in theory; it could work well, but then the drawbacks are too much, too many drawbacks compared to the advantages. One important thing to say, however, is that this handshake is part of the standard and it is implemented in our Wi-Fi cards. The possibility to use RTS and CTS is there. So what is the criterion under which they are used or not? When you have a network with an access point, you configure your network using a parameter called the RTS threshold. Whenever the size of your data packet is larger than the RTS threshold, you apply RTS/CTS. If the size of your packet is below the RTS threshold, so it is shorter, you do not apply RTS/CTS. It is not that a BSS always works with the basic version or always with the version with the handshake. In a BSS, depending on which packet has to be transmitted, the transmitter will apply the basic version or the version with the handshake, depending on the size of the packet that it has to transmit. The rationale is: if the packet is large, you try to protect its transmission by using RTS and CTS, with this explicit channel reservation. If the packet is short, you don't do that, because the overhead and the risk that it doesn't work are not worth it. It is best to send the packet applying the basic version of the protocol. That's the rationale. You can tune how often RTS/CTS are used by varying the RTS threshold. If you set it to a very high value, essentially all your packet sizes will be below it and you never use RTS/CTS. If you set it to a lower value, whenever you have a larger packet, a larger payload, you are going to use RTS and CTS. How often you actually apply them depends on how you set this configuration parameter called the RTS threshold.  
理论上这个想法很好；它可能工作得很好，但是缺点实在太多，与优点相比，缺点太多。不过，有一件重要的事需要说明：这个握手是标准的一部分，而且已经实现在我们的Wi-Fi网卡里。使用RTS和CTS的可能性是存在的。那么，决定使用还是不使用它们的判据是什么？当你有一个带接入点的网络时，你用一个叫作RTS阈值的参数来配置你的网络。每当数据包大小大于RTS阈值，你就应用RTS/CTS。如果数据包大小低于RTS阈值，也就是比较短，你就不应用RTS/CTS。并不是一个BSS总是使用基本版本工作，或者总是使用带握手的版本工作。在一个BSS中，根据需要发送的是哪个数据包，发送端会按照它必须发送的数据包大小，采用基本版本或者带握手的版本。其理由是：如果数据包很大，你就通过使用RTS和CTS、通过这种显式信道预留，尝试保护它的传输。如果数据包很短，你就不这样做，因为开销和它不起作用的风险不值得。最好采用协议的基本版本发送这个包。这就是理由。你可以通过改变RTS阈值，调节RTS/CTS的使用频率。如果你把它设为一个非常高的值，那么基本上你所有的数据包大小都会低于它，你就从不使用RTS/CTS。如果你把它设为一个较低的值，那么每当你有一个更大的数据包、更大的有效载荷时，你就会使用RTS和CTS。你实际多频繁地使用它们，取决于你怎样设置这个叫作RTS阈值的配置参数。

## 30 · 00:41:45 · 课堂阈值示例与恶劣环境

原标说话人 1  00:41:45  
Now, typical values of the RTS threshold are 400 bytes or slightly higher than that. Why? Because most Wi-Fi payloads are 400 bytes or below, so most of them will be transmitted according to the basic scheme. Only the very large ones will be transmitted using RTS and CTS. However, there are some specific scenarios, like in mines or other very harsh environments, where there are many hidden nodes. In those cases, you tend to lower the RTS threshold because you have many hidden nodes. It is better to use RTS and CTS more often, so you set the RTS threshold to a lower value, so that most of the packets will be transmitted using RTS and CTS. But this is something that you can adjust depending on the scenario that you are dealing with. Okay, good. We are almost at the break. Here are the considerations that I made, so you have them reported also in the slides. What we are going to see after the short break is the situation where we are back to the basic version of the protocol. We will further explain what happens when a packet fails.  
现在，RTS阈值的典型数值是400字节，或者略高一点。为什么？因为大多数Wi-Fi有效载荷为400字节或者更小，所以其中大多数会按照基本方案发送。只有非常大的那些，才会使用RTS和CTS发送。不过，有一些特定场景，比如矿井或者其他非常恶劣的环境，其中有许多隐藏节点。在这些情况下，你往往会降低RTS阈值，因为你有许多隐藏节点。更经常地使用RTS和CTS会更好，因此，你把RTS阈值设置为一个较低的值，这样大多数数据包都会使用RTS和CTS来发送。但是，这是你可以根据自己面对的场景来调整的事情。好，很好。我们快到休息时间了。这里是我刚才提出的考虑，所以你们在幻灯片里也能看到它们。短暂休息之后，我们要看的是回到协议基本版本的情况。我们会进一步解释数据包失败时发生什么。

# 重传预告、提问与课间讨论

## 31 · 00:43:53 · 停止等待与失败重传预告

原标说话人 1  00:43:53  
We know already that we are applying stop-and-wait, so we expect that when a packet fails, the transmitter will have to retransmit. We know that already, but we are going to specify a little bit better how that happens.  
我们已经知道，我们采用的是停止等待，所以我们预期，当数据包失败时，发送端必须重传。我们已经知道这一点，但是，我们要更具体一点地说明它是怎样发生的。

## 32 · 00:44:14 · 课间后回到基本DCF

原标说话人 1  00:44:14  
Just consider that after the short break we will go back to the basic version of DCF. Forget about RTS/CTS for now, and set your mind back to the scenario that we considered earlier.  
只要考虑到，短暂休息之后，我们会回到DCF的基本版本。暂时忘掉RTS/CTS，把思路重新放回我们之前考虑的那个场景。

## 33 · 00:44:45 · 无ACK场景与五分钟休息

原标说话人 1  00:44:45  
This one. Set your mind to this. What we are going to look at is the case where there is no ACK because the packet failed. That's what we are going to see after the short break. So we will start again in five minutes.  
这个。把思路放到这里。我们将要看的是，由于数据包失败而没有ACK的情况。这就是我们短暂休息后要看的。所以，我们五分钟后再次开始。

## 34 · 00:45:46 · 提问：隐藏节点能否同时发RTS

原标说话人 1  00:45:46  
Question: Since A and B cannot hear each other, could they send RTS at the same time? No, no, that's not the... I mean, they might, they may, but this is not the case that we made.  
问题：既然A和B不能听到彼此，它们能不能同时发送RTS？不，不，那不是……我的意思是，它们可能，它们可以，但这不是我们刚才给出的那个情况。

## 35 · 00:45:56 · 追问：其他节点如何听到回答

原标说话人 2、1（合并段）  00:45:56  
So... But how, how can others... ...hear the answer from A?  
所以……但是，其他节点怎样、怎样才能……听到A的回答？

## 36 · 00:46:02 · 约定课间后重讲

原标说话人 1  00:46:02  
Okay, so let me go back to this after the break, because if it's not clear, we need to repeat it.  
好，那么，休息之后让我再回到这一点，因为如果不清楚，我们就需要重复讲一遍。

## 37 · 00:48:46 · 课间讨论：图像处理项目选题

原标说话人 2  00:48:46  
So the image-processing topic will not be combined with the other projects. It feels difficult to connect them. A computer-vision topic might fit, but image processing seems harder to combine. In a large project, image processing might only be a very small part, so it would be difficult to develop it into the project itself.  
所以，图像处理这个题目不会和其他项目结合。感觉很难把它们联系起来。计算机视觉的题目可能合适，但图像处理似乎更难结合。在一个大项目里，图像处理可能只占很小的一部分，因此，很难把它本身发展成一个项目。

## 38 · 00:49:20 · 课间讨论：聚焦项目题目

原标说话人 2  00:49:20  
I feel that, based on the requirements, we should choose a more focused topic.  
我觉得，根据要求，我们应该选择一个更有针对性的题目。

# 拓扑重讲与各节点NAV时序

## 39 · 00:51:59 · 恢复课堂讲解

原标说话人 1  00:51:59  
Let me tell you.  
让我告诉你。

## 40 · 00:52:16 · 重讲AP1向B发送的拓扑

原标说话人 1  00:52:16  
Okay, so let me go back to the previous case, because maybe we need to clarify things. So, let me again consider this example in terms of network topology. This is the network topology that we are considering. Again, I changed the labels with respect to the slide that you had, so you need to update the labels. A and B are connected with access point one. But with respect to the initial scenario with the hidden terminals, I added this node here. Access point two. Now, the example that I made in this case is the following. These two nodes want to communicate with each other. In particular, access point one wants to send a packet to B. At this point we know what the RTS threshold is, so let's assume that the packet size is greater than the RTS threshold. We are going to use RTS and CTS, the version with the handshake, in order to transmit this packet. Assume that initially the channel is idle for everyone.  
好，那么，让我回到前面那个情况，因为也许我们需要把事情说清楚。所以，让我再次从网络拓扑的角度考虑这个例子。这就是我们正在考虑的网络拓扑。同样，相对于你们拿到的幻灯片，我改变了标号，所以你们需要更新标号。A和B连接着接入点一。但是，相对于最初带隐藏终端的场景，我在这里加了这个节点。接入点二。现在，我在这种情况下举的例子如下。这两个节点想要彼此通信。特别是，接入点一想要向B发送一个数据包。在这一点上，我们已经知道RTS阈值是什么，所以，假设数据包大小大于RTS阈值。我们将使用RTS和CTS，也就是带握手的版本，来发送这个数据包。假设一开始信道对每个节点都是空闲的。

## 41 · 00:54:04 · 绘制各节点的时间轴

原标说话人 1  00:54:04  
Now let me draw the behavior of the nodes over time. This is the timeline; the line represents the time evolution. We have access point one, we have B, and we have another BSS, access point two. This is another BSS nearby.  
现在，让我画出节点随时间的行为。这是时间轴；这条线代表时间的演进。我们有接入点一，有B，还有另一个BSS，接入点二。这是附近的另一个BSS。

## 42 · 00:54:41 · 区分无线可听范围与关联关系

原标说话人 1  00:54:41  
As we said, A and B are both connected with access point one, but A and B are hidden with respect to each other. They cannot hear each other. B, on the other hand, is exposed to both access point one and access point two. It is connected with access point one, but B and access point two can hear each other. As we said, hearing is different from having a communication link in place. If B wants to transmit something, it will be transmitted to access point one.  
正如我们说过的，A和B都连接着接入点一，但是A和B相对于彼此是隐藏的。它们听不到彼此。另一方面，B同时暴露在接入点一和接入点二的信号范围内。它连接着接入点一，但是B和接入点二可以听到彼此。正如我们说过的，能够听到，与已经建立通信链路，是不同的。如果B想发送某些东西，它会被发送到接入点一。

## 43 · 00:55:35 · AP1等待DIFS后接入

原标说话人 1  00:55:35  
But it can hear what access point two says, as when we pass by someone who is talking to someone else. Now, that said, access point one, in order to transmit its packet to B, will first sense the channel for a time equal to DIFS, because this is a regular data packet. We said the channel initially is idle for everyone, so access point one will start the process to transmit its packet.  
但是，它可以听到接入点二说什么，就像我们从一个正在和别人讲话的人身边经过。现在，说完这些，接入点一为了向B发送它的数据包，会先侦听信道，持续一段等于DIFS的时间，因为这是一个普通数据包。我们说过，信道一开始对所有节点都空闲，所以接入点一会开始发送数据包的过程。

## 44 · 00:56:26 · 大数据包触发RTS与A的NAV

原标说话人 1  00:56:26  
But the packet, the data packet payload, is larger than the RTS threshold. What access point one transmits upon accessing the channel is not the data packet at the beginning. It is first transmitting an RTS. RTS is a control packet; of course, it is intended for B because we have, as the destination address in the header, B. Clearly, the RTS is a request to send intended for B. But since it is a control packet, everyone who hears this control packet will demodulate it, because it's just a header and everyone, as we said, is demodulating packet headers. What does this mean? Who is going to demodulate this RTS? Clearly B, but also A in our scenario. What B will do is: oh, I got an RTS for me; I'm available to receive. B is going to reply after SIFS because this is the same dialogue, with a packet that is clear to send. What about A? We said this RTS is received also by A. A will read this RTS. Of course, it understands that the RTS is not for itself, but it will read the Duration field. The Duration field reports a value that covers all the expected duration of the dialogue. So it must set its NAV to this duration. Now A, which is a neighbor of the transmitter, has set its NAV according to the Duration field included in the RTS. Since its NAV is set to a value greater than zero for all this time, during all this time A must be silent.  
但是，数据包、数据包的有效载荷，大于RTS阈值。接入点一接入信道后，一开始发送的不是数据包。它首先发送一个RTS。RTS是控制数据包；当然，它是发给B的，因为首部中的目的地址是B。显然，RTS是发给B的请求发送。但是，由于它是控制数据包，任何听到这个控制数据包的节点都会解调它，因为它只是一个首部，而且，正如我们说过的，每个人都在解调数据包首部。这意味着什么？谁会解调这个RTS？显然有B，但是在我们的场景中还有A。B会做的是：哦，我收到了一个发给我的RTS；我可以接收。B会在SIFS之后回复，因为这是同一段对话，回复的是一个允许发送的数据包。A呢？我们说过，这个RTS也被A接收到了。A会读取这个RTS。当然，它知道RTS不是发给自己的，但是它会读取Duration字段。Duration字段给出的值覆盖整个对话的预计持续时间。所以，它必须把NAV设置为这个持续时间。现在，A作为发送端的邻居，已经按照RTS中包含的Duration字段设置了NAV。由于在所有这段时间里，它的NAV都被设为一个大于零的值，所以在所有这段时间里，A必须保持安静。

## 45 · 00:59:19 · B回复CTS与AP2旁听

原标说话人 1  00:59:19  
Now let's look at the CTS. The CTS is a reply, a response to this RTS, and says: I am available to receive. Clearly the R... sorry, the CTS is intended for access point one, of course. Access point one, upon receiving the CTS, says: oh, good, B is available to receive my packet, so I'm going to send a packet. The packet will be sent after SIFS because it still belongs to the same dialogue. Who else hears this CTS according to our example topology? Access point two, because access point two can hear B. It will demodulate the header of this CTS and understand that the channel is going to be busy.  
现在，我们来看CTS。CTS是一个回复，是对这个RTS的响应，它说：我可以接收。显然，这个R……抱歉，CTS当然是发给接入点一的。接入点一收到CTS后会说：哦，很好，B可以接收我的数据包，所以我要发送一个数据包。这个包会在SIFS之后发送，因为它仍然属于同一段对话。按照我们这个例子的拓扑，还有谁能听到这个CTS？接入点二，因为接入点二能够听到B。它会解调这个CTS的首部，并知道信道将会忙。

## 46 · 01:00:44 · AP2设置NAV及数据帧更新

原标说话人 1  01:00:44  
So it reads the Duration field in the CTS and sets its NAV to the remaining expected duration of the dialogue. This means that all the neighbors of the intended receiver, upon receiving the CTS, will set their NAV according to the value in the Duration field included in the CTS. Good. Now we see the effect of explicit channel reservation, because through RTS we essentially blocked all the neighbors of the transmitter. Through CTS, we block all the neighbors of the receiver. Now, as we said, access point one transmits data. This is a detail, but just for completeness: of course, this data packet has a header, and the header again is demodulated by everyone. In the header of the data packet there is also the Duration field. Upon hearing this Duration field, whoever hears it will update its NAV.  
所以，它读取CTS中的Duration字段，把自己的NAV设置为这段对话预计剩余的持续时间。这意味着，预期接收端的所有邻居在收到CTS时，都会根据CTS中包含的Duration字段的值来设置NAV。很好。现在，我们看到了显式信道预留的效果，因为，通过RTS，我们基本上阻止了发送端的所有邻居。通过CTS，我们阻止了接收端的所有邻居。现在，正如我们说过的，接入点一发送数据。这是一个细节，但只是为了完整起见：当然，这个数据包有一个首部，而且这个首部同样会被所有节点解调。在数据包首部中，也有Duration字段。一听到这个Duration字段，听到它的任何节点都会更新自己的NAV。

## 47 · 01:02:28 · 数据接收成功后回复ACK

原标说话人 1  01:02:28  
Now the practical effect is no change, because we already have the NAV set. This is no news, but to be precise, whenever I hear a Duration field, I update my NAV. Anyway, there is no practical effect here. We assume that the data packet is correctly received by B. We are optimistic: after SIFS, following the data packet, B transmits the ACK.  
现在，实际效果没有变化，因为我们已经设置了NAV。这不是新情况，但是，为了精确起见，每当我听到一个Duration字段，我就会更新自己的NAV。不管怎样，这里没有实际效果。我们假设B正确收到了数据包。我们乐观一点：在数据包之后，过一个SIFS，B发送ACK。

## 48 · 01:03:18 · 理解时序图中的其他节点

原标说话人 1  01:03:18  
In this case, in this example, everything worked fine. We were able to block the neighbors of the transmitter and block the neighbors of the receiver. The transmitter and the receiver could complete their dialogue successfully. Great. When we have this representation in the slides, let's say 'others', referring to our previous example, is B. What this slide represents is that whoever hears RTS sets its NAV based on the Duration field included in the RTS. Whoever hears the CTS updates its NAV based on the Duration field included in the CTS. It is a global representation, whoever can be there.  
在这种情况下，在这个例子中，一切都运行得很好。我们能够阻止发送端的邻居，也能够阻止接收端的邻居。发送端和接收端可以成功完成它们的对话。很好。当我们在幻灯片上采用这种表示时，比如说‘其他节点’，对应我们前面的例子，就是B。这张幻灯片表示的是，任何听到RTS的节点，都根据RTS中包含的Duration字段设置自己的NAV。任何听到CTS的节点，都根据CTS中包含的Duration字段更新自己的NAV。它是一种总体的表示，不管在那里的是谁。

## 49 · 01:04:41 · 将其他节点对应到A和AP2

原标说话人 1  01:04:41  
In this example, the example that we have here, 'others' are A and access point two. If it's clearer, we can actually modify these slides and move this a little bit higher, after this. This is the network topology, and at this point, the 'others' referring to...  
在这个例子中，在我们这里这个例子中，‘其他节点’是A和接入点二。如果这样更清楚，我们实际上可以修改这些幻灯片，把这个稍微向上移一点，放在这个后面。这是网络拓扑，而在这里，‘其他节点’所指的是……

## 50 · 01:05:34 · A与AP2分别由RTS、CTS触发

原标说话人 1  01:05:34  
Working. Okay, now this is the topology and this is the corresponding diagram. Clearly, as we said, when we say 'others' and mean A, A will be able to set its NAV in correspondence with the RTS. When we refer to access point two, it will be able to set its NAV starting from the CTS.  
起作用了。好，现在这是拓扑，这是对应的图。显然，正如我们说过的，当我们说‘其他节点’，指的是A时，A能够对应着RTS设置NAV。当我们指的是接入点二时，它能够从CTS开始设置NAV。

## 51 · 01:06:17 · 加入同时听到双方的节点C

原标说话人 1  01:06:17  
If we consider a similar topology but add a node, for example here, C, that is in radio range of both the source and the destination, then node C will hear both the RTS and the CTS. It will be able to set its NAV first when it hears the RTS, and then it will update it upon hearing the CTS.  
如果我们考虑一个类似的拓扑，但是添加一个节点，比如在这里，C，它同时位于源节点和目的节点的无线电覆盖范围内，那么节点C会听到RTS和CTS。它能够先在听到RTS时设置自己的NAV，然后在听到CTS时更新它。

## 52 · 01:07:03 · C先设置再刷新NAV

原标说话人 1  01:07:03  
If we add a node C there in the middle, it will set its NAV here in correspondence with the RTS. It will also hear the CTS, so it will update it. There is no practical effect because it has already set the NAV, but to be precise that will be what happens. If you like, we can just duplicate this slide and duplicate this slide, and then we essentially have another view.  
如果我们在那里中间加一个节点C，它就会在这里对应着RTS设置自己的NAV。它还会听到CTS，所以它会更新NAV。实际上没有效果，因为它已经设置了NAV，但是，为了精确起见，这就是将会发生的事情。如果你们愿意，我们可以复制这张幻灯片，再复制这张幻灯片，然后基本上就有了另一种视图。

## 53 · 01:08:24 · 继续调整课堂图示

原标说话人 1  01:08:24  
Like, for this.  
就像，对于这个。

## 54 · 01:08:34 · 标注C的NAV设置与刷新

原标说话人 1  01:08:34  
Okay, and C sets its NAV based on the RTS and refreshes the NAV based on the CTS. In these other cases, where we had A and access point two, we can have...  
好，C根据RTS设置NAV，并根据CTS刷新NAV。在这些其他情况中，我们有A和接入点二，我们可以有……

## 55 · 01:09:08 · 区分AP2的CTS触发时间

原标说话人 1  01:09:08  
And then we can add this one, access point two. Let me distinguish the two of them, and we let this NAV be set from CTS.  
然后，我们可以加上这一个，接入点二。让我把它们两个区分开，我们让这个NAV从CTS开始设置。

## 56 · 01:10:01 · 对比A与AP2的NAV时间轴

原标说话人 1  01:10:01  
I hope that now it's clearer by distinguishing the behavior of every neighbor. If we have this example, then this is the timeline, and we move this, where A only sets the NAV based on the RTS and the access point only hears the CTS.  
我希望，通过区分每一个邻居的行为，现在更清楚了。如果我们有这个例子，那么这就是时间轴，我们移动这个，其中A只根据RTS设置NAV，而接入点只听到CTS。

## 57 · 01:10:34 · 补充C并汇总各节点行为

原标说话人 1  01:10:34  
In this other example, where we added a node in the middle, the behavior of the other nodes is the same. Just highlighting the behavior of C: since C can hear both the RTS and the CTS, it will first set the NAV based on the RTS and then refresh it upon hearing the CTS. For extra clarity, if you wish, we can repeat these points on the next slide and have all of them represented here.  
在另一个例子中，我们在中间加了一个节点，其他节点的行为是一样的。这里只突出C的行为：由于C能够同时听到RTS和CTS，它会先根据RTS设置NAV，再在听到CTS时刷新它。为了更加清楚，如果你们愿意，我们可以在下一张幻灯片上重复这些要点，把它们全部表示在这里。

## 58 · 01:11:41 · 确认讲解与答疑

原标说话人 1  01:11:41  
In this way you have all the nodes' behavior there. Is it clear now? Okay, perfect. Are there other questions or points that are unclear?  
这样，你们就有了所有节点在那里的行为。现在清楚了吗？好，太好了。还有其他问题或者不清楚的地方吗？

# 基本DCF失败、ACK超时与重新竞争

## 59 · 01:12:08 · 回到所有节点互相可听的DCF

[课件图片：课件：02-WiFi_1-7.pdf · PDF第18页下半页 · 图36（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcnMY8v5YDoMlfXD1P8T9exFd)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

此图为课件中的成功传输基线。课堂01:13:47–01:17:08在此基础上改为失败情形：没有ACK，发送端等待T_F后重新竞争；原图未作改写。

原标说话人 1  01:12:08  
Let me know, and of course we can go back to any slide you may want to see again. If that is clear now, let me check my time. It's 10:25, right? Now let's go back to the basic DCF scheme, so forget about RTS/CTS for now. Let's consider the case where we had a simpler situation. We have an access point, we have A, let's also consider B, let's also consider C. This is the timeline. Remember that we considered the access point, A, B, C. Let's consider this simple scenario where all of them can hear each other. We are back to simple and basic.  
告诉我，当然，我们可以回到任何一张你们想再看的幻灯片。如果现在清楚了，让我看一下时间。现在是10:25，对吧？现在，我们回到基本DCF方案，所以暂时忘掉RTS/CTS。让我们考虑之前那个比较简单的情况。我们有一个接入点，有A，也考虑B，也考虑C。这是时间轴。记住，我们考虑了接入点、A、B、C。我们考虑这个所有节点都能听到彼此的简单场景。我们回到了简单、基本的情况。

## 60 · 01:13:47 · 基本DCF中的数据发送失败

原标说话人 1  01:13:47  
Now let's consider that A has waited for DIFS. The channel is idle as before. A could access the channel and transmit the data packet. The data packet is received by the access point, which, before, when we were optimistic, would send back an acknowledgment. The others, clearly, upon hearing the header of the data packet, will set their NAV, because everybody can hear everybody else. They will just set their NAV. This is more or less the situation that we considered before. Now the scenario is the simple one, but we want to be a little bit less optimistic. What we are going to say is: unfortunately this data packet transmission was not successful.  
现在，假设A已经等了一个DIFS。和之前一样，信道空闲。A能够接入信道并发送数据包。数据包由接入点接收，之前，当我们比较乐观时，它会发回一个确认。其他节点显然在听到数据包首部时，会设置自己的NAV，因为每个人都能听到其他每个人。它们就是设置自己的NAV。这大致就是我们之前考虑过的情况。现在场景是简单的那个，但是我们想稍微不那么乐观。我们要说的是：不幸的是，这次数据包传输没有成功。

## 61 · 01:15:04 · 无ACK时旁听节点仍保持NAV

原标说话人 1  01:15:04  
The result is that if the packet transmission fails, we cannot consider the acknowledgment. No ACK, according to the stop-and-wait mechanism. What we know, however, is that the other nodes, B and C, will still consider the channel busy for all this time. Physically, the channel here is idle, but at the MAC layer of B and C they still have the NAV set to a positive value. They consider that the channel is busy until this time instant. We knew that. B and C will remain there with the NAV set, but let's focus on what the source and the destination do in this case.  
结果是，如果数据包传输失败，我们就不能考虑确认了。按照停止等待机制，没有ACK。不过，我们知道的是，其他节点B和C，仍然会在所有这段时间里认为信道忙。在物理上，这里的信道是空闲的，但是在B和C的MAC层，它们仍然把NAV设置为一个正值。它们认为信道一直忙到这个时刻。我们已经知道这一点。B和C会留在那里，保持NAV的设置，但是我们来重点看看，在这种情况下源节点和目的节点会做什么。

## 62 · 01:16:17 · 发送端等待ACK超时

原标说话人 1  01:16:17  
What we know is that the access point, the intended destination, will not send back any acknowledgment. The transmitter, when it finishes transmitting, hopes to receive an acknowledgment. It is there waiting for the acknowledgment, which unfortunately will not arrive. What we can do is consider a timeout, as we said. After a while, of course, this source will get tired of waiting and understand that no acknowledgment is there.  
我们知道，接入点，也就是预期目的节点，不会发回任何确认。发送端完成发送时，希望收到一个确认。它在那里等确认，而不幸的是，这个确认不会到来。正如我们说过的，我们可以考虑一个超时。过一会儿，当然，这个源节点会厌倦等待，明白没有确认到来。

## 63 · 01:17:08 · 失败等待时间T_F与重新竞争

原标说话人 1  01:17:08  
Let's call this T_F; F stands for failure. Let's consider that this is the time during which the sender will wait for the acknowledgment. If no acknowledgment is received by this time T_F, then the source, the sender, understands that it has failed. According to stop-and-wait it has to try again. Now we try to understand what a node does in order to recontend for the channel. It needs to get the possibility to transmit again on the channel, so it has to recontend for the channel. This behavior that we are going to explain is the procedure called backoff.  
我们把它叫作T_F；F代表失败。我们认为，这是发送方等待确认的那段时间。如果到这个T_F时间还没有收到确认，那么源节点、发送方，就知道它失败了。按照停止等待，它必须再试一次。现在，我们试着理解，一个节点为了重新竞争信道会做什么。它需要获得再次在信道上发送的可能，所以必须重新竞争信道。我们将要解释的这种行为，就是叫作退避的过程。

# 随机退避、冻结与恢复

## 64 · 01:18:17 · DIFS后引入随机退避

原标说话人 1  01:18:17  
Our sender, once it understands that it has failed, in order to try again cannot just sense the channel for DIFS and, if the channel is idle, transmit. It needs to do something slightly more complicated, called the backoff procedure. The backoff procedure is actually relatively easy. The sender will first make sure that the channel is idle. This still has to be done, and we do it by making sure that the channel remains idle for a DIFS time. Now, instead of retransmitting immediately, it will draw a random instance of a random variable, a random time called the backoff time. It needs to sense the channel as idle for this backoff time before being able to access the channel and transmit. This is essentially an extra time it needs to wait for. After this time it can access the channel and transmit.  
我们的发送方一旦明白自己失败了，为了再试一次，就不能只是侦听信道一个DIFS，并在信道空闲时发送。它需要做一件稍微复杂一点的事情，叫作退避过程。退避过程其实相对简单。发送方首先要确保信道空闲。这仍然必须做，而我们通过确保信道保持空闲一个DIFS时间来做到这一点。现在，它不会立即重传，而会抽取一个随机变量的随机取值，一个叫作退避时间的随机时长。在能够接入信道并发送之前，它需要在这个退避时间内侦听到信道空闲。这基本上就是它需要等待的额外时间。在这段时间之后，它可以接入信道并发送。

## 65 · 01:20:11 · 退避三步骤与CW_min

[课件图片：课件：02-WiFi_1-7.pdf · PDF第23页下半页 · 图46（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcnDm9NYs2UHLxRKJIizGDJug)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

原标说话人 1  01:20:11  
The backoff procedure is essentially composed of three main steps. Make sure the channel is idle for DIFS; this is step one. Step two: compute this random backoff time and decrease it as long as the channel is idle. When this backoff time, during which the channel must be idle, is finished, you can access the channel and transmit. Three steps, not very difficult. What is slightly more complicated is how this backoff time has to be computed. We said it is a random time. 'Random' is a bit vague, right? What do I mean by random? The procedure is the following. There is a parameter specified by Wi-Fi called the contention window minimum. What is this contention window minimum? It is an integer number, and it defines a range of integers that starts with zero, up to this number. For simplicity, let's consider that this number is equal to 31. In this case, this range of integers goes from 0, 1, 2, 3, 4, 5, 6... up to 31.  
退避过程基本上由三个主要步骤组成。确保信道空闲一个DIFS；这是第一步。第二步：计算这个随机退避时间，并且只要信道空闲，就减少它。当这个要求信道必须空闲的退避时间结束时，你就可以接入信道并发送。三个步骤，并不很难。稍微复杂一点的是，这个退避时间必须怎样计算。我们说过，它是一个随机时间。‘随机’有点含糊，对吧？我说随机，是什么意思？过程如下。Wi-Fi规定了一个参数，叫作最小竞争窗口。这个最小竞争窗口是什么？它是一个整数，并定义了一个从零开始、一直到这个数的整数范围。为了简单起见，假设这个数等于31。在这种情况下，这个整数范围从0、1、2、3、4、5、6……一直到31。

## 66 · 01:22:23 · 均匀抽取整数计算首次退避

原标说话人 1  01:22:23  
Now, in order to compute this backoff, in this example this is the first time that we are computing the backoff time in order to eventually transmit. this data packet. It is the very first time that we apply the backoff to transmit this specific data packet. What A will do is draw an integer with equal probability out of this range. It will select 0, or 1, or 2, or 3, or 4, or 5... or 31 with equal probability. Let's assume that it draws 3. Our integer is equal to 3. The backoff time that A computes will then be three times the time slot.  
现在，为了计算这个退避，在这个例子中，这是我们第一次计算退避时间，以便最终发送这个数据包。这是我们为了发送这个特定的数据包，第一次应用退避。A会做的，就是从这个范围里以相等概率抽取一个整数。它会以相等概率选择0、或者1、或者2、或者3、或者4、或者5……或者31。假设它抽到了3。我们的整数等于3。然后，A计算出的退避时间，就会是时隙的三倍。

## 67 · 01:23:45 · 时隙与退避计数器

原标说话人 1  01:23:45  
Now we understand why we had the time slot. The time slot is useful. This is the integer that is drawn with equal probability out of this range, and based on this integer we compute the backoff time. The backoff time is an integer multiplied by the duration of a time slot. Then A sets a counter, called the backoff counter, to this value.  
现在，我们明白为什么要有时隙了。时隙是有用的。这是从这个范围里以相等概率抽取的整数，而根据这个整数，我们计算退避时间。退避时间就是一个整数乘以一个时隙的持续时间。然后，A把一个叫作退避计数器的计数器设置为这个值。

## 68 · 01:24:30 · 逐时隙递减与忙时冻结

原标说话人 1  01:24:30  
What it does, so we are now at step two, is: I computed the backoff time; now I'm going to decrease this backoff counter time slot by time slot. Every time slot I listen to the channel. If the channel has been idle, at the end of the time slot I decrease the backoff counter by that amount. Next, I'm going to sense the channel for a time slot. If the channel has been idle, I further decrease the counter, and so on. When the counter reaches zero, I access the channel and transmit. Now you may wonder: what happens if, while I'm decreasing the backoff counter, at a certain point the channel becomes busy? That might happen. In that case I have to stop decreasing the backoff counter. It cannot be decreased if I sense that during the time slot the channel is busy. I have to freeze the backoff counter until the channel becomes idle again. Let me draw it here. This is the way a node decreases the backoff counter. In our example, the backoff counter is three time slots. Let's assume that the channel is sensed idle during the first time slot, so we can decrease it by one. Let's say minus one because that time slot was idle. I can decrease the backoff counter by one time slot. But let's assume that at this point in time the channel becomes busy.  
它所做的，也就是说，我们现在到了第二步，是：我计算出了退避时间；现在我要逐个时隙地减少这个退避计数器。每个时隙我都监听信道。如果信道一直空闲，那么在时隙结束时，我就把退避计数器减少相应的量。接下来，我会侦听信道一个时隙。如果信道一直空闲，我就进一步减少计数器，如此继续。当计数器达到零时，我就接入信道并发送。现在，你们可能会想：如果当我正在减少退避计数器时，信道在某个时刻变忙了，会发生什么？这可能发生。在这种情况下，我必须停止减少退避计数器。如果我侦听到信道在这个时隙期间是忙的，就不能减少它。我必须冻结退避计数器，直到信道再次变为空闲。让我在这里画出来。这就是节点减少退避计数器的方式。在我们的例子中，退避计数器是三个时隙。假设第一个时隙期间侦听到信道空闲，那么我们就可以把它减一。我们说减一，因为那个时隙是空闲的。我可以把退避计数器减少一个时隙。但是，假设在这个时刻，信道变忙了。

## 69 · 01:27:27 · 非完整空闲时隙不递减

原标说话人 1  01:27:27  
During this time slot, initially the time slot was idle, but at a certain point the channel has become busy. Can I decrease the backoff counter at the end of this time slot? No, because the channel has become busy. I have to freeze the backoff counter; I cannot touch it. If the channel remains busy during all this time, I cannot touch the backoff counter. If the channel remains busy here, the remaining backoff is still equal to two. It was three; I decreased it by one, so here it is two, and it must remain two while the channel remains busy. I cannot touch it; it's frozen. Now assume that at a certain point the channel becomes idle again.  
在这个时隙期间，最开始这个时隙是空闲的，但是在某个时刻，信道变忙了。我能在这个时隙结束时减少退避计数器吗？不能，因为信道变忙了。我必须冻结退避计数器；我不能动它。如果信道在所有这段时间里一直忙，我就不能动退避计数器。如果这里信道一直忙，那么剩余退避仍然等于二。它原来是三；我把它减了一，所以这里它是二，而且当信道保持忙时，它必须一直是二。我不能动它；它被冻结了。现在，假设在某个时刻信道再次变为空闲。

## 70 · 01:29:11 · 再次空闲DIFS后恢复计数

原标说话人 1  01:29:11  
What I have to do is, first of all, make sure that the channel remains idle for DIFS. I really have to be sure that now the channel is idle again, so I need to sense it as idle for DIFS. If it remains idle for DIFS, then I can start decreasing the backoff counter again. In the next time slot, if the channel is idle, I can decrease the backoff counter by one.  
我必须做的，首先是确保信道保持空闲一个DIFS。我真的必须确定，现在信道再次空闲了，所以我需要侦听到它空闲一个DIFS。如果它保持空闲一个DIFS，那么我就能够再次开始减少退避计数器。在下一个时隙中，如果信道空闲，我就能把退避计数器减一。

## 71 · 01:29:53 · 计数器归零后发送

原标说话人 1  01:29:53  
Now I have only one time slot left. If the channel remains idle, I wait one time slot more. At that point the counter reaches zero; I can access the channel and transmit the packet.  
现在，我只剩一个时隙。如果信道保持空闲，我就再等一个时隙。在那个时候，计数器达到零；我就能够接入信道并发送数据包。

# 重复重传与竞争窗口增长

## 72 · 01:30:12 · 再次失败与重复退避

[课件图片：课件：02-WiFi_1-7.pdf · PDF第24页上半页 · 图47（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcnO9Fw95FzIaSMI5eMm9h1gh)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

此页展示课件的完整CW更新公式；课堂本段先说明重复退避与窗口大致翻倍，并表示下次再解释精确计算。正文仍保留课堂原话。

原标说话人 1  01:30:12  
This is how backoff works. Is it clear? We have five more minutes. Let me say one more thing. Next time we will make more examples and understand a little bit better why backoff is there, why they introduced backoff. But for today, let me just say that in this case we decreased the backoff counter to zero, so we said: now we can access the channel and transmit again. Assume that we fail again. This may happen, unfortunately, so let's be even more pessimistic. We fail again; we have to try another time. According to stop-and-wait, if we have not reached the maximum number of possible attempts, we need to try again. What do we do? We repeat the same procedure because we still have to recontend for the channel. It is exactly the same situation. We need to again make sure that the channel is idle for DIFS, then draw a random integer, multiply this random integer by the time slot, set our backoff counter to this new value, and start decreasing the backoff counter again as long as the channel is idle. When eventually the backoff counter reaches zero, I can try again and transmit. The only thing that changes now is that I'm not going to use the same range of possible integers. When I draw the random integer, I use a different range of possible integers.  
这就是退避的工作方式。清楚了吗？我们还有五分钟。让我再说一件事。下次我们会举更多例子，并且稍微更好地理解，为什么有退避，为什么他们引入退避。但是，今天就让我说，在这种情况下，我们把退避计数器减到零，所以我们说：现在我们可以接入信道，再次发送。假设我们再次失败。不幸的是，这可能发生，所以我们再悲观一点。我们再次失败；我们必须再尝试一次。按照停止等待，如果我们尚未达到可能尝试的最大次数，就需要再试一次。我们做什么？我们重复相同的过程，因为我们仍然必须重新竞争信道。这是完全相同的情况。我们需要再次确保信道空闲一个DIFS，然后抽取一个随机整数，把这个随机整数乘以时隙，把退避计数器设置为这个新值，然后，只要信道空闲，就再次开始减少退避计数器。当退避计数器最终达到零时，我就能再试一次并发送。现在唯一改变的是，我不会使用同样的可能整数范围。当我抽取随机整数时，我使用另一个可能整数范围。

## 73 · 01:32:41 · 竞争窗口从31扩展到63

[课件图片：课件：02-WiFi_1-7.pdf · PDF第24页下半页 · 图48（按PDF顺序）](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh#doxcnTO3I3piu0suzRmd0uQiHYS)

图片保存在飞书；此处为原图块链接。新增的4张PNG另收录于可恢复备份ZIP。

课件示例列出31、63、127等窗口及1023上限；课堂01:32:41明确讲到31→63，01:34:32的上限数值在原转写中标为［数字不清楚］。课件数值不替换该不确定标记；表中平均退避时延是课件信息，本段未逐项讲解。

原标说话人 1  01:32:41  
This is the second time that we use backoff for that same data packet. I'm not using this contention window minimum of 31; I use a larger value. We will explain better how this value is determined, but for now consider that, roughly speaking, we double this value. The second time it is basically doubled with respect to the previous value. Instead of 31, we are now using 63. It's not exactly double; roughly speaking, we double it. We are going to see how we determine this value exactly next time. Notice that this means we double the number of possible integers that can be selected. This range is important. Remember that this range always starts from zero. What we double is the right-hand extreme of the range. Before, we were considering from 0 up to 31, 32 possible integers. Now we are considering from 0 to 63, so 64 possible integer values, including zero.  
这是我们为同一个数据包第二次使用退避。我不使用这个值为31的最小竞争窗口；我使用一个更大的值。我们会更好地解释这个值如何确定，但是目前请认为，粗略地说，我们把这个值翻倍。第二次，相对于前一个值，它基本上翻倍。现在，我们不使用31，而使用63。它并非恰好翻倍；粗略地说，我们把它翻倍。下次我们会看怎样精确确定这个值。注意，这意味着我们把可以选择的可能整数的数量翻倍。这个范围很重要。记住，这个范围总是从零开始。我们翻倍的是这个范围的右端点。之前，我们考虑从0一直到31，共32个可能的整数。现在，我们考虑从0到63，因此是64个可能的整数值，包括零。

## 74 · 01:34:32 · 窗口增长上限CW_max

原标说话人 1  01:34:32  
If I fail again and have to repeat the procedure, again it is the same procedure, but this is the third time that I'm running backoff for that same data packet. I'm going to roughly double this value again. Every time, roughly speaking, I double it until I reach a value called CW_max, the maximum contention window, beyond which I don't increase it anymore. Even if I have to run another backoff for the same data packet, once I reach CW_max I don't increase it anymore. Just to give you the idea, this CW_max is typically [number unclear]. The very last thing is: notice that I double this contention window every time I have to repeat the backoff procedure for the same data packet. If at a certain point I'm done with this data packet and start the procedure for a new data packet, I always start from scratch.  
如果我再次失败，必须重复这个过程，那么，同样，它是相同的过程，但是这是我为同一个数据包第三次运行退避。我会再次把这个值大致翻倍。每一次，粗略地说，我都把它翻倍，直到达到一个叫作CW_max的值，也就是最大竞争窗口，超过这个值就不再增加。即使我必须为同一个数据包再运行一次退避，一旦达到CW_max，我就不再增加它。只是为了让你们有个概念，这个CW_max通常是［数字不清楚］。最后一点是：注意，每当我必须为同一个数据包重复退避过程时，我就把这个竞争窗口翻倍。如果在某个时刻，我处理完了这个数据包，并开始处理一个新的数据包，那么我总是从头开始。

## 75 · 01:36:06 · 新数据包从CW_min重新开始

原标说话人 1  01:36:06  
If I have to use backoff for a new data packet, for that new data packet I will start from scratch, that is, from CW_min. For every new packet, if I need to use the backoff procedure, I start from CW_min. It is doubled, roughly speaking doubled, only if I have to repeat the backoff procedure for the same data packet.  
如果我必须为一个新数据包使用退避，那么对于这个新数据包，我会从头开始，也就是从CW_min开始。对于每个新数据包，如果我需要使用退避过程，我就从CW_min开始。只有当我必须为同一个数据包重复退避过程时，它才会翻倍，粗略地说翻倍。

## 76 · 01:36:38 · 下课与下次课程安排

原标说话人 1  01:36:38  
Okay, good. We will see more next time, but for today we are done. We're good to go. Great. We'll meet Monday afternoon. Time to relax.  
好，很好。我们下次会看更多内容，但是今天我们结束了。我们可以走了。很好。我们周一下午见。该放松一下了。
