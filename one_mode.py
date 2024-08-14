import tkinter as tk
from PIL import Image, ImageTk  
import video_library as lib  # Assuming this module contains the necessary video-related functions

class CombineVideoApp:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Single Gui Window")
        window.configure(bg="#0C2D48")

        # Create the frames for Update Video and Create Video Playlist
        update_frame = tk.Frame(window, bg="lightblue", bd=5)
        update_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        create_list_frame = tk.Frame(window, bg="pink", bd=5)
        create_list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Update Video Section
        self.update_video_section(update_frame)
        
        # Create Video List Section
        self.create_video_list_section(create_list_frame)
        
        # Placeholder for image label to display video images
        self.image_label = tk.Label(create_list_frame, bg="pink")
        self.image_label.pack(pady=10)

    def update_video_section(self, frame):
        tk.Label(frame, text="Update Video", bg="lightblue", font=("Arial", 14)).pack(pady=10)
        tk.Label(frame, text="Video Number:", bg="lightblue").pack(pady=5)
        self.video_number_entry = tk.Entry(frame)
        self.video_number_entry.pack(pady=5)
        
        tk.Label(frame, text="New Rating:", bg="lightblue").pack(pady=5)
        self.new_rating_entry = tk.Entry(frame)
        self.new_rating_entry.pack(pady=5)
        
        tk.Button(frame, text="Update Video", command=self.update_video, bg="lightgreen").pack(pady=10)
        
        self.update_status_lbl = tk.Label(frame, text="", bg="lightblue", font=("Arial", 10))
        self.update_status_lbl.pack(pady=5)

    def create_video_list_section(self, frame):
        tk.Label(frame, text="Create Video Playlist", bg="pink", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(frame, text="Video Number:", bg="pink").pack(pady=5)
        self.create_video_number_entry = tk.Entry(frame)
        self.create_video_number_entry.pack(pady=5)
        
        tk.Button(frame, text="Add Video to Playlist", command=self.add_video, bg="lightcoral").pack(pady=10)
        
        self.playlist_display = tk.Text(frame, height=10, width=50)
        self.playlist_display.pack(pady=10)
        
        tk.Button(frame, text="Play Playlist", command=self.play_playlist, bg="lightgreen").pack(pady=5)
        tk.Button(frame, text="Reset Playlist", command=self.reset_playlist, bg="lightblue").pack(pady=5)
        
        self.create_status_lbl = tk.Label(frame, text="", bg="pink", font=("Arial", 10))
        self.create_status_lbl.pack(pady=5)

    def update_video(self):
        video_number = self.video_number_entry.get()
        new_rating = self.new_rating_entry.get()

        if video_number in lib.library:
            lib.set_rating(video_number, new_rating)
            self.update_status_lbl.configure(text=f"Updated video {video_number} to rating {new_rating}")
        else:
            self.update_status_lbl.configure(text=f"Invalid video number: {video_number}")

    def add_video(self):
        video_number = self.create_video_number_entry.get().zfill(2)  # Ensure the key is zero-padded to 2 digits
        
        if video_number in lib.library:
            video_name = lib.get_name(video_number)
            self.playlist_display.insert(tk.END, f"{video_name}\n")
            self.create_status_lbl.configure(text=f"Video '{video_name}' added to playlist")
            
            # Load and display the corresponding image
            self.display_video_image(video_number)
        else:
            self.create_status_lbl.configure(text=f"Invalid video number: {video_number}")

    def display_video_image(self,video_number):
        image_path = f"Video_{video_number}.jpg"
        width = 200
        height = 200
        self.display_image(image_path, width, height)

    def display_image(self, image_path, width, height):
        image = Image.open(image_path)
        image = image.resize((width, height), Image.Resampling.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def play_playlist(self):
        playlist = self.playlist_display.get("1.0", tk.END).strip().split("\n")
        for video_name in playlist:
            for key, item in lib.library.items():
                if item.name == video_name:
                    lib.increment_play_count(key)
        self.create_status_lbl.configure(text="Playlist played (simulated). Play counts incremented.")

    def reset_playlist(self):
        self.playlist_display.delete(1.0, tk.END)
        self.create_status_lbl.configure(text="Playlist reset")
        self.image_label.configure(image='')  # Clear the image display

if __name__ == "__main__":
    window = tk.Tk()
    app = CombineVideoApp(window)
    window.mainloop()
