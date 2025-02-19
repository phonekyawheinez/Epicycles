import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # For loading images

# Load the image
image_path = "./images/fouriertest.jpeg"  # Replace with your image path
image = Image.open(image_path).convert("L")  # Convert to grayscale
image_array = np.array(image)  # Convert to numpy array

# Compute the 2D Fourier Transform
fft_image = np.fft.fft2(image_array)  # Compute FFT
fft_shifted = np.fft.fftshift(fft_image)  # Shift zero frequency to center

# Calculate magnitude and phase
magnitude = np.abs(fft_shifted)  # Magnitude (radius)
phase = np.angle(fft_shifted)  # Phase (angle in radians)

# Plot the original image, magnitude, and phase
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image_array, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Magnitude Spectrum (log scale for better visualization)
plt.subplot(1, 3, 2)
plt.imshow(np.log1p(magnitude), cmap="gray")  # log1p to enhance visibility
plt.title("Magnitude Spectrum")
plt.axis("off")

# Phase Spectrum
plt.subplot(1, 3, 3)
plt.imshow(phase, cmap="gray")
plt.title("Phase Spectrum")
plt.axis("off")

plt.tight_layout()
plt.show()

# Output the magnitude and phase values
print("Magnitude (Radius):")
print(magnitude)

print("\nPhase (Angle in radians):")
print(phase)