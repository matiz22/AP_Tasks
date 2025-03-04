import cv2

from task_3.task_3 import open_in_gray_and_print_channel


def open_in_gray_and_print_channel_with_save(path):
    img = open_in_gray_and_print_channel(path)
    cv2.imwrite("../data/example_gray.png", img)

if __name__ == '__main__':
    open_in_gray_and_print_channel_with_save("../data/example.png")