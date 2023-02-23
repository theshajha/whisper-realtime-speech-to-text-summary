from pyannote.audio import Model, Pipeline
from pyannote.audio.pipelines import VoiceActivityDetection, OverlappedSpeechDetection, Resegmentation
import json

# Model.from_pretrained("pyannote/segmentation",
#                       use_auth_token="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")
HYPER_PARAMETERS = {
    # onset/offset activation thresholds
    "onset": 0.5, "offset": 0.5,
    # remove speech regions shorter than that many seconds.
    "min_duration_on": 0.0,
    # fill non-speech regions shorter than that many seconds.
    "min_duration_off": 0.0
}


def ai_speaker_diarization(audio):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                        use_auth_token="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")
    # output = pipeline(audio, min_speakers=2, max_speakers=5)
    output = pipeline(audio)
    speakers = {}
    for turn, _, speaker in output.itertracks(yield_label=True):
        # speaker speaks between turn.start and turn.end
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
        speakers[speaker] = {"start": turn.start, "stop": turn.end}

    # dump the diarization output to disk using RTTM format
    with open("./output/audio.rttm", "w") as rttm:
        output.write_rttm(rttm)
    return speakers


def ai_speaker_segmentation(audio, starts, stops):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-segmentation",
                                        use_auth_token="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")
    output = pipeline(audio)
    speakers = {}
    for turn, _, speaker in output.itertracks(yield_label=True):
        # speaker speaks between turn.start and turn.end
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
        speakers[speaker] = {"start": turn.start, "stop": turn.end}
    return speakers


# 4. apply pretrained pipeline
def voice_activity_detection(self, audio, sample_rate):
    pipeline = VoiceActivityDetection(segmentation=model)

    pipeline.instantiate(HYPER_PARAMETERS)
    vad = pipeline("audio.wav")
    # `vad` is a pyannote.core.Annotation instance containing speech regions
    # vad = VoiceActivityDetection(model=model)
    # vad(audio, sample_rate=sample_rate)


def overlapped_speech_detection(self, audio, sample_rate):
    pipeline = OverlappedSpeechDetection(segmentation=model)
    pipeline.instantiate(HYPER_PARAMETERS)
    osd = pipeline("audio.wav")


def speech_resegmentation(self, audio, sample_rate):
    pipeline = Resegmentation(segmentation=model,
                              diarization="baseline")
    pipeline.instantiate(HYPER_PARAMETERS)
    resegmented_baseline = pipeline({"audio": "audio.wav", "baseline": baseline})
    # where `baseline` should be provided as a pyannote.core.Annotation instance
