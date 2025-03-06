import cv2


def fill_center_square(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    height, width, _ = image.shape

    center_x, center_y = width // 2, height // 2

    half_size = 50
    start_x, end_x = max(0, center_x - half_size), min(width, center_x + half_size)
    start_y, end_y = max(0, center_y - half_size), min(height, center_y + half_size)

    image[start_y:end_y, start_x:end_x] = (0, 0, 255)

    cv2.imshow('Modified Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    path = "../data/example.jpg"
    fill_center_square(path)
