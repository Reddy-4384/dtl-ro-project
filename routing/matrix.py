import numpy as np

def create_matrix(locations):
    n = len(locations)
    dist_matrix = np.zeros((n, n))
    time_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            dist = np.linalg.norm(
                np.array(locations[i]) - np.array(locations[j])
            )
            dist_matrix[i][j] = dist
            time_matrix[i][j] = dist * 1.2

    return dist_matrix, time_matrix