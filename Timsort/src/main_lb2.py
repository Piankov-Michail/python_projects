def tim_sort(array):
    global gallops_arr
    gallops_arr = []
    if len(array) == 0:
        return None
    if len(array) == 1:
        print(f'Part 0: {array[0]}')
        return str(array[0])

    def min_run(size):
        result = 0
        while(size >= 16):
            result |= (size & 1)
            size >>= 1
        return result + size

    def bin_search(pointer, data, elem):
        if abs(data[0]) < abs(elem):
            return 0
        index = pointer
        while(index < len(data) and abs(data[index]) >= abs(elem)):
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

    def merge(first_array, second_array, gallop_size=3):
        global gallops_arr
        gallops = 0
        first_arr_pointer = 0
        first_gallop_counter = 0
        second_arr_pointer = 0
        second_gallop_counter = 0
        result = []
        while (first_arr_pointer < len(first_array) and second_arr_pointer < len(second_array)):
            if abs(first_array[first_arr_pointer]) >= abs(second_array[second_arr_pointer]):
                result.append(first_array[first_arr_pointer])
                first_arr_pointer += 1
                first_gallop_counter += 1
                second_gallop_counter = 0
                if first_gallop_counter == gallop_size:
                    gallops += 1
                    indexex = bin_search(first_arr_pointer, first_array, second_array[second_arr_pointer])
                    result += first_array[first_arr_pointer:indexex]
                    first_gallop_counter = 0
                    second_gallop_counter = 0
                    first_arr_pointer = indexex
            elif abs(first_array[first_arr_pointer]) < abs(second_array[second_arr_pointer]):
                result.append(second_array[second_arr_pointer])
                second_arr_pointer += 1
                second_gallop_counter += 1
                first_gallop_counter = 0
                if second_gallop_counter == gallop_size:
                    gallops += 1
                    indexex = bin_search(second_arr_pointer, second_array, first_array[first_arr_pointer])
                    result += second_array[second_arr_pointer:indexex]
                    first_gallop_counter = 0
                    second_gallop_counter = 0
                    second_arr_pointer = indexex
        result += first_array[first_arr_pointer:]
        result += second_array[second_arr_pointer:]
        gallops_arr.append(gallops)
        return result

    def stack_merging(my_stack):
        data = my_stack
        my_stack = []
        counter = 0
        for i in data:
            my_stack.append(i)
            while (len(my_stack) > 1):
                if len(my_stack) > 2 and not (my_stack[-3][0] > my_stack[-1][0] + my_stack[-2][0]):
                    if my_stack[-3][0] < my_stack[-1][0]:
                        my_stack[-2][1] = merge(my_stack[-3][1],my_stack[-2][1])
                        print(f'Gallops {counter}: {gallops_arr[counter]}')
                        print(f'Merge {counter}: ' + ' '.join(map(str, my_stack[-2][1])))
                        counter += 1
                        my_stack[-2][0] = len(my_stack[-2][1])
                        my_stack.pop(-3)
                    else:
                        my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
                        print(f'Gallops {counter}: {gallops_arr[counter]}')
                        print(f'Merge {counter}: ' + ' '.join(map(str, my_stack[-2][1])))
                        counter += 1
                        my_stack[-2][0] = len(my_stack[-2][1])
                        my_stack.pop(-1)

                if not (my_stack[-2][0] > my_stack[-1][0]):
                    my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
                    print(f'Gallops {counter}: {gallops_arr[counter]}')
                    print(f'Merge {counter}: ' + ' '.join(map(str, my_stack[-2][1])))
                    counter += 1
                    my_stack[-2][0] = len(my_stack[-2][1])
                    my_stack.pop(-1)
                else:
                    break


        while (len(my_stack) > 1):
            if len(my_stack) > 2:
                if my_stack[-3] < my_stack[-1]:
                    my_stack[-2][1] = merge(my_stack[-3][1], my_stack[-2][1])
                    print(f'Gallops {counter}: {gallops_arr[counter]}')
                    print(f'Merge {counter}: ' + ' '.join(map(str, my_stack[-2][1])))
                    counter += 1
                    my_stack[-2][0] = len(my_stack[-2][1])
                    my_stack.pop(-3)
                else:
                    my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
                    print(f'Gallops {counter}: {gallops_arr[counter]}')
                    print(f'Merge {counter}: ' + ' '.join(map(str, my_stack[-2][1])))
                    counter += 1
                    my_stack[-2][0] = len(my_stack[-2][1])
                    my_stack.pop(-1)
            if len(my_stack) > 1:
                my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
                print(f'Gallops {counter}: {gallops_arr[counter]}')
                print(f'Merge {counter}: ' + ' '.join(map(str, my_stack[-2][1])))
                counter += 1
                my_stack[-2][0] = len(my_stack[-2][1])
                my_stack.pop(-1)
        return my_stack

    my_stack = []

    max_size = min_run(len(array))
    run = []

    increase = 1
    start = 0
    while(start < len(array)):

        if len(run) >= 2 and increase:
            if abs(array[start]) > abs(run[-1]):
                run.append(array[start])
                start += 1
            elif abs(array[start]) <= abs(run[-1]) and len(run) < max_size:
                for i in range(len(run)):
                    if abs(run[i]) >= abs(array[start]):
                        run.insert(i, array[start])
                        start += 1
                        break
            else:
                my_stack.append([len(run), run[::-1]])
                run = []
        elif len(run) >= 2 and not(increase):
            if abs(array[start]) <= abs(run[-1]):
                run.append(array[start])
                start += 1
            elif abs(array[start]) > abs(run[-1]) and len(run) < max_size:
                for i in range(len(run)):
                    if abs(run[i]) < abs(array[start]):
                        run.insert(i, array[start])
                        start += 1
                        break
            else:
                my_stack.append([len(run), run])
                run = []

        if (len(run) < 2):
            run.append(array[start])
            start += 1

        if len(run) == 2:
            if abs(run[1]) > abs(run[0]):
                increase = 1
            else:
                increase = 0

        if start == len(array):
            if increase:
                my_stack.append([len(run), run[::-1]])
            else:
                my_stack.append([len(run), run])
            break

    for i in range(len(my_stack)):
        s = ' '.join(map(str, my_stack[i][1]))
        print(f'Part {i}: ' + s)

    my_stack = stack_merging(my_stack)

    return(' '.join(map(str, my_stack[0][1])))

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    print('Answer: ' + tim_sort(array))