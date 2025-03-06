import cv2

def extract_center_region(path):
    image = cv2.imread(path)

    if image is None:
        print("Failed to load image.")
        return

    height, width, _ = image.shape

    third_height, third_width = height // 3, width // 3

    start_x, end_x = third_width, 2 * third_width
    start_y, end_y = third_height, 2 * third_height

    center_fragment = image[start_y:end_y, start_x:end_x]

    cv2.imshow('Center Fragment', center_fragment)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/example.jpg"
    extract_center_region(image_path)
