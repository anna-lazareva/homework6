# Homework №3:
def square_of_sum(param):
    """
    Вычисление квадрата суммы
    :param param: Значение для расчета
    :return: Рассчитанное значение
    """
    return sum(range(1, param + 1)) ** 2


def sum_of_squares(param):
    """
    Вычисление суммы квадратов
    :param param: Значение для расчета
    :return: Рассчитанное значение
    """
    return sum([i ** 2 for i in range(1, param + 1)])


for i in range(1, 4):
    n = int(input("Введите число: "))
    print("Разность квадрата суммы и суммы квадратов:", square_of_sum(n) - sum_of_squares(n))


# Homework №4:
def check_length(data, limit, printable_string):
    """
    Проверить длину
    :param data: Срока для которой определяем длину
    :param limit: Сравниваемое значение длины
    :param printable_string: Выводимая строка в случае не равенства длины data c limit
    :return: True, если длина переданной строки равна limit
    """
    if len(data) != limit:
        print(printable_string)
        return False
    return True


def check_digit(param, error_str):
    """
    Проверка символа на цифру
    :param param: Проверяемый символ
    :param error_str: Выводимая строка в случае ошибки
    :return: True, если цифра
    """
    if not param.isdigit:
        print(error_str)
        return False
    return True


prefix = input("Введите серию паспорта: ")

if not check_length(prefix, 4, 'серию не корректна'):
    exit()

for char in prefix:
    if not check_digit(char, 'серию не корректна'):
        exit()
print("серия корректна")

prefix = input("Введите номер паспорта: ")

if not check_length(prefix, 6, 'номер не корректен'):
    exit()

for char in prefix:
    if not check_digit(char, 'номер не корректен'):
        exit()

print("номер корректен")

# Homework №5:
def check_number(data):
    """
    Проверка строки на число
    :param data: Проверяемая строка
    :return: True, если строка содержит только цифры
    """
    if not data.isdigit():
        print('Вы ввели не число!')
        return False
    return True


data = input("Введите число: ")
if not check_number(data):
    exit()

fib = [0, 1]
equals = []
for i in range(int(data)):
    if fib[-1] == fib[-2]:
        l = len(fib)
        equals += [l-2, l-1]
    fib.append(fib[-1] + fib[-2])
print(fib)
if equals:
    print('Индексы повторяющихся элементов:', equals)
