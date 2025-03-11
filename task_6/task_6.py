import cv2
import imutils


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    rotated_img = imutils.rotate_bound(img, -33)

    cv2.imshow("Rotated Image", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
