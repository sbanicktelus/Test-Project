# Daily Factoid

A simple Python script that retrieves interesting factoids about specific dates.

## Features

- Displays a random factoid about the current date when run without parameters
- Allows specifying a custom date using the `--date` parameter
- Shows help instructions when the `--help` parameter is used

## Data Sources

The script fetches factoids from online sources:
- Primary source: Wikipedia's "On This Day" API
- Fallback source: Numbers API

## Usage

```bash
# Get a factoid for today's date
python3 daily_factoid.py

# Get a factoid for a specific date
python3 daily_factoid.py --date "July 4"

# Display help instructions
python3 daily_factoid.py --help
```

## Requirements

- Python 3.x
- Internet connection (to fetch factoids from online sources)
