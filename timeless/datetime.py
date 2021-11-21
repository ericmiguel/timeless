"""Friendly datetime utilities."""

from datetime import date as _date
from datetime import datetime as _datetime
from typing import Optional
from typing import Union
from zoneinfo import ZoneInfo

from dateutil.relativedelta import relativedelta


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

    def isoformat(self):
        """Return the date's ISO 8601 string."""
        return self.isoformat()

    @property
    def zero(self):
        """Get rid of hour, minute, second, and microsecond information."""
        self.replace(hour=0, minute=0, second=0, microsecond=0)
        return self
