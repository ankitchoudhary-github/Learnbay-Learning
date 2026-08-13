# [1, [2, 3], [4, [5]]] -> find the sum of all elements in the nested list
def sum_nested_list(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_nested_list(element)  # Recursively sum nested lists
        else:
            total += element  # Add the integer value
    return total
