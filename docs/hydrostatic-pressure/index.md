# Hydrostatic pressure

This code is used to calculate the maximum height when the hydrostatic pressure
of the fluid is known.

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
        ) sd ON true where s.name='Pressure' 
    ''',
    "postgresql://data_viewer:tokuapidemosystems@apidemo.tokusystems.com/tsdb")

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

```

- Line 11-12 is a function to get five significant figures
- Line 13-16 is a function to get the height
- Line 19 - 21 is to make a connection with the demo database
- Line 22-34 is the SQL query to run
- Line 34-35 take dynamic input of prssure
- Line 40-52 loops each row and appends therows to the new array, formatting
  Last-time column(locale format) and the last column is the height.
- Line 56 prints the results
- In the end 58-60 closes the connection with the database

[View on Github.com](https://github.com/TOKU-Systems/tutorials/blob/develop/docs/hydrostatic-pressure/hydrostatic_pressure.py)

## Hydrostatic Pressure

As the name itself suggests, hydrostatic pressure is the pressure exerted by a
fluid (at rest) at equillibrium due to force of gravity.

<p align="center">
  <img width="460" height="300" src="https://chemistrygod.com/assets/media/image/hydrostatic-pressure-a-closed-container.png">
</p>

## Properties of Hydrostatic Pressure

1. Acts at a right angle to the surface of the container holding the fluid

1. It is exerted in all directions equally to the sides of the container

## Quanitfying Hydrostatic Pressure

We know that Pressure is force exerted on unit area,

$P = \frac{\text{Force}}{\text{Area}}$

and similarly, Force is the product of mass and acceleration

$F = mass * Acceleration$

in our case, acceleration is the acceleration due to gravity i.e.,g, hence the
equation can be modified as,

$$
F = mass * (acceleration\ due\ to\ gravity)
$$

symbolically,

$$
F = m g
$$

$$
P = F / A
$$

Also we consider Density of the liquid which is the product of mass and volume,

$Density = mass * Volume$

symbolically,

$$
D = m / V
$$

- Upon combining the above  equations, we get

$$
  P = \rho g  h
$$

Where

$P = pressure$

$\rho = specific\ gravity \ of \ the \ fluid$

$g = acceleration\ due\ to\ gravity$

$h = height\ of\ the\ fluid$

<p align="center">
  <img width="460" height="300" src="https://o.quizlet.com/MaIx7LqHSAVPoFcPNH28ng.png">
</p>
  
### Why calculate the height of the fluid?
  
 - If we know the specific gravity of the fluid and the pressure exerted by the
 liquid we can calculate the maximum height of the fluid
 that can be allowed.

 - We can avoid the occurence of any hazardous effects in the surroundings or to
 the equipment itself.

 The height can be calculated as

$$
 h = P / (\rho * g)
$$

### Specification sheet

- At TOKU Systems, highest grade equipments are employed which can withstand harsh
temperatures and weather conditions.

- To access the complete list of the specifications please visit

[Download the specifications](https://tokuindustry.com/wp-content/uploads/2020/07/Specifications-July-9-2020.pdf)
