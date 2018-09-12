import numpy as np
import matplotlib.pyplot as plt
import time
import serial
from time import sleep


L=0.01 # the length of the actuator
n=10# number of spatial samples


u0=0   # s

u0s=0### the voltage before the clamping at t is zero
#### the final value that voltage will reach at the space
#c=0.0009
c=0.0026
R=12e6
t_elapsed= 0.0001
Ke=9e9
A=2.167e-6
th_sq=6.25e-10

dx=L/n  ### space step
#alpha=0.00017# the inverse of tau (real value)
alpha=0.0001



#0.0002# time step
t_final=0.2### two minutes 
dt= 0.0001
b=2.167e-3
h= 2.5e-5

Inertia= (b*h**3)/12

#### flexure rigidity
Young_Modulus= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)




x=np.linspace(dx, L, n)  ### space


u=np.zeros(n)*u0
dudt=np.empty(n)  ### empty vector


# Here we assume the desired frequency, and we know the total time, and we know samples for computing the spatial domain, so we can estimate the each time step for the sampled voltage, so we can draw one time frame for sampling, and other time frame for computing spatial domain

u[0]=0


### here we define the amplitude of the voltage signal 
# number of samples for the sampled source voltage before entering the sample
for q in range(0, 2000): ### to generate 1 volt  
    u[0]=u[0]+ 0.0009## sampling rate
    u[0]=u[0]
   
    t= np.arange(0,t_final,dt)# iteration
    for j in range(0,len(t)):
        plt.clf()
        
        for i in range(1,n-1):  
            dudt[i]= alpha*(-(u[i]-u[i-1])/dx**2+(u[i+1]-u[i])/dx**2) 
    u=u+dudt*dt
    u[n-1] = u[n-2];
    
  

  
    
    q= c*u*(1-np.exp(-t_elapsed*alpha))
    #print q
  
  
    stress= (Ke*q**2)/(A* th_sq)
    
    bending_stress=  (Ke*q**2 * np.sin(89.9))/(A* th_sq) 
    
                    #### axial force
    Force= stress*A*1e6
    
    
    epsilon= bending_stress/Young_Modulus
    
    ''' defining the constraints of the tripod  the strain and the curvature'''  
    
    f= open("Strain.txt",'w')
    
    dl= dx* epsilon
    
   
    f.write( str(dl[9]) + "\n")
    
    #print dl
    
    #print Force
    ##print stress
    #q= (u*t_elapsed)/R 
    #print q
    
    
    Moment_neutral= (Inertia*bending_stress)/h
    
    ### moment curvature
    Curvature= Moment_neutral/(Young_Modulus* Inertia)
    
    #print Curvature
    
    
    
    
    
    #print Curvature
    
    #plt.figure(1)
    #plt.plot(x,u)
    #plt.axis([0,L,0,1])
    #plt.xlabel('length (m)')
    #plt.ylabel('voltage (v)')
    #plt.draw()
    #plt.pause(0.01)
    
  
    
    
    
    #https://en.wikipedia.org/wiki/Euler%E2%80%93Bernoulli_beam_theory
    #deflection
    #voight creep
    
    
    
    
