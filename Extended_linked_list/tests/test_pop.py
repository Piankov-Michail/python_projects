import pytest
from random import randint
from src.main_lb1 import Extended_Linked_List



@pytest.mark.parametrize('cnt',[10,20,30,100,101])
def test_pop_back(cnt):
    ell_1 = Extended_Linked_List()
    lst = list()
    for i in range(100):
        ell_1.push_back(i)
        lst.append(i)
    for i in range(cnt):
        if ell_1.length <= 0:
            assert ell_1.pop_back() == None
        elif ell_1.length >= 0:
            temp = lst[-1]
            ell_1.pop_back()
            lst.pop()
            assert ell_1.search(ell_1.length - 1) != temp

@pytest.mark.parametrize('cnt',[10,20,30,100,101])
def test_pop_front(cnt):
    ell_1 = Extended_Linked_List()
    lst = list()
    for i in range(100):
        ell_1.push_back(i)
        lst.append(i)
    for i in range(cnt):
        if ell_1.length <= 0:
            assert ell_1.pop_front() == None
        elif ell_1.length >= 0:
            temp = lst[0]
            ell_1.pop_front()
            lst.pop(0)
            assert ell_1.search(0) != temp

ell = Extended_Linked_List()
for i in range(100):
    ell.push_back(i)

@pytest.mark.parametrize('index',[-1] + [i for i in range(150)])
def test_pop(index):
    if index < 0 or index > ell.length - 1 or ell.length == 0:
        assert ell.pop(index) == None
    else:
        temp = ell.search(index)
        ell.pop(index)
        assert ell.search(index) != temp

del ell
ell = Extended_Linked_List()
for i in range(100):
    ell.push_back(i)

@pytest.mark.parametrize('value',[i for i in range(150)])
def test_pop_by_value_first(value):
    if ell.search_by_value_first(value) == None:
        assert ell.pop_by_value_first(value) == None
    else:
        index = ell.search_by_value_first(value)
        ell.pop_by_value_first(value)
        assert ell.search(index) != value

ell = Extended_Linked_List()
for i in range(100):
    ell.push_back(i)

@pytest.mark.parametrize('value',[-1] + [i for i in range(150)])
def test_pop_by_value_last(value):
    if ell.search_by_value_last(value) == None:
        assert ell.pop_by_value_last(value) == None
    else:
        index = ell.search_by_value_last(value)
        ell.pop_by_value_last(value)
        assert ell.search(index) != value

del ell
ell = Extended_Linked_List()
for i in range(100):
    ell.push_back(i)
    ell.push_back(i-1)

@pytest.mark.parametrize('value',[randint(i-5, i+5) for i in range(30)])
def test_pop_by_value_all(value):
    if ell.search_by_value_all(value) == None:
        assert ell.pop_by_value_all(value) == None
    else:
        ell.pop_by_value_all(value)
        assert ell.search_by_value_all(value) == None