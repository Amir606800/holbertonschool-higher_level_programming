-- Very complex and good display
SELECT s.title, g.name
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
RIGHT JOIN tv_shows s ON s.id = sg.show_id
ORDER BY s.title ASC, g.name ASC;
