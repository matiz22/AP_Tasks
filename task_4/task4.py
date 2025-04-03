import cv2

def blur_text_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    blur_avg = cv2.blur(image, (5, 5))
    blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)
    blur_median = cv2.medianBlur(image, 5)
    blur_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Oryginalny obraz", image)
    cv2.imshow("Rozmycie proste (5x5)", blur_avg)
    cv2.imshow("Rozmycie Gaussa (5x5)", blur_gaussian)
    cv2.imshow("Rozmycie medianowe (5x5)", blur_median)
    cv2.imshow("Rozmycie dwustronne", blur_bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    blur_text_image("../data/img_3.png")

#*
# Dla zdj, które wybrałem metoda medianowa i prosta najbardziej rozmyła napis
# Tekst został widoczny dla Gaussa
# *#