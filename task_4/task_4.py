import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    nearest = cv2.resize(img, (0, 0), fx=3, fy=3, interpolation=cv2.INTER_NEAREST)
    linear = cv2.resize(img, (0, 0), fx=3, fy=3, interpolation=cv2.INTER_LINEAR)
    cubic = cv2.resize(img, (0, 0), fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    lanczos = cv2.resize(img, (0, 0), fx=3, fy=3, interpolation=cv2.INTER_LANCZOS4)

    comparison = np.hstack((nearest, linear, cubic, lanczos))

    cv2.imshow("Interpolation Comparison (Nearest - Linear - Cubic - Lanczos4)", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
