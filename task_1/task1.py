import cv2

def porownanie_metod_progowania(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    resized = cv2.resize(image, (300, int(image.shape[0] * 300 / image.shape[1])))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    _, thresh_simple = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    _, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    thresh_adaptive_mean = cv2.adaptiveThreshold(gray, 255,
                                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                                 cv2.THRESH_BINARY, 11, 2)

    thresh_adaptive_gauss = cv2.adaptiveThreshold(gray, 255,
                                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                  cv2.THRESH_BINARY, 11, 2)

    cv2.imshow("Oryginalny", resized)
    cv2.imshow("Proste T=100", thresh_simple)
    cv2.imshow("Otsu", thresh_otsu)
    cv2.imshow("Adaptacyjne Mean", thresh_adaptive_mean)
    cv2.imshow("Adaptacyjne Gaussian", thresh_adaptive_gauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Komentarze/wnioski:
    # - Proste progowanie (T=100) słabo radzi sobie z nierównym oświetleniem – w niektórych obszarach tło i obiekty się zlewają.
    # - Otsu wybiera globalny próg, działa lepiej niż proste T=100, ale nadal może mieć problemy z cieniami i jasnymi partiami.
    # - Progowanie adaptacyjne (Mean i Gaussian) najlepiej radzi sobie z nierównym oświetleniem, ponieważ próg obliczany jest lokalnie – segmentacja jest bardziej jednolita i czytelna.


if __name__ == "__main__":
    porownanie_metod_progowania("../data/img.png")