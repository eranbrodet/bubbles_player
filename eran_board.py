import cv2
import numpy as np

from image_lib import color_from_image
from lib import Bubble


def read_bubbles_board():
    # TODO Eran magic numbers (per resolution?)
    img = cv2.imread('test.png', 0)
    color_img = cv2.imread('test.png')

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2.4, 15,
                               param1=30, param2=30, minRadius=10, maxRadius=15)
    circles = np.uint16(np.around(circles))

    board = [Bubble(x, y, r) for x, y, r in circles[0, :] if y < 400 and x < 430]
    board.sort(key=lambda b: b.x)
    board.sort(key=lambda b: b.y)
    for bubble in board:
        single_tile_from_screen = color_img[bubble.y-bubble.r:bubble.y+bubble.r, bubble.x-bubble.r:bubble.x+bubble.r]

        print color_from_image(single_tile_from_screen)

read_bubbles_board()