def sum(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)


def mult(x, y):
    print(x * y)


def div(x, y):
    if y != 0:
        print(x / y)
    else:
        print("Ділення на нуль неможливе")


def div_all(x, y):
    if y != 0:
        print(x // y)
    else:
        print("Ціле ділення на нуль неможливе")


while True:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    symbol = input("Введіть математичний знак (+, -, /, *, //, **): ")
    if symbol == "+":
        sum(a, b)
    elif symbol == "-":
        sub(a, b)
    elif symbol == "/":
        div(a, b)
    elif symbol == "*":
        mult(a, b)
    elif symbol == "//":
        div_all(a, b)
    elif symbol == "**":
        pow(a, b)
    else:
        print("Ви ввели неправильний математичний знак.")
        break
