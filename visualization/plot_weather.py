import matplotlib.pyplot as plt


def plot_temperature(entries):

    if not entries:
        print("No weather entries to display")
        return

    dates = [
        entry.date.strftime("%Y-%m-%d")
        for entry in entries
    ]

    temperatures = [
        entry.temperature
        for entry in entries
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
