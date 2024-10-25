from typing import TypedDict, Optional, List


class SingleWordSegment(TypedDict):
    """
    A single word of a speech.
    """

    word: str
    start: float
    end: float
    score: float


class SingleCharSegment(TypedDict):
    """
    A single char of a speech.
    """

    char: str
    start: float
    end: float
    score: float


class SingleSegment(TypedDict):
    """
    A single segment (up to multiple sentences) of a speech.
    """

    start: float
    end: float
    text: str


class SingleAlignedSegment(TypedDict, total=False):
    """
    A single segment (up to multiple sentences) of a speech with word alignment.
    """

    start: float
    end: float
    text: str
    language: Optional[str]
    words: List[SingleWordSegment]
    chars: Optional[List[SingleCharSegment]]
    speaker: Optional[str]


class TranscriptionResult(TypedDict):
    """
    A list of segments and word segments of a speech.
    """

    segments: List[SingleSegment]
    language: str
    speakers: List[str]


class AlignedTranscriptionResult(TypedDict):
    """
    A list of segments and word segments of a speech.
    """

    segments: List[SingleAlignedSegment]
    word_segments: List[SingleWordSegment]
    speakers: List[str]
