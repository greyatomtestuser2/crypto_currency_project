# Calculate and plot 20day and 100day moving average

Moving averages are one of the indicators used to predict the prices from a time series. In this task you will be calculating a short term moving average (20days) and a long term moving average (100days) and plot it along with the historical closing price of Bitcoin.

Read more here : https://www.investopedia.com/university/movingaverage/movingaverages1.asp

## Write a function `q08_moving_average` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Calculate the 20day moving average of `Close` column using `DataFrame.rolling()` function and store the value to a new column names `20d` in the existing dataframe. (Pay attention that you need to calulate the mean of the rolling series obtained using `DataFrame.rolling()`)
- Calculate the 100day moving average of `Close` column using `DataFrame.rolling()` function and store the value to a new column names `100d` in the existing dataframe. (Pay attention that you need to calulate the mean of the rolling series obtained using `DataFrame.rolling()`)
- Plot the `Close`, `20d` and `100d` time series on one plot
- Return the dataframe

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df | pandas.DataFrame | return the dataframe after performing above operations|


`use center = False argument in DataFrame.rolling()`