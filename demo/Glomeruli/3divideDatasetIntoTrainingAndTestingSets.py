import os
import random
print("cwd:", os.getcwd())
PATH_IMAGE = './data/Glomeruli-dataset/images/'
all_file_list = os.listdir(PATH_IMAGE)
all_file_num = len(all_file_list)
print("all_file_num",all_file_num)
random.shuffle(all_file_list) # 随机打乱全部数据文件名列表
train_ratio = 0.8
test_ratio = 1 - train_ratio
train_file_list = all_file_list[:int(all_file_num*train_ratio)]
test_file_list = all_file_list[int(all_file_num*train_ratio):]
print('数据集图像总数', all_file_num)
print('训练集划分比例', train_ratio)
print('训练集图像个数', len(train_file_list))
print('测试集图像个数', len(test_file_list))
os.mkdir('./data/Glomeruli-dataset/splits')  # 新建一个名为 splits 的子文件夹
with open('./data/Glomeruli-dataset/splits/train.txt', 'w') as f:
    f.writelines(line.split('.')[0] + '\n' for line in train_file_list)
with open('./data/Glomeruli-dataset/splits/val.txt', 'w') as f:
    f.writelines(line.split('.')[0] + '\n' for line in test_file_list)
