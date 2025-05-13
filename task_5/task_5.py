import cv2


def detekcja_ikony(image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    if image is None or template is None:
        raise ValueError("Nie znaleziono obrazu lub szablonu pod podanymi ścieżkami.")

    (tH, tW) = template.shape[:2]

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc
    bottom_right = (top_left[0] + tW, top_left[1] + tH)
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    print(f"Wartość dopasowania: {max_val}")
    cv2.imshow("Wykryte logo na oryginalnym obrazie", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detekcja_ikony("../data/img_4.png", "../data/img_2.png")
