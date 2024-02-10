import whisper
import json
import math


def run1():
    model = whisper.load_model("base")
    result = model.transcribe("outt.mp4")

    pretty = json.dumps(result, indent=2)
    with open("result.json", "wb") as file:
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


def run2():
    with open("result.json", "r") as file:
        json_str = file.read()

    obj = json.loads(json_str)
    result = [conv(seg) for seg in obj["segments"]]

    pretty = json.dumps(result, indent=2)
    with open("result2.json", "wb") as file:
        file.write(pretty.encode("utf-8"))


if __name__ == "__main__":
    # run1()
    run2()
