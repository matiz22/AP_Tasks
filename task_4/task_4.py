import cv2
import numpy as np


def draw_shapes():
    image = np.zeros((300, 300, 3), dtype=np.uint8)

    center = (150, 150)

    square_top_left = (100, 100)
    square_bottom_right = (200, 200)
    square_color = (255, 255, 255)
    cv2.rectangle(image, square_top_left, square_bottom_right, square_color, -1)

    circle_radius = 30
    circle_color = (0, 255, 0)
    cv2.circle(image, center, circle_radius, circle_color, -1)

    cv2.imshow("Complex Figure", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    draw_shapes()