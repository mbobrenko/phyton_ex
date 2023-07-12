# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
# задача на сдвиг

#1 решение
# list_1 = [5, 4, 6, 7, 8, -10]
# k = int(input())
# k = k % len(list_1)
# list_result = list()

# for i in range(k):
#     list_result.append(list_1[len(list_1) - 1 - i])

# for i in range(len(list_1) - k):
#     list_result.append(list_1[i])
# print(list_result)

#2 решение удаление элементов и перенос их на шаг указанный в функции Pop / insert
# lst = [1, 2, 3, 4, 5]
# k = 2

# for i in range(k):
# lst.insert(0, lst.pop(-1))
# print(lst)

list_1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list_1)
list_result = list()

for i in range(k):
    list_result.append(list_1[len(list_1) - k + i])

for i in range(len(list_1) - k):
    list_result.append(list_1[i])
print(list_result)
