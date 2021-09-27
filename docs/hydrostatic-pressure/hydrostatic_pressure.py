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
        ) sd ON true where s.name='Pressure'
    ''',
    "postgresql://data_viewer:tokuapidemosystems@apidemo.tokusystems.com/new_mareland")

df_new = df.set_axis([
    'Asset name',
    'Hardpoint',
    'Signal name',
    'Last time',
    'Height'], axis=1, inplace=False)
print('Enter the specific gravity of the liquid in kg/m3: ')
user_input_specific_gravity = float(input())
g = 9.81
df_new['Height'] = df_new['Height']/(user_input_specific_gravity * g)
for index, row in df_new.iterrows():
    df_new.iloc[index, [4]] = row['Height']
    df_new.iloc[index, [3]] = pd.to_datetime(row['Last time'])

print(df_new.to_string(
    formatters={
        'Last time': lambda x: f'{pd.to_datetime(x,unit="D"):%X}',
        'Height': lambda x: f'{x:.5g}'
    }))
