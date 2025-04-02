import cv2
import numpy as np


def apply_morphological_operations(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    kernels = {
        "kwadrat": cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)),
        "krzyż": cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2)),
        "elipsa": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    }

    results = {}

    for shape, kernel in kernels.items():
        eroded = cv2.erode(binary, kernel, iterations=1)
        dilated = cv2.dilate(binary, kernel, iterations=1)
        opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

        results[shape] = {
            "eroded": eroded,
            "dilated": dilated,
            "opened": opened,
            "closed": closed,
            "gradient": gradient
        }

    cv2.imshow("Oryginalny obraz", binary)

    for shape, operations in results.items():
        cv2.imshow(f"{shape} - Erozja", operations["eroded"])
        cv2.imshow(f"{shape} - Dylatacja", operations["dilated"])
        cv2.imshow(f"{shape} - Otwarcie", operations["opened"])
        cv2.imshow(f"{shape} - Zamknięcie", operations["closed"])
        cv2.imshow(f"{shape} - Gradient", operations["gradient"])

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    apply_morphological_operations("../data/img_3.png")

#*
# Dla wszystkich opercji morfologicznych efekty o najlepszej czytelności to zamknięcie i dylatacja
# Gradient w połaczeniu z kwadratem dobrze podkreśla kontur
# *#