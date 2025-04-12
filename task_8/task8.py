import cv2
import numpy as np

def segment_multiple_colors(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)

    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    combined_mask = cv2.bitwise_or(mask_blue, mask_red)
    combined_mask = cv2.bitwise_or(combined_mask, mask_green)

    segmented = cv2.bitwise_and(image, image, mask=combined_mask)

    cv2.imshow("Original", image)
    cv2.imshow("Segmented (Red, Green, Blue)", segmented)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    segment_multiple_colors("../data/img.png")
