import os
from pytrends.request import TrendReq
import pandas as pd

# Read input variables from environment variables
keywords = os.getenv('KEYWORDS', 'pizza,bagel').split(',')
region = os.getenv('REGION', 'united_states')
start_date = os.getenv('START_DATE', '2020-01-01')
end_date = os.getenv('END_DATE', '2021-01-01')
timeframe = f'{start_date} {end_date}'  # Format as 'YYYY-MM-DD YYYY-MM-DD'

# Initialize Pytrends
pytrend = TrendReq()

# Build payload with the additional parameters
pytrend.build_payload(kw_list=keywords, geo=region, timeframe=timeframe)

# Get interest over time
interest_over_time_df = pytrend.interest_over_time()

# Check if the dataframe is empty (i.e., no data)
if interest_over_time_df.empty:
    print(f"No data available for the keywords {keywords} in the region {region} between {start_date} and {end_date}.")
else:
    # Save to CSV
    interest_over_time_df.to_csv('interest_over_time.csv')

    # Print the first few rows of the dataframe for preview
    print(interest_over_time_df.head())
