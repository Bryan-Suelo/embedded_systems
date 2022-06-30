Dict = {'Beacon3': 'AC233F65F796', 'Beacon4':'AC233F65F79A', 'Beacon5': 'AC233F65F7A9', 'Beacon6': 'AC233F65F79C', 
    'Beacon7': 'AC233F65F79D', 'Beaco10':'AC233F65F7A7', 'Beaco11': 'AC233F65F7A0', 'Beaco12':'AC233F65F799', 'Beaco13':'AC233F65F7A5', 
    'Beaco18':'AC233F65F797', 'Beaco19':'AC233F65F798', 'Beaco20':'AC233F65F79B', 'Beaco17':'AC233F65F79F', 'MBeacon':'AC233F65F72E'}

search_age = 'AC233F65F79D'
for name, age in Dict.items():
	if age == search_age:
		print(name)
		print(age)
