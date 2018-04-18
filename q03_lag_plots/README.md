# Plot the lag plots for Bitcoin prices

It is very important to check whether a time series is random or not, before doing any further analysis. One of the ways to perform this check is to plot a `lag plot` and see whether it shows some pattern.Random data should not exhibit any identifiable structure in the lag plot. Non-random structure in the lag plot indicates that the underlying data are not random. 

You can read more on lag plots on http://www.statisticshowto.com/lag-plot/

## Write a function `q03_lag_plots` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Plot the lag using `pandas.plotting.lag_plot()`
- Customize the function to plot the lag plots for user specified number of lags

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|
| n_lags | integer | compulsory |  | User defined number of lags for which the plots are to be made|

### Returns:
There is no return parameter for the function. The plot should be similar to
https://github.com/commit-live-students/crypto_currency_project/blob/master/images/lag.png
