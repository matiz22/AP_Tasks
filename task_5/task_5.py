import cv2
import numpy as np


def run():
    img1 = cv2.imread('../data/example.png')
    img2 = cv2.imread('../data/shifted_example.png')

    diff = cv2.absdiff(img1, img2)

    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    _, thresh_diff = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    cv2.imshow("Image 1", img1)
    cv2.imshow("Image 2", img2)
    cv2.imshow("Difference", diff)
    cv2.imshow("Thresholded Difference", thresh_diff)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
