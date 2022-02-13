# Timeless

A datetime toolkit for people in a hurry.

**Timeless** sits on sholders of giants to provide a simple and easy to use datetime
toolkit. Simple date ranges, datetime operations and just one import.

This package is a work in progress and it was created as a study object.

## 🧠 Features

- ✔️ minimal code to get things done
- ✔️ easy use with other packages
- ✔️ one import, one syntax

## 📦 Installation

```bash
pip install timeless
```

## 📝 Why Timeless?

It provides a simple API, heavily inspired by [Pendulum](https://github.com/sdispater/pendulum).

I love Pendulum, although since last year (maybe 2 years) it doesn't seem to be actively maintained. If you like Pendulum, you will like Timeless. If you want a easy to adopt, integrate and expand package, you will like Timeless.

## 💻 Sample usage

Timeless use two main concepts: `Datetime` and `Period`.

- A datetime is a point in time
- A Period is a time range.

```py linenums="1" title="introduction/sample_usage.py"
--8<--
docs_src/introduction/sample_usage.py
--8<--
```

Remarks:

- Timeless doesn`t differentiate between datetime and date objects.
- All datetimes are assumed to be in the UTC if any other timezone is specified.
