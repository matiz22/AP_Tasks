import cv2
import numpy as np


def apply_blur_methods(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    blur_simple = cv2.blur(image, (5, 5))

    blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

    blur_median = cv2.medianBlur(image, 5)

    blur_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Oryginalny obraz", image)
    cv2.imshow("Rozmycie proste (cv2.blur)", blur_simple)
    cv2.imshow("Rozmycie Gaussa (cv2.GaussianBlur)", blur_gaussian)
    cv2.imshow("Rozmycie medianowe (cv2.medianBlur)", blur_median)
    cv2.imshow("Rozmycie dwustronne (cv2.bilateralFilter)", blur_bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    apply_blur_methods("../data/img.png")

    #*
    # Do usuwania szumu median blur bilateral filter
    # Do zachowania szczegółów bilateral filter
    # *#
