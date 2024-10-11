import pickle

# 加载pickle文件
with open('results_spa.pickle', 'rb') as f:
    alg_values, gr_values, group_size = pickle.load(f)

import matplotlib.pyplot as plt
import numpy as np

# 假设alg_values, gr_values, group_size已经加载
# 这里以某个具体的算法、图和属性为例

algorithm = 'Greedy'  # 选择一个算法
graphname = 'spa_500_0'  # 选择一个图
attribute = 'region'  # 选择一个属性

# 提取数据
greedy_vals = alg_values[algorithm][graphname][attribute]
group_sizes = group_size[graphname][attribute]

# 假设num_runs为1，可以简化数据
greedy_vals = greedy_vals[0]
group_sizes = group_sizes[0]

# 生成条形图
x = np.arange(len(greedy_vals))  # 属性值的数量
width = 0.35  # 条形图的宽度

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, greedy_vals, width, label='Greedy')
rects2 = ax.bar(x + width/2, group_sizes, width, label='Group Size')

# 添加一些文本标签
ax.set_xlabel('Attribute Values')
ax.set_ylabel('Values')
ax.set_title('Greedy Algorithm and Group Sizes by Attribute Values')
ax.set_xticks(x)
ax.set_xticklabels([f'Value {i}' for i in x])
ax.legend()

# 自动添加标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()

# 示例：生成多个属性的折线图
attributes = ['region', 'ethnicity', 'age', 'gender', 'status']
num_runs = 1  # 假设num_runs为1

for attribute in attributes:
    greedy_vals = alg_values[algorithm][graphname][attribute][0]
    group_sizes = group_size[graphname][attribute][0]

    plt.figure()
    plt.plot(greedy_vals, label='Greedy')
    plt.plot(group_sizes, label='Group Size')
    plt.xlabel('Attribute Values')
    plt.ylabel('Values')
    plt.title(f'Greedy Algorithm and Group Sizes by {attribute.capitalize()}')
    plt.legend()
    plt.show()
