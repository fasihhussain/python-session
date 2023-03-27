# basic data types
# https://www.tutorialspoint.com/python/python_data_types.htm
var_int = 123
var_float = 12.2
var_str = "this is a string"
var_bool = True

print("This is an int", var_int)
print("This is a float", var_float)
print("This is a string", var_str)
print("This is a bool", var_bool)

a = 3
b = 2

# operators
# https://www.tutorialspoint.com/python/python_operators.htm
print("a + b: " + str(a + b))       # addition
print("a - b: " + str(a - b))       # subtraction
print("a * b: " + str(a * b))       # multiplication
print("a / b: " + str(a / b))       # division
print("a % b: " + str(a % b))       # remainder
print("a // b: " + str(a // b))     # mod
print("a ** b: " + str(a ** b))     # exponent
print("a == b: " + str(a == b))     # equal to
print("a != b: " + str(a != b))     # not equal to
print("a < b: " + str(a < b))       # less than
print("a <= b: " + str(a <= b))     # less than or equal to
print("a > b: " + str(a > b))       # greater than
print("a >= b: " + str(a >= b))     # greater than or equal to

# type conversion
print("Integer value of " + str(var_float) + " is " + str(int(var_float)))
print("Integer value of " + str(var_bool) + " is " + str(int(var_bool)))