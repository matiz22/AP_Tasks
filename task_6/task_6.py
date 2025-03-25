import cv2
import numpy as np


def experiment_with_logo(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    B, G, R = cv2.split(img)

    swapped_img = cv2.merge([R, G, B])

    no_green_img = cv2.merge([R, np.zeros_like(G), B])

    cv2.imshow("Original Logo", img)
    cv2.imshow("Swapped Channels (Blue with Red)", swapped_img)
    cv2.imshow("Removed Green Channel", no_green_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/img_1.png"
    experiment_with_logo(image_path)
