carname = "Volvo"

x = 50

"""
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

Get the Type
x = 5
y = "John"
print(type(x))
print(type(y)) 

Sngl and Dbl
x = "John"
# is the same as
x = 'John'

Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a 

Variable Names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

"""

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

x, y, z = "Orange", "Banana", "Cherry"

x = y = z = "Orange"

"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""

def myfunc():
  global x
  x = "fantastic"