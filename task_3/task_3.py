import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')


    matrix = np.ones(img.shape, dtype="uint8") * 80
    opencv = cv2.subtract(img, matrix)

    numpy = img - matrix


    cv2.imshow("Darker opencv", opencv)
    cv2.imshow("Darker numpy", numpy)
    cv2.imshow("Difference", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    run()