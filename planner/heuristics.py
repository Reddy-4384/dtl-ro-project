import math

def greedy_route(locations):
    n = len(locations)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0

    for _ in range(n - 1):
        nearest = min(
            [i for i in range(n) if not visited[i]],
            key=lambda i: math.dist(locations[current], locations[i])
        )
        route.append(nearest)
        visited[nearest] = True
        current = nearest

    route.append(0)
    return route