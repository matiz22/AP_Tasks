import cv2
import numpy as np


def run(image_path, center, axes, angle):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return

    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    cv2.ellipse(mask, center, axes, angle, 0, 360, 255, -1)

    masked_img = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original Image", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Masked Image", masked_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "../data/example.png"
    face_center = (540, 540)
    face_axes = (400, 400)
    face_angle = 0

    run(image_path, face_center, face_axes, face_angle)