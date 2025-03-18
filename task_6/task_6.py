import cv2


def run():
    img = cv2.imread('../data/example.png')

    startX, startY = 50, 50
    endX, endY = startX + 100, startY + 100

    cropped_region = img[startY:endY, startX:endX]

    pasteX, pasteY = 200, 200

    h, w = cropped_region.shape[:2]
    if pasteY + h <= img.shape[0] and pasteX + w <= img.shape[1]:
        img[pasteY:pasteY + h, pasteX:pasteX + w] = cropped_region

    cv2.imshow("Image with Pasted Region", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
