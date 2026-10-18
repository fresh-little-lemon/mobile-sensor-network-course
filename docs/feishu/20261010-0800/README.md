# 20261010-0800 双语课程导航与课件核验备份

文档：https://lcn6dqn3m0yr.feishu.cn/docx/FfgDdqktToKXpyxwlCxcv7GanSb

状态：原导航核验完成，已补入确认来源的图34，2026-10-18 14:43 UTC最终回读。

- 原有81个H2与7个H1全部保留，格式、时间戳与段落语义正确，没有重复新增导航
- 81段原双语正文、录音、资源及12张原图完整保留
- 补图34《The Four Interframe Spaces》，来自固定02-WiFi_1-7.pdf第17页下半页，置于第58段标题后、正文前，对应同一对话中的DATA/ACK与SIFS讲解
- 唯一原块修改为文首状态行：更新13图及原导航核验状态

12张原图全部视觉匹配固定PDF，原顺序与位置符合讲解，未按图号重排。图29持久策略和图35的EIFS/指数退避细节未展开，不机械补入。

## 尚未找到原图来源的课堂示意

排队模型、功率随时间变化图、A/B优先级示例的原始图源未在固定PDF中找到，保留正文，不以无关课件图或重绘图冒充。不能据此宣称所有课堂示意图均已恢复。

verification.json记录逐段前后hash、原块完整比较、原导航保留及新增图定位；slide-source-manifest.json、slide-alignment-audit.md及audit/verification.json提供来源与独立核验记录。新增图为忠实PDF渲染裁图，未重绘。

本次核验确认编辑没有改变原稿，不等于重新逐字听校录音。音频二进制未包含，正文保留原播放链接。原始智能纪要与文字转写未修改。同步文件仅为私有课程仓库准备，本任务未推送或公开发布。本包不含凭据；SHA256SUMS.txt覆盖其他文件。


## GitHub私有备份与恢复方式

本目录只归档本课的已完成导航和已确认来源图，不表示全部课堂图像已经恢复。all_lecture_visuals_recovered=false。排队模型、功率随时间变化图及A/B优先级示例的原始图源缺口仍然存在，详见上文及来源清单。

[阅读双语正文及导航](bilingual-20261010-0800.md)。GitHub版本仅将13个本地图片引用换为飞书原图块链接，正文、图注及来源缺口说明保持不变。这里不包含PNG/PDF，来源清单image_path指完整ZIP内路径。

完整ZIP另行通过附件交付：course-20261010-0800-completed.zip，3,242,181字节。
SHA256：3c59baffa5eb39878e435a3869bcfa9e9c139dca2da3c00d1b19d3e36746cddd

运行 python3 decode_restore.py 恢复course-20261010-0800-evidence.zip；脚本先核验大小和SHA256，不修改飞书。紧凑包包含前后快照、正文、导航计划、状态修改、核验、图源及回执，不含PNG、PDF或录音。原始Markdown在紧凑包中保留完整包的图片路径。

上文SHA256SUMS.txt说明指ZIP内部文件；紧凑包另有自身逐文件哈希。audit/verification.json中的Markdown哈希对应完整包原版，publish-manifest.json分别记录原版与GitHub图片链接版哈希。

仅供用户指定课程私有仓库使用，不覆盖其他课次；本课导航完成不表示全课程完成。
