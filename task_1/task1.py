import cv2

def klasyczne_progowanie_kostka(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    scale_width = 300
    height = int(image.shape[0] * (scale_width / image.shape[1]))
    resized = cv2.resize(image, (scale_width, height))

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    thresholds = [100, 140, 180]

    for T in thresholds:
        _, binary = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
        cv2.imshow(f"Threshold = {T}", binary)

    cv2.imshow("Oryginalny obraz", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Komentarz:
    # - Dla T = 100: Kostki brukowe są dobrze widoczne, segmentacja skuteczna – najlepszy wynik.
    # - Dla T = 140: Widoczność kostek jest ograniczona, część detali zanika – segmentacja słaba.
    # - Dla T = 180: Obraz niemal całkowicie czarny, kostki niewidoczne – segmentacja nieudana.
    #
    # Wniosek: Najlepsze efekty uzyskano dla wartości progowej T = 100. Wyższe wartości prowadzą do utraty szczegółów.

if __name__ == "__main__":
    klasyczne_progowanie_kostka("../data/img.png")
