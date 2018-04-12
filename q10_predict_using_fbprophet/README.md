# Predict the price of bitcoin using fbprophet

Now as we are done with our analysis and finding different indicators, its time to predict the price of Bitcoin for next week. We will be using the fbprophet module developed by Facebook for thisp

Go through the quick start guide before starting the task : https://facebook.github.io/prophet/docs/quick_start.html

## Write a function `q10_predict_using_fbprophet` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Create a new dataframe `df_p` with columns as `ds` and `y` which will contain the dates and closing prices from original dataframe respectively (this is the defined input required for fbprophet)
- Predict the prices of Bitcoin using `Prophet` model. Set `dail_seasonality = False` in the model. Use `periods = 7` in `make_future_dataframe`.
- Plot the forecast using `Prohpet.plot()` method
- Return a pandas series of `yhat` column from forecast dataframe


### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| yhat | pandas.Series | Series containing the `yhat` column from forecast dataframe|

