## Sample program for checking installation
import copy as cp
import numpy as np
import matplotlib.pyplot as plt

## definition
L    = 1.0    #cavity length [m] 
N    = 40     #number of girds [-]
dl   = L/N    #grid spacing [m]

## grid
x  = np.zeros(N+2)
dx = np.zeros(N+2)
x[0]      = 0.0 
dx[0]     = 0.0
dx[N+1]   = 0.0
dx[1:N+1] = dl ##Note that 1 to N, but not N+1 in python
for i in range(1,N+2):
    x[i]=x[i-1]+0.5*(dx[i]+dx[i-1])
dy = cp.copy(dx) ## value copy, don't use dy=dx for array in python
y  = cp.copy(x)

## dummy data
t = np.zeros((N+2,N+2))
for j in range(1,N+1): 
    for i in range(1,N+1): 
        t[j,i] = j*i

## visualization & save image
fig=plt.figure(figsize=(6.0,6.0))
img=plt.contourf(x,y,t, cmap="Blues")
plt.gca().set_aspect('equal')
cbar=plt.colorbar(img)
cbar.set_label('Temperature [K]')
plt.title('Temperature distribution')
plt.xlabel('x [m]')
plt.ylabel('y [j]')
plt.show()
k=1
fn='t_' + '{:03}'.format(k) + '.png'
fig.savefig(fn)
