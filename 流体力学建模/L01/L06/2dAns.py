## python, steady-state 2d hce : d^2T/dx^2 + d^2T/dy^2 = -sphi 
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
import sys

##Case selection -> Give case as input parameter of "1dAns.py" from your console
##for case selection
case = "case1"
#if len(sys.argv) ==1:
#  case="default"
#else:
# case=sys.argv[1]

## definition
L    = 1.0    #cavity length [m] 
N    = 20     #number of girds [-]
dl   = L/N    #grid spacing [m]
TL   = 300.0  #low temperature  [K]
TH   = 500.0  #high temperature [K]
crit = 0.0001   #criteria for convergence [K]

## values for water
lm    = 0.6
rhoCp = 4.182*1.25   # volumetric specific heat [J/m3s]
alpha = lm/rhoCp     # thermal diffusivity [m2/s]
h     = 0.15         # heat transfer coeff. [W/m2] -- for case 3 

## grid
x  = np.zeros(N+2)
#x  = np.arange(N+2)
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

if case == "case3": 
    h = 10.0
    ht = h
    hb = h
    hs = h 
    #hb = h/10.0
    #hs = h/5.0
    ctop  =  lm/ht/0.5/dl
    cbottom =lm/hb/0.5/dl
    cside =  lm/hs/0.5/dl

## coefficient
ce=np.zeros(N+1)
cw=np.zeros(N+1)
cn=np.zeros(N+1)
cs=np.zeros(N+1)
co=np.zeros((N+1,N+1)) #for 2D
######### Q1: define coefficient  -- dummy values are inserted ##########
for i in range(1,N+1):
    for j in range(1,N+1):
        ce[i] = lm*dy[j]/(0.5*(dx[i]+dx[i+1]))
        cw[i] = lm*dy[j]/(0.5*(dx[i]+dx[i-1]))
        cn[j] = lm*dx[i]/(0.5*(dy[j]+dy[j+1]))
        cs[j] = lm*dx[i]/(0.5*(dy[j]+dy[j-1]))

for j in range(1,N+1):
    for i in range(1,N+1):
        co[j,i]=(ce[i]+cw[i]+cn[j]+cs[j])

##T(y,x):temperature, Tp(y,x):predicted temperatue
T            = np.zeros((N+2,N+2))
T[:,:]       = TL
##boudnary condition
##T[j,i]

if case =="case1": ##case 1
    T[N+1,:] = TH # top
    T[0,:]   = TL # bottom
    T[:,0]   = TL # side
    T[:,N+1] = TL # side
elif case == "case2" :
##case 2
    T[N+1,:] = TL # top
    T[0,:]   = TL
    T[:,0]   = TH
    T[:,N+1] = TH
##initial prediction values
Tp=cp.copy(T)

##sink term
Sphi=np.zeros((N+2,N+2))
if case=="case1" or case=="case2":
    Sphi[:,:]=0.0
elif case=="case3" :
    #Sphi[:,:] = rhoCp*50.0/3600.0
    Sphi[:,:] = 500.0 

##iteration loop
flg = 1 #control flag
l   = 0 #counter
while flg == 1:
   l+=1
   flg=0
   
   ##########Q2: Write equation to determine T[j,i] by Tp[:,:] and ce, cw, cn, cs, co
   for j in range(1,N+1): 
       for i in range(1,N+1): 
           ##calculation
           ##Jacob scheme
           T[j,i] = 1/co[j,i]* (ce[i]*Tp[j,i+1] + cw[i]*Tp[j,i-1] + cn[j]*Tp[j+1,i] + cs[j]*Tp[j-1,i] - Sphi[j,i]*dx[i]*dy[j]) 
   if case == "case3" :
       ##boundary
       T[1:N+1,0] =   (cside   * Tp[1:N+1,1] + TH)/(cside + 1.0)
       T[0,1:N+1] =   (cbottom * Tp[1,1:N+1] + TH)/(cbottom + 1.0)
       T[1:N+1,N+1] = (cside   * Tp[1:N+1,N] + TH)/(cside + 1.0)
       T[N+1,1:N+1] = (ctop    * Tp[N,1:N+1] + TH)/(ctop + 1.0)
 
   ##convergence check
   for j in range(0,N+2): 
   #for j in range(1,N+1): 
       for i in range(0,N+2):
       #for i in range(1,N+1):
           if(np.abs(T[j,i]-Tp[j,i])>crit):
               ##debug
               #print(i, j, T[j,i], Tp[j,i])
               flg=1 #calculate again until reaching the converged values
                 
   if(np.mod(l,100) == 0):  
       print(l)
   ##for debug
   #print(t)
   #print(tp)
   #tp=cp.copy(t)
   Tp[:,:]=T[:,:]

## visualization & save image
levels=np.linspace(TL,TH,11)
fig=plt.figure(figsize=(8.0,8.0))
img=plt.contourf(x/L,y/L,T, cmap="Blues",levels=levels)
#img=plt.contourf(x[1:N+1],y[1:N+1],T[1:N+1,1:N+1]-273.15, cmap="Blues")
plt.gca().set_aspect('equal')
cbar=plt.colorbar(img)
cbar.set_label('Temperature [K]')
plt.title('Temperature distribution')
plt.xlabel('x/L [-]')
plt.ylabel('y/L [-]')
#plt.grid()
#plt.show()
#fig.savefig('2d.png')
fn=case + '.png'
fig.savefig(fn)

