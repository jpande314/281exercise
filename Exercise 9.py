import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from scipy.integrate import odeint 


def one():
    gl = 1
    m = 1
    theta0 = pi/6
    omega0 = 0

    def fd(vec,t):
        omega,theta = vec 
        dtheta_dt = omega
        domega_dt = -gl*theta
        return domega_dt,dtheta_dt 
    
    t = np.linspace(0,10,1000)
    omg_the = odeint(fd,(omega0,theta0),t) 

    plt.plot(t,omg_the[:,0], label = 'theta')
    plt.plot(t,omg_the[:,1], label = 'omega')
    plt.title('theta, omega vs t')
    plt.legend()
    plt.figure()
    plt.plot(omg_the[:,0],omg_the[:,1], label = 'omg vs the')
    plt.title('omg vs theta')
    plt.legend()
    plt.show()
#one()
def two(): 
    g = 9.8
    m = 1
    l = 1

    n = 200
    tmax = 5
    h = tmax/n

    sig = np.zeros([n])
    th = np.zeros([n])
    t = np.linspace(0,tmax,n)

    sig0 = pi
    th0 = 0
    t0 = 0

    

    sig[0] = sig0
    th[0] = th0

    def fd(vec, t):
        sig,th = vec
        d_th = sig
        d_sig = -g/l*sin(th)
        return d_th,d_sig

    """for j in range(1, n):
        sig_th = [sig0, th0]
        time = h*(j-1)

        sig_mid = sig0 + (h/2) * fd(sig_th, time)[0]
        th_mid = th0 + (h/2) * fd(sig_th, time)[1]
        tmid = time + (h/2)
        sig_th_mid = [sig_mid, th_mid] 

        sig[j] = sig0 + h * fd(sig_th_mid, tmid)[0]
        th[j] = th0 + h * fd(sig_th_mid, tmid)[1]
        sig0, th0 = sig[j], th[j] """
        
    plt.plot(t,sig,label='Sigma')
    plt.plot(t,th,label='Theta')
    plt.xlabel('Time(s)')
    plt.legend()
    plt.figure()

    sig0 = linspace(0,10,50)
    th0 = 0
    t0 = 0

    


    def fd(vec, t):
        sig,th = vec
        d_th = sig
        d_sig = -g/l*sin(th)
        return d_th,d_sig

    """for sig0 in sig0: #plotting 50 sig plots vs t
        sig[0] = sig0
        th[0] = th0
        for j in range(1, n):
            sig_th = [sig0, th0]
            time = h*(j-1)

            sig_mid = sig0 + (h/2) * fd(sig_th, time)[0]
            th_mid = th0 + (h/2) * fd(sig_th, time)[1]
            tmid = time + (h/2)
            sig_th_mid = [sig_mid, th_mid]

            sig[j] = sig0 + h * fd(sig_th_mid, tmid)[0]
            th[j] = th0 + h * fd(sig_th_mid, tmid)[1]
            sig0, th0 = sig[j], th[j] 
        plt.plot(t,sig)"""

    #plt.figure()

    for sig0 in sig0: #plotting 50 th plots vs theta
        print(sig0)
        sig = np.zeros([n])
        th = np.zeros([n])
        sig[0] = sig0
        th[0] = th0
        for j in range(1, n):
            sig_th = [sig0, th0]
            time = h*(j-1)

            sig_mid = sig0 + (h/2) * fd(sig_th, time)[1]
            th_mid = th0 + (h/2) * fd(sig_th, time)[0]
            tmid = time + (h/2)
            sig_th_mid = [sig_mid, th_mid] 

            sig[j] = sig0 + h * fd(sig_th_mid, tmid)[1]
            th[j] = th0 + h * fd(sig_th_mid, tmid)[0]
            sig0, th0 = sig[j], th[j] 
        print('plotted')
        plt.plot(th,sig)
    plt.xlim([-pi,pi])
    plt.title('50 sigmas vs theta')
    #physics behind this?

    plt.show()
#two()
def four():
    for a in linspace(.5,3,5): #increasing a increases the frequency
        b = g = .5
        d =2

        R0 = F0 = 2
        t = np.linspace(0,15,100) # times for simulation

        def fd(vec,t):
            R,F = vec 
            dRdt = a*R-b*R*F
            dFdt = g*R*F-d*F
            return dRdt,dFdt 

        RF = odeint(fd,(R0,F0),t)

        plt.figure()
        plt.plot(t,RF[:,0],label='R')
        plt.plot(t,RF[:,1],label='F')
    plt.show()

    for b in linspace(.5,3,5): # increasing b makes the graphs less smooth, more of a platau at the bottom
        a = 1
        g = b
        d = 2

        R0 = F0 = 2
        t = np.linspace(0,15,100) # times for simulation

        def fd(vec,t):
            R,F = vec 
            dRdt = a*R-b*R*F
            dFdt = g*R*F-d*F
            return dRdt,dFdt

        RF = odeint(fd,(R0,F0),t)

        plt.figure()
        plt.plot(t,RF[:,0],label='R')
        plt.plot(t,RF[:,1],label='F')

    plt.show()

    for d in linspace(.5,3,5): 
        a = 1
        g = b = .5


        R0 = F0 = 2
        t = np.linspace(0,15,100) # times for simulation

        def fd(vec,t):
            R,F = vec 
            dRdt = a*R-b*R*F
            dFdt = g*R*F-d*F
            return dRdt,dFdt

        RF = odeint(fd,(R0,F0),t)
        plt.figure()
        plt.plot(t,RF[:,0],label='R')
        plt.plot(t,RF[:,1],label='F')

    plt.show()
#four()

#at 70?

def six():
    
    s0 = .95
    i0 = .05
    r0 = 0

    b = .1
    g = .05

    
    def SIR(s0,i0,r0,b,g,n):

        R0 = b/g
        S_label = f'S, b:{b}, g:{g}'
        I_label = f'I, b:{b}, g:{g}'
        R_label = f'R, b:{b}, g:{g}'
        t = linspace(0,n,100) #just put different numbers for t, not told what to put

        def fd(vec,t):
                s,i,r = vec 
                dsdt = -b*i*s
                didt = b*i*s-g*i
                drdt = g*i
                return dsdt,didt,drdt

        SIR = odeint(fd,(s0,i0,r0),t)
        plt.plot(t,SIR[:,0],label= S_label, color='blue')
        plt.plot(t,SIR[:,1],label= I_label, color='red')
        plt.plot(t,SIR[:,2],label= R_label,   color='green')

    SIR(s0,i0,r0,b,g,250)

    plt.title('SIR Model')
    plt.xlabel('Time')
    plt.legend()

    plt.figure()

    fig = plt.figure()

    for b in linspace(.1,1,4): #need to make a subplot for each set of for loop
        print(b)
    

    plt.title('Changing Beta')   
    plt.legend()

    """plt.figure()

    for g in linspace(.05,.5,4):
        SIR(s0,i0,r0,b,g,50)    

    plt.title('Changing Gamma')
    plt.legend()

    
    for i0 in linspace(.01,.5,4):
        SIR(s0,i0,r0,b,g,50)

    plt.title('Changing Initial Infected')
    plt.legend()"""
    #plt.show()

    
six()
