import json


def read_json(path: str):
    with open(path, "r") as file:
        json_str = file.read()
    return json_str


def to_pretty_json(json_str: str, result_path: str):
    pretty = json.dumps(json_str, indent=2)
    with open(result_path, "wb") as file:
        file.write(pretty.encode("utf-8"))
