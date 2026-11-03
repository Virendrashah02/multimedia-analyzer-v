from PIL import Image, ExifTags
import os


def analyze_image(image_path):
    """Extract metadata from an image file and return it as a dictionary."""

    if not os.path.exists(image_path):
        return {
            "error": "File does not exist."
        }

    try:
        image = Image.open(image_path)

        result = {
            "file_name": os.path.basename(image_path),
            "file_size": os.path.getsize(image_path),
            "file_format": image.format,
            "width": image.width,
            "height": image.height,
            "resolution": image.info.get("dpi", "Not available"),
            "color_mode": image.mode,
            "camera": "Not available",
            "date_taken": "Not available",
            "orientation": "Not available"
        }

        exif_data = image.getexif()

        if exif_data:
            camera_make = None
            camera_model = None

            for tag_id, value in exif_data.items():

                tag_name = ExifTags.TAGS.get(tag_id, tag_id)

                if tag_name == "Make":
                    camera_make = str(value)

                elif tag_name == "Model":
                    camera_model = str(value)

                elif tag_name == "DateTimeOriginal":
                    result["date_taken"] = str(value)

                elif tag_name == "Orientation":
                    result["orientation"] = str(value)

            if camera_make and camera_model:
                result["camera"] = f"{camera_make} {camera_model}"

            elif camera_make:
                result["camera"] = camera_make

            elif camera_model:
                result["camera"] = camera_model

        return result

    except Exception as e:
        return {
            "error": f"Error while analyzing image: {e}"
        }


def print_image_report(result):
    """Print image analysis result in a readable format."""

    if "error" in result:
        print(result["error"])
        return

    print("================================")
    print("IMAGE METADATA REPORT")
    print("================================")

    print("File Name       :", result["file_name"])
    print("File Size       :", result["file_size"], "bytes")
    print("File Format     :", result["file_format"])
    print("Width           :", result["width"])
    print("Height          :", result["height"])
    print("Resolution      :", result["resolution"])
    print("Color Mode      :", result["color_mode"])

    print()
    print("EXIF Metadata")
    print("-------------------------------")

    print("Camera          :", result["camera"])
    print("Date Taken      :", result["date_taken"])
    print("Orientation     :", result["orientation"])


# Run directly from terminal
if __name__ == "__main__":
    image_path = input("Enter image path: ")
    result = analyze_image(image_path)
    print_image_report(result)