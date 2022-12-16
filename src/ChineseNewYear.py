'''This program prompt the year and return the name of 
the year.
'''

import requests
import json

chinese_year_names = ('Rat','Ox','Tiger','Rabbit','Dragon','Snake',
                      'Horse','Goat','Monkey','Rooster','Dog','Pig')

# Using an API:
def api(run=False) -> None:
    if (run):
        response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
    return None

# Using Json:
def j_file(info : list, run=False) -> json:
    if (run):
        file = json.dumps(info, indent=4)
        return file

if __name__ == "__main__":
    api()
    new_file = j_file( chinese_year_names,run=True)
    print(new_file)
