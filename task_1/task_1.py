import cv2


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    rows, cols = img.shape[:2]
    center = (cols // 2, rows // 2)

    M = cv2.getRotationMatrix2D(center, 45, 1)

    rotated_img = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("Rotated Image", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
