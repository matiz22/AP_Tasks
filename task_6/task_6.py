import cv2

def open_and_show_resized(path):
    img = cv2.imread(path)
    cv2.imshow('Obraz', img)

    cv2.namedWindow('Obraz', cv2.WINDOW_NORMAL)

    cv2.resizeWindow('Obraz', img.shape[1], img.shape[0])

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    open_and_show_resized('../data/example.png')
