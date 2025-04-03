import cv2


def simulate_depth_of_field(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)

    _, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    mask = cv2.bitwise_not(thresholded)
    result = cv2.bitwise_and(image, image, mask=mask)

    blurred_bg = cv2.GaussianBlur(image, (21, 21), 0)
    final_image = cv2.add(result, blurred_bg)

    cv2.imshow("Efekt głebokości", final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = '../data/img.png'
    simulate_depth_of_field(image_path)
