#!/usr/bin/env python3
"""Uses the requests module to obtain the HTML content of
a particular URL and returns it."""
import redis
import requests

r = redis.Redis()


def get_page(url: str) -> str:
    """Track how many times a particular URL was accessed in the key
       "count:{url}" and cache the result with
       an expiration time of 10 seconds."""
    response = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, response.text)
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
