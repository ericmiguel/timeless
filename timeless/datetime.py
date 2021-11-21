"""Friendly datetime utilities."""

from datetime import date
from datetime import datetime
from typing import Optional
from typing import Union
from zoneinfo import ZoneInfo

from dateutil.relativedelta import relativedelta


class Datetime(datetime, date):
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
        zone: Union[ZoneInfo, str] = "UTC",
        *args,
        **kwargs
    ):
        """..."""

        if isinstance(zone, str):
            zone = ZoneInfo(zone)

        self = datetime.__new__(
            cls,
            year,
            month,
            day,
            hour,
            minute,
            second,
            microsecond,
            tzinfo=zone,
            *args,
            **kwargs
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
        return dt

    def subtract(self, *args, **kwargs) -> "Datetime":
        """
        Remove duration from the instance.

        Returns
        -------
        [type]
            [description]
        """
        dt = self - relativedelta(*args, **kwargs)
        return dt

    def set(
        self,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
        microsecond: Optional[int] = None,
        zone: Optional[Union[str, ZoneInfo]] = None,
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
        return self > datetime.now(tz=self.tzinfo)

    def is_past(self) -> bool:
        """
        Check if the instance is in the past.

        Returns
        -------
        bool
            [description]
        """
        return self < datetime.now(tz=self.tzinfo)
