# ##Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
import random
size=int(input('Enter size of the list'))
my_list = [random.randint(0,10) for_ in range(size)]
print(my_list)
count=0 
i=0
while i< len(my_list):
    j=i+1
    while j<len(my_list):
        if my_list[i]==my_list[j]:
            print(my_list[i],my_list[j])
            my_list.pop(j)
            my_list.pop(i)
            count+=1
            i=0
            j=0
        j+=1
        i+=1

print(my_list)
            