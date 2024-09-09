import time
from stt.model.model import SttModel
from stt.sbt.vtt import to_vtt_string


def test_model():
    print()
    start = time.time()

    model_size = "base"
    # model_size = "small"
    # model_size = "medium"
    # model_size = "large-v2"
    # model_size = "large-v3"
    compute_type = "int8"
    term_time_ms = 500
    # term_time_ms = 700
    relocation = True
    # relocation = False
    per_char_ms = 50
    model = SttModel(
        model_size=model_size,
        compute_type=compute_type,
        term_time_ms=term_time_ms,
        per_char_ms=per_char_ms,
        relocation=relocation,
    )
    print(f"{time.time() - start:.4f} sec")

    start = time.time()
    # file_path = "../dev/src/test1.mp3"
    file_path = "../dev/src/test2.opus"
    result = model.transcribe(file_path)
    print(f"{time.time() - start:.4f} sec")

    vtt = to_vtt_string(result)
    print(vtt)
