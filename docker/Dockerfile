FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu22.04

WORKDIR /usr/src/app
COPY . .

RUN apt-get update
RUN apt-get install python3 python3-venv -y

RUN python3 -m venv .venv
RUN .venv/bin/pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121
RUN .venv/bin/pip install -r requirements.txt
