import cv2

def porownaj_metody_adaptacyjne(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    resized = cv2.resize(image, (300, int(image.shape[0] * 300 / image.shape[1])))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    methods = {
        "Mean": cv2.ADAPTIVE_THRESH_MEAN_C,
        "Gaussian": cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    }

    C_values = [2, 5, 10, 15]

    for method_name, method in methods.items():
        for C in C_values:
            result = cv2.adaptiveThreshold(gray, 255, method, cv2.THRESH_BINARY, 21, C)
            cv2.imshow(f"{method_name} - C={C}", result)

    cv2.imshow("Oryginalny", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # - Metoda Mean z C=5 najlepiej radzi sobie z szumem i nierównym tłem,
    #   zachowując jednocześnie kontury obiektów.

if __name__ == "__main__":
    porownaj_metody_adaptacyjne("../data/img.png")
