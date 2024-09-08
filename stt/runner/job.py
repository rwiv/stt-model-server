import os.path

from stt.env.env import get_env
from stt.model.model import SttModel
from stt.sbt.vtt import to_vtt_string


def run():
    env = get_env()
    model = SttModel(env.model_type, env.compute_type)
    print("Model loaded")

    os.makedirs(env.dst_path, exist_ok=True)
    for filename in os.listdir(env.src_path):
        audio_path = os.path.join(env.src_path, filename)
        out_path = os.path.join(env.dst_path, f"{os.path.splitext(filename)[0]}.vtt")

        segments = model.transcribe(audio_path)
        vtt = to_vtt_string(segments)

        with open(out_path, "w") as f:
            f.write(vtt)
        print(f"Generated {out_path}")
