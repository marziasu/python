# use type casting
'''
base=float(input("enter your base:"))
height=float(input("enter your height: "))

area=0.5*base*height
print("Area is: ",area) #for string, use '+'sign otherwise comma
'''
# math function
'''
print(sqrt(25))
print(floor(3.4))
print(ceil(3.4))
print(abs(-6))
print(max(35,30))
'''
# data type
'''
num1=2.5
print("number:",num1)
print(type(num1))
num2=2
print(type(num2))
# formatted string
print(f"{num1}+{num2}={num1+num2}")
# otherwise
print(num1,"+",num2,"=",num1+num2)

if num1>num2:
    # print(num1,"is greater than",num2)
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(num1,"is less than",num2)
else:
    print("they are equal")
'''
# Find vowel and consonant
'''ch=input("enter your character:")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    print("consonant")
# Find Grade
num=80
if num>=80 and num<=100:
    print("A+")
elif num>=70 and num<80:
    print("A")
else:
    print("Fail")'''
# For , while loop
'''n=1
while n<10:
    print(n,end=" ")
    n=n+1
'''
# for x in range(10):
'''for x in range(1,10,1): #(start,end,range)
    print(x,end=" ")

print("\n")
# 1^2+2^2+3^2+.......+n^2
n=int(input("enter your length of series: "))
sum=0
for x in range(1,n+1,1):
    sum=sum+x*x
print(sum)'''

# List
# list =[1,2,3,4]
# print("list : ",list)

# List as user input
'''n=input("enter a text of number:") # [10 20 30]
list=n.split()  # [10,20,30] , split on following character 
print(list)'''
# dictionary
'''d={        #key: element
    101 : "rahim",
    102 : "karim",
}
print(d[101])
print(d.get(103,"not found"))

#tuple
t=(
    1,2,3,4
)
print("tuple : ",t) # in tuple, value not change 

# set , has no duplicate value
s={9,6,5}
print("set : ",s)
#list ke set a transfer
num=set([4,5,6,7])

num.add(10)
num.remove(4)
print(num)
print(7 in num)

# union in two set
print("union: ",s | num)
print("intersection:",s & num)
print("difference",s - num) 

# matrix
matrix=[
    [1,2,3],
    [4,5,6]
]
for row in matrix:
    for col in row:
        print(col)
    #print(row)'''
# swapping
'''a=20
b=10
a,b=b,a #swap
print(a,b);'''

# oop
'''class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calculate_area(self):
        area=0.5*self.base*self.height
        print("area=",area);

ob=Triangle(4,6)
print(isinstance(ob,Triangle)) #check object
ob.calculate_area()'''

# inheritance
'''class A:
    def display1(self):
        print("i am A")

class B(A):    # single inheritance
    def display2(self):
        # super().__init__()  # use super() keyword to get super class constructor
        print("i am B")
class C(A):     # heirarchicle inheritance
    def display3(self):
        print("i am C")
class D(B,C):      # mutiple inheritance
    def display4(self):
        pass   # for empty 

ob=D()
ob.display2()'''

# Abstruction
'''from abc import ABC,abstract method  # ABC means abstract base class and abstract method import 
class shape(ABC):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    @abstractmethod
    def area(self):
        pass
class triangle(shape):
    def area(self):
        area=0.5*self.base*self.height
        print("triangle area is = ", area)
class rectangle(shape):
    def area(self):
        area=self.base*self.height
        print("Rectangle area is = ",area)
ob=rectangle(10,20)
ob.area()

ob=triangle(10,20)
ob.area()'''

# polymorphism
# built in polymorphism
'''print(len("marzia sultana"))
print(len([ 1,4,7]))

print(5//2) # just integer part print so // sign
print(5**2) # square
i=1
while i<5:
    print(i*'*')
    i+=1 '''
'''import numpy as np

a=np.array([1,2,3])
print(a)'''



