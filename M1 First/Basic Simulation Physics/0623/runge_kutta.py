import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x0=0.0 # initial value of x
v0=1.0 # initial value of v
dt=0.01 # step width
tmax=2000 # number of repetition

def rk4(x,v,dt):
  k1=np.zeros((2,1))
  k2=np.zeros((2,1))
  k3=np.zeros((2,1))
  k4=np.zeros((2,1))

  k1[0]=dt*f1(x,v)
  k1[1]=dt*f2(x,v)
  k2[0]=dt*f1(x+k1[0]/2.0,v+k1[1]/2.0)
  k2[1]=dt*f2(x+k1[0]/2.0,v+k1[1]/2.0)
  k3[0]=dt*f1(x+k2[0]/2.0,v+k2[1]/2.0)
  k3[1]=dt*f2(x+k2[0]/2.0,v+k2[1]/2.0)
  k4[0]=dt*f1(x+k3[0],v+k3[1])
  k4[1]=dt*f2(x+k3[0],v+k3[1])

# Euler method
  dx=k1[0]
  dv=k1[1]
# midpoint method
#  dx=k2[0]
#  dv=k2[1]
# Runge-Kutta method
#  dx=(k1[0]+2.0*k2[0]+2.0*k3[0]+k4[0])/6.0
#  dv=(k1[1]+2.0*k2[1]+2.0*k3[1]+k4[1])/6.0

  return dx,dv

def f1(x,v):
  return v

def f2(x,v):
  return -x

#main
x=x0
v=v0
data=np.zeros((tmax,3))

data[0,0]=0.0
data[0,1]=x
data[0,2]=v

for i in range(1,tmax):
  t=i*dt
  [dx,dv]=rk4(x,v,dt)
  x=x+dx
  v=v+dv
  data[i,0]=t
  data[i,1]=x[0]
  data[i,2]=v[0]

np.savetxt('out.dat',data,fmt='%e')
plt.plot(data[:,0],data[:,1])
plt.show()
