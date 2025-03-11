import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, cols // 2], [0, 1, rows // 2]])
    shifted_img = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("Shifted Image", shifted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
