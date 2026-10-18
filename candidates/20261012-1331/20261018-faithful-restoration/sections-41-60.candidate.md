# 20261012-1331 第41–60段逐字恢复候选

状态：candidate_not_audio_certified。仅对照历史飞书、旧 Qwen 恢复重跑与新无提示 Whisper medium.en 原始识别；没有进行亲耳听辨，不能作为已认证逐字稿。方括号标出待听辨处。段 ID 和原时间标签保持不变；标签只是定位锚，部分完整句子的识别时段跨越标签。两份 m4a 的文件 SHA256 不同，不能称为同一字节音源；时长和内容支持对应。未写入飞书或 GitHub。

## 第41段 00:44:32
段 ID：doxcnpL38KX3LtqqoQ5CnydBzNd
Okay, now let's stop for five minutes.
好，现在我们停五分钟。
And then use the [short break / shortcut unclear], if I'm not wrong.
然后利用这个[短暂休息／捷径，待听辨]，如果我没有弄错的话。
Okay, and then we will resume and see how [this probability / these probabilities unclear] of collision can be computed.
好，然后我们会继续，看看[这个／这些，单复数待听辨]碰撞的概率如何能够计算出来。

## 第42段 00:49:19
段 ID：doxcnBQOCHSdBhJ0SZfY43litTc
Okay, good.
好，很好。
[So / Now unclear], let's look at our computation.
[所以／现在，待听辨]，我们来看我们的计算。
So, the probability that B and C collide is, as we said, very simply, so [don't / do not unclear] worry, this is a very, very simple derivation.
所以，B 和 C 碰撞的概率，正如我们所说，非常简单地，所以[不用／不要，待听辨]担心，这是一个非常、非常简单的推导。
Is the probability that B and C draw the same value, let's say n, okay?
就是 B 和 C 抽到相同的值，比如说 n，好吗？
[A / the unclear] same value, [a / the unclear] same integer.
[一个／这个，待听辨]相同的值，[一个／这个，待听辨]相同的整数。
That's what we said, all right.
那就是我们说的，好吧。
Let's start this computation by considering that B draws n, a given integer n, whatever this is.
我们开始这个计算，先考虑 B 抽到 n，一个给定的整数 n，不管这个是多少。
So, what we are first computing is the [conditional / conditioned unclear] probability, so the probability that C draws also n, so n, given that B drew n, okay?
所以，我们首先正在计算的是[conditional／conditioned，待听辨]概率，也就是 C 也抽到 n 的概率，所以是 n，已知 B 抽到了 n，好吗？
So this is the so-called conditioned probability.
所以这就是所谓的条件概率。
Now remember, our scheme is actually very simple because it's distributed.
现在记住，我们的方案实际上非常简单，因为它是分布式的。
And as we said, every node makes its own decisions according to the protocol rules, but it makes its own decisions independently from the others, right?
而且，正如我们说的，每个节点按照协议规则作出自己的决定，但它独立于其他节点作出自己的决定，对吧？

## 第43段 00:51:21
段 ID：doxcns4CMNfXgAjgRek2xop5aSh
So, the fact that B drew n will not affect the probability that C draws n.
所以，B 抽到了 n 这个事实不会影响 C 抽到 n 的概率。
C does whatever, let's say, [he / it unclear] likes, based on what decisions [he / it unclear] makes following the protocol, right?
C 做任何，假设说，[他／它，待听辨]喜欢做的事，根据[他／它，待听辨]遵循协议作出的决定，对吧？
But it's not affected by what other nodes do.
但它不会受到其他节点所做事情的影响。
So, this is actually equal to the probability that C draws n, simply that, because it doesn't matter what B does, right?
所以，这实际上就等于 C 抽到 n 的概率，就是这样，因为 B 做什么并不重要，对吧？
C will do things by [itself / himself / themselves unclear].
C 会[自己，反身代词待听辨]做事情。

## 第44段 00:52:17
段 ID：doxcndVEHARMqt6UlFaVILYkrob
Okay, so what is the probability that C draws n?
好，所以 C 抽到 n 的概率是什么？
So, what is the probability that an integer is selected out of the range zero, CW_min?
所以，从零、CW_min 这个范围中选出一个整数的概率是什么？
Well, we have written that here, right?
嗯，我们已经把那个写在这里了，对吧？
This is the probability.
这就是那个概率。
Okay, so now we know that given that B has drawn n, the probability that C will also draw n is this one.
好，所以现在我们知道，已知 B 已经抽到了 n，C 也会抽到 n 的概率就是这个。
Okay, so [conditioned / condition unclear] to the fact that B drew n, then this is the collision probability [conditioned / condition unclear] to the fact that B drew n, right?
好，所以[conditioned／condition，词尾待听辨]于 B 抽到了 n 这个事实，那么这就是[conditioned／condition，词尾待听辨]于 B 抽到了 n 这个事实的碰撞概率，对吧？

## 第45段 00:53:12
段 ID：doxcn1OwmYmonhT50Rlx5H4yd4K
What we need to do is to now to compute the original probability, is to decondition and make the computation for any possible n.
我们需要做的是现在去计算原来的概率，是去掉条件，并对任何可能的 n 进行计算。
So, what we want to now do is to compute in general the probability that B and C collide without conditioning to any event.
所以，我们现在想做的是一般地计算 B 和 C 碰撞的概率，不以任何事件为条件。
So that is, we need to consider all possible values of integer from zero to CW_min.
所以，也就是说，我们需要考虑从零到 CW_min 的所有可能的整数的值。
And for any n, we know that the probability of collision is what?
而对于任何 n，我们知道碰撞的概率是什么？
The probability that C draws n if also B has drawn n, right?
如果 B 也已经抽到了 n，C 抽到 n 的概率，对吧？

## 第46段 00:54:22
段 ID：doxcnflxhsrZ0Q4lhw4fU7eq5xe
So, let's first write the probability that B draws n.
所以，我们先写出 B 抽到 n 的概率。
The probability that B draws n is again this one.
B 抽到 n 的概率又是这个。
So we can write one over CW_min plus one.
所以我们可以写一除以（CW_min 加一）。
This is the probability that B draws n.
这就是 B 抽到 n 的概率。
And then given that, we know that [a / the unclear] collision happens if C also draws n.
然后，给定那个，我们知道，如果 C 也抽到 n，就会发生[一次／这次，待听辨]碰撞。
That happens with this probability.
那件事以这个概率发生。

## 第47段 00:54:59
段 ID：doxcnpIXR5BhdcEJODa1iMozspe
So we multiply by again one over CW_min plus one, which is the probability that C [draws / grows unclear] n.
所以我们再乘以一除以（CW_min 加一），也就是 C [抽到／grows，待听辨] n 的概率。
So what we have is simply sum over n that goes from zero to CW_min of one over CW_min plus one squared, [right / okay unclear]?
所以，我们得到的就是对从零到 CW_min 的 n 求和，求一除以（CW_min 加一）的平方的和，[对吧／好吗，待听辨]？
Now, this is a constant term, we are inside a sum, so we are summing this constant term how many times?
现在，这是一个常数项，我们在一个求和里面，所以我们把这个常数项加多少次？
CW_min plus one times, right?
（CW_min 加一）次，对吧？
So this is equal to CW_min plus one divided by CW_min plus one squared.
所以这等于（CW_min 加一）除以（CW_min 加一）的平方。
We simplify numerator and denominator, and we get one over CW_min plus one.
我们把分子和分母约简，就得到一除以（CW_min 加一）。

## 第48段 00:56:35
段 ID：doxcnnL1HcoGHeu170WeLRQgmwb
So, the final result of all [this computation / these computations unclear] is that the probability that B and C collide in our simple example that we presented earlier is one over the contention window plus one.
所以，所有[这个计算／这些计算，待听辨]的最终结果是，B 和 C 在我们前面展示的这个简单例子里碰撞的概率是一除以（竞争窗口加一）。
Okay, now if you [were / are unclear] able to follow the computation, great.
好，现在，如果你们[之前能够／能够，时态待听辨]跟上这个计算，那很好。
It's a simple probability computation, but if your background is different, and therefore you have not seen probability anywhere in your previous courses, do not worry.
这是一个简单的概率计算，但是如果你们的背景不同，因此在你们之前的课程里的任何地方都没有见过概率，不要担心。
The important thing is that you retain the final message.
重要的事情是你们记住最后的信息。

## 第49段 00:57:27
段 ID：doxcnJ5JJMQGLQYI4WCncznRwTb
The final message is, in our simple example, right, that we are considering, the probability that B and C [collide / collided unclear] while performing the backoff procedure is equal to this ratio, that clearly will decrease as the value of contention window minimum increases, right?
最后的信息是，在我们这个简单的例子里，对吧，在我们正在考虑的这个例子里，B 和 C 在执行退避过程时[碰撞／发生了碰撞，时态待听辨]的概率等于这个比值，而这个比值显然会随着最小竞争窗口的值增加而减小，对吧？
The larger the contention window, the lower this ratio, so the lower the collision probability.
竞争窗口越大，这个比值越低，所以碰撞概率越低。
This is, I think, something that everybody [can understand / understands unclear].
我觉得，这是每个人都[能够理解／理解，待听辨]的事情。
Okay, now, so this means that, okay, this refers, as I said, to the previous simple example, but it's a general rule.
好，现在，所以这意味着，好，正如我说的，这是指前面那个简单的例子，但它是一条一般规律。
The collision probability in the backoff procedure decreases as the value of contention window increases.
退避过程中的碰撞概率随着竞争窗口的值增加而降低。
So now, what does this tell you?
那么现在，这告诉你们什么？
Why am I marking this, [and making / I'm making unclear] this second observation?
我为什么要标出这一点，[并作出／我在作出，待听辨]这第二个观察？
Because remember, we wanted to understand the reason why in Wi-Fi we say every time we perform the backoff procedure for a given data packet, we roughly speaking double the contention window.
因为记住，我们想理解为什么在 Wi-Fi 中我们说，每次为一个给定的数据包执行退避过程时，我们大致来说把竞争窗口扩大一倍。
So we increase it very significantly every time.
所以我们每次都非常显著地增加它。
Why do we do that?
我们为什么这样做？
To reduce the probability of collision among [contending / contend unclear] nodes.
为了降低[正在竞争的／contend，词尾待听辨]节点之间的碰撞概率。

## 第50段 00:59:34
段 ID：doxcnUwQc9ePMHTxq4Ra0PKvQIf
[Okay unclear], so, backoff is a probabilistic mechanism, and essentially Wi-Fi assumes that the reason why a transmitter is failing, failing, failing is because there are too many nodes in the network that try to access the channel to transmit a packet.
[好，待听辨]，所以，退避是一种概率性机制，而基本上 Wi-Fi 假定，一个发送方失败、失败、失败的原因，是网络中有太多节点尝试接入信道来发送一个数据包。
The situation is too crowded.
这个情况太拥挤了。
So what Wi-Fi says is, if you fail, [fail, fail unclear], every time you fail means that there are other nodes trying, and you are selecting the same backoff, you have the same backoff time, and you keep colliding.
所以 Wi-Fi 说的是，如果你失败，[失败、失败，重复待听辨]，你每一次失败都意味着还有其他节点在尝试，而你们选择了相同的退避，你们有相同的退避时间，而且你们持续碰撞。
So in order to reduce the probability of collision, each node needs to enlarge the possible values, so the choice, right, among the integers that can be selected.
所以，为了降低碰撞的概率，每个节点都需要扩大可能的值，所以是选择，对吧，在那些可以被选中的整数之间。

## 第51段 01:00:35
段 ID：doxcneECTaGLIYZElqo3ZcJjZPe
It's like when you have a bag with candies, if they are all strawberry flavored, if there are two people picking the candy, clearly they will pick strawberry.
这就像当你有一个装着糖果的袋子，如果它们全是草莓味的，如果有两个人在拿糖果，显然他们会拿到草莓味的。
But if instead you fill the bag with banana, strawberry, peach, mint, and so on, then the probability that two people pick the same candy flavor will reduce.
但是，如果你改为在袋子里装上香蕉味、草莓味、桃子味、薄荷味等等，那么两个人拿到相同糖果口味的概率会降低。
So this is exactly the same [principle / thing unclear].
所以这完全是相同的[原理／事情，待听辨]。
Okay, so you may say, well, nice, Wi-Fi really takes care of this crowded situation and allow us to perform better.
好，所以你可能会说，嗯，很好，Wi-Fi 确实照顾到了这个拥挤的情况，而且让我们表现得更好。
True, but this is, this works, this is a good idea to double the contention window every time you perform a backoff to transmit [a / the unclear] packet.
是的，但是这是，这有效，这是个好主意，每次你为了发送[一个／这个，待听辨]数据包而执行退避时，就把竞争窗口扩大一倍。
It works, but it works if the reason why a transmitter is failing is indeed because it [it unclear] keeps colliding with others.
它有效，但它有效的条件是，发送方失败的原因确实是它[它，重复待听辨]持续与其他节点碰撞。
But remember, in wireless, a transmission may fail also because of channel errors.
但是记住，在无线通信中，一次传输也可能因为信道差错而失败。
So you may be the only one in the network with a packet to transmit and still fail because the channel is bad and the receiver cannot demodulate the signal correctly.
所以，你可能是网络中唯一有一个数据包要发送的那个，但仍然失败，因为信道不好，而接收方无法正确地解调信号。
Okay, so in that case, of course, you have to follow the protocol rules anyway.
好，所以在那种情况下，当然，你无论如何都必须遵守协议规则。
Okay, so if you fail and fail because of channel errors, you have to apply the rules.
好，所以如果你因为信道差错而失败，又失败，你必须应用这些规则。
And this means that every time you have to enlarge the contention window, and statistically it's more likely that you will draw a long and longer and longer backoff time, right?
而这意味着，你每次都必须扩大竞争窗口，而从统计上说，你更有可能会抽到一个长的、又更长、又更长的退避时间，对吧？
So is this good in this case?
所以，这在这种情况下好吗？
[Hmm unclear], not really good, right?
[嗯，待听辨]，不太好，对吧？
Because the reason why you are failing is not because there are others and you are colliding, that's not the reason.
因为你失败的原因不是因为有其他节点而你正在碰撞，那不是原因。
The reason is that the channel is poor, of poor quality, and this mechanism does not help to solve the issue, right?
原因是信道差，质量差，而这种机制没有帮助解决这个问题，对吧？
Actually, this [method / mechanism unclear] in this situation is even harmful.
实际上，这个[方法／机制，待听辨]在这种情况下甚至是有害的。
Why?
为什么？
Because it makes you delay channel access, right?
因为它让你延迟信道接入，对吧？
It makes you wait longer and longer and longer before accessing the channel, being able to access the channel and transmit the packet.
它让你等得更久、又更久、又更久，然后才能接入信道，能够接入信道并发送数据包。
With no reason, because the problem is not collision, the problem is poor channel quality.
没有理由，因为问题不是碰撞，问题是信道质量差。
So it just increases the channel access delay.
所以，它只是增加了信道接入时延。
It doesn't help with anything.
它对任何事情都没有帮助。

## 第52段 01:04:00
段 ID：doxcn7v1pOcJSqW4rkKPR4G6heb
Okay, so we need to be aware that, well, we need to understand why certain techniques, mechanisms are designed in a certain way.
好，所以我们需要意识到，嗯，我们需要理解为什么某些技术、机制以某种方式来设计。
But we need also always to look at these mechanisms or techniques or solutions with a critical eye.
但是我们也需要总是以批判的眼光来看这些机制，或者技术，或者解决方案。
That means we need to look at them and ask ourselves, is this really good in under all conditions, under all situations, or not?
那意味着我们需要看着它们并问自己，这真的在，在所有条件下，在所有情况下都好吗，还是不是呢？
There may be aspects of technology that are not that good, not always, and we need to be aware of that.
技术的某些方面可能不是那么好，不是总是好，而我们需要意识到这一点。
Okay, so whenever we design a system, whenever we design a technological solution, we need to account for possible issues that may arise.
好，所以每当我们设计一个系统，每当我们设计一个技术解决方案时，我们需要考虑可能出现的那些问题。
So an idea may be good to solve one problem, but it might actually make things worse in other situations.
所以，一个想法可能对解决一个问题很好，但它实际上可能会让其他情况下的事情变得更糟。
So we need also to look at the big picture when we design a technology.
所以我们在设计一项技术时，也需要看整体情况。
[Okay unclear], and [and unclear] this is indeed an example of [of unclear] that.
[好，待听辨]，而且[而且，重复待听辨]，这的确就是那个的[的，重复待听辨]一个例子。

## 第53段 01:05:29
段 ID：doxcn6EVnNwTDOuu398ghwuxGRc
[Um unclear], the last thing that I would like to comment, and then we go to the third situation, is remember that we are considering how to transmit unicast data packets, right?
[嗯，待听辨]，我最后想评论的事情，然后我们就去第三种情况，是记住我们正在考虑如何发送单播数据包，对吧？
We said that.
我们说过那个。
Let me just mention again that in the case of multicast or broadcast data packet, things are much, much simpler, because we do not expect any acknowledgement.
让我再提一下，在多播或广播数据包的情况下，事情要简单得多、得多，因为我们不期待任何确认。

## 第54段 01:06:05
段 ID：doxcnVDHtpDHmdLfVNMU7A5Z1nh
Indeed, since broadcast and multicast packets are intended for multiple destinations, we cannot have receivers sending back acknowledgments, because all these acknowledgments, if sent at the same time, will collide [with / within unclear] each other.
确实，因为广播和多播数据包面向多个目的地，我们不能让接收方发回确认，因为所有这些确认，如果同时发送，会相互[with／within，介词待听辨]碰撞。
So no use.
所以没用。

## 第55段 01:06:45
段 ID：doxcna5EZSQva8EAx8UH3RzbFKh
If you had to desynchronize the acknowledgments transmissions, that would be very, very complicated.
如果你必须让那些确认的传输错开时间，那会非常、非常复杂。
And [it / you unclear] would increase the overhead of the protocol.
而且[它／你，待听辨]会增加协议的开销。
So that's [not good / done unclear].
所以那[不好／完了，待听辨]。
So the choice that they made was, well, if a packet is broadcast or multicast, the transmitter of course needs to sense the channel.
所以他们作出的选择是，嗯，如果一个数据包是广播或多播数据包，发送方当然需要侦听信道。
If the channel is idle, transmit.
如果信道空闲，发送。
If the channel is busy, of course, you have to perform the backoff procedure because you have to wait.
如果信道忙，当然，你必须执行退避过程，因为你必须等待。
But then once you access the channel and transmit, that's it.
但然后一旦你接入信道并发送，就这样了。
Okay, you are done, because you don't care if the packet was received successfully or unsuccessfully.
好，你完成了，因为你不在乎数据包是被成功接收了，还是没成功接收。
[You / we unclear] are done.
[你／我们，待听辨]完成了。
Okay, so broadcast and multicast packets are transmitted only once.
好，所以广播和多播数据包只发送一次。
So you may need to run the backoff procedure for those data packets, but just if, when you want to access the channel, you sense the channel as busy the first time, okay?
所以，你可能需要为那些数据包运行退避过程，但只是在你想接入信道时，第一次就侦听到信道忙的情况下，好吗？
Then once you perform the backoff and you access the channel and transmit, you are done.
然后，一旦你执行退避，而你接入信道并发送，你就完成了。
Okay, [um unclear], if everything is clear so far, let me know if you have questions.
好，[嗯，待听辨]，如果到目前为止所有事情都清楚了，有问题就告诉我。
No questions?
没有问题吗？
Okay, so if we are good, then we can now tackle this last condition.
好，所以如果我们都没问题，那么我们现在就可以处理这最后一种情况。
That is, well, we have one more situation under which we perform the backoff.
也就是说，嗯，我们还有一种情况，在这种情况下我们执行退避。
In this third situation, actually, the procedure is slightly, slightly different, okay?
在这第三种情况下，实际上，这个过程稍微、稍微有点不同，好吗？
[It is / is, is unclear] essentially the same except for one [thing unclear].
[它是／是、是，待听辨]基本上相同的，除了一个[事情，待听辨]。
What is this third situation?
这个第三种情况是什么？
[And it is called unclear], in this case the procedure is called [fast / post unclear] backoff, just to underline that there is a small difference with respect to the backoff run under the previous two situations.
[而且它叫作，待听辨]，在这种情况下，这个过程叫作[fast／post，待听辨]退避，只是为了强调它与前面两种情况下运行的退避有一个小的区别。

## 第56段 01:09:19
段 ID：doxcnSOlCgY8oM1YQQ6YaPFWmPg
So what is this third situation?
所以，这第三种情况是什么？
[It is / is unclear] when a node transmits a data packet successfully.
[它是／是，待听辨]当一个节点成功发送一个数据包的时候。
So you may say, well, why do I have to perform the backoff in this case?
所以，你可能会说，嗯，在这种情况下我为什么必须执行退避？
[I transmitted / I've transmitted unclear] my packet correctly, [I'm / and unclear] done.
[我发送了／我已经发送了，时态待听辨]我的数据包，而且发送正确，[我／而且，待听辨]完成了。
What do you want from me?
你还想让我做什么？
Well, the Wi-Fi says, I know you transmitted your packet, you are done with that, but after you receive the ACK from the receiver, you need to perform a backoff using zero, CW_min as range of possible integers.
嗯，Wi-Fi 说，我知道你发送了你的数据包，你已经完成了那个，但在你从接收方收到 ACK 之后，你需要执行一次退避，用零、CW_min 作为可能的整数的范围。
That's [what / why unclear] the protocol says.
那就是协议[所说的／为什么说，待听辨]。

## 第57段 01:10:13
段 ID：doxcnYKp8xXaOwlMx8lzDMPjmEh
So again, we want to understand why, right?
所以，我们还是想理解为什么，对吧？
[I mean / maybe unclear], this is not enough.
[我的意思是／也许，待听辨]，这还不够。
Okay, I have to do it, I will do it, but tell me why, why do I have to do that?
好，我必须做，我会做，但告诉我为什么，为什么我必须那样做？
Well, the reason is fairness.
嗯，原因是公平性。
We want to be fair to our nodes.
我们想公平地对待我们的节点。

## 第58段 01:10:32
段 ID：doxcnBdnbpPGhKGwvSK0xHE3Xkf
Okay, so let me give [you unclear] an example, and that will allow us to indeed understand why they tell us, once you transmit successfully, run this post-backoff.
好，所以让我[给你们，待听辨]举一个例子，而那会让我们的确理解为什么他们告诉我们，一旦你成功发送，就运行这个发送后退避。
So let's consider again the same scenario, so that will be easy.
所以，我们再考虑同一个场景，那样就容易了。
Access point, and then node A.
接入点，然后节点 A。
And then we can also consider our B and C nodes, right?
然后我们也可以考虑我们的 B 和 C 节点，对吧？
Same as before.
和之前一样。
So we know [already / that with unclear] the story, it will be easier.
所以我们[已经／that with，待听辨]知道这个过程，它会更容易。
So the story starts in the same way.
所以，这个过程以同样的方式开始。
A has got a packet, [DIFS unclear], channel idle, transmits the data packet, unicast data packet to the access point.
A 有了一个数据包，[DIFS，待听辨]，信道空闲，发送这个数据包，单播数据包给接入点。
This packet transmission is successful, so the access point [sends / sent unclear] back the ACK.
这次数据包传输是成功的，所以接入点[发回／发回了，时态待听辨] ACK。

## 第59段 01:11:51
段 ID：doxcnWJukIbTM7WOpJFug42kc4d
And as we said before, all nodes are in radio visibility of each other, they can hear each other.
而且正如我们之前说的，所有节点都处在彼此的无线可见范围内，它们可以互相听到。
So B and C will set their [NAV unclear].
所以 B 和 C 会设置它们的[NAV，待听辨]。
And same as before, at a certain point B and C get a packet from their respective higher layers, so they will have to transmit their packet, right?
而且和之前一样，在某个时刻 B 和 C 从它们各自的高层收到一个数据包，所以它们将必须发送它们的数据包，对吧？

## 第60段 01:12:20
段 ID：doxcnJy0CfZy89ROVTTTAPVxpFe
And we know already how things work, fine, but now our attention is on A, okay?
而且我们已经知道事情如何进行，很好，但现在我们的注意力在 A 上，好吗？
Let's focus on A.
我们把注意力放在 A 上。
A is the one that performs its transmission successfully, so it's done.
A 是那个成功进行它的传输的节点，所以它完成了。
And according to the protocol, now we know that A actually, once it has finished transmitting the packet and [received / receive unclear] the ACK, needs to perform this [post / past / fast unclear] backoff procedure, right?
而根据协议，现在我们知道，A 实际上，一旦它已经发送完数据包并且[收到了／收到，时态待听辨] ACK，就需要执行这个[post／past／fast，待听辨]退避过程，对吧？
So [it / I unclear] will have to sense the channel for [DIFS unclear], and then [it / you / we unclear] will have to draw an integer out of the range zero, CW_min.
所以[它／我，待听辨]将必须侦听信道一个[DIFS，待听辨]的时间，然后[它／你／我们，待听辨]将必须从零、CW_min 这个范围中抽取一个整数。
And of course for B and C we'll have the same behavior as before.
而且当然，对于 B 和 C，我们会有和之前相同的行为。
We know [that already / that's ready unclear].
我们知道[那个已经／that's ready，待听辨]。
So B and [and unclear] C will have to run a, let's say, regular backoff procedure.
所以 B 和[和，重复待听辨] C 将必须运行一个，我们说，常规的退避过程。
