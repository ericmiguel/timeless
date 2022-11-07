"""Type converters for Numpy integrations."""

from datetime import datetime as _datetime

import numpy as np  # type: ignore

from timeless.converters.dt_conv import from_datetime
from timeless.datetime import Datetime


def to_np_datetime64(dt: Datetime) -> np.datetime64:
    """
    Convert a Datetime instance to a Numpy datetime64 instance.

    Parameters
    ----------
    dt : Datetime
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
    dt_datetime = _datetime.utcfromtimestamp(seconds_since_epoch)
    return from_datetime(dt_datetime)
