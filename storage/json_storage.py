import json

from models.weather_entry import WeatherEntry


def save_entries(entries, filename):

    data = [entry.to_dict() for entry in entries]

    try:

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    except IOError:
        print("Error saving file")


def load_entries(filename):

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return [
            WeatherEntry.from_dict(item)
            for item in data
        ]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Invalid JSON format")
        return []
