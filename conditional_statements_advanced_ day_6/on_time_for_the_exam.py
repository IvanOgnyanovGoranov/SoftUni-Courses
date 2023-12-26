hour_of_exam = int(input())
minutes_of_exam = int(input())

arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = hour_of_exam * 60 + minutes_of_exam
student_time_in_minutes = arrival_hour * 60 + arrival_minute

time_difference = exam_time_in_minutes - student_time_in_minutes

if time_difference > 30:
    print("Early")
elif time_difference < 0:
    print("Late")
else:
    print("On time")

hours = 0
minutes = abs(time_difference)

result = ""

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_difference > 0:
    result += " before the start"
elif time_difference < 0:
    result += " after the start"

print(result)

