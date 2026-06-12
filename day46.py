# Day 46 - Weather Forecast App

import requests

API_KEY = "YOUR_API_KEY"

class WeatherForecast:

    def get_weather(self, city):

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]

            print("\n===== WEATHER REPORT =====")
            print(f"City        : {city_name}")
            print(f"Temperature : {temperature}°C")
            print(f"Humidity    : {humidity}%")
            print(f"Condition   : {weather}")

        else:
            print("City not found or API issue.")


def main():

    print("===== WEATHER FORECAST APP =====")

    city = input("Enter city name: ")

    app = WeatherForecast()

    try:
        app.get_weather(city)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()