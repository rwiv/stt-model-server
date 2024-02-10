import whisper
import json
import math


def run1(model_name: str, file_path: str, result_path: str):
    model = whisper.load_model(model_name)
    result = model.transcribe(file_path)

    pretty = json.dumps(result, indent=2)
    with open(result_path, "wb") as file:
        file.write(pretty.encode("utf-8"))


def conv_ms(sec):
    return math.floor(sec * 1000)


def conv(seg):
    return {
        "id": seg["id"],
        "start": conv_ms(seg["start"]),
        "end": conv_ms(seg["end"]),
        "text": seg["text"],
    }


def run2(src_path: str, result_path: str):
    with open(src_path, "r") as file:
        json_str = file.read()

    obj = json.loads(json_str)
    result = [conv(seg) for seg in obj["segments"]]

    pretty = json.dumps(result, indent=2)
    with open(result_path, "wb") as file:
        file.write(pretty.encode("utf-8"))


if __name__ == "__main__":
    # run1("base", "outt.mp4", "result.json")
    run2("result.json", "result2.json")
