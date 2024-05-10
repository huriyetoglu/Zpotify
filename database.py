import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="zpotify"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM User")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


def addUser(NAME,MAIL,PASSWD,DATE):
    query = f"INSERT INTO User(name,email,password,date_of_birth) VALUES (\"{NAME}\",\"{MAIL}\",\"{PASSWD}\",\"{DATE}\");"
    mycursor.execute(query)
    mydb.commit()
    
def setCurrentUser(ID,NAME,MAIL,PASSWD,DATE):
    currentUserofDatabase.user_ID = ID
    currentUserofDatabase.user_name = NAME 
    currentUserofDatabase.user_email = MAIL
    currentUserofDatabase.user_password = PASSWD 
    currentUserofDatabase.user_date = DATE 
    check()
    
def check():
    print(currentUserofDatabase.user_name)
    
def getCurrent_Playlists():
    query = f"SELECT Playlist.id, Playlist.name FROM User_has_playlist INNER JOIN Playlist ON User_has_playlist.playlist_ID = Playlist.id WHERE User_has_playlist.user_ID = {currentUserofDatabase.user_ID};"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def get_all_playlists():
    query = f"SELECT * FROM Playlist"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return_data = []
    for i in result:
        return_data.append(i)
    return return_data

def save_playlist(playlist_id,user_id):
    query=f"INSERT INTO User_has_playlist(playlist_ID,user_ID) VALUES(\"{playlist_id}\",\"{user_id}\");"
    mycursor.execute(query)
    mydb.commit()

def get_all_songs():
    query = f"SELECT * FROM Track"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def get_liked_songs():
    query = f"SELECT User_likes_track.user_ID, User_likes_track.like_date, Track.name FROM User_likes_track INNER JOIN Track ON Track.id = User_likes_track.track_ID WHERE User_likes_track.user_ID = {currentUserofDatabase.user_ID}"
    mycursor.execute(query)
    return mycursor.fetchall()

def get_all_artists():
    query = f"SELECT id , name FROM Artist"
    mycursor.execute(query)
    return mycursor.fetchall()

def get_all_albums():
    query = f"SELECT album.id, Artist.id, album.name, Artist.name FROM album INNER JOIN Artist ON Album.artist_id = Artist.id"
    mycursor.execute(query)
    return mycursor.fetchall()    


def get_Playing_song():
    query = f"SELECT user_plays_track.song_ID,track.name FROM user_plays_track INNER JOIN track ON track.id = user_plays_track.song_ID WHERE user_plays_track.user_ID = {currentUserofDatabase.user_ID};"
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    return result


def clear_playing_song():
    query=f"DELETE FROM user_plays_track WHERE user_ID = {currentUserofDatabase.user_ID};"
    mycursor.execute(query)
    mydb.commit()

class User:
    
    def __init__(self,ID,NAME,MAİL,PASSWD,DATE):
        self.user_ID = ID
        self.user_name = NAME
        self.user_email = MAİL
        self.user_password = PASSWD
        self.user_date = DATE
    
    user_ID = 0
    user_name = None
    user_email = None
    user_password = None
    user_date = None

currentSongToAddPlaylist = None

all_playlists = get_all_playlists()
print(all_playlists)  
 
currentUserofDatabase = User(None,None,None,None,None)

current_playlist = []

current_liked_songs = []
 
all_songs = get_all_songs() 

current_playlist_id = 0

all_artists = get_all_artists()

new_playlist_to_add = None

all_albums = get_all_albums()

current_album_id = None

print(all_songs)

