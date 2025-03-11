import cv2
import imutils


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    rows, cols = img.shape[:2]
    center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(center, 60, 1)
    rotated_img_cv2 = cv2.warpAffine(img, M, (cols, rows))

    rotated_img_imutils = imutils.rotate(img, 60)

    cv2.imshow("Rotated Image (cv2.warpAffine)", rotated_img_cv2)
    cv2.imshow("Rotated Image (imutils.rotate)", rotated_img_imutils)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
