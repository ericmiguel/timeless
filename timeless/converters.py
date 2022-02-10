from datetime import datetime as _datetime
from typing import List
from typing import Union
from zoneinfo import ZoneInfo

import pandas as pd

from timeless import utils
from timeless.datetime import Datetime
from timeless.period import Period


def to_datetime(datetime: _datetime) -> _datetime:
    """
    Convert a timeless.Datetime to a datetime object.

    Returns
    -------
    _datetime
        [description]
    """
    return _datetime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=datetime.hour,
        minute=datetime.minute,
        second=datetime.second,
        microsecond=datetime.microsecond,
        tzinfo=datetime.tzinfo,
    )


def from_datetime(
    datetime: _datetime, zone: Union[ZoneInfo, str] = ZoneInfo("UTC")
) -> Datetime:

    return Datetime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=datetime.hour,
        minute=datetime.minute,
        second=datetime.second,
        microsecond=datetime.microsecond,
        zone=zone,
    )


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
            freq = "day"
            # raise ValueError("No frequency found in DatetimeIndex")

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
