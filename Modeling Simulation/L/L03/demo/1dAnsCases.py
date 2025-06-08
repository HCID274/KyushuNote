## python, 1d HCE, steady-state : (d^2t/dx^2 = -q/a with fixed B.C.)
## t: temperature, x: coordinate, q: heat loss [K/s], a: thermal diffusivity [m2/s]
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

##Case selection -> Give case as input parameter of "1dAns.py" from your console
if len(sys.argv) ==1:
  case="default"
else:
  case=sys.argv[1]

## definition
L    = 20.0    # cavity length [m] 
N    = 50     # number of girds [-]
dl   = L/N    # grid spacing [m]
TL   = 300.0  # low temperature  [K]
TH   = 1200.0  # high temperature [K]
crit = 0.0001   # criteria for convergence [K]

## values for aluminum
lm    = 209.5        # heat conduction [J/mKs]
rhoCp = 2.4*10.0**6  # volumetric specific heat [J/m3s]
alpha = lm/rhoCp     # thermal diffusivity [m2/s]

## for case 3
R  = 0.1   # Metal bar radius [10cm]
Ta = TL    # Ambient temperature [K]
h  = 2.0   # Heat transfer coefficient [W/m2s]

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
for i in range(1,N+1):
    ce[i] = 1.0/(0.5*(dx[i]+dx[i+1]))
    cw[i] = 1.0/(0.5*(dx[i]+dx[i-1]))
for i in range(1,N+1):
    if case == "case1" or case == "case2" : 
        ##for case 1 and 2
        co[i]=(ce[i]+cw[i])
    elif case == "case3":
        ##for case 3
        co[i]=(ce[i]+cw[i] + 2.0*h*dx[i]/lm/R)
    else: 
        print("Input case1, case2, or case 3")
        exit()


##t(x):temperature, tp(x):predicted temperature, q(x):heat loss
T          = np.zeros(N+2)
Tp         = np.zeros(N+2)
q          = np.zeros(N+2)

## define values
T[:]       = TL
## boudnary condition
T[0]    = TL
T[N+1]  = TH 
## initial prediction values
Tp[:]   = T[:]

##iteration loop
flg = 1 #control flag
l   = 0 #counter
while flg == 1:
   l+=1
   flg=0
   for i in range(1,N+1): 
       ##calculation
       if case=="case1":
           q[i]  = 0                     # Case 1
       elif case=="case2":
           q[i] = 2.0*lm*(TH-TL)/L**2    # Case 2 
       elif case=="case3":
           q[i] = -2.0*h*Ta/R            # Case 3
       T[i] = \
                ( ce[i] * Tp[i+1]\
                + cw[i] * Tp[i-1]\
                - q[i]/lm*dx[i]\
                )/co[i]
 
   ##convergence check
   for i in range(1,N+1):
       if(np.abs(T[i]-Tp[i])>crit):
           flg=1 #calculate again until reaching the converged values
             
   if(np.mod(l,10) == 0):  
       print(l)
   ##for debug
   #print(T)
   #print(tp)
   #print(q)
   #input()  
   Tp[:]=T[:]

## theoretical solution 
Tth = np.zeros(N+2)
if case=="case1":
    ##Case 1
    Tth = (TH-TL)/L * (x-L) + TH 
elif case=="case2":
    ##Case 2
    Tth = (TH-TL)*(x/L)**2 + TL
elif case=="case3":
    ##Case3
    A=np.sqrt(2.0*h/lm/R)
    dTH=TH-Ta
    dTL=TL-Ta
    de=np.exp(A*L)-np.exp(-A*L)
    Tth = Ta + dTH * (np.exp(A*x) - np.exp(-A*x))/de

## visualization & save image
fig = plt.figure(figsize=(6.0,6.0))
ax = fig.add_subplot(1,1,1)
## temperature distribution by numerical simulation
img = plt.plot(x, T, label='t', color='red')
## temperature distribution by theoretical solution
img = plt.plot(x, Tth, label='theo.', color='black', linestyle='dashed')
#plt.gca().set_aspect('equal')
plt.title('Temperature distribution')
plt.xlabel('x [m]')
plt.ylabel('T [K]')
ax.set_xlim(0,L)
ax.set_ylim(TL,TH)
ax.grid()
#plt.show()
fn=case + '.png'
fig.savefig(fn)
