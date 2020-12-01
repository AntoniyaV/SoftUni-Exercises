hours = int(input())
minutes = int(input())
minutes_15 = minutes + 15
if minutes_15 > 59:
    if (hours + 1) == 24:
        if (minutes_15 - 60) < 10:
            print(f"0:0{minutes_15 - 60}")
        elif (minutes_15 - 60) >= 10:
            print(f"0:{minutes_15 - 60}")
    elif (hours + 1) != 24:
        if (minutes_15 - 60) < 10:
            print(f"{hours + 1}:0{minutes_15 - 60}")
        elif (minutes_15 - 60) >= 10:
            print(f"{hours + 1}:{minutes_15 - 60}")
elif minutes_15 < 60:
    print(f"{hours}:{minutes_15}")