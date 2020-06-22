import cv2
import numpy as np
import sys
import os
try:
    from PIL import Image
except ImportError:
    import pytesseract

try:
    file = sys.argv[1]
    dirname = os.path.dirname(file)
    basename = os.path.basename(file)
except IndexError:
    print("Provide an image")
    exit(1)
    
def sort_contours(contours, method="left-right"):
    reverse = False
    i = 0

    if method == "right-left" or method == "bottom-top":
        reverse = True

    if method == "top-bottom" or method == "bottom -top":
        i = 1   

    boundingBoxes = [cv2.BoundingRect(c) for c in contours]
    (contours, boundingBoxes) = zip(*(sorted(zip(contours, boundingBoxes),
        key=lambda b: b[1][i], reverse=reverse)))
    return (contours, boundingBoxes)

img = cv2.imread(file, 0)
threshold, img_bin = cv2.threshold(img, 128, 255,
        cv2.THRESH_BINARY|cv2.THRESH_OTSU)

img_bin = 255 - img_bin
cv2.imwrite(os.path.join(dirname, "{}_bin.jpeg".format(basename,)),
        img_bin)

# Define kernel
kernel_len = np.array(img_bin).shape[1] // 100
ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))  # Vertical Kernel
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))  # Horizontal Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

# Get vertical lines in image
image = cv2.erode(img_bin, ver_kernel, iterations=3)
vertical_lines = cv2.dilate(image, ver_kernel, iterations=3)
cv2.imwrite(os.path.join(dirname, "{}_vertical.jpeg".format(basename,)),
        vertical_lines)
# Get horizontal lines in image
image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)
cv2.imwrite(os.path.join(dirname, "{}_horizontal.jpeg".format(basename,)),
        horizontal_lines)

# Get Horizontal and Vertical lines in an image
img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)
img_vh = cv2.erode(~img_vh, kernel, iterations=2)
thresh, img_vh = cv2.threshold(img_vh, 128, 255, cv2.THRESH_BINARY
        | cv2.THRESH_OTSU)
cv2.imwrite(os.path.join(dirname, "{}_ver_hor.jpeg".format(basename,)), img_vh)

bitxor = cv2.bitwise_xor(img, img_vh)
bitnot = cv2.bitwise_not(bitxor)

# Detect contours..
contours, hierarchy = cv2.findContours(img_vh, cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE)

contours, boundingBoxes = sort_contours(contours, method='top-bottom')

# Creating a list of heights for all detected boxes..
heights = [boundingBoxes[i][3] for i in range(len(boundingBoxes))]
mean = np.mean(heights)

box = []

# Get position(x, y) and width and height for every contour and show the
# contour on image..
for c in contours:
    x, y, w, h = cv2.boundingRect(c)

    if (w < 1000 and h < 500):
        image = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        box.append([x, y, w, h])

cv2.imwrite(os.path.join(dirname, "{}_rectangles.jpeg".format(basename,)), img)
