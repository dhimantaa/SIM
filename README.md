SIM
--------

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


To use this package
----
```python
import sim
symbol='BOM500010'
startDate = '20170601'
endDate = '20190213'
```
```python
# To run the RSI simulation
df, param = sim.technical.rsi.Rsi(symbol=symbol).simulation(startDate=startDate,endDate=endDate)
# To plot the simulation
sim.plotter.Plotter(data=df, symbol=symbol,param=param).plot()
```
![alt text](https://raw.githubusercontent.com/dhimantaa/SIM/master/doc/rsi.png)
```python
# To run the Macd simulation
df, param = sim.technical.macd.Macd(symbol=symbol).simulation(startDate=startDate,endDate=endDate)
# To plot the Macd simulation
sim.plotter.Plotter(data=df, symbol=symbol,param=param).plot()
```
![alt text](https://raw.githubusercontent.com/dhimantaa/SIM/master/doc/macd.png)
