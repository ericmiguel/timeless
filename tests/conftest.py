def assert_datetime(
    d, year, month, day, hour=None, minute=None, second=None, microsecond=None
):
    assert year == d.year
    assert month == d.month
    assert day == d.day

    if hour is not None:
        assert hour == d.hour

    if minute is not None:
        assert minute == d.minute

    if second is not None:
        assert second == d.second

    if microsecond is not None:
        assert microsecond == d.microsecond
