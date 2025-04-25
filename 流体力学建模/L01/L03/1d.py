## python, 1d HCE, steady-state : (d^2T/dx^2 = -q/a with fixed B.C.)
## T: temperature, x: coordinate, q: heat loss [K/s], a: thermal diffusivity [m2/s]
import copy as cp
import numpy as np
import matplotlib.pyplot as plt

##Consider following questions##############################################################
## Q1 (line 38): Think the meaning next two lines##
## Q2 (line 61): Write appropriate BC and IC for T and Tp. "0 is dummy value"
## Q3 (line 70): Add comments of meaning of next loop
## Q4 (line 74): Add comments of meaming of next loop
## Q5 (line 77): Define an appropriate value of q for case 1, 2, 3
## Q6 (line 79): Write correct equation to calculate T[i] using ce, cw, co, and q. The next lines are dummy.
## Q7 (line 86): Before reaching this line, what is the values of "flg"?
## Q8 (line 87): When flg becomes 1?
############################################################################################

## definition
L    = 1.0    # cavity length [m] 
N    = 20     # number of girds [-]
dl   = L/N    # grid spacing [m]
TL   = 300.0  # low temperature  [K]
TH   = 500.0  # high temperature [K]
crit = 0.01   # criteria for convergence [K]

## values for aluminum
lm    = 209.5      # heat conduction [J/mKs]
rhoCp = 2.4*10**6  # volumetric specific heat [J/m3s]
alpha = lm/rhoCp   # thermal diffusivity [m2/s]

## grid
x  = np.zeros(N+2)
dx = np.zeros(N+2)
x[0]      = 0.0 
dx[0]     = 0.0
dx[N+1]   = 0.0
dx[1:N+1] = dl ## Note that 1 to N, but not N+1 in python

## Q1: Think the meaning next two lines##
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
    co[i]=(ce[i]+cw[i])

##T(x):temperature, Tp(x):predicted temperature, q(x):heat loss
T          = np.zeros(N+2)
Tp         = np.zeros(N+2)
q          = np.zeros(N+2)

## Q2: Write appropriate BC and IC for T and Tp. "0 is dummy value"
T[:]    = 0 
T[0]    = 0
T[N+1]  = 0 
Tp[:]   = 0

##iteration loop
flg = 1 #control flag
l   = 0 #counter
## Q3: Add comments of meaning of next loop
while flg == 1:
   l+=1
   flg=0
   ## Q4: Add comments of meaming of next loop
   for i in range(1,N+1): 
       ##calculation
       ## Q5: Define an appropriate value of q for case 1, 2, 3
       q[i]  = 0
       ## Q6: Write correct equation to calculate T[i] using ce, cw, co, and q. The next lines are dummy.
       T[i] = \
                ( 1.0 * Tp[i+1]\
                + 1.0 * Tp[i-1]\
                - 1.0 * q[i]\
                )/1.0
 
   ## Q7: Before reaching this line, what is the values of "flg"?
   ## Q8: When flg becomes 1?
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
## case 1
Tth = (TH-TL)/L * (x-L) + TH 

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
plt.show()
fig.savefig('1dhce.png')
