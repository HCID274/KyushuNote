## python, steady-state 2d hce : d^2T/dx^2 + d^2T/dy^2 = -sphi 
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
##########################################################################
## Q1 (line 48) : Define coefficient ce, cw, cn, and cs.
## Q2 (line 88) : Write equation to determine T[j,i] from Tp, ce, cw, cn cs, and co.
## Q3 (line 95) : For case 3, write appropriate boundary conditions.
###### advanced #####
## Q4 : Re-write the code from Jacobi method to Gauss-Seidel method 
## Q5 : Re-write the code for Case 2 (hint: Update BC)
## Q6 : Re-write the code for Case 3 (hint: Update BC)
##########################################################################

## definition
L    = 1.0    #cavity length [m] 
N    = 20     #number of girds [-]
dl   = L/N    #grid spacing [m]
TL   = 300.0  #low temperature  [K]
TH   = 500.0  #high temperature [K]
crit = 0.001   #criteria for convergence [K]

## values for water
lm    = 0.6          # heat conductivity [J/mKs]
rhoCp = 4.182*1.25   # volumetric specific heat [J/m3s]
alpha = lm/rhoCp     # thermal diffusivity [m2/s]
h     = 0.15         # heat transfer coefficient [J/m2sK] used for case 3 

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
######### Q1: Define coefficients ce, cw, cn and cs. Dummy values are inserted ##########
for i in range(1,N+1):
    for j in range(1,N+1):
        ce[i] = 1.0
        cw[i] = 1.0
        cn[j] = 1.0
        cs[j] = 1.0
##define co
for j in range(1,N+1):
    for i in range(1,N+1):
        co[j,i]=(ce[i]+cw[i]+cn[j]+cs[j])

##T(y,x):temperature, Tp(y,x):predicted temperatue
T            = np.zeros((N+2,N+2))
T[:,:]       = TL
##boudnary condition
##T[j,i] : (j,i) is indices for (y,x)
##case 1
T[N+1,:] = TH # top at y=L
T[0,:]   = TL # bottom at y=0
T[:,0]   = TL # side at x=0
T[:,N+1] = TL # side at x=L
##initial prediction values
Tp=cp.copy(T)

##sink term
Sphi=np.zeros((N+2,N+2))
Sphi[:,:] = 1.0 

##iteration loop
flg = 1 #control flag
l   = 0 #counter
while flg == 1:
   l+=1
   flg=0

   ########## Q2: Write equation to determine T[j,i] from Tp, ce, cw, cn cs, and co. ###########
   for j in range(1,N+1): 
       for i in range(1,N+1): 
           ##calculation
           ##Jacob scheme --> Dummy equation is written.
           T[j,i] = Tp[j,i]

   ########## Q3: For case 3, write appropriate boundary conditions ##########
   #T[1:N+1,0] =   1.0 
   #T[0,1:N+1] =   1.0 
   #T[1:N+1,N+1] = 1.0
   #T[N+1,1:N+1] = 1.0

   ##convergence check
   #for j in range(0,N+2): 
   for j in range(1,N+1): 
       #for i in range(0,N+2):
       for i in range(1,N+1):
           if(np.abs(T[j,i]-Tp[j,i])>crit):
               ##debug
               #print(i, j, T[j,i], Tp[j,i])
               flg=1 #calculate again until reaching the converged values
                 
   if(np.mod(l,10) == 0):  
       print(l)
   ##for debug
   #print(t)
   #print(tp)
   #tp=cp.copy(t)
   Tp[:,:]=T[:,:]

## visualization & save image
levels=np.linspace(TL,TH,41)
fig=plt.figure(figsize=(6.0,6.0))
img=plt.contourf(x/L,y/L,T, cmap="Blues",levels=levels)
plt.gca().set_aspect('equal')
cbar=plt.colorbar(img)
cbar.set_label('Temperature [oC]')
plt.title('Temperature distribution')
plt.xlabel('x/L [-]')
plt.ylabel('y/L [-]')
plt.grid()
plt.show()
fig.savefig('2d.png')
