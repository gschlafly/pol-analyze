import numpy as np
import os
import tifffile
import matplotlib.pyplot as plt

intensity_dir = "dataset/original/bg_intensity"
image_names = os.listdir(intensity_dir)
image_names.sort()
intensity_images = []
for image_name in image_names:
    image = tifffile.imread(os.path.join(intensity_dir, image_name))
    intensity_images.append(image)

# Take the sum of the intensity images
intensity_sum = np.zeros_like(intensity_images[0])
for image in intensity_images:
    intensity_sum += image
    # plt.imshow(intensity_sum / np.max(intensity_sum), cmap='gray')
    # plt.title(f'Averge Intensity Image (so far)')
    # plt.axis('off')
    # plt.show(block=True)

# Normalize the intensity sum
intensity_avg = intensity_sum / np.max(intensity_sum)

plt.imshow(intensity_avg, cmap='gray')
plt.title(f'Averge Intensity Image')
plt.axis('off')
plt.show(block=True)

intensity_avg_filename = "dataset/bg_intensity_avg.tif"
tifffile.imwrite(intensity_avg_filename, intensity_avg)

threshold_value = 0.32
intensity_avg_thresholded = np.zeros_like(intensity_sum)
intensity_avg_thresholded[intensity_avg > threshold_value] = 1
plt.imshow(intensity_avg_thresholded, cmap='gray')
plt.title(f'Averge Intensity Image Thresholded')
plt.axis('off')
plt.show(block=True)

intensity_avg_ths_filename = "dataset/bg_intensity_avg_ths.tif"
tifffile.imwrite(intensity_avg_ths_filename, intensity_avg_thresholded)
