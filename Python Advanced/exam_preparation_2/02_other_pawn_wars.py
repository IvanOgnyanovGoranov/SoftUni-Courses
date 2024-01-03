def check

chessboard = []

black = []
white = []
chessboard_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

for _ in range(8):
    row = input().split()
    if "b" in row:
        black = [row, chessboard[row].index("b")]
    if "a" in row:
        white = [row, chessboard[row].index("a")]

while True:
    up_left = [white[0] - 1, white[1] - 1]
    up_right = [white[0] - 1, white[1] + 1]
    up = [white[0] - 1, white[1]]





print(chessboard)