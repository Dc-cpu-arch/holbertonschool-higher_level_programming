-- Lists elements from a database and shows it with format
SELECT cities.id,
	cities.name,
	states.name
FROM cities
	JOIN states ON cities.state_id = states.id;
