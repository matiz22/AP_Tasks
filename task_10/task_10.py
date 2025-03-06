import cv2

def compare_pixel_values(path):
    image = cv2.imread(path)

    if image is None:
        print("Failed to load image.")
        return

    height, width, _ = image.shape

    coord1 = (50, 50)
    coord2 = (200, 200)

    if coord1[0] >= width or coord1[1] >= height or coord2[0] >= width or coord2[1] >= height:
        print("One or both coordinates are out of bounds.")
        return

    b1, g1, r1 = image[coord1[1], coord1[0]]
    b2, g2, r2 = image[coord2[1], coord2[0]]

    diff_r = abs(r1 - r2)
    diff_g = abs(g1 - g2)
    diff_b = abs(b1 - b2)

    print(f"Pixel at {coord1}: (B: {b1}, G: {g1}, R: {r1})")
    print(f"Pixel at {coord2}: (B: {b2}, G: {g2}, R: {r2})")
    print(f"Difference - R: {diff_r}, G: {diff_g}, B: {diff_b}")


if __name__ == "__main__":
    image_path = "../data/example.jpg"
    compare_pixel_values(image_path)
