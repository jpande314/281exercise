from ctypes import c_int16
import sys
locate_python = sys.exec_prefix
print(locate_python)

from numpy import*
import matplotlib.pyplot as plt



#Problems 1 (completed 1(15pts) havent done 2)

def prob_1():
    """
    asks for x,y gives radius and angle
    need to make angle between -pi and pi, depending on x,y
    """
    x = float(input('X: ')) 
    
    if x != 0: 
        y = float(input('Y: '))
        r = sqrt(x**2+y**2)
        theta = (arctan(y/x))*180/pi
        print(f'R: {r:.3} Theta: {theta:.3}')
        prob_1()
    else: 
        print('Please don\'t enter 0 for X')

#Problem 3 (completed a(10), b(10), c(5))

def prob_3():
    #converting polar eq to cart
    #pt a
    fig, axs = plt.subplots(1,3)
    b = linspace(0,2*pi,1000)
    x =[2*cos(i)+cos(2*i) for i in b]
    y =[2*sin(i)-sin(2*i) for i in b]
    axs[0].plot(x,y)
    #pt b
    theta = linspace(0,10*pi,500)
    x_2 = theta**2*cos(theta)
    y_2 = theta**2*sin(theta)
    axs[1].plot(x_2,y_2)
    #pt c
    theta_2 = linspace(0,24*pi,10000)
    x_3 = ((exp(cos(theta_2)))-(2*cos(4*theta_2))+(sin(theta_2/12)**5))*cos(theta_2)
    y_3 = ((exp(cos(theta_2)))-(2*cos(4*theta_2))+(sin(theta_2/12)**5))*sin(theta_2)
    print(x_3)
    axs[2].plot(x_3,y_3)
    plt.show()

#Problem 4 (completed(10))

def prob_4():
    #4 subplots
    fig, axs = plt.subplots(2,2)
    theta = linspace(0,2*pi)
    s = sin(theta)
    t = tan(theta)
    x = 2*cos(theta)+cos(2*theta)
    y = 2*sin(theta)-sin(2*theta)
    axs[0,0].plot(theta,s)
    axs[0,1].plot(theta,t)
    axs[1,0].plot(theta,x)
    axs[1,1].plot(theta,y)
    axs[0,0].set_title('Sin')
    axs[0,1].set_title('Tan')
    axs[1,0].set_title('x')
    axs[1,1].set_title('y')
    axs[0,0].set_xlabel('Theta')
    axs[0,0].set_ylabel('Radius')
    axs[0,1].set_xlabel('Theta')
    axs[0,1].set_ylabel('Radius')
    axs[1,0].set_xlabel('Theta')
    axs[1,0].set_ylabel('Radius')
    axs[1,1].set_xlabel('Theta')
    axs[1,1].set_ylabel('Radius')

    plt.subplots_adjust(hspace=.5)
    plt.show()

#Problem 5 (completed(15))

def prob_5():
    #plot 3 variations of one function
    x = linspace(-10,10,10000)
    f = x + 2*cos(x**2)
    fig, axs = plt.subplots(1,3)
    axs[0].plot(x,f)
    axs[1].plot(x+5,f) #translates the function 5 to the right
    axs[2].plot(x,f+10) #10 right
    
    plt.show()

#Problem 6 (completed(10))

def prob_6():
    x = linspace(0,10,1000)
    f = ((cos(x))**2)+5
    plt.plot(x,f)
    plt.figure()
    plt.hist(f, bins = 30)
    plt.show()

#Problem 7(completed(10))

def prob_7(): #slice arrays
    "plotting loadtxt data with error bars"
    x =loadtxt('C:\\Users\\johnp\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\error_bars.txt',skiprows=1)
    c_1 = []
    c_2 = []
    c_3 = []
    for n in range(50):
        c_1.append(x[n,0])
        c_2.append(x[n,1])
        c_3.append(x[n,2])
    plt.plot(c_1,c_2,color='teal')
    plt.errorbar(c_1,c_2,yerr=c_3, ecolor='red')
    plt.show()

#Problem 8 (completed(20))

def prob_8():
    #meshgrid
    #D = 50
    
    


    """f = empty((2*D,2*D))
    for i in range(-D,D):
        x=i
        for j in range(-D,D):
            y=j
            f[i,j] = sin(sqrt(x**2+y**2))""" #the larger the second part is, the more warped
    x,y = meshgrid(linspace(-50,50,100),linspace(-50,50,100))
    f = sin(sqrt(x**2+y**2)+5*arctan2(y,x))
    plt.imshow(f) #
    
    plt.show()
