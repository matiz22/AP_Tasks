import cv2
import numpy as np

def run():
    img1 = np.zeros((200, 200), dtype=np.uint8)
    img2 = np.zeros((200, 200), dtype=np.uint8)

    triangle_pts = np.array([[100, 50], [50, 150], [150, 150]], np.int32)
    cv2.fillPoly(img1, [triangle_pts], 255)

    cv2.circle(img2, (100, 100), 50, 255, -1)

    bitwise_and = cv2.bitwise_and(img1, img2)
    bitwise_or = cv2.bitwise_or(img1, img2)
    bitwise_xor = cv2.bitwise_xor(img1, img2)
    bitwise_not_triangle = cv2.bitwise_not(img1)
    bitwise_not_circle = cv2.bitwise_not(img2)

    cv2.imshow("Triangle", img1)
    cv2.imshow("Circle", img2)
    cv2.imshow("AND (Intersection)", bitwise_and)
    cv2.imshow("OR (Union)", bitwise_or)
    cv2.imshow("XOR (Non-overlapping)", bitwise_xor)
    cv2.imshow("NOT Triangle (Inverted)", bitwise_not_triangle)
    cv2.imshow("NOT Circle (Inverted)", bitwise_not_circle)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
