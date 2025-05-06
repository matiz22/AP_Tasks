import cv2

def adaptacyjne_blocksize(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Nie znaleziono obrazu pod podaną ścieżką.")

    resized = cv2.resize(image, (300, int(image.shape[0] * 300 / image.shape[1])))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    block_sizes = [11, 21, 31, 41]

    for block in block_sizes:
        if block % 2 == 1 and block > 1:
            thresh = cv2.adaptiveThreshold(gray, 255,
                                           cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, block, 2)
            cv2.imshow(f"Adaptive Threshold - blockSize={block}", thresh)

    cv2.imshow("Oryginalny", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # blockSize=21 najlepiej radzi sobie z detekcją konturów w przypadku silnych różnic oświetlenia,
    # zapewniając dobry balans między czułością a odpornością na szum.

if __name__ == "__main__":
    adaptacyjne_blocksize("../data/img.png")
