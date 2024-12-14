from linked_list import Linked_List
from src.main_cw import HashTable, Student
from random import randint
import time
import matplotlib.pyplot as plt

ranges = [10, 1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 90000,
          130000, 160000, 190000, 240000, 280000, 350000, 400000, 450000,
          500000, 600000, 650000, 700000, 800000, 900000, 1_000_000,
          1_200_000, 1_400_000, 1_600_000, 1_800_000, 2_000_000, 2_500_000,
          3_000_000, 3_500_000, 4_000_000, 4_500_000, 5_000_000, 6_000_000,
          7_000_000, 8_000_000, 9_000_000, 10_000_000]

hash_table_insertion_speed = []
python_dictionary_insertion_speed = []
linked_list_insertion_speed = []

hash_table_pop_speed = []
python_dictionary_pop_speed = []
linked_list_pop_speed = []

hash_table_search_speed = []
python_dictionary_search_speed = []
linked_list_search_speed = []

hash_table_update_speed = []
python_dictionary_update_speed = []
linked_list_update_speed = []


def research(sizes):
    test_hash_table = HashTable(max_size=max(sizes)*2)
    linked_list = Linked_List()
    dictionary = dict()

    name = 'Infinity'
    age = 42
    special = 'abcdefg'
    name2 = 'Infinity2'
    student = Student(name, age, special)
    update_student = Student(name2, age, special)

    for i in range(max(sizes)+1):
        student_id = str(i)
        if i in ranges:
            start = time.perf_counter()
            test_hash_table.insert(student_id, student)
            hash_table_insertion_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            dictionary[student_id] = student
            python_dictionary_insertion_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            linked_list.push_back(student_id)
            linked_list_insertion_speed.append(time.perf_counter() - start)
        else:
            test_hash_table.insert(student_id, student)
            dictionary[student_id] = student
            linked_list.push_back(student_id)

        if i in ranges:
            start = time.perf_counter()
            test_hash_table.search(student_id)
            hash_table_search_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            dictionary.get(student_id)
            python_dictionary_search_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            linked_list.search(randint(0, linked_list.length - 1))
            linked_list_search_speed.append(time.perf_counter() - start)

            start = time.perf_counter()
            test_hash_table.update(student_id, update_student)
            hash_table_update_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            dictionary[student_id] = 'Updated'
            python_dictionary_update_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            linked_list.update(randint(0, linked_list.length - 1), 'Updated')
            linked_list_update_speed.append(time.perf_counter() - start)

    for i in range(max(sizes)+1):
        student_id = str(i)
        start = time.perf_counter()
        test_hash_table.erase(student_id)
        if i in ranges:
            hash_table_pop_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            dictionary[student_id] = None
            python_dictionary_pop_speed.append(time.perf_counter() - start)
            start = time.perf_counter()
            linked_list.pop(randint(0, linked_list.length - 1))
            linked_list_pop_speed.append(time.perf_counter() - start)


research(ranges)

line_width = 5
plt.figure()

plt.subplot(2, 2, 1)
plt.title('insertion')
plt.grid()
plt.ylabel('Время')
plt.xlabel('Кол-во элементов')
plt.ylim(0)
plt.plot(ranges, hash_table_insertion_speed, color='blue', label='hash table', linewidth=line_width)
plt.plot(ranges, python_dictionary_insertion_speed, color='green', label='python dict', linewidth=line_width)
plt.plot(ranges, linked_list_insertion_speed, color='orange', label='linked list', linewidth=line_width)
plt.legend(fontsize=10)

plt.subplot(2, 2, 2)
plt.title('search')
plt.grid()
plt.ylabel('Время')
plt.xlabel('Кол-во элементов')
plt.ylim(0)
plt.plot(ranges, hash_table_search_speed, color='blue', label='hash table', linewidth=line_width)
plt.plot(ranges, python_dictionary_search_speed, color='green', label='python dict', linewidth=line_width)
plt.plot(ranges, linked_list_search_speed, color='orange', label='linked list', linewidth=line_width)
plt.legend(fontsize=10)

plt.subplot(2, 2, 3)
plt.title('update')
plt.grid()
plt.ylabel('Время')
plt.xlabel('Кол-во элементов')
plt.ylim(0)
plt.plot(ranges, hash_table_update_speed, color='blue', label='hash table', linewidth=line_width)
plt.plot(ranges, python_dictionary_update_speed, color='green', label='python dict', linewidth=line_width)
plt.plot(ranges, linked_list_update_speed, color='orange', label='linked list', linewidth=line_width)
plt.legend(fontsize=10)

plt.subplot(2, 2, 4)
plt.title('pop')
plt.grid()
plt.ylabel('Время')
plt.xlabel('Кол-во элементов')
plt.ylim(0)
plt.plot(ranges[::-1], hash_table_pop_speed, color='blue', label='hash table', linewidth=line_width)
plt.plot(ranges[::-1], python_dictionary_pop_speed, color='green', label='python dict', linewidth=line_width)
plt.plot(ranges[::-1], linked_list_pop_speed, color='orange', label='linked list', linewidth=line_width)
plt.legend(fontsize=10)

plt.show()

print(hash_table_insertion_speed[-1], hash_table_insertion_speed[-6], hash_table_insertion_speed[-17])
print(hash_table_search_speed[-1], hash_table_search_speed[-6], hash_table_search_speed[-17])
print(hash_table_update_speed[-1], hash_table_update_speed[-6], hash_table_update_speed[-17])
print(hash_table_pop_speed[-1], hash_table_pop_speed[-6], hash_table_pop_speed[-17])
print('\n')
print(python_dictionary_insertion_speed[-1], python_dictionary_insertion_speed[-6], python_dictionary_insertion_speed[-17])
print(python_dictionary_search_speed[-1], python_dictionary_search_speed[-6], python_dictionary_search_speed[-17])
print(python_dictionary_update_speed[-1], python_dictionary_update_speed[-6], python_dictionary_update_speed[-17])
print(python_dictionary_pop_speed[-1], python_dictionary_pop_speed[-6], python_dictionary_pop_speed[-17])
print('\n')
print(linked_list_insertion_speed[-1], linked_list_insertion_speed[-6], linked_list_insertion_speed[-17])
print(linked_list_search_speed[-1], linked_list_search_speed[-6], linked_list_search_speed[-17])
print(linked_list_update_speed[-1], linked_list_update_speed[-6], linked_list_update_speed[-17])
print(linked_list_pop_speed[-1], linked_list_pop_speed[-6], linked_list_pop_speed[-17])
