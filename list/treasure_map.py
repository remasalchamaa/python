
map = [['+','+','+'], ['+','+','+'], ['+','+','+']]
print(f"{map[0]}\n{map[1]}\n{map[2]}")


position = input("Where do you want to put the treasure? ")
col = int(position[0])
row = int(position[1])

map[row - 1][col - 1] = 'X'
print(f"{map[0]}\n{map[1]}\n{map[2]}")
