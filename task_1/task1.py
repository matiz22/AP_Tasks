import cv2

def show_rgb_hsv_channels(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    cv2.imshow("RGB", image)
    for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
        cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
        cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_rgb_hsv_channels("../data/img.png")
