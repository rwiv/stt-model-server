from dataclasses import dataclass

from stt.model.model import Segment


@dataclass
class SbtChunk:
    start: int
    end: int
    text: str

    def to_srt_string(self, num: int) -> str:
        result = f"{num}\n"
        result += f"{to_vtt_time_string(self.start)} --> {to_vtt_time_string(self.end)}\n"
        result += f"{self.text}\n"
        return result


def from_segment(segment: Segment):
    return SbtChunk(segment["start"], segment["end"], segment["text"].strip())


def to_srt_string(chunks: list[SbtChunk]):
    srt_str = ""
    for idx, chunk in enumerate(chunks):
        srt_str += f"{chunk.to_srt_string(idx + 1)}\n"
    return srt_str


def to_vtt_string(chunks: list[SbtChunk]):
    return "WEBVTT\n\n" + to_srt_string(chunks)


def to_vtt_time_string(ms: int):
    ph = 3600000  # milliseconds in an hour
    pm = 60000  # milliseconds in a minute
    ps = 1000  # milliseconds in a second

    rest = ms

    hour = rest // ph
    rest %= ph

    minute = rest // pm
    rest %= pm

    sec = rest / ps

    chunks = f"{sec:.3f}".split(".")
    left = chunks[0].zfill(2)
    right = chunks[1].ljust(3, '0')[:3]  # Ensure 3 digits in milliseconds

    hour_string = str(hour).zfill(2)
    minute_string = str(minute).zfill(2)

    return f"{hour_string}:{minute_string}:{left},{right}"
