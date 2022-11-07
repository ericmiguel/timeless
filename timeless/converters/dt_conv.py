"""Type converters for native Datetime integrations."""

from datetime import datetime as _datetime

from timeless.datetime import Datetime


def to_datetime(dt: Datetime) -> _datetime:
    """
    Convert a timeless.Datetime to a datetime object.

    Parameters
    ----------
    dt : Datetime
        Timeless datetime to convert to.

    Returns
    -------
    _datetime
        Python's default datetime object.
    """
    return _datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second,
        microsecond=dt.microsecond,
        tzinfo=dt.tzinfo,
    )


def from_datetime(dt: _datetime, zone: str = "UTC") -> Datetime:
    """
    Convert a datetime object to a timeless.Datetime.

    Parameters
    ----------
    dt : _datetime
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
