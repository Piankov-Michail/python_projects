import time
import matplotlib.pyplot as plt
from modules.timsort import tim_sort
import numpy as np

n = 0.87
max_numbers = 1_000_000_0
increase_lst = [i for i in range(max_numbers)]
decrease_list = [max_numbers - i for i in range(max_numbers)]
random_list = list(np.random.randint(-10000, 10000, max_numbers).tolist())
random_with_incr_list = []
while(len(random_with_incr_list) < max_numbers):
    random_with_incr_list.extend([i for i in range(np.random.randint(1,int(max_numbers**0.2), 1)[0])])

increase_lst_times = []
decrease_lst_times = []
random_lst_times = []
random_with_incr_list_times = []
numbers = []

def test_increase_list_sort():
    arr = increase_lst
    i = 1
    while(i < len(arr)):
        start = time.perf_counter()
        result = (tim_sort(arr[:i]))
        increase_lst_times.append(time.perf_counter() - start)
        numbers.append(i)
        i += int(i**n)

def test_dencrease_list_sort():
    arr = decrease_list
    i = 1
    while (i < len(arr)):
        start = time.perf_counter()
        result = (tim_sort(arr[:i]))
        decrease_lst_times.append(time.perf_counter() - start)
        i += int(i ** n)

def test_random_list_sort():
    arr = random_list
    i = 1
    while (i < len(arr)):
        start = time.perf_counter()
        result = (tim_sort(arr[:i]))
        random_lst_times.append(time.perf_counter() - start)
        i += int(i ** n)

def test_random_with_inc_decr_list_sort():
    arr = random_with_incr_list
    i = 1
    while (i < len(arr)):
        start = time.perf_counter()
        result = (tim_sort(arr[:i]))
        random_with_incr_list_times.append(time.perf_counter() - start)
        i += int(i ** n)

def test_graphs():
    plt.grid()
    plt.ylabel('Время')
    #plt.ylim(0)
    plt.xlabel('Кол-во элементов')
    plt.plot(numbers, increase_lst_times, color='green', linewidth=3, label='increase_lst')
    plt.plot(numbers, decrease_lst_times, color='blue', linewidth=3, label='decrease_lst')
    plt.plot(numbers, random_lst_times, color='black', linewidth=3, label='random_lst')
    plt.plot(numbers, random_with_incr_list_times, color='gray', linewidth=3, label='random_with_sorted_lst')
    plt.legend()
    #plt.semilogy()
    plt.show()