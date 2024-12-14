import pytest
from src.main_cw import Student, HashTable
from random import randint


@pytest.mark.parametrize('size', [10, 100, 200, 500, 1000, 2000, 10000, 20000])
def test_search(size):
    ids = []
    test_hash_table = HashTable()
    for i in range(size):
        name = ''.join([chr(randint(0, 127)) for _ in range(randint(3, 15))])
        age = randint(15, 40)
        special = ''.join([chr(randint(0, 127)) for _ in range(randint(10, 25))])
        student = Student(name, age, special)
        student_id = str(randint(1, 1_000_000))
        ids.append(student_id)
        test_hash_table.insert(student_id, student)
    for i in ids:
        key_hash = test_hash_table.hash_function(i)
        assert any([j[1] == test_hash_table.search(i) for j in test_hash_table.data[key_hash]])


@pytest.mark.parametrize('size', [10, 100, 200, 500, 1000, 2000, 10000, 20000])
def test_insert(size):
    ids = []
    dictionary = dict()
    test_hash_table = HashTable()
    for i in range(size):
        name = ''.join([chr(randint(0, 127)) for _ in range(randint(3, 15))])
        age = randint(15, 40)
        special = ''.join([chr(randint(0, 127)) for _ in range(randint(10, 25))])
        student = Student(name, age, special)
        student_id = str(randint(1, 1_000_000))
        while student_id in ids:
            student_id = str(randint(1, 1_000_000))
        test_hash_table.insert(student_id, student)
        dictionary[student_id] = student
        ids.append(str(student_id))
    for i in ids:
        assert test_hash_table.search(i) == dictionary[i]


@pytest.mark.parametrize('size', [10, 100, 200, 500, 1000, 2000, 10000, 20000])
def test_pop(size):
    ids = []
    test_hash_table = HashTable()
    dictionary = dict()
    for i in range(size):
        name = ''.join([chr(randint(0, 127)) for _ in range(randint(3, 15))])
        age = randint(15, 40)
        special = ''.join([chr(randint(0, 127)) for _ in range(randint(10, 25))])
        student = Student(name, age, special)
        student_id = str(randint(1, 1_000_000))
        test_hash_table.insert(student_id, student)
        dictionary[student_id] = student
        ids.append(str(student_id))
    for i in ids:
        test_hash_table.erase(i)
        assert test_hash_table.search(i) is None


@pytest.mark.parametrize('size', [10, 100, 200, 500, 1000, 2000, 10000, 20000])
def test_update(size):
    ids = []
    test_hash_table = HashTable()
    dictionary = dict()
    for i in range(size):
        name = ''.join([chr(randint(0, 127)) for _ in range(randint(3, 15))])
        age = randint(15, 40)
        special = ''.join([chr(randint(0, 127)) for _ in range(randint(10, 25))])
        student = Student(name, age, special)
        student_id = str(randint(1, 1_000_000))
        while student_id in ids:
            student_id = str(randint(1, 1_000_000))
        test_hash_table.insert(student_id, student)
        dictionary[student_id] = student
        ids.append(str(student_id))
    for i in range(len(ids)):
        temp = test_hash_table.search(ids[i])
        test_hash_table.update(ids[i], test_hash_table.search(ids[-i]))
        test_hash_table.update(ids[-i], temp)
        dictionary[ids[i]] = dictionary[ids[-i]]
        dictionary[ids[-i]] = temp
    for i in ids:
        assert test_hash_table.search(i) == dictionary[i]
