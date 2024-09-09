import os
from dataclasses import dataclass, asdict

default_env = "dev"
default_model_type = "base"
default_compute_type = "int8"
default_term_time_ms = "1000"
default_relocation = "true"
default_port = "8080"
default_host = "0.0.0.0"


@dataclass
class Env:
    py_env: str
    model_type: str
    compute_type: str
    term_time_ms: int
    relocation: bool
    port: int
    host: str
    src_path: str
    dst_path: str

    def to_dict(self):
        return asdict(self)


def get_env() -> Env:
    py_env = os.getenv("PY_ENV") or default_env

    model_type = os.getenv("MODEL_SIZE", default_model_type)
    compute_type = os.getenv("MODEL_COMPUTE_TYPE", default_compute_type)
    term_time_ms = int(os.getenv("SEG_TERM_TIME_MS", default_term_time_ms))
    relocation = os.getenv("SEG_RELOCATION", default_relocation).lower() == "true"

    port = int(os.getenv("APP_PORT", default_port))
    host = os.getenv("APP_HOST", default_host)
    src_path = os.getenv("APP_SRC_PATH")
    if not src_path:
        raise ValueError("APP_SRC_PATH is required")
    dst_path = os.getenv("APP_DST_PATH")
    if not dst_path:
        raise ValueError("APP_DST_PATH is required")

    return Env(
        py_env=py_env,
        model_type=model_type,
        compute_type=compute_type,
        term_time_ms=term_time_ms,
        relocation=relocation,
        port=port,
        host=host,
        src_path=src_path,
        dst_path=dst_path,
    )
