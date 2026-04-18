def cost(route, dist):
    return sum(dist[route[i]][route[i+1]] for i in range(len(route) - 1))

def two_opt(route, dist):
    best = route
    for i in range(1, len(route) - 2):
        for j in range(i + 1, len(route)):
            new = route[:]
            new[i:j] = reversed(route[i:j])
            if cost(new, dist) < cost(best, dist):
                best = new
    return best