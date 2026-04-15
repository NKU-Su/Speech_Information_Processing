import torch
import torchvision

print(f"Torch Version: {torch.__version__}") # 应输出 2.8.0
print(f"TorchVision Version: {torchvision.__version__}") # 应输出 0.23.0

# 检查 CUDA 是否可用
print(f"CUDA Available: {torch.cuda.is_available()}") 

# 检查 CUDA 版本（PyTorch 编译时链接的版本）
print(f"CUDA Version: {torch.version.cuda}") 

# 检查 cuDNN 版本
print(f"cuDNN Version: {torch.backends.cudnn.version()}") 