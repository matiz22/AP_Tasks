import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')

    matrix = np.ones(img.shape, dtype="uint8") * 50
    opencv = cv2.add(img, matrix)

    numpy = img + matrix

    cv2.imshow("Lighter opencv", opencv)
    cv2.imshow("Lighter numpy", numpy)
    cv2.imshow("Difference", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    run()
