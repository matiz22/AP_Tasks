import sys

import cv2


def open_and_print_channel(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        print("Błąd: Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku!")
    else:
        num_channels = img.shape[2]
        print(f"Liczba kanałów: {num_channels}")

        cv2.imshow(f"Obraz kolorowy, Liczba kanalow: {num_channels}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    open_and_print_channel("../data/example.png")