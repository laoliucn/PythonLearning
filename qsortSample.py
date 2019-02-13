# qsort sample

def qsort(input_list):
    if len(input_list) < 2:
        return input_list
    pivot = input_list[0]
    less = [i for i in input_list[1:] if i <= pivot]
    more = [j for j in input_list[1:] if j > pivot]

    return qsort(less) + [pivot] + qsort(more)


list1 = [4, 2, 6, 8, 1, 0, 9, 3]
list2 = [1, 0, 8]
list3 = [-2, 45, 23, 1, 4, 8, 2, 5]

print(qsort(list1))
print(qsort(list2))
print(qsort(list3))
