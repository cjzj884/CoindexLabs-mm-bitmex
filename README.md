# Coindex
The goal of this project is to take advantage of API-driven trading available on BitMEX and other platforms, and execute automated trades based on indicator behavior from TradingView. 

This project is initially based off the sample Market Maker Bot available on the BitMEX Github, with additional code added to provide indication data from Tradingview, and additional code to execute more complex trading strategies and actions beyond basic market making.

# Features
This market maker bot operates just like the [sample BitMEX Market Maker bot](https://github.com/BitMEX/sample-market-maker) with some important key improvements:
* Get historical trade data from API in bulk
* Calculate moving averages over historical data to determine if it's time to trade
* Run (and perform averaging) on exact time intervals based on an aggression setting (1 min, 5 min, 1 hr, or 1 day)
* Ordering mode setting for short or long behavior 
* Create orders based on when the moving averages cross; order in the correct direction based on mode

## Next steps
See the [TODO](/TODO.md) file.
