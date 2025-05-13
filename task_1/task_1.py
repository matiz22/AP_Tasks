import cv2

def wykrywanie_logo(image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    if image is None or template is None:
        raise ValueError("Nie znaleziono obrazu lub szablonu pod podanymi ścieżkami.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    (tH, tW) = gray_template.shape[:2]

    result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc
    bottom_right = (top_left[0] + tW, top_left[1] + tH)
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    cv2.imshow("Wykryte logo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Współrzędne lewego górnego rogu: {top_left}")
    print(f"MaxVal: {max_val}")

if __name__ == "__main__":
    wykrywanie_logo("../data/img.png", "../data/img_1.png")
