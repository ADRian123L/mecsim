'''This program prompt the year and return the name of 
the year.
'''

import requests
import json
import getpass
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

# List of chinese years:
chinese_year_names = ('Rat','Ox','Tiger','Rabbit','Dragon','Snake',
                      'Horse','Goat','Monkey','Rooster','Dog','Pig')

# URL:
URL: str = "https://api.github.com"

# Using an API:
def api(run=False) -> None:
    if (run):
        try:
            # Requests to a server:
            response = requests.get(url=URL, params={'q': 'requests+language:python'})
            # Raises any errors:
            response.raise_for_status
        except HTTPError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Couldn't open server: {error}")
        else:
            print(f"Success: {response.status_code}")
            print(f"Server: {response.headers['Server']}")
            print(f"Date: {response.headers['Date']}")
            print(f"Content: {response.headers['content-type']}")
    return None

# Using Json:
def j_file(info : list, run=False) -> json:
    if (run):
        try:
            with open ("json_file.json", "w") as text:
                json.dump(info, text, indent=4)
        except Exception as error:
            print(f"Couldn't open the file: {error}")

def json_read(run=False) -> list:
    if (run):
        with open("json_file.json", "r") as text:
            info = json.load(text)
        return info



if __name__ == "__main__":
    api(run=True)
    new_file = j_file(chinese_year_names,run=False)
    info = json_read()