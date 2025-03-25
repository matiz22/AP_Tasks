import cv2
import numpy as np


def enhance_channel(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    (B, G, R) = cv2.split(img)

    R_enhanced = cv2.add(R, 50)

    img_enhanced = cv2.merge([B, G, R_enhanced])

    cv2.imshow("Original Image", img)
    cv2.imshow("Enhanced Red Channel", img_enhanced)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    enhance_channel("../data/img.png")

