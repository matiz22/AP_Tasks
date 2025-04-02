import cv2


def apply_erosion(image_path, kernel_shape, kernel_size):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    if kernel_shape == "square":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    elif kernel_shape == "ellipse":
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    else:
        raise ValueError("Nieznany kształt elementu strukturalnego.")

    eroded_img = cv2.erode(binary_img, kernel, iterations=1)

    cv2.imshow("Original Binary Image", binary_img)
    cv2.imshow(f"Eroded Image ({kernel_shape})", eroded_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path = "../data/img_3.png"
    apply_erosion(path, kernel_shape="square", kernel_size=2)
    apply_erosion(path, kernel_shape="ellipse", kernel_size=2)
