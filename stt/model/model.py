import whisper
import math


def transcribe(model_name: str, file_path: str):
    model = whisper.load_model(model_name)
    result = model.transcribe(file_path)

    # print(result["language"])
    return [conv(seg) for seg in result["segments"]]


def conv(seg):
    return {
        "id": seg["id"],
        "start": math.floor(seg["start"] * 1000),
        "end": math.floor(seg["end"] * 1000),
        "text": seg["text"],
    }
