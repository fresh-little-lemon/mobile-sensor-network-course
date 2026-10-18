待核验候选：未完成人工听辨，不可当成最终逐字稿。方括号标示争议或缺词；保留原段时间锚。

原标说话人 1  00:22:43
What I need to do is to apply backoff.
我需要做的就是执行退避。
So what [it will / you will, unclear] do is wait for the channel to become idle again, sense the channel idle for DIFS, and then, if the channel is idle for DIFS, it will be able to draw an integer, right?
所以，[它将要／你将要，待听辨]做的就是等信道再次变为空闲，侦听信道空闲一个 DIFS 的时间，然后，如果信道空闲了一个 DIFS 的时间，它就能够抽取一个整数，对吧？
Out of what?
从什么里面抽取？
Out of the range zero, CW_min.
从零、CW_min 这个范围里面。
And the same C, right?
C 也一样，对吧？
C at this point in time says, oh, I got a packet to transmit, but the channel is busy.
C 在这个时间点说，哦，我拿到了一个要发送的数据包，但是信道是忙的。
So again, it knows that it has to perform a backoff.
所以，再说一次，它知道它必须执行一次退避。
So what it will do?
所以，它会做什么？
It will wait for the channel to become idle.
它会等信道变为空闲。
Then it needs to verify that the channel is idle for DIFS.
然后，它需要确认信道空闲了一个 DIFS 的时间。
The channel will be idle because nobody else is doing anything, so the channel is idle.
信道会是空闲的，因为其他谁也没有在做什么，所以信道是空闲的。

原标说话人 1  00:24:00
[And it too will draw / And it will do, will draw, unclear] an integer with equal probability out of this same range of values, okay?
[它也会抽取／它会做，会抽取，待听辨]一个整数，从这同一个取值范围中等概率地抽取，好吗？
So let's assume that the value drawn by B, the integer, is equal to two.
所以，我们假设 B 抽到的值，这个整数，等于二。
And let's assume that the integer drawn by C is equal to five.
再假设 C 抽到的整数等于五。
This is just an example.
这只是一个例子。

原标说话人 1  00:24:36
Okay, so if this is the case, then we know that B will compute its backoff time, that will be equal to two times the time-slot duration, right?
好，所以，如果是这种情况，那么我们知道 B 会计算它的退避时间，这个时间会等于时隙时长的两倍，对吧？
And similarly C will compute its backoff time, that will be five time slots.
同样，C 会计算它的退避时间，这个时间会是五个时隙。
And then each of them will have to decrease its own backoff counter, time slot by time slot.
然后，它们各自都必须逐个时隙地递减自己的退避计数器。
So B will start sensing the channel for a time slot.
所以，B 会开始侦听信道一个时隙的时间。
The channel is currently idle, so it will decrease its backoff counter by one.
信道目前是空闲的，所以它会把退避计数器减一。
And the same will do C, right?
C 也会这样做，对吧？
So it will decrease it by, its own counter by one.
所以，它会把它减去，把自己的计数器减一。
Then, next time slot, again B senses the channel [is / as, unclear] idle, decreases its backoff counter by one.
然后，下一个时隙，B 再次侦听信道[是／为，待听辨]空闲，把退避计数器减一。
And C will do the same.
C 也会这样做。
But now the backoff counter of B has reached zero.
但是现在，B 的退避计数器已经到零了。

原标说话人 1  00:26:12
So B is entitled to access the channel [and transmit, unclear].
所以，B 有资格接入信道[并发送，待听辨]。
So it will transmit its data packet.
所以，它会发送自己的数据包。
The data packet clearly is intended for the access point because, as we said, we are considering unicast packets.
这个数据包显然是发给接入点的，因为，正如我们说过的，我们考虑的是单播数据包。
And in this network topology, network architecture, all Wi-Fi user nodes communicate with the access point only.
而在这种网络拓扑，网络架构中，所有 Wi-Fi 用户节点都只与接入点通信。
Let's again be optimistic.
让我们再乐观一点。
So this means that this packet is received successfully by the access point, which will send back an acknowledgement after SIFS.
所以，这意味着接入点成功接收到了这个数据包，它会在 SIFS 之后发回一个确认。

原标说话人 1  00:27:02
Upon the data transmission by B, the other nodes, right, can set their NAV.
在 B 发送数据时，其他节点，对吧，可以设置自己的 NAV。
They can read the Duration field in the header of the data packet.
它们可以读取数据包首部中的 Duration 字段。
So we need also to highlight this, that both A and also C will set their NAV, right?
所以，我们还需要强调这一点，就是 A，还有 C，都会设置自己的 NAV，对吧？
So what does it mean for A?
所以，这对 A 来说意味着什么？
This is okay, fine, it doesn't have anything to do, so that's [not okay / okay, unclear].
这没问题，很好，它没有什么要做的，所以那是[不行的／没问题的，待听辨]。
But for C, this means that [it / you, unclear] will have to freeze its backoff counter for this duration, right?
但是对 C 来说，这意味着[它／你，待听辨]必须在这段时间内冻结它的退避计数器，对吧？

原标说话人 1  00:28:03
Because now the channel is busy, so C cannot decrease its counter, it has to suspend the countdown.
因为现在信道是忙的，所以 C 不能递减计数器，它必须暂停倒计时。
Okay, so during all this time C will be essentially blocked, and what it does is to wait for the channel to become idle again.
好，所以，在这整个时间里，C 基本上会被阻住，而它做的就是等待信道再次变为空闲。
[It / he, unclear] makes sure that the channel is idle for DIFS, and then [it / he, unclear] can resume decreasing its backoff [counter / count, unclear], [right, unclear]?
[它／他，待听辨]确认信道空闲了一个 DIFS 的时间，然后[它／他，待听辨]就可以恢复递减它的退避[计数器／计数，待听辨]，[对吧，待听辨]？
It has still three time slots to go, so [it / he, unclear] will sense the channel for a [time slot, possibly incomplete].
它还剩三个时隙，所以[它／他，待听辨]会侦听信道一个[时隙，此处可能没说完，待听辨]。
Yes, this is idle, so it can decrease the backoff counter by one.
是的，这是空闲的，所以它可以把退避计数器减一。
Then it senses the channel again for a time slot.
然后，它再次侦听信道一个时隙的时间。
The channel is idle, it can decrease the counter by one, and then again, the channel is idle for one more time slot, it can decrease its counter by one.
信道是空闲的，它可以把计数器减一，然后再一次，信道又空闲了一个时隙，它可以把计数器减一。

原标说话人 1  00:29:23
Now its backoff counter is down to zero, so [it / you, unclear] can access the channel and transmit its data packet.
现在，它的退避计数器降到了零，所以[它／你，待听辨]可以接入信道并发送它的数据包。
And again, being optimistic, we say that this is successful, so [it / we, unclear] will receive the acknowledgement after SIFS.
再一次，乐观地说，我们说这次是成功的，所以[它／我们，待听辨]会在 SIFS 之后收到确认。
And we are all happy because all nodes could transmit [their data packet successfully, unclear].
我们都很高兴，因为所有节点都能够[成功发送各自的数据包，待听辨]。
Okay, so this is an example of how we apply [in the, unclear] backoff procedure, in particular under this condition, right?
好，所以，这是一个我们如何应用[此处有不清楚的词]退避过程的例子，特别是在这种情况下，对吧？
But it allows [us, unclear] also to understand the importance of backoff.
但是，它也让[我们，待听辨]理解退避的重要性。
That's the final goal [that I, unclear], the ultimate goal that I was aiming.
这就是最后的目标[我所，待听辨]，我所追求的最终目标。

原标说话人 1  00:30:26
How can we understand the importance of backoff?
我们怎样才能理解退避的重要性？
Well, let's make a little game that is, scientifically speaking, is called ablation study, okay?
嗯，让我们做一个小游戏，这就是，从科学上说，是叫作消融研究的东西，好吗？
An ablation study is when you remove a feature of a system, and you study the behavior of that system without that feature.
消融研究就是，你去掉一个系统的某个特性，然后研究没有那个特性时这个系统的行为。
So our small game is an ablation study of this particular [um, unclear] backoff procedure, or, or Wi-Fi channel access.
所以，我们这个小游戏是对这个特定的[嗯，待听辨]退避过程，或者，或者 Wi-Fi 信道接入，做一个消融研究。
So let's make this [a, unclear] small game and think, what would happen if the backoff were not there?
所以，让我们做这个[这里是否有 a，待听辨]小游戏并想一想，如果没有退避，会发生什么？

原标说话人 1  00:31:22
Okay, so let's roll back the story, let's start from the beginning, but this time let's assume that there is no backoff, okay?
好，所以，让我们把这个故事倒回去，让我们从头开始，但这次我们假设没有退避，好吗？
So what would be the behavior of our nodes?
那么，我们的节点会有怎样的行为？

原标说话人 1  00:31:43
Well, at the beginning everything is the same because the only node that has got a packet to transmit is A, right?
嗯，在一开始，一切都是一样的，因为唯一拿到了一个要发送的数据包的节点是 A，对吧？
So it will listen to the channel, the channel is idle for DIFS.
所以，它会侦听信道，信道空闲了一个 DIFS 的时间。
It will access the channel and transmit the packet.
它会接入信道并发送这个数据包。

原标说话人 1  00:32:02
And again, let's be optimistic.
再一次，让我们乐观一点。
The access point sends back [the / an / no article, unclear] acknowledgement, and the other nodes, B and C, both set their NAV, right?
接入点发回确认，[英文这里的冠词待听辨]，而其他节点 B 和 C 都设置自己的 NAV，对吧？
This is exactly as before.
这和之前完全一样。
And again, B and C at different points in time, assume that they [get / got, unclear] also a packet to transmit.
再一次，B 和 C 在不同的时间点，假设它们也[拿到／拿到了，待听辨]一个要发送的数据包。
But again, now we do not have backoff, okay?
但是，再说一次，现在我们没有退避，好吗？
So we have to think, what would happen if backoff were not there?
所以，我们必须想一想，如果没有退避，会发生什么？
So what would B and C do?
那么，B 和 C 会做什么？
Well, we still have carrier sensing, right, multiple access.
嗯，我们仍然有载波侦听，对吧，多址接入。
So since both B and C sense the channel as busy because they have their NAV set, they cannot access the channel, right?
所以，由于 B 和 C 都侦听到信道为忙，因为它们设置了 NAV，它们就不能接入信道，对吧？
Till the channel is busy, I cannot access the channel.
直到信道忙着的时候，我不能接入信道。
So for sure B and C will again wait for the channel to be idle, make sure that the channel is idle.
所以，B 和 C 肯定会再次等待信道变为空闲，确认信道是空闲的。
But then if there is no backoff, they can just access the channel, right?
但是随后，如果没有退避，它们就可以直接接入信道，对吧？
Because now the channel is idle, so they say, oh, channel idle, I can access the channel and transmit.
因为现在信道是空闲的，所以它们说，哦，信道空闲，我可以接入信道并发送。
Remember, we are playing this small game assuming that there is no backoff.
记住，我们是在玩这个小游戏，假设没有退避。
So what we have is that, no backoff, we have both transmitting their data packet after having sensed the channel idle.
所以，我们得到的情况是，没有退避，我们有两个节点都在侦听到信道空闲之后发送自己的数据包。
So what do we have here?
所以，我们这里有什么？
Collision, right?
碰撞，对吧？
They both access the channel at the same time with probability one.
它们以概率一同时接入信道。
It is sure that they will do that, and of course they will fail because they overlap, their transmissions overlap.
它们肯定会这样做，当然它们会失败，因为它们重叠了，它们的传输重叠了。
And the access point will not be able to demodulate correctly either this packet.
而接入点将无法正确解调这两个数据包中的任何一个。

原标说话人 1  00:34:43
Okay, so what is the first conclusion here?
好，所以，这里的第一个结论是什么？
That the backoff procedure has been introduced in our system in order to avoid collisions between contending nodes.
就是，在我们的系统中引入退避过程，是为了避免竞争节点之间的碰撞。
Our contending nodes in these examples are B and C, right?
在这些例子中，我们的竞争节点是 B 和 C，对吧？
They are contending for the channel.
它们在竞争信道。
And the backoff procedure is there to avoid the collision between them.
退避过程就是用来避免它们之间的碰撞的。
So again, remember that we said Wi-Fi is a CSMA scheme with collision avoidance, [right, unclear]?
所以，再说一次，记住我们说过，Wi-Fi 是一种带碰撞避免的 CSMA 方案，[对吧，待听辨]？

原标说话人 1  00:35:39
This backoff is a mechanism that helps to avoid collisions.
这个退避是一种帮助避免碰撞的机制。
So the basic principle, the basic idea is very simple.
所以，基本原理，基本想法，非常简单。
Whenever there is a crowded situation, right, you try to desynchronize from the others so that you find a free [route / road, unclear] ahead, and this is exactly the same thing.
每当出现拥挤的情况，对吧，你就试着与其他人错开，使你前面有一条空闲的[路线／道路，待听辨]，而这完全是同一回事。
So if there is peak hour, you don't want to jump into the traffic, right, [as all / as for, unclear] the others.
所以，如果是高峰时段，你就不想冲进车流，对吧，[像其他所有人／至于其他人，待听辨]。

原标说话人 1  00:36:25
You try to pick, you wait, you try to pick a time at which not many other people will be there.
你试着挑选，你等待，你试着挑选一个没有太多其他人会在那里的时间。
And this is exactly the same principle.
而这完全是同一个原理。
You try to pick a time in order to desynchronize your action with respect to the others, and this way you avoid meeting, [unclear words], colliding with the others, or finding yourself in a, in a traffic jam.
你试着挑选一个时间，让你的行动与其他人的行动错开，这样你就避免遇到，[此处词语不清楚]，与其他人发生碰撞，或者发现自己陷在一个，一个交通堵塞中。
[Hmm, unclear], that's exactly the same principle.
[嗯，待听辨]，这完全是同一个原理。

原标说话人 1  00:37:02
Now what I would like to underline is that, so we observe, our first observation is that backoff is a mechanism for avoiding collisions, but it is still probabilistic, okay?
现在，我想强调的是，所以我们观察到，我们的第一个观察是，退避是一种避免碰撞的机制，但它仍然是概率性的，好吗？
Why?
为什么？
Because if, like in our example, both B and C draw the same value of backoff, they are going to collide.
因为，如果像我们的例子中那样，B 和 C 都抽到同一个退避值，它们就会发生碰撞。
Okay, so if, for example, C too drew two as an integer, then they will not be [synchronized / desynchronized, unclear] from each other, okay?
好，所以，如果，例如，C 也抽到了二这个整数，那么它们彼此就不会[同步／错开，待听辨]，好吗？
Because they will both decrease the [the, unclear] backoff counter during the first time slot, and then again during the second time slot.
因为它们都会在第一个时隙内递减这个[英文这里是否重复 the，待听辨]退避计数器，然后在第二个时隙内再递减一次。
But under the assumption that they now both drew two as an integer, they will decrease the backoff counter to zero exactly at the same time.
但是，在假设它们现在都抽到了二这个整数的情况下，它们会在完全相同的时刻把退避计数器减到零。
That means that they will access the channel exactly at the same time and collide.
这意味着，它们会在完全相同的时刻接入信道，并发生碰撞。

原标说话人 1  00:38:58
So backoff is a way to avoid collisions, but it does not avoid collisions with probability one.
所以，退避是一种避免碰撞的方法，但它并不是以概率一避免碰撞。
There is still a certain probability with which the nodes, the contending nodes, may collide, [right / okay, unclear]?
仍然存在一定的概率，使这些节点，这些竞争节点，可能发生碰撞，[对吧／好吗，待听辨]？
So it's a probabilistic collision-avoidance mechanism.
所以，它是一种概率性的碰撞避免机制。

原标说话人 1  00:39:28
Okay, this is our first observation.
好，这是我们的第一个观察。
Is it clear so far?
到目前为止清楚吗？
Okay, now if this is clear, let me make a second, [sorry, check this, because today is a bit different, unclear].
好，现在，如果这点清楚了，让我作第二个，[抱歉，检查一下这个，因为今天有点不同，待听辨]。
Okay, we have a second observation to make.
好，我们要作第二个观察。
We are close to the break, but let me start introducing it, and then we will finish after [the / a, unclear] short break.
我们快到休息时间了，但让我先开始介绍它，然后我们会在短暂休息之后把它讲完，[英文冠词是 the 还是 a，待听辨]。

原标说话人 1  00:40:13
So the second observation that I want to make is about the benefit of increasing the contention window parameter every time we need to perform a backoff procedure for a given data packet, okay?
所以，我想作的第二个观察，是关于每次需要为一个给定数据包执行退避过程时，增大竞争窗口参数的好处，好吗？
So let's consider still the same example as before.
所以，让我们仍然考虑和之前相同的例子。
So we still have the access point, A, B and C.
所以，我们仍然有接入点、A、B 和 C。
A talk with the access point, then B and C get the packet, both of them, while the channel is busy.
A 与接入点交谈，然后 B 和 C 拿到数据包，它们两个都是在信道忙的时候拿到的。
So they need to apply the backoff, and they need to draw [unclear words], after having sensed the channel as idle for DIFS, an integer out of, as we know, out of this range of values, because this is the first time that they run the backoff for the packet.
所以，它们需要执行退避，而且它们需要抽取[此处词语不清楚]，在侦听到信道空闲一个 DIFS 的时间之后，抽取一个整数，从，我们知道，从这个取值范围中抽取，因为这是它们第一次为这个数据包执行退避。
So they both use zero, contention window minimum, as a possible range, as a range of possible integers to be selected.
所以，它们都使用零、最小竞争窗口，作为一个可能的范围，作为可供选择的整数的范围。
So how many values are [in / in in, unclear] this range?
那么，这个范围里有多少个值，[英文这里是否重复 in，待听辨]？
There are CW_min...
有 CW_min……

原标说话人 1  00:41:48
Plus one integers, right?
加一这么多个整数，对吧？
Because [unclear words], including the zero is plus one.
因为[此处词语不清楚]，包括零就是加一。
Okay, this is the number of integers in that range.
好，这就是那个范围里的整数个数。

原标说话人 1  00:41:59
Okay, so what we want to compute, since we said that backoff is a probabilistic collision-avoidance mechanism, is the probability that B and C collide.
好，所以，我们想计算的，既然我们说过退避是一种概率性的碰撞避免机制，就是 B 和 C 发生碰撞的概率。
Okay, that's the probability that we want to compute.
好，这就是我们想计算的概率。
Okay, now we know already that they will collide if they draw the same integer out of this range.
好，现在我们已经知道，如果它们从这个范围里抽到同一个整数，它们就会碰撞。
And remember that the way a node draws an integer out of this range is with uniform probability, right?
还要记住，一个节点从这个范围里抽取整数的方式，是采用均匀概率，对吧？
So same probability for every value to be selected by the node.
所以，每个值被节点选中的概率相同。
So if we consider the probability for a node to draw a generic integer n out of this range, this probability is given by one over CW_min plus one, right?
所以，如果我们考虑一个节点从这个范围中抽到任意一个整数 n 的概率，这个概率由一除以（CW_min 加一）给出，对吧？
Because this is the number of integers in the range.
因为这就是这个范围中的整数个数。
Since we draw each value with equal probability, uniform probability, it's easy to see that the probability that an integer, a generic integer, is drawn out of this range by a node is given by one over CW_min plus one.
由于我们以相等的概率，均匀的概率，抽取每个值，很容易看出，一个整数，一个任意的整数，被一个节点从这个范围里抽到的概率，由一除以（CW_min 加一）给出。
This is basic probability theory, okay?
这是基本的概率论，好吗？
So in this way you can see that they are selected exactly, each of them with the same probability.
所以，这样你就可以看到，它们被选择时，恰好，每一个都具有相同的概率。
[Okay, unclear], this probability is the same for all of them.
[好，待听辨]，这个概率对它们所有值都是一样的。
