import numpy as np
import matplotlib.pyplot as plt
from mmseg.apis import init_model, inference_model, show_result_pyplot
import mmcv
import cv2
from mmengine import Config
from mmengine.runner import Runner
from mmseg.utils import register_all_modules


cfg = Config.fromfile('./demo/Glomeruli/new_cfg.py')
# register all modules in mmseg into the registries
# do not init the default scope here because it will be init in the runner
register_all_modules(init_default_scope=False)
runner = Runner.from_cfg(cfg)
checkpoint_path = './work_dirs/tutorial/iter_1000.pth'
model = init_model(cfg, checkpoint_path, 'cuda:0')
img = mmcv.imread('./data/Glomeruli-dataset/images/VUHSK_1702_39.png')
result = inference_model(model, img)
print("result.keys()",result.keys())
pred_mask = result.pred_sem_seg.data[0].cpu().numpy()
print("pred_mask.shape",pred_mask.shape)
print("np.unique(pred_mask)",np.unique(pred_mask))
plt.imshow(pred_mask)
plt.show()
# 可视化预测结果
visualization = show_result_pyplot(model, img, result, opacity=0.7, out_file='pred.jpg')
plt.imshow(mmcv.bgr2rgb(visualization))
plt.show()
# 语义分割预测结果-连通域分析
plt.imshow(np.uint8(pred_mask))
plt.show()
connected = cv2.connectedComponentsWithStats(np.uint8(pred_mask), connectivity=4)
# 连通域个数（第一个有可能是全图，可以忽略）
print("connected[0]",connected[0])