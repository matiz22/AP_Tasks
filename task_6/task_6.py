import cv2

def run():
    img = cv2.imread('../data/example.png')

    flip_choice = int(input("Enter the type of flip (0 for vertical, 1 for horizontal, -1 for both): "))

    flipped_img = cv2.flip(img, flip_choice)

    cv2.imshow("Flipped Image", flipped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
