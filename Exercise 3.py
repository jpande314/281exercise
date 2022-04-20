# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:55:51 2022

@author: johnp
"""

#import sys
#locate_python = sys.exec_prefix
#print(locate_python)

from numpy import*
import matplotlib.pyplot as plt

"""from sympy import*
init_printing()"""


#Problem 1,2

def probz():
    rows = int(input('Number of rows: '))
    cols = int(input('Number of columns: '))
    rows_n = []
    
    for n in range(1,rows+1):
        rows_n.append([])#add a new now
        for i in range(1,cols+1): #add entry to each column, changes per row
            rows_n[n-1].append((n-1)*cols+i)
    cols_n = [row[3] for row in rows_n] #print specific column ex 3
    right = [rows_n[i][cols-3:] for i in range(3)] #top right 3x3
    left = [rows_n[i][:3] for i in range(3)] #top left 3x3
    
    print(f'Array: \n {array(rows_n)} \nRows: {rows}\nColumns: {cols}')
    print(f'fifth row: {rows_n[4]} fourth column: {cols_n}')
    print(f'3x3 top right:\n{right}')
    print(f'3x3 top left:\n{left}')
    print(transpose(rows_n))
probz()
#Problem 3,4,5

def probzz():
    h = float(input('Height(m): '))
    ang = float(input('Angle from +x axis(rad): '))*pi
    v = float(input('Velocity(m/s): '))
    t=0
    d_y=1
    
    x=[]
    y=[]
    while d_y>0:
        d_x = v*t*cos(ang) #formula for change in x
        d_y = h+v*t*sin(ang)-.5*9.8*t**2
        x.append(d_x)
        y.append(d_y)
        t+=.1 #increments of .1
    projectile_motion = array([x,y]) 
    print(projectile_motion)
    #print(f'X: {x}\nY: {y}')
    print(f'Array: \n{projectile_motion}')
    savetxt('C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\foo.csv',transpose(projectile_motion),header='data2 Jan 9 2018\r\X,Y',newline='\r\n',delimiter=",")
    """
    Problem 4
    """



    plt.plot(*projectile_motion) # == projectile_motion[0], projectile_motion[1]
    plt.show()
probzz()

#Problem 6

def prob_6():
    load = loadtxt('C:\\Users\\johnp\\Desktop\\UMass\\Spring 2022\\Physics 281\\In class exercises\\Files\\foo.txt')
    print(load)

#Problem 7

def prob_7():
    #two functions, one is maclaurin series of e^x with 5 steps, second is same maclaurin but to much higher accuracy
    '''
    n = symbols('n')
    f_1 = []
    f_2 = []
    for x in linspace(0,5,10): 
        f_1.append(series(e**n,n,0,x))
    for x in linspace(0,5,10): 
        f_2.append(series(e**n,n,0,x)) #same as previous but now to 12th powa
    x = linspace(0,5,200)
    plt.plot(x, f_1, 'g-')
    plt.plot(x, f_2, 'b--')
    plt.show() 
    print(f_1)
    '''
    x_left = 0
    x_right = 4*3.141592653589
    """f_1 = [sin(i) for i in linspace(x_right,x_left,20)]"""
    f_2 = [cos(i) for i in linspace(x_right,x_left,20)]
    
    x_1 = linspace(x_left,x_right,20)
    
    """plt.plot(x_1,f_1,'b--')
    plt.plot(x_1,f_2,'g-')"""
    plt.xlim([x_left,x_right])
    plt.ylim([-1, 1])
    """
    #plt.ylim([min(f_1), max(f_1)]) ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
    """
    """plt.scatter(x_1,f_1)"""
    plt.scatter(x_1,f_2)
    plt.xlabel('x value')
    plt.ylabel('y value')
    plt.title('Sin(x), Cos(x)')
    plt.show()
    

#Problem 11

def prob_11(): #a and b, not c
    x = random.choice(range(1,37), size=(1000000)) #random number generator, does it a million times
    result = bincount(x) #counts how many instances of numbers in the list
    count_num= result[36] #how many instances of 36 in a million roles
    print(count_num/1000000) #instances of 36 in a million roles divided by a million, rought equals 1/36
    plt.hist(x,6) #data, specify how many bins
    plt.show()
