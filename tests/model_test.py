from stt.model.model import transcribe


def test_model():
    # model_name = "base"
    model_name = "small"
    # model_name = "medium"
    result = transcribe(model_name, "../assets/test1.mp3")
    print()
    for elem in result:
        print(elem["text"])
