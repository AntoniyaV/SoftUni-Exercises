import math

runner_1 = int(input())
runner_2 = int(input())
runner_3 = int(input())
sum = runner_1 + runner_2 + runner_3
minutes = sum / 60
seconds = sum % 60
minutes = math.floor(minutes)
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")