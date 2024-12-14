def DotLeftSide(first, second, third):
    left = (second[0] - first[0]) * (third[1] - second[1]) - (second[1] - first[1]) * (third[0] - second[0])
    if left < 0:
        return -1
    return 1


def StartPointSetting(dots, indexes):
    for i in range(1, len(dots)):
        if dots[indexes[i]][0] < dots[indexes[0]][0]:
            indexes[i], indexes[0] = indexes[0], indexes[i]
    return indexes


def InsertionSortByLeftSideStart(dots, indexes):
    for i in range(2, len(indexes)):
        j = i
        while j > 1 and DotLeftSide(dots[indexes[0]], dots[indexes[j - 1]], dots[indexes[j]]) <= 0:
            indexes[j], indexes[j - 1] = indexes[j - 1], indexes[j]
            j -= 1
    return indexes


def AngleSlicing(dots, indexes):
    result = [indexes[0], indexes[1]]
    for i in range(2, len(dots)):
        while DotLeftSide(dots[result[-2]], dots[result[-1]], dots[indexes[i]]) < 0:
            result.pop()
        result.append(indexes[i])
    return result


def Graham(dots):
    n = len(dots)
    indexes = [i for i in range(n)]
    indexes = StartPointSetting(dots, indexes)
    indexes = InsertionSortByLeftSideStart(dots, indexes)
    return AngleSlicing(dots, indexes)


def Area(dots, indexes):
    square = 0
    for i in range(len(indexes)):
        x1, y1 = dots[indexes[i]]
        x2, y2 = dots[indexes[(i + 1) % len(indexes)]]
        square += x1 * y2 - x2 * y1
    return abs(square) / 2


if __name__ == "__main__":
    n = int(input())
    dots = []
    for i in range(n):
        x, y = list(map(int, input().split(', ')))
        dots.append([x, y])
    indexes = Graham(dots)
    print(([dots[i] for i in indexes], Area(dots, indexes)))
