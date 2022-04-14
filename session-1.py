# Basic Data Types
# var_int = 12
# var_float = 12.1
# var_str = "123"
# var_bool = True


# print("This is an int", var_int)
# print("This is a float", var_float)
# print("This is a string", var_str)
# print("This is a bool", var_bool)


a = 9
b = 9


# Operators
# print(a + b)  # addition
# print(a - b)  # subtraction
# print(a * b)  # multiplication
# print(a / b)  # division
# print(a % b)  # remainder
# print(a // b)  # mod
# print(a**b)  # exponent
# print(a == b)  # equal to
# print(a != b)  # not equal to
# print(a < b)  # less than
# print(a <= b)  # less than or equal to
# print(a > b)  # greater than
# print(a >= b)  # greater than or equal to


# Conditional Statements
# if a > b:
#     print("a is greater than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("a is not greater than b")


# Loops

# for loop
# for i in range(10):
#     print(i)


# while loop
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1


# break statement
# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if i == 10:
#         break

arr_test = [1, 2, 3, 4, 5]


def abc(a):
    s = 0
    print(len(a))
    for i in range(len(a)):
        s = s + a[i]
    return s
    print("This is after return")


print(abc(arr_test))
