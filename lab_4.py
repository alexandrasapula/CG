import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.cluster import DBSCAN


def load_dataset(file_path):
    data = np.loadtxt(file_path)
    return data


def find_clusters(data):
    db = DBSCAN(eps=5, min_samples=5)
    clusters = db.fit_predict(data)
    return clusters


def calculate_centroids(data, clusters):
    centroids = []
    unique_clusters = np.unique(clusters)
    for cluster in unique_clusters:
        if cluster != -1:
            cluster_points = data[clusters == cluster]
            centroid = np.mean(cluster_points, axis=0)
            centroids.append(centroid)
    return np.array(centroids)


def voronoi_diagram(centroids, canvas_size=(960, 540)):
    vor = Voronoi(centroids)

    fig, ax = plt.subplots(figsize=(canvas_size[0] / 100, canvas_size[1] / 100), dpi=100)

    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_width=1, line_colors='blue', zorder=1)

    return fig, ax


def plot_results(data, centroids, canvas_size=(960, 540)):
    fig, ax = voronoi_diagram(centroids, canvas_size)

    ax.scatter(centroids[:, 0], centroids[:, 1], color='red', s=20, zorder=2)

    ax.scatter(data[:, 0], data[:, 1], color='black', alpha=0.1, s=2, zorder=0)

    ax.set_xlim([0, canvas_size[0]])
    ax.set_ylim([0, canvas_size[1]])
    ax.set_aspect('equal')
    ax.axis('off')

    return fig


def save_plot(fig, output_path):
    fig.savefig(output_path, format='png')


def main():
    file_path = "DS3.txt"
    data = load_dataset(file_path)

    clusters = find_clusters(data)

    centroids = calculate_centroids(data, clusters)

    fig = plot_results(data, centroids)

    output_path = "voronoi_diagram.png"
    save_plot(fig, output_path)


if __name__ == "__main__":
    main()
