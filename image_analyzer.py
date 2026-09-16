from PIL import Image, ExifTags
import os


def analyze_image(image_path):
    """Extract metadata from an image file."""

    if not os.path.exists(image_path):
        print("Error: File does not exist.")
        return

    try:
        image = Image.open(image_path)

        print("================================")
        print("IMAGE METADATA REPORT")
        print("================================")

        print("File Name       :", os.path.basename(image_path))
        print("File Size       :", os.path.getsize(image_path), "bytes")
        print("File Format     :", image.format)
        print("Width           :", image.width)
        print("Height          :", image.height)
        print("Resolution      :", image.info.get("dpi", "Not available"))
        print("Color Mode      :", image.mode)

        print()
        print("EXIF Metadata")
        print("-------------------------------")

        exif_data = image.getexif()

        camera = "Not available"
        date_taken = "Not available"
        orientation = "Not available"

        if exif_data:
            for tag_id, value in exif_data.items():

                tag_name = ExifTags.TAGS.get(tag_id, tag_id)

                if tag_name == "Make":
                    camera = str(value)

                elif tag_name == "Model":
                    if camera == "Not available":
                        camera = str(value)
                    else:
                        camera += " " + str(value)

                elif tag_name == "DateTimeOriginal":
                    date_taken = str(value)

                elif tag_name == "Orientation":
                    orientation = str(value)

        print("Camera          :", camera)
        print("Date Taken      :", date_taken)
        print("Orientation     :", orientation)

    except Exception as e:
        print("Error while reading image:", e)


# Program starts here
image_path = input("Enter image path: ")
analyze_image(image_path)