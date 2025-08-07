def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}


def calculator():
    n1 = float(input("please enter the 1st number\n"))
    continue_calculation = True
    while continue_calculation:
        for symbol in operations:
            print(symbol)
        operation = input("please select a symbol from above\n")
        n2 = float(input("please input your 2nd number for calculation"))
        answer = operations[operation](n1, n2)
        print(f" your result is {answer}")
        choice = input(f"please enter 'y' to continue with {answer}"
                       f", 'n' to start a new calculation and 'e' to end").strip().lower()

        if choice == "y":
            n1 = answer

        elif choice == "n":
            n1 = float(input("please enter the 1st number\n"))

        else:
            print("Thanks for using the calculator!")
            return
