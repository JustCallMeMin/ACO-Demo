import numpy as np
from AntColony import AntColony
from ACOAnimation import ACOAnimation
from sklearn.manifold import MDS

def generate_random_distances(num_cities, min_distance, max_distance, seed=None):
    if seed is not None:
        np.random.seed(seed)

    distances = np.empty((num_cities, num_cities), dtype=float)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = np.random.randint(min_distance, max_distance)
            distances[i, j] = distance
            distances[j, i] = distance

    np.fill_diagonal(distances, np.inf)
    return distances

# Generate a random distance matrix
num_cities = 15
min_distance = 1
max_distance = 6  # Đặt là 6 để sinh ra các số từ 1 đến 5
random_seed = 42
distances = generate_random_distances(num_cities, min_distance, max_distance, random_seed)

# Replace np.inf with large values for MDS
distances_for_mds = np.where(distances == np.inf, 1000, distances)

# Use MDS to generate coordinates
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=1)
coords = mds.fit_transform(distances_for_mds)

# Initialize and run AntColony
ant_colony = AntColony(distances, 10, 5, 100, 0.95, alpha=1, beta=2)
shortest_path = ant_colony.run()
print("shorted_path: {}".format(shortest_path))

# Initialize and run ACOAnimation
aco_anim = ACOAnimation(ant_colony, coords, distances)
aco_anim.run()
