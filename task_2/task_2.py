import cv2


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    resized_img = cv2.resize(img, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    cv2.imshow("Resized Image (200%)", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
