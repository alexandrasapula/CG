import matplotlib.pyplot as plt
import os


def read_file(filename):
    """
    Зчитування точок з файлу
    :param filename: Ім'я вхідного файлу
    :return: Список точок (x, y).
    """
    if not os.path.exists(filename):
        print(f"Файл {filename} не знайдено")
        return []

    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            points.append((x, y))
    return points


def save_plot(output_filename):
    """
    Збереження графіку у файл
    :param output_filename: Ім'я вихідного файлу
    """
    plt.savefig(output_filename, format="png")
    print(f"Графік збережено як {output_filename}")


def andrews_algorithm(points):
    """
    Реалізація алгоритму Ендрю для знаходження опуклої оболонки
    :param points: Список точок (x, y)
    :return: Список точок, що формують опуклу оболонку
    """
    points = sorted(points)  # Сортуємо точки за координатою x, а у випадку рівності — за координатою y

    def half_hull(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and (hull[-1][0] - hull[-2][0]) * (p[1] - hull[-2][1]) - (hull[-1][1] - hull[-2][1]) * (p[0] - hull[-2][0]) <= 0:
                hull.pop()
            hull.append(p)
        return hull

    lower = half_hull(points)  # Нижня частина оболонки
    upper = half_hull(points[::-1])  # Верхня частина оболонки

    return lower[:-1] + upper[:-1]  # Видаляємо повторювані точки


def save_hull_dataset(points, output_filename):
    """
    Зберігає точки опуклої оболонки у файл
    :param points: Список точок (x, y)
    :param output_filename: Ім'я вихідного файлу для збереження
    """
    with open(output_filename, 'w') as file:
        for x, y in points:
            file.write(f"{x} {y}\n")
    print(f"Точки опуклої оболонки збережено у {output_filename}")


def main():
    # Ім'я вхідного файлу
    input_file = 'DS3.txt'
    points = read_file(input_file)

    # Знаходження опуклої оболонки
    hull_points = andrews_algorithm(points)

    # Збереження опуклої оболонки у файл
    save_hull_dataset(hull_points, "hull_dataset.txt")

    # Параметри графіка
    width = 960
    height = 540
    point_color = 'red'
    point_marker = 'o'
    line_color = 'blue'
    dpi = 100

    # Створення графіка
    plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    plt.gca().axis('off')

    # Відображення точок
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, c=point_color, marker=point_marker)

    # Відображення опуклої оболонки
    hull_x, hull_y = zip(*(hull_points + [hull_points[0]]))
    plt.plot(hull_x, hull_y, c=line_color)

    # Збереження графіку
    save_plot("output_file.png")


if __name__ == "__main__":
    main()
