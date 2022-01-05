import os
import csv

from fixed_path_gas_station_problem_algorithm import *
from naive import *
from csv_parser import read_route_file


if __name__ == "__main__":
    route = read_route_file("../../data/Fahrzeugrouten/Bertha Benz Memorial Route.csv")

    calculate_naively(route)
    calculate_using_fixed_path_gas_station_problem_algorithm(route)
