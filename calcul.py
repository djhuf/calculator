def sum(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def mult(a, b):
    print(a * b)


def div(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Ділення на нуль неможливе")


while True:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    symbol = input("Введіть математичний знак (+, -, /, *): ")
    if symbol == "+":
        sum(a, b)
    elif symbol == "-":
        sub(a, b)
    elif symbol == "/":
        div(a, b)
    elif symbol == "*":
        mult(a, b)
    else:
        print("Ви ввели неправильний математичний знак.")
        break
