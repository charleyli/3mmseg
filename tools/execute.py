import os
import torch
import numpy as np
import matplotlib.pyplot as plt
import mmcv
from mmseg.apis import init_model, inference_model, show_result_pyplot
from mmseg.utils import register_all_modules
from PIL import Image
from mmseg.apis import init_model
from mmseg.apis import inference_model
from mmengine.model.utils import revert_sync_batchnorm
from mmseg.apis import show_result_pyplot


print("cwd:", os.getcwd())
config_file = './configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024.py'
checkpoint_file = 'https://download.openmmlab.com/mmsegmentation/v0.5/pspnet/pspnet_r50-d8_512x1024_40k_cityscapes/pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth'
register_all_modules()
model = init_model(config_file, checkpoint_file, device='cuda:0')
if not torch.cuda.is_available():
    model = revert_sync_batchnorm(model)

img_path = './demo/demo.png'
img_pil = Image.open(img_path)
print("img_pil.size",img_pil.size)
result = inference_model(model, img_path)
print("result",result)
keys = result.keys()
print(keys)
print("pred_sem_seg.shape:", result.pred_sem_seg.data.shape)
print("np.unique(result.pred_sem_seg.data.cpu())",np.unique(result.pred_sem_seg.data.cpu()))

print("seg_logits.shape:", result.seg_logits.data.shape)
class_map = result.pred_sem_seg.data[0].detach().cpu().numpy()
plt.imshow(class_map)
plt.show()
visualization = show_result_pyplot(model, img_path, result, opacity=0.8, title='MMSeg', out_file='./outputs/B2.jpg')
print(visualization.shape)
visualization.shape
plt.imshow(mmcv.bgr2rgb(visualization))
plt.show()
Image.open('./outputs/B2.jpg')