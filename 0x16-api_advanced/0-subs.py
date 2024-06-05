#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    # Define the base URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set headers including a custom User-Agent
    # headers = {
    #     'User-Agent': 'Custom/0.1 (https://example.com)',
    # }

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the subscriber count from the data
            # The key 'data' contains the subreddit details,
            # and 'account_active' within it has the subscriber count
            subscriber_count = data['data']['subscribers']
            return subscriber_count
        else:
            # If the request was not successful, log the status code
            # print(f"Failed to fetch data: HTTP {response.status_code}")
            return 0
    except Exception as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return 0


# Example usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
