import cv2
import numpy as np


def case_study(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold_basic = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

    _, threshold_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)

    kernel = np.ones((3, 3), np.uint8)
    eroded = cv2.erode(threshold_otsu, kernel, iterations=1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Basic Threshold (T=100)", threshold_basic)
    cv2.imshow("Otsu Threshold", threshold_otsu)
    cv2.imshow("Blurred Image", blurred)
    cv2.imshow("Eroded Image (Otsu)", eroded)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    case_study("../data/img_1.png")

# Dla wybranego zdjęcia efekt jest najlepszy dla progowania podstawowego 100
