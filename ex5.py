## По данному целому неотрицательному n вычислите значение N! n=1*2*3*..n
n=int(input("введите число"))
result=1
i=2
while i<=n:
    result*=i
    i+=1
print(result)