import cv2


def run():
    img = cv2.imread('../data/example.png')

    height, width = img.shape[:2]

    bottom_half = img[height // 2:, :]

    cv2.imshow("Bottom Half", bottom_half)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
