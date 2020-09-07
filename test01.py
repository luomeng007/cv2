# -*- coding: utf-8 -*-
import cv2


# read image
im1 = cv2.imread(r"./debug.jpg")

# name the window and set the format of window,cv2.WINDOW_NORMAL means 
# the size of window could be changed and the window could be moved
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

cv2.imshow("image", im1)

# wait for a press key in case the window is destroyed directly
cv2.waitKey(0)

# destroy window
cv2.destroyWindow("image")