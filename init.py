from stt.env.env import get_env
from stt.model.model import SttModel


if __name__ == "__main__":
    env = get_env()
    SttModel(env.model_type, env.compute_type)

