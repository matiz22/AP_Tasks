import cv2


def run():
    img = cv2.imread('../data/example.png')

    flipped_img = cv2.flip(img, 1)

    cv2.imshow("Horizontal Flip", flipped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
