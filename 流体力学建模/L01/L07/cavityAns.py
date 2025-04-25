## python, NS equation by smac method for cavity flow
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
import sys

##argument from command line
args = sys.argv

Re=float(args[1])
#Re   = 1000.0    #Reynolds number = nu ut/L1## definition
N    = 20     #number of girds [-]
nu   = 1.5e-5 #kinetic viscosity [m2/s]
ut   = 1.0    #BC
L    = nu*Re/ut #cavity length [m]
dl   = L/N    #grid spacing [m]
r    = 0.1    #diffusion number < 1/4 for 2D
cou  = 0.25   #courant number [-] > 1.0 for explicit scheme
dtd  = r/nu*dl**2 #dt
dta  = cou*dl/ut
dt   = min(dtd,dta)
## for calculation control
NO   = 1000      #time step
ST   = 10        #file num per time step
crit = 1.0e-3   #criteria for convergence [Pa]
#crit = 1.0e-8   #criteria for convergence [Pa]

## info.
print('Conditions:  ')
print('   Reynolds number: ' + str(Re))
print('   dl: ' + str(dl))
print('   dt: ' + str(dt))
print('   L: ' + str(L))

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

## variables
## u(y,x), v(y,x), p(y,x)
u  = np.zeros((N+2,N+2))
v  = np.zeros((N+2,N+2))
p  = np.zeros((N+2,N+2))
pn  = np.zeros((N+2,N+2))
u[:,:] = 0.0
v[:,:] = 0.0
p[:,:] = 0.0
pn[:,:]=0.0
## boudnary condition
u[N+1,1:N] = ut 
uo=cp.copy(u)
vo=cp.copy(v)
ui=cp.copy(u)
vi=cp.copy(v)
pp=cp.copy(p)

## coefficient u[j,i]->[1:N,2:N], v[j,i]->[2:N, 1:N]
cuw=np.zeros((N+1,N+1))
cue=np.zeros((N+1,N+1))
cus=np.zeros((N+1,N+1))
cun=np.zeros((N+1,N+1))
cud=np.zeros((N+1,N+1))
cuo=np.zeros((N+1,N+1))
cvw=np.zeros((N+1,N+1))
cve=np.zeros((N+1,N+1))
cvs=np.zeros((N+1,N+1))
cvn=np.zeros((N+1,N+1))
cvd=np.zeros((N+1,N+1))
cvo=np.zeros((N+1,N+1))
#diffusion
auw=np.zeros(N+1)
aue=np.zeros(N+1)
aus=np.zeros(N+1)
aun=np.zeros(N+1)
avw=np.zeros(N+1)
ave=np.zeros(N+1)
avs=np.zeros(N+1)
avn=np.zeros(N+1)
#advection
fuw=np.zeros((N+1,N+1))
fue=np.zeros((N+1,N+1))
fus=np.zeros((N+1,N+1))
fun=np.zeros((N+1,N+1))
fvw=np.zeros((N+1,N+1))
fve=np.zeros((N+1,N+1))
fvs=np.zeros((N+1,N+1))
fvn=np.zeros((N+1,N+1))
## poisson eq. p[j,i]->[1:N, 1:N]
cw=np.zeros(N+1)
ce=np.zeros(N+1)
cs=np.zeros(N+1)
cn=np.zeros(N+1)
cd=np.zeros((N+1,N+1)) 

##fixed coefficient au[j direc.], av[i direc.]
##for u, v, diffusion
auw[:]=nu
aue[:]=nu
aus[:]=nu
aun[:]=nu
aus[1]=2.0*nu
aun[N]=2.0*nu
avw[:]=nu
ave[:]=nu
avs[:]=nu
avn[:]=nu
avw[1]=2.0*nu
ave[N]=2.0*nu
##for u, v, storage
cuo[:,:] = dl**2/dt
cvo[:,:] = dl**2/dt
##for p
cw[:]=1.0
ce[:]=1.0
cs[:]=1.0
cn[:]=1.0
for i in range(1,N+1):
    for j in range(1,N+1):
        cd[j,i]=(ce[i]+cw[i]+cn[j]+cs[j])

## time step loop
##for store
Us=[]
Vs=[]
Ps=[]
for n in range(NO):
    print('time=' + str(n))
    #n+=1
    flgt=0
    ## u, v calculation
    ## update coefficient in every time step
    for i in range(1,N+1):
        for j in range(1,N+1): 
            fuw[j,i] = 0.5* (uo[j,i]  +uo[j,i-1])    * dl  
            fue[j,i] = 0.5* (uo[j,i]  +uo[j,i+1])    * dl 
            fus[j,i] = 0.5* (vo[j,i]  +vo[j,i-1])    * dl  
            fun[j,i] = 0.5* (vo[j+1,i]+vo[j+1,i-1])  * dl  
     
            fvw[j,i] = 0.5* (uo[j,i]  +uo[j-1,i])    * dl  
            fve[j,i] = 0.5* (uo[j,i+1]+uo[j-1,i+1])  * dl 
            fvs[j,i] = 0.5* (vo[j,i]  +vo[j-1,i])    * dl  
            fvn[j,i] = 0.5* (vo[j,i]  +vo[j+1,i])    * dl  
            
            cuw[j,i] = auw[j] + 0.5*fuw[j,i]       
            cue[j,i] = aue[j] - 0.5*fue[j,i]       
            cus[j,i] = aus[j] + 0.5*fus[j,i]       
            cun[j,i] = aun[j] - 0.5*fun[j,i]       
   
            cvw[j,i] = avw[i] + 0.5*fvw[j,i] 
            cve[j,i] = ave[i] - 0.5*fve[j,i] 
            cvs[j,i] = avs[i] + 0.5*fvs[j,i] 
            cvn[j,i] = avn[i] - 0.5*fvn[j,i] 

    cud[:,:] = cuw[:,:] + cue[:,:] + cus[:,:] + cun[:,:]\
              -fuw[:,:] + fue[:,:] - fus[:,:] + fun[:,:] 
    cvd[:,:] = cvw[:,:] + cve[:,:] + cvs[:,:] + cvn[:,:]\
              -fvw[:,:] + fve[:,:] - fvs[:,:] + fvn[:,:] 
    for i in range(1,N+1):
        for j in range(1,N+1):
            ## equation to determine u, v
            u[j,i] = (\
                      cuw[j,i]*uo[j,i-1] + cue[j,i]*uo[j,i+1]\
                     +cus[j,i]*uo[j-1,i] + cun[j,i]*uo[j+1,i]\
                     + (cuo[j,i]-cud[j,i])*uo[j,i]\
                     + (p[j,i-1]-p[j,i])*dl\
                     )/cuo[j,i]
            v[j,i] = (\
                      cvw[j,i]*vo[j,i-1] + cve[j,i]*vo[j,i+1]\
                     +cvs[j,i]*vo[j-1,i] + cvn[j,i]*vo[j+1,i]\
                     + (cvo[j,i]-cvd[j,i])*vo[j,i]\
                     + (p[j-1,i]-p[j,i])*dl\
                     )/cvo[j,i]
    ##BC update because of overwriting at i=1 and j=1
    u[:,1]=0.0
    v[1,:]=0.0
    ## for debug
    #print(u)
    #print(v)
    #input()

    ## p iteration loop
    pn=cp.copy(p)
    ##To eliminate previous step. --> When tolerance level (crit is small) is very strict, 
    ##initial values of pp does not affect the converged values of pp, but it's not when
    ##crit is set small. In such cases, use constant value; otherwise, temporal oscilaiton occurs.
    pp[:,:]=0.0
    flg = 1 #control flag
    l   = 0 #counter
    while flg == 1:
       l+=1
       flg=0
       ##BC -- Caution: N+1 not included in python
       p[1:N+1,0] = pp[1:N+1,1]
       p[0,1:N+1] = pp[1,1:N+1]
       for i in range(1,N+1): 
           for j in range(1,N+1): 
               ##Gauss-Seidel scheme
               p[j,i] = \
                        ( cw[i] * p[j,i-1]\
                        + ce[i] * pp[j,i+1]\
                        + cs[j] * p[j-1,i]\
                        + cn[j] * pp[j+1,i]\
                        #Jacobi scheme
                        #( cw[i] * pp[j,i-1]\
                        #+ ce[i] * pp[j,i+1]\
                        #+ cs[j] * pp[j-1,i]\
                        #+ cn[j] * pp[j+1,i]\
                        - (( u[j,i+1] - u[j,i] ) *dl \
                          +( v[j+1,i] - v[j,i] ) *dl )/dt\
                        )/cd[j,i]
       #BC, GS scheme --Caution:  N+1 not included in python
       p[1:N+1,N+1] = p[1:N+1,N]
       p[N+1,1:N+1] = p[N,1:N+1]
     
       ##convergence check
       for i in range(0,N+2):
           for j in range(0,N+2): 
               if(np.abs(p[j,i]-pp[j,i])>crit):
                   flg=1 #calculate again until reaching the converged values
                     
       if(np.mod(l,100) == 0):  
           print('     itr=' + str(l))
           ##for debug
           #print(p)

       ## update val.
       pp=cp.copy(p)
    
    ##vel. correction
    for i in range(2,N+1):
        u[1:N,i] = u[1:N,i] - dt*(p[1:N,i]-p[1:N,i-1])/dl 
        v[i,1:N] = v[i,1:N] - dt*(p[i,1:N]-p[i-1,1:N])/dl
    ##pressure update
    p[:,:]=pn[:,:]+p[:,:]

    ## update data
    uo=cp.copy(u)
    vo=cp.copy(v)

    ##interpolation 
    for i in range(1,N+1):
        for j in range(1,N+1):
            ui[j,i] = 0.5*(u[j,i]+u[j,i+1])   
            vi[j,i] = 0.5*(v[j,i]+v[j+1,i])   

    ##store data for animation
    if(np.mod(n,ST)==0):
        #print('time=' + str(n))
        tmp=cp.copy(ui)
        Us.append(tmp)
        tmp=cp.copy(vi)
        Vs.append(tmp)
        tmp=cp.copy(p)
        Ps.append(tmp)

## visualization & save image every NOF step
ims=[]
fig=plt.figure(figsize=(8.0,8.0))
ax=fig.add_subplot(111)
ax.set_ylim(0,1)
ax.set_xlim(0,1)
levelsp=np.linspace(-0.4,0.4,11) ## for p
levelsu=np.linspace(0,ut,11)      ## for u, v
#levelsu=np.linspace(-ut,ut,11)      ## for u, v
plt.gca().set_aspect('equal')
plt.title('Velocitydistribution')
plt.xlabel('x/L')
plt.ylabel('y/L')
## time step position
xp=L*0
yp=L*(1.03)
for i in range(len(Us)):
    ui=Us[i]
    vi=Vs[i]
    p=Ps[i]
    uMag=np.sqrt(ui**2+vi**2)
    txt = ax.text(xp/L, yp/L, 'timestep=' + str(i*ST), size=12, backgroundcolor='white')
    #cnt=plt.contourf(x/L,y/L, u, cmap='bwr', levels=levelsu) ##vel
    cnt=plt.contourf(x/L,y/L, uMag, cmap='Blues', levels=levelsu) ##vel
    #cnt=plt.contourf(x/L,y/L,p, cmap='bwr', levels=levelsp) ##p
    vec=plt.quiver(x/L, y/L, ui, vi, color='red')
    ##bar label for figures
    if(len(ims) == 0):
       cbar=plt.colorbar(cnt)
       cbar.set_label('Vel. magnitude [-]')
       #cbar.set_label('p [-]')

    ##add animaiton
    ims.append(cnt.collections + [vec]+ [txt])

## animation draw
ani=an.ArtistAnimation(fig, ims, interval=100)
fn= str(Re) + '.gif'
ani.save(fn, writer="imagemagick")
plt.show()

