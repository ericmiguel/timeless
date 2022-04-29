"""Type converters for ease integrations."""

import warnings

from datetime import datetime as _datetime
from typing import Union


try:  # Python <3.9
    from zoneinfo import ZoneInfo
except ImportError:
    from backports import zoneinfo as ZoneInfo  # type: ignore

import numpy as np
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
        Python's default datetime object.
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
    dt: _datetime, zone: Union[ZoneInfo, str] = ZoneInfo("UTC")
) -> Datetime:
    """
    Convert a datetime object to a timeless.Datetime.

    Parameters
    ----------
    datetime : _datetime
        Python's default datetime object.
    zone : Union[ZoneInfo, str], optional
        Timezone, by default ZoneInfo("UTC")

    Returns
    -------
    Datetime
        Timeless datetime
    """
    return Datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second,
        microsecond=dt.microsecond,
        zone=zone,
    )


def from_pd_datetimeindex(dt: pd.DatetimeIndex) -> Period:
    """Pandas DatetimeIndex to Period."""
    freq = None

    if dt.freq:
        freq = utils.parse_pandas_offset_freq(dt.freq.name)

    if freq is None:
        warnings.warn("No frequency found in DatetimeIndex: assuming 'days'.")
        freq = "days"

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


def from_pd_timestamp(
    dt: pd.Timestamp, zone: str = "UTC", enforce_zone: bool = False
) -> Datetime:
    """
    Pandas Timestamp to Datetime.

    Parameters
    ----------
    dt : pd.Timestamp
        Pandas Timestamp.
    zone : str, optional
        Timezone name in case of any is found, by default "UTC"
    enforce_zone : bool, optional
        Force timezone conversion to 'zone' value, by default False

    Returns
    -------
    Datetime
        Timeless Datetime
    """
    if not hasattr(dt.tz, "zone"):
        dt = dt.tz_localize(zone)

    if enforce_zone:
        dt = dt.tz_convert(zone)

    datetime_obj = dt.to_pydatetime()

    return Datetime(
        datetime_obj.year,
        datetime_obj.month,
        datetime_obj.day,
        datetime_obj.hour,
        datetime_obj.minute,
        datetime_obj.second,
        datetime_obj.microsecond,
        str(datetime_obj.tzinfo),
    )


def to_pd_timestamp(dt: Datetime) -> pd.Timestamp:
    """
    Create a pandas.Timestamp instance from a Datetime.

    Parameters
    ----------
    dt : Datetime
        Timeless Datetime.

    Returns
    -------
    pd.Timestamp
        Pandas Timestamp.
    """
    return pd.Timestamp(dt)


def to_np_datetime64(dt: Datetime) -> np.datetime64:
    """
    Convert a Datetime instance to a Numpy datetime64 instance.

    Parameters
    ----------
    datetime : Datetime
        Datetime or Period instance.

    Returns
    -------
    np.datetime64
        Numpy time instances.
    """
    return np.datetime64(dt)


def from_np_datetime64(dt: np.datetime64) -> Datetime:
    """
    Convert a Numpy datetime64 instance to a Timeless Datetime instance.

    Parameters
    ----------
    datetime : np.datetime64
        Numpy Datetime64 instance.

    Returns
    -------
    Datetime
        Timeless Datetime instance.
    """
    unix_epoch = np.datetime64(0, "s")
    one_second = np.timedelta64(1, "s")
    seconds_since_epoch = float((dt - unix_epoch) / one_second)
    dt_datetime = _datetime.utcfromtimestamp(seconds_since_epoch)
    return from_datetime(dt_datetime)
