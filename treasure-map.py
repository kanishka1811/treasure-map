
row1 = ["🧡", "🧡", "🧡"]
row2 = ["🧡", "🧡", "🧡"]
row3 = ["🧡", "🧡", "🧡"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input('Where do you want to place the treasure? enter "columnRow"')

col = position[0]
row = position[1]

map[int(row)-1][int(col)-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
