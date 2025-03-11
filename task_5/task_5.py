import cv2
import numpy as np


def draw_shapes():
    image = np.zeros((300, 300, 3), dtype=np.uint8)

    center = (150, 150)

    num_squares = 5
    initial_size = 40
    increment = 20
    square_color = (255, 255, 255)

    for i in range(num_squares):
        size = initial_size + i * increment
        top_left = (center[0] - size // 2, center[1] - size // 2)
        bottom_right = (center[0] + size // 2, center[1] + size // 2)
        cv2.rectangle(image, top_left, bottom_right, square_color, 1)

    cv2.imshow("Growing Squares", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    draw_shapes()