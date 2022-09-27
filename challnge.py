# if the list contain negative numbers, the function will not return list end with zeros
def sort_zeros(list):
    return sorted(list, reverse=True)

# if the list contain negative numbers or any latter, the function will return list end with zeros
def zeros_list(list):
    number = []
    zeros = []
    for item in list:
        if item == 0:
            zeros.append(item)
        else:
            number.append(item)
    return number+zeros

number = [-10, 1, 2, 0, 0, 3, -15, 4, 5, 0, 6, 0, 7, 8, 9, -1]
print(sort_zeros(number))
print(zeros_list(number))
