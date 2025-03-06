import cv2

def modify_row(path):
    image = cv2.imread(path)

    if image is None:
        print("Failed to load image.")
        return

    cv2.imshow('Before Modification', image)

    height, width, _ = image.shape

    if height > 100:
        image[100, :] = (0, 255, 0)
    else:
        print("The image is too small to modify the 100th row.")
        return

    cv2.imshow('After Modification', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/example.jpg"
    modify_row(image_path)
