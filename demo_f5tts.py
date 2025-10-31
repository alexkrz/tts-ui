import scipy.io.wavfile as wavfile
from f5_tts.api import F5TTS

f5tts = F5TTS()

wav, sr, spec = f5tts.infer(
    ref_file="targets/Rogger.wav",
    ref_text="",  # Transcribe reference automatically
    gen_text="It took me quite a long time to develop a voice and now that I have it I am not going to be silent.",
)

# Write output
print("Writing output to file..")
wavfile.write("outputs/f5-tts.wav", rate=24000, data=wav)
