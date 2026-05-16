from datetime import datetime


class WeatherEntry:

    def __init__(
        self,
        date,
        temperature,
        description,
        precipitation
    ):

        self.date = self.validate_date(date)

        self.temperature = (
            self.validate_temperature(
                temperature
            )
        )

        self.description = description
        self.precipitation = precipitation

    def validate_date(self, date_string):

        try:

            return datetime.strptime(
                date_string,
                "%Y-%m-%d"
            )

        except ValueError:

            raise ValueError(
                "Invalid date format. Use YYYY-MM-DD"
            )

    def validate_temperature(
        self,
        temperature
    ):

        if temperature is None:

            raise ValueError(
                "Temperature cannot be empty"
            )

        try:

            return float(temperature)

        except (
            ValueError,
            TypeError
        ):

            raise ValueError(
                "Temperature must be a number"
            )

    def to_dict(self):

        return {

            "date": self.date.strftime(
                "%Y-%m-%d"
            ),

            "temperature": self.temperature,

            "description": self.description,

            "precipitation": self.precipitation
        }

    @classmethod
    def from_dict(cls, data):

        return cls(

            data["date"],

            data["temperature"],

            data["description"],

            data["precipitation"]
        )

    def __str__(self):

        return (

            f"Date: "
            f"{self.date.strftime('%Y-%m-%d')}, "

            f"Temperature: "
            f"{self.temperature}°C, "

            f"Description: "
            f"{self.description}, "

            f"Precipitation: "
            f"{self.precipitation}"
        )
