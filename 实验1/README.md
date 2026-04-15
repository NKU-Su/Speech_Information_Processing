# 语音技术与应用 - 实验一

## 实验概述

本实验涵盖了音频信号处理的基础知识，包括传统特征提取方法（FBank、MFCC）以及基于预训练模型的深度特征提取。

---

## 完成内容

### 课程一：环境配置与音频基础（15%）

- [x] 配置 anaconda 虚拟环境 `speech_env` (Python 3.8)
- [x] 安装依赖包：numpy, matplotlib, librosa, pandas, scipy, torch, torchaudio
- [x] 使用 `librosa` 加载音频文件 `LJ001-0011.wav`，打印音频形状和采样率
- [x] 使用 `matplotlib` 绘制原始音频波形图
- [x] 使用 `librosa` 计算幅度谱图（STFT）并绘制
- [x] 使用 `librosa` 计算并绘制 Mel 频谱图
- [x] 使用 `torchaudio` 加载音频，计算 Mel 频谱图并绘制

### 课程二：手动实现幅度谱（30%）

- [x] 实现**预加重函数** `pre_emphasis(sig, alpha=0.97)`
  - 高通滤波器，提升高频部分，平衡频谱
- [x] 实现**分帧函数** `framing(sig, fs, frame_len_s=0.025, frame_shift_s=0.01)`
  - 帧长 25ms，帧移 10ms
  - 对信号末尾进行填充确保帧采样数相等
- [x] 实现**加窗函数** `add_window(frame_sig, fs, frame_len_s=0.025)`
  - 使用 Hamming 窗减少频谱泄漏
- [x] 实现**短时傅里叶变换函数** `stft(frame_sig, nfft=512)`
  - 使用 `np.fft.rfft()` 计算幅度谱
- [x] 取对数绘制可查看的幅度谱图

### 课程三：实现 FBank 和 MFCC（45%）

- [x] 实现 **Mel 滤波器函数** `mel_filter(frame_pow, fs, n_filter=40, nfft=512)`
  - 根据 Mel 频率刻度设计滤波器组
  - 符合人耳对低频敏感、高频分辨率低的特性
- [x] 取对数绘制 Mel 频谱图（Fbank）
- [x] 实现**离散余弦变换函数** `discrete_cosine_transform(filter_banks)`
  - 将 Fbank 经过 DCT 得到 MFCC
  - 提取 12 维 MFCC 特征
- [x] 绘制 MFCC 特征图

### 课程四：深度音频特征提取 - 加分项（10%）

- [x] 使用 `torchaudio` 加载预训练 **Wav2Vec2_BASE** 模型
- [x] 对音频进行重采样以符合模型采样率要求（16kHz）
- [x] 提取深度特征并绘制特征图

---

## 文件结构

```
.
├── LJ001-0011.wav              # 示例音频文件
├── exp1_2026.ipynb             # Jupyter Notebook 实验代码
├── exp1_2026.pdf               # 实验指导文档
├── librosa-0.10.0-py3-none-any.whl  # librosa 离线安装包
└── README.md                   # 本文档
```

---

## 关键函数汇总

| 函数 | 功能 |
|------|------|
| `pre_emphasis()` | 预加重处理 |
| `framing()` | 分帧 |
| `add_window()` | 加 Hamming 窗 |
| `stft()` | 短时傅里叶变换 |
| `mel_filter()` | Mel 滤波器组 |
| `discrete_cosine_transform()` | 离散余弦变换（DCT） |

---

## 依赖环境

- Python 3.8
- anaconda / miniconda
- numpy, matplotlib, pandas, scipy
- librosa
- torch, torchaudio
- IPython

---

## 参考资料

- [Conda 环境配置指南](https://blog.csdn.net/ming12131342/article/details/140233867)
- [换源指南 - 北外源](https://blog.csdn.net/weixin_43667077/article/details/108282523)
- [PyTorch 官网](https://pytorch.org/)
- [torchaudio Wav2Vec2 文档](https://docs.pytorch.org/audio/stable/generated/torchaudio.models.Wav2Vec2Model.html)
