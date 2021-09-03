# Hydrostatic pressure

This code is used to calculate the maximum height when the hydrostatic pressure 
of the fluid is known.

```python
import psycopg2
from math import log10, floor
from tabulate import tabulate
import datetime 

def round_sig(x, sig=5):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def height_calculation(pressure, acceleration_due_to_gravity, specific_gravity):
    height = pressure/(acceleration_due_to_gravity * specific_gravity)
    return height

try:
    conn = psycopg2.connect(host="apidemo.tokusystems.com",port="5432",dbname="tsdb",user="data_viewer",password="tokuapidemosystems")
    cur = conn.cursor()
    cur.execute('''
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
    where s.name='Pressure' 
    ''')
    query_results = cur.fetchall()
    print('Enter the specific gravity of the liquid in kg/m3: ')
    user_inputted_specific_gravity = float(input())
    g = 9.81
    formatted_results = []
    for row in query_results:
        newRow = []
        for value in row:
        
            height = 0.0
            if isinstance(value,float)and value!= 0.0 : 
                height = height_calculation(value, g, user_inputted_specific_gravity)    
                newRow.append(round_sig(height,5)) 
            elif isinstance(value,datetime.datetime):
                newRow.append( value.strftime('%c'))

            else:
                newRow.append(value)
        
        formatted_results.append(newRow)

    print(tabulate(formatted_results,headers=["Asset name","Hardpoint", "Signal name","Last Time","Last Height"]))
       
finally:    
    cur.close()
    conn.close()
    
```

- Line 11-12 is a function to get five significant figures
- Line 13-16 is a function to get the height
- Line 19 - 21 is to make a connection with the demo database
- Line 22-34 is the SQL query to run
- Line 34-35 take dynamic input of prssure
- Line 40-52 loops each row and appends therows to the new array, formatting
  Last-time column(locale format) and last column is the height.
- Line 56 prints the results
- In the end 58-60 closes the connection with the database

## Hydrostatic Pressure

As the name itself suggests, hydrostatic pressure is the pressure exerted by a
fluid (at rest) at equillibrium due to force of gravity.

<p align="center">
  <img width="460" height="300" src="https://media.sciencephoto.com/c0/41/57/64/c0415764-800px-wm.jpg">
</p>

## Properties of Hydrostatic Pressure

1. Acts at a right angle to the surface of the container holding the fluid

1. It is exerted in all directions equally to the sides of the container

## Quanitfying Hydrostatic Pressure

We know that Pressure is force exerted on unit area,

1. P = Force / Area

and similarly, Force is the product of mass and acceleration

1. F = mass * acceleration

in our case, acceleration is the acceleration due to gravity i.e.,g, hence the
equation can be modified as,

 F = mass * (acceleration due to gravity)

symbolically,

$$
F = m g , P = F / A
$$

Also we consider Density of the liquid which is the product of mass and volume,

Density = mass * Volume

symbolically,

$$
D = m / V
$$

- Upon combining the above  equations, we get

$$
  P = \rho g  h
$$

where P = pressure, r (rho) = specific gravity of the fluid, g = accelration due
to gravity and h = height of the fluid

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

- At Toku systems, highest grade equipments are employed which can withstand harsh
temperatures and weather conditions.

- To access the complete list of the specifications please visit
