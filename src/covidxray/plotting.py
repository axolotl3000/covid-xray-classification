import matplotlib.pyplot as plt
import cv2

def plot_image(img, save_path=None, title=None):
    """
    Plots an image using matplotlib.

    Parameters:
    img (numpy.ndarray): The image to be plotted.
    save_path (str, optional): Path to save the plotted image. If None, the image will not be saved.
    title (str, optional): Title for the plot.
    Returns:
    fig, ax: The matplotlib figure and axes objects.
    """
    fig, ax = plt.subplots(1, figsize=(7, 7), layout="constrained")
    ax.imshow(img, cmap='gray')
    ax.axis('off')  # Hide axes

    if title:
        ax.set_title(title)

    if save_path:
        fig.savefig(save_path)
        print(f"Image saved to {save_path}")
    
    return fig, ax


def read_image(image_path):
    """
    Reads an image from the specified path using OpenCV.

    Parameters:
    image_path (str): Path to the image file.

    Returns:
    numpy.ndarray: The read image.
    """

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return img