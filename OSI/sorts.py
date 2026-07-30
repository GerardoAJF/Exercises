import random


list_ = [random.randint(1, 101) for _ in range(0, 11)]
def insertion_sort(array):
    
    for current in range(1, len(array)):
        key = array[current]
        previous = current - 1
        
        while previous >= 0 and key < array[previous]:
            array[previous + 1] = array[previous]
            previous -= 1
            
        array[previous + 1] = key
        
    return array

print(insertion_sort(list_))


list_ = [random.randint(1, 101) for _ in range(0, 11)]
def selection_sort(array):

    for current in range(0, len(array) - 1):
        for after in range(current, len(array)):

            if array[current] > array[after]:
                array[after], array[current] = array[current], array[after]

    return array

print(selection_sort(list_))


list_ = [random.randint(1, 101) for _ in range(0, 11)]
def bubble_sort(array):

    sort = False
    while not sort:

        sort = True
        for current in range(1, len(array)):
            previous = current - 1

            if array[previous] > array[current]:
                array[previous], array[current] = array[current], array[previous]
                sort = False
    
    return array

print(bubble_sort(list_))


list_ = [random.randint(1, 101) for _ in range(0, 11)]
def merge_sort(array):
    
    if len(array) == 1:
        return array
    
    fused = []
    
    l_point = 0
    r_point = 0
    
    l_list = merge_sort(array[:len(array) // 2])
    r_list = merge_sort(array[len(array) // 2:])
    
    while l_point < len(l_list) and r_point < len(r_list):
        
        if l_list[l_point] < r_list[r_point]:
            fused.append(l_list[l_point])
            l_point += 1
            continue
        
        fused.append(r_list[r_point])
        r_point += 1
    
    if l_point < len(l_list):
        fused += l_list[l_point:]
    elif r_point < len(r_list):
        fused += r_list[r_point:]
    
    return fused

print(merge_sort(list_))

