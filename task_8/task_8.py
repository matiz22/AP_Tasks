import cv2
import numpy as np


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    rows, cols = img.shape[:2]
    center = (cols // 2, rows // 2)

    M1 = cv2.getRotationMatrix2D(center, 30, 1)
    rotated_img_30_1 = cv2.warpAffine(img, M1, (cols, rows))

    M2 = cv2.getRotationMatrix2D(center, 30, 1)
    rotated_img_30_2 = cv2.warpAffine(rotated_img_30_1, M2, (cols, rows))

    M3 = cv2.getRotationMatrix2D(center, 30, 1)
    rotated_img_30_3 = cv2.warpAffine(rotated_img_30_2, M3, (cols, rows))

    cv2.imshow("Rotated Image (3 x 30 degrees)", rotated_img_30_3)

    M_single = cv2.getRotationMatrix2D(center, 90, 1)
    rotated_img_90 = cv2.warpAffine(img, M_single, (cols, rows))

    cv2.imshow("Rotated Image (1 x 90 degrees)", rotated_img_90)

    print("Are the images the same?", np.array_equal(rotated_img_30_3, rotated_img_90))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
