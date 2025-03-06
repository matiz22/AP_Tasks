import cv2


def set_pixel_to_black(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    height, width, _ = image.shape

    x = int(input(f"Enter x coordinate (0 to {width - 1}): "))
    y = int(input(f"Enter y coordinate (0 to {height - 1}): "))

    if x < 0 or x >= width or y < 0 or y >= height:
        print("Coordinates are out of bounds.")
        return

    image[y, x] = (0, 0, 0)

    cv2.imshow('Modified Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/example.jpg"
    set_pixel_to_black(image_path)