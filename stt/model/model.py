from faster_whisper import WhisperModel
import math

from faster_whisper.transcribe import Segment


def create_model(model_name: str):
    device = "cuda"
    # compute_type = "float16"  # change to "int8" if low on GPU mem (may reduce accuracy)
    compute_type = "int8"
    return WhisperModel(model_name, device=device, compute_type=compute_type)


def transcribe(model: WhisperModel, file_path: str):
    segments, info = model.transcribe(file_path, beam_size=5)
    # print(info)
    return [conv(seg) for seg in segments]


def conv(segment: Segment):
    return {
        "id": segment.id,
        "start": math.floor(segment.start * 1000),
        "end": math.floor(segment.end * 1000),
        "text": segment.text,
    }
