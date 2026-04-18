import folium

def show_map(locations, route):
    m = folium.Map(location=locations[0], zoom_start=12)

    for i, loc in enumerate(locations):
        folium.Marker(loc, popup=f"Node {i}").add_to(m)

    route_coords = [locations[i] for i in route]
    folium.PolyLine(route_coords, color="blue").add_to(m)

    m.save("route_map.html")
    print("Map saved as route_map.html")