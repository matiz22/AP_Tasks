import cv2

def apply_blur_with_kernels(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    kernel_sizes = [3, 5, 9, 15]

    for k in kernel_sizes:
        blur_simple = cv2.blur(image, (k, k))

        blur_gaussian = cv2.GaussianBlur(image, (k, k), 0)

        blur_median = cv2.medianBlur(image, k)

        blur_bilateral = cv2.bilateralFilter(image, k, 75, 75)

        cv2.imshow(f"Rozmycie proste ({k}x{k})", blur_simple)
        cv2.imshow(f"Rozmycie Gaussa ({k}x{k})", blur_gaussian)
        cv2.imshow(f"Rozmycie medianowe ({k}x{k})", blur_median)
        cv2.imshow(f"Rozmycie dwustronne (d={k})", blur_bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    apply_blur_with_kernels("../data/img.png")

#*
# Zbyt duże wartość kernela powoduje artefakty na zdjęciu.
# Kernel powinnien skalować się z rozdzielczością.
# Wartości optymalne dla malych zdj to 3x3 5x5
# *$
