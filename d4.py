#!/usr/bin/env python3

bingo = []
boards = []

def collect(_input):
    while True:
        columns = {}
        board = {"nbr": len(boards)}
        for i in range(5):
            data = _input.readline()
            if data == "":
                return

            board[f"row{i}"] = data.strip().replace("  ", " ").split(" ")
            columns[f"col{i}"] = []


        for key in board.keys():
            if key.startswith("row"):
                for i in range(5):
                    columns[f"col{i}"].append(board[key][i])

        board.update(columns)
        boards.append(board)
        
        _input.readline()

# Collect boards 
with open("4.in", "r") as _input:
    bingo = _input.readline().split(",")
    _input.readline()
    collect(_input)


for i in range(5, len(bingo)):
    numbers = bingo[:i]
    for board in boards:
        for thing in board:
            if thing == "nbr":
                continue
            board_numbers = board[thing]
            if [x for x in board_numbers if x in numbers] == board_numbers:
                all_numbers = []
                for row in board:
                    if row.startswith("row"):
                        all_numbers += board[row]

                unmarked = sum([int(x) for x in all_numbers if x not in numbers])
                score = unmarked * int(numbers[-1])

                assert False, score

print("vittu")
