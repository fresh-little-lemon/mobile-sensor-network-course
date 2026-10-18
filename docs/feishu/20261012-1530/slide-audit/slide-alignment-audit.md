# 20261012-1530 逐图只读审计

## 结论

44段全文与9张原图逐一核验。9图均保持原位置；没有确认需移动的图或可从固定PDF补回的缺图。2项课堂示意原图未在固定PDF找到，不能宣称全部授课视觉材料已恢复。无远端改动。

## 逐图证据

### 图53：EIFS: Extended Interframe Space
- 原图块：doxcnhqJgZ7aHCx5mJHgikj1sug
- 位置：第1段（00:00:02）后、第2段前
- 固定PDF：第27页上半页
- 结论：保留。第1段00:00:02明确引入EIFS，解释物理忙但无法设置NAV、出错；第2段继续解释双重侦听不一致。图紧跟第1段，定义与后文保护ACK解释一致。
- 原图：../slide-images/slide-053.png

### 图54：EIFS in Action
- 原图块：doxcnuGpgWY0ADM2kFSK7nLrIYf
- 位置：第5段（00:04:48）后、第6段前
- 固定PDF：第27页下半页
- 结论：保留。第2–5段依次建立B向C发DATA、C等待SIFS发ACK、A在C覆盖范围外并错误解调B；第4段明确指向右上拓扑图，图中A/B/C位置、三条时间线及received in error均吻合。图在第5段后，后接第6–11段NAV失败、EIFS与ACK碰撞反例，保留。
- 原图：../slide-images/slide-054.png

### 图35：DCF Basic Rules
- 原图块：doxcnTM9GdmtKTFz200FEd61KqW
- 位置：第11段（00:11:24）后、第12段前
- 固定PDF：第18页上半页
- 结论：保留。第10段反事实推演没有EIFS时A等待DIFS可能干扰C的ACK，第11段回到真实规则：出错、不理解信道时空闲后继续等待。图35第一条明确错误后等EIFS；放11段后是规则回引，不应按PDF编号移到课首。图上的忙后退避为已学背景，未将其误判为当前新讲内容。
- 原图：../slide-images/slide-035.png

### 图55：EIFS: the Recovery Rule
- 原图块：doxcnLs8llbcvuFDfQCri2oEeFg
- 位置：第12段（00:12:10）后、第13段前
- 固定PDF：第28页上半页
- 结论：保留。第12段00:12:10说EIFS中正确读到首部及Duration即可立即恢复正常，第13段再次总结恢复正常。图55第二点和蓝色提前结束规则逐项吻合。
- 原图：../slide-images/slide-055.png

### 图58：PCF Superframe Structure
- 原图块：doxcnwAs8Tdssehx6xC8qTzTXfg
- 位置：第20段（00:16:48）后、第21段前
- 固定PDF：第29页下半页
- 结论：保留。第20段定义连续beacon之间的superframe；紧随其后的21–23段解释CFP先、CP/DCF后并反复循环。图58的B/CFP/CP、重复区间与文字一致，原位置恰好在定义后。
- 原图：../slide-images/slide-058.png

### 图59：PCF and DCF Coexistence
- 原图块：doxcnfVboKtDFO8u1f1SlyBSBXg
- 位置：第23段（00:19:08）后、第24段前
- 固定PDF：第30页上半页
- 结论：保留。第23段明确PCF和DCF在同一superframe内时分共存，图59第一点准确对应；后续26–32段展开poll、数据/ACK捎带和CF-End。位于23段后是本节机制概览，应保留。
- 原图：../slide-images/slide-059.png

### 图57：PCF: Basic Characteristics
- 原图块：doxcnEUX76MKvIcPH4ZN8vU1Lyf
- 位置：第24段（00:19:46）后、第25段前
- 固定PDF：第29页上半页
- 结论：保留。第24段00:19:46明确AP持有节点列表、在association时声明愿否参加PCF；第25段举A/C/D参加而B/E不参加。图57最后一条就是Association Request与static polling list，原图紧跟24段恰当；不能仅凭57小于58/59就提前。
- 原图：../slide-images/slide-057.png

### 图34：The Four Interframe Spaces
- 原图块：doxcnLAi3eX5pfpllViehJuLu1g
- 位置：第37段（00:35:39）后、第38段前
- 固定PDF：第17页下半页
- 结论：保留。第37段00:35:39明确SIFS<PIFS<DIFS、AP以PIFS获取发送beacon优先权；第38段继续说明PIFS目的。图34的PIFS定义及优先级排序与相邻内容直接对应。
- 原图：../slide-images/slide-034.png

### 图60：Why PCF Never Really Happened
- 原图块：doxcnUA0UtNOFZB3YwkrgnVtUge
- 位置：第42段（00:41:36）后、第43段前
- 固定PDF：第30页下半页
- 结论：保留。第41–42段讲poll/null浪费与静态列表缺少实时队列信息；第43段讲beacon延迟不可预测；44段预告第三个问题。图60相应列出static polling list、unpredictable beacon delay及unknown transmission duration，放42段后连接已讲第一项与将讲第二项。第三条属于已展示的预告，不能据此声称本课已展开第三问题。
- 原图：../slide-images/slide-060.png

## 原课件未找到的课堂图

### A/C/D参与列表和PCF逐站轮询、fast ACK、NULL、CF-End课堂时序图
第24段明确说“let me draw here an example”；25段列A/C/D参加而B/E不参加；26–32段在该示意中逐步画beacon、poll A、A DATA、poll C+DATA、fast ACK、poll D、NULL、CF-End；41段回指poll/null交换。
固定74页PDF全文检索poll/null/TBTT/contention-free，视觉检查第16、17、18、27–33、40–43页。图57/59是文字机制，图58只有宏观CFP/CP；第41页802.11e图为后续HCCA/QSTA/CAP，不是此A/C/D PCF例子。
保留相关图57/58/59与全部正文；不使用后续802.11e图冒充，不凭文字重绘。

### DCF DATA/ACK跨越TBTT并延迟beacon的具体课堂时间线
第34–37段指节点在beacon之前DIFS后占信道、完成DATA/ACK，再PIFS后发beacon；43段指图中移动的superframe起点。图58仅显示规则superframe，没有跨TBTT的DATA/ACK延迟细节。
同一固定PDF搜索beacon/TBTT/delay并检查第29–31、41–43页；图60有文字解释，未找到与课堂描述相同的详细时序图。
保留图58/60，记录源图未找到；不认定缺了一张能从该PDF恢复的幻灯片。

## 不机械补图

- 图56：第14–17段仅安排次日练习并说结束基础DCF，没有逐项总结DATA/ACK、NAV、RTS/CTS、collision/backoff，也没有明确指向该summary页；不能单凭53–55后缺56补入。
- 图61：本课末尾仍在PCF局限并预告休息后第三问题，没有进入完整DCF/PCF总结；不能按页码续接。
- 图33：第38段提到IFS优先级阶梯，但紧邻原图34已有完整SIFS<PIFS<DIFS<EIFS及定义；无明确重新展示图33的证据，不重复插图。

## 发布建议

可独立发布该审计检查点。将课件审计pending标为false，保留2项源图缺口和未做音频校订的说明。无需远端图文变更。

固定来源：https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf
PDF SHA256：15011ccc6e929fd6f0b9fb7837ee450734a12058891fa028e6e1bf658c4902e8
原音、原始文字记录、智能纪要均未改动，也未打包音频。
