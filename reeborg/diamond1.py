rec_width = 4
rec_height = 4
diam_width = 7
symb = '*'


def header(width, rep, symb):
    for i in range(1,width,2):
        line = " "*((width-i)//2) + f"{symb}"*i + " "* ((width-i)//2)
        print(line*rep)

    for i in range(width,0,-2):
        line = " "*((width-i)//2) + f"{symb}"*i + " "* ((width-i)//2)
        print(line*rep)


for i in range(rec_height):
    header(diam_width, rec_width, symb)
