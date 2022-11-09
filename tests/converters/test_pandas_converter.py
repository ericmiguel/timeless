import timeless

from pandas import Timestamp


def test_to_pd_timestamp():
    dt = timeless.datetime(1975, 1, 1, 15, zone="America/Sao_Paulo")
    dt_ref = Timestamp("1975-01-01 15:00:00-03:00")
    pd_dt = timeless.to_pd_timestamp(dt)

    assert isinstance(pd_dt, Timestamp)
    assert dt_ref.hour == pd_dt.hour


def test_from_pd_timestamp_utc():
    dt = Timestamp(f"1975-01-01 15:00:00")
    dt_ref = timeless.datetime(1975, 1, 1, 15)
    dt_pd = timeless.from_pd_timestamp(dt)

    assert isinstance(dt_pd, timeless.datetime)
    assert dt_ref.hour == dt_pd.hour


def test_from_pd_timestamp_arbitrary_timezone():
    dt = Timestamp("1975-01-01 15:00:00", tz="America/Sao_Paulo")
    dt_ref = timeless.datetime(1975, 1, 1, 15, zone="America/Sao_Paulo")
    dt_pd = timeless.from_pd_timestamp(dt)

    assert isinstance(dt_pd, timeless.datetime)
    assert dt_ref.hour == dt_pd.hour


def test_from_pd_timestamp_arbitrary_offset():
    offset = 3
    dt = Timestamp(f"1975-01-01 15:00:00-0{offset}:00")
    dt_ref = timeless.datetime(1975, 1, 1, 15, zone="America/Sao_Paulo")
    dt_pd = timeless.from_pd_timestamp(dt)

    assert isinstance(dt_pd, timeless.datetime)
    assert dt_ref.hour + offset == dt_pd.hour
