import os
from dataclasses import dataclass

default_env = "dev"
default_port = 8080
default_host = "0.0.0.0"
# default_model_type = "large-v3"
default_model_type = "base"
default_compute_type = "int8"


@dataclass
class Env:
    py_env: str
    port: int
    host: str
    model_type: str
    compute_type: str
    src_path: str
    dst_path: str


def get_env() -> Env:
    py_env = os.getenv("PY_ENV") or default_env
    port = int(os.getenv("APP_PORT") or default_port)
    host = os.getenv("APP_HOST") or default_host
    model_type = os.getenv("APP_MODEL_TYPE") or default_model_type
    compute_type = os.getenv("APP_COMPUTE_TYPE") or default_compute_type
    src_path = os.getenv("APP_SRC_PATH")
    if not src_path:
        raise ValueError("APP_SRC_PATH is required")
    dst_path = os.getenv("APP_DST_PATH")
    if not dst_path:
        raise ValueError("APP_DST_PATH is required")

    return Env(
        py_env=py_env,
        port=port,
        host=host,
        model_type=model_type,
        compute_type=compute_type,
        src_path=src_path,
        dst_path=dst_path,
    )
