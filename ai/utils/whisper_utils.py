import json

import whisper


def get_diarization(audio_path, model_name="pyannote/speaker-diarization", use_auth_token=None):
    pipeline = whisper.Pipeline.from_pretrained(model_name, use_auth_token=use_auth_token)
    diarization = pipeline(audio_path)
    return diarization


def get_transcript(audio_mp3):
    model = whisper.load_model("base")
    # model = whisper.load_model("large")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_mp3)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    # options = whisper.DecodingOptions()
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    res = json.dumps(result.text)
    res_json = json.loads(res)

    data = {
        "Audio Transcript": res_json,
        "Detected Language": max(probs, key=probs.get),
    }
    print(data)
    return max(probs, key=probs.get), res_json
