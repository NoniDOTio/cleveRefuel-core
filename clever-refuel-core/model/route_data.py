from datetime import datetime
import pandas as pd
pd.options.mode.chained_assignment = None

"""
Enthaelt die Daten ueber die abgefahrene Route

raw_data die Daten wie sie raw in der Datei stehen
data Die Tankstellen wie sie abzufahren sind. columns: ['time', 'fuel-station']
fuel_tank_size Die Groesse des Treibstofftanks
"""
class RouteData:
    def __init__(self, route_path : str) -> None:
        self.path = route_path

        self.raw_data = pd.read_csv(
            route_path,
            delimiter=";",
            names=["time", "fuel-station"]
        )
        self.data = self.raw_data[1:]
        self.data['time'] = self.data['time'].map(
            lambda time: datetime.strptime(time + "00", "%Y-%m-%d %H:%M:%S%z")
        )
        self.data['fuel-station'] = self.data['fuel-station'].map(
            lambda station: int(station)
        )
        self.fuel_tank_size = float(self.raw_data['time'][0])
        self.stops = []