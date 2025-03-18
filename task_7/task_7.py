import cv2


def run():
    img = cv2.imread('../data/example.png')

    height, width = img.shape[:2]

    cell_height = height // 3
    cell_width = width // 3

    for i in range(3):
        for j in range(3):
            startX = j * cell_width
            startY = i * cell_height
            endX = (j + 1) * cell_width
            endY = (i + 1) * cell_height

            cell = img[startY:endY, startX:endX]

            cv2.imshow(f"Grid Cell ({i}, {j})", cell)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
