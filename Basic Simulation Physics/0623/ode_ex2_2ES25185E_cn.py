import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定义描述微分方程组的函数
# 这个函数对应于二阶常微分方程 d^2x/dt^2 = -a*x
# 我们将其转换为一阶方程组：
# 令 y[0] = x (位置)
# 令 y[1] = dx/dt (速度)
# 则:
# dy[0]/dt = y[1]
# dy[1]/dt = d^2x/dt^2 = -a*x = -a*y[0]
def f(xy, t, a):
    """
    微分方程组的定义。
    xy: 一个包含 [x, dx/dt] 的列表或数组。
    t: 当前时间。
    a: 方程中的参数 (对应 omega^2)。
    返回: [dx/dt, d^2x/dt^2]
    """
    x_val = xy[0]      # 当前 x 的值
    dxdt_val = xy[1]   # 当前 dx/dt 的值

    # dx/dt (即 y[1])
    # d(dx/dt)/dt = -a * x (即 -a * y[0])
    return [dxdt_val, -a * x_val]

# --- 参数设定 ---
# 题目中原始问题是 d^2x/dt^2 = -x，这意味着 a = 1
# 如果 a = 1, 则角频率 omega = sqrt(a) = 1 rad/s
# 周期 T = 2 * pi / omega = 2 * pi 秒
a = 1.0

# 初始条件:
# x(0) = 0.0
# x'(0) = 1.0 (即 dx/dt 在 t=0 时的值)
# xy0 = [x_initial, dx/dt_initial]
xy0 = [0.0, 1.0]

# 时间范围:
# 我们需要显示两个周期的振动。
# 一个周期 T = 2 * pi
# 两个周期 = 2 * T = 4 * pi
t_start = 0.0
t_end = 4 * np.pi  # 结束时间设置为两个周期
num_points = 400   # 时间点数量，可以根据需要调整以获得更平滑的曲线
# t = np.arange(t_start, t_end, 0.01) # 也可以用 arange，但 linspace 更能保证端点
t = np.linspace(t_start, t_end, num_points) # 在 t_start 和 t_end 之间生成 num_points 个等间距的时间点

# --- 求解微分方程 ---
# odeint 函数用于求解常微分方程组
# 参数:
#   f: 定义微分方程的函数
#   xy0: 初始条件
#   t: 需要求解其对应y值的时间点序列
#   args=(a,): 传递给函数f的额外参数 (必须是元组形式)
orbit = odeint(f, xy0, t, args=(a,))

# --- 绘制结果 ---
# orbit 是一个二维数组:
# orbit[:, 0] 存储的是所有时间点上的 x(t) 的值 (位置)
# orbit[:, 1] 存储的是所有时间点上的 dx/dt(t) 的值 (速度)
plt.figure(figsize=(10, 6)) # 设置图像大小
plt.plot(t, orbit[:, 0], label=f'x(t) for a={a}') # 绘制 x(t) vs t
plt.xlabel('Time (t) / seconds') # x轴标签
plt.ylabel('Position (x)')      # y轴标签
plt.title('Simple Harmonic Oscillation (Two Periods)') # 图像标题
plt.grid(True) # 显示网格

# 为了清晰显示周期，可以标记出周期点
one_period = 2 * np.pi
plt.axvline(x=one_period, color='r', linestyle='--', label=f'1 Period ({one_period:.2f} s)')
plt.axvline(x=2 * one_period, color='g', linestyle='--', label=f'2 Periods ({2*one_period:.2f} s)')

plt.legend() # 显示图例
plt.show()   # 显示图像

print(f"角频率 omega = sqrt(a) = {np.sqrt(a):.2f} rad/s")
print(f"一个周期 T = 2*pi/omega = {2*np.pi/np.sqrt(a):.4f} s")
print(f"两个周期 2T = {4*np.pi/np.sqrt(a):.4f} s")
print(f"绘图时间范围: 从 {t_start} s 到 {t_end:.4f} s")