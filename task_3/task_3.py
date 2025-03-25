import cv2
import numpy as np


def manipulate_channels(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    (B, G, R) = cv2.split(img)

    img_swapped = cv2.merge([R, B, G])

    img_zero_channel = cv2.merge([np.zeros_like(R), G, B])

    cv2.imshow("Swapped Channels (R, B, G)", img_swapped)
    cv2.imshow("Image with Zero Red Channel", img_zero_channel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    image_path = "../data/example.jpg"
    manipulate_channels(image_path)
