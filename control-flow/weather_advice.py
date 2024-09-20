# This script asks a user about current weather conditions
# and provides clothing recommendations based on the input.

# Prompt user for weather conditions

weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendations based on weather conditions

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")