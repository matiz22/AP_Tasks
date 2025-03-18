import cv2


def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    height, width = img.shape[:2]

    new_height = 400
    aspect_ratio = new_height / height
    new_width = int(width * aspect_ratio)

    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    cv2.imshow("Resized Image (Height 400)", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
