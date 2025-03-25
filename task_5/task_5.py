import cv2
import numpy as np


def enhance_red_with_mask(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_img, lower_red, upper_red)

    hsv_img[:, :, 1] = cv2.add(hsv_img[:, :, 1], mask // 255 * 50)

    enhanced_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

    cv2.imshow("Original Image", img)
    cv2.imshow("Enhanced Red Channel", enhanced_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    enhance_red_with_mask("../data/img.png")
