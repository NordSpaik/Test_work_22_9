def sort(array):
# Функция сортировки вставками
    for i in range(1, len(num_list)):
        a = num_list[i]
        b = i
        while b > 0 and num_list[b - 1] > a:
            num_list[b] = num_list[b - 1]
            b -= 1
        num_list[b] = a

    return(num_list)

def search(array, element, left, right):
# Функция двоичного поиска позиции введенного числа
    if left > right:
        return left
    middle = (left + right) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return search(array, element, left, middle - 1)
    else:
        return search(array, element, middle + 1, right)

# Ввод списка чисел и проверка введенных данных на соответствие
x = "str"
while not x.isdigit():
    print("Введите последовательность чисел через пробел:")
    num_list = [x for x in input().split(" ")]
    for x in num_list:
        if not x.isdigit():
            print("Данные не являются числами. Повторите ввод данных")
num_list = [int(x) for x in num_list]
# Ввод числа для сравнения и проверка его на соответствие
num = "str"
while not num.isdigit():
    num = input("Введите любое целое число - ")

num = int(num)

sort(num_list)
print(f"Список чисел после сортировки: {num_list}")

end_num = search(num_list, num, 0, len(num_list))
print(f"Номер позиции элемента, меньшего, чем введенное число, в списке {num_list} - '{end_num}'")
