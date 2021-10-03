# Latest readings

Below is an example in python to query for all latest readings.

```python
import pandas as pd

df = pd.read_sql(
    '''
    SELECT a.name, h.name, s.name, sd.t, sd.y
    FROM assets a
    JOIN hardpoints h ON a.id = h.asset_id
    JOIN signals s ON h.id = s.hardpoint_id
    JOIN LATERAL (
        SELECT x.t, x.y
        FROM signal_data x
        WHERE x.signal_id = s.id
        ORDER BY x.t DESC
        LIMIT 1
        ) sd ON true
    ''',
    "postgresql://data_viewer:tokuapidemosystems@apidemo.tokusystems.com/tsdb")
df_new = df.set_axis([
    'Asset name',
    'Hardpoint',
    'Signal name',
    'Last time',
    'Last reading'], axis=1, inplace=False)
for index, row in df_new.iterrows():
    df_new.iloc[index, [4]] = row['Last reading']
    df_new.iloc[index, [3]] = pd.to_datetime(row['Last time'])

print(df_new.to_string(
    formatters={
        'Last time': lambda x: f'{pd.to_datetime(x,unit="D"):%X}',
        'Last reading': lambda x: f'{x:.5g}'
    }))
```

- Line 3-16 is the SQL query to run.
- Line 17 also has the connect string to the demo database.
- Line 18-23 prints the dataframe with a header consisting the column names.
- Line 24-26 iterates through each row and locates the columns that need to be formatted.
- Line 28-32 prints the time column formatted in locale and readings formatted
to five significant digits.

[View on GitHub](https://github.com/TOKU-Systems/tutorials/blob/develop/docs/latest-readings/latest_readings.py)
