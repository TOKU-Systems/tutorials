# Fourier analysis on the pressure signals

This is a python code to get the pressure signals in a time period of 60 minutes
and perform fourier transform on them and view their respective wave forms.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_sql(
    '''
    select sd.t,sd.y
    from signal_data sd
    where signal_id = 125 and
    sd.t between '2021-08-30 12:00:00' and '2021-08-30 13:00:00'
    order by sd.t
    ''',
    "postgresql://data_viewer:tokuapidemosystems@apidemo.tokusystems.com/tsdb")

df_new = df.set_axis(['Last time', 'Amplitude'], axis=1, inplace=False)
print(df_new)

plt.subplot(1, 2, 1)
plt.plot('Last time', 'Amplitude', data=df_new)
plt.title('Time signal')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.subplot(1, 2, 2)
sp1 = np.fft.fft(df_new['Amplitude'])
freq1 = np.fft.fftfreq(df_new['Last time'].shape[-1])
fourier_signal = pd.DataFrame(dict(
    frequency=freq1, spectrum=sp1)).reset_index()
print(fourier_signal)
plt.plot(freq1, sp1.real, freq1, sp1.imag)
plt.title('fourier signal')
plt.xlabel('w')
plt.ylabel('f(w)')
plt.show()
```

- Line 4-11 is the SQL query to run.
- Line 14-15 is to print the data (pressure signals) with a header.
- Line 17-21 is to sub-plot the time signal in figure1.
- Line 23-26 is the the fourier transforme of the time signal.
- Line 27 prints the values of the fourier transform.
- Line 28-32 subplots the fourier transformed signal in the same figure.

[View on GitHub](https://github.com/TOKU-Systems/tutorials/tree/develop/docs/fourier-transform)

An example plot is given below

<p align="center">
  <img width="460" height="300" src="https://raw.githubusercontent.com/TOKU-Systems/tutorials/develop/docs/Fourier%20plot/Figure_1.png">
</p>
