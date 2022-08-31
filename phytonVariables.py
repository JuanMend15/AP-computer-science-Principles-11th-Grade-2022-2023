x=5
y="John"
print(x)
print(y)
#5=integer=int
#hello=word=integer\
#Boolean @ and 1
#3.0=float#Variables are case sensitives 
a=4
A= "Bob"
print(a,A)
#A will not overwrite a 
# =in progamming means "assigned to" example 5 is assigned to variable x
# LEGAL VARIBLE NAMES
#  A variable name must start or underscore character
# It cannot start with a number 
#IS A CASE SENSITIVE ADN CANNOT contain Alpha-Numeric characters (A-z,0-9)
# the "#" can also mean  "man equal to"
# phython allow you to assign many values to multiple variables 
x,y,z= "Orange","Banana", "cherry"
print(x)
print(y)
print(z)
# phython allows you to assing multiple variables 
x=y=z="Orange"
print(x)
print(y)
print(z)



#Random Number 
import random 
print(random.randrange(1,10))  
# concatination 
# to concatinate or combine 2 strings you can use the + operator
a= "Hello"
b="patricia"
c= a + "" + b
print(c)
# String format 
age ="36"
text="My name is Patricia ,Iam "+ age 
print( text )
s ="Juan  "
t= "Carlos"
mytxt= "hello my name is "+ s + t
print(mytxt)
import os
os.system('clear')


# Booleans ( True/0False)
# It uses two values True Or False , It evalute any expression to true or or False ,Python then Evaluate and reiterms to a boolean 
print(10<9)
print(10==9)
#1 equal means assign, 2 equals mean equal to 
print(10<9)
# Boolean in a condition ( and if statement )
a=200
b=33
if b>a:
  print('b is greater than a')
else:
  print("b is greater than a")
  # evaluate values and variables 
  # evaluate a string and a number , example function bool()
print(bool("Hello"))
print(bool(15))
#python operators
#examples 
x=15
y=2
#print(x%y)
print(x//y)# the floor division //rounds the result down to the nearest
print(x**y)

