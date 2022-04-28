"""Friendly interface for time span manipulations."""

from typing import Union

from dateutil.relativedelta import relativedelta
from timeless.datetime import Datetime
from timeless.datetime import parse


class Period(list):
    """Timeless time span."""

    def __init__(
        self,
        start: Union[str, Datetime],
        end: Union[str, Datetime],
        freq: str = "days",
        step: int = 1,
        parse_kwargs: dict = dict(),
    ):
        list.__init__(self)

        if isinstance(start, str):
            start = parse(start, **parse_kwargs)

        if isinstance(end, str):
            end = parse(end, **parse_kwargs)

        if end < start:
            raise ValueError("End date must be greater than start date")

        self.start = start
        self.end = end
        self.freq = freq
        self.step = step

        self.append(start)
        while start < end:
            start = start.add(**{freq: step})
            self.append(start)

    def append(self, item: Datetime) -> None:
        """
        Append a datetime instance to the end of the period.

        Parameters
        ----------
        item : Datetime
            Datetime instance to append.

        Raises
        ------
        ValueError
            Only Datetime instances allowed.
        TypeError
            Periods cannot have duplicate items.
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
        Insert a datetime instance at the given index.

        Parameters
        ----------
        index : int
            List index to insert at.
        item : Datetime
            Datetime instance to insert.

        Raises
        ------
        ValueError
            Only Datetime instances allowed.
        TypeError
            Periods cannot have duplicate items.
        """
        if not isinstance(item, Datetime):
            raise ValueError("Only Datetime instances allowed")

        if item in self:
            raise TypeError("Period cannot have duplicate items")

        super(Period, self).insert(index, item)
        self.start = min(self)
        self.end = max(self)

    def add(self, other: relativedelta) -> "Period":
        """
        Sum a given timedelta to the period.

        Currently only supports relativedelta.

        Returns
        -------
        Period
            New period with the given timedelta added.
        """
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
            end = self.end.add(**delta)
            return self.__class__(start, end, self.freq, self.step)

        return NotImplemented

    def subtract(self, other: relativedelta) -> "Period":
        """
        Sum (subtract) a given timedelta to the period.

        Currently only supports relativedelta.

        Uses the __add__ method, since relativedelta can be positive or negative.

        Returns
        -------
        Period
            New period with the given timedelta added.
        """
        return self.add(other)

    def shift(
        self,
        years: int = 0,
        months: int = 0,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
        microseconds: int = 0,
    ) -> "Period":
        """
        Sum or subtract a timedelta from the period.

        Currently only supports relativedelta.

        Parameters
        ----------
        years : int, optional
            years delta, by default 0
        months : int, optional
            months delta, by default 0
        days : int, optional
            days delta, by default 0
        hours : int, optional
            hours delta, by default 0
        minutes : int, optional
            minutes delta, by default 0
        seconds : int, optional
            seconds delta, by default 0
        microseconds : int, optional
            microseconds delta, by default 0

        Returns
        -------
        Period
            New period with the given timedelta added.
        """
        return self.add(
            relativedelta(
                years=years,
                months=months,
                days=days,
                hours=hours,
                minutes=minutes,
                seconds=seconds,
                microseconds=microseconds,
            )
        )

    @property
    def duration(self) -> float:
        """
        Total duration of the period in seconds.

        Returns
        -------
        float
            total seconds in the time span.
        """
        delta = self.start - self.end
        return abs(delta.total_seconds())

    def get_duration(self) -> float:
        """Equivalent function of duration property."""
        return self.duration

    def lt(self, other: "Period") -> bool:
        """Less than."""
        if self.duration < other.duration:
            return True

        return False

    def le(self, other: "Period") -> bool:
        """Less than or equal."""
        if self.duration <= other.duration:
            return True

        return False

    def eq(self, other: "Period") -> bool:
        """Equal."""
        if self.duration == other.duration:
            return True

        return False

    def gt(self, other: "Period") -> bool:
        """Greater than."""
        if self.duration > other.duration:
            return True

        return False

    def ge(self, other: "Period") -> bool:
        """Greater than or equal."""
        if self.duration >= other.duration:
            return True

        return False
