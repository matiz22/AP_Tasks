import cv2


def draw_line_on_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load the image.")
        return

    height, width, _ = image.shape
    start_point = (width // 2, height // 2)
    end_point = (width - 1, height - 1)
    color = (255, 0, 0)  # Blue in BGR format
    thickness = 2

    cv2.line(image, start_point, end_point, color, thickness)
    cv2.imshow("Image with Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    input_image_path = "../data/example.png"
    draw_line_on_image(input_image_path)