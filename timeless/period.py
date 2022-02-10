"""Friendly time span utilities."""

from typing import Union

from dateutil.relativedelta import relativedelta
from timeless.datetime import Datetime


class Period(list):
    """Timeless time span."""

    def __init__(
        self,
        start: Datetime,
        end: Union[int, Datetime],
        freq: str = "days",
        step: int = 1,
    ):
        list.__init__(self)

        self.start = start
        self.end = end
        self.freq = freq
        self.step = step

        if isinstance(end, int):
            end = start.add(**{freq: end})

        self.append(start)
        while start < end:
            start = start.add(**{freq: step})
            self.append(start)

    def append(self, item: Datetime) -> None:
        """
        [summary]

        [extended_summary]

        Parameters
        ----------
        item : Datetime
            [description]

        Raises
        ------
        ValueError
            [description]
        TypeError
            [description]
        """
        if not isinstance(item, Datetime):
            raise ValueError("Only Datetime instances allowed")

        if item in self:
            raise TypeError("Period cannot have duplicate items")

        super(Period, self).append(item)
        self.start = min(self)
        self.end = max(self)

    def insert(self, index: int, item: Datetime) -> None:
        """
        [summary]

        [extended_summary]

        Parameters
        ----------
        index : int
            [description]
        item : Datetime
            [description]

        Raises
        ------
        ValueError
            [description]
        TypeError
            [description]
        """
        if not isinstance(item, Datetime):
            raise ValueError("Only Datetime instances allowed")

        if item in self:
            raise TypeError("Period cannot have duplicate items")

        super(Period, self).insert(index, item)
        self.start = min(self)
        self.end = max(self)

    def __add__(self, other) -> "Period":
        if isinstance(other, relativedelta):
            delta = {
                "years": other.years,
                "months": other.months,
                "days": other.days,
                "hours": other.hours,
                "minutes": other.minutes,
                "seconds": other.seconds,
                "microseconds": other.microseconds,
            }
            start = self.start.add(**delta)
            end = self.end.add(**delta)  # type: ignore
            return self.__class__(start, end, self.freq, self.step)

        return NotImplemented

    def shift(
        self,
        years: int = 0,
        months: int = 0,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
        microseconds: int = 0,
    ):
        return self + relativedelta(
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            microseconds=microseconds,
        )

    def __sub__(self, other) -> "Period":
        return self.__add__(other)

    def __lt__(self, item) -> bool:
        raise NotImplementedError

    def __le__(self, item) -> bool:
        raise NotImplementedError

    def __eq__(self, item) -> bool:
        raise NotImplementedError

    def __gt__(self, item) -> bool:
        raise NotImplementedError

    def __ge__(self, item) -> bool:
        raise NotImplementedError
