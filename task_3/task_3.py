import cv2


def run():
    img = cv2.imread('../data/example.png')

    height, width = img.shape[:2]

    right_half = img[:, width // 2:]

    cv2.imshow("Right Half", right_half)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
