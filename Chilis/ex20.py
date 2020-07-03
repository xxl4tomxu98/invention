# linear search
def find1(odered_list, guessed_number):
    return guessed_number in odered_list


# binary search approach

# The following is the iterative binary search
def find(ordered_list, element_to_find):

    start_index = 0
    end_index = len(ordered_list) - 1

    while start_index <= end_index:

        middle_index = int(start_index + (end_index - start_index) / 2)

        middle_element = ordered_list[middle_index]

        if middle_element == element_to_find:
            return (middle_index, middle_element)
        elif middle_element > element_to_find:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    return False


# The following is the recursive binary search
def find2(ordered_list, element_to_find, start_index, end_index):

    while start_index <= end_index:

        middle_index = int(start_index + (end_index - start_index) / 2)
        middle_element = ordered_list[middle_index]

        if middle_element == element_to_find:
            return (middle_index, middle_element)
        elif middle_element > element_to_find:
            return find2(ordered_list, element_to_find, start_index, middle_index-1)
        else:
            return find2(ordered_list, element_to_find, middle_index+1, end_index)
    return False


#list = input('please enter ordered list of numbers: ')
#number = input('please enter a number: ')
list = [12, 43, 45, 65, 78, 129, 345, 876, 2345]
number = 2345

if __name__ == '__main__':
    print(find1(list, number))
    print(find(list, number))
    print(find2(list, number, 0, len(list)-1))
