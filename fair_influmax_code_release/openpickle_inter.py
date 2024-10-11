import pickle

# 加载 pickle 文件
with open('results_spa_intersectional.pickle', 'rb') as f:
    alg_values, gr_values, group_size = pickle.load(f)

# 打印加载的数据结构
print("Algorithms:", list(alg_values.keys()))
print("Graphs:", list(gr_values.keys()))

# 示例：查看某个算法在某个图上的结果
algorithm = 'Greedy'
graphname = 'spa_500_0'
run = 9

print(f"Results for algorithm {algorithm} on graph {graphname}, run {run}:")
print("Influence values:", alg_values[algorithm][graphname][run])
print("Group influence values:", gr_values[graphname][run])
print("Group sizes:", group_size[graphname][run])

import pickle

# 加载 pickle 文件
with open('results_spa_intersectional.pickle', 'rb') as f:
    alg_values, gr_values, group_size = pickle.load(f)

# 打印加载的数据结构
print("Algorithms:", list(alg_values.keys()))
print("Graphs:", list(gr_values.keys()))

# 示例：查看某个算法在某个图上的结果
algorithm = 'GR'
graphname = 'spa_500_0'
run = 9

print(f"Results for algorithm {algorithm} on graph {graphname}, run {run}:")
print("Influence values:", alg_values[algorithm][graphname][run])
print("Group influence values:", gr_values[graphname][run])
print("Group sizes:", group_size[graphname][run])

import pickle

# 加载 pickle 文件
with open('results_spa_intersectional.pickle', 'rb') as f:
    alg_values, gr_values, group_size = pickle.load(f)

# 打印加载的数据结构
print("Algorithms:", list(alg_values.keys()))
print("Graphs:", list(gr_values.keys()))

# 示例：查看某个算法在某个图上的结果
algorithm = 'MaxMin-Size'
graphname = 'spa_500_0'
run = 9

print(f"Results for algorithm {algorithm} on graph {graphname}, run {run}:")
print("Influence values:", alg_values[algorithm][graphname][run])
print("Group influence values:", gr_values[graphname][run])
print("Group sizes:", group_size[graphname][run])
