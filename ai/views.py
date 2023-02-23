from pathlib import Path

from ai.utils.pyannote_utils import *
from ai.utils.whisper_utils import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import wave


@permission_classes((permissions.AllowAny,))
class AudioDiarizationView(APIView):
    # renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    # template_name = 'index.html'

    def get(self, request):
        audio = Path("./samples/meeting_audio/FTC_Sample_1.wav")

        print(100 * "*")
        print(audio)
        # sample_rate = 16000

        data = {
            # "Speaker Segmentation": ai_speaker_segmentation(audio),
            "Speaker Diarization": ai_speaker_diarization(audio),
        }
        return Response(data, status=200)


@permission_classes((permissions.AllowAny,))
class AudioTranscriptView(APIView):
    def get(self, request):
        audio_mp3 = Path("./samples/meeting_audio/FTC_Sample_1.mp3")

        print(100 * "#")
        print(audio_mp3)
        # sample_rate = 16000
        language, transcript = get_transcript(audio_mp3)

        data = {
            "Audio Transcript": transcript,
            "Audio Language": language,
        }
        print(data)
        return Response(data, status=200)


@permission_classes((permissions.AllowAny,))
class SpeechToTextView(APIView):
    def get(self, request):
        audio = Path("./samples/meeting_audio/FTC_Sample_1.wav")
        speakers = ai_speaker_diarization(audio)
        full_transcript = {}
        for speaker in speakers:
            transcript = {
                "speaker": speakers[speaker]["speaker"],
                "start": speakers[speaker]["start"],
                "stop": speakers[speaker]["stop"],
                "talktime": speaker["stop"] - speaker["start"],
                "transcribed_text": get_transcript(audio)[1],
                "language": get_transcript(audio)[0],
            }

        print(100 * "*")
        print(audio)
        # sample_rate = 16000

        data = {
            # "Speaker Segmentation": ai_speaker_segmentation(audio),
            "Speaker Diarization": ai_speaker_diarization(audio),
        }
        return Response(data, status=200)
