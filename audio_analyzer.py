import subprocess
import json
import os


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


def analyze_audio(audio_path):
    """Extract metadata from an audio file."""

    if not os.path.exists(audio_path):
        print("Error: File does not exist.")
        return

    try:
        command = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            audio_path
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("Error: Unable to analyze the audio.")
            return

        data = json.loads(result.stdout)

        print("================================")
        print("AUDIO METADATA REPORT")
        print("================================")

        print(
            "File Name       :",
            os.path.basename(audio_path)
        )

        print(
            "File Size       :",
            os.path.getsize(audio_path),
            "bytes"
        )

        format_data = data.get("format", {})

        print(
            "Format          :",
            format_data.get(
                "format_name",
                "Not available"
            )
        )

        duration = format_data.get("duration")

        if duration:
            print(
                "Duration        :",
                format_duration(duration)
            )
        else:
            print("Duration        : Not available")

        # Find audio stream
        audio_stream = None

        for stream in data.get("streams", []):

            if stream.get("codec_type") == "audio":
                audio_stream = stream
                break

        print()
        print("AUDIO")
        print("--------------------------------")

        if audio_stream:

            codec = audio_stream.get(
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

            bit_rate = audio_stream.get(
                "bit_rate"
            )

            print("Codec           :", codec)
            print("Channels        :", channels)

            if sample_rate != "Not available":
                print(
                    "Sampling Rate   :",
                    sample_rate,
                    "Hz"
                )
            else:
                print(
                    "Sampling Rate   :",
                    "Not available"
                )

            print(
                "Bit Rate        :",
                format_bitrate(bit_rate)
            )

        else:
            print("No audio stream found.")

        # Metadata
        print()
        print("METADATA")
        print("--------------------------------")

        tags = {}

        # Format-level tags
        format_tags = format_data.get("tags", {})
        tags.update(format_tags)

        # Stream-level tags
        if audio_stream:
            stream_tags = audio_stream.get("tags", {})
            tags.update(stream_tags)

        if tags:
            for key, value in tags.items():
                print(f"{key:<24}: {value}")
        else:
            print("No metadata available.")

    except json.JSONDecodeError:
        print("Error: FFprobe returned invalid data.")

    except Exception as e:
        print("Error while analyzing audio:", e)


# Program starts here
audio_path = input("Enter audio path: ")
analyze_audio(audio_path)