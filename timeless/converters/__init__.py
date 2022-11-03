"""Type converters for ease integrations."""

try:
    from timeless.converters.np_conv import from_np_datetime64
    from timeless.converters.np_conv import to_np_datetime64
    from timeless.converters.pd_conv import from_pd_datetimeindex
    from timeless.converters.pd_conv import from_pd_timestamp
except ImportError:
    raise ImportError("Run 'pip install timeless --extras converters'")


__all__ = [
    "from_np_datetime64",
    "from_pd_datetimeindex",
    "from_pd_timestamp",
    "to_np_datetime64",
]
