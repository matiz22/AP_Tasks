import cv2


def open_2_imgs(path1, path2):
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    if img1 is None:
        print(f"Błąd: Nie udało się wczytać obrazu {path1}")
    if img2 is None:
        print(f"Błąd: Nie udało się wczytać obrazu {path2}")

    if img1 is not None:
        cv2.imshow("Obraz 1", img1)
    if img2 is not None:
        cv2.imshow("Obraz 2", img2)

    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == ord('1'):
            cv2.destroyWindow("Obraz 1")
        elif key == ord('2'):
            cv2.destroyWindow("Obraz 2")

        if cv2.getWindowProperty("Obraz 1", cv2.WND_PROP_VISIBLE) < 1 and cv2.getWindowProperty("Obraz 2", cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    open_2_imgs("../data/example.png", "../data/example_gray.png")
