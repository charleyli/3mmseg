import numpy as np
from PIL import Image

label_path = r"C:\data\potsdam\5_Labels_all_noBoundary\top_potsdam_2_10_label_noBoundary.tif"
label = np.array(Image.open(label_path), dtype=np.uint8)

# 提取所有独特 RGB 颜色
unique_colors = np.unique(label.reshape(-1, 3), axis=0)

print("标注图里的颜色值：")
for idx, color in enumerate(unique_colors):
    print(f"类别 {idx}: {color.tolist()}")


# 结果为：
# 标注图里的颜色值：
# 类别 0: [0, 0, 0]
# 类别 1: [0, 0, 255]
# 类别 2: [0, 255, 0]
# 类别 3: [0, 255, 255]
# 类别 4: [255, 0, 0]
# 类别 5: [255, 255, 0]
# 类别 6: [255, 255, 255]