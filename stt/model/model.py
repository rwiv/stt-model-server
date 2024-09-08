import math
from dataclasses import dataclass
from typing import BinaryIO, Iterable
from faster_whisper import WhisperModel
from faster_whisper.transcribe import Segment
from numpy import ndarray

from stt.utils.logger import log


device = "cuda"
beam_size = 5
word_timestamps = True


@dataclass
class Sentence:
    start: int
    end: int
    text: str


@dataclass
class Word:
    start: int
    end: int
    text: str
    is_first: bool
    is_last: bool


class SttModel:
    def __init__(self, model_size: str, compute_type: str):
        self.model = WhisperModel(
            model_size, device=device, compute_type=compute_type
        )
        log.info(f"Model loaded: {model_size}")

    def transcribe(self, file: str | BinaryIO | ndarray, is_split=True) -> list[Sentence]:
        segments, info = self.model.transcribe(
            file, beam_size=beam_size, word_timestamps=word_timestamps,
        )
        if is_split:
            return split_by_word(segments)
        else:
            result = []
            for seg in segments:
                result.append(Sentence(
                    start=math.floor(seg.start * 1000),
                    end=math.floor(seg.end * 1000),
                    text=seg.text.strip(),
                ))
            return result


def merge_segments(segments: list[Word]) -> Sentence:
    return Sentence(
        start=segments[0].start,
        end=segments[-1].end,
        text="".join([seg.text for seg in segments]).strip()
    )


def split_by_word(segments: Iterable[Segment]) -> list[Sentence]:
    words = []
    for seg in segments:
        for idx, word in enumerate(seg.words):
            words.append(Word(
                start=math.floor(word.start * 1000),
                end=math.floor(word.end * 1000),
                text=word.word,
                is_first=idx == 0,
                is_last=idx == len(seg.words) - 1,
            ))

    if len(words) == 0:
        raise ValueError("No words found in the audio")

    sentences: list[Sentence] = []
    cur_sentence: list[Word] = []
    for word in words:
        if word.is_first and len(word.text.strip()) > 0 and word.text.strip()[0].isupper():
            if len(cur_sentence) > 0:
                sentences.append(merge_segments(cur_sentence))
                cur_sentence = []
        cur_sentence.append(word)
        if word.text.strip().endswith(('.', '?', '!')):
            sentences.append(merge_segments(cur_sentence))
            cur_sentence = []

    return sentences

