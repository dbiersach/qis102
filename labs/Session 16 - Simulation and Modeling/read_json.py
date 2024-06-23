# read_json.py

import json
from pathlib import Path

# Create a Python dictionary from the JSON file
file_name = "uranium_isotopes.json"
file_path = Path(__file__).parent / file_name
with open(file_path, "rb") as f_in:
    uranium_isotopes = json.load(f_in)

# Find the two isotopes with the maximum difference in half-life
max_diff = 0.0
for k1, v1 in uranium_isotopes.items():
    for k2, v2 in uranium_isotopes.items():
        h1 = float(v1["half-life"])
        h2 = float(v2["half-life"])
        diff = abs(h1 - h2)
        if diff > max_diff:
            iso1 = k1
            iso2 = k2
            max_diff = diff

# Convert maximum half-life difference from seconds to years
max_diff = max_diff / (60 * 60 * 24 * 365.25)

# Determine difference in neutrons between the two isotopes
neutrons1 = uranium_isotopes[iso1]["neutrons"]
neutrons2 = uranium_isotopes[iso2]["neutrons"]
neutron_delta = abs(neutrons1 - neutrons2)

print(f"{iso1} and {iso2}:")
print(f"Half-life difference: {max_diff:,.0f} years")
print(f"Neutron difference:   {neutron_delta}")
