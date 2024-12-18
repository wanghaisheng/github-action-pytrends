# File: top_charts.py

import os
from pytrends.request import TrendReq
import pandas as pd

# Read input variables from environment variables
year = os.getenv('YEAR', '2018')
region = os.getenv('REGION', 'GLOBAL')

# Initialize Pytrends
pytrend = TrendReq()

# Get top charts data for a specific year
top_charts_df = pytrend.top_charts(year, hl='en-US', tz=300, geo=region)

# Save to CSV
top_charts_df.to_csv('top_charts.csv')

print(top_charts_df.head())
