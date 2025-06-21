import numpy as np
def block_average(image, block_size):
    h, w = image.shape[:2]
    new_img = np.zeros_like(image)
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = image[y:y+block_size, x:x+block_size]
            mean_val = block.mean(axis=(0, 1), dtype=int)
            new_img[y:y+block_size, x:x+block_size] = mean_val
    return new_img
