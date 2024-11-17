from PIL import Image

# Open the original image
img = Image.open(r"C:\Users\OKH20\OneDrive - University of Canterbury\Projects\CARWHO.github.io\images\favicon.png")

# Resize the image to 32x32 using LANCZOS for high-quality downsampling
img = img.resize((32, 32), Image.LANCZOS)

# Convert to RGB mode to save as JPEG (JPEG does not support transparency)
img_rgb = img.convert("RGB")

# Save the resized image as a .jpg
img_rgb.save(r"C:\Users\OKH20\OneDrive - University of Canterbury\Projects\CARWHO.github.io\images\favicon.jpg", "JPEG")

# Save the resized image as an .ico (ICO supports transparency, so no need to convert)
img.save(r"C:\Users\OKH20\OneDrive - University of Canterbury\Projects\CARWHO.github.io\images\favicon.ico", "ICO")
