## python, 2D heat conduction equation: (dT/dt=alpha*(d^2T/dx^2 + d^2T/dy^2) with fixed B.C.)
## ikegaya
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
######################################################################################
## Complete code for 2d HCE by Explicit method
## Hint: find BC, IC, Coefficients (Ce, Cw, Cs, Cn) and equation for TIJ
######################################################################################

## definition
L    = 1.0    #cavity length [m] 
N    = 20     #number of girds [-]
dl   = L/N    #grid spacing [m]
TL   = 300.0  #low temperature  [K]
TH   = 500.0  #high temperature [K]
crit = 0.01   #criteria for convergence [K]
a    = 1.0    #heat diffusivity [m2/s]
r    = 0.1    #diffusion number < 1/4for 2D
dt   = r/a*dl**2 #dt
#NO   = 5000   #time step
#dt   = dt
NO   = 5000   #time step
ST   = 100    #output stride  

print("    Explicit simulation  ")

##natural propaty
## values for water
lm    = 0.6
rhoCp = 4.182*1.25   # volumetric specific heat [J/m3s]
alpha = lm/rhoCp     # thermal diffusivity [m2/s]

## grid
x  = np.zeros(N+2)
dx = np.zeros(N+2)
x[0]      = 0.0 
dx[0]     = 0.0
dx[N+1]   = 0.0
dx[1:N+1] = dl ##Note that 1 to N, but not N+1 in python
for i in range(1,N+2):
    x[i]=x[i-1]+0.5*(dx[i]+dx[i-1])
    ##for debug
    #print(x[i])
dy = cp.copy(dx) ## value copy, don't use dy=dx for array in python
y  = cp.copy(x)
## for debug
#x.size
#y.size

## coefficient
ce=np.zeros(N+1)
cw=np.zeros(N+1)
cn=np.zeros(N+1)
cs=np.zeros(N+1)
co=np.zeros((N+1,N+1)) #for 2D
cd=np.zeros((N+1,N+1))
for i in range(1,N+1):
    ce[i] = 1.0
    cw[i] = 1.0
    cn[i] = 1.0
    cs[i] = 1.0
for j in range(1,N+1):
    for i in range(1,N+1):
        co[j,i]=1.0

##t(y,x):temperatuer, tp(y,x):predicted temperatue
T            = np.zeros((N+2,N+2))
T[:,:]       = TH
##boudnary condition
T[N+1,0:N+2] = 0.0
##initial & prediction values
Tp=cp.copy(T)
To=cp.copy(T)

## time step loop
Ts=[]
for n in range(NO):
    ##iteration loop
    #flg = 1 #control flag
    #l   = 0 #counter
    #while flg == 1:
    #   l+=1
    #   flg=0

    ##data store
    if(np.mod(n,ST)==0):
        print('time=' + str(n))
        tmp=cp.copy(T)
        Ts.append(tmp)

    for j in range(1,N+1): 
        for i in range(1,N+1): 
            ##calculation : Use To[j,i], co, ce, cw, cn, cs
            T[j,i] = To[j,i]
    
    ##convergence check
    #for j in range(1,N+1): 
    #    for i in range(1,N+1):
    #        if(np.abs(T[j,i]-Tp[j,i])>crit):
    #            flg=1 #calculate again until reaching the converged values
    #              
    #if(np.mod(l,10) == 0):  
    #    print('itr=' + str(l))

    ## update val.
    #Tp=cp.copy(T)

    ##update data
    To=cp.copy(T)


##for visualization
## for animation
ims=[]
fig=plt.figure(figsize=(8.0,8.0))
ax=fig.add_subplot(111)
ax.set_ylim(0, 1)
ax.set_xlim(0,1)
levels=np.linspace(TL,TH,11)
plt.gca().set_aspect('equal')
plt.title('Temperature distribution')
plt.xlabel('x/L')
plt.ylabel('y/L')
## time step position
xp=L*0
yp=L*(1.03)
for i in range(len(Ts)):
    tmOut='t=' + '{:.3f}'.format(i*dt*ST)
    txt = ax.text(xp/L, yp/L, str(tmOut), size=12, backgroundcolor='white')
    img = plt.contourf(x/L,y/L,Ts[i], cmap='Blues', levels=levels)
    ##bar label for figures
    if(len(ims) == 0):
       cbar=plt.colorbar(img)
       cbar.set_label('Temperature [K]')

    ##add animaiton
    ims.append(img.collections + [txt])

## animation draw
ani=an.ArtistAnimation(fig,ims, interval=100)
ani.save('explicit.gif', writer="imagemagick")
plt.show()

