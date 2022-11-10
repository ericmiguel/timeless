import timeless

from numpy import datetime64


def test_to_np_datetime64_utc():
    dt = timeless.datetime(1975, 1, 1, 15)
    dt_ref = datetime64("1975-01-01T15:00:00")
    np_dt = timeless.to_np_datetime64(dt)

    assert isinstance(np_dt, datetime64)
    assert dt_ref == np_dt


def test_to_np_datetime64_arbitrary_timezone():
    dt = timeless.datetime(1975, 1, 1, 15, zone="America/Sao_Paulo")
    dt_ref = datetime64("1975-01-01T18:00:00")
    np_dt = timeless.to_np_datetime64(dt)

    assert isinstance(np_dt, datetime64)
    assert dt_ref == np_dt


def test_from_np_datetime64_utc():
    dt = datetime64("1975-01-01T15:00:00")
    dt_ref = timeless.datetime(1975, 1, 1, 15, zone="UTC")
    dt_np = timeless.from_np_datetime64(dt)

    assert isinstance(dt_np, timeless.datetime)
    assert dt_ref == dt_np
