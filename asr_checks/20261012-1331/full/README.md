# 20261012-1331 全文原音重转写原始证据

本目录逐块保存对原录音真实运行的medium.en无提示ASR。先保存原始输出，再做校订。这里不包含录音、下载链接、模型或认证信息。

- 原音长5622.281333秒。核心分块每180秒，共32块；每侧加15秒上下文（首尾截断），相邻窗口重叠30秒
- 所有raw.json和raw.jsonl中的时间均相对于该块window_start_seconds，绝对时间须加run_metadata.absolute_offset_seconds；absolute.txt已经转换
- 重叠区原样保留，不自动删词、不自动将两块不一致结果拼成一句；后续核验必须复查边界
- language=en，无文本提示，无前块文本条件，无VAD；beam_size=5，temperature=0，word_timestamps=true。每块立即checkpoint并计算SHA256
- 模型输出不是最终逐字稿。术语、重说、口语、语法不完整、模型疑似重复等都需要核验；不能直接用机器输出覆盖双语文稿
- 本次接口无法直接听音，因此不得宣称已人工听辨。双模型一致也不排除共同误识别
- README和run-manifest表示完整计划；只以实际存在且哈希核验通过的chunk文件判断完成范围
