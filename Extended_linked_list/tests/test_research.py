import time
import psutil
from math import ceil
process = psutil.Process()
from src.main_lb1 import Extended_Linked_List
from modules.linked_list import Linked_List
import matplotlib.pyplot as plt

max_value = 2_000_000_0
number_of_elements = [10] + [10000] + [100000]

i = 100000

while(i < max_value):
    number_of_elements.append(i)
    i += ceil(i**0.85)

extended_linked_list_data = {
    'push_back' : [[], []],
    'push_middle' : [[], []],
    'push_front' : [[], []],
    'pop_back' : [[], []],
    'pop_front' : [[], []],
    'pop_middle': [[], []],
    'search_back': [[], []],
    'search_front': [[], []],
    'search_middle': [[], []],
    'memory' : [[], []]
}

linked_list_data = {
    'push_back' : [[], []],
    'push_middle' : [[], []],
    'push_front' : [[], []],
    'pop_back' : [[], []],
    'pop_front' : [[], []],
    'pop_middle': [[], []],
    'search_back': [[], []],
    'search_front': [[], []],
    'search_middle': [[], []],
    'memory': [[], []]
}

python_list_data = {
    'push_back' : [[], []],
    'push_middle' : [[], []],
    'push_front' : [[], []],
    'pop_back' : [[], []],
    'pop_front' : [[], []],
    'pop_middle': [[], []],
    'search_back': [[], []],
    'search_front': [[], []],
    'search_middle': [[], []],
    'memory': [[], []]
}

line_width = 3

def test_extended_linked_list():
    ell = Extended_Linked_List(auto_balance_flag=False)
    start_size = process.memory_info().rss
    for i in range(max_value):
        ell.push_back(0)
        if i in number_of_elements:
            start = time.time()
            ell.push_back(-1000)
            end = time.time() - start
            extended_linked_list_data['push_back'][0].append(end)
            extended_linked_list_data['push_back'][1].append(i)

            start = time.time()
            ell.push_front(-1000)
            end = time.time() - start
            extended_linked_list_data['push_front'][0].append(end)
            extended_linked_list_data['push_front'][1].append(i)

            start = time.time()
            ell.insert(ell.length // 2, -1000)
            end = time.time() - start
            extended_linked_list_data['push_middle'][0].append(end)
            extended_linked_list_data['push_middle'][1].append(i)

            start = time.time()
            ell.pop_back()
            end = time.time() - start
            extended_linked_list_data['pop_back'][0].append(end)
            extended_linked_list_data['pop_back'][1].append(i)

            start = time.time()
            ell.pop(ell.length // 2)
            end = time.time() - start
            extended_linked_list_data['pop_middle'][0].append(end)
            extended_linked_list_data['pop_middle'][1].append(i)

            start = time.time()
            ell.pop_front()
            end = time.time() - start
            extended_linked_list_data['pop_front'][0].append(end)
            extended_linked_list_data['pop_front'][1].append(i)

            start = time.time()
            x = ell.get_last()
            end = time.time() - start
            extended_linked_list_data['search_back'][0].append(end)
            extended_linked_list_data['search_back'][1].append(i)

            start = time.time()
            x = ell.search(ell.length // 2)
            end = time.time() - start
            extended_linked_list_data['search_middle'][0].append(end)
            extended_linked_list_data['search_middle'][1].append(i)

            start = time.time()
            x = ell.get_first()
            end = time.time() - start
            extended_linked_list_data['search_front'][0].append(end)
            extended_linked_list_data['search_front'][1].append(i)

            end_size = process.memory_info().rss - start_size
            extended_linked_list_data['memory'][0].append(end_size)
            extended_linked_list_data['memory'][1].append(i)
            ell.balance()

def test_python_list():
    lst = []
    start_size = process.memory_info().rss
    for i in range(max_value):
        lst.append(0)
        if i in number_of_elements:
            start = time.time()
            lst.append(-1000)
            end = time.time() - start
            python_list_data['push_back'][0].append(end)
            python_list_data['push_back'][1].append(i)

            start = time.time()
            lst.insert(0, -1000)
            end = time.time() - start
            python_list_data['push_front'][0].append(end)
            python_list_data['push_front'][1].append(i)

            start = time.time()
            lst.insert(len(lst) // 2, -1000)
            end = time.time() - start
            python_list_data['push_middle'][0].append(end)
            python_list_data['push_middle'][1].append(i)

            start = time.time()
            lst.pop()
            end = time.time() - start
            python_list_data['pop_back'][0].append(end)
            python_list_data['pop_back'][1].append(i)

            start = time.time()
            lst.pop(len(lst) // 2)
            end = time.time() - start
            python_list_data['pop_middle'][0].append(end)
            python_list_data['pop_middle'][1].append(i)

            start = time.time()
            lst.pop(0)
            end = time.time() - start
            python_list_data['pop_front'][0].append(end)
            python_list_data['pop_front'][1].append(i)

            start = time.time()
            x = lst[-1]
            end = time.time() - start
            python_list_data['search_back'][0].append(end)
            python_list_data['search_back'][1].append(i)

            start = time.time()
            x = lst[len(lst) // 2]
            end = time.time() - start
            python_list_data['search_middle'][0].append(end)
            python_list_data['search_middle'][1].append(i)

            start = time.time()
            x = lst[0]
            end = time.time() - start
            python_list_data['search_front'][0].append(end)
            python_list_data['search_front'][1].append(i)

            end_size = process.memory_info().rss - start_size
            python_list_data['memory'][0].append(end_size)
            python_list_data['memory'][1].append(i)

def test_linked_list():
    ell = Linked_List()
    start_size = abs(process.memory_info().rss)
    start_size = abs(process.memory_info().rss)
    start_size = abs(process.memory_info().rss)
    for i in range(max_value):
        ell.push_back(0)
        if i in number_of_elements:
            start = time.time()
            ell.push_back(-1000)
            end = time.time() - start
            linked_list_data['push_back'][0].append(end)
            linked_list_data['push_back'][1].append(i)

            start = time.time()
            ell.push_front(-1000)
            end = time.time() - start
            linked_list_data['push_front'][0].append(end)
            linked_list_data['push_front'][1].append(i)

            start = time.time()
            ell.insert(ell.length // 2, -1000)
            end = time.time() - start
            linked_list_data['push_middle'][0].append(end)
            linked_list_data['push_middle'][1].append(i)

            start = time.time()
            ell.pop_back()
            end = time.time() - start
            linked_list_data['pop_back'][0].append(end)
            linked_list_data['pop_back'][1].append(i)

            start = time.time()
            ell.pop(ell.length // 2)
            end = time.time() - start
            linked_list_data['pop_middle'][0].append(end)
            linked_list_data['pop_middle'][1].append(i)

            start = time.time()
            ell.pop_front()
            end = time.time() - start
            linked_list_data['pop_front'][0].append(end)
            linked_list_data['pop_front'][1].append(i)

            start = time.time()
            x = ell.get_last()
            end = time.time() - start
            linked_list_data['search_back'][0].append(end)
            linked_list_data['search_back'][1].append(i)

            start = time.time()
            x = ell.search(ell.length // 2)
            end = time.time() - start
            linked_list_data['search_middle'][0].append(end)
            linked_list_data['search_middle'][1].append(i)

            start = time.time()
            x = ell.get_first()
            end = time.time() - start
            linked_list_data['search_front'][0].append(end)
            linked_list_data['search_front'][1].append(i)

            end_size = abs(process.memory_info().rss - start_size)
            end_size = abs(process.memory_info().rss - start_size)
            end_size = abs(process.memory_info().rss - start_size)
            linked_list_data['memory'][0].append(end_size)
            linked_list_data['memory'][1].append(i)

def test_graphics():
    plt.figure()
    plt.subplot(1,3,1)
    plt.title('push_back')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['push_back'][1], extended_linked_list_data['push_back'][0], color = 'orange', label = 'Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['push_back'][1], linked_list_data['push_back'][0], color='green', label = 'Linked_List', linewidth=line_width)
    plt.plot(python_list_data['push_back'][1], python_list_data['push_back'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)

    plt.subplot(1,3,2)
    plt.title('push_middle')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['push_front'][1], extended_linked_list_data['push_middle'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['push_middle'][1], linked_list_data['push_middle'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['push_middle'][1], python_list_data['push_middle'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)

    plt.subplot(1,3,3)
    plt.title('push_front')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['push_front'][1], extended_linked_list_data['push_front'][0], color = 'orange', label = 'Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['push_front'][1], linked_list_data['push_front'][0], color='green', label = 'Linked_List', linewidth=line_width)
    plt.plot(python_list_data['push_front'][1], python_list_data['push_front'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)
    plt.show()

    plt.figure()
    plt.subplot(1, 3, 1)
    plt.title('pop_back')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['pop_back'][1], extended_linked_list_data['pop_back'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['pop_back'][1], linked_list_data['pop_back'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['pop_back'][1], python_list_data['pop_back'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)

    plt.subplot(1, 3, 2)
    plt.title('pop_middle')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['pop_middle'][1], extended_linked_list_data['pop_middle'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['pop_middle'][1], linked_list_data['pop_middle'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['pop_middle'][1], python_list_data['pop_middle'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)

    plt.subplot(1, 3, 3)
    plt.title('pop_front')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['pop_front'][1], extended_linked_list_data['pop_front'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['pop_front'][1], linked_list_data['pop_front'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['pop_front'][1], python_list_data['pop_front'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)
    plt.show()

    plt.figure()
    plt.subplot(1, 3, 1)
    plt.title('search_back')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['search_back'][1], extended_linked_list_data['search_back'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['search_back'][1], linked_list_data['search_back'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['search_back'][1], python_list_data['search_back'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)

    plt.subplot(1, 3, 2)
    plt.title('search_middle')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['search_middle'][1], extended_linked_list_data['search_middle'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['search_middle'][1], linked_list_data['search_middle'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['search_middle'][1], python_list_data['search_middle'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)

    plt.subplot(1, 3, 3)
    plt.title('search_front')
    plt.grid()
    plt.ylabel('Время')
    plt.xlabel('Кол-во элементов')
    plt.ylim(0)
    plt.plot(extended_linked_list_data['search_front'][1], extended_linked_list_data['search_front'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['search_front'][1], linked_list_data['search_front'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['search_front'][1], python_list_data['search_front'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)
    plt.show()

    plt.figure()
    plt.title('memory_usage')
    plt.grid()
    plt.ylabel('Мегабайты')
    plt.xlabel('Кол-во элементов')
    plt.plot(extended_linked_list_data['memory'][1], extended_linked_list_data['memory'][0], color='orange', label='Extended_Linked_List', linewidth=line_width)
    plt.plot(linked_list_data['memory'][1], linked_list_data['memory'][0], color='green', label='Linked_List', linewidth=line_width)
    plt.plot(python_list_data['memory'][1], python_list_data['memory'][0], color='blue', label='python_list', linewidth=line_width)
    plt.legend(fontsize=10)

    plt.show()
