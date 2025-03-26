-- Clear existing data
DELETE FROM reservation;
DELETE FROM projection;
DELETE FROM screen;
DELETE FROM user;
DELETE FROM movie;

-- Insert sample movies
INSERT INTO movie (id, title, director, duration, main_cast, synopsis, img)
VALUES
(1, 'Inception', 'Christopher Nolan', 148, 'Leonardo DiCaprio, Joseph Gordon-Levitt', 'A thief who steals corporate secrets through dream-sharing.', 'inception.jpg'),
(2, 'The Matrix', 'The Wachowskis', 136, 'Keanu Reeves, Laurence Fishburne', 'A computer hacker learns the truth about his reality.', 'matrix.jpg'),
(3, 'Interstellar', 'Christopher Nolan', 169, 'Matthew McConaughey, Anne Hathaway', 'A team of explorers travel through a wormhole in space.', 'interstellar.jpg');

-- Insert sample screens
INSERT INTO screen (id, name, capacity)
VALUES
(1, 'Main Hall', 100),
(2, 'Studio 2', 50);

-- Insert sample projections
INSERT INTO projection (id, movie_id, screen_id, projection_time)
VALUES
(1, 1, 1, '2025-03-28 18:00:00'),
(2, 2, 2, '2025-03-29 20:00:00');

-- Insert sample users
INSERT INTO user (id, username, password, is_admin)
VALUES
(1, 'admin', 'adminpass', 1),
(2, 'user1', 'userpass', 0);

-- Insert sample reservations
INSERT INTO reservation (id, user_id, projection_id, seat_number)
VALUES
(1, 2, 1, 'A5'),
(2, 2, 1, 'A6');