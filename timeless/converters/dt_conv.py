"""Type converters for native Datetime integrations."""

from datetime import datetime as _datetime
from typing import Union


try:  # Python <3.9
    from zoneinfo import ZoneInfo  # type: ignore
except ImportError:
    from backports.zoneinfo import ZoneInfo  # type: ignore


from timeless.datetime import Datetime


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
