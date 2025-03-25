import cv2
import numpy as np


def extract_color(path, lower_bound, upper_bound):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    extracted = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Oryginalny obraz", img)
    cv2.imshow("Maska", mask)
    cv2.imshow("Wyodrębniony kolor", extracted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/img.png"
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    extract_color(image_path, lower_red, upper_red)