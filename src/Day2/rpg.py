house1 = {'location': 'London',
          'beds': 2,
          'garden': False
          }

house2 = {'location': 'Paris',
          'beds': 1,
          'garden': True,
          }

house3 = {'location': 'Berlin',
          'beds': 3,
          'garden': True,
          }

houses = [house1, house2, house3]

for house in houses:
    location = house['location']
    beds = house['beds']
    garden = house['garden']

    print(f"Location: {location}")
    print(f"No. Beds: {beds}")
    print(f"Has Garden? {garden}")

    price = 100_000 + beds * 50_000

    print(f"Estimated Price: £{price:,}")

    print()
