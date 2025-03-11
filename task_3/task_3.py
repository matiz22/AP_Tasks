import cv2
import numpy as np


def draw_shapes():
    image = np.zeros((300, 300, 3), dtype=np.uint8)

    blue_center = (40, 40)
    blue_radius = 40
    blue_color = (255, 0, 0)
    cv2.circle(image, blue_center, blue_radius, blue_color, -1)

    red_center = (150, 150)
    red_radius = 60
    red_color = (0, 0, 255)
    cv2.circle(image, red_center, red_radius, red_color, -1)

    cv2.imshow("Image with Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    draw_shapes()