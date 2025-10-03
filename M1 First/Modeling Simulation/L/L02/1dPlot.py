## Sample program plotting 1d graph animation
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
##for Jupyter user: execute by
#%matplotlib notebook
#exec(open("1dPlot.py").read())

#***************************************************************#
##Ex1: Read this soruce code and understand the structure
##Ex2: Write initial distribution of  y. 
##     Hints: Use np.sqrt() and np.exp() for square root and exponential.
##Ex3: Write distribution y at time t
##Ex4: Add distribution with the diffusivity of 10 times y)
#***************************************************************#

## definition
L    = 1.0            # length [m] 
N    = 101            # number of girds [-]
dx   = L/N            # grid spacing [m]
a    = 0.00001        # diffusivity [m2/s]
dt   = dx**2/(2.0*a)  # time step [s]
y0   = 30.0           # initial temperature [oC]
x0   = L/2            # heat source location [m]  
A    = (5*dx)**2      # heat source distribution length^2 [m^2]
Nt   = 20             # number of time step

## coordinate 
x  = np.zeros(N+1) #array from 0 to N+1
x[0]      = 0.0 
for i in range(1,N+1):
    x[i]=x[i-1]+dx

## define function
y = np.zeros(N+1)   # array from 0 to N+1, for value y at time t
yInit=np.zeros(N+1) # array for value yInit
## initial condition --> Ex2: Write equation for initial condition
yInit=x
## time step
ys=[]  # used for animation
for i in range(0,Nt):
   # time at step i
   t=i*dt
   # y value at step i --> Ex3: Write equation for y at time step i
   y=x*i
   # y2 value at step i --> Ex4: Write equation for y at time step i at y2
   # for animation
   ys.append(y)

## visualization
ymin = 0.0
ymax = y0
xp   = 0
yp   = ymax + 0.04*(ymax-ymin)
## animation
ims = []
fig = plt.figure(figsize=(6.0,6.0))
ax  = fig.add_subplot(111)
ax.set_ylim(ymin, ymax)
plt.title('Temperature distribution')
plt.xlabel('x [m]')
plt.ylabel('T [oC]')
plt.grid()
for i in range(len(ys)):
    txt=ax.text(xp, yp, str(i), size=12, backgroundcolor='white')  # time step on figure
    img=plt.plot(x,ys[i], label='t',color='red')                   # plot y at t
    plt.plot(x,yInit, label='t',color='black', linestyle='dashed') # plot initial condition
    ims.append(img +  [txt])                                       # for animation
## animation draw
ani=an.ArtistAnimation(fig,ims,interval=200)
ani.save('anim.gif', writer="imagemagick")
plt.show()

