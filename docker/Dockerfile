FROM nvidia/cuda:12.6.1-runtime-ubuntu22.04

WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY stt stt

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN apt-get install libcudnn8 -y

RUN pip install torch==2.4.1 --index-url https://download.pytorch.org/whl/cu124
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-u", "main.py"]