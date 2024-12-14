from modules.avl_tree import AVLTree
import time
import matplotlib.pyplot as plt
insertion = {'time': [],
             'size': []}
pop = {
    'pop_min': [],
    'pop_max': [],
    'pop': [],
    'size': []
}
max_size = 5_000_00
galop = 2_000_0


def insertion_speed():
    tree = AVLTree()
    for i in range(max_size):
        if i % galop == 0:
            start = time.perf_counter()
            tree.insert(i)
            insertion['time'].append(time.perf_counter() - start)
            insertion['size'].append(i)
        else:
            tree.insert(i)


def pop_speed():
    tree = AVLTree()
    for i in range(max_size):
        tree.insert(i)
    for i in range(max_size):
        if i % galop == 0:
            res = []
            for j in range(5):
                start = time.perf_counter()
                tree.pop_min()
                res.append(time.perf_counter() - start)
                tree.insert(i)
            pop['pop_min'].append(sum(res) / len(res))
            tree.pop_min()
        else:
            tree.pop_min()
    for i in range(max_size):
        tree.insert(i)
    for i in range(max_size):
        if i % galop == 0:
            res = []
            for j in range(5):
                start = time.perf_counter()
                tree.pop_max()
                res.append(time.perf_counter() - start)
                tree.insert(max_size - i)
            pop['pop_max'].append(sum(res) / len(res))
            tree.pop_max()
        else:
            tree.pop_max()
    for i in range(max_size):
        tree.insert(i)
    for i in range(max_size):
        if i % galop == 0:
            res = []
            for j in range(5):
                start = time.perf_counter()
                tree.pop((i + max_size) // 2)
                res.append(time.perf_counter() - start)
                tree.insert((i + max_size) // 2)
            tree.pop((i + max_size) // 2)
            pop['pop'].append(sum(res) / len(res))
            pop['size'].append(i)
        else:
            tree.pop_max()


if __name__ == "__main__":
    insertion_speed()
    plt.grid()
    plt.title('График зависимости скорости вставки от количества элементов')
    plt.ylabel('Время, мкс')
    plt.xlabel('Кол-во элементов')
    plt.plot(insertion['size'], insertion['time'], color='green', linewidth=3, label='insertion')
    plt.legend()
    plt.show()

    pop_speed()
    plt.grid()
    plt.title('График зависимости скорости удаления от количества элементов')
    plt.ylabel('Время, мкс')
    plt.xlabel('Кол-во элементов')
    plt.plot(pop['size'][:-1], pop['pop_min'][::-1][:-1], color='green', linewidth=2, label='pop_min')
    plt.plot(pop['size'][:-1], pop['pop_max'][::-1][:-1], color='blue', linewidth=2, label='pop_max')
    plt.plot(pop['size'][:-1], pop['pop'][::-1][:-1], color='gray', linewidth=2, label='pop')
    plt.legend()
    plt.show()
