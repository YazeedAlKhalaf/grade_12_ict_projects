import math

active = True


def print_empty_line():
    print("")


def print_error(error):
    print_empty_line()
    print("🛑", error)
    print_empty_line()


def print_menu():
    print("\033[H\033[J", end="")
    print("Choose an operation from the options below:")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print_empty_line()
    print("0) exit (or any unassigned number)")


def add(num1: float, num2: float) -> float:
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    return num1 / num2


while(active):
    print_menu()

    try:
        result = 0

        print_empty_line()

        user_choice = int(input("Option: "))

        print_empty_line()

        if user_choice <= 4 and user_choice != 0:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            print_empty_line()

        if user_choice == 1:
            result = add(first, second)
        elif user_choice == 2:
            result = subtract(first, second)
        elif user_choice == 3:
            result = multiply(first, second)
        elif user_choice == 4:
            result = divide(first, second)
        elif user_choice == 0:
            print("Good Bye 👋")
        else:
            print("This choice is not listed in the options.")

        if user_choice <= 4 and user_choice != 0:
            print("Your Result is:", result)

        active = False  # this exits the calculator

    except NameError:
        print_error("NameError: please use numbers only.")
    except SyntaxError:
        print_error("SyntaxError: please use numbers only.")
    except TypeError:
        print_error("TypeError: please use numbers only.")
    except AttributeError:
        print_error("AttributeError: please use numbers only.")
    except ValueError:
        print_error("ValueError: please use numbers only.")
