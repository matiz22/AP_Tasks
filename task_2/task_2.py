import cv2
import imutils

def wykrywanie_logo(image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    if image is None or template is None:
        raise ValueError("Nie znaleziono obrazu lub szablonu pod podanymi ścieżkami.")

    (tH, tW) = template.shape[:2]

    for angle in [0, 30, 45]:
        rotated = imutils.rotate(image, angle)

        result = cv2.matchTemplate(rotated, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        top_left = max_loc
        bottom_right = (top_left[0] + tW, top_left[1] + tH)
        cv2.rectangle(rotated, top_left, bottom_right, (0, 255, 0), 2)

        cv2.imshow(f"Wykryte logo (obrót {angle}°)", rotated)
        print(f"Kąt obrotu: {angle}°, MaxVal: {max_val}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    wykrywanie_logo("../data/img.png", "../data/img_1.png")
