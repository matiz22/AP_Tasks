import cv2


def otsu_segmentation(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, otsu_mask = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    result = cv2.bitwise_and(image, image, mask=otsu_mask)

    cv2.imshow("Original Image", image)
    cv2.imshow("Otsu Mask", otsu_mask)
    cv2.imshow("Segmented Object", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    otsu_segmentation("../data/img.png")

#Zbyt mały kontrast między tłem a obiektem, obecność szumów i złożoność obrazu mogą ograniczyć skuteczność tej metody.