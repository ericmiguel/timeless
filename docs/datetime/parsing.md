# Parsing

Under construction.


## Strings to datetime

Parse some strings to datetime:

```python
fill_date = timeless.datetime(2099, 2, 26, zone="UTC")
timeless.parse("1900", zone="America/Sao_Paulo", fill=fill_date)
```

## Datetime to string

Or get it as a ISO 8601 string or any other format:

```python
timeless.now().format()
timeless.now().format("%Y-%m-%d %H:%M:%S")
```
