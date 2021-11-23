"""Friendly datetime utilities."""

from datetime import date as _date
from datetime import datetime as _datetime
from typing import Iterator
from typing import Optional
from typing import Union
from zoneinfo import ZoneInfo

from dateutil.relativedelta import relativedelta
from timeless import utils


class Datetime(_datetime, _date):
    """..."""

    def __new__(
        cls,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        microsecond: int,
        zone: Union[ZoneInfo, str] = ZoneInfo("UTC"),
    ):
        """..."""

        if isinstance(zone, str):
            zone = ZoneInfo(zone)

        self = _datetime.__new__(
            cls,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
            tzinfo=zone,
        )
        return self

    def add(self, *args, **kwargs) -> "Datetime":
        """
        Add duration to the instance.

        Returns
        -------
        [type]
            [description]
        """
        dt = self + relativedelta(*args, **kwargs)
        return self.__class__(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            microsecond=dt.microsecond,
            zone=self.zone,
        )

    def subtract(self, *args, **kwargs) -> "Datetime":
        """
        Remove duration from the instance.

        Returns
        -------
        [type]
            [description]
        """
        dt = self - relativedelta(*args, **kwargs)
        return self.__class__(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            microsecond=dt.microsecond,
            zone=self.zone,
        )

    def __iter__(self) -> Iterator[int]:
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
        zone: Optional[Union[str, ZoneInfo]] = "UTC",
    ):

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

        return self.__class__(
            year, month, day, hour, minute, second, microsecond, zone=zone
        )

    @property
    def zone(self) -> str:
        return str(self.tzinfo)

    @property
    def zone_info(self) -> ZoneInfo:
        """
        Return the timezone object.

        Returns
        -------
        ZoneInfo
            [description]
        """
        return ZoneInfo(self.zone)

    def is_future(self) -> bool:
        """
        Check if the instance is in the future.

        Returns
        -------
        bool
            [description]
        """
        return self > _datetime.now(tz=self.tzinfo)

    def is_past(self) -> bool:
        """
        Check if the instance is in the past.

        Returns
        -------
        bool
            [description]
        """
        return self < _datetime.now(tz=self.tzinfo)

    def format(self, format: Optional[str] = None) -> str:
        if format is None:
            return self.isoformat()

        return self.strftime(format)

    @property
    def zero(self):
        """Get rid of hour, minute, second, and microsecond information."""
        return self.set(hour=0, minute=0, second=0, microsecond=0, zone=self.zone)

    def diff(self, other: "Datetime") -> relativedelta:
        """
        Get the difference between the instance and another.

        Returns
        -------
        Datetime
            [description]
        """
        return relativedelta(self, other)

    def get_next(self, weekday: str) -> "Datetime":
        weekday_ = utils.Weekdays.__dict__[weekday]
        next_weekday = self + relativedelta(days=1, weekday=weekday_)

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

    def to_datetime(self) -> _datetime:
        """
        Convert the instance to a datetime object.

        Returns
        -------
        _datetime
            [description]
        """
        return _datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=self.hour,
            minute=self.minute,
            second=self.second,
            microsecond=self.microsecond,
            tzinfo=self.tzinfo,
        )
