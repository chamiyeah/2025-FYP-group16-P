import matplotlib.pyplot as plt

def plot_before_after(all_images, save_path):
    """Creates a side-by-side comparison of the first 5 images."""

    num_images = min(len(all_images), 5)  # Limit to 5 images
    fig, axes = plt.subplots(num_images, 3, figsize=(12, num_images * 3))  # 3 columns (Original | Enhanced | Hair Removed)

    for idx, (original, enhanced, no_hair, filename) in enumerate(all_images[:5]):
        # Left column: Original Image
        axes[idx, 0].imshow(original)
        axes[idx, 0].set_title(f"Original: {filename}")
        axes[idx, 0].axis("off")

        # Middle column: Enhanced Image
        axes[idx, 1].imshow(enhanced, cmap="gray")
        axes[idx, 1].set_title(f"Enhanced: {filename}")
        axes[idx, 1].axis("off")

        # Right column: Hair Removed Image
        axes[idx, 2].imshow(no_hair)
        axes[idx, 2].set_title(f"Hair Removed: {filename}")
        axes[idx, 2].axis("off")

    plt.savefig(save_path)
    plt.close(fig)