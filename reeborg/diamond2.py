import time
rec_width = 7
rec_height = 4
diam_width = 7
symb = '*'


def head_foot(diam_width, rec_width, symb):
    for i in range(1,diam_width,2):
        line = " "*((diam_width-i)//2) + f"{symb}"*i + " "* ((diam_width-i)//2)
        print(line*rec_width)


    for i in range(diam_width,0,-2):
        line = " "*((diam_width-i)//2) + f"{symb}"*i + " "* ((diam_width-i)//2)
        print(line*rec_width)
        time.sleep(0.5)

def body(diam_width, rec_height, symb):
    for i in range(1,diam_width,2):
        line = " "*((diam_width-i)//2) + f"{symb}"*i + " "* ((diam_width-i)//2)
        line2 = " " * diam_width * (rec_width-2)
        print(line + line2 + line)
        time.sleep(0.5)

    for i in range(diam_width,0,-2):
        line = " "*((diam_width-i)//2) + f"{symb}"*i + " "* ((diam_width-i)//2)
        line2 = " " * diam_width * (rec_width-2)
        print(line + line2 + line)
        time.sleep(0.5)
    

#generate header
head_foot(diam_width, rec_width, symb)
#generate body
for i in range(rec_height - 2):
    body(diam_width, rec_width, symb)
#generate footer
head_foot(diam_width, rec_width, symb)
