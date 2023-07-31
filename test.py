

def generate_caption(image):
    caption = "lkj;lkj"
    return caption

csv_dimesions = (22000)

def most_similar(catpion, serial_no, topk):
    #trad_marks_desc = read the descriptions from the csv file
    #score_list = cosine_similarity between caption and trad_marks_descs (1000, 1)
    #sort the score_list and get the topk indices
    # 
    # if the serial_no exists in the topK return a hit else a miss
    # calculate the accuracy 
    # return the accuracy and topk serial_no
    #topk = 1 accuracy 80
    # topk = 10 accuray 80
    # topk = 1000 accuray 100

    return hitormiss, topk_serial_no

#iterate over the whole images #1000
preds = []
for image in images:
    caption = generate_caption(image)
    hitormiss, topk_serial_no = most_similar(caption, serial_no, topk)
    preds.append(hitormiss)

#calculate the accuracy