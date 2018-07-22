# TODO

## Bot code base
* Ensure that short and long behavior also closes orders instead of just open them
* Make exponential moving average calculation more consistent for last step
* Cache the prices received from the API in memory to speed up analysis and decrease API queries
* Cache past moving average calculations to speed up analysis
* Persist data about open orders
* Analyze past orders to show profitability
* Persist settings so not dependent on config files
* Web admin site for changing bot settings and viewing progress

## DevOps
* Deploy bot to cloud compute instances
* Multi-bot deploy where bots can be started and stopped via database control
