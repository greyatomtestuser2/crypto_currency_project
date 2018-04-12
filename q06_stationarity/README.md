# Test whether the Bitcoin price time series is stationary

Before applying any time series model we need to check whether a time series in stationary.
Read more on stationarity
http://www.statisticshowto.com/stationarity/

We will apply a ADF test to check stationarity https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test

## Write a function `q06_stationarity` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Apply `adfuller` test from `statsmodel` module to the `Close` column from dataframe

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| test_stat | float | Value of test statistic from ADF test|
| p_value | float | p-value for ADF test|

