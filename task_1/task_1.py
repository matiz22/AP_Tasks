import cv2


def split_and_save_channels(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Nie znaleziono obrazu lub nie można go załadować.")

    (B, G, R) = cv2.split(img)
    path_data = "../data/"
    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)

    cv2.imwrite(f"{path_data}blue_channel.jpg", B)
    cv2.imwrite(f"{path_data}green_channel.jpg", G)
    cv2.imwrite(f"{path_data}red_channel.jpg", R)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/example.jpg"

    split_and_save_channels(image_path)
