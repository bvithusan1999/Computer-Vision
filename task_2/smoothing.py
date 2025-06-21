import cv2
def average_filter(image, ksize):
    return cv2.blur(image, (ksize, ksize))
