import tkinter as tk
import video_library as lib  # Import the library module

class UpdateVideo:
    def __init__(self, window):
        window.geometry("400x200")
        window.title("Update Video")

        # Set the background color of the window to blue
        window.configure(bg="lightblue")

        # Label for entering video number
        video_number_lbl = tk.Label(window, text="Video Number:", bg="lightblue")
        video_number_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="E")

        # Entry for video number
        self.video_number_entry = tk.Entry(window, width=10)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label for entering new rating
        rating_lbl = tk.Label(window, text="New Rating:", bg="lightblue")
        rating_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="E")

        # Entry for new rating
        self.rating_entry = tk.Entry(window, width=10)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # Button to update video information
        update_video_btn = tk.Button(window, text="Update Video", command=self.update_video_clicked, bg="deepskyblue")
        update_video_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Status label to show success or error messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="lightblue")
        self.status_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def update_video_clicked(self):
        # Retrieve data from the entry fields
        video_number = self.video_number_entry.get()
        try:
            new_rating = int(self.rating_entry.get())
        except ValueError:
            self.status_lbl.configure(text="Invalid rating")
            return

        # Update the library item if the video number is valid
        if video_number in lib.library:
            item = lib.library[video_number]
            item.rating = new_rating
            self.status_lbl.configure(text=f"Video '{item.name}' updated! Rating: {new_rating}, Plays: {item.play_count}")
        else:
            self.status_lbl.configure(text="Invalid video number")

        # Clear the entry fields
        self.video_number_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

if __name__ == "__main__":
    window = tk.Tk()
    UpdateVideo(window)
    window.mainloop()
