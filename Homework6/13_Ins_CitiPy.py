# Dependencies
# You can install citipy by doing the following in your terminal:
# - Make sure you are in the PythonData environment:
#       type `source activate PythonData`
# - type `pip install citipy`

from citipy import citipy

# Some random coordinates
coordinates = [(200, 200), (23, 200), (42, 100)]

cities = []
for lat, lon in coordinates:
    cities.append(citipy.nearest_city(lat, lon))

for city in cities:
    country_code = city.country_code
    name = city.city_name
    print("The country code of " + name + " is '" + country_code + "'.")
