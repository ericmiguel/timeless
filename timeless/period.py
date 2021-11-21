from typing import Iterator
from typing import List
from typing import Union

from timeless.datetime import Datetime


class Period:
    def __init__(
        self,
        start: Datetime,
        end: Union[int, Datetime],
        freq: str = "days",
    ):
        self._start = start
        self._end = end
        self._freq = freq

    @property
    def freq(self) -> str:
        return self._freq

    @property
    def start(self) -> Datetime:
        return self._start

    @property
    def end(self) -> Datetime:
        if isinstance(self._end, int):
            return self._start.add(**{self.freq: self._end - 1})
        else:
            return self._end

    @staticmethod
    def _create_period(start: Datetime, end: Datetime, freq: str) -> Iterator[Datetime]:
        while start <= end:
            yield start
            start = start.add(**{freq: 1})

    @property
    def period(self) -> Iterator[Datetime]:
        period = self._create_period(self._start, self.end, self.freq)

        return period

    def to(self, freq: str) -> "Period":
        return Period(self.start, self.end, freq)

    def __iter__(self) -> Iterator[Datetime]:
        return self.period

    def compute(self) -> List[Datetime]:
        return list(self.period)
