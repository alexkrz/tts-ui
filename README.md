# TTS-UI

A WebUI for Text-to-Speech generation.

## Setup

We recommend [miniforge](https://conda-forge.org/download/) to set up your python environment. \
Set up a new conda environment with the following commands:

```bash
conda env create -n $YOUR_ENV_NAME -f environment.yml
conda activate $YOUR_ENV_NAME
pip install -r requirements.txt
pre-commit install
```

## Included Models

- XTTS from [coqui-tts](https://github.com/idiap/coqui-ai-TTS)

    Download the [XTTS-v2 checkpoint](https://huggingface.co/coqui/XTTS-v2) (main) from Huggingface to the local `checkpoints/` directory:

    ```bash
    cd checkpoints
    hf download coqui/XTTS-v2 --local-dir=XTTS-main
    ```

- F5-TTS from [f5-tts](https://github.com/SWivid/F5-TTS)

    The model checkpoints are available on Huggingface: <https://huggingface.co/SWivid/F5-TTS>.
    The corresponding model checkpoint will be downloaded automatically when running `demo_f5tts.py`.

## WebUI

Run the WebUI by launching `app.py`:

```bash
python app.py
```

The WebUI is adopted from <https://github.com/BoltzmannEntropy/xtts2-ui>.

## License

Currently, there are unresolved issues concerning the licensing of XTTS, after the developing company Coqui AI has shut down.
A corresponding thread can be found here: <https://github.com/coqui-ai/TTS/issues/3490#issuecomment-1878926431>
