import numpy as np
from matplotlib import pyplot as plt
# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 设置大文本显示
np.set_printoptions(threshold=10000)
# 使用load方法读取二进制文件
data = np.load("matplot_data/国民经济核算季度数据.npz")
# print(type(data))#<class 'numpy.lib.npyio.NpzFile'>
values = data["values"]
columns = data["columns"]
# print(columns)
# print(values)

"""2000-2017 各产业与行业的国民生产总值散点图"""
# 1.创建画布1000*1300大小
f = plt.figure(figsize=(10,13))
# 2.创建子视图
f.add_subplot(2,1,1)
# 3.绘制散点图
# 第一产业
plt.scatter(values[:,0],values[:,3],marker="D")
# 第二产业
plt.scatter(values[:,0],values[:,4],marker="o")
# 第三产业
plt.scatter(values[:,0],values[:,5],marker="+")

# 4.设置样式
# plt.xlabel("产业种类")
plt.ylabel("各产业生产总值（单位：亿元）")
plt.title("2000-2017年各产业的国民生产总值散点图")
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
plt.legend(["第一产业","第二产业","第三产业"])
# 5.保存与显示
# plt.savefig("img/1.散点图1.png")


"""2000-2017 各产业与行业的国民生产总值折线图"""

# 1.创建画布
# f = plt.figure(figsize=(8,8),dpi=200)
# 2.创建子视图
f.add_subplot(2,1,2)
# 3.绘制散点图
# 农林牧渔业
plt.scatter(values[:,0],values[:,6],marker="D")
# 工业
plt.scatter(values[:,0],values[:,7],marker="o")
# 建筑业
plt.scatter(values[:,0],values[:,8],marker="+")
# 批发和零售业
plt.scatter(values[:,0],values[:,9],marker="x")
# 交通运输、仓储和邮政业
plt.scatter(values[:,0],values[:,10],marker="v")
# 住宿和餐饮业
plt.scatter(values[:,0],values[:,11],marker="h")
# 金融业
plt.scatter(values[:,0],values[:,12],marker="*")
# 房地产业
plt.scatter(values[:,0],values[:,13],marker="s")
# 其他行业
plt.scatter(values[:,0],values[:,14],marker="8")



# 4.设置样式
# plt.xlabel("产业种类")
plt.ylabel("各行业生产总值（单位：亿元）")
plt.title("2000-2017年各行业的国民生产总值散点图")
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
plt.legend(["农林牧渔业","工业","建筑业","批发和零售业","交通运输、仓储和邮政业","住宿和餐饮业","金融业","房地产业","其他行业"])
# 5.保存与显示
plt.savefig("img/1.散点图1.png")
plt.show()