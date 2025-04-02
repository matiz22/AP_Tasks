import cv2


def apply_opening(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Nie można wczytać obrazu.")

    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    kernel_sizes = [3, 5, 7]
    results = {}

    for size in kernel_sizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))

        opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        results[size] = opened

    cv2.imshow("Obraz przed otwarciem", binary)

    for size, opened_img in results.items():
        cv2.imshow(f"Otwarcie {size}x{size}", opened_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    apply_opening("../data/img_3.png")
