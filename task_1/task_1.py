import cv2


def run():
    img = cv2.imread('../data/example.png')

    roi = img[0:100, 0:100]

    cv2.imshow("ROI - Top Left Corner (100x100)", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
