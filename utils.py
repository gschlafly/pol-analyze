import os
import matplotlib.pyplot as plt
import tifffile


def load_images(directory):
    """Load and sort TIFF images from a specified directory."""
    image_names = os.listdir(directory)
    image_names.sort()
    images = [tifffile.imread(os.path.join(directory, name)) for name in image_names]
    return images


def display_image(image, title):
    """Display an image with a given title."""
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()


def display_image_with_mla_grid(image_array, pix_per_lenslet, title='Image with MLA Grid'):
    plt.imshow(image_array, cmap='gray')
    height, width = image_array.shape
    for i in range(0, height, pix_per_lenslet):
        plt.hlines(i, xmin=0, xmax=width, colors='red', linestyles='dashed', linewidths=0.5)
    for j in range(0, width, pix_per_lenslet):
        plt.vlines(j, ymin=0, ymax=height, colors='red', linestyles='dashed', linewidths=0.5)
    plt.title(title)
    plt.axis('off')
    plt.show()


def save_image(filename, image):
    """Save an image to a TIFF file."""
    tifffile.imwrite(filename, image)
    print(f"Image saved as {filename}")

