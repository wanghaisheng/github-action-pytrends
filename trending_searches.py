# File: trending_searches.py

import os
from pytrends.request import TrendReq
import pandas as pd

# Read input variables from environment variables
region = os.getenv('REGION', 'united_states')

# Initialize Pytrends
pytrend = TrendReq()

# Get trending searches for a specific region
trending_searches_df = pytrend.trending_searches(pn=region)

# Save to CSV
trending_searches_df.to_csv('trending_searches.csv')

print(trending_searches_df.head())
