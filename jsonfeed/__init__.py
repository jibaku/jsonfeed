"""jsonfeed python package.

A wrapper around requests / json to handle JSON Feed
https://jsonfeed.org/
"""
import requests


def parse(url):
    """Parse the url and return json content."""
    return requests.get(url).json()
