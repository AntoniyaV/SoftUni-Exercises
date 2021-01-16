budget = float(input())
season = input()

destination = ""
stay_type = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        stay_type = "Camp"
        price = budget * 0.3
    elif season == "winter":
        stay_type = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        stay_type = "Camp"
        price = budget * 0.4
    elif season == "winter":
        stay_type = "Hotel"
        price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    stay_type = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{stay_type} - {price:.2f}")