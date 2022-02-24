# Datetime basics

Timeless dates and datetimes are represented by the `Datetime` class. It's the fundamental stone of the package. All Timeless objects are assumed to be UTC if any other timezone is specified.

```py linenums="1"
--8<--
docs_src/datetime/datetime_intro_1.py
--8<--
```

## Timezones

Note that Timeless make use of the standard module [zoneinfo](https://docs.python.org/3/library/zoneinfo.html) to handle timezones. Said that, you can set any system timezone you want or any other listed at [tzdata](https://pypi.org/project/tzdata/).

```py linenums="1"
--8<--
docs_src/datetime/timezones_1.py
--8<--
```

## Getting the current time

One can also use the convenience methods `now` and `today` to create a `Datetime` object. Since Timeless doesn't differentiate between datetime and date objects, `now` and `today` are almost equivalent, despite values other than day, month and year being zero on when using `today`.

```py linenums="1"
--8<--
docs_src/datetime/getting_the_current_time_1.py
--8<--
```

## Replacing object values

There are two ways to replace the values of a `Datetime` object.

If you just want to zero out hour, minute, second and microsecond, you can use the `set_zero` method.

```py linenums="1"
--8<--
docs_src/datetime/replacing_object_values_1.py
--8<--
```

However, if you want to replace other values of a `Datetime` object, you can use the `set` method.

```py linenums="1"
--8<--
docs_src/datetime/replacing_object_values_2.py
--8<--
```

## Timeless datetime and other time representations

Timeless offers a number of methods to convert a `Datetime` and `Period` objects to other time representations like Python's `datetime` module and even Pandas' `Timestamp` and `DateTimeIndex`. You can read more about these methods in the [converters](datetime.md) section.
