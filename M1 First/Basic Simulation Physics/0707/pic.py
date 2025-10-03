import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

"""
创建你自己的等离子体PIC模拟 (使用Python)
Philip Mocz (2020) Princeton Univeristy, @PMocz
模拟一维双流不稳定性
代码使用粒子网格法(PIC)计算电子在泊松-麦克斯韦方程下的运动
"""


def getAcc( pos, Nx, boxsize, n0, Gmtx, Lmtx ):
	"""
    计算每个粒子由于电场而产生的加速度
	pos      是一个Nx1矩阵，表示粒子位置
	Nx       是网格单元的数量
	boxsize  是域的大小 [0,boxsize]
	n0       是电子数密度
	Gmtx     是一个Nx x Nx矩阵，用于计算网格上的梯度
	Lmtx     是一个Nx x Nx矩阵，用于计算网格上的拉普拉斯算子
	a        是一个Nx1矩阵，表示加速度
	"""
	# 通过将粒子放置到最近的2个网格点(j & j+1，使用适当权重)
	# 并进行归一化来计算网格上的电子数密度
	N          = pos.shape[0]
	dx         = boxsize / Nx
	j          = np.floor(pos/dx).astype(int)
	jp1        = j+1
	weight_j   = ( jp1*dx - pos  )/dx
	weight_jp1 = ( pos    - j*dx )/dx
	jp1        = np.mod(jp1, Nx)   # 周期边界条件
	n  = np.bincount(j[:,0],   weights=weight_j[:,0],   minlength=Nx);
	n += np.bincount(jp1[:,0], weights=weight_jp1[:,0], minlength=Nx);
	n *= n0 * boxsize / N / dx 
	
	# 求解泊松方程: laplacian(phi) = n-n0
	phi_grid = spsolve(Lmtx, n-n0, permc_spec="MMD_AT_PLUS_A")
	
	# 应用导数得到电场
	E_grid = - Gmtx @ phi_grid
	
	# 将网格值插值到粒子位置
	E = weight_j * E_grid[j] + weight_jp1 * E_grid[jp1]
	
	a = -E

	return a
	

def run_simulation(n0=1, tEnd=50, output_filename="pic.png", plotRealTime=False):
	""" 
	等离子体PIC模拟的参数化版本
	n0: 电子数密度
	tEnd: 模拟结束时间
	output_filename: 输出图片文件名
	plotRealTime: 是否实时绘图
	"""
	
	# 模拟参数
	N         = 40000   # 粒子数量
	Nx        = 400     # 网格单元数量
	t         = 0       # 模拟当前时间
	dt        = 1       # 时间步长
	boxsize   = 50      # 周期域 [0,boxsize]
	vb        = 3       # 束流速度
	vth       = 1       # 束流宽度
	A         = 0.1     # 扰动幅度
	
	# 生成初始条件
	np.random.seed(42)            # 设置随机数种子
	# 构造两个方向相反的高斯束流
	pos  = np.random.rand(N,1) * boxsize  
	vel  = vth * np.random.randn(N,1) + vb
	Nh = int(N/2)
	vel[Nh:] *= -1
	# 添加扰动
	vel *= (1 + A*np.sin(2*np.pi*pos/boxsize))
	
	# 构造矩阵G来计算梯度(一阶导数)
	dx = boxsize/Nx
	e = np.ones(Nx)
	diags = np.array([-1,1])
	vals  = np.vstack((-e,e))
	Gmtx = sp.spdiags(vals, diags, Nx, Nx);
	Gmtx = sp.lil_matrix(Gmtx)
	Gmtx[0,Nx-1] = -1
	Gmtx[Nx-1,0] = 1
	Gmtx /= (2*dx)
	Gmtx = sp.csr_matrix(Gmtx)

	# 构造矩阵L来计算拉普拉斯算子(二阶导数)
	diags = np.array([-1,0,1])
	vals  = np.vstack((e,-2*e,e))
	Lmtx = sp.spdiags(vals, diags, Nx, Nx);
	Lmtx = sp.lil_matrix(Lmtx)
	Lmtx[0,Nx-1] = 1
	Lmtx[Nx-1,0] = 1
	Lmtx /= dx**2
	Lmtx = sp.csr_matrix(Lmtx)
	
	# 计算初始重力加速度
	acc = getAcc( pos, Nx, boxsize, n0, Gmtx, Lmtx )
	
	# 时间步数
	Nt = int(np.ceil(tEnd/dt))
	
	# 准备图形
	fig = plt.figure(figsize=(8,6), dpi=100)
	
	# 模拟主循环
	for i in range(Nt):
		# (1/2) kick
		vel += acc * dt/2.0
		
		# drift (应用周期边界条件)
		pos += vel * dt
		pos = np.mod(pos, boxsize)
		
		# 更新加速度
		acc = getAcc( pos, Nx, boxsize, n0, Gmtx, Lmtx )
		
		# (1/2) kick
		vel += acc * dt/2.0
		
		# 更新时间
		t += dt
		
		# 实时绘图 - 将一半粒子着色为蓝色，另一半为红色
		if plotRealTime or (i == Nt-1):
			plt.cla()
			plt.scatter(pos[0:Nh],vel[0:Nh],s=.4,color='blue', alpha=0.5, label='Beam 1')
			plt.scatter(pos[Nh:], vel[Nh:], s=.4,color='red',  alpha=0.5, label='Beam 2')
			plt.axis([0,boxsize,-6,6])
			plt.xlabel('Position (x)')
			plt.ylabel('Velocity (v)')
			plt.title(f'Phase Space Plot (n0 = {n0}, t = {t:.1f})')
			plt.legend()
			plt.grid(True, alpha=0.3)
			
			if plotRealTime:
				plt.pause(0.1)
			
	
	# 保存图形
	plt.savefig(output_filename, dpi=240, bbox_inches='tight')
	if not plotRealTime:
		plt.close()  # 如果不是实时绘图，关闭图形以节省内存
	    
	return 0


def main():
	""" 默认主函数，保持向后兼容性 """
	plotRealTime = True # 切换开关用于模拟过程中的绘图
	return run_simulation(n0=1, tEnd=50, output_filename='pic.png', plotRealTime=plotRealTime)


  
if __name__== "__main__":
  main()