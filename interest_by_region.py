# File: interest_by_region.py

import os
from pytrends.request import TrendReq
import pandas as pd

# Read input variables from environment variables
keywords = os.getenv('KEYWORDS', 'pizza,bagel').split(',')

# Initialize Pytrends
pytrend = TrendReq()

# Build payload
pytrend.build_payload(kw_list=keywords)

# Get interest by region
interest_by_region_df = pytrend.interest_by_region()

# Save to CSV
interest_by_region_df.to_csv('interest_by_region.csv')

print(interest_by_region_df.head())
