# Timeless: datetime for people in a hurry

A datetime toolkit for people in a hurry. It provides a simple API, heavily inspired by [Pendulum](https://github.com/sdispater/pendulum).

Timeless is a work in progress.

## 🧠 Features

- ✔️ very simple API
- ✔️ easy to extend and use with other packages
- ✔️ built on top of standard packages and [dateutil](https://github.com/dateutil/dateutil)

## 📦 Installation

```bash
pip install timeless
```

## 📝 Why Timeless?

I love Pendulum, although since last year it doesn't seem to be actively maintained. If you like Pendulum, you will like Timeless. If you want a easy to adopt, integrate and expand package, you will like Timeless.

## 💻 Examples of usage

Timeless use two main concepts: `Datetime` and `Period`. A datetime is a point in Time, and a Period is a duration.

Timeless doesn`t differentiate between datetime and date objects.

All datetimes are assumed to be in the UTC+00:00 timezone if any other timezone isn`t specified.

---

### Datetime

```python
import timeless

start = timeless.datetime(1900, 1, 1, zone="UTC")
end = start.add(years=1)

end.subtract(months=1)

start.set(year=2099, month=2, day=26, hour=5, zone="America/Sao_Paulo")

start.is_past()  # True
start.is_future()  # False
start.set(year=2099).is_future()  # True
```

Surely, you can get the current time:

```python
timeless.today()
timeless.now()
```

Timeless heavily uses [dateutil](https://github.com/dateutil/dateutil). The difference between two dates gives you a relativedelta object:

```python
start.diff(end)
```

### Periods

Create a date range with `Period`:

```python
period_1 = timeless.period(start, end, freq="days")
period_2 = period_1.compute()
```

Periods are always yielded. Use compute or just list(period) to get the list of datetimes.

To easily change the frequency of a date range, use `to`:

```python
period_1.to("hours")
```

### Using Timeless and Pandas

Who else loves Pandas? The ones who says doens`t like Pandas probabily never used it for real. Timeless has some basic Pandas Timestamp compatibility methods.

```python
import pandas as pd

pd_timestamp = pd.Timestamp('1900-01-01 00:00:00', tz=None)
pd_daterange = pd.date_range(pd_timestamp, periods=2, freq="MS")

timeless.from_pandas(pd_timestamp)
timeless.from_pandas(pd_daterange)

timeless.to_pandas(period_1)
```

Note that only the main Pandas freqs are implemented: D, W, M, A/ Y, H, T/min, S and U/ US. Freqs like MS, AS and YS are coerced to months and years, respectively.

### Utilitaries

Parse some strings to datetime:

```python
fill_date = timeless.datetime(2099, 2, 26, zone="UTC")
timeless.parse("1900", zone="America/Sao_Paulo", fill=fill_date)
```

Or get it as a ISO 8601 string or any other format:

```python
timeless.now().format()
timeless.now().format("%Y-%m-%d %H:%M:%S")
```

Or find the next friday!

```python
timeless.now().get_next("friday")
```

Timeless tries to be as flexible as possible. You can create some quite cool chain operations easily:

```python
timeless.period(start, end.add(days=7), freq="days").to("weeks").compute()
```

## 🏗️ Development

Timeless relies on [Poetry](https://github.com/python-poetry/poetry).

Install the Python dependencies with:

```bash
poetry install
```

## ⚗️ Testing

```bash
poetry run pytest --cov=timeless tests/
```
