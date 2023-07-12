# a=1
# b=3.99
# c= 'eje"nkv'

# ##print(f"{a}- {b}- {c}")
# print("{} - {} - {}".format(a,b,c))


# # print(n)
# print(6)
# # print(3,4,44)


##ВВод данных через функцию input которая запрашивает данные через консоль, для сохранения значений происходит через присвоение какой то переменной 

# print ("Введите первую строку")
# a=input()
# print(a)
# b=input("Ввведите второе число ")

# print(a, '+',b,"=", a+b)


## приведение типов функция int отбрасывает дробную часть

# c=5.89
# print(c)
# print(type(c))
# ##c=int(c)
# c=str(c) 
# ##print(c)
# print(c+"djfoj")
# # print(type(c))


# c= 1
# print(c)
# print(type(c))
# ##c=int(c)
# c=bool(c) 
# print(c)
# ##print(c+"djfoj")
# print(type(c))

## Корректная программа сложения синтаксис
# print ("Введите первую строку")
# a=int(input())
# print(a)
# b=int(input("Ввведите второе число "))

# print(a, '+',b,"=", a+b)

## Функция округления чисел
# a=5.899
# b=6.32
# print(round(a*b,3))

## Функция присваивания
# iter=2
# iter+=3 #iter=iter+3
# iter-=4 #iter=iter-4
# iter*=5 #iter=iter*5
# iter/=4 #iter=iter/4
# iter//=4 #iter=iter//4
# iter%=4 #iter=iter%4
# iter**=4 #iter=iter**4

# text ='jfkjer ehrghg iegig gghvhhvhhhv fhrifyeflsk hiv'
# text=text[2:9]+text[-6]+text[5]
# print(text)


# import modul1
# print(modul1.max1(5,9))

# from modul1 import max1
# print(max1(5,9))

# from modul1 import *
# print(max1(15,9))

##import modul1 as m1
# print(m1.max1(5,9))

list_1 = ["H", "e", "l", "l", "o"]
print(' '.join(list_1))
## H e l l o

stroka = 'Hello world Moscow Name'
print(stroka.split("o")) 
#Hell, w, rldM, scw,  Name

stroka = 'Hello world Moscow Name'
print(len(stroka.split(" ")))
#4 (слова)

stroka = 'Hello world Moscow Name'
list_1 = []
for i in stroka:
list_1.append(i)
print(list_1)
# разделение по символам