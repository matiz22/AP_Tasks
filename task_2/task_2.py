import cv2


def analyze_channels(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    (B, G, R) = cv2.split(img)

    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    image_path = "../data/img.png"
    analyze_channels(image_path)
