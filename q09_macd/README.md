# Calculate and plot MACD

Moving Average Convergence Divergence (MACD) is one of the frequently used technical indicators. MACD signals whether to buy or sell an asset. In this task you will calculate MACD for Bitcoin prices and plot the same.

Read more here : https://www.investopedia.com/terms/m/macd.asp

## Write a function `q09_macd` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Calculate the 12day exponential moving average of `Close` column using `Series.ewm()` function and store the value to a new column names `12ema` in the existing dataframe. (Pay attention that you need to calulate the mean of the exponential rolling series obtained using `Series.ewm()`)
- Calculate the 26day exponential moving average of `Close` column using `Series.ewm()` function and store the value to a new column names `26ema` in the existing dataframe. (Pay attention that you need to calulate the mean of the exponential rolling series obtained using `Series.ewm()`)
- Calculate the 9day exponential moving average of `Close` column using `Series.ewm()` function and store the value to a new column names `signal` in the existing dataframe. (Pay attention that you need to calulate the mean of the exponential rolling series obtained using `Series.ewm()`)
- Calulate the difference between columns `12ema` and `26ema` and store the same in new column `macd`
- Plot the `Close`, `macd` and `signal` time series on one plot
- Return the dataframe

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df | pandas.DataFrame | return the dataframe after performing above operations|
The plot should be similar to https://github.com/commit-live-students/crypto_currency_project/blob/master/images/macd.png

`use adjust = False argument in Series.ewm()`
