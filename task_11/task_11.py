import cv2

def find_brightest_pixel(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray_image)

    b, g, r = image[max_loc[1], max_loc[0]]

    print(f"Brightest pixel at: {max_loc}")
    print(f"Brightness value (grayscale): {max_val}")
    print(f"Color value (B, G, R): ({b}, {g}, {r})")




if __name__ == "__main__":
    image_path = "../data/example.jpg"
    find_brightest_pixel(image_path)
