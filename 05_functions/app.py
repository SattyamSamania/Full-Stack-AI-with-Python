from weather_utils import get_weather_message, get_weather_data

# User input for manual temperature classification
temp = int(input("Enter the temperature in Celsius: "))
message = get_weather_message(temp)
print(f"The weather is: {message}")

# User input for real-time temperature
city = input("Enter the city name: ")
weather_data = get_weather_data(city)
print(weather_data)