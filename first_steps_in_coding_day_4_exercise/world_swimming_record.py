record_in_seconds = float(input())
distance_in_metres = float(input())
meter_per_second = float(input())

time_in_seconds = meter_per_second * distance_in_metres

slowing_down = (distance_in_metres // 15) * 12.5
total_time = time_in_seconds + slowing_down

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.")