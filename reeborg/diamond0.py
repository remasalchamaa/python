diam_width = 19
symb = '*'

for i in range(1, diam_width, 2):
    line = " "*((diam_width - i)//2) + f"{symb}"*(i) + " "*((diam_width - i)//2)
    print(line)

for i in range(diam_width, 0, -2):
    line = " "*((diam_width - i)//2) + f"{symb}"*(i) + " "*((diam_width - i)//2)
    print(line)
