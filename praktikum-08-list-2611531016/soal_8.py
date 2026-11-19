number_of_rows = 4
seats_per_row = 5
# Write your code below

board = []
for _ in range(number_of_rows):
    board.append(["."] * seats_per_row)

seats_taken = 0

while True:
    for i in range(number_of_rows):
        print(f"Row {i + 1}: " + " ".join(board[i]))

    row = int(input("Row (0 to stop): "))
    if row == 0:
        break

    seat = int(input("Seat: "))

    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
        continue

    r = row - 1
    c = seat - 1

    if board[r][c] == "X":
        print("Seat already taken.")
    else:
        board[r][c] = "X"
        seats_taken += 1
        print("Seat booked.")

print(f"Seats taken: {seats_taken}")