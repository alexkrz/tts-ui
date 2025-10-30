# TTS-UI

A WebUI for Text-to-Speech generation.

The WebUI is build on top of the [coqui-tts](https://github.com/idiap/coqui-ai-TTS) Python package.

## Setup

We recommend [miniforge](https://conda-forge.org/download/) to set up your python environment. \
Set up a new conda environment with the following commands:

```bash
conda env create -n $YOUR_ENV_NAME -f environment.yml
conda activate $YOUR_ENV_NAME
pip install -r requirements.txt
pre-commit install
```

Clone the [XTTS-v2 checkpoint](https://huggingface.co/coqui/XTTS-v2) (main) from Huggingface to the local `checkpoints/` directory:

```bash
cd checkpoints
hf download coqui/XTTS-v2 --local-dir=XTTS-main
```

## WebUI

Run the WebUI by launching `app.py`:

```bash
python app.py
```
