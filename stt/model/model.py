import math
from typing import BinaryIO, TypedDict
from faster_whisper import WhisperModel
from faster_whisper.transcribe import Segment as WhisperSegment
from numpy import ndarray


class Segment(TypedDict):
    id: int
    start: float
    end: float
    text: str


class SttModel:
    def __init__(self, model_name: str):
        device = "cuda"
        # compute_type = "float16"  # change to "int8" if low on GPU mem (may reduce accuracy)
        compute_type = "int8"
        self.model = WhisperModel(model_name, device=device, compute_type=compute_type)
        print("whisper model load complete")

    def transcribe(self, file: str | BinaryIO | ndarray) -> list[Segment]:
        segments, info = self.model.transcribe(file, beam_size=5)
        # print(info)
        return [conv(seg) for seg in segments]


def conv(segment: WhisperSegment) -> Segment:
    return {
        "id": segment.id,
        "start": math.floor(segment.start * 1000),
        "end": math.floor(segment.end * 1000),
        "text": segment.text,
    }
