import cv2
import numpy as np


def erode_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold_100 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)

    eroded_image = cv2.erode(threshold_100, kernel, iterations=1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Thresholded Image (T=100)", threshold_100)
    cv2.imshow("Eroded Image", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    erode_image("../data/img.png")

#*
# Jeśli na obrazie są małe białe plamki lub szum w tle, operacja erozji pozwala je usunąć.
#
# Jednakże, w zależności od kształtu i rozmiaru elementu strukturalnego, może dojść również do utraty szczegółów w większych obiektach.
# *#
