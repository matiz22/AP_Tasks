import cv2

def fill_region_with_white(path):
    image = cv2.imread(path)

    if image is None:
        print("Failed to load image.")
        return

    cv2.imshow('Before Modification', image)

    height, width, _ = image.shape

    start_x, start_y = 50, 50
    end_x, end_y = min(100, width), min(100, height)

    image[start_y:end_y, start_x:end_x] = (255, 255, 255)

    cv2.imshow('After Modification', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "../data/example.jpg"
    fill_region_with_white(image_path)
