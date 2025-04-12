import cv2


def thresholding_with_blurring(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    _, threshold_100_no_blur = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
    _, threshold_100_blur = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original Image", image)

    cv2.imshow("Thresholded (T=100) - No Blur", threshold_100_no_blur)

    cv2.imshow("Thresholded (T=100) - With Blur", threshold_100_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    thresholding_with_blurring("../data/img.png")
