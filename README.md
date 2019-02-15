SIM
--------

To use this package
----
```
import SIM
symbol='BOM500010'
startDate = '20170601'
endDate = '20190213'
# To run the RSI simulation
df, param = SIM.rsi.Rsi(symbol=symbol).simulation(startDate=startDate,endDate=endDate)
# To plot the simulation
SIM.plotter.Plotter(data=df, symbol=symbol,param=param).plot()
# To run the Macd simulation
df, param = SIM.macd.Macd(symbol=symbol).simulation(startDate=startDate,endDate=endDate)
# To plot the Macd simulation
SIM.plotter.Plotter(data=df, symbol=symbol,param=param).plot()
```