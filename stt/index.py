from stt.model.model import transcribe, create_model
import time

if __name__ == "__main__":
    # model_name = "base"
    # model_name = "small"
    # model_name = "medium"
    model_name = "large-v3"
    model = create_model(model_name)

    start = time.time()
    result = transcribe(model, "../assets/test1.mp3")
    print(f"{time.time() - start:.4f} sec")

    for segment in result:
        print(segment)
