from modules.stack_merging import stack_merging
from modules.min_run import min_run
def tim_sort(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return str(arr[0])

    my_stack = []

    max_size = min_run(len(arr))
    run = []

    increase = 1
    start = 0
    while(start < len(arr)):

        if len(run) >= 2 and increase:
            if abs(arr[start]) > abs(run[-1]):
                run.append(arr[start])
                start += 1
            elif abs(arr[start]) <= abs(run[-1]) and len(run) < max_size:
                for i in range(len(run)):
                    if abs(run[i]) >= abs(arr[start]):
                        run.insert(i, arr[start])
                        start += 1
                        break
            else:
                my_stack.append([len(run), run[::-1]])
                run = []
        elif len(run) >= 2 and not(increase):
            if abs(arr[start]) <= abs(run[-1]):
                run.append(arr[start])
                start += 1
            elif abs(arr[start]) > abs(run[-1]) and len(run) < max_size:
                for i in range(len(run)):
                    if abs(run[i]) < abs(arr[start]):
                        run.insert(i, arr[start])
                        start += 1
                        break
            else:
                my_stack.append([len(run), run])
                run = []

        if (len(run) < 2):
            run.append(arr[start])
            start += 1

        if len(run) == 2:
            if abs(run[1]) > abs(run[0]):
                increase = 1
            else:
                increase = 0

        if start == len(arr):
            if increase:
                my_stack.append([len(run), run[::-1]])
            else:
                my_stack.append([len(run), run])
            break

    my_stack = stack_merging(my_stack)

    return(' '.join(map(str, my_stack[0][1])))