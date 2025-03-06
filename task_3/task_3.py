import cv2


def find_center_and_pixel(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    height, width, _ = image.shape

    center_x, center_y = width // 2, height // 2

    pixel = image[center_y, center_x]
    b, g, r = pixel

    print(f"Center coordinates: ({center_x}, {center_y})")
    print(f"Color components (B, G, R) at center: ({b}, {g}, {r})")


if __name__ == "__main__":
    image_path = "../data/example.jpg"
    find_center_and_pixel(image_path)