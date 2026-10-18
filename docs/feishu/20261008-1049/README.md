# 20261008-1049 · 已完成目录及课件核验

[飞书完成版](https://lcn6dqn3m0yr.feishu.cn/docx/ENxEdQVrvoRZ6lxgUeAcu5yBnng) · [双语正文及导航](bilingual-20261008-1049.md)

- 已写入9个原生H1、88个原生H2，全部88个双语正文及所有原有块保持不变
- 原有25张课件图、录音及资源链接保留，图片与讲解语义核验通过
- 首个时间戳00:01:10及原稿重复时间戳均保留，不推算、不改写
- 未修改原始智能纪要和文字转写文档
- 本目录仅确认本课完成，不代表其他课程均完成，不覆盖其他课程或原双语目录

## 图片核验

图的排列按讲解语义，非仅按页码：图45在图48之后，对应第76段接收端复算与比较校验位的总结，保留原位置。图51详细对比未在本段展开，不因编号跳过就补图。逐图证据见slide-alignment-audit.md及slide-source-manifest.json。

## 图片与完整ZIP

本GitHub目录不含25张PNG及PDF大文件。可读正文仅将本地图片引用转换为飞书原图块链接，正文与图注不变。来源清单中的image_path指完整ZIP内路径，不表示GitHub内包含PNG。

完整ZIP另行通过附件交付：course-20261008-1049-completed.zip，7,547,678字节。
SHA256：92d7ec5315711199a3892d68e5ca6ca0e90cc1d17b5ce6be4f57147fb4706ee4

## 紧凑恢复证据

运行 python3 decode_restore.py 可恢复course-20261008-1049-evidence.zip。脚本先验证字节数和SHA256后写出，不会修改飞书。

紧凑ZIP包含前后块快照、正文、导航计划、逐段核验、图片清单和操作回执，不包含PNG、PDF或录音媒体。包内原始Markdown保留完整ZIP的图片路径；无媒体时不内嵌显示这些图片。

verification.json记录原块完整对象比较及逐段哈希。audit/verification.json的Markdown哈希对应完整包原始版本，publish-manifest.json分别记录原始与GitHub图片链接版哈希。核验不等于重新逐字听校音频。

仅用于用户指定的课程私有仓库。
