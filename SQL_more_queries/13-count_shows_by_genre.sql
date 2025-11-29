-- Counting the movies according to the genres
SELECT g.name genre, COUNT(sg.show_id) number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres sg
ON sg.genre_id = g.id
GROUP BY g.name
ORDER BY COUNT(sg.show_id) DESC;
