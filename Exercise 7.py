from numpy import*
from scipy.integrate import quad
from scipy import special
import matplotlib.pyplot as plt

#can do more problems, that will add up to a hundred

#1 (not checked (15))
def p_1():
    a = 3
    b = 4 
    
    c = 5
    d = 6

    x = (a*c+d*b)/(c**2+d**2)
    y = (b*c-a*d)/(c**2+d**2)

    print(f'manual: {x,y}, python version: {(3+4j)/(5+6j):.3},')

    def e_iz(z):
        return cos(z)+1j*sin(z)
    def cos_z(z):
        return ((exp(1j*z)+exp((-1)*1j*z))/2) #substituite cos sin function

    print(f'manual: {e_iz(2):.3}, python: {exp(2j):.3}')
    print(f'manual: {cos_z(3):.3}, python: {cos(3j):.3}')
#p_1()
#2 (not checked (15))
def p_2():
    t = linspace(0,10,11)
    z = 5+.2j
    def e(t):
        e_t = [exp(1j*z*t) for t in range(0,t+1)]
        return e_t
    real = [ele.real for ele in e(10)]
    imag = [ele.imag for ele in e(10)]

    plt.plot(t,real, label = 'real')
    plt.plot(t,imag, label = 'imaginary')
    plt.legend()
    plt.figure()
    plt.plot(real, imag,)
    plt.xlabel('real')
    plt.ylabel('imaginary')
    axes=plt.gca()
    axes.set_aspect('equal')  
    plt.show()
    #idk why they look like that
#p_2()
#4 (not checked (20))
def p_4():
    N = 300 #number of points
    n_max = 20 #max number of iterations
    region = zeros(shape = (N,N)) #create a N x N array
    x_count = 0 #x counter for indexing
    
    for x in linspace(-2,1, N):
        y_count = 0
        for y in linspace(-1.5,1.5,N):
            C = x+y*1j
            z = x+y*1j
            n = 0
            while abs(z) < 2 and n < n_max: #if the absolute value of z is less than 2 and n is less than n_max
                z = z**2+C
                n += 1
            region[x_count][y_count] = n
            
            y_count += 1
        x_count += 1
    plt.imshow(region, cmap = 'inferno')
    plt.show()
#p_4()
#5 (not completed (20))
def p_5():
    N = 50 
    n_max = 5
    region = zeros(shape = (N,N))
    x_count = 0
    for x in linspace(-2,1, N):
        y_count = 0
        for y in linspace(-1.5,1.5,N):
            C = x+y*1j
            z = x+y*1j
            n = 0
            diverge = x**2+y**2 > 4
            if(diverge):
                while abs(z) < 2 and n < n_max:
                    z = z**2+C
                    n += 1
                region[x_count][y_count] = n
        
            
            y_count += 1
        x_count += 1
    plt.imshow(region, cmap = 'inferno')
    plt.show()
#not sure why the output is flat color, 
p_5()
#7 (not completed (15))
def p_7():
    m = .9999
    a = 0
    b = pi/2
    n = 1000
    h = 1

    def f(t):
        return (1-m*sin(t)**2)**(1/2) #function to be integrated
    
    def tsum(a,b,n): #sum function, trapezoid
        s = 0.5*f(a) + 0.5*f(b)
        h = (b-a)/n
        for k in range(1,n):
            s += f(a+k*h)
        return s
    def s_odd_sum(a,k,h):
        s = 0
        for k in range(1,n,2):
            s +=4*f(a+k*h)
        return s
    def s_even_sum(a,k,h):
        s = 0
        for k in range(2,n,2):
            s +=4*f(a+k*h)
        return s

    ans1 = special.ellipe(m) #easy way
    
    ans2 = ((b-a)/n)*(((f(a)+f(b))/2)+tsum(a,b,n)) #trapezoidal 

    def simpsons_rule(a,b,n):
        s = 0
        h = (b-a)/n
        for k in range(1,n,2):
            s += 4*f(a+k*h)
        for k in range(2,n,2):
            s += 2*f(a+k*h)
        return s*(h/3)

    def trapezoidal_rule(a,b,n): #git hub co pilot
        s = 0
        h = (b-a)/n
        for k in range(1,n):
            s += 2*f(a+k*h)
        return s*(h/2)
    
    ans4 = quad(f,0,pi/2)

    print(ans1,ans2,simpsons_rule(a,b,n), ans4[0])
    print(f'github copilot: {trapezoidal_rule(a,b,n)}')
#p_7()
"""#8 (should be checked (15))
def p_8():
    debye = 428 #K
    V = 1000 #cm^3
    p = 6.022*10**28 #m^-3
    T = 275 #K
    k_b = 1.3806*10**(-23)
    h_c = []

    def C(T):

    def int(x):
        return (x**4)*exp(x)/(exp(x)-1)**2
    I = quad(int, 0,debye/T)
    C = I[0]*9*V*p*k_b*(T/debye)**3

    for T in linspace(5,500,100):
        def int(x):
            return (x**4)*exp(x)/(exp(x)-1)**2
        I = quad(int, 0,debye/T)
        C = I[0]*9*V*p*k_b*(T/debye)**3
        h_c.append(C)

    plt.plot(linspace(5,500,100), h_c)
    plt.show()
#p_8()
"""
