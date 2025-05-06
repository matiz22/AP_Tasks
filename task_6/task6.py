import cv2

def nothing(x):
    pass

def interaktywna_segmentacja(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    resized = cv2.resize(image, (600, int(image.shape[0] * 600 / image.shape[1])))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow("Segmentacja")

    cv2.createTrackbar("blockSize", "Segmentacja", 11, 51, nothing)
    cv2.createTrackbar("C", "Segmentacja", 10, 40, nothing)

    while True:
        b = cv2.getTrackbarPos("blockSize", "Segmentacja")
        c = cv2.getTrackbarPos("C", "Segmentacja")

        if b < 3:
            b = 3
        if b % 2 == 0:
            b += 1

        C = c - 20

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        binary = cv2.adaptiveThreshold(
            blurred,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            blockSize=b,
            C=C
        )

        cv2.imshow("Segmentacja", binary)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    interaktywna_segmentacja("../data/img.png")
