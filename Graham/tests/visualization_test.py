from src.main import StartPointSetting, InsertionSortByLeftSideStart, AngleSlicing, Area

from random import randint
from matplotlib import pyplot as plt
import numpy as np

def visualize_dots(dots, indexes):
    plt.figure()
    dots = np.array(dots)
    ordered_dots = dots[indexes]
    plt.plot(ordered_dots[:, 0], ordered_dots[:, 1], 'o-', color='b')
    plt.plot([ordered_dots[-1, 0], ordered_dots[0, 0]],
             [ordered_dots[-1, 1], ordered_dots[0, 1]], 'b-')
    for i in range(len(indexes)):
        current_index = indexes[i]
        next_index = indexes[(i + 1) % len(indexes)]
        current_point = dots[current_index]
        next_point = dots[next_index]
        plt.annotate("", xy=next_point, xytext=current_point,
                     arrowprops=dict(facecolor='blue', edgecolor='none', width=1, headwidth=10, headlength=10, shrink=0.05))
    all_indexes = list(range(len(dots)))
    unused_indexes = set(all_indexes) - set(indexes)
    unused_points = dots[list(unused_indexes)]
    plt.scatter(unused_points[:, 0], unused_points[:, 1], marker='o', color='g')
    for i, index in enumerate(indexes):
        point = dots[index]
        plt.text(point[0], point[1]+5, f'{index}', ha='center', va='top', fontsize=15)
    plt.xlim(np.min(dots[:, 0]) - 1, np.max(dots[:, 0]) + 1)
    plt.ylim(np.min(dots[:, 1]) - 1, np.max(dots[:, 1]) + 1)
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Многоугольник')
    plt.show()

def plot_first_step(dots):
    dots = np.array(dots)
    plt.figure()
    plt.grid()
    plt.plot(dots[:, 0], dots[:, 1], linestyle='none', marker='o', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Набор случайных точек')
    plt.show()

def plot_second_step(dots, indexes):
    dots = np.array(dots)
    dots = dots[indexes]
    plt.figure()
    plt.grid()
    plt.plot(dots[0][0], dots[0][1], linestyle='none', marker='o', color='red')
    plt.text(dots[0][0], dots[0][1] + 4, 'Самая левая точка', ha='center', va='bottom', fontsize=15)
    plt.plot(dots[:, 0][1:], dots[:, 1][1:], linestyle='none', marker='o', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Набор случайных точек')
    plt.show()

if __name__ == "__main__":
    dots_count = randint(10,50)
    dots = []
    for i in range(dots_count):
        dots.append([randint(1,100), randint(1,100)])

    n = len(dots)
    indexes = [i for i in range(n)]
    plot_first_step(dots)
    indexes = StartPointSetting(dots, indexes)
    plot_second_step(dots, indexes)
    indexes = InsertionSortByLeftSideStart(dots, indexes)
    visualize_dots(dots, indexes)
    indexes = AngleSlicing(dots, indexes)
    print(indexes)
    visualize_dots(dots, indexes)
    print(Area(dots, indexes))