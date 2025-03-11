import cv2
import imutils
import numpy as np


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    shifted_img_imutils = imutils.translate(img, 100, 50)

    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    shifted_img_cv2 = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("Shifted Image (imutils)", shifted_img_imutils)
    cv2.imshow("Shifted Image (cv2.warpAffine)", shifted_img_cv2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
