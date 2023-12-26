number_of_reservations = int(input())
reservations = set()

for reservation in range(number_of_reservations):
    res_num = input()
    reservations.add(res_num)

while True:
    guest_arriving = input()
    if guest_arriving == "END":
        break
    if guest_arriving in reservations:
        reservations.remove(guest_arriving)

print(len(reservations))
for reservation in sorted(reservations):
    print(reservation)
