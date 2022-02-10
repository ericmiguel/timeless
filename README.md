# Timeless - a datetime toolkit for people in a hurry.

**Timeless** sits on sholders of giants to provide a simple and easy to use datetime
toolkit. Simple date ranges, datetime operations and just one import.

This package is a work in progress and it was created as a study object.

## 🧠 Features

- ✔️ very simple API
- ✔️ minimal code to get things done
- ✔️ easy use with other packages
- ✔️ just one import
- ✔️ few dependencies

## 📦 Installation

```bash
pip install timeless
```

## 📝 Why Timeless?

It provides a simple API, heavily inspired by [Pendulum](https://github.com/sdispater/pendulum).

I love Pendulum, although since last year (maybe 2 years) it doesn't seem to be actively maintained. If you like Pendulum, you will like Timeless. If you want a easy to adopt, integrate and expand package, you will like Timeless.

## 💻 Sample usage

Timeless use two main concepts: `Datetime` and `Period`. A datetime is a point in Time, and a Period is a duration.

Timeless doesn`t differentiate between datetime and date objects.

All datetimes are assumed to be in the UTC+00:00 timezone if any other timezone isn`t specified.

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

## 📜 Docs

The docs are under development, but it's (very) early stage is already [available](https://ericmiguel.github.io/timeless/).

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
