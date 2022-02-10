from datetime import date as _date
from datetime import datetime as _datetime
from typing import Optional
from zoneinfo import ZoneInfo

from dateutil import parser
from timeless.datetime import Datetime


def now(zone: str = "UTC") -> Datetime:
    """
    Get a DateTime instance for the current date and time.

    Parameters
    ----------
    zone : Optional[str], optional
        [description], by default None

    Returns
    -------
    Datetime
        [description]
    """
    dt_ = _datetime.now(tz=ZoneInfo(zone))
    dt = Datetime(
        dt_.year,
        dt_.month,
        dt_.day,
        dt_.hour,
        dt_.minute,
        dt_.second,
        dt_.microsecond,
        zone,
    )

    return dt


def today(zone: str = "UTC") -> Datetime:
    dt = _date.today()
    return Datetime(dt.year, dt.month, dt.day, 0, 0, 0, 0, zone)


def parse(
    dt_str: str, zone: str = "UTC", fill: Optional[Datetime] = None, *args, **kwargs
) -> Datetime:
    parsed = parser.parse(dt_str, ignoretz=True, default=fill, *args, **kwargs)

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
