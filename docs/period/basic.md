# Periods basics

Create a date range with `Period`:

```python
period_1 = timeless.period(start, end, freq="days")
```

To easily change the frequency of a date range, use `to`:

```python
period_1.to("hours")
```
