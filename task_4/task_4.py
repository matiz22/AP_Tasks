import cv2


def wykrywanie_logo(image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    if image is None or template is None:
        raise ValueError("Nie znaleziono obrazu lub szablonu pod podanymi ścieżkami.")

    (tH, tW) = template.shape[:2]

    methods = [
        cv2.TM_CCOEFF,
        cv2.TM_CCOEFF_NORMED,
        cv2.TM_CCORR,
        cv2.TM_CCORR_NORMED,
        cv2.TM_SQDIFF,
        cv2.TM_SQDIFF_NORMED
    ]

    for method in methods:
        result = cv2.matchTemplate(image, template, method)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            min_val, _, min_loc, _ = cv2.minMaxLoc(result)
            top_left = min_loc
            bottom_right = (top_left[0] + tW, top_left[1] + tH)
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            print(f"Metoda: {method}, MinVal: {min_val}")
        else:
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            top_left = max_loc
            bottom_right = (top_left[0] + tW, top_left[1] + tH)
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            print(f"Metoda: {method}, MaxVal: {max_val}")

        cv2.imshow(f"Wykryte logo - metoda {method}", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    wykrywanie_logo("../data/img.png", "../data/img_1.png")
#cv2.TM_CCORR_NORMED,