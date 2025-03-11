import cv2

def anonymize_face(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load the image.")
        return

    eye_left = (311, 136)
    eye_right = (347, 143)
    mouth_left_up = (308, 177)
    mouth_right_down = (350, 190)
    face_center = (346, 141)
    face_radius = 80

    cv2.circle(image, eye_left, 10, (0, 0, 255), -1)
    cv2.circle(image, eye_right, 10, (0, 0, 255), -1)

    cv2.rectangle(image, mouth_left_up, mouth_right_down, (0, 255, 0), -1)

    cv2.circle(image, face_center, face_radius, (255, 0, 0), 2)

    cv2.imshow("Anonymized Face", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "../data/img.png"
    anonymize_face(image_path)
