from typing import Any

import cv2
from numpy import ndarray, dtype


def open_in_gray_and_print_channel(path) -> ndarray[Any, dtype] | None:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Błąd: Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku!")
    else:
        if len(img.shape) == 2:
            num_channels = 1
        else:
            num_channels = img.shape[2]

        print(f"Liczba kanałów: {num_channels}")

        cv2.imshow(f"Obraz kolorowy, Liczba kanalow: {num_channels}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return img

if __name__ == "__main__":
    open_in_gray_and_print_channel("../data/example.png")
