import pytest

from src.main import Graham, DotLeftSide

from random import randint

@pytest.mark.parametrize('size', [5, 10, 15, 20])
def test(size):
    dots = []
    for i in range(size):
        dot = [randint(1, 100), randint(1, 100)]
        while dot in dots:
            dot = [randint(1, 100), randint(1, 100)]
        dots.append(dot)
    indexes = Graham(dots)
    minimal_convex_hull = [dots[i] for i in indexes]
    remaining_dots = list(filter(lambda x: not(x in minimal_convex_hull), dots))
    for i in range(0, len(minimal_convex_hull)):
        for j in range(len(remaining_dots)):
            assert DotLeftSide(minimal_convex_hull[i-1], minimal_convex_hull[i], remaining_dots[j]) > 0
