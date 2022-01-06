from model.route_data import RouteData
from calculate_gas_usage.distance_utils import distance_between
from calculate_gas_usage.constants import GAS_PER_KILOMETER
from forecast.base_forecast import BaseForecast


"""
Durchläuft eine Fahrzeugroute und schlägt eine naive Tankstrategie vor
"""
def calculate_naively(route: RouteData, forecast: BaseForecast) -> None:
    max_possible_distance = route.fuel_tank_size / GAS_PER_KILOMETER
    money_spent_on_refueling = 0
    total_refueled = 0
    current_fuel = 0

    # Loop through all stops in route
    for i in range(0, len(route.stops) - 1):
        current_stop = route.stops[i]
        next_stop = route.stops[i+1]

        if i == len(route.stops) + 1:
            km_to_next_stop = 0
        else:
            km_to_next_stop = distance_between(route.stops[i], route.stops[i+1])

        fuel_to_next_stop = km_to_next_stop * GAS_PER_KILOMETER

        print(current_stop.meta.name, "-->", next_stop.meta.name, f"({round(km_to_next_stop, 2)}km)")
        print("Fuel required to next stop:", round(fuel_to_next_stop, 2), "liters")
        print("Current fuel: " + str(round(current_fuel, 2)) + " out of " + str(round(route.fuel_tank_size, 2)) + "")

        if current_fuel < fuel_to_next_stop:
            # Refuel to max tank capacity
            price_prediction = forecast.get_forecast_for(current_stop)
            amount_to_refuel = route.fuel_tank_size - current_fuel
        # Determine distance to destination
        km_to_destination = 0
        j = i
        while km_to_destination < max_possible_distance:
            if j + 1 >= len(route.stops):
                break
            km_to_destination += distance_between(route.stops[j], route.stops[j + 1])
            if km_to_destination > max_possible_distance:
                break
            j += 1

        if current_fuel < fuel_to_next_stop and i < len(route.stops) - 2:
            price_prediction = forecast.get_forecast_for(current_stop)

            # If destination is in reach, only refuel the necessary amount
            if km_to_destination < max_possible_distance:
                amount_to_refuel = (km_to_destination * GAS_PER_KILOMETER) - current_fuel
            # Otherwise refuel to max tank capacity
            else:
                amount_to_refuel = route.fuel_tank_size - current_fuel

            refuel_cost = amount_to_refuel * price_prediction
            money_spent_on_refueling += refuel_cost
            total_refueled += amount_to_refuel
            current_fuel = current_fuel + amount_to_refuel

            print("Refueling", round(amount_to_refuel, 2), "litres for", round(refuel_cost / 100, 2), "€")

        current_fuel -= fuel_to_next_stop
        print("")

    print("Total refueled:", round(total_refueled, 2), "liters - Total money spend on refueling:", round(money_spent_on_refueling / 100, 2), "€")
