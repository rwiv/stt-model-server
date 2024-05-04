import time
from stt.model.model import SttModel


def test_model():
    print()
    start = time.time()

    # model_name = "base"
    # model_name = "small"
    # model_name = "medium"
    model_name = "large-v3"
    model = SttModel(model_name)
    print(f"{time.time() - start:.4f} sec")

    start = time.time()
    result = model.transcribe("../assets/test1.mp3")
    print(f"{time.time() - start:.4f} sec")

    for segment in result:
        print(segment)
