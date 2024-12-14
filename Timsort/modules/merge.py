from modules.bin_search import bin_search
def merge(first_array, second_array, gallop_size=7):
    first_array_pointer = 0
    first_gallop_counter = 0
    second_array_pointer = 0
    second_gallop_counter = 0
    result = []
    while (first_array_pointer < len(first_array) and second_array_pointer < len(second_array)):
        if abs(first_array[first_array_pointer]) >= abs(second_array[second_array_pointer]):
            result.append(first_array[first_array_pointer])
            first_array_pointer += 1
            first_gallop_counter += 1
            second_gallop_counter = 0
            if first_gallop_counter == gallop_size:
                index = bin_search(first_array_pointer, first_array, second_array[second_array_pointer])
                result += first_array[first_array_pointer:index]
                first_gallop_counter = 0
                second_gallop_counter = 0
                first_array_pointer = index
        elif abs(first_array[first_array_pointer]) < abs(second_array[second_array_pointer]):
            result.append(second_array[second_array_pointer])
            second_array_pointer += 1
            second_gallop_counter += 1
            first_gallop_counter = 0
            if second_gallop_counter == gallop_size:
                index = bin_search(second_array_pointer, second_array, first_array[first_array_pointer])
                result += second_array[second_array_pointer:index]
                first_gallop_counter = 0
                second_gallop_counter = 0
                second_array_pointer = index
    result += first_array[first_array_pointer:]
    result += second_array[second_array_pointer:]
    return result