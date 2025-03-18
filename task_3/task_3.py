import cv2


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    resized_img = cv2.resize(img, (200, 300))

    cv2.imshow("Resized Image (200x300)", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
