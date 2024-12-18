# File: suggestions.py

import os
from pytrends.request import TrendReq
import pandas as pd

# Read input variables from environment variables
keyword = os.getenv('KEYWORD', 'pizza')

# Initialize Pytrends
pytrend = TrendReq()

# Get suggestions for a specific keyword
suggestions_dict = pytrend.suggestions(keyword=keyword)

# Print and save suggestions
suggestions_df = pd.DataFrame(suggestions_dict['suggestions'])
suggestions_df.to_csv('suggestions.csv')

print(suggestions_df.head())
