# TODO: Task 2
#  Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
#  the value of squared a divided by b, construct a try-except block which raises an exception if the two values given
#  by the input function were not numbers, and if value b was zero (cannot divide by zero).

def numb(a, b):
    result = int(a) ** 2 / int(b)
    print(result)
    return

try:
    numb(input('1st num: '), input('2nd num: '))
except ZeroDivisionError:
    print('Делить на ноль нельзя.')
except ValueError:
    print('Неверный тип данных.')
