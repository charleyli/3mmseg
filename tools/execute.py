import os
import numpy as np
import cv2
from mmseg.apis import init_model, inference_model, show_result_pyplot
import mmcv
import matplotlib.pyplot as plt


# 创建 checkpoint 文件夹，用于存放预训练模型权重文件
# 创建 outputs 文件夹，用于存放预测结果
# 创建 data 文件夹，用于存放图片和视频素材
# 创建 图表 文件夹，用于存放生成的图表
# 创建 Zihao-Configs 文件夹，用于存放自己的语义分割模型的 config 配置文件
folders = ['checkpoint', 'outputs', 'data', '图表', 'Zihao-Configs']
for folder in folders:
    os.makedirs(folder, exist_ok=True)  # 如果已存在就不报错






# 模型 config 配置文件
config_file = 'configs/segformer/segformer_mit-b5_8xb1-160k_cityscapes-1024x1024.py'

# 模型 checkpoint 权重文件
checkpoint_file = 'https://download.openmmlab.com/mmsegmentation/v0.5/segformer/segformer_mit-b5_8x1_1024x1024_160k_cityscapes/segformer_mit-b5_8x1_1024x1024_160k_cityscapes_20211206_072934-87a052ec.pth'

img_path = 'data/street_uk.jpeg'

# img_bgr = cv2.imread(img_path)

# print("img_bgr.shape",img_bgr.shape)
# plt.imshow(img_bgr[:,:,::-1])
# plt.show()

# result = inference_model(model, img_bgr)
