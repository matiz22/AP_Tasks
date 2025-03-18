import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')

    flipped_vertical = cv2.flip(img, 0)

    comparison = np.hstack((img, flipped_vertical))

    cv2.imshow("Original and Vertical Flip", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
