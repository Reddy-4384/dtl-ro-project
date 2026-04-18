import matplotlib.pyplot as plt

def plot_route(locations, route):
    x = [locations[i][0] for i in route]
    y = [locations[i][1] for i in route]

    plt.plot(x, y, marker='o')
    plt.title("DTL-RO Optimized Route")
    plt.grid()
    plt.show()