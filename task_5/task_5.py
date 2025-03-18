import cv2

def run():
    img = cv2.imread('../data/example.png')

    startX = 130
    startY = 47
    endX = 300
    endY = 220

    height, width = img.shape[:2]
    startX = max(0, min(startX, width))
    startY = max(0, min(startY, height))
    endX = max(0, min(endX, width))
    endY = max(0, min(endY, height))

    face_crop = img[startY:endY, startX:endX]

    cv2.imshow("Cropped Face", face_crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
