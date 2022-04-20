from re import X
from numpy import*
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from matplotlib import cm



#Problem 1 (not checked (10))
def prob_1():

    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\peak4.txt", float,skiprows = 1)
    x = data[:,0]
    y = data[:,1]
    yerr = array([.1 for i in x])
    
    def f(x,p_0,p_1,p_2,p_3,p_4):
        return p_0*exp((-1/2)*((x-p_1)**2)/p_2**2)+p_3*x+p_4
    
    guesses = (1,5,1,6,1) #second, p_1 most sensitive, best at around 5

    (p0,p1,p2,p3,p4),cc = curve_fit(f,x,y,p0=guesses, sigma=yerr) #store fit parameter

    xmod = linspace(x[0],x[-1],100) #Generate x values between initial and end
    ymod = f(xmod,p0,p1,p2,p3,p4)


    nn = len(x)
    pp = 4
    yfit = f(x,p0,p1,p2,p3,p4) # this calculates the model fitting function at the x 
    

    
    yys = ((y-yfit)**2)/yerr**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    plt.plot(xmod,ymod)
    plt.scatter(x,y)
    plt.show()

#Problem 2 (not checked (10))
def prob_2():
    #chi squared is .05 lower for quadratic background
    #not sure why we use a linear background without using a constant parameter
    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\peak4.txt", float,skiprows = 1)
    x = data[:,0]
    y = data[:,1]
    yerr = array([.1 for i in x])
    
    def f(x,p_0,p_1,p_2,p_5):
        return p_0*exp((-1/2)*((x-p_1)**2)/p_2**2)+p_5
    
    guesses = (1,5,1,1) #second, p_1 most sensitive, best at around 5

    (p0,p1,p2,p5),cc = curve_fit(f,x,y,p0=guesses, sigma=yerr) #store fit parameter

    xmod = linspace(x[0],x[-1],100) #Generate x values between initial and end
    ymod = f(xmod,p0,p1,p2,p5)


    nn = len(x)
    pp = 4
    yfit = f(x,p0,p1,p2,p5) # this calculates the model fitting function at the x 
    

    
    yys = ((y-yfit)**2)/yerr**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    plt.plot(xmod,ymod)
    plt.scatter(x,y)
    plt.show()

#Problem 3 (not checked (10))
def prob_3():
    """
    Read in the data from the file wavedata.txt, set σy = 0.2, and plot
    it. Based on the plot, decide on a likely model for the data. Decide
    on how many parameters will be needed; define the model fit function,
    and write a program to fit your model to the data. Show both model
    and data on the same plot.
    """
    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\wavedata.txt", float,skiprows = 1)
    x = data[:,0]
    y = data[:,1]
    plt.plot(x,y)

    def f(x,p_0,p_1,p_2,p_3):
        return p_0+p_3*sin(p_2*(x+p_1))
    
    guesses = (1,7,.6,3) #had to manual test, parameters with "1,1,1,1" guesses was really bad

    (p0,p1,p2,p3),cc = curve_fit(f,x,y,p0=guesses) #store fit parameter

    xmod = linspace(x[0],x[-1],100) #Generate x values between initial and end
    ymod = f(xmod,p0,p1,p2,p3)
    print(p0,p1,p2,p3)
    plt.plot(xmod,ymod)
    plt.show()

#Problem 4 (not checked (15))
def prob_4():
    """
    radioactive decay, plotting and uncertainties
    """
    data1 = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\decay1.txt", float,skiprows = 1)
    data2 = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\decay2.txt", float,skiprows = 1)
    x1 = data1[:,0]
    y1 = data1[:,1]
    yerr1 = array([sqrt(n) for n in y1])
    x2 = data2[:,0]
    y2 = data2[:,1]
    yerr2 = array([sqrt(n) for n in y2])
    
    plt.errorbar(x1,y1, yerr = yerr1, ecolor = 'red',label = 'decay 1')
    
    plt.errorbar(x2,y2,yerr = yerr2, ecolor = 'blue',label = 'decay 2')
    plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    #linear plot when you take the log means the original plot is exp
    plt.show()
#Problem 5 (not completed (20))
def prob_5():
    """
    fitting the model from 4 to each of the two data sets
    """
    data1 = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\decay1.txt", float,skiprows = 1)
    data2 = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\decay2.txt", float,skiprows = 1)
    x1 = data1[:,0]
    y1 = data1[:,1]
    yerr1 = array([sqrt(n) for n in y1])
    x2 = data2[:,0]
    y2 = data2[:,1]
    yerr2 = array([sqrt(n) for n in y2])
    
    #plt.errorbar(x1,(y1), yerr = yerr1, ecolor = 'red')
    plt.errorbar(x2,(y2),yerr = yerr2, ecolor = 'blue')

    def f(x,p_0,p_1,p_2):
        return p_0*exp(-x/p_1)+p_2
    
    guesses = (250,1,1) #second, p_1 most sensitive, best at around 5

    (p0,p1,p2),cc = curve_fit(f,x1,y1,p0=guesses, sigma=yerr1) #store fit parameter

    #xmod = linspace(x1[0],x1[-1],100) #Generate x values between initial and end
    #ymod = f(xmod,p0,p1,p2)


    nn = len(x1)
    pp = 3
    yfit = f(x1,p0,p1,p2) # this calculates the model fitting function at the x 
    

    yys = ((y1-yfit)**2)/yerr1**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    #print(f'Reduced chi-squared = {chisqr:.3f}')
    
    #plt.plot(xmod,ymod, color = 'blue')

    #2nd function

    def f2(x,p_0,p_1,p_2):
        return p_0*exp(-x/p_1)+p_2
    
    guesses = (165,54,45) #second, p_1 most sensitive, best at around 5

    (p0,p1,p2),cc = curve_fit(f2,x1,y1,p0=guesses, sigma=yerr2, maxfev = 10000, method = 'trf') #store fit parameter

    xmod2 = linspace(x2[0],x2[-1],100) #Generate x values between initial and end
    ymod2 = f2(xmod2,p0,p1,p2)


    nn = len(x2)
    pp = 3
    yfit = f2(x1,p0,p1,p2) # this calculates the model fitting function at the x 
    

    yys = ((y2-yfit)**2)/yerr2**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')
    
    plt.plot(xmod2,ymod2, color = 'orange')
    print(p0,p1,p2)
    plt.show()
    #dont know why the plots are linear, and why the orange plot is off
prob_5()
#Problem 7 (not completed (15))
def prob_7():
    """
    3D surface plot of a given function
    """
    x = linspace(-20,20,50)
    y = x
    X,Y = meshgrid(x,y)
    r = sqrt(X**2+Y**2)
    V = X*(6-r)*exp(-r/3)
    
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(projection='3d') # get some 3D axes
    ax.plot_surface(X,Y,V,cmap=cm.plasma) 
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('$\psi(x,y)$')
    plt.title('Wave Function')

    plt.show()
    
    plt.show()
    
#Problem 8 (not checked (10))
def prob_8():
    """
    continuation of 7, use a density plot instead
    """
    x = linspace(-20,20,50)
    y = x
    X,Y = meshgrid(x,y)
    V = X*(6-(sqrt(X**2+Y**2)))*exp(-(sqrt(X**2+Y**2))/3)
    plt.imshow(V)
    plt.show()

#Problem 9 (not completed (10))
def prob_9():
    """
    3D scatter plot of points on a sphere
    """
    r = 5
    X = []
    Y = []
    Z = []
    nn = 100

   

    for theta in linspace(0,pi,nn):
        for azimuthal in linspace(0,2*pi,nn):
            x = r*sin(theta)*cos(azimuthal)
            y = r*sin(theta)*sin(azimuthal)
            z = r*cos(theta)
            X.append(x)
            Y.append(y)
            Z.append(z)
        

    fig = plt.figure(figsize=(8,6))
    plt.rc('font', size=12)
    ax = fig.add_subplot(projection='3d') # get some 3D axes
    ax.scatter(X,Y,Z,s=1,color='m')     
    plt.show()


#this gets me to 100pts