from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

tts.tts_to_file(
    text="Namaste, yeh meri cloned awaaz hai.",
    speaker_wav="my_voice.wav",
    language="hi",          # "en" for English
    file_path="output.wav"
)
print("Done: output.wav")