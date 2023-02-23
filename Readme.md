# Transcribe real-world speech with an API call.
`meetlyai.audio` is an open-source toolkit written in Python for speaker diarization. Based on [PyTorch](pytorch.org) machine learning framework, it provides a set of trainable end-to-end neural building blocks that can be combined and jointly optimized to build speaker diarization pipelines.


What inspired me to build this [ Transcription and diarization (speaker identification) ](https://github.com/openai/whisper/discussions/264)

Main page: [ai.meetly.so](https://ai.meetly.so)

Demo page: [ai.meetly.so/playground](https://ai.meetly.so/playground)

## Current Capabilities
- [x] Generate transcript for speaker speeches using OpenAI Whisper
- [x] List speakers from an audio source

## Todos
- [ ] Split audio for speaker diarization using pyannote.audio
- [ ] Generate transcript for speaker speeches using OpenAI Whisper
- [ ] API endpoint to upload audio and get speaker-wise split audio files
- [ ] API to upload speech audio and get transcript as output
- [ ] API to upload full speech with multiple speakers and get speaker wise transcript
- [ ] API to summarise transcript using OpenAI
- [ ] Implement a demo page for anyone to test
- [ ] Implement realtime transcription using WebRTC

## Tools Used
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) for speaker diarization
- [OpenAI Whisper](https://github.com/openai/whisper) for Speech to Text transcription
- `TBD` for transcript to summary. Maybe [Learning to Summarize from Human Feedback](https://github.com/openai/summarize-from-feedback)


## Installation
### Pyannote.audio
```bash

Only Python 3.8+ is officially supported (though it might work with Python 3.7)

```bash
conda create -n pyannote python=3.8
conda activate pyannote

# pytorch 1.11 is required for speechbrain compatibility
# (see https://pytorch.org/get-started/previous-versions/#v1110)
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 -c pytorch

pip install pyannote.audio
```
### Whisper (by OpenAI)
Whisper also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

For more information on Whisper please see https://github.com/openai/whisper

## Recognitions

This repository would not be possible without [pyannote.audio](https://github.com/pyannote/pyannote-audio), [OpenAI Whisper](https://github.com/openai/whisper)
Some other notable repository that I referenced to build this - [Whisper Real Time](https://github.com/davabase/whisper_real_time)

The code in this repository is public domain.