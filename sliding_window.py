#* Sliding Windows Problems

def max_sliding_window(iterator, number=2):

    """
    Divide the iterator in subiterator
    With 1 space to distance and large defined by "number"
    Return the subiterator with the max sum
    """

    max_list = []
    max_sum = 0

    for index in range(len(iterator)):
        sub_list = iterator[index:index+number]
        sub_sum = sum(sub_list)

        if sub_sum > max_sum:
            max_list = sub_list
            max_sum = sub_sum

    return max_list, max_sum


print(max_sliding_window([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))

def string_sliding_window(iterator, number=2):
    
    """
    Divide the iterator in subiterator
    With 1 space to distance and large defined by "number"
    Return the subiterator with the max diferent chars
    """

    string_list = []
    string_difference = 0

    for index in range(len(iterator)):
        sub_list = iterator[index:index+number]
        sub_string = "".join(sub_list)

        sub_list_difference = []
        sub_difference = 0

        for character in sub_string:
            if not character in sub_list_difference:
                sub_list_difference.append(character)
        
        sub_difference = len(sub_list_difference)

        if sub_difference > string_difference:
            string_list = sub_list
            string_difference = sub_difference

    return string_list, string_difference


print(string_sliding_window(["aadsfadfg", "afdsewascvg", "a", "a", "abcdef"], 2))
