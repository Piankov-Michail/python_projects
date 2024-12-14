def min_run(size):
    result = 0
    while (size >= 64):
        result |= (size & 1)
        size >>= 1
    return result + size