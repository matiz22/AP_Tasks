import cv2
import numpy as np

def detect_skin_hsv(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 30, 60], dtype=np.uint8)
    upper_skin = np.array([20, 150, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Original", image)
    cv2.imshow("Skin Mask", mask)
    cv2.imshow("Detected Skin", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_skin_hsv("../data/img_1.png")
