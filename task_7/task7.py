import cv2

def analyze_saturation(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    s_lowered = cv2.subtract(s, 50)
    hsv_lowered = cv2.merge([h, s_lowered, v])
    image_lowered = cv2.cvtColor(hsv_lowered, cv2.COLOR_HSV2BGR)

    s_boosted = cv2.add(s, 50)
    hsv_boosted = cv2.merge([h, s_boosted, v])
    image_boosted = cv2.cvtColor(hsv_boosted, cv2.COLOR_HSV2BGR)

    cv2.imshow("Original", image)
    cv2.imshow("Lower Saturation", image_lowered)
    cv2.imshow("Higher Saturation", image_boosted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    analyze_saturation("../data/img.png")
