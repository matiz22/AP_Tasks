import cv2

def read_pixel(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    pixel = image[0, 0]
    b, g, r = pixel
    print(f"Color components (B, G, R): ({b}, {g}, {r})")

if __name__ == "__main__":
    image_path = "../data/example.jpg"
    read_pixel(image_path)
