import cv2
import imutils


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    resized_img = imutils.resize(img, width=500)

    cv2.imshow("Resized Image (Width 500)", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
