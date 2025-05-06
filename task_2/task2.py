import cv2

def znajdz_kontury(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    # Skalowanie
    scale_width = 300
    height = int(image.shape[0] * (scale_width / image.shape[1]))
    resized = cv2.resize(image, (scale_width, height))

    # Skala szarości i progowanie
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Tryby do przetestowania
    modes = {
        "RETR_EXTERNAL": cv2.RETR_EXTERNAL,
        "RETR_TREE": cv2.RETR_TREE,
        "RETR_LIST": cv2.RETR_LIST
    }

    for name, mode in modes.items():
        # Skopiuj obraz do rysowania konturów
        image_copy = resized.copy()
        contours, _ = cv2.findContours(binary, mode, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image_copy, contours, -1, (0, 0, 255), 2)
        cv2.imshow(f"Kontury - {name}", image_copy)

    cv2.imshow("Obraz binarny", binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Komentarze:
    # RETR_EXTERNAL – Wykrywa tylko zewnętrzne kontury (kontury „główne” bez zagłębiania się w hierarchię).
    # RETR_TREE – Wykrywa wszystkie kontury i buduje pełną hierarchię (kontury w konturach).
    # RETR_LIST – Wykrywa wszystkie kontury, ale bez budowania hierarchii (wszystkie są równorzędne).
    #
    # RETR_TREE przydaje się, gdy interesuje nas relacja między konturami (np. dziury w obiektach),
    # RETR_EXTERNAL nadaje się, gdy zależy nam tylko na konturach zewnętrznych (np. obiekty bez wnętrz),
    # RETR_LIST jest pomocne, gdy chcemy wszystkie kontury, ale nie potrzebujemy relacji między nimi.

    # Wnioski:
    # - RETR_EXTERNAL: Najlepsze do prostych obiektów, ale nie wykrywa konturów wewnętrznych, wybrane zdjęcie ma artefakty na niektórych kostach, a skupiamy się na zewnętrznych.

if __name__ == "__main__":
    znajdz_kontury("../data/img.png")
