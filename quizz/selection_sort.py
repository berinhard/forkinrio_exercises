def selection_sort(sortable_list):
    list_copy = sortable_list[:]
    for i, number in enumerate(list_copy):
        minor_pos = find_min_position(list_copy[i:])
        minor_pos += i
        list_copy[i], list_copy[minor_pos] = list_copy[minor_pos], list_copy[i]
    return list_copy

def find_min_position(integer_list):
    minor_integer = integer_list[0]
    minor_position = 0
    for i, integer in enumerate(integer_list):
        if integer <= minor_integer:
            minor_position = i
            minor_integer = integer
    return minor_position
