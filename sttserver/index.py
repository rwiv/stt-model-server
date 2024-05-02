import whisper
import math


def run(model_name: str, file_path: str):
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


if __name__ == "__main__":
    model_name = "base"
    # model_name = "medium"
    result = run(model_name, "../assets/test1.mp3")
    for elem in result:
        print(elem)
