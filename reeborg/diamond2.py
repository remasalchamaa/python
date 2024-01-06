rec_height = 6
rec_width = 4
diam_width = 7
symb = '*'

def h_f(diam_width, symb, rec_width):
    for i in range(1, diam_width, 2):
        line = " "*((diam_width - i)//2) + f"{symb}"*(i) + " "*((diam_width - i)//2)
        print(line*rec_width)

    for i in range(diam_width, 0, -2):
        line = " "*((diam_width - i)//2) + f"{symb}"*(i) + " "*((diam_width - i)//2)
        print(line*rec_width)

def body(diam_width, symb, rec_width):
    for i in range(1, diam_width, 2):
        line = " "*((diam_width - i)//2) + f"{symb}"*(i) + " "*((diam_width - i)//2)
        line2 = " "*diam_width*(rec_width-2)
        print(line+line2+line)

    for i in range(diam_width, 0, -2):
        line = " "*((diam_width - i)//2) + f"{symb}"*(i) + " "*((diam_width - i)//2)
        line2 = " "*diam_width*(rec_width-2)
        print(line+line2+line)



h_f(diam_width, symb, rec_width)
for i in range(rec_height-2):
    body(diam_width, symb, rec_width)
h_f(diam_width, symb, rec_width)
