import cv2
import numpy as np
import matplotlib.pyplot as plt


def analyze_histogram(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    otsu_threshold, threshold_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    plt.figure()
    plt.title("Histogram Skali Szarości")
    plt.xlabel("Intensywność Pikseli")
    plt.ylabel("Liczba Pikseli")
    plt.plot(hist)

    plt.axvline(x=otsu_threshold, color='r', linestyle='--', label=f"Otsu Threshold: {otsu_threshold}")

    plt.legend()

    plt.show()


if __name__ == "__main__":
    analyze_histogram("../data/img.png")

#*
# Metoda Otsu oblicza wartość progową na podstawie analizy histogramu obrazu.
# Tak, na histogramie możemy zauważyć dwa wyraźne zbiory intensywności
# *#
