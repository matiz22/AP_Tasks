import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')

    flipped_horizontal = cv2.flip(img, 1)
    flipped_vertical = cv2.flip(img, 0)
    flipped_both_axes = cv2.flip(img, -1)

    comparison = np.hstack((img, flipped_horizontal, flipped_vertical, flipped_both_axes))

    cv2.imshow("Comparison (Original, Horizontal, Vertical, Both Axes)", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
