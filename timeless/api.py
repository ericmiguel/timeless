from datetime import date as _date
from datetime import datetime as _datetime
from typing import List
from typing import Optional
from typing import Union
from zoneinfo import ZoneInfo

import pandas as pd

from dateutil import parser
from timeless import utils
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


def from_pandas(dt: Union[pd.DatetimeIndex, pd.Timestamp]) -> Union[Datetime, Period]:
    """
    Get a Datetime instance from a pandas.Timestamp.

    Returns
    -------
    Datetime
        [description]
    """
    if isinstance(dt, pd.DatetimeIndex):
        if dt.freq:
            freq = utils.parse_pandas_offset_freq(dt.freq.name)
        else:
            raise ValueError("No frequency found in DatetimeIndex")

        _start = dt.min().to_pydatetime()
        _end = dt.max().to_pydatetime()

        try:
            _ = _start.tzinfo.zone
        except AttributeError:
            _start = _start.astimezone(ZoneInfo("UTC"))
            _end = _end.astimezone(ZoneInfo("UTC"))

        start = Datetime(
            _start.year,
            _start.month,
            _start.day,
            _start.hour,
            _start.minute,
            _start.second,
            _start.microsecond,
            _start.tzinfo.key,
        )
        end = Datetime(
            _end.year,
            _end.month,
            _end.day,
            _end.hour,
            _end.minute,
            _end.second,
            _end.microsecond,
            _end.tzinfo.key,
        )
        return Period(start, end, freq)

    else:
        datetime_obj = dt.to_pydatetime()

        try:
            _ = datetime_obj.tzinfo.zone
        except AttributeError:
            datetime_obj = datetime_obj.astimezone(ZoneInfo("UTC"))

        return Datetime(
            datetime_obj.year,
            datetime_obj.month,
            datetime_obj.day,
            datetime_obj.hour,
            datetime_obj.minute,
            datetime_obj.second,
            datetime_obj.microsecond,
            datetime_obj.tzinfo.key,
        )


def to_pandas(dt: Union[Period, Datetime]) -> Union[List[pd.Timestamp], pd.Timestamp]:
    """
    Get a pandas.Timestamp instance from a Datetime.

    Periods are converted to a list of pandas.Timestamp instances.

    Lists of Timestamps are automatically coerced DatetimeIndex by Pandas.

    Returns
    -------
    pd.Timestamp
        [description]
    """
    if isinstance(dt, Period):
        return [pd.Timestamp(d) for d in dt]
    else:
        return pd.Timestamp(dt)


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
