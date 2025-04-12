import cv2
import numpy as np


def increase_brightness(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    brightened_image = cv2.add(gray_image, 50)

    _, threshold_original = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
    _, threshold_brightened = cv2.threshold(brightened_image, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original Image", gray_image)
    cv2.imshow("Brightened Image", brightened_image)
    cv2.imshow("Thresholded Original", threshold_original)
    cv2.imshow("Thresholded Brightened", threshold_brightened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    increase_brightness("../data/img.png")
