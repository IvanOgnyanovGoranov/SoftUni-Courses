length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())

aquarium_volume = length_in_cm * width_in_cm * height_in_cm
volume_in_litres = aquarium_volume / 1000

required_litres = volume_in_litres * (1 - 0.17)

print(required_litres)

