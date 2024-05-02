import whisper
import json
import math


def run(model_name: str, file_path: str):
    model = whisper.load_model(model_name)
    result = model.transcribe(file_path)
    result2 = [conv(seg) for seg in result["segments"]]

    return result2


def conv(seg):
    return {
        "id": seg["id"],
        "start": math.floor(seg["start"] * 1000),
        "end": math.floor(seg["end"] * 1000),
        "text": seg["text"],
    }


def read_json(path: str):
    with open(path, "r") as file:
        json_str = file.read()
    return json_str


def to_pretty_json(json_str: str, result_path: str):
    pretty = json.dumps(json_str, indent=2)
    with open(result_path, "wb") as file:
        file.write(pretty.encode("utf-8"))


if __name__ == "__main__":
    model_name = "base"
    # model_name = "medium"
    result = run(model_name, "test1.mp3")
    for elem in result:
        print(elem)

