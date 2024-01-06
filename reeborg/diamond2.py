import time

rec_width = 7
rec_height = 4
diam_width = 7
symb = '*'


def head_foot(width, rep, symb):
    for i in range(1,width,2):
        line = " "*((width-i)//2) + f"{symb}"*i + " "* ((width-i)//2)
        print(line*rep)
        time.sleep(0.5)

    for i in range(width,0,-2):
        line = " "*((width-i)//2) + f"{symb}"*i + " "* ((width-i)//2)
        print(line*rep)
        time.sleep(0.5)

def body(width, rep, symb):
    for i in range(1,width,2):
        line = " "*((width-i)//2) + f"{symb}"*i + " "* ((width-i)//2)
        line2 = " " * width * (rep-2)
        print(line + line2 + line)
        time.sleep(0.5)

    for i in range(width,0,-2):
        line = " "*((width-i)//2) + f"{symb}"*i + " "* ((width-i)//2)
        line2 = " " * width * (rep-2)
        print(line + line2 + line)
        time.sleep(0.5)
    

#generate header
head_foot(diam_width, rec_width, symb)
#generate body
for i in range(rec_height - 2):
    body(diam_width, rec_width, symb)
#generate footer
head_foot(diam_width, rec_width, symb)
