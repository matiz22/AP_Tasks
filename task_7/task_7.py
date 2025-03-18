import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    resized_area = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

    resized_linear = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
    resized_cubic = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)

    comparison = np.hstack((resized_area, resized_linear, resized_cubic))

    # Display the comparison image
    cv2.imshow("Scaling Down Comparison (Area - Linear - Cubic)", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
