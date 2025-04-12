import cv2
import numpy as np

def shift_hue(image_path, shift_value=30):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    h_shifted = (h.astype(np.int32) + shift_value) % 180
    h_shifted = h_shifted.astype(np.uint8)

    hsv_shifted = cv2.merge([h_shifted, s, v])
    result = cv2.cvtColor(hsv_shifted, cv2.COLOR_HSV2BGR)

    cv2.imshow("Original", image)
    cv2.imshow("Hue Shifted", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    shift_hue("../data/img.png", shift_value=30)
