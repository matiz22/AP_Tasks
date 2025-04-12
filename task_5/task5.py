import cv2


def otsu_thresholding(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    brightened_image = cv2.add(gray_image, 50)

    _, threshold_otsu = cv2.threshold(brightened_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    cv2.imshow("Original Image", gray_image)
    cv2.imshow("Brightened Image", brightened_image)
    cv2.imshow("Otsu Thresholding", threshold_otsu)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    otsu_thresholding("../data/img.png")

#*
# dostosowuje próg na podstawie obrazu, co może dawać lepsze rezultaty
# *#