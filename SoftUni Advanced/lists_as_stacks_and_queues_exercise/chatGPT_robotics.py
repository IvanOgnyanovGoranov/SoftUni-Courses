from collections import deque
import time

# Read robot names and processing times
robot_names_and_seconds = input().split(";")
robots = deque()

for item in robot_names_and_seconds:
    name, process_time = item.split("-")
    robots.append({"name": name, "time": int(process_time), "product": None, "processing_until": 0})

# Read starting time
start_time = input()
hours, minutes, seconds = map(int, start_time.split(":"))

current_time = 0  # Initialize current time

# Create a queue for products
products = deque()

# Read products until "End" command
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

# Simulate product assembly and robot processing
while products:
    current_time += 1

    # Check if a product is available to process
    if robots and current_time >= robots[0]["processing_until"]:
        robot = robots.popleft()
        product = products.popleft()
        robot["product"] = product
        robot["processing_until"] = current_time + robot["time"]

        # Print processing information
        processed_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
        print(f"{robot['name']} - {product} [{processed_time}]")

    # Rotate robots to maintain the order
    if robots:
        robots.rotate(-1)