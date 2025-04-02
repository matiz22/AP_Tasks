import cv2
import numpy as np


def improve_license_plate(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    dilated = cv2.dilate(binary_image, kernel, iterations=1)


    cv2.imshow("Oryginalny obraz", image)
    cv2.imshow("Binary Image", binary_image)
    cv2.imshow("Dylatacja", dilated)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    improve_license_plate("../data/img.png")
