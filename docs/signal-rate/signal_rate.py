import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_sql(
    '''
        select sd.t,sd.y
        from signal_data sd
        where signal_id = 125 and
        sd.t between '2021-09-12 12:00:00' and '2021-09-12 13:00:00'
        order by sd.t
''',
    "postgresql://data_viewer:tokuapidemosystems@apidemo.tokusystems.com/new_mareland")

df_new = df.set_axis(['Last time', 'Amplitude'], axis=1, inplace=False)

df_new['Last time'] = df_new['Last time'].astype(str)

print(df_new)

timeline = pd.to_datetime(df_new['Last time'])
recv = pd.Series(df_new['Amplitude'].array, timeline.array)
output = (recv.diff() / (recv.index.to_series().diff().dt.total_seconds()))
print(output)
