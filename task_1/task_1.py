import sys

import cv2

def open_and_show(path):
    img = cv2.imread(path)
    cv2.imshow('Obraz', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    open_and_show('../data/example.png')
    open_and_show('example2.png')