import cv2
import os
import numpy as np

def licz_kostki(image_path, output_dir="kostki_finalne"):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    resized = cv2.resize(image, (300, int(image.shape[0] * 300 / image.shape[1])))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result = resized.copy()
    dimensions = []
    idx = 1

    for contour in contours:
        area = cv2.contourArea(contour)
        if 500 <= area <= 5000:
            x, y, w, h = cv2.boundingRect(contour)
            dimensions.append((w, h))

            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(result, f"{w}x{h}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.4, (0, 255, 0), 1, cv2.LINE_AA)

            roi = resized[y:y + h, x:x + w]
            idx += 1

    if dimensions:
        widths, heights = zip(*dimensions)
        print(f"Liczba wykrytych kostek: {len(dimensions)}")
        print(f"Średnia szerokość: {np.mean(widths):.2f} px")
        print(f"Średnia wysokość: {np.mean(heights):.2f} px")
        print(f"Minimalny rozmiar: {min(widths)}x{min(heights)} px")
        print(f"Maksymalny rozmiar: {max(widths)}x{max(heights)} px")
    else:
        print("Nie wykryto żadnych kostek w zadanym zakresie powierzchni.")

    cv2.imshow("Kostki - raport", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    licz_kostki("../data/img_1.png")
