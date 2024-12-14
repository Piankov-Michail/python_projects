import random
import pytest
from src.main_lb1 import Extended_Linked_List

@pytest.mark.parametrize('func',[lambda x : x%2 ==0, lambda x : x%3 == 0, lambda x : x > 5 and x < 15])
def test_filter(func):
    ell = Extended_Linked_List()
    lst = list()
    for i in range(100):
        ell.push_back(i)
        lst.append(i)
    lst = list(filter(func, lst))
    ell.filter(func)
    for i in range(ell.length):
        assert ell.search(i) == lst[i]

@pytest.mark.parametrize('node_size',[1,2,3,4,5,10,20])
def test_balance(node_size):
    ell = Extended_Linked_List(auto_balance_flag=False)
    for i in range(100):
        ell.push_back(i)
    ell.balance(node_size)
    assert ell.node_size == node_size and len(ell.__head__.data) <= (node_size + 1) // 2

@pytest.mark.parametrize('cnt',[10,20,30,100])
def test_iadd(cnt):
    data_1 = list()
    data_2 = list()
    ell = Extended_Linked_List()
    lst = Extended_Linked_List()
    for i in range(cnt//2):
        x = random.randint(i-10, i+10)
        data_1.append(x)
        ell.push_back(x)
    for i in range(cnt//2, cnt):
        x = random.randint(i-10, i+10)
        data_2.append(x)
        lst.push_back(x)
    ell += lst
    data_1 += data_2
    for i in range(cnt):
        assert ell.search(i) == data_1[i]

@pytest.mark.parametrize('cnt',[10,20,30,100])
def test_deep_copy(cnt):
    ell = Extended_Linked_List()
    for i in range(cnt + 10):
        ell.push_back(i)
    lst = ell.__deepcopy__()
    for i in range(cnt):
        assert ell.search(i) == lst.search(i)
    for i in range(cnt):
        ell.insert(i, i*100 + 1)
    for i in range(lst.length):
        assert ell.search(i) != lst.search(i)
