import cv2


def wykrywanie_logo(image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    if image is None or template is None:
        raise ValueError("Nie znaleziono obrazu lub szablonu pod podanymi ścieżkami.")

    (tH, tW) = template.shape[:2]

    scales = [0.5, 1.5]

    for scale in scales:
        resized_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

        result = cv2.matchTemplate(resized_image, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        top_left = max_loc
        bottom_right = (top_left[0] + tW, top_left[1] + tH)
        cv2.rectangle(resized_image, top_left, bottom_right, (0, 255, 0), 2)

        cv2.imshow(f"Wykryte logo (skala {scale})", resized_image)
        print(f"Skala: {scale}, MaxVal: {max_val}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    wykrywanie_logo("../data/img.png", "../data/img_1.png")
    #nie działa poprawnie
