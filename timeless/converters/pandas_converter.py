import warnings

from typing import Optional

import pandas as pd  # type: ignore

from timeless.datetime import Datetime
from timeless.period import Period


try:  # Python <3.9
    from zoneinfo import ZoneInfo  # type: ignore
    from zoneinfo._common import ZoneInfoNotFoundError  # type: ignore
except ImportError:
    from backports.zoneinfo import ZoneInfo  # type: ignore
    from backports.zoneinfo._common import ZoneInfoNotFoundError  # type: ignore


def parse_pandas_offset_freq(offset: str) -> Optional[str]:
    """
    Map pandas offset strings to timeless.Datetime strings.

    Parameters
    ----------
    offset : str
        Pandas offset string.

    Returns
    -------
    Optional[str]
        Timeless offset string.

    Raises
    ------
    ValueError
        Invalid or unknown offset string.
    """
    offsets = {
        "B": None,
        "C": None,
        "D": "days",
        "W": "weeks",
        "M": "months",
        "SM": None,
        "BM": None,
        "CBM": None,
        "MS": "months",
        "SMS": None,
        "BMS": None,
        "CBMS": None,
        "Q": None,
        "BQ": None,
        "QS": None,
        "BQS": None,
        "A": "years",
        "Y": "years",
        "BA": None,
        "BY": None,
        "AS": "years",
        "YS": "years",
        "BAS": None,
        "BYS": None,
        "BH": None,
        "H": "hours",
        "T": "minutes",
        "min": "minutes",
        "S": "seconds",
        "L": None,
        "ms": None,
        "U": "microseconds",
        "US": "microseconds",
        "N": None,
    }

    if offset not in offsets or offsets[offset] is None:
        raise ValueError(f"Unknown offset: {offset}")

    return offsets[offset]


def from_pd_datetimeindex(dt: pd.DatetimeIndex) -> Period:  # type: ignore
    """
    Pandas DatetimeIndex to Period.

    Only avaible if Pandas is installed.

    Run 'pip install timeless --extras converters'
    """
    freq = None

    if dt.freq:
        freq = parse_pandas_offset_freq(dt.freq.name)

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


def from_pd_timestamp(dt: pd.Timestamp) -> Datetime:
    """
    Pandas Timestamp to Datetime.

    If no timezone info is offered, UTC is assumed. If just fixed hour offset exists,
    the time value is converted to UTC (thus the offset is apllyed).

    Only avaible if Pandas is installed.

    Run 'pip install timeless --extras converters'

    Parameters
    ----------
    dt : pd.Timestamp
        Pandas Timestamp.

    Returns
    -------
    Datetime
        Timeless Datetime
    """
    # No timezone info (fixed offset or timezone name)
    if not hasattr(dt.tz, "zone"):
        dt = dt.tz_localize("UTC")
        dt = dt.tz_convert("UTC")

    datetime_obj = dt.to_pydatetime()

    zone = str(datetime_obj.tzinfo) if datetime_obj.tzinfo else "UTC"

    try:
        _ = ZoneInfo(zone)
    # Some timezone info, but unamed fixed offset
    except ZoneInfoNotFoundError:
        zone = "UTC"
        datetime_obj = dt.tz_convert("UTC").to_pydatetime()

    return Datetime(
        datetime_obj.year,
        datetime_obj.month,
        datetime_obj.day,
        datetime_obj.hour,
        datetime_obj.minute,
        datetime_obj.second,
        datetime_obj.microsecond,
        zone,
    )


def to_pd_timestamp(dt: Datetime) -> pd.Timestamp:  # type: ignore
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
