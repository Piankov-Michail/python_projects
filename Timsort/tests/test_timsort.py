import pytest

from modules.timsort import tim_sort

arrs = [[1,2,3], [4,5,6], [1,0,15,6,1,6,8,1,6,3,7,9,1,10],
        [0,10,5,1,67,1,7,9,10],[1,1,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,1]
        ]

@pytest.mark.parametrize('arr',arrs)
def test_timsort(arr):
    assert tim_sort(arr) == ' '.join(map(str, sorted(arr)[::-1]))
