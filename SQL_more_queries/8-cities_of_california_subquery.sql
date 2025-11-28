-- Selecting cities from states
SELECT c.id, c.name FROM states s, cities c WHERE c.state_id = s.id and s.name = 'California' ORDER BY c.id ASC;
