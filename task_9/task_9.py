import cv2

def run():
    img = cv2.imread('../data/example.png')

    startX, startY = 50, 50

    width, height = 300, 300

    cropped_image = img[startY:startY + height, startX:startX + width]

    cv2.imwrite('cropped_image.jpg', cropped_image)

    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
