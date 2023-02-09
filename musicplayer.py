
from os import remove
from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Music Player')
root.iconbitmap('D:/music/musicplayer.ico')
root.geometry("500x300")

pygame.mixer.init()

#Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='D:/audio', title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"), ))
    song = song.replace("D:/audio/", "")
    song = song.replace(".mp3", "")
    
    #Add song to listbox
    song_box.insert(END, song)


# Add many songs to playlist
def add_many_songs():
    song = filedialog.askopenfilenames(initialdir='D:/audio', title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"), ))

    # Loop through song list and replace directory info and mp3
    for song in song:
        song = song.replace("D:/audio/", "")
        song = song.replace(".mp3", "")
        # Insert into playlist
        song_box.insert(END, song)

# Play select song
def play():
    song = song_box.get(ACTIVE) 
    song = f'D:/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# Play the next song in the playlist
def next_song():
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current song number
    next_one = next_one[0]+1 
    # Grab song title from playlist
    song = song_box.get(next_one) 

    song = f'D:/audio/{song}.mp3' 
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    song_box.selection_clear(0, END)

    # Activate new song bar
    song_box.activate(next_one)

    # Set Active Bar to next song
    song_box.selection_set(next_one, last=None)

# Play Previous Song in playlist
def previous_song():
     # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current song number
    next_one = next_one[0]-1 
    # Grab song title from playlist
    song = song_box.get(next_one) 

    song = f'D:/audio/{song}.mp3' 
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active bar in playlist listbox
    song_box.selection_clear(0, END)

    # Activate new song bar
    song_box.activate(next_one)

    # Set Active Bar to next song
    song_box.selection_set(next_one, last=None)

# Delete a song
def delete_song():
    # Delete currently selected song
    song_box.delete(ANCHOR)
    # Stop Music if it is playing
    pygame.mixer.music.stop()

# Delete all songs from playlist
def delete_all_songs():
     # Delete all songs132
    song_box.delete(0, END)
    # Stop Music if it is playing
    pygame.mixer.music.stop()

# Create Global Pause Variable
global paused
paused = False

# Pause and Unpause the current song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

   

#Create Playlist Box
song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)


# Define Player Control Buttons Images
back_btn_img = PhotoImage(file='D:/Images/back.png')
forward_btn_img = PhotoImage(file='D:/Images/forward.png')
play_btn_img = PhotoImage(file='D:/Images/play.png')
pause_btn_img = PhotoImage(file='D:/Images/pause.png')
stop_btn_img = PhotoImage(file='D:/Images/stop.png')

# Create Player Contol Frame 
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0) 
forward_button.grid(row=0, column=1) 
play_button.grid(row=0, column=2) 
pause_button.grid(row=0, column=3) 
stop_button.grid(row=0, column=4) 

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
#Add many songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Create Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song from playlist", command=delete_song)
remove_song_menu.add_command(label="Delete all songs from playlist", command=delete_all_songs)

root.mainloop()