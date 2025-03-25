import cv2
import numpy as np

def mask_eyes(image_path, eye_top_left, eye_bottom_right):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or unable to load.")

    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    cv2.rectangle(mask, eye_top_left, eye_bottom_right, 255, -1)

    masked_img = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Masked Eyes", masked_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "../data/example.png"

    eye_top_left = (280, 400)
    eye_bottom_right = (820, 520)

    mask_eyes(image_path, eye_top_left, eye_bottom_right)
