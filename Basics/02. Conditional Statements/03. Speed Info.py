velocity = float(input())
if velocity <= 10:
    print("slow")
elif velocity <= 50:
    print("average")
elif velocity <= 150:
    print("fast")
elif velocity <= 1000:
    print("ultra fast")
elif velocity > 1000:
    print("extremely fast")
