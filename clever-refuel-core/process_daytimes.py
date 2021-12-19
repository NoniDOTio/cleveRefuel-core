import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import csv
import os


def main():
    limiter = 10000
    folder = "data/Benzinpreise"
    parsed_values = initialize_dict()

    i = 1
    for path in os.listdir(folder):
        if i > limiter:
            break

        if not path.endswith(".csv"):
            break

        with open(os.path.join(folder, path), "r") as file:
            reader = csv.reader(file, delimiter=";")

            for i, line in enumerate(reader):
                if i > limiter:
                    break
                hour_of_the_day = int(extract_hour_from_datetime(line[0]))
                price = int(line[1])
                parsed_values[hour_of_the_day].append(price)
        i += 1

    # plot data
    last_calculated_average = 0
    plot_data = {}
    for hour in parsed_values:
        try:
            last_calculated_average = sum(parsed_values[hour]) / len(parsed_values[hour])
        except ZeroDivisionError:
            last_calculated_average = last_calculated_average
        plot_data[hour] = last_calculated_average
    print(plot_data)

    # Make plot
    plt.style.use('_mpl-gallery')
    plt.plot(plot_data.keys(), plot_data.values())
    plt.show()


def extract_hour_from_datetime(str):
    try:
        # datetime_object = datetime.strptime(str, '%Y-%m-%d %H:%M:%S+%Z')
        # return datetime_object.hour
        return str[11:13]
    except ValueError:
        print('Invalid datetime string')
        return -1


def initialize_dict():
    d = {}
    for i in range(0, 24):
        d[i] = []
    return d