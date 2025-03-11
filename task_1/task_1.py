import cv2
import numpy as np


def shift_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Error: Could not load the image.")
        return

    cv2.imshow("Original Image", image)
    cv2.waitKey(0)

    height, width = image.shape[:2]
    M = np.float32([[1, 0, 30], [0, 1, 40]])
    shifted_image = cv2.warpAffine(image, M, (width, height))

    cv2.imshow("Shifted Image", shifted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "../data/example.png"
    shift_image(image_path)
