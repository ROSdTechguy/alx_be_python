# weather_advice.py

# Prompt the user for the weather condition
weather_con = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide recommendations based on the weather condition
if weather_con == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_con == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_con == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
