import pytest
from src.main_lb1 import Extended_Linked_List

@pytest.mark.parametrize('value', [10,30,50])
def test_push_back(value):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(value):
        ell.push_back(i)
        lst.append(i)
        assert ell.search(ell.length - 1) == lst[-1]

@pytest.mark.parametrize('value', [10,30,50])
def test_push_front(value):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(value):
        ell.push_front(i)
        lst.insert(0, i)
        assert ell.search(0) == lst[0]

ell = Extended_Linked_List()
lst = list()

@pytest.mark.parametrize('index, value', [[-1, -1]] + [[i, i] for i in range(50)] + [[52, 52]]+ [[100, 100]])
def test_insert(index, value):
    if index < 0 or index > ell.length:
        assert ell.insert(index, value) == None
    else:
        ell.insert(index, value)
        lst.insert(index, value)
        assert ell.search(index) == lst[index]
