import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from datetime import datetime as dt

class DataHolder:
    def __init__(self) -> None:
        # monday 0 sunday 6
        self.weekdays = {
            0: {"total": 0, "points": 0},
            1: {"total": 0, "points": 0},
            2: {"total": 0, "points": 0},
            3: {"total": 0, "points": 0},
            4: {"total": 0, "points": 0},
            5: {"total": 0, "points": 0},
            6: {"total": 0, "points": 0}
        }

    def get_prices_formatted(self) -> list:
        all_prices = []

        for key in self.weekdays:
            data = self.weekdays[key]
            price = 0
            if (data["points"] != 0):
                price = (data['total'] / data["points"])
            all_prices.append(price)
        return all_prices

def get_tankstellen_dataframe() -> DataFrame:
    data = pd.read_csv("data/Tankstellen.csv", delimiter=";", names=[
        "id",
        "chain",
        "company",
        "road",
        "number",
        "zipcode",
        "place",
        "lat",
        "long"
    ])
    print(data.head())
    return data[:10] # TODO Remove slicing, only to test the first 5

def get_tankstellen_data(id) -> DataFrame:
    data = pd.read_csv(f"data/Benzinpreise/{id}.csv", delimiter=";", names=[
        "datetime",
        "price"
    ])
    return data

def process_price_data(row:Series, dh:DataHolder) -> Series:
    weekday = (dt.strptime(row["datetime"][:19], r"%Y-%m-%d %H:%M:%S")).weekday()
    dh.weekdays[weekday]["points"] += 1
    dh.weekdays[weekday]["total"] += int(row["price"])
    return row

def process_date_data(row:Series, dh:DataHolder):
    try:
        prices = get_tankstellen_data(row["id"])
        prices.apply(
            lambda dat_row: process_price_data(dat_row, dh), axis=1
        )
    except:
        pass
    return row

def showPlot():
    data = get_tankstellen_dataframe()

    # Getting data
    data_holder = DataHolder()
    data.apply(
        lambda row: process_date_data(row, data_holder), axis=1
    )

    # creating dataframe
    df = pd.DataFrame({
        'Weekday': ['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday", "Sunday"],
        'Price': data_holder.get_prices_formatted()
    })

    # plotting a bar graph
    df.plot(x="Weekday", y="Price", ylabel="Price", xlabel="")

    plt.show()