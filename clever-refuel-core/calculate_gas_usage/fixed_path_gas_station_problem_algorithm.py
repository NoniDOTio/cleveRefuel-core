#from model.vehicleroute import VehicleRoute
from model.vehicleroute import VehicleRoute

# Constants
GAS_PER_KILOMETER = 0.056


#
def calculate_using_fixed_path_gas_station_problem_algorithm(route: VehicleRoute) -> None:
    max_distance = route.tank_capacity / GAS_PER_KILOMETER

    for i in range(0, len(route.stops)):
        break
