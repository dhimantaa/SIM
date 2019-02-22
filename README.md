SIM
--------

[![Build Status](https://travis-ci.com/dhimantaa/SIM.svg?branch=master)](https://travis-ci.com/dhimantaa/SIM)


Installation
--------
```bash
git clone https://github.com/dhimantaa/SIM.git
cd SIM
pip install .
```

OR
--------
```bash
cd SIM
```
```python
python setup.py install
```


How to use this package
----
```python
import sim
symbol = 'BOM500003'
```
```python
# To run the RSI simulation
df, param = sim.technical.rsi.Rsi(symbol=symbol).simulation(startDate='20171201', endDate='20190212')
# To plot the simulation
sim.plotter.Plotter(data=df,symbol=symbol, param=param).plot()
```
![alt text](https://raw.githubusercontent.com/dhimantaa/SIM/master/doc/rsi.png)
```python
# To run the Macd simulation
df, param = sim.technical.macd.Macd(symbol=symbol).simulation(startDate='20171201', endDate='20190215')
# To plot the Macd simulation
sim.plotter.Plotter(data=df,symbol=symbol, param=param).plot()
```
![alt text](https://raw.githubusercontent.com/dhimantaa/SIM/master/doc/macd.png)
```python
# To run the Bollinger simulation
df, param = sim.technical.bollinger.Bollinger(symbol=symbol).simulation(startDate='20171201', endDate='20190215')
# To plot the Bollinger simulation
sim.plotter.Plotter(data=df,symbol=symbol, param=param).plot()
```
![alt text](https://raw.githubusercontent.com/dhimantaa/SIM/master/doc/bollinger.png)
