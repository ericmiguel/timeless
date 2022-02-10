# Pandas and Timeless

Who else loves Pandas? Timeless has some basic Pandas Timestamp compatibility methods.

```py linenums="1"
import pandas as pd

pd_timestamp = pd.Timestamp('1900-01-01 00:00:00', tz=None)
pd_daterange = pd.date_range(pd_timestamp, periods=2, freq="MS")

timeless.from_pandas(pd_timestamp)
timeless.from_pandas(pd_daterange)

timeless.to_pandas(period_1)
```

Note that only the main Pandas freqs are implemented: D, W, M, A/ Y, H, T/min, S and U/ US. Freqs like MS, AS and YS are coerced to months and years, respectively.
