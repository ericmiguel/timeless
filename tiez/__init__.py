"""..."""

from datetime import datetime as _datetime
from typing import Optional

from pytz import timezone
from pytz import utc

from .datetime import Datetime


def datetime(*args, **kwargs) -> Datetime:
    """
    Get a Datetime instance.

    Returns
    -------
    Datetime
        tiez.datetime.Datetime instance.
    """
    return Datetime(*args, **kwargs)


def now(zone: Optional[str]) -> Datetime:
    """
    Get a DateTime instance for the current date and time.

    Parameters
    ----------
    zone : Optional[str]
        timezone name as in pytz.

    Returns
    -------
    Datetime
        tiez.datetime.Datetime instance.
    """
    tz = timezone(zone) if zone else utc
    dt = _datetime.now(tz=tz)

    return Datetime(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond
    )
