import cv2


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    cv2.imshow("Resized Image (50%)", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
