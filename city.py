class City:
    def __init__(self, name, country_code, temperature, humidity, weather_conditions):
        self.name = name
        self.country_code = country_code
        self.temperature = temperature
        self.humidity = humidity
        self.weather_conditions = weather_conditions

    def __str__(self):
        return f"{self.name}, {self.country_code} - {self.temperature}°C, {self.humidity}%, {self.weather_conditions}"

# Example usage
city = City("Athens", "GR", 25, 50, "Cloudy")
print(city)
