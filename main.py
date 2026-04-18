from data.models import Order, Vehicle
from routing.matrix import create_matrix
from routing.traffic import apply_traffic
from planner.advanced import AdvancedPlanner
from simulation.dynamic import add_order
from ui.visualization import plot_route
from ui.map_visualization import show_map
import pandas as pd

def main():
    print("DTL-RO SYSTEM STARTED\n")

    try:
        orders = []
        locations = [(0, 0)]

        n = int(input("Enter number of orders: "))

        for i in range(n):
            print(f"\nEnter details for Order {i+1}")

            lat_pick = float(input("Pickup Latitude: "))
            lng_pick = float(input("Pickup Longitude: "))
            lat_drop = float(input("Drop Latitude: "))
            lng_drop = float(input("Drop Longitude: "))
            weight = float(input("Weight: "))
            volume = float(input("Volume: "))

            order = Order(
                id=f"O{i+1}",
                pickup_location=(lat_pick, lng_pick),
                dropoff_location=(lat_drop, lng_drop),
                weight=weight,
                volume=volume,
                earliest_pickup_time="09:00",
                latest_delivery_time="12:00",
                service_time=5,
                priority=1
            )

            orders.append(order)
            locations.append(order.pickup_location)

        vehicle = Vehicle(
            id="V1",
            capacity_weight=100,
            capacity_volume=10,
            fixed_cost=100,
            cost_per_km=10,
            cost_per_min=2,
            start_location=(0, 0),
            end_location=(0, 0),
            shift_start="08:00",
            shift_end="18:00",
            current_state="idle"
        )

        print("\nOrders and Vehicle Initialized")

        dist_matrix, time_matrix = create_matrix(locations)

        if input("Apply traffic? (y/n): ").lower() == 'y':
            time_matrix = apply_traffic(time_matrix)

        if input("Add new order dynamically? (y/n): ").lower() == 'y':
            x = float(input("New order latitude: "))
            y = float(input("New order longitude: "))
            locations = add_order(locations, (x, y))

        planner = AdvancedPlanner()
        route = planner.plan(locations, dist_matrix)

        print("\nOptimized Route:", route)

        output_data = [
            {"node": i, "latitude": locations[i][0], "longitude": locations[i][1]}
            for i in route
        ]

        pd.DataFrame(output_data).to_csv("output.csv", index=False)
        print("Output saved to output.csv")

        plot_route(locations, route)
        show_map(locations, route)

    except Exception as e:
        print("\nError occurred:", e)

if __name__ == "__main__":
    main()