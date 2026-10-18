# 20261008-0910 · 已完成目录及课件核验（私有备份）

[飞书完成版](https://lcn6dqn3m0yr.feishu.cn/docx/R8JJdjfT2oKLnVxpZTTcSJO6nth) · [双语正文及导航](bilingual-20261008-0910.md)

- 已写入6个原生H1、46个原生H2，全部46个原双语正文块及所有原有块保持不变
- 保留12张原图、录音及原资源链接；标题顺序和原块对象经过回读核验
- 12张图与对应讲解位置的语义核验通过，详见slide-alignment-audit.md和slide-source-manifest.json
- 保留原稿重复时间戳及讲师口头更正，不推算或编造时间
- 这仅确认本课完成，不代表其余课程全部完成；不修改其他课次或原双语目录

## 私有使用范围

原稿含个人敏感叙述，仅维持用户已指定的课程私有备份范围，不应公开发布或扩散至其他项目。本说明不复述敏感内容。

## 图片与完整ZIP

本GitHub目录不含12张PNG及PDF大文件。可读正文中的图片引用转换为飞书原图块链接，正文与图注不变。来源清单中image_path指完整ZIP内的路径，不表示GitHub中已包含图片。

完整ZIP另行通过附件交付：course-20261008-0910-completed.zip，16,487,993字节。
SHA256：ca66cc0b704c5b37cac51ff97292a28e73fd6d7dea3a2c2385ceaf3b7021ca7d

## 紧凑恢复证据

运行 python3 decode_restore.py 可恢复course-20261008-0910-evidence.zip。脚本在验证字节数和SHA256后写出，不会修改远端文档。

紧凑包包含前后块快照、正文、导航计划、逐段核验、图片清单与操作回执，不包含PNG、PDF或录音媒体。包内原始Markdown保留完整ZIP的图片路径；缺少媒体时这些图片不会内嵌显示。

verification.json为线上原块比较；包内audit/verification.json的Markdown哈希对应完整包原始版本，publish-manifest.json分别记录原始与GitHub图片链接版的哈希。核验不表示重新逐字听校全部录音。
