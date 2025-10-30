import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize TTS
print("Initializing model..")
tts = TTS(model_path="checkpoints/XTTS-v2", config_path="checkpoints/XTTS-v2/config.json")
tts.to(device)

# List speakers
print("Number of available speakers:", len(tts.speakers))
print(tts.speakers)

# Run TTS
# ❗ XTTS supports both, but many models allow only one of the `speaker` and
# `speaker_wav` arguments

# TTS with list of amplitude values as output, clone the voice from `speaker_wav`
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")

# TTS to a file, use a preset speaker
print("Saving TTS to file..")
tts.tts_to_file(text="Hello world", speaker="Craig Gutsy", language="en", file_path="outputs/output.wav")
