# DeepLabV3+
# Continual Learning for Abdominal Multi-Organ and Tumor Segmentation
# SUnet: A multi-organ segmentation network based on multiple attention

## step 1
运行一个DeepLabV3+的完整案例，涉及到数据库的处理，模型的搭建、模型的调试、结果的分析

1 文件下载
https://blog.csdn.net/qq_44961869/article/details/123760704
https://pan.baidu.com/s/1SgoM8-_JIMJbXyQ9i7eDtw(密码是lala)


2 数据处理
https://mmsegmentation.readthedocs.io/zh-cn/0.x/dataset_prepare.html
最后的数据集的结构如下：
mmsegmentation
├── mmseg
├── tools
├── configs
├── data
│   ├── potsdam
│   │   ├── img_dir
│   │   │   ├── train
│   │   │   ├── val
│   │   ├── ann_dir
│   │   │   ├── train
│   │   │   ├── val
ISPRS Potsdam
Potsdam 数据集是一个有着2D 语义分割内容标注的城市遥感数据集。需要其中的 ‘2_Ortho_RGB.zip’ 和 ‘5_Labels_all_noBoundary.zip’。
对于 Potsdam 数据集，请运行以下命令下载并重新组织数据集 使用我们默认的配置， 将生成 3456 张图片的训练集和 2016 张图片的验证集。
 使用这个命令：python tools/dataset_converters/potsdam.py  /data/potsdam
 数据在C:\data\potsdam文件夹下。



## step 2
运行一个DeepLabV3+与Continual Learning的完整案例
