import cv2
import numpy as np

def add_noise(image, noise_type="salt_pepper"):
    if noise_type == "salt_pepper":
        noise_img = image.copy()
        prob = 0.02
        num_salt = int(prob * image.size)
        coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
        noise_img[coords[0], coords[1]] = 255

        num_pepper = int(prob * image.size)
        coords = [np.random.randint(0, i-1, num_pepper) for i in image.shape]
        noise_img[coords[0], coords[1]] = 0
        return noise_img
    elif noise_type == "gaussian":
        noise = np.zeros_like(image)
        cv2.randn(noise, (0), (50))
        noisy_image = cv2.add(image, noise)
        return noisy_image
    return image

def apply_blurring_methods(image):
    blur_avg = cv2.blur(image, (5, 5))

    blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

    blur_median = cv2.medianBlur(image, 5)

    blur_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Oryginalny obraz z szumem", image)
    cv2.imshow("Rozmycie proste (5x5)", blur_avg)
    cv2.imshow("Rozmycie Gaussa (5x5)", blur_gaussian)
    cv2.imshow("Rozmycie medianowe (5x5)", blur_median)
    cv2.imshow("Rozmycie dwustronne", blur_bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    img = cv2.imread("../data/img.png")

    if img is None:
        raise ValueError("Nie udało się wczytać obrazu.")

    noisy_img_gaussian = add_noise(img, "gaussian")
    noisy_img_sp = add_noise(img, "salt_pepper")

    apply_blurring_methods(noisy_img_gaussian)
    apply_blurring_methods(noisy_img_sp)


#*
# Szum gausian
# Dla wybranego zdjęcia szum wyeliminowało najlepiej rozmycie Gaussa
# Szum salt pepper
# Najlepszy wynik metoda medianowa
# *#