-- Complex listing of the tv shows according to their genres
SELECT s.title, sg.genre_id FROM tv_shows s, tv_show_genres sg WHERE s.id = sg.show_id ORDER BY s.title ASC, sg.genre_id ASC;
