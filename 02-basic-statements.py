# conditional statements
a = int(input("Please enter a value: "))

if a > 10:
    print("This number is greater than 10")
elif a == 10:
    print("This number is 10")
elif a == 20:
    print("This number is 20")
else:
    print("This number is smaller than 10")


# for loop
# https://www.tutorialspoint.com/python/python_for_loop.htm
for i in range(10):
    a = int(input(str(i) + ". " + "Please enter a value: "))

    if a > 10:
        print("This number is greater than 10")
    elif a == 0:
        print("I'm breaking this loop")
        break
        # https://www.tutorialspoint.com/python/python_break_statement.htm
    elif a == 5:
        print("Got input 5, won't print the value")
        continue
        # https://www.tutorialspoint.com/python/python_continue_statement.htm
    elif a == 10:
        print("This number is 10")
    elif a == 20:
        print("This number is 20")
    else:
        print("This number is smaller than 10")
    
    print("Got user input " + str(a))



# 10
# 9
# 8
# ...
# 0

# prints the above sequence
start = 10
stop = -1
step = -1

print("Print countdown from 10 to 0")
for i in range(start, stop, step):
    print(i)