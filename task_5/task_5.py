import cv2


def color_top_left_quarter(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    height, width, _ = image.shape

    quarter_height, quarter_width = height // 2, width // 2

    image[0:quarter_height, 0:quarter_width] = (255, 0, 0)

    cv2.imshow('Modified Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/example.jpg"
    color_top_left_quarter(image_path)