# Make the time series stationary

In the previous task we applied the ADF test and found that the time series of Bitcoin prices is non stationary. There are various ways in which you can convert a non stationary time series to stationary. We will make us of log transformation and differencing method for the same.

Read more here : https://www.otexts.org/fpp/8/1

## Write a function `q07_make_stationary` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Add a cloumn `lClose` to the existing dataframe and store the log values of `Close` column in the same
- Calculate the moving average of `lClose` column using `pandas.rolling_mean()` with `window=12` and store in series called `moving_avg`
- Add a column `sClose` to the existing dataframe and store the difference between `lClose` and `moving_avg`
- Return the dataframe

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df | pandas.DataFrame | return the dataframe after performing above operations|


