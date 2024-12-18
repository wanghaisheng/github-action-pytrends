# File: realtime_search_trends.py

import os
from pytrends.request import TrendReq
import pandas as pd

# Read input variables from environment variables
region = os.getenv('REGION', 'US')

# Initialize Pytrends
pytrend = TrendReq()

# Get realtime trending searches for a specific region
realtime_searches_df = pytrend.realtime_trending_searches(pn=region)

# Save to CSV
realtime_searches_df.to_csv('realtime_search_trends.csv')

print(realtime_searches_df.head())
