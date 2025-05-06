import cv2

def automatyczna_maska_roi(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    binary_mask = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blockSize=21,
        C=10
    )

    roi = cv2.bitwise_and(image, image, mask=binary_mask)

    # Wyświetlenie wyników
    cv2.imshow("Oryginalny", image)
    cv2.imshow("Maska obiektów", binary_mask)
    cv2.imshow("Obiekty (ROI)", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    automatyczna_maska_roi("../data/img_2.png")
