import cv2
def reduce_intensity_levels(image, levels):
    grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    factor = 256 // levels
    return (grayScaleImage // factor) * factor