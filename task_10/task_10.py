import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')

    rows, cols = img.shape[:2]
    center = (cols // 2, rows // 2)

    for angle in range(0, 361, 15):
        M = cv2.getRotationMatrix2D(center, angle, 1)

        rotated_img = cv2.warpAffine(img, M, (cols, rows))

        cv2.imshow(f"Rotated Image {angle} degrees", rotated_img)

        cv2.waitKey(500)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
