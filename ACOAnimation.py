import matplotlib.pyplot as plt
import numpy as np
import string
from matplotlib.animation import FuncAnimation
class ACOAnimation:
    def __init__(self, ant_colony, coords, distances):
        self.ant_colony = ant_colony
        self.coords = coords
        self.distances = distances

        self.fig_matrix, self.ax_matrix = plt.subplots(1, 1, figsize=(14, 8))
        self.fig_path, (self.ax, self.ax_best) = plt.subplots(2, 1, figsize=(10, 12))

        self.best_path = None
        self.best_path_length = float('inf')
        self.best_iteration = -1

    def init_plot(self):
        X, Y = self.coords[:, 0], self.coords[:, 1]
        self.ax.scatter(X, Y, c='red')
        labels = list(string.ascii_uppercase)
        for i, (x, y) in enumerate(zip(X, Y)):
            label = labels[i % len(labels)]
            self.ax.text(x, y, label, color='blue', fontsize=12, ha='right', va='bottom')

    def display_matrix(self):
        self.ax_matrix.imshow(self.distances, cmap='viridis', interpolation='nearest')
        self.ax_matrix.set_title("Distance Matrix", fontsize=14)

        labels = list(string.ascii_uppercase)
        num_vertices = len(self.distances)
        self.ax_matrix.set_xticks(np.arange(num_vertices))
        self.ax_matrix.set_yticks(np.arange(num_vertices))
        self.ax_matrix.set_xticklabels(labels[:num_vertices], fontsize=10)
        self.ax_matrix.set_yticklabels(labels[:num_vertices], fontsize=10)

    def plot_path(self, ax, path, path_color):
        for start, end in path:
            start_x, start_y = self.coords[start]
            end_x, end_y = self.coords[end]
            ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                        arrowprops=dict(arrowstyle="->", color=path_color))

    def update(self, frame):
        self.ax.clear()
        self.init_plot()

        try:
            all_paths = self.ant_colony.path_history[frame]
            path, path_length = min(all_paths, key=lambda x: x[1])
        except IndexError:
            print(f"Error: Frame {frame} is out of bounds in path_history.")
            return

        start_vertex = path[0][0]
        self.ax.scatter(self.coords[start_vertex][0], self.coords[start_vertex][1], c='green', s=70, marker='o')
        self.plot_path(self.ax, path, 'b')

        # Hiển thị thông số tiêu hao
        self.ax.set_title(f"Iteration {frame + 1}, Path Length: {path_length}")

        if path_length < self.best_path_length:
            self.best_path = path
            self.best_path_length = path_length
            self.best_iteration = frame
            self.update_best()

    def update_best(self):
        if self.best_path is not None:
            self.ax_best.clear()
            X, Y = self.coords[:, 0], self.coords[:, 1]
            self.ax_best.scatter(X, Y, c='red', s=50, marker='o', edgecolors='black')
            labels = list(string.ascii_uppercase)
            for i, (x, y) in enumerate(zip(X, Y)):
                label = labels[i % len(labels)]
                self.ax_best.text(x, y, label, color='blue', fontsize=12, ha='right', va='bottom')

            start_vertex = self.best_path[0][0]
            self.ax_best.scatter(self.coords[start_vertex][0], self.coords[start_vertex][1], c='green', s=70, marker='o')
            self.plot_path(self.ax_best, self.best_path, 'g')
            self.ax_best.set_title(f"Best Iteration - Iteration {self.best_iteration + 1}")

    def run(self):
        self.init_plot()
        anim_path = FuncAnimation(self.fig_path, self.update, frames=self.ant_colony.n_iterations, repeat=False)
        self.display_matrix()
        plt.show()
    def __init__(self, ant_colony, coords, distances):
        self.ant_colony = ant_colony
        self.coords = coords
        self.distances = distances

        # Tạo cửa sổ riêng biệt cho ma trận khoảng cách và tên đỉnh
        self.fig_matrix, self.ax_matrix = plt.subplots(1, 1, figsize=(14, 8))

        # Tạo cửa sổ cho biểu đồ đường đi
        self.fig_path, (self.ax, self.ax_best) = plt.subplots(2, 1, figsize=(10, 12))

        self.best_path = None
        self.best_path_length = float('inf')
        self.best_iteration = -1

    def init_plot(self):
        X, Y = self.coords[:, 0], self.coords[:, 1]
        self.ax.scatter(X, Y, c='red')
        labels = list(string.ascii_uppercase)
        for i, (x, y) in enumerate(zip(X, Y)):
            label = labels[i % len(labels)]
            self.ax.text(x, y, label, color='blue', fontsize=12, ha='right', va='bottom')

    def display_matrix(self):
        # Hiển thị ma trận khoảng cách dưới dạng heatmap
        self.ax_matrix.imshow(self.distances, cmap='viridis', interpolation='nearest')
        self.ax_matrix.set_title("Distance Matrix", fontsize=14)

        # Tạo nhãn cho các đỉnh
        labels = list(string.ascii_uppercase)
        num_vertices = len(self.distances)
        self.ax_matrix.set_xticks(np.arange(num_vertices))
        self.ax_matrix.set_yticks(np.arange(num_vertices))
        self.ax_matrix.set_xticklabels(labels[:num_vertices], fontsize=10)
        self.ax_matrix.set_yticklabels(labels[:num_vertices], fontsize=10)
        
    def plot_path(self, ax, path, path_color):
        for start, end in path:
            start_x, start_y = self.coords[start]
            end_x, end_y = self.coords[end]
            ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                        arrowprops=dict(arrowstyle="->", color=path_color))

    def update(self, frame):
        self.ax.clear()
        self.init_plot()

        try:
            all_paths = self.ant_colony.path_history[frame]
            path, path_length = min(all_paths, key=lambda x: x[1])
        except IndexError:
            print(f"Error: Frame {frame} is out of bounds in path_history.")
            return

        start_vertex = path[0][0]
        self.ax.scatter(self.coords[start_vertex][0], self.coords[start_vertex][1], c='green', s=70, marker='o')
        self.plot_path(self.ax, path, 'b')
        self.ax.set_title(f"Iteration {frame + 1}, Path Length: {path_length}")

        if path_length < self.best_path_length:
            self.best_path = path
            self.best_path_length = path_length
            self.best_iteration = frame
            self.update_best()

    def update_best(self):
        if self.best_path is not None:
            self.ax_best.clear()
            X, Y = self.coords[:, 0], self.coords[:, 1]
            self.ax_best.scatter(X, Y, c='red', s=50, marker='o', edgecolors='black')
            labels = list(string.ascii_uppercase)
            for i, (x, y) in enumerate(zip(X, Y)):
                label = labels[i % len(labels)]
                self.ax_best.text(x, y, label, color='blue', fontsize=12, ha='right', va='bottom')

            start_vertex = self.best_path[0][0]
            self.ax_best.scatter(self.coords[start_vertex][0], self.coords[start_vertex][1], c='green', s=70, marker='o')
            self.plot_path(self.ax_best, self.best_path, 'g')
            self.ax_best.set_title(f"Best Iteration - Iteration {self.best_iteration + 1}")

    def run(self):
        self.init_plot()
        anim_path = FuncAnimation(self.fig_path, self.update, frames=self.ant_colony.n_iterations, repeat=False)
        self.display_matrix()
        plt.show()