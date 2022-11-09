from datetime import datetime as _datetime

import numpy as np  # type: ignore

from timeless.converters.datetime_converter import from_datetime
from timeless.datetime import Datetime


def to_np_datetime64(dt: Datetime) -> np.datetime64:
    """
    Convert a Datetime instance to a Numpy datetime64 instance.

    Internally a datetime64 represents a moment in time as a value since the
    UNIX epoch (1970-01-01) - not counting leap seaconds.

    Therefore, time zones are not preserved. If you pass in a time zone offset,
    it will apply it to determine the correct UTC time. If you don't pass one,
    it will use the local machine's time zone. Regardless of input, on output
    it uses the local machine's time zone to project the UTC time to a local
    time with offset.

    Only avaible if Numpy is installed.

    Run 'pip install timeless --extras converters'

    Parameters
    ----------
    dt : Datetime
        Datetime or Period instance.

    Returns
    -------
    np.datetime64
        Numpy time instances.
    """
    offset = dt.get_utc_offset() * -1
    dt_conv = dt.set(zone="UTC").add(hours=offset).format(r"%Y-%m-%dT%H:%M:%S.%f")
    return np.datetime64(dt_conv)


def from_np_datetime64(dt: np.datetime64, zone: str = "UTC") -> Datetime:
    """
    Convert a Numpy datetime64 instance to a Timeless Datetime instance.

    Only avaible if Numpy is installed.

    Run 'pip install timeless --extras converters'

    Parameters
    ----------
    dt : np.datetime64
        Numpy Datetime64 instance.

    Returns
    -------
    Datetime
        Timeless Datetime instance.
    """
    unix_epoch = np.datetime64(0, "s")
    one_second = np.timedelta64(1, "s")
    seconds_since_epoch = float((dt - unix_epoch) / one_second)
    _dt_datetime = _datetime.utcfromtimestamp(seconds_since_epoch)
    dt_datetime = from_datetime(_dt_datetime)

    if zone != "UTC":
        dt_datetime_zone = dt_datetime.set(zone=zone)
        offset = dt_datetime_zone.get_utc_offset()
        dt_datetime = dt_datetime_zone.add(hours=offset)

    return dt_datetime
