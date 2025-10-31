import scipy.io.wavfile as wavfile
import torch
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"


def tts_with_model():
    # Initialize TTS
    print("Initializing model..")
    config = XttsConfig()
    config.load_json("checkpoints/XTTS-main/config.json")
    model = Xtts.init_from_config(config)
    model.load_checkpoint(config, checkpoint_dir="checkpoints/XTTS-main", eval=True)
    model.to(device)

    # Run inference
    print("Running inference..")
    outputs = model.synthesize(
        "It took me quite a long time to develop a voice and now that I have it I am not going to be silent.",
        config,
        speaker_wav="targets/Rogger.wav",
        gpt_cond_len=3,
        language="en",
    )

    # Write output
    print("Writing output to file..")
    wav = outputs["wav"]
    wavfile.write("outputs/xtts-model.wav", rate=24000, data=wav)


def tts_with_api():
    # Initialize TTS
    print("Initializing model..")
    tts = TTS(model_path="checkpoints/XTTS-main", config_path="checkpoints/XTTS-main/config.json")
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
    tts.tts_to_file(text="Hello world", speaker="Craig Gutsy", language="en", file_path="outputs/xtts-api.wav")


if __name__ == "__main__":
    # tts_with_api()
    tts_with_model()
