"""Type converters for ease integrations."""

import warnings


try:
    from timeless.converters.np_conv import from_np_datetime64
    from timeless.converters.np_conv import to_np_datetime64
    from timeless.converters.pd_conv import from_pd_datetimeindex
    from timeless.converters.pd_conv import from_pd_timestamp
except ImportError:
    warnings.warn("Run 'pip install timeless --extras converters'")

from timeless.converters.dt_conv import from_datetime
from timeless.converters.dt_conv import to_datetime


__all__ = [
    "to_datetime",
    "from_datetime",
    "from_np_datetime64",
    "from_pd_datetimeindex",
    "from_pd_timestamp",
    "to_np_datetime64",
]
