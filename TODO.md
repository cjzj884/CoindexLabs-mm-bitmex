# TODO

## Bot code base
* [Reconfigure order pattern to more heavily favor the price indicated by analysis](#1)
* Update a graph per iteration run showing the data it's using for analysis
* Persist settings to database so not dependent on config files

## DevOps
* Deploy bot to cloud compute instances
* Multi-bot deploy where bots can be started and stopped via database control

## High-Level Roadmap
[Roadmap Documentation](https://docs.google.com/document/d/1B2ExBDF5tEURjI19bCUmllr8HaYMCWlNhBi7Y1iX_u8/edit?usp=sharing)
### 0.0 - Alpha (Current)
* 0.1 ROE trigger functionality
   * RoE or Return on Equity is a calculated as: 
      * % nominal profit of the margin applied to a given position. It represents a function of position leverage and position PnL.
   * Triggers for RoE will typically be limit based
      * IE: RoE > or < X amount = trigger
         * RoE > 40% = take profit trade 
         * Roe < -10% = stop loss trade
* 0.2 MACD calculations and trigger functionality
   * MACD or Moving Average Convergence Divergence is calculated as: 
      * X = 12-period EMA of price
         * (potentially want to make this period adjustable) 
      * Y = 26-period EMA of price 
         * (potentially want to make this period adjustable)
      * A = X - Y
      * B = a nine-period EMA of A
         * (potentially want to make this period adjustable)
   * Triggers for MACD will typically be based on crossovers or dramatic reversals
      * MACD rises above the signal line = buy bias, buy trade 
         * A > B = buy order for 2% available margin balance at 5x leverage 
      * MACD falls below the signal line = sell bias, sell trade
         * A < B = sell order for 2% available margin balance at 5x leverage 
      * Dramatic rise upward = overbought, dramatic reversal incoming
         * A - B > F = exit long position
         * A - B > F = sell order for 2% available balance at 25x leverage
      * Dramatic fall downward = oversold, dramatic reversal incoming
         * B - A > F = exit short position
         * B - A > F = buy order for 2% available balance at 25x leverage
* 0.3 RSI calculations and trigger functionality 
   * RSI or Relative Strength Index is calculated as:
      *  RSI = 100 - (100 / (1 + RS))
      * RS = Average Gain / Average Loss (losses expressed as positive values)
      * 1st average gain and average loss = simple 14-period averages.
         * First Average Gain = Sum of Gains over the past 14 periods / 14
         * First Average Loss = Sum of Losses over the past 14 periods / 14
      * 2nd, and subsequent, calculations are based on prior averages and the current gain loss:
         * Average Gain = [(previous Average Gain) x 13 + current Gain] / 14
         * Average Loss = [(previous Average Loss) x 13 + current Loss] / 14
      * Triggers for RSI will typically be based on limits or reversals
         * RSI rises above the upper limit = overbought bias, sell trade 
                * RSI > X = sell order for 2% available margin balance at 5x leverage (X = 70 default) 
         * RSI falls below the lower limit = oversold bias, buy trade
                * RSI < Y = buy order for 2% available margin balance at 5x leverage (Y = 30 default)
         * RSI moves downward after Z or more periods trending upward
                * Trigger = exit long position
                * Trigger = sell order for 2% available balance at 25x leverage
         * RSI moves upward after Z or more periods trending downward
                * Trigger = exit short position
                * Trigger = buy order for 2% available balance at 25x leverage
* 0.4 VWAP calculations and trigger functionality 
* 0.5 OBV calculations and trigger functionality 
* 0.6 Ichimoku calculations and trigger functionality
* 0.7 Multiple trigger toggling
* 0.8 DevOps migration to AWS 
* 0.9 Security infrastructure

### 1.0 - Beta (Year Goal)
* 1.1 Multiple strategy management
* 1.2 Front end interface integration
* 1.3 Licensing and access
* 1.4 Account creation and management
* 1.5 Strategy templating

### 2.0 - Mu (Future State)
* 2.1 Deribit Integration
* 2.2 1Broker Integration (+1Fox Integration)
* 2.3 Bittrex Integration
* 2.4 Binance Integration
* 2.5 Multi-coin analysis
* 2.6 Multi-coin cross comparison
* 2.7 Multi-coin strategy management
* 2.8 Strategy comparison analysis
* 2.9 Strategy learning module
    
