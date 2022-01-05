from model.route_data import RouteData

# Constants
GAS_PER_KILOMETER = 0.056


#
def calculate_using_fixed_path_gas_station_problem_algorithm(route: RouteData) -> None:
    max_distance = route.fuel_tank_size / GAS_PER_KILOMETER

    for i in range(0, len(route.stops)):
        break
