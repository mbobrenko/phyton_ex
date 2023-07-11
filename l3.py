def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        pivot =array[0]
    less=[i for i in array[1:] if i<=pivot]
    greater=[i for i in array[1:] if i>pivot]
    return quick_sort(less)+[pivot]+quick_sort(greater)

print(quick_sort([13,3,533,24,5,8,624,556,67]))

        