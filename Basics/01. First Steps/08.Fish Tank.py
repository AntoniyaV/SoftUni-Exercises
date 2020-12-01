length = int(input())
width= int(input())
height = int(input())
taken_size = float(input())
volume = length * width * height * 0.001
litres = volume - (volume * taken_size / 100)
print(litres)
