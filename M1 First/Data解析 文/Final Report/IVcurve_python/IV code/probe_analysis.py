# Data解析 文\Final Report\IVcurve_python\IV code\probe_analysis.py
import numpy as np
import scipy as sp
import sys
from scipy.optimize import curve_fit
import math
import sympy as syp

def sweep_sort(time,sweep,raw,npoint):
    """
    This function reshapes and sorts time series data for the analysis of the iv curve.

    Parameters
    ----------
    time : 1D-array
        Time for sigs
    sweep : 1D-array
        Time series of sweep voltage
    raw : 1D-array
        Time series of probe current
    npoint : int
        Length of each sweep (2pi).

    Returns
    -------
    time_mid : 1D-array
       Time in the middle of iv curve
    sweep : 2D-array
       Reshaped sweep voltage divided for each curve.  (vmin-vmax).
    raw : 2D-array
       Probe currents divided for each curve.
    """
 
    sind=np.argmin(sweep[0:npoint]) #argmin >> is find index number of smallest value in array' To find -75V`s index During in first time sweep!
    eind=npoint-sind #To find final -75V`s index During in toal time sweep!
    time=time[sind:-eind] #Using completely time cycle(28times) during in 0.2s~0.5S
    raw=raw[sind:-eind] # All raw data of 28timse cycle in toal time!
    sweep=sweep[sind:-eind] #All sweep data of 28timse cycle in toal time!

    npoint_half=int(npoint/2) #-75V to 75V (half sweep) is 10,000point
    nsweep=int(len(sweep)/npoint_half) # calculate How many times half sweep, ex) 100,000 data / npoint is # of cycle

    time =np.reshape(time,[nsweep,npoint_half]) # nsweep is NUMBER OF ROWS, npoint_half is NUMBER OF COLOUMNS and we can access it by time[13][3980]            len(time) is 28 because, during in 0.2s~0.5S it can about 30 tims sweep!
    raw  =np.reshape(raw,[nsweep,npoint_half]) #Reshape for raw[0][9999] to raw[27][9999]
    sweep=np.reshape(sweep,[nsweep,npoint_half])#Reshape for sweep[0][9999] to raw[27][9999]

    time_mid=np.empty([nsweep])

    for it in range(0,len(raw),1):
        time_mid[it]=np.median(time[it,:]) #put in data of median time, to time[], To equal interval step up 0.01s.   
        if it%2==0:    #se it è pari
            continue
        else:
            sweep[it,:]=sweep[it,::-1] #if return (75V to -75) put in revers sequence data that is same to -75V to 75   , sweep -> sweep[0][9999]~sweep[27][9999], during in half sweep, npoint is 10,000
            raw[it,:]  =raw[it,::-1] #if return (75V to -75) put in revers sequence data that is same to -75V to 75, raw -> raw[0][9999]~sweep[27][9999], during in half sweep, npoint is 10,000

    return  time_mid, sweep, raw,nsweep

def linear_fit(vp,a,b):  #To fit linear function. except saturation value, gragh looks like linear func 
    return   a*vp + b

def te_fit(vp,a,b):
    return   vp/a + b  #Because Te is reciprocal number of gradient electron current

def floating(sweep, raw, verbose=True): # 1. 添加 verbose=True 参数
    """
    This function returns floating poteintial

    Parameters
    ----------
    sweep : 1D-array
        Time series of sweep voltage
    raw : 1D-array
        Time series of probe current
    verbose : bool, optional
        If True, prints the calculated floating potential. Default is True.

    Returns
    -------
    floating : float
       floating potential[V]
    """
    ind = np.argmin(np.abs(raw - 0.0)) # Floating potential is point of zero plasma current
    vf = sweep[ind] # voltage that become point of zero plasma current
    
    if verbose: # 2. 根据 verbose 的值来决定是否打印
        print() # 这几个空 print 看起来是为了格式化输出，可以保留在 verbose 条件内或移出
        print()
        print()
        print()  
        print("Vf = {} [V]".format(vf)) 
    return vf


def fit_ion_current(sweep,raw,vmin,vmax): # In this step, raw and sweep is changed single data
    """
    This function returns ion current.

    Parameters
    ----------

    sweep : 1D-array
        Time series of sweep voltage
    raw : 1D-array
        Time series of probe current
    vmin,vmax : float
        Fitting range (voltage)

    Returns
    -------
    i_ion: 1D-array
       Fitting ion_current
    """

    ind1=np.argmin(np.abs(sweep-vmin)) #Pick start point voltage of Saturation ion current. in V<0 case , electron current can't diagnostic, so anywhere is okay
    ind2=np.argmin(np.abs(sweep-vmax)) # vmax = 0, in theory,  in V>0 case , ion current can't diagnostic
    sweep_fit=sweep[ind1:ind2+1] #redfine sweep range
    raw_fit=raw[ind1:ind2+1] #redfine raw data range

    popt,pcov=curve_fit(linear_fit,sweep_fit,raw_fit)
    i_ion=popt[0]*sweep+popt[1] #a first-order function   #HERE WE FIND THE ION CURRENT (TAHT WE SUBSTRACT TO TOTAL CURRENT) POINT BY POINT 
                                                         
    return i_ion



def fit_te(sweep,ie,vmin,vmax):
    """
    This function returns Te [eV].

    Parameters
    ----------

    sweep : 1D-array
        Time series of sweep voltage
    ie : 1D-array
        Time series of electron current
    imin,imax : float
        Fitting range of electron current [mA]

    Returns
    -------
    te : float
       electron temperature [eV]
    b : y-intercept of te fitting
    """

    # ind1=np.argmin(np.abs(ie-imin*1e-3)) #1e-3 is Using for [mA]   since ie[5580] , ie is increas that look like about 10mA <- bigger than 0V
    # ind2=np.argmin(np.abs(ie-imax*1e-3))
    ind1 = np.argmin(np.abs(sweep - vmin))
    ind2 = np.argmin(np.abs(sweep - vmax))
    sweep_fit=sweep[ind1:ind2+1] #redfine sweep range
    ie_fit=ie[ind1:ind2+1] #redfine raw data range

    popt,pcov=curve_fit(te_fit,sweep_fit,np.log(ie_fit))      # FOR THE TRANSITORY PART FITTING IN LOGARHITMIC SCALE 
    te=popt[0] # variable 'a' in Te_fit that is slope of func
    b=popt[1] #variable 'b' in Te_fit that is y-intercept of func
    
    print()
    print("Te={}[eV]".format(te)) 
    
    # if te>=4.0:                               
    #     print("error!!! change fitting range")
    #     sys.exit()

    return te,b


# def fit_te(sweep,ie,imin,imax):       #SAME FITTING FOR THE ELECTRON TEMPERATURE BUT HERE WE CHOOSE THE FITTING INTERVAL ON THE CURRENT AXIS (y) AND NOT ON THE VOLTAGE AXIS (x)
#     """
#     This function returns Te [eV].

#     Parameters
#     ----------

#     sweep : 1D-array
#         Time series of sweep voltage
#     ie : 1D-array
#         Time series of electron current
#     imin,imax : float
#         Fitting range of electron current [mA]

#     Returns
#     -------
#     te : float
#        electron temperature [eV]
#     b : y-intercept of te fitting
#     """

#     ind1=np.argmin(np.abs(ie-imin*1e-3)) #1e-3 is Using for [mA]   since ie[5580] , ie is increas that look like about 10mA <- bigger than 0V
#     ind2=np.argmin(np.abs(ie-imax*1e-3))
#     sweep_fit=sweep[ind1:ind2+1] #redfine sweep range
#     ie_fit=ie[ind1:ind2+1] #redfine raw data range

#     popt,pcov=curve_fit(te_fit,sweep_fit,np.log(ie_fit))      #PER IL FITTING DELLA PARTE TRANSITORIA IN SCALA LOGARITMICA
#     te=popt[0] # variable 'a' in Te_fit that is slope of func
#     b=popt[1] #variable 'b' in Te_fit that is y-intercept of func
#     print("Te={}[eV]".format(te)) 

#     # if te>=4.0:                                    #????  #NB L'HO RESO IO COMMENTO ALTRIMENTI A 20mm MI DA ERRORE PERCHE LA T ESPLODE. MA DOVREBBE ESSERE UN PROBLEMA DEL SISTEMA DI MISURA
#     #     print("error!!! change fitting range")
#     #     sys.exit()

#     return te,b



def fit_vs(sweep,ie,te,te_b,vmin,vmax):
    """
    This function returns space potential by fitting.

    Parameters
    ----------

    sweep : 1D-array
        Time series of sweep voltage
    ie : 1D-array
        Time series of electron current
    vmin,vmax : float
        Fitting range of probe voltage [V]

    Returns
    -------
    Vs : float
       Space potential [V]
    ie_fit : 1D-array
       Fitting line of Ie
    te_fit : 1D-array
       Fitting line of Te

    """

    te_fit=np.exp(sweep/te+te_b) # why use exp func-> in fit_te, te is calculated by log scale  

    ind1=np.argmin(np.abs(sweep-vmin)) #Pick start point voltage of Saturation current
    ind2=np.argmin(np.abs(sweep-vmax)) #Pick start point voltage of Saturation current
    sweep_fit=sweep[ind1:ind2+1] #redfine sweep range
    ie_fit=ie[ind1:ind2+1] #redfine raw data range
    popt,pcov=curve_fit(linear_fit,sweep_fit,np.log(ie_fit))
    ie_fit=np.exp(sweep*popt[0]+popt[1])

    ind_vs=np.argmin(np.abs(te_fit-ie_fit)) # cross point 
    vs = sweep[ind_vs]
    print("Vs={}[V]".format(vs))

    return vs,ie_fit,te_fit


def diff_poly(fit0_1mm,diff_sweep,poly_value,sweep):
    x= syp.symbols('x')
  
    poly_range = list(range(poly_value+1))
    f=0
    for i in poly_range:
        order=poly_value-i
        f+=fit0_1mm[i]*x**order
        
    diff_f = syp.diff(f, x)
    t=diff_sweep
    s = diff_f.subs(x,t)
 
    
    

    print("At {}[V]`s momentary Te={}[eV]".format(t,1/s))
    return s

def tangent_line(slope,diff_sweep,sweep,ie): #To fit linear function. except saturation value, gragh looks like linear func 
     vind=np.argmin(np.abs(sweep-diff_sweep)) #Pick start point voltage of Saturation current
     cind=np.argmin(np.abs(sweep-diff_sweep))
 
     y = slope*(sweep-sweep[vind])+ie[cind]
     return y
 
    
 
    