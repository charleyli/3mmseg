# DeepLabV3+
# Continual Learning for Abdominal Multi-Organ and Tumor Segmentation
# SUnet: A multi-organ segmentation network based on multiple attention

## step 1
运行一个DeepLabV3+的完整案例，涉及到数据库的处理，模型的搭建、模型的调试、结果的分析


Pascal VOC 2012+Aug 数据集
https://github.com/open-mmlab/mmsegmentation/tree/main/configs/deeplabv3plus
http://host.robots.ox.ac.uk/pascal/VOC/voc2012/
https://github.com/zbf1991/CDL(里面：https://drive.google.com/file/d/1jhtdjj3xrEp60zO3B7jZ14yxxZkCJMeM/view)
https://www.kaggle.com/datasets/gopalbhattrai/pascal-voc-2012-dataset（也下载了数据）
数据集的处理
https://blog.csdn.net/qq_31347869/article/details/93742029/
https://blog.csdn.net/RossoCorsa/article/details/136466251
https://www.sun11.me/blog/2018/how-to-use-10582-trainaug-images-on-DeeplabV3-code/
https://blog.51cto.com/u_16099177/13064564
https://zhuanlan.zhihu.com/p/692329506
https://blog.51cto.com/u_16213690/11721814（感觉比较靠谱，先看这个链接）


下载两个文件：
VOCtrainval_11-May-2012.tar（包含 train/val 图像 + 标注）
VOCtest_11-May-2012.tar（测试集，可选）
SBD 数据增强集（Aug）
http://home.bharathh.info/pubs/codes/SBD/download.html
下载 dataset_RELEASE.zip，包含训练和验证的标注 PNG 文件。



data/
└── VOC2012/
    ├── VOCdevkit/
    │   └── VOC2012/
    │       ├── JPEGImages/          # 原图
    │       ├── SegmentationClass/   # VOC2012 官方分割标注
    │       ├── ImageSets/
    │       │   └── Segmentation/    # train.txt / val.txt / ...
    │       └── ...
    └── SBD/
        ├── dataset/                  # SBD 图像和标注
        └── ...




## step 2
运行一个DeepLabV3+与Continual Learning的完整案例
