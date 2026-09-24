import subprocess
import json
import os
from fractions import Fraction


def format_duration(seconds):
    """Convert seconds into HH:MM:SS format."""

    seconds = float(seconds)

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def format_bitrate(bits_per_second):
    """Convert bitrate into readable format."""

    if not bits_per_second:
        return "Not available"

    bits_per_second = float(bits_per_second)

    if bits_per_second >= 1_000_000:
        return f"{bits_per_second / 1_000_000:.2f} Mbps"

    return f"{bits_per_second / 1_000:.2f} kbps"


def format_frame_rate(frame_rate):
    """Convert fraction frame rate into FPS."""

    try:
        fps = float(Fraction(frame_rate))
        return f"{fps:.2f} FPS"
    except (ValueError, ZeroDivisionError):
        return "Not available"


def analyze_video(video_path):
    """Extract metadata from a video file."""

    if not os.path.exists(video_path):
        print("Error: File does not exist.")
        return

    try:
        command = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            video_path
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("Error: Unable to analyze the video.")
            return

        data = json.loads(result.stdout)

        print("================================")
        print("VIDEO METADATA REPORT")
        print("================================")

        print("File Name       :", os.path.basename(video_path))
        print("File Size       :", os.path.getsize(video_path), "bytes")

        format_data = data.get("format", {})

        container = format_data.get(
            "format_name",
            "Not available"
        )

        duration = format_data.get(
            "duration",
            None
        )

        print("Container       :", container)

        if duration:
            print("Duration        :", format_duration(duration))
        else:
            print("Duration        : Not available")

        # Find video and audio streams
        video_stream = None
        audio_stream = None

        for stream in data.get("streams", []):

            if stream.get("codec_type") == "video":
                video_stream = stream

            elif stream.get("codec_type") == "audio":
                audio_stream = stream

        # VIDEO
        print()
        print("VIDEO")
        print("--------------------------------")

        if video_stream:

            width = video_stream.get(
                "width",
                "Not available"
            )

            height = video_stream.get(
                "height",
                "Not available"
            )

            codec = video_stream.get(
                "codec_name",
                "Not available"
            )

            frame_rate = video_stream.get(
                "r_frame_rate",
                None
            )

            bit_rate = video_stream.get(
                "bit_rate",
                None
            )

            print("Resolution      :", f"{width}x{height}")

            if frame_rate:
                print(
                    "Frame Rate      :",
                    format_frame_rate(frame_rate)
                )
            else:
                print("Frame Rate      : Not available")

            print(
                "Bit Rate        :",
                format_bitrate(bit_rate)
            )

            print("Codec           :", codec)

        else:
            print("No video stream found.")

        # AUDIO
        print()
        print("AUDIO")
        print("--------------------------------")

        if audio_stream:

            audio_codec = audio_stream.get(
                "codec_name",
                "Not available"
            )

            channels = audio_stream.get(
                "channels",
                "Not available"
            )

            sample_rate = audio_stream.get(
                "sample_rate",
                "Not available"
            )

            audio_bit_rate = audio_stream.get(
                "bit_rate",
                None
            )

            print("Codec           :", audio_codec)
            print("Channels        :", channels)

            if sample_rate != "Not available":
                print(
                    "Sampling Rate   :",
                    sample_rate,
                    "Hz"
                )
            else:
                print("Sampling Rate   : Not available")

            print(
                "Bit Rate        :",
                format_bitrate(audio_bit_rate)
            )

        else:
            print("No audio stream found.")

        # METADATA
        print()
        print("METADATA")
        print("--------------------------------")

        tags = format_data.get("tags", {})

        if tags:
            for key, value in tags.items():
                print(f"{key:<20}: {value}")
        else:
            print("No metadata available.")

    except json.JSONDecodeError:
        print("Error: FFprobe returned invalid data.")

    except Exception as e:
        print("Error while analyzing video:", e)


# Program starts here
video_path = input("Enter video path: ")
analyze_video(video_path)
