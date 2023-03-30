def print_square(n):
    if n < 2:
        print('"n" should be greater than 2')
        return
    print("*" * n)
    for i in range(n - 2):
        print("*" + " " * (n - 2) + "*")
    print("*" * n)


def print_right_triangle(n):
    if n < 0:
        print('"n" should be greater than 0')
        return
    for i in range(1, n + 1):
        print("*" * i)


def print_mirrored_right_triangle(n):
    if n < 0:
        print('"n" should be greater than 0')
        return
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


# https://www.codingem.com/diamond-pattern-in-python-using-for-loop/
def print_diamond(n):
    for i in range(n):
        print(" " * (n - i), "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i), "*" * (2 * i + 1))


print("1 - Square")
print("2 - Right Triangle")
print("3 - Mirrored Right Triangle")
print("4 - Diamond")

shape = int(input("Enter shape you want to print: "))
size = int(input("Enter size of shape: "))

if shape == 1:
    print_square(size)
elif shape == 2:
    print_right_triangle(size)
elif shape == 3:
    print_mirrored_right_triangle(size)
elif shape == 4:
    print_diamond(size)
else:
    print("Invalid shape choice")
