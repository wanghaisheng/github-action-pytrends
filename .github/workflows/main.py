name: Run Pytrends Scripts

on:
  workflow_dispatch:
    inputs:
      keywords:
        description: 'Keywords for pytrends (comma separated)'
        required: true
        default: 'pizza,bagel'
      region:
        description: 'Region for trending searches'
        required: true
        default: 'united_states'
      year:
        description: 'Year for top charts'
        required: true
        default: '2020'

jobs:
  run-pytrends:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytrends pandas

      - name: Set environment variables
        run: |
          echo "KEYWORDS=${{ github.event.inputs.keywords }}" >> $GITHUB_ENV
          echo "REGION=${{ github.event.inputs.region }}" >> $GITHUB_ENV
          echo "YEAR=${{ github.event.inputs.year }}" >> $GITHUB_ENV

      - name: Run interest_over_time.py
        run: |
          python interest_over_time.py

      - name: Run interest_by_region.py
        run: |
          python interest_by_region.py

      - name: Run related_queries.py
        run: |
          python related_queries.py

      - name: Run trending_searches.py
        run: |
          python trending_searches.py

      - name: Run realtime_search_trends.py
        run: |
          python realtime_search_trends.py

      - name: Run top_charts.py
        run: |
          python top_charts.py

      - name: Run suggestions.py
        run: |
          python suggestions.py
