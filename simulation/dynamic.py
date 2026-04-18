def add_order(route, new_node):
    print("Dynamic order inserted")
    route.insert(-1, new_node)
    return route