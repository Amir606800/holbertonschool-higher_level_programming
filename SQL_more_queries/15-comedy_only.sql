-- Comedy only outputs
SELECT s.title
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
INNER JOIN tv_shows s ON s.id = sg.show_id
WHERE g.name = 'Comedy'
ORDER BY g.name ASC;
