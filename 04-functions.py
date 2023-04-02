def print_hello():
    print("hello")


def is_even(n):
    remainder = n % 2
    result = remainder == 0
    # print(result)
    return result
    print("test after return")  # this will not print


# print_hello()
# res = is_even(2)
# print(res)

def generate_report_card(student_name, maths, physics, chemistry, computer_science):
    output_str = "Student Name: " + student_name + "\n" + \
    "Maths: " + str(maths) + "% out of 100%\n" + \
    "Physics: " + str(physics) + "% out of 100%\n" + \
    "Chemistry: " + str(chemistry) + "% out of 100%\n" + \
    "Computer Science: " + str(computer_science) + "% out of 100%"
    percentage = (maths + physics + chemistry + computer_science) / 400
    return output_str, percentage

def show_report_card(percentage):
    if percentage >= 50:
        print("Passed")
        print("\a")
    else:
        print("Failed")
        print("\a")

report_card, percentage = generate_report_card("abc", 60, 70, 80, 80)
print(report_card)
show_report_card(percentage)