import cv2


def apply_closing(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    kernel_sizes = [3, 5, 7]
    kernels = [
        cv2.getStructuringElement(cv2.MORPH_RECT, (size, size)) for size in kernel_sizes
    ]

    results = {}

    for size, kernel in zip(kernel_sizes, kernels):
        closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        results[size] = closed

    cv2.imshow("Obraz przed zamknięciem", binary)

    for size, closed_img in results.items():
        cv2.imshow(f"Zamknięcie {size}x{size}", closed_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    apply_closing("../data/img_3.png")
