from datetime import date as _date
from datetime import datetime as _datetime
from zoneinfo import ZoneInfo

import pandas as pd

from timeless.datetime import Datetime
from timeless.period import Period


def datetime(
    year: int,
    month: int,
    day: int,
    hour: int = 0,
    minute: int = 0,
    second: int = 0,
    microsecond: int = 0,
    zone: str = "UTC",
) -> Datetime:
    """
    Get a Datetime instance.

    Returns
    -------
    Datetime
        [description]
    """
    return Datetime(year, month, day, hour, minute, second, microsecond, zone)


def period(*args, **kwargs):
    return Period(*args, **kwargs)


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


def from_pandas(dt: pd.Timestamp) -> Datetime:
    """
    Get a Datetime instance from a pandas.Timestamp.

    Returns
    -------
    Datetime
        [description]
    """
    datetime_obj = dt.to_pydatetime()
    return Datetime(
        datetime_obj.year,
        datetime_obj.month,
        datetime_obj.day,
        datetime_obj.hour,
        datetime_obj.minute,
        datetime_obj.second,
        datetime_obj.microsecond,
        datetime_obj.tzinfo.zone,
    )


def to_pandas(dt: Datetime) -> pd.Timestamp:
    """
    Get a pandas.Timestamp instance from a Datetime.

    Returns
    -------
    pd.Timestamp
        [description]
    """
    return pd.Timestamp(dt)
