import cv2

def run():
    img = cv2.imread('../data/example.png')

    startX = int(input("Enter the start X coordinate: "))
    endX = int(input("Enter the end X coordinate: "))
    startY = int(input("Enter the start Y coordinate: "))
    endY = int(input("Enter the end Y coordinate: "))

    height, width = img.shape[:2]
    startX = max(0, min(startX, width))
    endX = max(0, min(endX, width))
    startY = max(0, min(startY, height))
    endY = max(0, min(endY, height))

    roi = img[startY:endY, startX:endX]

    cv2.imshow("Cropped ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
