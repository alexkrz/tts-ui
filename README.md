# TTS-UI

A WebUI for Text-to-Speech generation.

The WebUI is build on top of the [coqui-tts](https://github.com/idiap/coqui-ai-TTS) Python package.

## Setup

We recommend [miniforge](https://conda-forge.org/download/) to set up your python environment.
In case VSCode does not detect your conda environments, install [nb_conda](https://github.com/conda-forge/nb_conda-feedstock) in the base environment.

```bash
conda env create -n $YOUR_ENV_NAME -f environment.yml
conda activate $YOUR_ENV_NAME
pip install -r requirements.txt
pre-commit install
```

Clone the [XTTS-v2 checkpoint](https://huggingface.co/coqui/XTTS-v2) (main) from Huggingface to the local `checkpoints/` directory:

```bash
cd checkpoints
hf download coqui/XTTS-v2 --local-dir=XTTS-v2
```
