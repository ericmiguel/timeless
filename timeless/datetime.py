"""Friendly interface for datetime manipulations."""

import calendar

from dataclasses import dataclass
from datetime import date as _date
from datetime import datetime as _datetime
from typing import Iterator
from typing import Optional


try:  # Python <3.9
    from zoneinfo import ZoneInfo  # type: ignore
except ImportError:
    from backports.zoneinfo import ZoneInfo  # type: ignore

from dateutil import parser
from dateutil import relativedelta


@dataclass
class Weekdays:
    """Weekdays mapping for easy acess."""

    monday = relativedelta.MO
    tuesday = relativedelta.TU
    wednesday = relativedelta.WE
    thursday = relativedelta.TH
    friday = relativedelta.FR
    saturday = relativedelta.SA
    sunday = relativedelta.SU


class Datetime(_datetime):
    """Timeless datetime."""

    def __new__(
        cls,
        year: int,
        month: int,
        day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
        microsecond: int = 0,
        zone: str = "UTC",
    ) -> "Datetime":
        """Control the instance creation."""
        self = _datetime.__new__(
            cls,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
            tzinfo=ZoneInfo(zone),
        )

        return self

    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
        microsecond: int = 0,
        zone: str = "UTC",
    ) -> None:
        """
        Init a Timeless Datetime.

        Parameters
        ----------
        year : int
            _description_
        month : int
            _description_
        day : int
            _description_
        hour : int, optional
            _description_, by default 0
        minute : int, optional
            _description_, by default 0
        second : int, optional
            _description_, by default 0
        microsecond : int, optional
            _description_, by default 0
        zone : str, optional
            _description_, by default "UTC"
        """
        self.zone = zone

    def add(
        self,
        years: int = 0,
        months: int = 0,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
        microseconds: int = 0,
    ) -> "Datetime":
        """
        Add duration to the instance.

        Returns
        -------
        Datetime
            New datetime instance with added value.
        """
        other = relativedelta.relativedelta(
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            microseconds=microseconds,
        )

        result = (
            _datetime(
                self.year,
                self.month,
                self.day,
                self.hour,
                self.minute,
                self.second,
                self.microsecond,
                self.tzinfo,
            )
            + other
        )

        return Datetime(
            result.year,
            result.month,
            result.day,
            result.hour,
            result.minute,
            result.second,
            result.microsecond,
            str(self.tzinfo),
        )

    def subtract(
        self,
        years: int = 0,
        months: int = 0,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
        microseconds: int = 0,
    ) -> "Datetime":
        """
        Remove duration to the instance.

        Returns
        -------
        Datetime
            New datetime instance with the subtracted value.
        """
        other = relativedelta.relativedelta(
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            microseconds=microseconds,
        )

        result = (
            _datetime(
                self.year,
                self.month,
                self.day,
                self.hour,
                self.minute,
                self.second,
                self.microsecond,
                self.tzinfo,
            )
            - other
        )

        return Datetime(
            result.year,
            result.month,
            result.day,
            result.hour,
            result.minute,
            result.second,
            result.microsecond,
            str(self.tzinfo),
        )

    def __iter__(self) -> Iterator[int]:
        """
        Allow iteration over the instance.

        Yields
        ------
        Iterator[int]
            Instance values.
        """
        for attr in [
            "year",
            "month",
            "day",
            "hour",
            "minute",
            "second",
            "microsecond",
            "zone",
        ]:
            yield getattr(self, attr)

    def set(
        self,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
        microsecond: Optional[int] = None,
        zone: Optional[str] = "UTC",
    ) -> "Datetime":
        """
        Override the instance values.

        Parameters
        ----------
        year : Optional[int], optional
            new year value, by default None
        month : Optional[int], optional
            new month value, by default None
        day : Optional[int], optional
            new day value, by default None
        hour : Optional[int], optional
            new hour value, by default None
        minute : Optional[int], optional
            new minute value, by default None
        second : Optional[int], optional
            new second value, by default None
        microsecond : Optional[int], optional
            new microsecond value, by default None
        zone : Optional[Union[str, ZoneInfo]], optional
            new timezone value

        Returns
        -------
        Datetime
            New instance with the new values.
        """
        if year is None:
            year = self.year
        if month is None:
            month = self.month
        if day is None:
            day = self.day
        if hour is None:
            hour = self.hour
        if minute is None:
            minute = self.minute
        if second is None:
            second = self.second
        if microsecond is None:
            microsecond = self.microsecond
        if zone is None:
            # since timeless always uses UTC as default,
            # we can safely assume that timezone is always set
            zone = str(self.tzinfo)

        return self.__new__(
            self.__class__,
            year,
            month,
            day,
            hour,
            minute,
            second,
            microsecond,
            zone=zone,
        )

    def set_utc(self) -> "Datetime":
        """Set datetime as UTC without applying the timezone offset."""
        return self.set(zone="UTC")

    def is_leap(self) -> bool:
        """Return true or false for leap year Datetime instances."""
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def is_future(self) -> bool:
        """
        Check if the instance is in the future (within the same timezone).

        Returns
        -------
        bool
            is the instance in the future (relative to now).
        """
        return self > _datetime.now(tz=self.tzinfo)

    def is_past(self) -> bool:
        """
        Check if the instance is in the past (within the same timezone).

        Returns
        -------
        bool
            is the instance in the past (relative to now).
        """
        return self < _datetime.now(tz=self.tzinfo)

    def format(self, format: Optional[str] = None) -> str:
        """
        Format the instance as a string to isoformat or custom format.

        Parameters
        ----------
        format : Optional[str], optional
            Follows the same rules as the python strftime, by default None

        Returns
        -------
        str
            Datetime formated string.
        """
        if format is None:
            return self.isoformat()

        return self.strftime(format)

    def set_zero(self) -> "Datetime":
        """Get rid of hour, minute, second and microsecond values."""
        return self.set(
            hour=0, minute=0, second=0, microsecond=0, zone=str(self.tzinfo)
        )

    def diff(self, other: "Datetime") -> relativedelta.relativedelta:
        """
        Get the difference between the instance and another.

        Parameters
        ----------
        other : Datetime
            Other datetime instance to compare to.

        Returns
        -------
        relativedelta
            Delta between the two instances.
        """
        return relativedelta.relativedelta(self, other)

    def get_next(self, weekday: str) -> "Datetime":
        """
        Get the next instance of a given weekday.

        Does't consider the current day.

        Returns
        -------
        Datetime
            Next closest given weekday.
        """
        weekday_ = Weekdays.__dict__[weekday]
        next_weekday = self + relativedelta.relativedelta(days=1, weekday=weekday_)

        return self.__class__(
            next_weekday.year,
            next_weekday.month,
            next_weekday.day,
            0,
            0,
            0,
            0,
            zone=self.zone,
        )

    def get_last(self, weekday: str) -> "Datetime":
        """
        Get the last instance of a given weekday.

        Returns
        -------
        Datetime
            Last closest given weekday.
        """
        weekday_ = Weekdays.__dict__[weekday](-1)
        next_weekday = self + relativedelta.relativedelta(days=-1, weekday=weekday_)

        return self.__class__(
            next_weekday.year,
            next_weekday.month,
            next_weekday.day,
            0,
            0,
            0,
            0,
            zone=self.zone,
        )

    def get_weekday_name(self, week_start: Optional[str] = None) -> str:
        """
        Get the weekday name of the instance.

        Parameters
        ----------
        week_start : Optional[str], optional
            First day of the week, by default None (monday)

        Returns
        -------
        str
            [description]
        """
        if week_start:
            calendar.setfirstweekday(Weekdays.__dict__[week_start])

        numeric_weekday = self.weekday()
        weekday_name = calendar.day_name[numeric_weekday]
        return weekday_name.lower()

    def is_today(self, weekday: str, week_start: Optional[str] = None) -> bool:
        """
        Check if the instance weekday is at a given weekday.

        Parameters
        ----------
        weekday : str
            Weekday to check against.
        week_start : Optional[str], optional
            First day of the week, by default None (monday).

        Returns
        -------
        bool
            True if the instance weekday is at the given weekday.
        """
        instance_weekday = self.get_weekday_name(week_start=week_start)

        if weekday.lower() == instance_weekday:
            return True

        return False

    @property
    def days_in_month(self) -> int:
        """
        Get the number of days in the month.

        Returns
        -------
        int
            Total days in the instance month.
        """
        return calendar.monthrange(self.year, self.month)[1]

    def get_days_in_month(self) -> int:
        """
        Equivalent function of days_in_month property.

        Returns
        -------
        int
            Total days in the instance month.
        """
        return self.days_in_month

    def get_month_start(self) -> "Datetime":
        """
        Get a Datetime instance on the first day of the month.

        Only for semantic purposes.

        Returns
        -------
        Datetime
            First day of the month
        """
        return self.__class__(
            self.year,
            self.month,
            1,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
            zone=self.zone,
        )

    def get_month_end(self) -> "Datetime":
        """
        Get a Datetime instance on the last day of the month.

        Returns
        -------
        Datetime
            Kast day of the month
        """
        return self.__class__(
            self.year,
            self.month,
            self.days_in_month,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
            zone=self.zone,
        )


def now(zone: str = "UTC", microseconds: bool = False) -> Datetime:
    """
    Get a DateTime instance for the current date and time.

    Parameters
    ----------
    zone : Optional[str], optional
        Instance timezone, by default "UTC"

    Returns
    -------
    Datetime
        Current date and time.
    """
    dt_ = _datetime.now(tz=ZoneInfo(zone))

    if microseconds:
        ms = dt_.microsecond
    else:
        ms = 0

    dt = Datetime(
        dt_.year,
        dt_.month,
        dt_.day,
        dt_.hour,
        dt_.minute,
        dt_.second,
        ms,
        zone,
    )

    return dt


def today(zone: str = "UTC") -> Datetime:
    """
    Get a DateTime instance for the current date.

    Hours, minutes, seconds and microseconds are set to 0.

    Parameters
    ----------
    zone : str, optional
        Instance timezone, by default "UTC"

    Returns
    -------
    Datetime
        Current date.
    """
    dt = _date.today()
    return Datetime(dt.year, dt.month, dt.day, 0, 0, 0, 0, zone)


def get_first_weekday_in_month(
    datetime: Datetime, weekday: str, week_start: Optional[str] = None
) -> "Datetime":
    """
    Get the first occourance of a weekday at the instance month.

    Parameters
    ----------
    datetime : Datetime
        Datetime instance.
    weekday: str
        weekday name.
    week_start : Optional[str], optional
        week start day, by default None (monday)

    Returns
    -------
    Datetime
        First occourance of the given weekday at the instance month.
    """
    instance_weekday = datetime.get_weekday_name(week_start)

    if instance_weekday.lower() == weekday.lower():
        return datetime
    else:
        last_in_month = datetime.get_last(weekday)
        if last_in_month.month != datetime.month:
            return datetime.get_next(weekday)
        else:
            return last_in_month


def parse(
    string: str,
    format: Optional[str] = None,
    zone: Optional[str] = None,
    day_first: bool = False,
    year_first: bool = False,
) -> Datetime:
    """
    Parse a string into a Datetime.

    If no format is provided, the string is parsed using Dateutil's parser. Otherwise,
    the string is parsed using strptime. In the latter case dateutil's parser arguments
    (nominally day_first, year_first) are ignored.

    The "ignoretz" parameter is not supported, since "zone" can override the timezone
    value and Timeless does not accept naive datetimes.

    See https://dateutil.readthedocs.io/en/stable/parser.html for more information on
    dautil's parser arguments.

    Parameters
    ----------
    string : str
        datetime string to parse.
    format : Optional[str]
        dateutil format string, by default None.
    zone : Optional[str]
        timezone name (overrides parsed value), by default None.
    day_first : bool, optional
        Whether to interpret the first value in an ambiguous 3-integer date as the day,
        by default False
    year_first : bool, optional
        Whether to interpret the first value in an ambiguous 3-integer date as the year,
        by default False.

    Returns
    -------
    Datetime
        Parsed datetime.
    """
    if format:
        parsed = _datetime.strptime(string, format)
    else:
        parser_info = parser.parserinfo(dayfirst=day_first, yearfirst=year_first)
        parsed = parser.parse(string, parser_info)

    if not zone:
        zone = parsed.tzname()
        if not zone:
            zone = "UTC"

    return Datetime(
        parsed.year,
        parsed.month,
        parsed.day,
        parsed.hour,
        parsed.minute,
        parsed.second,
        parsed.microsecond,
        zone,
    )
