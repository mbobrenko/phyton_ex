# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# n = int(input())
# list_first = list()
# for i in range(n):
#     x = int(input())
# list_first.append(x)
# count = 0
# for i in range(1, n - 1):
#     if list_first[i - 1] < list_first[i] < list_first[i + 1]:
#         count += 1
# print(count)

numbers = [5, 1, 5, 3, 6, 3, 4]
count= 0
for i in range(1, len(numbers)-1):
    if numbers[i - 1] < numbers[i] > numbers[i+1]:
        count += 1
print(count)

