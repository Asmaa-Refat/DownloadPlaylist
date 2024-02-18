import tkinter 
from tkinter import filedialog
from pytube import Playlist, YouTube

def choose_folder():
    path = filedialog.askdirectory()
    chosen_path.set(path)

def download_playlist():
    playlist_url = entry_url.get()
    path = chosen_path.get()
    
    if not playlist_url:
        label_status.config(text="Please enter a playlist URL!", fg="red")
        return

    if not path:
        label_status.config(text="Please choose a folder to save the videos!", fg="red")
        return

    try:
        playlist = Playlist(playlist_url)
        for video_url in playlist.video_urls:
            video = YouTube(video_url)
            video.streams.get_highest_resolution().download(output_path=path)
        
        label_status.config(text="download completed! 🎉🎉🥳🥳", fg="green")
        main_window.after(2000, main_window.destroy)  # Close the window after 2 seconds
    except Exception as e:
        label_status.config(text="Sorry, An error occurred: " + str(e), fg="red")

# Creating the main window
main_window = tkinter.Tk()
main_window.title("Welcome to the YouTube Playlist Downloader! 🎥")

# Creating and placing widgets
label_url = tkinter.Label(main_window, text="Enter YouTube Playlist URL:")
label_url.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_url = tkinter.Entry(main_window, width=60)
entry_url.grid(row=0, column=1, padx=5, pady=5)

browse_button = tkinter.Button(main_window, text="Choose Folder", command=choose_folder)
browse_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# creating a variable to hold the choosen path of the folder
chosen_path = tkinter.StringVar()
chosen_path.set("") 

start = tkinter.Button(main_window, text="Start Downloading", command=download_playlist)
start.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

label_status = tkinter.Label(main_window, text="", fg="black") 
label_status.grid(row=3, column=0, columnspan=2, padx=5, pady=5) 

# Start the GUI event loop
main_window.mainloop()
