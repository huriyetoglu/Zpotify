INSERT INTO User (name, email, password, date_of_birth)
VALUES ('John Doe', 'john@example.com', 'password123', '1990-05-15'),
       ('Jane Smith', 'jane@example.com', 'securepass', '1985-12-22'),
       ('Alice Johnson', 'alice@example.com', 'pass1234', '1993-08-10'),
       ('Bob Williams', 'bob@example.com', 'bobs_secret', '1982-04-05'),
       ('Eva Davis', 'eva@example.com', 'evapassword', '1998-11-30'),
       ('Michael Lee', 'michael@example.com', 'mikepass', '1989-07-18'),
       ('Sophie Turner', 'sophie@example.com', 'sophie123', '1995-09-25'),
       ('Daniel White', 'daniel@example.com', 'daniel_pass', '1987-03-12'),
       ('Olivia Brown', 'olivia@example.com', 'olivia_pass', '1994-06-08'),
       ('David Miller', 'david@example.com', 'david123', '1984-02-20');
       
INSERT INTO Artist (name)
VALUES ('Ed Sheeran'),
       ('Adele'),
       ('Taylor Swift'),
       ('Bruno Mars'),
       ('Rihanna'),
       ('Justin Bieber'),
       ('Beyoncé'),
       ('Katy Perry'),
       ('Drake'),
       ('Shawn Mendes');


INSERT INTO Album (artist_id, name, release_date)
VALUES (1, 'Divide', '2017-03-03'),
       (2, '21', '2011-01-24'),
       (3, '1989',  '2014-10-27'),
       (4, '24K Magic', '2016-11-18'),
       (5, 'Anti', '2016-01-28'),
       (6, 'Purpose', '2015-11-13'),
       (7, 'Lemonade', '2016-04-23'),
       (8, 'Teenage Dream', '2010-08-24'),
       (9, 'Scorpion', '2018-06-29'),
       (10, 'Illuminate', '2016-09-23');

INSERT INTO Track (album_id, name, genre, duration)
VALUES (1, 'Shape of You', 'Pop', 235),
       (2, 'Rolling in the Deep', 'Soul', 228),
       (3, 'Shake It Off', 'Pop', 219),
       (4, '24K Magic', 'R&B', 206),
       (5, 'Work', 'R&B', 221),
       (6, 'Sorry', 'Pop', 200),
       (7, 'Formation', 'R&B', 240),
       (8, 'Firework', 'Pop', 224),
       (9, 'God\'s Plan', 'Hip Hop', 196),
       (10, 'Stitches', 'Pop', 199);
       
INSERT INTO Playlist (creator_id, name)
VALUES (1, 'My Favorites'),
       (2, 'Chill Vibes'),
       (3, 'Top Hits'),
       (4, 'Party Mix'),
       (5, 'R&B Classics'),
       (6, 'Pop Extravaganza'),
       (7, 'Empowerment Anthems'),
       (8, 'Feel-Good Tunes'),
       (9, 'Hip Hop Hooray'),
       (10, 'Indie Jams');
       
