from planner.heuristics import greedy_route
from planner.local_search import two_opt

class AdvancedPlanner:
    def plan(self, locations, dist):
        print("Running Multi-Algorithm Planner")

        route = greedy_route(locations)
        route = two_opt(route, dist)

        return route