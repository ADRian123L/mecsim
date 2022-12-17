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
        with open ("json_file.json", "w") as text:
            json.dump(info, text, indent=4)

def json_read() -> list:
    with open("json_file.json", "r") as text:
        info = json.load(text)
    return info



if __name__ == "__main__":
    api()
    new_file = j_file(chinese_year_names,run=False)
    info = json_read()
    print(info)

    
