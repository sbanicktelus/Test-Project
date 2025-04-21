#!/usr/bin/env python3
import argparse
import datetime
import sys
import urllib.request
import urllib.error
import json
import random

def get_current_date():
    """Return the current date as a tuple of (month_num, day)"""
    today = datetime.datetime.now()
    return (today.month, today.day)

def parse_date(date_str):
    """Parse a date string into a tuple of (month_num, day)"""
    try:
        # Try to parse the date string (expecting format like "April 21" or "04/21")
        date_formats = ["%B %d", "%b %d", "%m/%d"]
        parsed_date = None
        
        for fmt in date_formats:
            try:
                parsed_date = datetime.datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        
        if parsed_date is None:
            print(f"Error: Could not parse date '{date_str}'. Please use format like 'April 21' or '04/21'.")
            sys.exit(1)
        
        # Return month number and day
        return (parsed_date.month, parsed_date.day)
    except Exception as e:
        print(f"Error parsing date: {e}")
        sys.exit(1)

def get_factoid_from_numbers_api(month, day):
    """Get a factoid from the Numbers API for the given month and day"""
    try:
        # Format the URL for the Numbers API
        url = f"http://numbersapi.com/{month}/{day}/date"
        
        # Make the request
        with urllib.request.urlopen(url) as response:
            fact = response.read().decode('utf-8')
            # Convert month number to month name for display
            month_name = datetime.date(1900, month, 1).strftime('%B')
            return f"On this day ({month_name} {day}): {fact}"
    except urllib.error.URLError as e:
        return f"Error retrieving factoid from Numbers API: {e}"

def get_factoid_from_wikipedia(month, day):
    """Get a factoid from Wikipedia's On This Day API for the given month and day"""
    try:
        # Convert month number to month name
        month_name = datetime.date(1900, month, 1).strftime('%B')
        
        # Format the URL for the Wikipedia API
        url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{month}/{day}"
        
        # Set up the request with a user agent
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'DailyFactoidScript/1.0'}
        )
        
        # Make the request
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            events = data.get('events', [])
            
            if not events:
                return f"No historical events found for {month_name} {day}."
            
            # Select a random event
            event = random.choice(events)
            year = event.get('year', 'Unknown year')
            text = event.get('text', 'No description available.')
            
            return f"On this day ({month_name} {day}) in {year}: {text}"
    except urllib.error.URLError as e:
        # If Wikipedia API fails, try the Numbers API as a fallback
        return get_factoid_from_numbers_api(month, day)
    except json.JSONDecodeError as e:
        # If JSON parsing fails, try the Numbers API as a fallback
        return get_factoid_from_numbers_api(month, day)
    except Exception as e:
        # For any other error, try the Numbers API as a fallback
        return get_factoid_from_numbers_api(month, day)

def get_factoid(month, day):
    """Get a factoid for the given month and day, trying multiple sources"""
    # Try Wikipedia first, with Numbers API as fallback
    return get_factoid_from_wikipedia(month, day)

def main():
    """Main function to parse arguments and display factoid"""
    parser = argparse.ArgumentParser(description='Display an interesting factoid about a specific date.')
    parser.add_argument('--date', help='Specify a date (e.g., "April 21" or "04/21")')
    
    args = parser.parse_args()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        parser.print_help()
        sys.exit(0)
    
    if args.date:
        month, day = parse_date(args.date)
    else:
        month, day = get_current_date()
    
    factoid = get_factoid(month, day)
    print(factoid)

if __name__ == "__main__":
    main()
