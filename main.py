from models.weather_entry import WeatherEntry

from storage.json_storage import (
    save_entries,
    load_entries
)

from visualization.plot_weather import (
    plot_temperature
)


def display_entries(entries):

    if not entries:

        print("No entries found")
        return

    for index, entry in enumerate(entries):

        print(f"{index + 1}. {entry}")


def filter_by_temperature(
    entries,
    minimum
):

    return [

        entry

        for entry in entries

        if entry.temperature >= minimum
    ]


def filter_by_date(
    entries,
    target_date
):

    return [

        entry

        for entry in entries

        if entry.date.strftime("%Y-%m-%d")
        == target_date
    ]


def main():

    entries = load_entries(
        "weather_data.json"
    )

    while True:

        print("\nWEATHER DIARY")

        print("1. Add entry")
        print("2. View entries")
        print("3. Delete entry")
        print("4. Filter by date")
        print("5. Filter by temperature")
        print("6. Show graph")
        print("7. Save")
        print("8. Exit")

        choice = input(
            "Choose option: "
        )

        if choice == "1":

            try:

                date = input(
                    "Enter date (YYYY-MM-DD): "
                )

                temperature = input(
                    "Enter temperature: "
                )

                description = input(
                    "Enter description: "
                )

                precipitation = input(
                    "Enter precipitation: "
                )

                entry = WeatherEntry(
                    date,
                    temperature,
                    description,
                    precipitation
                )

                entries.append(entry)

                print("Entry added")

            except ValueError as error:

                print(error)

        elif choice == "2":

            display_entries(entries)

        elif choice == "3":

            if not entries:

                print("No entries to delete")
                continue

            display_entries(entries)

            try:

                index = int(
                    input(
                        "Enter entry number: "
                    )
                )

                entries.pop(index - 1)

                print("Entry deleted")

            except (
                ValueError,
                IndexError
            ):

                print("Invalid entry number")

        elif choice == "4":

            try:

                target_date = input(
                    "Enter date (YYYY-MM-DD): "
                )

                WeatherEntry(
                    target_date,
                    0,
                    "",
                    ""
                )

                filtered = filter_by_date(
                    entries,
                    target_date
                )

                display_entries(filtered)

            except ValueError as error:

                print(error)

        elif choice == "5":

            try:

                minimum = float(

                    input(
                        "Minimum temperature: "
                    )
                )

                filtered = (
                    filter_by_temperature(
                        entries,
                        minimum
                    )
                )

                display_entries(filtered)

            except ValueError:

                print(
                    "Invalid temperature"
                )

        elif choice == "6":

            plot_temperature(entries)

        elif choice == "7":

            save_entries(
                entries,
                "weather_data.json"
            )

            print("Data saved")

        elif choice == "8":

            save_entries(
                entries,
                "weather_data.json"
            )

            print("Program closed")

            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
