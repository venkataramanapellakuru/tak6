#print statement
print("hello")

#variables
#.only allow characters are A-Z,a-z and  decimal number from [0-9] and one special symbol is( _)
ABC_abc_123=123
print()
print( "the value of abc is:",ABC_abc_123)
print()
print("the address of abc is:",id(ABC_abc_123))
print()
print("the type of abc is:",type(ABC_abc_123))

#data types
#int data type
x1=15000
print(x1)
print()
print(type(x1))
x2=-10000
print(x2)
print()
print(type(x2))

#2.float or floating data type:
  #python supports floating data type .
  # It can be represented in decimal  point number or floating point number either positive number or negative number. it can be 1.3e also floating datatype.
x1=123.45
print(x1)
print()
print(type(x1))
print()
x2=-156.90
print(x2)
print()
print(type(x2))

#3. boolean data type:
	# python supports Boolean datatypes. the main objectives of boolean datatypes is returns
# the boolean values after checking the conditions either true or false.
x1=120
x2=150
res1=x1==x2
res2=x1!=x2
print("the result is:", res1)
print()
print("the data type is:",type(res1))
print()
print("the results is:",res2)

#4.complex datatype:
    # python supports complex datatype. the main objective of complex data type is to perform some complex operations in our application. in python complex data type can be define or declare as x1=123+148j or x2=156+178j. it may be either +ve or -ve complex data type.
# here :x1=123+145j-->123 is real part -->x1.real-->output is 123.00
#145 is imaginary part-->x1.imag-->output is 145.00
x1=123+145j
x2=-156-178j
print(x1)
print()
print(type(x1))
print()
print(x2)
print()
print(type(x2))

#5.string datatype:
#-->string can be represented as collection of characters or sequence of characters an enclosed with ('')/("")/('''''')("""""")
#-->while working with string data type space is also one character
#-->python support +ve index which start from 0 to end-1.it is also know as forward direction.
#-->python support -ve index which start from -1 to end+1
#-->('''''')/("""""") is also used for mutli line.
str1="i will be a 'software developer' after end of an program"
print(str1)
print()
print(type(str1))
print()

#list data type:
#python supports list data type. if you want to represent one object or group of object in single entity then we can use list data type.in python list data type can be represented as [] or ().

l1=[]
print(l1)
print()
print(type(l1))
print()

#properties of list data type:
#->Inseration is preserved
#->Duplicate objects are allowed 
#->Hetrogenious objects are allowed
#->List is a mutable(statefull object)
#->List is a dynamic or growable
#->Indexing and slice operator is applicable for list data type

#Tuple data type:
=============
#Python supports tuple data type. If you want to represent more objects or group of objects
#as a single entity then we can go with tuple data type. In python tuple data type can be represent as () or tuple().While working with tuple data type in python () are optional.

t1=()
print(t1)
print()
print(type(t1))
print()
t2=tuple()
print(t2)
print()
print(type(t2))

#Properties for tuple data type.
#->Inseration is preserved
#->Duplicate objects are allowed
#->Hetrogenious objects are allowed
#->Tuple is a immutable object
#->Tuple is not dynamic or not growable
#->Indexing and slice operator is applicable for tuple data type.
#->Inseration is preserved:


#Set data type:
#Python supports set data. if you want to represent one or more than object or group of object as a single entity. Then we can be define or declare using curli braces ‘{}’ .while working with set data type if define or declare {} then pvm will consider dict data type to overcome this problem.

set_one={}
print(set_one)
print()
print(type(set_one))
print()
s1=set()
print(s1)
print()
print(type(s1))
print()

#Properties of set data type:
#insertion is not preserved.
##heterogeneous objects are allowed
#set is mutable object
#set is dynamic or growable
#indexing and slice operator is not applicable for set data type.
#insertion is not preserved.

#DICT DATA TYPE:
#Python support dict data type . if you want to represent one or more than one objects into key and value pair then we can go with dict data type.in python dict data type cab represented as {} and dict() function.
#Ex:a={‘key’:value}

import time
d1={'pid':100,'pname':'mobile','price':17000,'pid':101}
print(d1)
print()
print(type(d1))

#bytearray data type:
#Python supports bytearray data type. It is exactly same as bytes data type. Except bytearray is a
#mutable object

d1=[123,124,255,111,222,250]
b1=bytearray(d1)
print(b1)
print(type(b1))

#frozenset data type:
#Python supports frozenset data type. It is exactly same as set data type. frozenset data is immutable object.
import time
d1={123,124,255,111,222,250}
b1=frozenset(d1)
print(b1)
print(type(b1))
time.sleep(2)
print("end of an application")

#Range data type:
#Python supports range data type. The main objective of range data type is generate the only decimal numbers. It is always associated with for and while.

import time
for i in range(10):
    time.sleep(1)
    print(i)
time.sleep(2)
print("end of an application")



#None data type:
#Python supports None data type which nothing or empty.

sal=25000
print(sal)
print(type(sal))
sal=None
print(sal)
print(type(sal))
sal1=35000
print(sal1)
print(type(sal1))


#->Arithmetic operators:
#Python supports AO. The main objective of AO is perform arithmetic operations in our application 
#as per the application requirement. Following are the AO in python
#->+,*,-,/,//,%,**


x1=eval(input("enter the x1 value :"))
x2=eval(input("enter the x2 value :"))
res1=x1+x2
print("the addition of two numbers are :",res1)
res2=x1-x2
print("the subtration of two numbers are :",res2)
res3=x1*x2
print("the multiplication of two numbers are :",res3)
res4=x1/x2
print("the division of two numbers are :",res4)
res5=x1//x2
print("the floor of two numbers are :",res5)
res6=x1**x2
print("the power of two numbers are :",res6)

#Assignment operators:
#Python supports Assignment operator. The main objective of Assignment operator is meant
#for memory utilization. In python we can define or declare assignment operators follows

#->a=a+b  ------------->a+=b
#->a=a/b ------------->a/=b 
#->a=a*b ------------->a*=b

x1=eval(input("enter the x1 value :"))
x2=eval(input("enter the x2 value :"))
x1+=x2
print("the addition of two numbers are :",x1)
x1-=x2
print("the subtraction of two numbers are :",x1)
x1*=x2
print("the multiplication of two numbers are :",x1)

#->Logical operators:
#Python supports logical operator. The main objective of logical operator is to perform some logical operations in our application as per the application requirement. Following are the logical operators in python
#->logical and operator ----> and
#->logical or operator ------>   or
#->logical not operator ----->not


#->logical and operator:
username=input("enter username :")
password=input("enter the password")
if(username=="rahul" and password=="_12345"):
    print(username,password,"login successfully")
else:
    print(username,password"invalid user")


#Logical or operator ---- or :

username=input("enter username :")
password=input("enter the password")
if(username=="rahul" or password=="_12345"):
    print(username,password,"login successfully")
else:
    print(username,password,"invalid user")

#Logical not operator:
t1=True
print(t1)
print(type(t1))
t2=not(t1)
print(t2)


#->Equality operator:
#Python supports EO. The main objective of quality operator is to meant content comparison. If
#the content comparison is true. It return boolean values either True or False as per the application 
#requirement. Following are the EO in python.

import time
list1=['A','B','C','D']
list2=['A','B','C','D']
print(list1)
print(type(list1))
print(list2)
print(type(list2))
print("the comparison of list1 and list2 is :",list1==list2)
print("the comparison data type of list1 and list2 is :",type(list1==list2))
print("the comparison of list1 and list2 is :",list1!=list2)
print("the comparison data type of list1 and list2 is :",type(list1==list2))

#->Comprision operator:
===================
#Python supports CO. The main objective of CO is to perform some comparision operation in python. Following are CO in python
x1=eval(input("enter the value of x1 :"))
x2=eval(input("enter the value of x2 :"))
obj1=x1>x2
print("the x1 is greater than x2 :",obj1)
obj2=x1<x2
print("the x1 is less than x2 :",obj2)
obj3=x1>=x2
print("the x1 is greater than equal x2 :",obj3)
obj4=x1<=x2
print("the x1 is less than equal x2 :",obj4)

#if-else statements:
#==============
#Python supports if-else statements.if 'if' codition is true then if block will be executed.Otherwise
#else block will be executed.

p1=input("enter the password")
p2=input("enter confirmation password")
if(p1=="_12345" and p2=="_12345"):
    print(p1,p2,"login valid")
else:
    print(p1,p2,"invalid login")

#->for loop:
#It is a iterative statement in python. If you want to execute number of statements number of time 
#if our data or information is in sequence or in order or we know the limit of data then we can go with for loop 

import time
for x in range(10):
    print("for loop")
time.sleep(2)
print("end of an application")



#while loop:
#------------
#It is a iterative statement in python. The main objective of while loop if you want to execute number 
#of statements number of time if our data not in sequence or infinite data.Then we can go with 
#while loop.

import time
i=0
while(i<3):
    print(i)
    i+=1
print()
time.sleep(2)
print("end of an application")











































































































































































































































































