import matplotlib.pyplot as plt
import os


def read_file(filename):
    """
    Читання точок з файлу
    :param filename: Ім'я вхідного файлу
    :return: Список точек (x, y).
    """
    if not os.path.exists(filename):
        print(f"Файл {filename} не знайден")
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
    print(f"Файл збережен як {output_filename}")


def main():
    # Ім'я вхідного файлу
    input_file = 'DS3.txt'
    points = read_file(input_file)

    # Параметри графіка
    width = 960
    height = 540
    point_color = 'blue'
    point_marker = 'o'
    dpi = 100

    # Створення графіка
    plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    plt.gca().axis('off')

    # Відображення точок
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, c=point_color, marker=point_marker)

    # Збереження графіка
    save_plot("output_file.png")


if __name__ == "__main__":
    main()
