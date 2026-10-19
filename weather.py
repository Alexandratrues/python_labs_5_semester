import requests
from datetime import datetime

city_name = input("введите город (на английском): ")
try:
    data = datetime.strptime(input("введите день на который нужна погода ГГГГ-ММ-ДД: "), "%Y-%m-%d").date()
except ValueError:
    print("напишите дату в таком виде: ГГГГ-ММ-ДД")
    exit()
today = datetime.today().date()

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city_name, "count": 1, "language": "ru", "format": "json"}
geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()
if "results" not in geo_data:
    print(f"{city_name} не существует")
    exit()

latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]
found_city_name = geo_data["results"][0]["name"]
country = geo_data["results"][0].get("country", "")
print(f"найден: {found_city_name} ({country}), координаты: {latitude}, {longitude}")

if data < today:
    weather_url = "https://open-meteo.com"
else:
    weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": data,
    "end_date": data,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "auto",
}

weather_response = requests.get(weather_url, params=weather_params)

if weather_response.status_code != 200:
    print("загадывать больше, чем на 16 дней вперед нельзя")
    exit()

weather_data = weather_response.json()

temp_max = weather_data["daily"]["temperature_2m_max"][0]
temp_min = weather_data["daily"]["temperature_2m_min"][0]
precip = weather_data["daily"]["precipitation_sum"][0]

print(f"погода в г.{found_city_name} на {data}:")
print(f"максимальная температура: {temp_max} градусов")
print(f"минимальная температура: {temp_min} градусов")
print(f"осадки за сутки: {precip} мм")