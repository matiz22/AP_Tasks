import cv2

def increase_saturation(image_path, increase_value=30):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    s = cv2.add(s, increase_value)

    hsv_modified = cv2.merge([h, s, v])
    image_modified = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)

    cv2.imshow("Original", image)
    cv2.imshow("Modified (Increased Saturation)", image_modified)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    increase_saturation("../data/img.png", 100)
