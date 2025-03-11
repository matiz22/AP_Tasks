import cv2
import numpy as np


def draw_shapes():
    image = np.zeros((400, 400, 3), dtype=np.uint8)

    top_left_start = (0, 0)
    top_left_end = (100, 50)
    green_color = (0, 255, 0)
    cv2.rectangle(image, top_left_start, top_left_end, green_color, -1)

    bottom_right_start = (300, 350)
    bottom_right_end = (399, 399)
    red_color = (0, 0, 255)
    cv2.rectangle(image, bottom_right_start, bottom_right_end, red_color, 3)

    cv2.imshow("Image with Rectangles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    draw_shapes()
