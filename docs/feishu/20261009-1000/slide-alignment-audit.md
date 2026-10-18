# 20261009-1000 课件图片审计

## 结论

- 已完整阅读97对双语正文，18张原PNG逐张与固定PDF视觉核验一致；未发现原图错位，无须移动
- 确认并补齐图6：第2段明确回到标准演进表，第2–8段解释最大PHY速率与吞吐量，第63、82、91段继续回引该表；主任务已放在第2段标题后、正文前
- 补图6复用0845双语稿原PNG，远端重新下载后的SHA256与源PNG完全相同
- 全量回读核验通过：97个H2、10个H1、19张图；除文首状态计数外，所有原非根块逐块不变，18张原图顺序和相邻正文不变

## 未解决的原图来源缺口

- OFDM子载波sinc图：第81–90段明确谈到补充幻灯片和一张图，尤其第83–88段反复指向窄子信道、频谱峰值、sinc和并行信号。当前固定74页PDF未找到对应基础图
- MIMO四天线/半波长间距示意图：第91–97段描述两端各四天线及并行比特串，当前固定PDF未找到对应原图；也可能是课堂补充或板书，无法仅凭转写确认
- 已搜索固定PDF全文并视觉复核后部候选第44、50、56、57、67页。Wi-Fi6的OFDMA/RU和后续MU-MIMO/beamforming页并不是上述原图，未用它们替代
- 两处正文均完整保留。本包可用于当前已核实内容，不能声称全部课堂配图已补齐

## 不按页码机械补图或重排

- 图13先于图12：第15段先定义ESS，第16–18段再转入ad hoc，符合课堂顺序
- 图14在第58段后：本节此时才讲关联过程中的校园漫游和AP间通知，位置合理
- 未补图17：第52段明确不解释Wi-Fi认证机制，50–54段只讲认证层次和应用层登录；PDF图17主体为Open System/WEP/WPA2/WPA3/802.1X，未展开且有口述差异，不能只因编号缺17而补
- 未补图26起的MAC章节：本节在转入MAC前改讲补充OFDM/MIMO，没有展开DCF/PCF

## 保留与差异说明

- 97段逐字保留，中英文、说话人、时间戳、重复时间戳、段内换行不变；47–49段课间对话和27段Bye也完整保留
- 第75段口述室外160m与图23的460m不一致，未改正文或图片；认证简化说法、OFDM正交性解释、MIMO天线描述及97段mono均按原稿保留
- 原图7底部文字裁切与部分图标题区重叠已存在于源PDF，图片保持原字节，没有重绘或伪造修复
- 原始文字记录、智能纪要、录音未修改；仅保留来源链接，不打包音频二进制

## 图片对应表

|图号|固定PDF位置|正文位置|内容|结论|
|---:|---|---|---|---|
|6|第3页下半页|第1/2段间，第2段H2之后新增|Standards Evolution: the Throughput Line|匹配第2–8,63–64,82,91–95段|
|7|第4页上半页|第9/10段间，原位置|Other Notable Amendments (Not About Raw Speed)|匹配第9段|
|8|第4页下半页|第9/10段间，原位置|From Amendment Names to “Wi-Fi Generations”|匹配第9–10段|
|9|第5页上半页|第10/11段间，原位置|The Full Picture: 27 Years of Amendments|匹配第9–10段|
|10|第5页下半页|第11/12段间，原位置|Basic Architectural Concepts|匹配第10–11,16–18段|
|11|第6页上半页|第13/14段间，原位置|WLAN with Infrastructure (BSS)|匹配第11–14段|
|13|第7页上半页|第15/16段间，原位置|Extended Service Set (ESS)|匹配第12–15段|
|12|第6页下半页|第16/17段间，原位置|Ad Hoc WLAN (Independent BSS, IBSS)|匹配第16–18段|
|15|第8页上半页|第19/20段间，原位置|Joining a BSS: Three Steps|匹配第19–21,50–61段|
|16|第8页下半页|第29/30段间，原位置|Scanning: Passive vs. Active|匹配第21–32段|
|14|第7页下半页|第58/59段间，原位置|Mobility Within an ESS|匹配第58–60段|
|18|第9页下半页|第61/62段间，原位置|Association (Step 3)|匹配第54–64段|
|19|第10页上半页|第66/67段间，原位置|Physical-Layer Fundamentals (Wi-Fi 1–3)|匹配第65–66段|
|20|第10页下半页|第67/68段间，原位置|Frequency Band and Channels (2.4 GHz)|匹配第67–69段|
|21|第11页上半页|第68/69段间，原位置|Non-Overlapping Channels in the 2.4 GHz Band|匹配第67–69段|
|22|第11页下半页|第71/72段间，原位置|The Case for Multi-Rate Transmission|匹配第70–72段|
|23|第12页上半页|第73/74段间，原位置|Range vs. Data Rate (802.11b Example)|匹配第72–75段|
|24|第12页下半页|第75/76段间，原位置|Rate Adaptation|匹配第63–64,75–77段|
|25|第13页上半页|第78/79段间，原位置|Final Remark: Wi-Fi Radios Are Half-Duplex|匹配第78–80段|

## 核验资料

- [飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/JT5ydOxALoxXVSxQTN0cM40enid)
- [固定版本源PDF](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf)
- slide-source-manifest.json：逐图来源、哈希、页/半页、原图块ID、图注、相邻段落、语义理由与两项未解决来源缺口
- bilingual-20261009-1000.md：97对原文、97个分段标题、10个主题标题、19张图和缺图说明
- audit/verification.json：正文逐字、顺序、原块一致、原图位置、标题及新增图远端字节核验
- audit/missing-slide-006.json：补图依据及原PNG来源
- audit/wifi-*.png：原图视觉比对及不补图边界检查的PDF渲染

当前已执行变更已核验。两项课堂原图来源缺口仍未解决。
