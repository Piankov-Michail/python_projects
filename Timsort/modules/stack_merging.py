from modules.merge import merge

def stack_merging(my_stack):
    data = my_stack
    my_stack = []
    counter = 0
    for i in data:
        my_stack.append(i)
        while (len(my_stack) > 1):
            if len(my_stack) > 2 and not (my_stack[-3][0] > my_stack[-1][0] + my_stack[-2][0]):
                if my_stack[-3][0] < my_stack[-1][0]:
                    my_stack[-2][1] = merge(my_stack[-3][1], my_stack[-2][1])
                    counter += 1
                    my_stack[-2][0] = len(my_stack[-2][1])
                    my_stack.pop(-3)
                else:
                    my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
                    counter += 1
                    my_stack[-2][0] = len(my_stack[-2][1])
                    my_stack.pop(-1)

            if not (my_stack[-2][0] > my_stack[-1][0]):
                my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
                counter += 1
                my_stack[-2][0] = len(my_stack[-2][1])
                my_stack.pop(-1)
            else:
                break

    while (len(my_stack) > 1):
        if len(my_stack) > 2:
            if my_stack[-3] < my_stack[-1]:
                my_stack[-2][1] = merge(my_stack[-3][1], my_stack[-2][1])
                counter += 1
                my_stack[-2][0] = len(my_stack[-2][1])
                my_stack.pop(-3)
            else:
                my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
                counter += 1
                my_stack[-2][0] = len(my_stack[-2][1])
                my_stack.pop(-1)
        if len(my_stack) > 1:
            my_stack[-2][1] = merge(my_stack[-2][1], my_stack[-1][1])
            counter += 1
            my_stack[-2][0] = len(my_stack[-2][1])
            my_stack.pop(-1)
    return my_stack