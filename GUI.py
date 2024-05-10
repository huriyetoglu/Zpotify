from tkinter import *
import database as db
from PIL import Image, ImageTk
import datetime

def go_to_page(page):
        page.tkraise()

def find_user(mail,password): 
    query = f"SELECT * FROM User WHERE email = \"{mail}\" AND password = \"{password}\""
    db.mycursor.execute(query)
    myresult = db.mycursor.fetchall()   
    if myresult != None:
        return myresult[0]
    else:
        go_to_page(LogInPage.main_frame)   

class logInPage:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="green")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)
        #window.geometry("220x215")  
    
    def create_sıgnInPage(self):
        
        label = Frame(self.main_frame , background="#27b878")
        label.grid(row=0,column=0,columnspan=1,rowspan=1)

        
        def get_atts():
            user_email = email_entry.get()
            user_password = password_entry.get()
            user = find_user(user_email,user_password)
            db.setCurrentUser(user[0],user[1],user[2],user[3],user[4])
            
        topLabel = Label(label, text= "Log Into Your Account!" , background="green")
        topLabel.grid(row=0, column=0, columnspan=2, pady=20,padx=10 ,sticky="nsew")

        # Email Entry
        email_label = Label(label,text="Email", background="green")
        email_label.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        email_entry = Entry(label)
        email_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        # Password Entry
        password_label = Label(label,text="Password", background="green")
        password_label.grid(row=4, column=0, pady=5, padx=10, sticky="w")
        password_entry = Entry(label, show="*") 
        password_entry.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        # Log In Button
        log_in_button = Button(label,text="Log In", width= 10 ,command = lambda: [get_atts(),window.geometry("1200x750"),UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)])
        log_in_button.grid(row=6, column=0, columnspan=2, pady=10  )        

        button = Button(label, text="Go to the Main Page", command=lambda: [window.geometry("177x330"),go_to_page(MainHomePage.main_frame)])
        button.grid(row=7,column=0,columnspan=2, pady=10 )

class sıgnInPage:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="green")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)
        #window.geometry("220x277")  
    
    def create_sıgnInPage(self):
        
        label = Frame(self.main_frame , background="#27b878")
        label.grid(row=0,column=0,columnspan=1,rowspan=1)

        
        def add_user():
            user_name = name_entry.get()
            user_email = email_entry.get()
            user_password = password_entry.get()
            user_date = date_entry.get()
            
            db.addUser(user_name,user_email,user_password,user_date)


        topLabel = Label(label, text= "Sign In to Zpotify!" , background="green")
        topLabel.grid(row=0, column=0, columnspan=2, pady=20,padx=10 ,sticky="nsew")

        # Name Entry
        name_label = Label(label,text="Name", background="green")
        name_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        name_entry = Entry(label)
        name_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        # Email Entry
        email_label = Label(label,text="Email", background="green")
        email_label.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        email_entry = Entry(label)
        email_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        # Password Entry
        password_label = Label(label,text="Password", background="green")
        password_label.grid(row=4, column=0, pady=5, padx=10, sticky="w")
        password_entry = Entry(label, show="*") 
        password_entry.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        # Date Entry
        date_label = Label(label,text="Birthday", background="green")
        date_label.grid(row=5, column=0, pady=5, padx=10, sticky="w")
        date_entry = Entry(label)
        date_entry.grid(row=5, column=1, pady=5, padx=10, sticky="w")


        sign_in_button = Button(label,text="Sign In", width= 10 ,command = lambda: [add_user(),window.geometry("177x330"),go_to_page(MainHomePage.main_frame)])
        sign_in_button.grid(row=6, column=0, columnspan=2, pady=10  )        
        
        button = Button(label, text="Go to the Main Page", command=lambda: [window.geometry("177x330"),go_to_page(MainHomePage.main_frame)])
        button.grid(row=7,column=0,columnspan=2, pady=10 )

class MainPage:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="green")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)
        window.geometry("177x330")  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((150, 150), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
    
    def create_MainPage(self):
        
        label = Frame(self.main_frame , background="#27b878")
        label.grid(row=0,column=0,columnspan=1,rowspan=1)
            
        topLabel = Label(label, text= "Welcome To Zpotify!" , background="green")
        topLabel.grid(row=0, column=0, columnspan=2, pady=20,padx=10 ,sticky="nsew")

        imgHolder = Label(label)
        imgHolder.grid(row=1, column=0, columnspan=2, pady=5 ,padx=10 ,sticky="nsew")
        image_label = Label(imgHolder, image=self.image)
        image_label.pack(pady=5)

        
        sign_in_button = Button(label,text="Sign In", width= 10 ,command = lambda: [window.geometry("220x277"),go_to_page(RegisterPage.main_frame)])
        sign_in_button.grid(row=2, column=0, columnspan=2, pady=10 )   

        log_in_button = Button(label,text="Log In", width= 10 ,command = lambda: [window.geometry("220x215"),go_to_page(LogInPage.main_frame)])
        log_in_button.grid(row=3, column=0, columnspan=2, pady=10 ) 

class UserHomePage:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)


    def del_playlist(self,playlist_ID,user_ID):
        query = f"DELETE FROM Playlist WHERE id = {playlist_ID} AND creator_id = {user_ID}"
        db.mycursor.execute(query)
        db.mydb.commit()
        
    def create_page(self, songs, my_playlists, liked_songs):
        
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()      
        

        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        
        

        menu_playlist_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_playlist_container.pack(fill="both")

        menu = Frame(menu_playlist_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs)]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs)]
                                )
        liked_songs_btn.pack(pady=30)
        
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30)     

        playlist_container = Frame(menu_playlist_container,
                          background="#222A2A",
                          width=850
                          )
        playlist_container.pack(side="right", fill="both")
        playlist_container.pack_propagate(False)

        header = Label(playlist_container,
                       text="All Playlists",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)
                    
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
         
        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(playlist_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        playlists = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=playlists, anchor="nw", width=canvas.winfo_reqwidth())

        canvas.bind("<Configure>", on_canvas_configure)

        playlists_from_db = db.get_all_playlists()
   
        for playlist in playlists_from_db:
            playlist_box = Frame(playlists,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            playlist_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(playlist_box,
                                 font=("Arial", 22),
                                  text=playlist[2],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)

            add_btn = Button(playlist_box,
                             text="+",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command=lambda playlist=playlist: db.save_playlist(playlist[0], db.currentUserofDatabase.user_ID),
                             padx=3
                             )
            add_btn.pack(side="right", padx=10)
            
            if(db.currentUserofDatabase.user_ID == playlist[1]):
                del_btn = Button(playlist_box,text="DEL",font=("Arial", 15,"bold"),highlightbackground="#0C4443",command=lambda playlist=playlist: [self.del_playlist(playlist[0], db.currentUserofDatabase.user_ID),UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)],padx=3)
                del_btn.pack(side="right", padx=10)
                

        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


class Songs:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
    
    def setSongIdToAddPlaylist(self,song):
        db.currentSongToAddPlaylist =  song[0]
    
    def likeSong(self,song_ID):
        query = f"INSERT INTO user_likes_track(user_ID,track_ID) VALUES({db.currentUserofDatabase.user_ID},{song_ID})"
        db.mycursor.execute(query)
        db.mydb.commit()
    
    def playsong(self,song_id):
        query = f"INSERT INTO user_plays_track VALUES({db.currentUserofDatabase.user_ID},{song_id},\"{datetime.date.today()}\");"
        db.mycursor.execute(query)
        db.mydb.commit()
    
    def create_page(self, songs, my_playlists, liked_songs):

        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        

        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )
        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)        

        menu_songs_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_songs_container.pack(fill="both")

        menu = Frame(menu_songs_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: go_to_page(songs)
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs)]
                                )
        liked_songs_btn.pack(pady=30)
        
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30)         

        song_container = Frame(menu_songs_container,
                          background="#222A2A",
                          width=850
                          )
        song_container.pack(side="right", fill="both")
        song_container.pack_propagate(False)

        header = Label(song_container,
                       text="Songs",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(song_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        songs = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=songs, anchor="nw", width=canvas.winfo_reqwidth()) 

        canvas.bind("<Configure>", on_canvas_configure)


        songs_from_db = db.all_songs

        for song in songs_from_db:
            song_box = Frame(songs,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            song_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(song_box,
                                 font=("Arial", 22),
                                  text=song[2],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)

            add_btn = Button(song_box,
                             text="+",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command= lambda song=song: [add_to_playlist.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(add_to_playlist.main_frame),self.setSongIdToAddPlaylist(song)],
                             padx=3
                             )
            add_btn.pack(side="right", padx=10)

            like_btn = Button(song_box,
                              text="<3",
                              font=("Arial", 15,"bold"),
                              highlightbackground="#0C4443",
                              command= lambda song=song: [self.likeSong(song[0])],
                              padx=3
                              )
            like_btn.pack(side="right", padx=10)
            
            play_btn = Button(song_box,
                              text="Play",
                              font=("Arial", 15,"bold"),
                              highlightbackground="#0C4443",
                              command= lambda song=song: [db.clear_playing_song(),self.playsong(song[0]),db.get_Playing_song(),songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs_.main_frame)],
                              padx=3
                              )
            play_btn.pack(side="right", padx=10)
        
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


class My_Playlists:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
    
    def setcurrentPlaylistId(self,id):
        db.current_playlist_id = id
    
    def delete_users_playlist(self,playlist):
        
        query = f"DELETE FROM User_has_playlist WHERE playlist_ID = {playlist[0]} AND user_ID = {db.currentUserofDatabase.user_ID}"
        db.mycursor.execute(query)
        db.mydb.commit()
    
    def create_page(self, songs, my_playlists, liked_songs):

        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()           

        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")


        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        menu_playlist_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_playlist_container.pack(fill="both")

        menu = Frame(menu_playlist_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs),self.setcurrentPlaylistId(songs[0])]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: go_to_page(my_playlists)
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame) ,go_to_page(liked_songs_.main_frame)]
                                )
        liked_songs_btn.pack(pady=30)
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30)         

        add_new_pl_btn = Button(menu,
                                 text="New Playlist +",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [new_playlist.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(new_playlist.main_frame)]
                                )
        add_new_pl_btn.pack(pady=30)


        playlist_container = Frame(menu_playlist_container,
                          background="#222A2A",
                          width=850
                          )
        playlist_container.pack(side="right", fill="both")
        playlist_container.pack_propagate(False)

        header = Label(playlist_container,
                       text="My Playlists",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(playlist_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        playlists = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=playlists, anchor="nw", width=canvas.winfo_reqwidth())

        canvas.bind("<Configure>", on_canvas_configure)

        db.current_playlist = db.getCurrent_Playlists()

        playlists_from_db = db.current_playlist


        for playlist in playlists_from_db:
            playlist_box = Frame(playlists,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            playlist_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(playlist_box,
                                 font=("Arial", 22),
                                  text=playlist[1],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)

            del_btn = Button(playlist_box,
                             text="X",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             padx=3,
                             command = lambda playlist=playlist: [self.delete_users_playlist(playlist) , playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame)]
                             )
            del_btn.pack(side="right", padx=10)

            go_btn = Button(playlist_box,
                             text="Songs",
                             font=("Arial", 15, "bold"),
                             highlightbackground="#0C4443",
                             command = lambda playlist=playlist: [self.setcurrentPlaylistId(playlist[0]) , my_playlist_songs.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlist_songs.main_frame)],
                             padx=3
                             )
            go_btn.pack(side="right", padx=10)
        
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


class New_Playlist:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
    
    def add_new_playlist(self):
        query = f"INSERT INTO Playlist(creator_id,name) VALUES({db.currentUserofDatabase.user_ID}, \"{db.new_playlist_to_add}\")"
        db.mycursor.execute(query)
        db.mydb.commit()
    
    def setcurrentPlaylistId(self,id):
        db.current_playlist_id = id
    
    def delete_users_playlist(self,playlist):
        
        query = f"DELETE FROM User_has_playlist WHERE playlist_ID = {playlist[0]} AND user_ID = {db.currentUserofDatabase.user_ID}"
        db.mycursor.execute(query)
        db.mydb.commit()
    
    def create_page(self, songs, my_playlists, liked_songs):
        
        def get_atts():
            db.new_playlist_to_add = playlist_name.get()
            

        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")


        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        menu_playlist_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_playlist_container.pack(fill="both")

        menu = Frame(menu_playlist_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs),self.setcurrentPlaylistId(songs[0])]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: go_to_page(my_playlists)
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame) ,go_to_page(liked_songs_.main_frame)]
                                )
        liked_songs_btn.pack(pady=30)
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30) 

        playlist_container = Frame(menu_playlist_container,
                          background="#222A2A",
                          width=850
                          )
        playlist_container.pack(side="right", fill="both")
        playlist_container.pack_propagate(False)

        header = Label(playlist_container,
                       text="Add a New Playlist",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        entry_container = Frame(playlist_container,
                                background="#222A2A")
        entry_container.pack(pady=80)

        playlist_name = Entry(entry_container,
                              width=60
                            )
        playlist_name.pack()

        submit = Button(entry_container,
                        highlightbackground="#222A2A",
                        text="Add",
                        command= lambda: [get_atts(),self.add_new_playlist(),playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(playlist_.main_frame)]
                        )
        submit.pack(pady=20)




class My_playlist_add_song:

    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)

    def addSongToPlaylist(self,song_id,playlist_id):
        
        query = f"INSERT INTO track_has_playlist(playlist_ID, track_ID) VALUES({playlist_id},{song_id})"
        db.mycursor.execute(query)
        db.mydb.commit()
        
    
    def create_page(self, songs, my_playlists, liked_songs):

        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        menu_playlist_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_playlist_container.pack(fill="both")

        menu = Frame(menu_playlist_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs)]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [ liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(liked_songs)]
                                )
        liked_songs_btn.pack(pady=30)
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30) 
        playlist_container = Frame(menu_playlist_container,
                          background="#222A2A",
                          width=850
                          )
        playlist_container.pack(side="right", fill="both")
        playlist_container.pack_propagate(False)

        header = Label(playlist_container,
                       text="Select a playlist to add the song",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(playlist_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        playlists = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=playlists, anchor="nw", width=canvas.winfo_reqwidth())

        canvas.bind("<Configure>", on_canvas_configure)

        db.current_playlist = db.getCurrent_Playlists()

        playlists_from_db = db.current_playlist


        for playlist in playlists_from_db:
            playlist_box = Frame(playlists,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            playlist_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(playlist_box,
                                 font=("Arial", 22),
                                  text=playlist[1],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)

            add_btn = Button(playlist_box,
                             text="+",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command=lambda playlist = playlist : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(songs_.main_frame),self.addSongToPlaylist(db.currentSongToAddPlaylist,playlist[0])],
                             padx=3
                             )
            add_btn.pack(side="right", padx=10)
        
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

class My_playlist_songs:

    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
        
    def playsong(self,song_id):
        query = f"INSERT INTO user_plays_track VALUES({db.currentUserofDatabase.user_ID},{song_id},\"{datetime.date.today()}\");"
        db.mycursor.execute(query)
        db.mydb.commit()    
    
    def deleteSongFromPlaylist(self,playlist_id,song_id):
        query = f"DELETE FROM track_has_playlist WHERE playlist_ID = {playlist_id} AND track_ID = {song_id};"
        db.mycursor.execute(query)
        db.mydb.commit()
        
    
    def create_page(self, songs, my_playlists, liked_songs):

        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        menu_songs_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_songs_container.pack(fill="both")

        menu = Frame(menu_songs_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs_.main_frame)]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(liked_songs_.main_frame)]
                                )
        liked_songs_btn.pack(pady=30)
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30) 
        song_container = Frame(menu_songs_container,
                          background="#222A2A",
                          width=850
                          )
        song_container.pack(side="right", fill="both")
        song_container.pack_propagate(False)

        header = Label(song_container,
                       text="Songs inside the Playlist",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        songs = Frame(song_container,
                          width=650,
                          height=500,
                          background="black"
                          )
        songs.pack()
        songs.pack_propagate(False)

        query = f"SELECT DISTINCT Playlist.name , Track.id ,  Track.name FROM User_has_playlist INNER JOIN Playlist ON Playlist.id = User_has_playlist.playlist_ID INNER JOIN track_has_playlist ON  track_has_playlist.playlist_ID = User_has_playlist.playlist_ID INNER JOIN Track ON Track.id = track_has_playlist.track_ID WHERE User_has_playlist.user_ID = {db.currentUserofDatabase.user_ID} AND track_has_playlist.playlist_ID = {db.current_playlist_id} ;"
        db.mycursor.execute(query)
        songs_from_db = db.mycursor.fetchall()
        

        for song in songs_from_db:
            song_box = Frame(songs,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            song_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(song_box,
                                 font=("Arial", 22),
                                  text=song[2],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)

            del_btn = Button(song_box,
                             text="Delete",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command= lambda song=song: [self.deleteSongFromPlaylist(db.current_playlist_id,song[1]),go_to_page(playlist_.main_frame)],
                             padx=3
                             )
            del_btn.pack(side="right", padx=10)
            
            play_btn = Button(song_box,
                              text="Play",
                              font=("Arial", 15,"bold"),
                              highlightbackground="#0C4443",
                              command= lambda song=song: [db.clear_playing_song(),self.playsong(song[1]),db.get_Playing_song(),my_playlist_songs.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(my_playlist_songs.main_frame)],
                              padx=3
                              )
            play_btn.pack(side="right", padx=10)            




class LikedSongs:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
    def playsong(self,song_id):
        query = f"INSERT INTO user_plays_track VALUES({db.currentUserofDatabase.user_ID},{song_id},\"{datetime.date.today()}\");"
        db.mycursor.execute(query)
        db.mydb.commit()
    def del_liked_song(self,song_id):
        
        query = f"DELETE FROM user_likes_track WHERE user_ID = {db.currentUserofDatabase.user_ID} AND track_ID = {song_id};"
        db.mycursor.execute(query)
        db.mydb.commit()
        
    def create_page(self, songs, my_playlists, liked_songs):
        
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        menu_playlist_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_playlist_container.pack(fill="both")

        menu = Frame(menu_playlist_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs)]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: go_to_page(liked_songs)
                                )
        liked_songs_btn.pack(pady=30)
    
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30) 
        playlist_container = Frame(menu_playlist_container,
                          background="#222A2A",
                          width=850
                          )
        playlist_container.pack(side="right", fill="both")
        playlist_container.pack_propagate(False)

        header = Label(playlist_container,
                       text="Liked Songs",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)
    
        
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(playlist_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        playlists = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=playlists, anchor="nw", width=canvas.winfo_reqwidth())

        canvas.bind("<Configure>", on_canvas_configure)


        query = f"SELECT Track.name,Track.id FROM user_likes_track INNER JOIN Track ON Track.id = user_likes_track.track_ID WHERE user_ID = {db.currentUserofDatabase.user_ID}"
        db.mycursor.execute(query)
        playlists_from_db = db.mycursor.fetchall()

        for playlist in playlists_from_db:
            playlist_box = Frame(playlists,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            playlist_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(playlist_box,
                                 font=("Arial", 22),
                                  text=playlist[0],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)

            del_btn = Button(playlist_box,
                             text="Del",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command=lambda playlist=playlist: [self.del_liked_song(playlist[1]),liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs_.main_frame)],
                             padx=3
                             )
            del_btn.pack(side="right", padx=10)
            play_btn = Button(playlist_box,
                              text="Play",
                              font=("Arial", 15,"bold"),
                              highlightbackground="#0C4443",
                              command= lambda playlist=playlist: [db.clear_playing_song(),self.playsong(playlist[1]),db.get_Playing_song(),liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs_.main_frame)],
                              padx=3
                              )
            play_btn.pack(side="right", padx=10)        
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        

            
class Profile:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)

    def unfollow(self,artist_ID):
        query = f"DELETE FROM user_follows_artists WHERE user_ID = {db.currentUserofDatabase.user_ID} AND artist_ID = {artist_ID};"
        db.mycursor.execute(query)
        db.mydb.commit()

    def create_page(self, songs, my_playlists, liked_songs):
        
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        menu_playlist_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_playlist_container.pack(fill="both")

        menu = Frame(menu_playlist_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs)]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs)]
                                )
        liked_songs_btn.pack(pady=30)
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30)         
        seeartists_btn = Button(menu,
                                 text="See All Artists",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [all_artist.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(all_artist.main_frame)]
                                )
        seeartists_btn.pack(pady=30)
        
        
        info = f"User Info\nID : {db.currentUserofDatabase.user_ID}\nName: {db.currentUserofDatabase.user_name}\nEmail : {db.currentUserofDatabase.user_email}\nBirthday : {db.currentUserofDatabase.user_date}"
        
        placeholder_userInfo = Label(menu,text=info,background="white",width=100,height=100,
                                    font=("Arial", 20),
                                    fg="white",
                                    bg="Black"
                                    )
        placeholder_userInfo.pack()

        playlist_container = Frame(menu_playlist_container,
                          background="#222A2A",
                          width=850
                          )
        playlist_container.pack(side="right", fill="both")
        playlist_container.pack_propagate(False)

        header = Label(playlist_container,
                       text="Following Artists",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(playlist_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        playlists = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=playlists, anchor="nw", width=canvas.winfo_reqwidth())

        canvas.bind("<Configure>", on_canvas_configure)

        query = f"SELECT artist.name , artist.id FROM user_follows_artists INNER JOIN artist ON artist.id = user_follows_artists.artist_ID WHERE user_follows_artists.user_ID = {db.currentUserofDatabase.user_ID};"
        db.mycursor.execute(query)
        
        playlists_from_db = db.mycursor.fetchall()

        for playlist in playlists_from_db:
            playlist_box = Frame(playlists,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            playlist_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(playlist_box,
                                 font=("Arial", 22),
                                  text=playlist[0],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)


            unf_btn = Button(playlist_box,
                             text="Unfollow",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command=lambda playlist=playlist: [self.unfollow(playlist[1]),profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)],
                             padx=3
                             )
            unf_btn.pack(side="right", padx=10)
        
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

class Artists:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
    
    def followArtist(self,artistID):
        query = f"INSERT INTO user_follows_artists(user_ID, artist_ID) VALUES({db.currentUserofDatabase.user_ID},{artistID})"
        db.mycursor.execute(query)
        db.mydb.commit()
    
    def create_page(self, songs, my_playlists, liked_songs):

        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )
        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)        

        menu_songs_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_songs_container.pack(fill="both")

        menu = Frame(menu_songs_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: go_to_page(songs)
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs)]
                                )
        liked_songs_btn.pack(pady=30)
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30) 
        song_container = Frame(menu_songs_container,
                          background="#222A2A",
                          width=850
                          )
        song_container.pack(side="right", fill="both")
        song_container.pack_propagate(False)

        header = Label(song_container,
                       text="All Artists",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(song_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        songs = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=songs, anchor="nw", width=canvas.winfo_reqwidth()) 

        canvas.bind("<Configure>", on_canvas_configure)


        songs_from_db = db.all_artists

        for song in songs_from_db:
            song_box = Frame(songs,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            song_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(song_box,
                                 font=("Arial", 22),
                                  text=song[1],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)


            add_btn = Button(song_box,
                             text="+",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command= lambda song=song: [self.followArtist(song[0]),profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(profilePage.main_frame)],
                             padx=3
                             )
            add_btn.pack(side="right", padx=10)
        
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

class Albums:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)

    def setCurrentAlbumID(self,album_ID):
        db.current_album_id = album_ID
    
    def create_page(self, songs, my_playlists, liked_songs):
        
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()   
        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )

        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)
        
        

        menu_playlist_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_playlist_container.pack(fill="both")

        menu = Frame(menu_playlist_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs)]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs)]
                                )
        liked_songs_btn.pack(pady=30)
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30) 
        playlist_container = Frame(menu_playlist_container,
                          background="#222A2A",
                          width=850
                          )
        playlist_container.pack(side="right", fill="both")
        playlist_container.pack_propagate(False)

        header = Label(playlist_container,
                       text="All Albums",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)
                    
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
         
        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(playlist_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        playlists = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=playlists, anchor="nw", width=canvas.winfo_reqwidth())

        canvas.bind("<Configure>", on_canvas_configure)

        playlists_from_db = db.all_albums
   
        for playlist in playlists_from_db:
            playlist_box = Frame(playlists,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            playlist_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(playlist_box,
                                 font=("Arial", 22),
                                  text=playlist[2],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)
            
            artist_name = Label(playlist_box,
                                 font=("Arial", 18),
                                  text=" -- by "+playlist[3],
                                  background="#0C4443")
            artist_name.pack(side="left", 
                               padx=15,
                               pady=15)


            add_btn = Button(playlist_box,
                             text="See Songs",
                             font=("Arial", 15,"bold"),
                             highlightbackground="#0C4443",
                             command=lambda playlist=playlist: [self.setCurrentAlbumID(playlist[0]),songs_ınAlbum.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs_ınAlbum.main_frame)],
                             padx=3
                             )
            add_btn.pack(side="right", padx=10)
            
            
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
class Songs_InAlbum:
    
    def __init__(self, window):
        self.main_frame = Frame(window,
                                background="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        window.rowconfigure(0, weight=1)  
        window.columnconfigure(0, weight=1)  
        image_path = "Python\Database_Project\logo.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized_image)
    def playsong(self,song_id):
        query = f"INSERT INTO user_plays_track VALUES({db.currentUserofDatabase.user_ID},{song_id},\"{datetime.date.today()}\");"
        db.mycursor.execute(query)
        db.mydb.commit()    
    def setSongIdToAddPlaylist(self,song):
        db.currentSongToAddPlaylist =  song[0]
    
    def likeSong(self,song_ID):
        query = f"INSERT INTO user_likes_track(user_ID,track_ID) VALUES({db.currentUserofDatabase.user_ID},{song_ID})"
        db.mycursor.execute(query)
        db.mydb.commit()
    
    def create_page(self, songs, my_playlists, liked_songs):

        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        
        navbar = Frame(self.main_frame,
                       height=20,
                       background="#0C4443"  #code:#1F9360
                       )
        navbar.pack(fill="x")
        playbar = Frame(self.main_frame,
                       height=40,
                       background="#0C4443"  #code:#1F9360
                       )
        playbar.pack(side="bottom",fill="x")
        
        
        
        if len(db.get_Playing_song()) != 0:
            playing = db.get_Playing_song()[0][1]
        else:
            playing = "Nothing"
        
        playing_info = Label(playbar,
                       text="Now Playing : "+playing,
                       font=("Arial", 20),
                       bg="#0C4443"
                       )  
        playing_info.pack()           

        image_label = Label(navbar, image=self.image)
        image_label.pack(side="left")



        logo = Label(navbar,
                     text="logo",
                     width=10,
                     height=5,
                     )
        profile_button = Button(navbar, 
                               text=db.currentUserofDatabase.user_name,
                               highlightbackground="#0C4443",
                               command= lambda : [profilePage.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(profilePage.main_frame)]
                               )
        profile_button.pack(side="right", padx=20)
        
        go_toHomeButton = Button(navbar, 
                               text="Go To HomePage",
                               highlightbackground="#0C4443",
                               command= lambda : [UserHome.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(UserHome.main_frame)]
                               )
        go_toHomeButton.pack(side="right", padx=20)        

        menu_songs_container = Frame(self.main_frame,
                                        background="#222A2A")
        menu_songs_container.pack(fill="both")

        menu = Frame(menu_songs_container,
                     background="black",
                     width=350,
                     height=660,
                     pady=20)
        menu.pack(side="left")

        menu.pack_propagate(False)

        songs_btn = Button(menu, 
                           text="Songs",
                           highlightbackground="black",
                           background="#6DEEBD",
                           width=23,
                           command= lambda: [songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs_.main_frame)]
                           )
        songs_btn.pack(pady=30)

        playlist_btn = Button(menu, 
                              text="My Playlists",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [playlist_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(my_playlists)]
                            )
        playlist_btn.pack(pady=30)

        liked_songs_btn = Button(menu,
                                 text="Liked Songs",
                                 highlightbackground="black",
                                 width=23,
                                 command= lambda: [liked_songs_.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(liked_songs)]
                                )
        liked_songs_btn.pack(pady=30)
        
        playlist_btn = Button(menu, 
                              text="Albums",
                              highlightbackground="black",
                              width=23,
                              command= lambda: [all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame), go_to_page(all_albums.main_frame)]
                            )   
        playlist_btn.pack(pady=30)         

        song_container = Frame(menu_songs_container,
                          background="#222A2A",
                          width=850
                          )
        song_container.pack(side="right", fill="both")
        song_container.pack_propagate(False)

        header = Label(song_container,
                       text="Songs In the Album",
                       font=("Arial", 40),
                       bg="#222A2A"
                       )
        header.pack(padx=20, pady=30)

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Add a frame to hold the canvas and scrollbar
        canvas_frame = Frame(song_container, background="black", width=650, height=500)
        canvas_frame.pack(side="left", expand=True)

        # Add a canvas to hold the playlists with a scrollbar
        canvas = Canvas(canvas_frame, background="black", width=650, height=500)
        canvas.pack(side="left", expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, troughcolor="#444444")
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the playlists inside the canvas
        songs = Frame(canvas, background="black")
        canvas.create_window((0, 0), window=songs, anchor="nw", width=canvas.winfo_reqwidth()) 

        canvas.bind("<Configure>", on_canvas_configure)

        query = f"SELECT album.id, track.id, track.name, track.genre FROM album INNER JOIN track ON Album.id = track.album_id WHERE album.id = {db.current_album_id}"
        db.mycursor.execute(query)
        

        songs_from_db = db.mycursor.fetchall()

        for song in songs_from_db:
            song_box = Frame(songs,
                                 height=40,
                                 background="#0C4443",
                                 highlightbackground="#222A2A", 
                                 highlightthickness=2
                                 )
            song_box.pack(fill="x")
            #playlist_box.pack_propagate(False)
            
            playlist_name = Label(song_box,
                                 font=("Arial", 22),
                                  text=song[2],
                                  background="#0C4443")
            playlist_name.pack(side="left", 
                               padx=15,
                               pady=15)
            
            genre_name = Label(song_box,
                                 font=("Arial", 22),
                                  text=song[3],
                                  background="#0C4443")
            genre_name.pack(side="left", 
                               padx=15,
                               pady=15)

            like_btn = Button(song_box,
                              text="<3",
                              font=("Arial", 15,"bold"),
                              highlightbackground="#0C4443",
                              command= lambda song=song: [self.likeSong(song[1]),all_albums.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(all_albums.main_frame)],
                              padx=3
                              )
            like_btn.pack(side="right", padx=10)
            play_btn = Button(song_box,
                              text="Play",
                              font=("Arial", 15,"bold"),
                              highlightbackground="#0C4443",
                              command= lambda song=song: [db.clear_playing_song(),self.playsong(song[1]),db.get_Playing_song(),songs_ınAlbum.create_page(songs_.main_frame, playlist_.main_frame, liked_songs_.main_frame),go_to_page(songs_ınAlbum.main_frame)],
                              padx=3
                              )
            play_btn.pack(side="right", padx=10)
        
        # Update the canvas height based on the total height of the playlists
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

window = Tk()
window.title("Zpotify")
window.geometry("1200x750")

MainHomePage = MainPage(window)
UserHome = UserHomePage(window)
playlist_ = My_Playlists(window)
songs_ = Songs(window)
liked_songs_ = LikedSongs(window)
RegisterPage = sıgnInPage(window) 
LogInPage = logInPage(window)
add_to_playlist = My_playlist_add_song(window)
my_playlist_songs = My_playlist_songs(window)
profilePage = Profile(window)
new_playlist = New_Playlist(window)
all_artist = Artists(window)
all_albums = Albums(window)
songs_ınAlbum = Songs_InAlbum(window)

MainHomePage.create_MainPage()
RegisterPage.create_sıgnInPage()
LogInPage.create_sıgnInPage()

go_to_page(MainHomePage.main_frame)

window.mainloop()