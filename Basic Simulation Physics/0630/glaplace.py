# 来源: リレーション 小高知宏 著、オーム社
# 文件名: glaplace.py (修改版)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math

# --- 参数定义 ---
LIMIT = 1000  # 迭代次数
N = 101       # x方向的网格点数
M = 101       # y方向的网格点数

# --- 迭代函数 ---
# 对该函数进行了修正，使其索引 u[j][i] (即 u[y][x]) 更加清晰
def iteration(u):
    # 创建一个与u相同大小的临时网格，用于存放下一次迭代的结果
    u_next = [[0 for i in range(N)] for j in range(M)]
    
    # 遍历所有内部点 (不包括边界)
    # j 代表 y 坐标 (行), i 代表 x 坐标 (列)
    for j in range(1, M - 1):
        for i in range(1, N - 1):
            # 拉普拉斯方程的差分形式：一个点的值是其周围四个点的平均值
            u_next[j][i] = (u[j][i - 1] + u[j][i + 1] +  # 左边 + 右边
                           u[j - 1][i] + u[j + 1][i]) / 4 # 上边 + 下边
    
    # 将计算出的新值更新回原网格 u
    # 同样只更新内部点，边界值保持不变
    for j in range(1, M - 1):
        for i in range(1, N - 1):
            u[j][i] = u_next[j][i]

# --- 主程序部分 ---

# 初始化一个 M x N 的二维网格，所有值为 0
# u[j][i] 对应于 u(y, x)
u = [[0 for i in range(N)] for j in range(M)]  # 初始化

# --- 设置四个边界的非均匀边界条件 ---

# 边界条件 1: 底部 (y=0)
# 沿 x 轴设置为一个正弦波
for i in range(N):
    u[0][i] = math.sin(2 * math.pi * i / (N - 1))

# 边界条件 2: 顶部 (y=100, M-1)
# 沿 x 轴设置为一个余弦波
for i in range(N):
    u[M - 1][i] = math.cos(2 * math.pi * i / (N - 1))

# 边界条件 3: 左侧 (x=0)
# 沿 y 轴设置为线性增加的值 (-1 到 1)
for j in range(M):
    u[j][0] = 2.0 * j / (M - 1) - 1.0

# 边界条件 4: 右侧 (x=100, N-1)
# 沿 y 轴设置为一个抛物线形状
for j in range(M):
    val = j / (M - 1) # 归一化到 [0, 1]
    u[j][N - 1] = 4 * (val - 0.5)**2 # [0, 1]范围的抛物线

# --- 执行迭代计算 ---
# 重复调用迭代函数，使网格内的值逐渐收敛
for i in range(LIMIT):
    iteration(u)

# --- 绘制三维曲面图 ---

# 创建 x, y 坐标网格
x = np.arange(0, N)
y = np.arange(0, M)
X, Y = np.meshgrid(x, y)

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 将列表 u 转换为 NumPy 数组以便绘图
U = np.array(u)

# 绘制表面图
# cmap='coolwarm' 是一个常用的颜色映射
surf = ax.plot_surface(X, Y, U, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 设置图表标题和坐标轴标签 (使用英文以避免方块字问题)
ax.set_title("2D Laplace Equation with Inhomogeneous Boundaries")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("U value")

# 显示图形
plt.show()