"""Friendly interface for time span manipulations."""

from typing import TypedDict
from typing import Union

from dateutil.relativedelta import relativedelta
from timeless.datetime import Datetime
from timeless.datetime import parse
from timeless.datetime import today
from typing_extensions import SupportsIndex
from typing_extensions import Unpack


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

    def insert(self, index: SupportsIndex, item: Datetime) -> None:
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

    def _add(self, other: relativedelta) -> "Period":
        """
        Sum a given timedelta to the period.

        Parameters
        ----------
        other : relativedelta
            _description_

        Returns
        -------
        Period
            New period with the given timedelta added.

        Raises
        ------
        NotImplementedError
            Currently only supports relativedelta.
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

        raise NotImplementedError

    def _subtract(self, other: relativedelta) -> "Period":
        """
        Sum (subtract) a given timedelta to the period.

        Currently only supports relativedelta.

        Uses the __add__ method, since relativedelta can be positive or negative.

        Returns
        -------
        Period
            New period with the given timedelta added.
        """
        return self._add(other)

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
        return self._add(
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


class Periodkwargs(TypedDict):
    """Types for Period class."""

    freq: str
    step: int


def get_week(
    day: Datetime, week_first_day: str = "monday", **period_kwargs: Unpack[Periodkwargs]
) -> Period:
    """
    Given a datetime object, get relative week as a Period in days.

    You can set Period Kwargs to change time freq and step.

    Parameters
    ----------
    day : Datetime
        Reference Datetime.
    week_first_day : str, optional
        Start day of the week, by default "monday"

    Returns
    -------
    Period
        Week time span.
    """
    start = day.get_last(week_first_day)
    end = start.add(days=7)
    return Period(
        start,
        end,
        freq=period_kwargs.get("freq", "days"),
        step=period_kwargs.get("step", 1),
    )


def get_current_week(
    week_first_day: str = "monday",
    zone: str = "UTC",
    **period_kwargs: Unpack[Periodkwargs]
) -> Period:
    """
    Get current week as a Period in days.

    You can set Period Kwargs to change time freq and step.

    Parameters
    ----------
    week_first_day : str, optional
        Start day of the week, by default "monday"
    zone : str, optional
        Timezone, by default "UTC"

    Returns
    -------
    Period
        Week time span.
    """
    start = today(zone).get_last(week_first_day)
    end = start.add(days=7)
    return Period(
        start,
        end,
        freq=period_kwargs.get("freq", "days"),
        step=period_kwargs.get("step", 1),
    )


def get_month(day: Datetime, **period_kwargs: Unpack[Periodkwargs]) -> Period:
    """
    Given a datetime object, get relative month as a Period in days.

    You can set Period Kwargs to change time freq and step.

    Parameters
    ----------
    day : Datetime
        Reference Datetime.

    Returns
    -------
    Period
        Month time span.
    """
    start = day.get_month_start()
    end = start.get_month_end()
    return Period(
        start,
        end,
        freq=period_kwargs.get("freq", "days"),
        step=period_kwargs.get("step", 1),
    )


def get_current_month(
    zone: str = "UTC", **period_kwargs: Unpack[Periodkwargs]
) -> Period:
    """
    Get current month as a Period in days.

    You can set Period Kwargs to change time freq and step.

    Parameters
    ----------
    zone : str, optional
        Timezone, by default "UTC"

    Returns
    -------
    Period
        Month time span.
    """
    start = today(zone).get_month_start()
    end = start.get_month_end()
    return Period(
        start,
        end,
        freq=period_kwargs.get("freq", "days"),
        step=period_kwargs.get("step", 1),
    )
