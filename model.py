from enum import StrEnum, auto


class Role(StrEnum):
    USER = auto()
    ASSISTANT = auto()
    SYSTEM = auto()
