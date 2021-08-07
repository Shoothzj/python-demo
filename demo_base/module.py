from dataclasses import dataclass


@dataclass
class TimeModule:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    ms: int
    ns: int
