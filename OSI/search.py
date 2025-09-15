def create_permutations(set_: set) -> list:
    if len(set_) == 1:
        return [[set_.pop()]]

    list_ = []
    for i in set_:
        for j in create_permutations(set_.difference((i, ))):
            list_.append([i] + j)
        
    return list_


def binary_search(list_, n, init_index, end_index):
    index = (init_index + end_index) // 2
    
    if list_[index] == n:
        return index

    if list_[index] > n:
        return binary_search(list_, n, init_index, index)

    else:
        return binary_search(list_, n, index, end_index)

def binary_search_pivot(list_, init_index, end_index):
    index = (init_index + end_index) // 2
    
    if init_index + 1 == end_index:
        return -1
    
    if sum(list_[:index]) == sum(list_[index:]):
        return index
    
    if sum(list_[:index]) > sum(list_[index:]):
        return binary_search_pivot(list_, init_index, index)
    
    else:
        return binary_search_pivot(list_, index, end_index)


if __name__ == "__main__":

    import random

    # print(create_permutations({1, 2, 3, 4}))

    random_list = [random.randint(0, 1000) for _ in range(0, 101)] + [682]
    random_list.sort()

    print(binary_search(random_list, 682, 0, len(random_list)))
    print(binary_search_pivot([-6,-4,-2], 0, 3))