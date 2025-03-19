import cv2
import numpy as np

def run():
    img = cv2.imread('../data/example.png')

    b, g, r = cv2.split(img)

    r = cv2.add(r, 30)
    g = cv2.subtract(g, 20)
    b = cv2.add(b, 10) 

    filtered_img = cv2.merge([b, g, r])

    cv2.imshow("Original Image", img)
    cv2.imshow("Filtered Image", filtered_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
