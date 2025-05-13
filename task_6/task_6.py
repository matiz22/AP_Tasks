import cv2
import numpy as np

def detekcja_falszywych_trafien(image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    if image is None or template is None:
        raise ValueError("Nie znaleziono obrazu lub szablonu pod podanymi ścieżkami.")

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):
        cv2.rectangle(image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

    print(f"Liczba wykrytych obiektów: {len(locations[0])}")
    cv2.imshow("Wykryte obiekty", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detekcja_falszywych_trafien("../data/img_3.png", "../data/img_5.png")
