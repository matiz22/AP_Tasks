import cv2
import matplotlib.pyplot as plt

def apply_dilation(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Nie można wczytać obrazu.")

    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    kernel_sizes = [3, 5, 7]
    results = {}

    for size in kernel_sizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
        dilated = cv2.dilate(binary, kernel, iterations=1)
        results[size] = dilated

    fig, axes = plt.subplots(1, len(results) + 1, figsize=(12, 4))
    axes[0].imshow(binary, cmap='gray')
    axes[0].set_title("Oryginał")

    for i, (size, img) in enumerate(results.items()):
        axes[i + 1].imshow(img, cmap='gray')
        axes[i + 1].set_title(f"Dylatacja {size}x{size}")

    plt.show()

if __name__ == "__main__":
    apply_dilation("../data/img_3.png")
