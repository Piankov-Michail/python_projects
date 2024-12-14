import pytest
from random import randint
from src.RabinKarp import RabinKarp, hash
alphabet = 'abcdefghigklmnopqrstuvwzyz'
@pytest.mark.parametrize('size', [10,50,100,200,1000])
def test(size):
    s = ''
    for i in range(size):
        s += alphabet[randint(1,100)%len(alphabet)]
    m = randint(1, (size) // 10)
    start = randint(1, (size) // 2)
    w = s[start: start + m]
    print(w, s)
    data = RabinKarp(w, s)
    if data != '':
        ans = list(map(int, data.split(' ')))
        for i in ans:
            assert s[i:i+m] == w