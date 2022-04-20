from numpy import*
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#Problem 1 ((15))
def prob_1():
    #Plot data with error bars along with a model for the data
    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\data1.txt", float,skiprows = 1)
    x = data[:,0]
    y = data[:,1]
    b = linspace(0,8,len(x))
    f = .9*(b-2.8)**2-3.5
    err = data[:,2]
    plt.errorbar(x,y,err,capsize=3)
    plt.plot(b,f,color = 'red')
    plt.show()

#Problem 2 ((20))
def prob_2():
  
    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\data1.txt", float,skiprows = 1)
    
    x = data[:,0]
    y = data[:,1]
    err = data[:,2]
    nn = len(x) #number of data points
   
    def f(x,p_0,p_1):
        return p_0 + x*p_1

    pp = 4 #number of fit parameters
    guesses = (1,1) #initial parameter guess

    (p0,p1),cc = curve_fit(f,x,y,p0=guesses,sigma=err) # store fit parameter

    xmod = linspace(x[0],x[-1],100) # Generate x values between initial and
    ymod = f(xmod,p0,p1)
    
    yfit = f(x,p0,p1) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    plt.errorbar(x,y,err,fmt='bo') # plot the data
    plt.plot(xmod,ymod,'r') 
    plt.figure()

    def f(x,p_0,p_1,p_2):
        return p_0 + x*p_1 + p_2*(x)**2
   
    pp = 4 #number of fit parameters
    guesses = (1,1,1) #initial parameter guess

    (p0,p1,p2),cc = curve_fit(f,x,y,p0=guesses,sigma=err) # store fit parameter

    xmod = linspace(x[0],x[-1],100) # Generate x values between initial and
    ymod = f(xmod,p0,p1,p2)
    
    yfit = f(x,p0,p1,p2) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    plt.errorbar(x,y,err,fmt='bo') # plot the data
    plt.plot(xmod,ymod,'r') 
    plt.figure()


    def f(x,p_0,p_1,p_2,p_3):
        return p_0 + x*p_1 + p_2*(x)**2 + p_3*(x)**3
    
    pp = 4 #number of fit parameters
    guesses = (1,1,1,1) #initial parameter guess

    (p0,p1,p2,p3),cc = curve_fit(f,x,y,p0=guesses,sigma=err) # store fit parameter

    xmod = linspace(x[0],x[-1],100) # Generate x values between initial and
    ymod = f(xmod,p0,p1,p2,p3)
    
    yfit = f(x,p0,p1,p2,p3) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    plt.errorbar(x,y,err,fmt='bo') # plot the data
    plt.plot(xmod,ymod,'r') 




    plt.show()

#Problem 3 ((10))
def prob_3():
    #sub plot with prob 2, and the residuals
    def f(x,p_0,p_1,p_2,p_3,p_4):
        return p_0 + x*p_1 + p_2*(x)**2 + p_3*(x)**3 + p_4*(x)**4
    
    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\data1.txt", float,skiprows = 1)
   
    x = data[:,0]
    y = data[:,1]
    err = data[:,2]
    nn = len(x) #number of data points
    
    pp = 4 #number of fit parameters
    guesses = (1,1,1,1,1) #initial parameter guess

    (p0,p1,p2,p3,p4),cc = curve_fit(f,x,y,p0=guesses,sigma=err) # store fit parameter

    xmod = linspace(x[0],x[-1],100) # Generate x values between initial and
    ymod = f(xmod,p0,p1,p2,p3,p4)
    
    yfit = f(x,p0,p1,p2,p3,p4) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    res = ((yfit-y))

    plt.errorbar(x,y,err,fmt='bo') # plot the data
    plt.plot(xmod,ymod,'r') 
    plt.figure()
    plt.errorbar(x,res, err,fmt='bo')
    plt.scatter(x,res)
    plt.show()

#Problem 4 ((10))
def prob_4():
    def f(x,p_0,p_1,p_2,p_3,p_4):
        return p_0 + x*p_1 + p_2*(x)**2 + p_3*(x)**3 + p_4*(x)**4
    
    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\data1.txt", float,skiprows = 1)
   
    x = data[:,0]
    y = data[:,1]
    err = data[:,2]
    nn = len(x) #number of data points
    
    
    def f(x,p_0,p_1):
        return p_0 + x*p_1
    guesses = (1,1) #initial parameter guess

    (p0,p1),cc = curve_fit(f,x,y,p0=guesses,sigma=err) # store fit parameter
    
    yfit = f(x,p0,p1) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-2) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    def f(x,p_0,p_1,p_2):
        return p_0 + p_1*x + p_2*x**2
    guesses = (1,1,1) #initial parameter guess

    (p0,p1,p2),cc = curve_fit(f,x,y,p0=guesses,sigma=err)

    yfit = f(x,p0,p1,p2) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-3) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    def f(x,p_0,p_1,p_2,p_3):
        return p_0 + p_1*x + p_2*x**2 + p_3*x**3
    guesses = (1,1,1,1) #initial parameter guess

    (p0,p1,p2,p3),cc = curve_fit(f,x,y,p0=guesses,sigma=err)

    yfit = f(x,p0,p1,p2,p3) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-4) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    def f(x,p_0,p_1,p_2,p_3,p_4):
        return p_0 + p_1*x + p_2*x**2 + p_3*x**3 + p_4*x**4
    guesses = (1,1,1,1,1) #initial parameter guess

    (p0,p1,p2,p3,p4),cc = curve_fit(f,x,y,p0=guesses,sigma=err)

    yfit = f(x,p0,p1,p2,p3,p4) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-5) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

    def f(x,p_0,p_1,p_2,p_3,p_4,p_5):
        return p_0 + p_1*x + p_2*x**2 + p_3*x**3 + p_4*x**4 + p_5*x**5
    guesses = (1,1,1,1,1,1) #initial parameter guess

    (p0,p1,p2,p3,p4,p5),cc = curve_fit(f,x,y,p0=guesses,sigma=err)

    yfit = f(x,p0,p1,p2,p3,p4,p5) # this calculates the model fitting function at the x 
    yys = (y-yfit)**2/err**2 # this generates an array of the squared differ
    chisqr = sum(yys)/(nn-6) # compute reduced chi-squared
    print(f'Reduced chi-squared = {chisqr:.3f}')

#Problem 6 (not checked off(15))
def prob_6():
    data = loadtxt("C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\Homework\\HW2\\co2_data.txt", float,skiprows = 2)
    
    def f(x,p_0,p_1,p_2,p_3,p_4):
        return p_0+p_2*cos(p_1*x+p_3)+p_4*x

    t = data[:,2]
    co2 = data[:,3]
    yrt = t[0:24]
    yrc = co2[0:24]
    plt.plot(yrt,yrc)


    nn = len(yrt) #number of data points
    
    pp = 5 #number of fit parameters
    guesses = (300,1,1,1,1) #initial parameter guess
    


    params,cc = curve_fit(f,yrt,yrc,p0=guesses) # store fit parameter
    (p0,p1,p2,p3,p4) = params

    xmod = linspace(t[0],yrt[-1],100) # Generate x values
    ymod = f(xmod,p0,p1,p2,p3,p4)
    plt.plot(xmod,ymod,'r')


    #yfit = f(yrt,p0,p1) # this calculates the model fitting function at the x 
    print(params)

    """plt.figure()
    plt.plot((yfit-yrc))"""

    plt.show()

#Problem 7 (not checked off(20))
def prob_7():

    v = 0 #sum 

    L = 50

    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if i ==0  and j == 0 and k == 0:
                    continue
                f = (sqrt(i**2+j**2+k**2))
                if (i+j+k) % 2== 0:
                    v -= 1/f
                else:
                    v += 1/f
                
    print(v)

#Problem 8 (not completed(10))
def prob_8():
    """Choose a set of increasing L values, and use your previous program to
    plot how the Madelung constant changes as a function of lattice size"""
    
    v = 0 #sum 

    L = 40

    a = 1

    x = range(1,1000000,100000)

    f_a = []


    for a in x:
        for i in range(-L,L+1):
            for j in range(-L,L+1):
                for k in range(-L,L+1):
                    if i ==0  and j == 0 and k == 0:
                        continue
                    f = 1/(a*(sqrt(i**2+j**2+k**2)))
                    if (i+j+k) % 2== 0:
                        v -= f
                    else:
                        v += f
        f_a.append(v)
        print(v)
    plt.plot(x,f_a)
    plt.xlabel('a')
    plt.ylabel('M')
    plt.show()
                
#all the above would put me at 100pts