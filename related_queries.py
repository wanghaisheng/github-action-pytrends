# File: related_queries.py

import os
from pytrends.request import TrendReq
import pandas as pd

# Read input variables from environment variables
keywords = os.getenv('KEYWORDS', 'pizza,bagel').split(',')

# Initialize Pytrends
pytrend = TrendReq()

# Build payload
pytrend.build_payload(kw_list=keywords)

# Get related queries
related_queries_dict = pytrend.related_queries()

# Print and save related queries for each keyword
for keyword in keywords:
    related_queries_dict[keyword].to_csv(f'related_queries_{keyword}.csv')

print(related_queries_dict)
