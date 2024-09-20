# This script asks a user about current weather conditions
# and provides clothing recommendations based on the input.

# Prompt user for weather conditions

weather_condtion = input("What's the weather like today?\n(sunny/rainy/cold): ")

# Provide clothing recommendations based on weather conditions

if weather_condtion == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condtion == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condtion == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")