import matplotlib.pyplot as plt


def plot_red_x_on_image(image, indices):
    """
    Plot an image and mark a red 'X' on specified indices.

    Parameters:
        image (np.array): The image array.
        indices (list of tuples): List of (row, column) indices to mark with an 'X'.
    """
    plt.imshow(image, cmap='gray')  # Display the image in grayscale
    for (row, col) in indices:
        # Draw a red 'X' at the specified index
        # Define the size of the 'X'
        offset = 5  # Size of the 'X'
        # Draw the 'X'
        plt.plot([col - offset, col + offset], [row - offset, row + offset], color='red', marker='x', markersize=10)
        plt.plot([col - offset, col + offset], [row + offset, row - offset], color='red', marker='x', markersize=10)

    plt.axis('off')  # Turn off axis labels
    plt.show()


def display_image_with_mla_grid_and_x_marks(image_array, pix_per_lenslet, marked_combinations, title='Image with MLA Grid and X Marks'):
    """
    Display an image with an MLA grid and place a red 'X' over specified regions.
    
    Parameters:
        image_array (numpy.array): The image array.
        pix_per_lenslet (int): The number of pixels per lenslet square.
        marked_combinations (list of tuples): List of (i, j) tuples specifying which regions to mark with an 'X'.
        title (str): Title for the plot.
    """
    plt.imshow(image_array, cmap='gray')
    height, width = image_array.shape
    
    # Draw the grid
    for i in range(0, height, pix_per_lenslet):
        plt.hlines(i, xmin=0, xmax=width, colors='red', linestyles='dashed', linewidths=0.5)
    for j in range(0, width, pix_per_lenslet):
        plt.vlines(j, ymin=0, ymax=height, colors='red', linestyles='dashed', linewidths=0.5)
    
    # Draw a red 'X' on specified grid regions
    for i, j in marked_combinations:
        start_x = j * pix_per_lenslet
        start_y = i * pix_per_lenslet
        end_x = start_x + pix_per_lenslet
        end_y = start_y + pix_per_lenslet
        
        # Draw lines from corner to corner
        plt.plot([start_x, end_x], [start_y, end_y], color='red', linewidth=2)  # From top-left to bottom-right
        plt.plot([start_x, end_x], [end_y, start_y], color='red', linewidth=2)  # From bottom-left to top-right

    plt.title(title)
    plt.axis('off')
    plt.show()
