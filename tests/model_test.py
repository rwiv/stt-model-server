import time
from stt.model.model import SttModel
from stt.sbt.vtt import from_segment, to_vtt_string


def test_model():
    print()
    start = time.time()

    model_name = "base"
    # model_name = "small"
    # model_name = "medium"
    # model_name = "large-v3"
    compute_type = "int8"
    model = SttModel(model_name, compute_type)
    print(f"{time.time() - start:.4f} sec")

    start = time.time()
    result = model.transcribe("../assets/test1.mp3")
    print(f"{time.time() - start:.4f} sec")

    vtt = to_vtt_string([from_segment(segment) for segment in result])
    print(vtt)
