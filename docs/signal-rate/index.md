# Signal rate

Below is an example in python to get the rate of signal for all pressure signals.

```python
import pandas as pd

df = pd.read_sql(
    '''
        select sd.t ,sd.y
        from signal_data sd
        where signal_id = 125 and
        sd.t between '2021-09-12 12:00:00' and '2021-09-12 13:00:00'
        order by sd.t
    ''',
    "postgresql://data_viewer:tokuapidemosystems@apidemo.tokusystems.com/new_mareland")

df_new = df.set_axis(['Last time', 'Amplitude'], axis=1, inplace=False)
df_new['Last time'] = pd.to_numeric(pd.to_datetime(df_new['Last time']))/100_000_0000

output = []

for i in range(0, len(df_new)):
    if i > 0 and i < (len(df_new)-1):
        da = (df_new['Amplitude'][i+1]-df_new['Amplitude'][i-1])
        dt = (df_new['Last time'][i+1]-df_new['Last time'][i-1])
        signal_rate = da/dt
        output.append(signal_rate)
    else:
        output.append('NaN')
output = pd.DataFrame(output)
output.append(df_new['Last time'])
output = output.set_axis(['Signal Rate'], axis=1, inplace=False)
print(output)
```

- Line 8-15 is the SQL query to run
- Line 16 also has the connect string to the demo database
- Line 21 creates an empty list.
- Line 23-30 loops through each row and formats the results and adds it into
    the list.
- Line 32 loads the values onto a dataframe.
- Line 33 uses a heaader to name the column.
- Finally on line 34 the results are printed out.

[View on GitHub](https://github.com/TOKU-Systems/tutorials/blob/develop/docs/signal-rate/signal_rate.py)
