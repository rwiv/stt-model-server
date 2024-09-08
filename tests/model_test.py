import time
from stt.model.model import SttModel
from stt.sbt.vtt import to_vtt_string


def test_model():
    print()
    start = time.time()

    # model_name = "base"
    # model_name = "small"
    # model_name = "medium"
    # model_name = "large-v2"
    model_name = "large-v3"
    compute_type = "int8"
    model = SttModel(model_name, compute_type)
    print(f"{time.time() - start:.4f} sec")

    start = time.time()
    is_split = True
    # is_split = False
    result = model.transcribe("../dev/src/test2.opus", is_split)
    print(f"{time.time() - start:.4f} sec")

    vtt = to_vtt_string(result)
    print(vtt)
