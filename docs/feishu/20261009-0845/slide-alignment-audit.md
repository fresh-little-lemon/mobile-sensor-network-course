# 20261009-0845 课件图片审计

## 结论

- 已完整阅读88对双语正文，原图6下载成功并与固定版本PDF第3页下半页视觉核验一致；原位置紧接第69段，准确对应标准演进表，无须移动
- 确认缺少图5 Where 802.11 Sits in the Protocol Stack（PDF第3页上半页）：第5–22段持续讲收发端协议层、调制解调、ACK与停止等待，第26–46段进一步解释层次分工，第67–68段再明确Wi-Fi仅规定PHY和MAC
- 主任务已在飞书和本地Markdown第6段标题后、原文前加入图5；复用0759双语稿已核验的原PNG字节，不重绘、不修改图内内容
- 图7–9的其他修订、Wi-Fi世代命名及完整历史图未展开；图10–18的BSS/IBSS/ESS及接入过程未讲，不把一般路由器背景说明当作这些图已授课
- 第73–82段对三个信道和干扰隔离的解释是演进表旁的预告，明确说稍后会讲；未讲14信道、22 MHz宽度、5 MHz间隔或1/6/11标号，不因此提前补图19–21
- 已准备完整Markdown、2张原PNG、1份固定PDF及逐图来源/段落清单；审计执行方未远程修改或发布

## 完整性与边界

- 88个原正文块逐字保留，中英文、说话人、全部时间戳、重复时间戳与段内换行不变
- 8个主题标题和88个分段标题来自主任务heading-plan.json，独立于原正文
- 原图6的块ID、图注、顺序与相邻段落（第69/70段）保持不变；新增图5位于第5/6段之间、第6段标题之后
- Muy、Ours、Laughter、原文OFDM展开、天线传播、CRC位于首部等表述均保留；本次不做科学改写或音频重转写
- 原始文字记录和录音仅保留来源链接，不修改；不打包音频二进制

## 图片对应表

|图号|固定PDF位置|段落位置|内容|结论|
|---:|---|---|---|---|
|5|第3页上半页|第6段标题后、正文前（新增）|Where 802.11 Sits in the Protocol Stack|匹配第5–22、26–46、67–68段|
|6|第3页下半页|第69段后、第70段前（原位置）|Standards Evolution: the Throughput Line|匹配第69–87段|

## 核验资料

- [飞书双语稿](https://lcn6dqn3m0yr.feishu.cn/docx/PnXMd5tSLoFiWDxmYvDcS6BJnfe)
- [固定版本源PDF](https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf)
- slide-source-manifest.json：PDF版本/哈希、图号/页/半页、图片哈希、原图块ID与图注、相邻段落和语义对应
- bilingual-20261009-0845.md：88对原文、8个主题标题、88个分段标题和2张图
- slide-images/：原图6和补充图5原PNG
- audit/wifi-03.png、wifi-04.png、wifi-10.png、wifi-11.png：源PDF视觉核验与边界检查
- audit/missing-slide-005.json：补图依据、字节来源、哈希和插入位置
- audit/verification.json：逐字、顺序、原图位置与标题数量验证结果

最终远程快照已独立回读比对：88个二级标题、8个主题标题及2张图准确；除文首状态计数外，所有原非根块逐块不变。新增图5位置准确，远程重新下载的PNG与原PNG的SHA256完全相同。状态行仅保留新的2图与标题计数，旧1图尾片段已清除。
