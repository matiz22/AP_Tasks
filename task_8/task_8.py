import cv2
import numpy as np

def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    resized_cubic = cv2.resize(img, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    resized_lanczos = cv2.resize(img, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

    comparison = np.hstack((resized_cubic, resized_lanczos))

    cv2.imshow("Upscaling Comparison (Cubic - Lanczos4)", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
