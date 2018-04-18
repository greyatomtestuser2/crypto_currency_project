# Plot the closing prices of Bitcoin

Now you have the historical prices of Bitcoin, let's start with exploring the data. 

## Write a function `q02_plot_closing_price` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Plot the closing prices of Bitcoin

Note: Include the line `plt.switch_backend('agg')` after the import statements

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
There is no return parameter for the function. 
The plot should be similar to https://github.com/commit-live-students/crypto_currency_project/blob/master/images/price_history.png

