name = input("What is the dragon's name? ")
age = input("How many years old is the dragon? ")
colour = input("What colour is the dragon? ")
location = input("Where does the dragon live? ")
treasure = input("What does the dragon collect? ")

text = f"""
{name} was a {colour} dragon, who was {age} years old. They lived in {location}
and spent all their time collecting {treasure}.
"""

print(text)
