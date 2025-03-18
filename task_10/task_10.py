import cv2

def run():
    img = cv2.imread('../data/example.png')

    aspect_ratio = 800 / img.shape[1]
    new_height = int(img.shape[0] * aspect_ratio)
    resized_img = cv2.resize(img, (800, new_height), interpolation=cv2.INTER_LINEAR)

    cv2.imwrite('resized_output.jpg', resized_img)

if __name__ == "__main__":
    run()
