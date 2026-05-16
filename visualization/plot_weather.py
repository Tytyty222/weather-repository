import matplotlib.pyplot as plt


def plot_temperature(entries):

    if not entries:

        print("No weather entries to display")
        return

    sorted_entries = sorted(
        entries,
        key=lambda entry: entry.date
    )

    dates = [

        entry.date.strftime("%Y-%m-%d")

        for entry in sorted_entries
    ]

    temperatures = [

        entry.temperature

        for entry in sorted_entries
    ]

    plt.figure(figsize=(8, 5))

    plt.plot(
        dates,
        temperatures,
        marker="o"
    )

    plt.xlabel("Date")

    plt.ylabel("Temperature")

    plt.title("Temperature by Date")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()
