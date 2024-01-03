from math import ceil

name_of_show = str(input())
length = int(input())
break_time = int(input())

lunch_break = break_time / 8
rest_time = break_time / 4

free_time = break_time - lunch_break - rest_time

if free_time >= length:
    print (f"You have enough time to watch {name_of_show} and left with {ceil(free_time - length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_show}, you need {ceil(abs(length - free_time))} more minutes.")