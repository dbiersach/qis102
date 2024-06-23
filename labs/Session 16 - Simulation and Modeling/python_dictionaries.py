# python_dictionaries.py

from pprint import pprint

# Create a dictionary of key:value string pairs
capitals = {
    "USA": "Washington D.C.",
    "Germany": "Berlin",
    "France": "Paris",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
}
pprint(capitals)
print()

# Two different ways to add a new key-value pair
capitals.update({"United Kingdom": "London"})
capitals["Spain"] = "Madrid"
pprint(capitals)
print()

# Change an existing key's value
capitals["USA"] = "New York"
pprint(capitals)
print()

# Remove a key-value pair
del capitals["Russia"]
pprint(capitals)
