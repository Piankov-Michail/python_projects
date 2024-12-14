import pytest

from modules.avl_tree import AVLTree

sizes = [10, 100, 1000]


@pytest.mark.parametrize('size', sizes)
def test_insert(size):
    check_arr = []
    tree = AVLTree()
    for i in range(size):
        check_arr.append(i)
        tree.insert(i)
    assert tree.in_order(tree.root) == ' '.join(map(str, check_arr))


values = [i for i in range(-100, 100)]


@pytest.mark.parametrize('value', values)
def test_pop(value):
    tree = AVLTree()
    for i in range(-100, 100):
        tree.insert(i)
    assert tree.search(value) is True
    tree.pop(value)
    assert tree.search(value) is False


sizes = [10, 25, 50, 100]


@pytest.mark.parametrize('size', sizes)
def test_pop_min_max(size):
    tree = AVLTree()
    check_arr = []
    for i in range(-size, size):
        check_arr.append(i)
        tree.insert(i)
    for i in range(size):
        assert tree.search(min(check_arr)) is True
        tree.pop_min()
        assert tree.search(min(check_arr)) is False
        check_arr.pop(check_arr.index(min(check_arr)))
    tree = AVLTree()
    check_arr = []
    for i in range(-size, size):
        check_arr.append(i)
        tree.insert(i)
    for i in range(size):
        assert tree.search(max(check_arr)) is True
        tree.pop_max()
        assert tree.search(max(check_arr)) is False
        check_arr.pop(check_arr.index(max(check_arr)))
