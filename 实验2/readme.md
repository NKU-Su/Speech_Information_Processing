# 实验二：古诗生成

## 实验内容

本实验基于 CharRNN 模型实现古诗自动生成，功能包括：
- 生成藏头诗
- 续写古诗

## 实验流程

### 1. 环境配置与 PyTorch 基础

- 创建 conda 虚拟环境并安装 PyTorch、numpy、pandas、matplotlib、tqdm、opencc-python-reimplemented
- 完成 PyTorch 基础练习：张量操作、自动求导（Autograd）、nn.Module 神经网络模块、训练循环（损失函数、优化器、前向传播+反向传播）

### 2. 数据预处理

- **数据来源**：全唐诗 JSON 数据集（来自 chinese-poetry/chinese-poetry）
- **数据清洗**：
  - 去除括号内的内容（）、{}、【】、《》
  - 去除数字和连字符
  - 合并重复句号
  - 繁体中文转简体中文
- **构建词典**：建立 word2ix（字符到索引）和 ix2word（索引到字符）的映射，添加特殊符号 `<START>`、`<EOP>`、`<UNK>`、`</s>`
- **序列填充**：将所有诗歌填充至统一长度 125，不足部分用 `</s>` 填充
- **输出文件**：`tang.npz`（包含 data、word2ix、ix2word）

### 3. 构建模型并训练

- **底层实现多层 LSTM**：
  - `LSTMCell`：实现 LSTM 门的计算（输入门、遗忘门、候选值、输出门）
  - `MultiLayerLSTM`：堆叠多层 LSTMCell，支持任意层数
- **模型配置**：
  - embedding_dim: 256
  - hidden_dim: 256
  - layer_num: 2
  - batch_size: 128
  - learning_rate: 1e-3
  - epochs: 50
- **训练结果**：
  - 训练集损失从 2.93 降至 1.60
  - 验证集损失稳定在 2.1 左右
  - 每 10 个 epoch 保存一次模型
- **输出文件**：
  - `checkpoints/tang_model.pth`（最终模型）
  - `checkpoints/model_epoch{10,20,30,40,50}.pth`（中间检查点）

### 4. 生成诗歌

- **藏头诗生成**：给定藏头字（如"深度学习"），生成四句七言诗
- **续写古诗**：给定开头诗句，续写完整古诗
- **控制词**：通过 prefix_words 控制生成诗歌的意境

### 5. 大语言模型对比

- 调用 Hugging Face Router API 使用 Qwen2.5-7B-Instruct 模型
- 使用相同输入（"深度学习"藏头诗、"大漠孤烟照高阁"续写）生成诗歌
- 与自建模型结果进行对比

## 文件说明

| 文件 | 说明 |
|------|------|
| `lab2.ipynb` | 实验完整代码 |
| `readme.md` | 本文档 |
| `tang.npz` | 预处理后的唐诗数据 |
| `test.py` | 测试脚本 |
| `checkpoints/` | 模型检查点目录 |
| `data/` | 原始唐诗 JSON 数据 |

## 生成示例

### 自建 LSTM 模型

**藏头诗（深度学习）**：
> 深巷花如少，东篱花渐繁。
> 度林多少酒，疎嬾不相亲。
> 学劒来相问，高歌不厌贫。
> 习池多种竹，幽僻有邻园。

**续写（"大漠孤烟照高阁"）**：
> 大漠孤烟照高阁，南楼一望胡笳绝。
> 秦川络水连山陂，越客相逢心已矣。
> ...

### Qwen2.5-7B-Instruct 模型

**藏头诗（深度学习）**：
> 深山藏古寺，度牒需修行。
> 学艺无止境，习字炼精神。

**续写（"大漠孤烟照高阁"）**：
> 大漠孤烟照高阁，长河落日共秋波。
> 天涯游子归何处，烟柳画桥锁清...

## 依赖环境

- Python 3.9
- PyTorch 2.8.0+
- numpy
- pandas
- matplotlib
- tqdm
- opencc-python-reimplemented
- requests（用于调用 Hugging Face API）