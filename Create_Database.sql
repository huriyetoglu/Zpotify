CREATE DATABASE zpotify;

USE zpotify;

CREATE TABLE User(
	
    id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50),
    email VARCHAR(150),
    password VARCHAR(150),
    date_of_birth DATE

);

CREATE TABLE Artist(
	
    id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50)

);

CREATE TABLE Album(
	
    id INT PRIMARY KEY AUTO_INCREMENT,
    artist_id INT, 
	name VARCHAR(50),
    release_date DATE,
	FOREIGN KEY (artist_id) REFERENCES Artist(id) 
    
);

CREATE TABLE Track(
	
    id INT PRIMARY KEY AUTO_INCREMENT,
    album_id INT, 
	name VARCHAR(50),
    genre VARCHAR(100),
    duration INT,
	FOREIGN KEY (album_id) REFERENCES Album(id)
    
);

CREATE TABLE Playlist(
	
    id INT PRIMARY KEY AUTO_INCREMENT,
    creator_id INT, 
	name VARCHAR(50),
    FOREIGN KEY(creator_ID) REFERENCES User(id)
    
);

CREATE TABLE User_follows_artists(
	
    user_ID INT,
    artist_ID INT,
    PRIMARY KEY(user_ID,artist_ID),
    FOREIGN KEY(user_ID) REFERENCES User(id),
    FOREIGN KEY(artist_ID) REFERENCES Artist(id) 

);

CREATE TABLE User_has_playlist(
	
    playlist_ID INT ,
    user_ID INT,
    PRIMARY KEY(playlist_ID,user_ID),
    FOREIGN KEY(playlist_ID) REFERENCES Playlist(id),
    FOREIGN KEY(user_ID) REFERENCES User(id) 
	
);

CREATE TABLE Track_has_playlist(
	
    playlist_ID INT ,
    track_ID INT ,
    PRIMARY KEY(playlist_ID,track_ID),
    FOREIGN KEY(playlist_ID) REFERENCES Playlist(id),
    FOREIGN KEY(track_ID) REFERENCES Track(id) 

);

CREATE TABLE User_likes_track(
	
    user_ID INT ,
    track_ID INT ,
    like_date DATE,
    PRIMARY KEY(user_ID,track_ID) ,
    FOREIGN KEY(user_ID) REFERENCES User(id),
    FOREIGN KEY(track_ID) REFERENCES Track(id) 

);

CREATE TABLE User_plays_track(
	
    user_ID INT AUTO_INCREMENT,
    song_ID INT,
    play_date DATE,
    FOREIGN KEY(user_ID) REFERENCES User(id),
    FOREIGN KEY(song_ID) REFERENCES Track(id), 
    PRIMARY KEY(user_ID, play_date)

);

CREATE TRIGGER add_playlists_ofCreators
	AFTER INSERT ON Playlist
		FOR EACH ROW
			INSERT INTO User_has_playlist VALUES(NEW.id, NEW.creator_ID);
