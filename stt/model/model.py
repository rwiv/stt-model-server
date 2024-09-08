import math
from dataclasses import dataclass
from typing import BinaryIO
from faster_whisper import WhisperModel
from numpy import ndarray

from stt.utils.logger import log


device = "cuda"
beam_size = 5
word_timestamps = True
vad_filter = True


@dataclass
class Segment:
    start: int
    end: int
    text: str


class SttModel:
    def __init__(self, model_size: str, compute_type: str):
        self.model = WhisperModel(
            model_size, device=device, compute_type=compute_type
        )
        log.info(f"Model loaded: {model_size}")

    def transcribe(self, file: str | BinaryIO | ndarray) -> list[Segment]:
        segments, info = self.model.transcribe(
            file, beam_size=beam_size, word_timestamps=word_timestamps, vad_filter=vad_filter,
        )
        words = []
        for seg in segments:
            for word in seg.words:
                words.append(Segment(
                    start=math.floor(word.start * 1000),
                    end=math.floor(word.end * 1000),
                    text=word.word,
                ))

        if len(words) == 0:
            raise ValueError("No words found in the audio")

        sentences: list[Segment] = []
        cur_sentence: list[Segment] = []
        for word in words:
            cur_sentence.append(word)
            if word.text.strip().endswith(('.', '?', '!')):
                sentences.append(merge_segments(cur_sentence))
                cur_sentence = []

        return sentences


def merge_segments(segments: list[Segment]) -> Segment:
    return Segment(
        start=segments[0].start,
        end=segments[-1].end,
        text="".join([seg.text for seg in segments]).strip()
    )
