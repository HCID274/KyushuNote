import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 微分方程式系を記述する関数を定義
# この関数は二階の常微分方程式 d^2x/dt^2 = -a*x に対応します
# これを以下のように一階の連立方程式に変換します：
# y[0] = x (位置) とおく
# y[1] = dx/dt (速度) とおく
# すると:
# dy[0]/dt = y[1]
# dy[1]/dt = d^2x/dt^2 = -a*x = -a*y[0]
def f(xy, t, a):
    """
    微分方程式系の定義。
    xy: [x, dx/dt] を含むリストまたは配列。
    t: 現在の時刻。
    a: 方程式中のパラメータ (ω^2 に対応)。
    戻り値: [dx/dt, d^2x/dt^2]
    """
    x_val = xy[0]      # 現在の x の値
    dxdt_val = xy[1]   # 現在の dx/dt の値

    # dx/dt (つまり y[1])
    # d(dx/dt)/dt = -a * x (つまり -a * y[0])
    return [dxdt_val, -a * x_val]

# --- パラメータ設定 ---
# 元の問題は d^2x/dt^2 = -x なので、a = 1 となります
# もし a = 1 ならば、角振動数 ω = sqrt(a) = 1 rad/s
# 周期 T = 2 * pi / ω = 2 * pi 秒
a = 1.0

# 初期条件:
# x(0) = 0.0
# x'(0) = 1.0 (つまり t=0 における dx/dt の値)
# xy0 = [初期位置, 初期のdx/dt]
xy0 = [0.0, 1.0]

# 時間範囲:
# 2周期分の振動を表示する必要があります。
# 1周期 T = 2 * pi
# 2周期 = 2 * T = 4 * pi
t_start = 0.0
t_end = 4 * np.pi  # 終了時刻を2周期に設定
num_points = 400   # 時間点の数。より滑らかな曲線を得るために必要に応じて調整
# t = np.arange(t_start, t_end, 0.01) # arange も使えますが、linspace の方が端点を保証しやすいです
t = np.linspace(t_start, t_end, num_points) # t_start と t_end の間に num_points 個の等間隔な時間点を生成

# --- 微分方程式の求解 ---
# odeint 関数は常微分方程式系を解くために使用されます
# 引数:
#   f: 微分方程式を定義する関数
#   xy0: 初期条件
#   t: 対応するyの値を求めたい時間点のシーケンス
#   args=(a,): 関数fに渡す追加の引数 (タプル形式である必要があります)
orbit = odeint(f, xy0, t, args=(a,))

# --- 結果の描画 ---
# orbit は2次元配列です:
# orbit[:, 0] はすべての時間点における x(t) の値 (位置) を格納
# orbit[:, 1] はすべての時間点における dx/dt(t) の値 (速度) を格納
plt.figure(figsize=(10, 6)) # 図のサイズを設定
plt.plot(t, orbit[:, 0], label=f'x(t) (a={a})') # x(t) vs t をプロット
plt.xlabel('Time (t) / seconds') # x轴标签
plt.ylabel('Position (x)')      # y轴标签
plt.title('Simple Harmonic Oscillation (Two Periods)') # 图像标题
plt.grid(True) # グリッドを表示

# 周期を明確に表示するために、周期点をマークする
one_period = 2 * np.pi
plt.axvline(x=one_period, color='r', linestyle='--', label=f'1 Period ({one_period:.2f} s)')
plt.axvline(x=2 * one_period, color='g', linestyle='--', label=f'2 Periods ({2*one_period:.2f} s)')

plt.legend() # 凡例を表示
plt.show()   # 図を表示

print(f"角振動数 ω = sqrt(a) = {np.sqrt(a):.2f} rad/s")
print(f"1周期 T = 2*pi/ω = {2*np.pi/np.sqrt(a):.4f} s")
print(f"2周期 2T = {4*np.pi/np.sqrt(a):.4f} s")
print(f"描画時間範囲: {t_start} s から {t_end:.4f} s まで")