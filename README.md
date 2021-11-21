# Timeless: datetime for people in a hurry

Timeless is a datetime simple toolkit for people in a hurry. It provides a simple API, heavily inspired by [Pendulum](https://github.com/sdispater/pendulum).

## 🧠 Features

- ✔️ very simple API
- ✔️ few dependencies
- 🔨 probably will be more actively maintained than Pendulum

## 💻 Examples of usage

Timeless use two main concepts: `Datetime` and `Period`. A datetime is a point in time, and a period is a duration.

Timeless does`t differentiate between a datetime and date.

All datetimes are explicit considered to be in the UTC+00:00 timezone if not any other timezone name is specified.

---

Basic usage:

```python
import timeless

start = timeless.datetime(1900, 1, 1, zone="UTC")
# Datetime(1900, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))

end = start.add(years=1)
# Datetime(1901, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))

end.subtract(months=1)
# Datetime(1900, 12, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
```

Datetime utility methods:

```python
start = timeless.datetime(1900, 1, 1, zone="UTC")

start.set(year=2099, month=2, day=26, hour=5, zone="America/Sao_Paulo")
# Datetime(2099, 2, 26, 5, 0, tzinfo=zoneinfo.ZoneInfo(key='America/Sao_Paulo'))

start.is_future()  # False

start.set(year=2099).is_future()  # True
```

Create a date range:

```python
start = timeless.datetime(1900, 1, 1, zone="UTC")
end = start.add(months=2)

list(timeless.period(start, end, freq="months"))
""" 
[Datetime(1900, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
 Datetime(1900, 2, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
 Datetime(1900, 3, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))]
"""
```

Change the frequency of a date range:

```python
start = timeless.datetime(1900, 1, 1, zone="UTC")
end = start.add(days=1)

period_1 = timeless.period(start, end, freq="days")
period_2 = period_1.to("hours")

list(period_1)
""" 
[Datetime(1900, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
 Datetime(1900, 1, 2, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))]
"""

list(period_2)
"""
[Datetime(1900, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
 Datetime(1900, 1, 1, 1, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
...
 Datetime(1900, 1, 1, 23, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
 Datetime(1900, 1, 2, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))]
"""
```

## 🏗️ Development

Botree relies on [Poetry](https://github.com/python-poetry/poetry).

Install the Python dependencies with:

```bash
poetry install
```

## ⚗️ Testing

```bash
poetry run pytest --cov=botree tests/
```
