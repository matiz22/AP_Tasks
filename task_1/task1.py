import cv2


def thresholding_example(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold_30 = cv2.threshold(gray_image, 30, 255, cv2.THRESH_BINARY)
    _, threshold_100 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
    _, threshold_200 = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original Image", image)
    cv2.imshow("Thresholded (T=30)", threshold_30)
    cv2.imshow("Thresholded (T=100)", threshold_100)
    cv2.imshow("Thresholded (T=200)", threshold_200)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    thresholding_example("../data/img.png")
