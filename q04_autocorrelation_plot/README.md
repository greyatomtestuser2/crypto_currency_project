# Autocorrelation plot of Bitcoin prices

It is very important to check whether a time series is autocorrelated or not, before doing any further analysis. One of the ways to perform this check is to plot a `autocorrelation plot`. 

You can read on the following link to know how to interpret a autocorrelation plot
https://en.wikipedia.org/wiki/Correlogram

## Write a function `q04_autocorrelation_plot` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Plot the correlogram using `pandas.plotting.autocorrelation_plot()` for the `Close` column of the dataframe

Note: Include the line `plt.switch_backend('agg')` after the import statements

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
There is no return parameter for the function. The plot should be similar to https://github.com/commit-live-students/crypto_currency_project/blob/master/images/autocorrelation.png
