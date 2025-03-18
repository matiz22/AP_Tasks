import cv2

def run():
    img = cv2.imread('../data/example.png')

    roi_width, roi_height = 100, 100

    height, width = img.shape[:2]

    startX = 0
    startY = height // 2 - roi_height // 2

    while startX + roi_width <= width:
        endX = startX + roi_width
        endY = startY + roi_height

        roi = img[startY:endY, startX:endX]

        cv2.imshow("Moving ROI", roi)

        key = cv2.waitKey(500)
        if key == 27:
            break

        startX += 10

    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
