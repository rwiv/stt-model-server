import time
from stt.model.model import SttModel, Segment
from fastapi import APIRouter, UploadFile

router = APIRouter(prefix="/api/trans")

model_name = "large-v3"
model = SttModel(model_name)


@router.post("/")
def transcribe(file: UploadFile) -> list[Segment]:
    start = time.time()
    result = model.transcribe(file.file)
    print(f"{time.time() - start:.4f} sec")

    return result
