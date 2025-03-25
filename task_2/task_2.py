import cv2

def run():
    img1 = cv2.imread("../data/example.png")
    img2 = cv2.imread("../data/shifted_example.png")

    if img1.shape != img2.shape:
        print("Images must have the same dimensions!")
        return

    difference = cv2.bitwise_xor(img1, img2)

    cv2.imshow("Image 1", img1)
    cv2.imshow("Image 2", img2)
    cv2.imshow("XOR Difference", difference)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
