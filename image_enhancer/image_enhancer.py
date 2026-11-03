from PIL import Image, ImageEnhance
import os


def enhance_image(input_path, output_path):
    # Check if file exists
    if not os.path.exists(input_path):
        print("Error: Image file not found.")
        return

    try:
        # Open image
        image = Image.open(input_path)

        print("Original Image")
        print("----------------------------")
        print("File Name :", os.path.basename(input_path))
        print("Size      :", image.size)
        print("Format    :", image.format)
        print()

        # Brightness enhancement
        brightness = ImageEnhance.Brightness(image)
        image = brightness.enhance(1.1)

        # Contrast enhancement
        contrast = ImageEnhance.Contrast(image)
        image = contrast.enhance(1.2)

        # Color enhancement
        color = ImageEnhance.Color(image)
        image = color.enhance(1.1)

        # Sharpness enhancement
        sharpness = ImageEnhance.Sharpness(image)
        image = sharpness.enhance(1.5)

        # Save enhanced image
        image.save(output_path)

        print("Image enhanced successfully!")
        print("Output file:", output_path)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    input_path = input("Enter image path: ")
    output_path = input("Enter output image path: ")

    enhance_image(input_path, output_path)