import tkinter as tk
import video_library as lib  # Import the library module

class CreateVideoList:
    def __init__(self, window):
        self.playlist = []  # Initialize an empty playlist

        window.geometry("600x400")
        window.title("Create Video Playlist")

        # Set the background color of the window to pink
        window.configure(bg="pink")

        # Label for entering video number
        video_number_lbl = tk.Label(window, text="Video Number:", bg="pink")
        video_number_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="E")

        # Entry for video number
        self.video_number_entry = tk.Entry(window, width=10)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to add video to the playlist
        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked, bg="lightcoral")
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        # Text area to display the playlist
        self.playlist_display = tk.Text(window, height=10, width=50)
        self.playlist_display.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Button to play the playlist
        play_playlist_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked, bg="lightgreen")
        play_playlist_btn.grid(row=2, column=0, padx=10, pady=10)

        # Button to reset the playlist
        reset_playlist_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked, bg="lightblue")
        reset_playlist_btn.grid(row=2, column=1, padx=10, pady=10)

        # Status label to show success or error messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="pink")
        self.status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def add_video_clicked(self):
        video_key = self.video_number_entry.get().zfill(2)  # Ensure the key is zero-padded to 2 digits
        
        if video_key in lib.library:
            video_name = lib.get_name(video_key)
            self.playlist.append(video_name)
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Video '{video_name}' added to playlist")
        else:
            self.status_lbl.configure(text=f"Invalid video number: {video_key}")

        self.video_number_entry.delete(0, tk.END)

    def play_playlist_clicked(self):
        for video_name in self.playlist:
            for key, item in lib.library.items():
                if item.name == video_name:
                    lib.increment_play_count(key)

        self.status_lbl.configure(text="Playlist played (simulated). Play counts incremented.")

    def reset_playlist_clicked(self):
        self.playlist = []
        self.playlist_display.delete(1.0, tk.END)
        self.status_lbl.configure(text="Playlist reset")

    def update_playlist_display(self):
        self.playlist_display.delete(1.0, tk.END)
        for video in self.playlist:
            self.playlist_display.insert(tk.END, f"{video}\n")


if __name__ == "__main__":
    window = tk.Tk()
    CreateVideoList(window)
    window.mainloop()
