import cv2

def kontury_rozdzielczosc(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    # Rozdzielczości do przetestowania
    scale_factors = [1.0, 0.75, 0.5, 0.25]

    for scale in scale_factors:
        resized = cv2.resize(image, (0, 0), fx=scale, fy=scale)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        result = resized.copy()
        cv2.drawContours(result, contours, -1, (0, 0, 255), 2)

        print(f"Skala: {scale} — Liczba konturów: {len(contours)}")
        cv2.imshow(f"Kontury - skala {scale}", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Obserwacje:
    # - Przy wyższej rozdzielczości wykrywana jest większa liczba małych konturów.
    # - Zmniejszenie obrazu powoduje uproszczenie krawędzi, co może pomóc w eliminacji szumu.
    # - Jednak zbyt mała rozdzielczość może powodować utratę szczegółów — mniejsze obiekty mogą nie zostać wykryte.
    # - Optymalna rozdzielczość zależy od celu: uproszczona analiza (mniej konturów) vs. dokładna detekcja.

if __name__ == "__main__":
    kontury_rozdzielczosc("../data/img.png")
