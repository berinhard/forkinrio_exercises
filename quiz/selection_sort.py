def selection_sort(sortable_list):
    list_copy = sortable_list[:]
    for i in xrange(len(list_copy)):
        minor_pos = find_min_position(list_copy[i:])
        minor_pos += i
        list_copy[i], list_copy[minor_pos] = list_copy[minor_pos], list_copy[i]
    return list_copy

def find_min_position(integer_list):
    minor_position = 0
    for i in xrange(len(integer_list)):
        if integer_list[i] <= integer_list[minor_position]:
            minor_position = i
    return minor_position
