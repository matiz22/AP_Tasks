import cv2


def run():
    img = cv2.imread('../data/example.png')

    height, width = img.shape[:2]

    right_half = img[:, width // 2:]

    flipped_right_half = cv2.flip(right_half, 1)

    img[:, width // 2:] = flipped_right_half

    cv2.imshow("Image with Flipped Right Half", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
