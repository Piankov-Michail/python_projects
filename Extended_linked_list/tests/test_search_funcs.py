import pytest
from src.main_lb1 import Extended_Linked_List

ell = Extended_Linked_List()
lst = list()

for i in range(30):
    ell.push_back(i)
    lst.append(i)

@pytest.mark.parametrize('index', [-1] + [i for i in range(30)] + [31] + [100])
def test_search(index):
    if index < 0 or index > ell.length:
        assert ell.search(index) == None
    else:
        assert ell.search(index) == lst[index]

@pytest.mark.parametrize('data', [10,20,30])
def test_get_last(data):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(data):
        ell.push_back(i)
        lst.append(i)
    assert ell.get_last() == lst[-1]

@pytest.mark.parametrize('data', [10,20,30])
def test_get_first(data):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(data):
        ell.push_back(i)
        lst.append(i)
    assert ell.get_first() == lst[0]

@pytest.mark.parametrize('value', [i for i in range(50)])
def test_search_by_value_first(value):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(50):
        ell.push_back(i)
        lst.append(i)
    for i in range(50):
        ell.push_back(i)
        lst.append(i)
    assert ell.search_by_value_first(value) == lst.index(value)

@pytest.mark.parametrize('value', [i for i in range(50)])
def test_search_by_value_last(value):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(50):
        ell.push_back(i)
        lst.append(i)
    for i in range(50):
        ell.push_back(i)
        lst.append(i)
    assert ell.search_by_value_last(value) != lst.index(value) and ell.search(ell.search_by_value_last(value)) == lst[value]

@pytest.mark.parametrize('value', [1,5,7,10])
def test_search_by_value_all(value):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(50):
        ell.push_back(i)
        lst.append(i)
    for i in range(50):
        ell.push_back(i)
        lst.append(i)
    data = list()
    for i in range(len(lst)):
        if lst[i] == value:
            data.append(i)
    assert ell.search_by_value_all(value) == data
