number = float(input())
metric_in = input()
metric_out = input()
if metric_in == "m":
    if metric_out == "cm":
        print(f"{number * 100:.3f}")
    elif metric_out == "mm":
        print(f"{number * 1000:.3f}")
elif metric_in == "cm":
    if metric_out == "m":
        print(f"{number / 100:.3f}")
    elif metric_out == "mm":
        print(f"{number * 10:.3f}")
elif metric_in == "mm":
    if metric_out == "m":
        print(f"{number / 1000:.3f}")
    elif metric_out == "cm":
        print(f"{number / 10:.3f}")