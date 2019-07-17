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
"""2000年各产业生产总值在国民生产总值中构成占比"""
# 1.创建子视图
f.add_subplot(2,2,1)
# 2.提取数据
value = values[0,3:6]
# print(value)
# 3.绘制饼状图
label=["第一产业","第二产业","第三产业"]
plt.pie(value,explode=[0.01,0.01,0.01],labels=label,autopct='%.2f%%')
# 4.样式设计
plt.title("2000年各产业生产总值在国民生产总值中构成占比")



"""2017年各产业生产总值在国民生产总值中构成占比"""
# 1.创建子视图
f.add_subplot(2,2,2)
# 2.提取数据
value = values[-1,3:6]
# print(value)
# 3.绘制饼状图
label=["第一产业","第二产业","第三产业"]
plt.pie(value,explode=[0.01,0.01,0.0],labels=label,autopct='%.2f%%')
# 4.样式设计
plt.title("2017年各产业生产总值在国民生产总值中构成占比")


"""2000年各行业生产总值在国民生产总值中构成占比"""
# 1.创建子视图
f.add_subplot(2,2,3)
# 2.提取数据
value = values[0,6:]
# print(value)
# 3.绘制饼状图
label=["农林牧渔业","工业","建筑业","批发和零售业","交通运输、仓储和邮政业","住宿和餐饮业","金融业","房地产业","其他行业"]
plt.pie(value,explode=[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01],labels=label,autopct='%.2f%%')
# 4.样式设计
plt.title("2000年各行业生产总值在国民生产总值中构成占比")


"""2017年各行业生产总值在国民生产总值中构成占比"""
# 1.创建子视图
f.add_subplot(2,2,4)
# 2.提取数据
value = values[-1,6:]
# print(value)
# 3.绘制饼状图
label=["农林牧渔业","工业","建筑业","批发和零售业","交通运输、仓储和邮政业","住宿和餐饮业","金融业","房地产业","其他行业"]
plt.pie(value,explode=[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01],labels=label,autopct='%.2f%%')
# 4.样式设计
plt.title("2017年各行业生产总值在国民生产总值中构成占比")

# 5.保存与显示
plt.savefig("img/1.饼状图.png")
plt.show()