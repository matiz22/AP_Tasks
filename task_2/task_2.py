import cv2


def modify_pixel(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    cv2.imshow('Before Modification', image)

    height, width, _ = image.shape

    image[height - 1, width - 1] = (0, 0, 255)

    cv2.imshow('After Modification', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "../data/example.jpg"
    modify_pixel(image_path)
