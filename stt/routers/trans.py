import time

from stt.env.env import get_env
from stt.model.model import SttModel, Sentence
from fastapi import APIRouter, UploadFile

from stt.utils.logger import log

router = APIRouter(prefix="/api/trans")

env = get_env()
model = SttModel(env.model_type, env.compute_type, env.term_time_ms, env.relocation)


@router.post("/")
def transcribe(file: UploadFile) -> list[Sentence]:
    start = time.time()
    result = model.transcribe(file.file)
    log.info(f"Time taken: {time.time() - start:.4f} sec")

    return result
