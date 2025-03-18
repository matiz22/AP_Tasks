import cv2

def run():
    img = cv2.imread('../data/example.png')
    cv2.imshow("Original Image", img)

    scale_factor = 1.0
    while scale_factor <= 3.0:
        resized_img = cv2.resize(img, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
        cv2.imshow(f"Scaled Image ({int(scale_factor * 100)}%)", resized_img)
        cv2.waitKey(500)
        scale_factor += 0.2

    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
