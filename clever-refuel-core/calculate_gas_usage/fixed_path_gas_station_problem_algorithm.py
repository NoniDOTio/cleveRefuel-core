from model.route_data import RouteData
from calculate_gas_usage.distance_utils import distance_between
from calculate_gas_usage.constants import GAS_PER_KILOMETER
from forecast.base_forecast import BaseForecast


def calculate_using_fixed_path_gas_station_problem_algorithm(route: RouteData, forecast: BaseForecast) -> None:
    max_possible_distance = route.fuel_tank_size / GAS_PER_KILOMETER
    prices = []
    distances = []
    optimal_stops = {}

    money_spent_on_refueling = 0
    total_refueled = 0
    current_fuel = 0

    # Get necessary data
    for i in range(0, len(route.stops) - 1):
        # Store price prediction
        forecasted_price = forecast.get_forecast_for(route.stops[i])
        prices.append(forecasted_price)

        # Store distance to following stop, except for last stop
        if i == len(route.stops) - 1:
            break
        distance_to_next = distance_between(route.stops[i], route.stops[i + 1])
        distances.append(distance_to_next)

    print(prices)
    print(distances)
    print(len(route.stops))
    print(max_possible_distance)

    # Loop through all gas stations starting from destination
    i = len(route.stops) - 2
    while i > 0:
        print("Current stop", i)

        # Loop through stations that are within max_possible_distance
        distance = 0
        cheapest_gas_station_index = None
        cheapest_gas_station_distance = None
        for j in range(i-1, 0, -1):
            distance += distances[j]

            # Initialize cheapest gas station with closes gas station
            if j == i-1:
                cheapest_gas_station_index = j
                cheapest_gas_station_distance = distance

            print("Checking", j, "Distance:", distance, "Price:", prices[j])

            # Quit loop if max_possible_distance is exceeded
            if distance > max_possible_distance:
                break

            # Replace cheapest gas station with j if it's cheaper
            if prices[j] < prices[cheapest_gas_station_index]:
                cheapest_gas_station_index = j
                cheapest_gas_station_distance = distance

        # Debug
        print("Cheapest gas station is", cheapest_gas_station_index)
        print("Distance to it", cheapest_gas_station_distance)
        print("")
        print("")

        optimal_stops[cheapest_gas_station_index] = prices[cheapest_gas_station_index] * (cheapest_gas_station_distance * GAS_PER_KILOMETER)
        i = cheapest_gas_station_index

    print(optimal_stops)




