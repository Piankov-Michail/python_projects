def bin_search(pointer, data, elem):
    if abs(data[0]) < abs(elem):
        return 0
    index = pointer
    while (index < len(data) and abs(data[index]) >= abs(elem)):
        index *= 2
    right = min(index, len(data) - 1)
    left = pointer
    while (True):
        if left > right:
            return len(data)
        middle = (left + right) // 2
        if abs(data[middle]) > abs(elem):
            left = middle + 1
        elif abs(data[middle]) < abs(elem):
            if middle - 1 >= 0 and abs(data[middle - 1]) >= abs(elem):
                return middle
            right = middle - 1
        else:
            left = middle + 1