import pytest
import timeless


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, (1976, 1977)), (0, (1975, 1976)), (-1, (1974, 1975))],
)
def test_shift_years(offset_value, expected_result):
    obj = timeless.period("1975-12-01", "1976-01-01").shift(years=offset_value)
    assert obj.start.year == expected_result[0]
    assert obj.end.year == expected_result[1]


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, (2, 3)), (0, (1, 2)), (-1, (12, 1))],
)
def test_shift_months(offset_value, expected_result):
    obj = timeless.period("1975-01-01", "1975-02-01").shift(months=offset_value)
    assert obj.start.month == expected_result[0]
    assert obj.end.month == expected_result[1]


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, (2, 3)), (0, (1, 2)), (-1, (31, 1))],
)
def test_shift_days(offset_value, expected_result):
    obj = timeless.period("1975-01-01", "1975-02-02").shift(days=offset_value)
    assert obj.start.day == expected_result[0]
    assert obj.end.day == expected_result[1]


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, (2, 13)), (0, (1, 12)), (-1, (0, 11))],
)
def test_shift_hours(offset_value, expected_result):
    obj = timeless.period("1975-01-01 01", "1975-01-02 12", freq="hours").shift(
        hours=offset_value
    )
    assert obj.start.hour == expected_result[0]
    assert obj.end.hour == expected_result[1]


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, (10, 11)), (0, (9, 10)), (-1, (8, 9))],
)
def test_shift_minutes(offset_value, expected_result):
    obj = timeless.period("1975-01-01 01:09", "1975-01-01 01:10", freq="minutes").shift(
        minutes=offset_value
    )
    assert obj.start.minute == expected_result[0]
    assert obj.end.minute == expected_result[1]


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, (2, 3)), (0, (1, 2)), (-1, (0, 1))],
)
def test_shift_seconds(offset_value, expected_result):
    obj = timeless.period(
        "1975-01-01 01:10:01", "1975-01-01 01:10:02", freq="seconds"
    ).shift(seconds=offset_value)
    assert obj.start.second == expected_result[0]
    assert obj.end.second == expected_result[1]
