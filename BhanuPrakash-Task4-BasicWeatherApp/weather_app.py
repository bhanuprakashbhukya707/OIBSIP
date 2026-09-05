import requests

API_KEY = "77086b26d9fda915b7807a7b708603aa"

city = input("Enter city name: ").strip()

if not city:
    print("Please enter a city name.")
else:
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n===== WEATHER REPORT =====")
            print("City:", city_name)
            print(f"Temperature: {temperature_c:.1f} °C")
            print(f"Temperature: {temperature_f:.1f} °F")
            print(f"Humidity: {humidity}%")
            print("Condition:", condition.title())
            print(f"Wind Speed: {wind_speed} m/s")
            print("==========================")

        elif response.status_code == 401:
            print("Error: Invalid API key.")

        elif response.status_code == 404:
            print("Error: City not found.")

        else:
            print("Error: Unable to fetch weather data.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")

    except requests.exceptions.RequestException:
        print("Error: Something went wrong.")