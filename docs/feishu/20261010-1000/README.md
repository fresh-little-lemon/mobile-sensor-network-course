# 20261010-1000 · 已完成的目录与课件图更新

[打开飞书完整文档](https://lcn6dqn3m0yr.feishu.cn/docx/LN0Xdi9daou8cFxTeT8cSCsbnnh) · [阅读完成版双语正文与目录](completed-navigation.md)

## 已完成并核验

- 9个原生H1主题标题、76个原生H2分段标题，顺序01–76且无重复
- 9张课件图：原有5张完整保留，新增4张，3张原有图已调整位置
- 76/76个原双语正文块的ID、文本和格式保持不变；英文与中文分行
- 原录音块、原始文字链接和课件链接保留
- 保留原文［数字不清楚］及课堂更正；本次核验不表示重新听校全部录音

该目录只新增完成版备份，不覆盖仓库原有双语文件。Markdown由完成后飞书实际块快照生成，图片以原始图注及飞书图块链接标识，并非已在GitHub内嵌渲染。飞书资源仍需原有访问权限。

## 文件

- completed-navigation.md：按实际块顺序导出的可读完成版
- navigation-headings.json、navigation-plan.json：标题和定位方案；其中的建议状态以实际完成版和核验记录为准
- final-verification.json、order-and-hashes.json：完成计数、顺序、76段逐段SHA256核验
- completion.md：完成记录
- backup.zip.base64.part1.txt、backup.zip.base64.part2.txt：完整ZIP的两段Base64文本备份
- decode_restore.py：合并、解码并验证后恢复ZIP

## 恢复完整ZIP（含4张新增PNG）

在本目录运行：

    python3 decode_restore.py

输出：course-1000-completed-navigation-ppt.zip（618548字节）。
SHA256：3198e7171180a863469a29af93fe1f7fcd25cdb1b5812cfa054682fea6097758

ZIP包含4张新增课件PNG、前后块快照、完成版方案及逐段哈希和操作结果；并不包含全部9张图或原录音媒体。原有5张图和录音仍在飞书原文档中。
