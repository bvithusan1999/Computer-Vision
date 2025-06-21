# main.py

import cv2
from task_1.intensity_reduction import reduce_intensity_levels
from task_2.smoothing import average_filter
from task_3.rotation import rotate_image
from task_4.resolution import block_average


image = cv2.imread("task_1/input.jpg")
# Task 1 
for level in [2, 4, 8, 16, 32, 64, 128, 256]:
    result = reduce_intensity_levels(image, level)
    cv2.imwrite(f"task_1/intensity_reduced_{level}.jpg", result)


# Task 2 
for k in [3, 10, 20]:
    blurred = average_filter(image, k)
    cv2.imwrite(f"task_2/blurred_{k}x{k}.jpg", blurred)

# Task 3 
for angle in [45, 90]:
    rotated = rotate_image(image, angle)
    cv2.imwrite(f"task_3/rotated_{angle}.jpg", rotated)

# Task 4 
for b in [3, 5, 7]:
    low_res = block_average(image, b)
    cv2.imwrite(f"task_4/lowres_{b}x{b}.jpg", low_res)
