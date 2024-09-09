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

    def first_is_upper(self) -> bool:
        return (self.is_first
                and len(self.text.strip()) > 0
                and self.text.strip()[0].isupper())

    def is_last_in_sentence(self):
        return self.text.strip().endswith(('.', '?', '!'))


class SttModel:
    def __init__(self, model_size: str, compute_type: str, term_time_ms: int, relocation: bool):
        self.model = WhisperModel(
            model_size, device=device, compute_type=compute_type
        )
        self.term_time_ms = term_time_ms
        self.relocation = relocation
        log.info(f"Model loaded: {model_size}")

    def transcribe(self, file: str | BinaryIO | ndarray) -> list[Sentence]:
        segments, info = self.model.transcribe(
            file, beam_size=beam_size, word_timestamps=word_timestamps,
        )
        if self.relocation:
            return self._relocate_words(segments)
        else:
            result = []
            for seg in segments:
                result.append(Sentence(
                    start=math.floor(seg.start * 1000),
                    end=math.floor(seg.end * 1000),
                    text=seg.text.strip(),
                ))
            return result

    def _relocate_words(self, segments: Iterable[Segment]) -> list[Sentence]:
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
        for idx, word in enumerate(words):
            if len(cur_sentence) > 0 and word.first_is_upper():
                sentences.append(merge_segments(cur_sentence))
                cur_sentence = []
            cur_sentence.append(word)
            if word.is_last_in_sentence() or self._check_term_time(words, idx):
                sentences.append(merge_segments(cur_sentence))
                cur_sentence = []

        return sentences

    def _check_term_time(self, words: list[Word], idx: int) -> bool:
        if idx == len(words)-1:
            return False
        rest_time = words[idx+1].start - words[idx].start
        return rest_time > self.term_time_ms


def merge_segments(segments: list[Word]) -> Sentence:
    return Sentence(
        start=segments[0].start,
        end=segments[-1].end,
        text="".join([seg.text for seg in segments]).strip()
    )
