import cv2
import os

def numeruj_i_zapisz_kostki(image_path, output_dir="kostki"):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    os.makedirs(output_dir, exist_ok=True)

    resized = cv2.resize(image, (300, int(image.shape[0] * 300 / image.shape[1])))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # zmieniłem zdj zmieniam na 140
    _, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result = resized.copy()

    for i, contour in enumerate(contours, 1):
        x, y, w, h = cv2.boundingRect(contour)
        cx, cy = x + w // 2, y + h // 2

        cv2.putText(result, str(i), (cx - 10, cy), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 1, cv2.LINE_AA)

        roi = resized[y:y + h, x:x + w]
        filename = os.path.join(output_dir, f"kostka_{i:02d}.png")
        cv2.imwrite(filename, roi)

    cv2.imshow("Ponumerowane kostki", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    numeruj_i_zapisz_kostki("../data/img_1.png")
