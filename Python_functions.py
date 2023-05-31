# python functions
# functions are used to perform certain task repetively
a=10
b=20
print('The sum :',a+b)
print('The diff:',a-b)
print('The product:',a*b)
a=200
b=300
print('The sum :',a+b)
print('The diff:',a-b)
print('The product:',a*b)
a=1000
b=2000
print('The sum :',a+b)
print('The diff:',a-b)
print('The product:',a*b)

# Declare Functions by using def keyword 
def cal(a,b): # define function 
    print('The sum :',a+b)
    print('The diff:',a-b)  # function body
    print('The product:',a*b)
cal(10,20)  # calling the function
cal(200,100)
cal(2000,20000)

# types of functions
# 1.built-in functions 
# ex: id(),type(),input(),print(),eval() .........

# 2.user defined functions/customized functions
# syntax:
# def func_name( pass any no of parameters):
#    '''doc string'''
#   body /logic code
#   return value
# def keyword is mandatory
# return keyword is not mandatory

# write a function to print wish message
def wish():
    print('Hello friends, good morning')
wish()
wish()
wish()
wish()

# function parameters/arguments
# parameters are input values from user
# write a functiom to take name of the student as input and print the wish message
def wish(name):
    print('Hello, {} Good morning:'.format(name))
wish('Hari')    

import argparse
parser=argparse.ArgumentParser()
parser.add_argument('name',type=str,help='enter name')
args=parser.parse_args()
def wish(name):
    print('Hello, {} Good morning:'.format(name))
wish(args.name)  

# write a function to take a number as a input and print square value?

def sqr(num):
    sq=num*num
    print('The square of {} is :{}'.format(num,sq))
sqr(2)

# return statement
# write a function to accept 2 numbers as input and return sum

def add(a,b):
    sum=a+b
    return sum
re=add(10,20)
print('The sum:',re)
print('The sum:',add(100,200))

def f1():
    print('Hello')
x=f1()
print('The return value:',x) # default return value is None

# write a function to find factorial of give positive int value

def factorial(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
re=factorial(5)
print('The factorial of a number is:{}'.format(re))

def factorial(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,7):
    print('The factorial of ',i, 'is:',factorial(i)) 

re=factorial(5)
print('The factorial of a number is:{}'.format(re))
# returning multiple values from a function

def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(1,2)
print(x,y)
def cal(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
t=cal(20,10)
print(type(t))
print(t)

def cal(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
t=cal(20,10)
print(type(t))
print(t)
for i in t:
    print(i,sep=':',end='\t')

def f1(a,b):
    print(a+b)
f1(10,20)

# Types of arguments

# 1.positional arguments
# 2.keyword arguments
# 3.default arguments
# 4.variable length arguments

# positional arguments
# in the positional arguments order will must be required

def sub(a,b):
    print(a-b)
sub(10,20)
sub(20,10)
sub(1)

# keyword arguments
# in keyword arguments the values we assign to the variable even we change the order
def sub(a,b):
    print(a-b)
sub(200,100)    
sub(a=100,b=200)
sub(b=200,a=300)
sub(200,100)
sub(a=200,b=100)
# sub(a=100,200)# invalid
sub(100,b=200)# valid
# we can use both positional and keyword arguments at time but first is positional argument and next will be keyword argument

# 16/12/22

# 3.Default arguments
def wish(name):
    print('Hello' ,name,'good evening')
wish('Praveen')

def wish(name='guest'):
    print('Hello' ,name,'good evening')
wish()
wish('Praveen')

def wish(name,msg):
    pass
def wish(name='Guest',msg='Good morning'):
    pass
def wish(name,msg='Good morning'):
    pass
# def wish(name='guest',msg) # invalid
    pass
# if we are not passing any value then only default value will be considered
# after default arguments, We should not take non-default arguments.

# 4. Variable length arguments
def func(*n):   # *n ->variable length arguments
    print(type(n))
    print(n)
    print('variable length argument function')
func() 
func(4)
func(1,3,2,2)

def sum(*n):
    total=0
    for x in n:
        total=total+x
    print('The sum:',total)
sum()# The sum:0
sum(9)# The sum:10
sum(10,20)# the sum:30

def f1(*n):
    print(n)
f1(10,20)
f1((1,2,2,2,3),(1,2,4,6,8))
def f1(x,*y):
    print(x)
    print(y)
f1(10,20,30,40)
f1(10)
f1() # invalid calling function required positional argument
def f1(x,*y):
    print(x)
    for y1 in y:
        print(y1)
f1(10,20,30,40)

def f(*x,Y): # invalid bcz of after var arguments there no positional arguments
    print(x)
    print(y)# f() missing 1 required keyword-only argument: 'Y' 
f(10,20,30) # error
def f1(*x,y):
    print(x)
    print(y)
f1(10,20,30,y=10)
def f1(*x,**y):
    print(x)
    print(y)
f1(10,20,30)

# def f1(*x,*y): #invalid 
#     print(x)
#     print(y)
# f1(10,20,30)

def f1(*x,**y):
    print(x)
    print(y)
f1(10,20,30)

# difference between *args & **kwargs?
# *args                                 **kwargs
# 1.variable length arguments        1.variable keyword arguments
# 2.f1(*n)#tuple                     2.f1(**kwargs)==>dictionary
# eg: def f1(*n):                   3.eg: def f1(**kwargs):
#         print(n)                                print(kwargs)
#     f1()==>()                              f1()==>{}
#     f1(10)==>(10,)                          f1(name='abc',rollno='10')==>{'name'='abc','rollno'=10}
#     f1(10,20,30)==>(10,20,30)               f1(a=10,b=20,c=30)==>{'a'=10,'b'=20,'c'=30}

# def f1(**kwargs):
#     print(kwargs)
# f1()
f1(a=10,name='praveen')
f1(a=10,b=20,c=30)

def f1(*args,**kwargs):
    print(args)
    print(kwargs)
f1(10,20,a=30,b=40)


# def f1(**kwargs,*args): #invalid syntax
    # print(args)
    # print(kwargs)
# f1(10,20,a=30,b=40)

def f(*x,y=10):
    print(x)
    print(y)
f(10,20,30,y=30)

def f(arg1,arg2,arg3=4,arg4=9):
    print(arg1,arg2,arg3,arg4)
f(3,2)
f(25,50,arg4=10)
f(10,20,30,40)
f(arg4=2,arg1=3,arg2=4)
f()#f() missing 2 required positional arguments: 'arg1' and 'arg2'
# f(arg3=10,arg4=20,30,40) #invalid # positional argument follows keyword argument
f(4,5,arg2=20)# TypeError: f() got multiple values for argument 'arg2'
f(4,5,arg3=4,arg5=6)#TypeError: f() got an unexpected keyword argument 'arg5'

# Types of variables

# 1.Global variables
# 2.Local variables
a=10
def f1():
    print(a)
f1()
def f2():
    print(a)
f2()

def f1():
    a=10
    print(a)
def f2():
    print(a)#NameError: name 'a' is not defined
f2()
f1()
def f1():
    a=10
    print(a)
f1()
def f2():
    a=20
    print(a)
f2()

# need of global keyword
a=10 # global variable
def f1():
    a=20 # local variable
    print(a)
def f2():
    print(a)
f1()
f2()
# to make global variable available to the function so that we can perform required modification
a=10
def f1():
    global a # To bring global variable to the function for the reqiured modification
    a=20 # we are changing the value of global variable
    print(a)
def f2():
    print(a)
f1()
f2()

def f1():
    a=10
    print(a)
def f2():
    print(a)# NameError: name 'a' is not defined
f1()
f2()

a=20
def f1():
    global a
    a=10
    print(a)
def f2():
    print(a)
f1()
f2()

a=10
def f1():
    print(a)
    # global a #SyntaxError: name 'a' is used prior to global declaration
    a=20
    print(a)
f1()

a=10
def f1():
    global a
    print(a) 
    a=20
    print(a)
f1()

globals()

a=333
def f1():
    a=22
    print(a) #22
    print(globals()) #{'a'=333}
f1()

a=333
def f1():
    a=22
    print(a) #22
    print(globals().get('a')) # 333
    print(globals()['a'])# 333
f1()

# Recursive Functions

# factorial function without using Recursion
def factorial(n):
    result=1
    while n>=1:
        result=result*n
        n=n-1
        return result



def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print('Factorial of 4 is: ',factorial(4))


def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
for i in range(11): #0 to 10
    print('Factorial of {} is:{} '.format(i,factorial(i)))

def factorial(n):
    print('Execution of factorial function for n:',n)
    if n==0:
        result=1
    else:
        result=n* factorial(n-1)
    print('returning factorial ({}) is :{}'.format(n,result))
    return result
print(factorial(3))
count=0
def factorial(n):
    global count
    count=count+1
    print("execution of factorial function for n:",n)
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(994))
print('The number of times factorial execution :',count)


count=0
def factorial(n):
    global count
    count=count+1
    print("execution of factorial function for n:",n)
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(995))#RecursionError: maximum recursion depth exceeded while calling a Python object
print('The number of times factorial execution :',count)

# Anyonymous functions (lambda functions)

def square(n):
    return n*n

s=lambda n:n*n
print(s(4))

# lambda input_arguments:expresion

s=lambda n:n*n
for i in range(1,11):
    print('the square of {} is: {}'.format(i,s(i)))

# lambda function to find sum of given 2 nnumbers

s=lambda a,b:a+b
print(s(10,20))
print(s(100,200))

# lambda function to find biggest of given 2 nnumbers
# 2 input values 

bigger=lambda a,b:a if a>b else b
print(bigger(10,20))
print(bigger(-10,-30))

# 3 input values
bigger=lambda a,b,c:a if a>b and a>c else b if b>c else c
print(bigger(10,202,30))
print(bigger(20,10,40))
print(bigger(50,10,2))

# functions as arguments

# filter(function,sequence)
# map(function,sequence)
# reduce(function,sequence)

# filter function
filter()

# without filter function


l=[1,2,3,4,5,6,7,8]

def isEven(n):
    if n%2==0:
        return True
    else:
        return False
l1=[]
for n in l:
    if isEven(n)==True:
        l1.append(n)
print(l1)

# with filter function
l=[1,2,3,4,5,6,7,8,9,10]
def isEven(n):
    if n%2==0:
        return True
    else:
        return False
l1=list(filter(isEven,l))
print(l1)

# filter() with lambda function

l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda n:n%2==0,l))
print(l1)

l=[1,2,3,4,5,6,7,8,9,10,11]
even=list(filter(lambda n:n%2==0,l))
print(even)
odd=list(filter(lambda n:n%2!=0,l))
print(odd)
# The nmbers which are divisible by 3 and odd
odd_by_3=list(filter(lambda n:n%3==0 and n%2!=0,l))
print(odd_by_3)

# map() function
l=[1,2,3,4,5,6]
def square(n):
    return n*n
l1=list(map(square,l))
print(l1)

l=[1,2,3,4,5,6]
l1=list(map(lambda n:n*n,l))
print(l1)

l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l3=list(map(lambda i,j:i*j,l1,l2))
print(l3)

l1=[1,2,3,4,5,6,7,8] # if diff length remaining elemets ignored
l2=[5,10,15,20,25]
l3=list(map(lambda i,j:i*j,l1,l2))
print(l3)

l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l4=[2,3,4,5,6,6,7,9]
l3=list(map(lambda i,j,k:i*j*k,l1,l2,l4))
print(l3)

# reduce function
l=[10,20,30,40]
result=reduce(lambda i,j:i+j,l)#NameError: name 'reduce' is not defined
print(result) 
# reduce is not inbuilt function in python it should be import from functools library
from functools import reduce
l=[10,20,30,40]
result=reduce(lambda i,j:i+j,l)
print(result)

# find the sum of first 100 numbers by using reduce() function
from functools import reduce
result=reduce(lambda i,j:i+j,range(1,101))
print(result)