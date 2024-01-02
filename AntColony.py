import random as rn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.random import choice as np_choice

class AntColony(object):

    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Đối số:
            distances (2D numpy.array): Ma trận vuông chứa khoảng cách giữa các điểm. Đường chéo của ma trận được giả định là np.inf.
            n_ants (int): Số lượng kiến chạy trong mỗi lần lặp
            n_best (int): Số lượng kiến tốt nhất (có đường đi ngắn nhất) gửi mùi sau mỗi lần lặp
            n_iteration (int): Số lần lặp
            decay (float): Tỷ lệ giảm mùi pheromone sau mỗi lần lặp. Giá trị mùi pheromone sẽ được nhân với decay, vì vậy 0.95 sẽ dẫn đến sự giảm nhẹ, 0.5 sẽ giảm nhanh hơn.
            alpha (int hoặc float): Số mũ cho pheromone, alpha càng cao thì pheromone có trọng số càng lớn. Mặc định=1
            beta (int hoặc float): Số mũ cho khoảng cách, beta càng cao thì khoảng cách có trọng số càng lớn. Mặc định=1

        Example:
            ant_colony = AntColony(german_distances, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        """
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        self.path_history = []  # Thêm dòng này để lưu trữ lịch sử đường đi
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths() # Tạo ra tất cả các đường đi của kiến trong lần lặp hiện tại và lưu chúng vào biến
            self.path_history.append(all_paths)  # Thêm danh sách các đường đi trong lần lặp này vào lịch sử các đường đi
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            print (shortest_path)
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone = self.pheromone * self.decay            
        return all_time_shortest_path

    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move