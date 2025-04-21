# Daily Factoid

A simple Python script that retrieves interesting factoids about specific dates. This project is designed as a beginner-friendly example to illustrate vibe-coding concepts to non-developers.

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

## What is Vibe-Coding?

Vibe-coding is an approach to programming that focuses on creating a positive, enjoyable experience rather than strictly adhering to technical best practices. This project demonstrates vibe-coding principles by:

- Keeping the code simple and approachable for beginners
- Focusing on a fun, interesting output (historical factoids)
- Providing immediate satisfaction through quick results
- Using straightforward, readable code that non-developers can understand
- Creating something useful without unnecessary complexity

If you're new to programming, this project shows how a few lines of code can create something interesting and functional without needing to understand complex programming concepts.
