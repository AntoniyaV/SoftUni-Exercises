record_sec = float(input())
meters = float(input())
sec_per_m = float(input())
time = meters * sec_per_m
if meters >= 15:
    time = time + ((meters // 15) * 12.5)
    if time < record_sec:
        print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
    else:
        print(f"No, he failed! He was {time - record_sec:.2f} seconds slower.")
else:
    if time < record_sec:
        print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
    else:
        print(f"No, he failed! He was {time - record_sec:.2f} seconds slower.")