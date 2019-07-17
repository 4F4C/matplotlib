# 通用设置
import numpy as np
from matplotlib import pyplot as plt
# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 设置大文本显示
np.set_printoptions(threshold=10000)

# 1.创建画布
f = plt.figure(figsize=(10,12))
# 2.读取数据
data = np.load("./matplot_data/国民经济核算季度数据.npz")
values = data["values"]
columns = data["columns"]
print(columns)
print(values)
"""2000年第一季度各产业生产总值构成分布"""
# 1.创建子视图
f.add_subplot(2,2,1)
# 2.提取数据
value = values[0,3:6]
# print(value)
# 3.绘制直方图
plt.bar(range(3,6),value,width=0.6)
# 4.样式设计
label=["第一产业","第二产业","第三产业"]
plt.xticks(range(3,6),label)
plt.title("2000年第一季度各产业生产总值构成分布")
plt.xlabel("2000年第一季度")
plt.ylabel("各产业国民生产总值（单位：亿元）")


"""2017年第一季度各产业生产总值构成分布"""
# 1.创建子视图
f.add_subplot(2,2,2)
# 2.提取数据
value = values[-1,3:6]
# print(value)
# 3.绘制直方图
plt.bar(range(3,6),value,width=0.6)
# 4.样式设计
label=["第一产业","第二产业","第三产业"]
plt.xticks(range(3,6),label)
plt.title("2017年第一季度各产业生产总值构成分布")
plt.xlabel("2017年第一季度")
plt.ylabel("各产业国民生产总值（单位：亿元）")


"""2000年第一季度各行业生产总值构成分布"""
# 1.创建子视图
f.add_subplot(2,2,3)
# 2.提取数据
value = values[0,6:]
# print(value)
# 3.绘制直方图
plt.bar(range(9),value,width=0.3)
# 4.样式设计
label=["农林牧渔业","工业","建筑业","批发和零售业","交通运输、仓储和邮政业","住宿和餐饮业","金融业","房地产业","其他行业"]
plt.xticks(range(9),label,rotation=60)
plt.title("2000年第一季度各产业生产总值构成分布")
plt.xlabel("2000年第一季度")
plt.ylabel("各行业国民生产总值（单位：亿元）")


"""2017年第一季度各行业生产总值构成分布"""
# 1.创建子视图
f.add_subplot(2,2,4)
# 2.提取数据
value = values[-1,6:]
# print(value)
# 3.绘制直方图
plt.bar(range(9),value,width=0.3)
# 4.样式设计
label=["农林牧渔业","工业","建筑业","批发和零售业","交通运输、仓储和邮政业","住宿和餐饮业","金融业","房地产业","其他行业"]
plt.xticks(range(9),label,rotation=60)
plt.title("2017年第一季度各行业生产总值构成分布")
plt.xlabel("2017年第一季度")
plt.ylabel("各产业国民生产总值（单位：亿元）")
# 5.保存与显示
plt.savefig("img/1.直方图.png")
plt.show()