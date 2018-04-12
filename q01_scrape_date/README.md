# Scrape data from web, process data and save to a csv file

Before starting the analysis we need to scrape the web for extracting the Bitcoin historical prices time series.

This exercise is split into three parts. 
 - Scrape the data and save to dataframe
 - Process the data in dataframe as per the requirements of the study
 - Save the processed dataframe to a csv file
  

## Write a function `q01_scrape_date` that :
- Scrape the given url using `pandas.read_html()`. You will get a list of which you need to extract the first element to get a dataframe. Store it in a dataframe
- Change the `Date` column to `datetime` format using `pandas.to_datetime()`
- Sort the `Date` column in ascending order
- Save the processed dataframe to a `csv` file, the location to store the file should be `./data/bitcoin.csv`

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| url | string | compulsory |  | Path to the website for scraping bitcoin prices|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df | pd.DataFrame | DataFrame after performing the above operations|

`url = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170101&end=20180401'`