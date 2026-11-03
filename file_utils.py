import os


# Supported file extensions
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".tiff",
    ".tif",
    ".webp",
    ".bmp"
}

AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".m4a"
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".webm",
    ".flv"
}


def file_exists(file_path):
    """Check whether the file exists."""

    return os.path.isfile(file_path)


def get_file_size(file_path):
    """Return file size in bytes."""

    return os.path.getsize(file_path)


def get_file_extension(file_path):
    """Return file extension in lowercase."""

    return os.path.splitext(file_path)[1].lower()


def identify_file_type(file_path):
    """Identify whether a file is an image, audio, or video."""

    extension = get_file_extension(file_path)

    if extension in IMAGE_EXTENSIONS:
        return "IMAGE"

    elif extension in AUDIO_EXTENSIONS:
        return "AUDIO"

    elif extension in VIDEO_EXTENSIONS:
        return "VIDEO"

    return "UNKNOWN"
