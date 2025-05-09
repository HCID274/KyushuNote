## python, 1d unsteady HCE, explicit, implicite comparison : (rhoCp*dT/dt=lmd^2T/dx^2 -q with fixed B.C.)
## t: temperature, x: coordinate, q: heat loss [J/m3s], a = lm/rhoCp: thermal diffusivity [m2/s]
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
import math
import sys

## definition
L    = 1.0    # cavity length [m] 
N    = 10     # number of girds [-]
dl   = L/N    # grid spacing [m]
TL   = 300.0  # low temperature  [K]
TH   = 500.0  # high temperature [K]
crit = 0.0001   # criteria for convergence [K]

## values for aluminum
lm    = 209.5        # heat conduction [J/mKs]
rhoCp = 2.4*10.0**6  # volumetric specific heat [J/m3s]
alpha = lm/rhoCp     # thermal diffusivity [m2/s]

## for unsteady simulation
r     = 0.25
dt    = r*(dl)**2/alpha #delta t [s]
NO    = 500     #time steps to solve
ST    = 10       #output stride
IST   = 10       #time step interval for implicit simulation
#IST   = 10      #time step interval for implicit simulation
NOI   = int(NO/IST)

## for case 3
R  = 0.005    # Metal bar radius [5mm]
Ta = TL      # Ambient temperature [K]
h  = 10.0    # Heat transfer coefficient [W/m2s]

## grid
x  = np.zeros(N+2)
dx = np.zeros(N+2)
x[0]      = 0.0 
dx[0]     = 0.0
dx[N+1]   = 0.0
dx[1:N+1] = dl ## Note that 1 to N, but not N+1 in python
for i in range(1,N+2):
    x[i]=x[i-1]+0.5*(dx[i]+dx[i-1])
    ##for debug
    #print(x[i])
## for debug
#x.size

## coefficient
ce = np.zeros(N+1)
cw = np.zeros(N+1)
co = np.zeros(N+1)
coI = np.zeros(N+1)
cd = np.zeros(N+1)
for i in range(1,N+1):
    ce[i] = lm/(0.5*(dx[i]+dx[i+1]))
    cw[i] = lm/(0.5*(dx[i]+dx[i-1]))
co[:]=rhoCp*dl/dt
##for implicit
coI[:]=rhoCp*dl/(IST*dt)
cd[:] = cw[:] + ce[:] + coI[:] 

##t(x):temperature, tp(x):predicted temperature, q(x):heat loss
T          = np.zeros(N+2)
Tp         = np.zeros(N+2)
To         = np.zeros(N+2)
q          = np.zeros(N+2)

##source zero
q[:]  = 0


##Explicit
## define values
T[:]       = TL
## boudnary condition
T[0]    = TL
T[N+1]  = TH 
## initial prediction values
Tp[:]   = T[:]
To[:]   = T[:]

Ts=[]
for n in range(0,NO):
   flg=0
   for i in range(1,N+1):
       T[i] = (ce[i]*To[i+1] + cw[i]*To[i-1] + (co[i]-ce[i]-cw[i])*To[i] - q[i]/lm*dx[i])/co[i]
 
   To[:]=T[:]

   ## visualization & save image --> include thin in last line of time loop
   if(np.mod(n,ST) == 0):  
       print(n)
       tmp=cp.copy(T)
       Ts.append(tmp)


##Implicite method
## define values
T[:]       = TL
## boudnary condition
T[0]    = TL
T[N+1]  = TH 
## initial prediction values
Tp[:]   = T[:]
To[:]   = T[:]


TsI=[]
for n in range(0,NOI):
#for n in range(1,NOI):
   ##iteration loop
   l = 0 #counter
   flg=1
   while flg ==1:
      flg=0
      l=l+1
      for i in range(1,N+1):
          T[i] = (ce[i]*Tp[i+1] + cw[i]*Tp[i-1] + coI[i]*To[i] - q[i]/lm*dx[i])/cd[i]
      ##convergence check
      for i in range(1,N+1):
          if(np.abs(T[i]-Tp[i])>crit):
              flg=1 #calculate again until reaching the converged values
      Tp[:]=T[:]
      ## for debug
      #if(np.mod(l,10) == 0):
      #    print(l)

   To[:]=T[:]

   ## visualization & save image --> include thin in last line of time loop
   if(np.mod(n,ST) == 0):
       print(n)
       tmp=cp.copy(T)
       TsI.append(tmp)

## visualization & save image
ymin=TL
ymax=TH
xp=0
yp=ymax + 0.04*(ymax-ymin)
##for animation
ims=[]
fig=plt.figure(figsize=(6.0,6.0))
ax=fig.add_subplot(111)
ax.set_ylim(ymin, ymax)
ax.set_xlim(0,L)
#plt.gca().set_aspect('equal')
plt.title('Temperature distribution')
plt.xlabel('x [m]')
plt.ylabel('T [K]')
plt.grid()
iI=0
for i in range(len(Ts)):
    txt=ax.text(xp/L, yp, 'timestep='+str(i*ST), size=12, backgroundcolor='white')
    img=plt.plot(x/L,Ts[i], label='t',color='red')

    if(np.mod(i,IST) == 0):
        img2=plt.plot(x/L,TsI[iI], label='t',color='blue', linestyle='dashed')
        ims.append(img + img2 + [txt])
        iI=iI+1
    else:
        ims.append(img + [txt])

## animation draw
ani=an.ArtistAnimation(fig,ims,interval=500)
ani.save('comparison.gif', writer="imagemagick")
#plt.show()
