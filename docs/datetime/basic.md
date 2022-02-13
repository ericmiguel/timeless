# Datetime basics

Timeless dates and datetimes are represented by the `Datetime` type. It's the fundamental piece of the package.

```py linenums="1"
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

```py linenums="1"
timeless.today()
timeless.now()
```

Timeless heavily uses [dateutil](https://github.com/dateutil/dateutil). The difference between two dates gives you a relativedelta object:

```py linenums="1"
start.diff(end)
```
