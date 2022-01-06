from model.route_data import RouteData
from forecast.naive_forecast import NaiveForecasts

# Constants
GAS_PER_KILOMETER = 0.056


#
def calculate_using_fixed_path_gas_station_problem_algorithm(route: RouteData, forecast: NaiveForecasts) -> None:
    max_distance = route.fuel_tank_size / GAS_PER_KILOMETER

    print("The algorithm has completed successfully!")

    for i in range(0, len(route.stops)):
        break
