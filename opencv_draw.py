import cv2 as cv
import math

img = cv.imread('public\scrapper\screenshot.png')
height, width, channels = img.shape

black_pixel = (0, 0, 0)
white_pixel = (255, 255, 255)

y_1 = int(height*0.34)
y_2 = int(height*0.45)

def fill_whites():
    cv.line(img, (0, y_1),
                 (int(width), y_1), black_pixel, 1)
    cv.line(img, (0, y_2),
                 (int(width), y_2), black_pixel, 1)

def print_info():
    print("=====================================")
    print("IMAGE SIZE: [", height, ", ", width, "]")
    print("starting point of line 1: ", (0, int(height*0.34)))
    print("ending point of line 1: ", (int(width), int(height*0.34)))
    print("starting point of line 2: ", (0, int(height*0.45)))
    print("ending point of line 2: ", (int(width), int(height*0.45)))
    print("y_1: ", y_1)
    print("y_2: ", y_2)
    print("=====================================\n")

# #first line
# for x in range(0, 50):
#     if ((round(img[x, y_1 + 1][0], -2) == 200).any() and (round(img[x, y_1 - 1][0], -2) == 200).any()):
#         print("Black pixel found in (x: ", x, "y: ", y_1, ")")
#         print("pixel: ", round(img[x, y_1 + 1][0], -2))
#     cv.line(img, (x, y_1), (x + 1, y_1), black_pixel, 1)

# #cv.line(img, (13, 17), (27, 17), black_pixel, 1)

# cv.imshow('image', img)
# cv.waitKey(0)
