# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# text = input().split()
# text1 = {}
# for i in text:
#     if i in text1:
#         text1[i] += 1
#     print(f'{i}_{text1[i]}', end=" ")
#     else:
#         print(i, end=' ')
#         text1[i] = 0


# stroka=input().split()
# result={}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end='')
#     else:
#         print(i,end=''),
#     result[i]=result.get(i,0)+1
    
    
text = input().split()
text1 = {}
for i in text:
    if i in text1:
        text1[i] += 1
print(f'{i}_{text1[i]}', end=" ")
    else: print(i, end=' ')
    text1[i] = 0