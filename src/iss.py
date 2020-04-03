"""
Learning about the ISS
Date: 02/04/20
Author: Will

Code copied from a Raspberry Pi Project:
https://github.com/RaspberryPiLearning/where-is-the-space-station
"""

import json
import urllib.request
import time

# Who is in space right now?
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

number = result['number']
print(f"People in Space: {number}")
print()

people = result['people']
for person in people:
    name = person['name']
    craft = person['craft']
    print(f"{name} in {craft}")
print()

# Where is the ISS?
for update in range(5):

    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")
    print()

    time.sleep(5)
