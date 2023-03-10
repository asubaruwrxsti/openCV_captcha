import cv2 as cv
import math
import numpy as np

im = cv.imread("screenshot.png")
original_size_x = im.shape[1]
original_size_y = im.shape[0]

scale_x = 600
scale_y = 300

im = cv.resize(im, (scale_x, scale_y), interpolation=cv.INTER_NEAREST)

# add contrast
alpha = 2
beta = 3
im = cv.convertScaleAbs(im, alpha=alpha, beta=beta)

# if the pixel is not white, make it black
for i in range(scale_x):
    for j in range(scale_y):
        if im[j][i][0] != 255 or im[j][i][1] != 255 or im[j][i][2] != 255:
            im[j][i] = [0, 0, 0]

edges = cv.Canny(im, 100, 200)
contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

def cropLetter(start_x):
    print('starting at start_x: ' + str(start_x))
    initial_start_x = start_x
    end_x = 0

    # add condition to stop the recursion
    if start_x >= scale_x:
        return
    
    # tranverse x axis and find the cordination of the first black pixel in the y axis
    for i in range(initial_start_x ,scale_x):
        for j in range(scale_y):
            if im[j][i][0] == 0:
                start_x = i
                break
        else:
            continue
        break

    # tranverse x axis starting from start_x and find the first column that has no black pixel
    for i in range(start_x, scale_x):
        for j in range(scale_y):
            # find the first row tha has no black pixel
            if im[j][i][0] == 0:
                break
        else:
            end_x = i
            break
    
    print('start_x: ' + str(start_x))
    print('end_x: ' + str(end_x))

    im_crop = im[:, start_x:end_x]

    try:
        cv.imwrite("./letters/letter" + str(start_x) + ".png", im_crop)
    except Exception as e:
        print(e)
        return

    print('range: ' + str(start_x) + ' to ' + str(end_x))
    initial_start_x = end_x
    cropLetter(end_x)

cropLetter(0)