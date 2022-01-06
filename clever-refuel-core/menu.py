from data_reader import DataReader
from model.route_data import RouteData
import processing_routines as pr

class Menu:
    def __init__(self) -> None:
        self.data_reader = DataReader()
        self.options = {
            "Analyze Naively" : pr.AnalyzeWithNaiveForecastOnNaiveRoute,
            "Analyze with Brandwide Forecast on Naive Route" : pr.AnalyzeWithBrandwideForecastOnNaiveRoute,
            "Analyze using Fixed Path Gas Station Problem Algorithm with Naive Forecast" : pr.AnalyzeWithFixedPathGasStationProblem,
            "Analyze using Fixed Path Gas Station Problem Algorithm with Brandwide Forecast" : pr.AnalyzeBrandwideWithFixedPathGasStationProblem,
        }
        self.route_folder = "data/Fahrzeugrouten"
        print("---- Clever Refuel Core ----", end="\n\n\n")
        route_data = self.get_route()
        print("\n\n")
        processing_type = self.get_processing_type()

        print("\n\n")
        print("---- Starte Analyze... ----", end="\n\n")
        if not processing_type.run(route_data):
            print("Huch da ist bei der Verarbeitung was falsch gelaufen")


    def get_route(self) -> RouteData:
        print("---- Routen Auswahl ----")
        all_routes = self.data_reader.get_all_routes()
        for route_index, route_name in enumerate(all_routes):
            print("(", route_index + 1, ") ", route_name)
        print()
        selected = self.get_user_input_int(
            "Welche Route moechtest du verwenden?",
            len(all_routes)
        ) - 1
        print()
        selected_route = all_routes[selected]
        return self.data_reader.get_route_data(selected_route)


    def get_processing_type(self) -> pr.BaseProcessingType:
        print("---- Auswertungsverfahren Auswahl ----")
        for option_index, option_name in enumerate(self.options.keys()):
            print("(", option_index + 1, ") ", option_name)
        print()
        selected = self.get_user_input_int(
            "Wie soll die verwendete Route verarbeitet werden?",
            len(list(self.options.keys()))
        ) - 1
        print()
        return self.options[list(self.options.keys())[selected]]

    def get_user_input_int(self, prompt, upper_bound) -> int:
        selected = 0
        while selected <= 0 or selected > upper_bound:
            raw_user_input = input(f"{prompt}\n")
            if raw_user_input.isdigit():
                selected = int(raw_user_input)
            else:
                print("Bitte gib eine Zahl ein")
        return selected