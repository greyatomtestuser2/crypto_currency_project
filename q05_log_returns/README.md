# Calculate the log returns from Bitcoin prices

Now we are done with basic analysis, let us calculate the returns from the historical prices of Bitcoin. We will be calculate the log retruns.

Go through the following link to understand why we are calulcatin log returns instead of arithmatic returns
https://quantivity.wordpress.com/2011/02/21/why-log-returns/

## Write a function `q05_log_returns` that :
- Reads the previously stored csv file into a dataframe and assign the first column (`Date`) as `index`
- Calculate the log returns from the `Close` columns using the formula $$return = \log (\frac{p_t}{p_{t-1}})$$ ; Apply the transformation to the entire dataframe
- Drop the first row of the dataframe to remove 'nan' value
- Plot the `Close` column
- Return the transformed dataframe

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the stored csv file containing the Bitcoin historical price|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df | pd.DataFrame | DataFrame after performing the above operations|

