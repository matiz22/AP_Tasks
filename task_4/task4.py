import cv2

def segmentacja_tekstu_dokument(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    binary = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blockSize=15,
        C=10
    )

    cv2.imshow("Oryginalny", image)
    cv2.imshow("Tekst - progowanie adaptacyjne", binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    segmentacja_tekstu_dokument("../data/img_1.png")
