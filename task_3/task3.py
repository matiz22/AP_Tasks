import cv2

def apply_bilateral_filter(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    bilateral_params = [(5, 75, 75), (9, 150, 150), (15, 250, 250)]

    for d, sigma_color, sigma_space in bilateral_params:
        bilateral = cv2.bilateralFilter(image, d, sigma_color, sigma_space)
        cv2.imshow(f"Rozmycie dwustronne d={d}, σ_color={sigma_color}, σ_space={sigma_space}", bilateral)

    blur_gaussian = cv2.GaussianBlur(image, (9, 9), 0)
    blur_median = cv2.medianBlur(image, 9)

    cv2.imshow("Rozmycie Gaussa (9x9)", blur_gaussian)
    cv2.imshow("Rozmycie medianowe (9x9)", blur_median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    apply_bilateral_filter("../data/img_2.png")

#*
# Rozmycie dwustronne skutecznie redukuje szum, lepiej niż inne metody, ponieważ nie rozmywa obszarów z teksturą.
# W przeciwieństwie do filtrów Gaussa i medianowego, zachowuje krawędzie.
# Optymalne parametry to np. d = 9, σ_color = 150, σ_space = 150 dla balansu między redukcją szumu a krawędziami lub d = 15, σ_color = 250, σ_space = 250 dla mocniejszego wygładzenia przy zachowaniu krawędzi.
# *#
