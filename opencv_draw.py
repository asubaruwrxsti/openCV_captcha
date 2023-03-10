import cv2 as cv
import os

def getFiles(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.png' in file:
                files.append(os.path.join(r, file))
    return files

files = getFiles('letters')

# y1 = 102
# y2 = 109

# y1-1 = 131
# y2-1 = 138
def drawLine(image):
    # get the image size
    size_x = image.shape[1]
    size_y = image.shape[0]
    start_x = 0
    end_x = 0
    start_x2 = 0
    end_x2 = 0

    # scan the y=102 line and find the first black pixel in the x axis
    for i in range(size_x):
        if image[102][i][0] == 0:
            start_x = i
            break
    
    # scan the y=109 line and find the first black pixel in the x axis
    for i in range(size_x):
        if image[109][i][0] == 0:
            end_x = i
            break
    
    # scan the y=102 line and find the first black pixel in the x axis from the end
    for i in range(size_x-1, 0, -1):
        if image[102][i][0] == 0:
            start_x2 = i
            break
    
    # scan the y=109 line and find the first black pixel in the x axis from the end
    for i in range(size_x-1, 0, -1):
        if image[109][i][0] == 0:
            end_x2 = i
            break
    
    # draw the rectangle, fill black
    cv.rectangle(image, (start_x, 102), (end_x, 109), (255, 255, 255), 1)
    cv.rectangle(image, (start_x2, 102), (end_x2, 109), (255, 255, 255), 1)

    #fill the difference of the two rectangles
    cv.rectangle(image, (start_x, 102), (start_x2, 109), (0, 0, 0), -1)
    cv.rectangle(image, (end_x, 102), (end_x2, 109), (0, 0, 0), -1)

    # get the image size
    size_x = image.shape[1]
    size_y = image.shape[0]
    start_x = 0
    end_x = 0
    start_x2 = 0
    end_x2 = 0

    # scan the y=102 line and find the first black pixel in the x axis
    for i in range(size_x):
        if image[131][i][0] == 0:
            start_x = i
            break
    
    # scan the y=109 line and find the first black pixel in the x axis
    for i in range(size_x):
        if image[138][i][0] == 0:
            end_x = i
            break
    
    # scan the y=102 line and find the first black pixel in the x axis from the end
    for i in range(size_x-1, 0, -1):
        if image[131][i][0] == 0:
            start_x2 = i
            break
    
    # scan the y=109 line and find the first black pixel in the x axis from the end
    for i in range(size_x-1, 0, -1):
        if image[138][i][0] == 0:
            end_x2 = i
            break
    
    # draw the rectangle, fill black
    cv.rectangle(image, (start_x, 131), (end_x, 138), (255, 255, 255), 1)
    cv.rectangle(image, (start_x2, 131), (end_x2, 138), (255, 255, 255), 1)

    #fill the difference of the two rectangles
    cv.rectangle(image, (start_x, 131), (start_x2, 138), (0, 0, 0), -1)
    cv.rectangle(image, (end_x, 131), (end_x2, 138), (0, 0, 0), -1)

    cv.imshow('image', image)
    cv.waitKey(0)

drawLine(cv.imread(files[0]))
