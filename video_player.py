import tkinter as tk
from update_video import UpdateVideo
from create_video_list import CreateVideoList
from one_mode import CombineVideoApp
from check_videos import CheckVideos
from datetime import datetime

def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))

def create_videos_clicked():
    status_lbl.configure(text="Create Videos button was clicked!")
    CreateVideoList(tk.Toplevel(window))

def update_video_clicked():
    status_lbl.configure(text="Update Videos button was clicked!")
    UpdateVideo(tk.Toplevel(window))

def one_mode_clicked():
    status_lbl.configure(text="One Mode activated!")
    single_gui_window = tk.Toplevel(window)
    app = CombineVideoApp(single_gui_window)

def update_clock():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clock_lbl.configure(text=now)
    clock_lbl.after(1000, update_clock)

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        bg_color = "#121212"
        fg_color = "#FFFFFF"
        btn_bg_color = "#1F1F1F"
        btn_fg_color = "#BB86FC"
        theme_btn_text.set("Switch to Light Theme")
    else:
        bg_color = "#FFFFFF"
        fg_color = "#000000"
        btn_bg_color = "#E0E0E0"
        btn_fg_color = "#000000"
        theme_btn_text.set("Switch to Dark Theme")

    # Update window and widgets with new theme colors
    window.configure(bg=bg_color)
    header_lbl.configure(bg=bg_color, fg=fg_color)
    check_videos_btn.configure(bg=btn_bg_color, fg=btn_fg_color)
    create_video_list_btn.configure(bg=btn_bg_color, fg=btn_fg_color)
    update_videos_btn.configure(bg=btn_bg_color, fg=btn_fg_color)
    one_mode_btn.configure(bg=btn_bg_color, fg=btn_fg_color)
    status_lbl.configure(bg=bg_color, fg=fg_color)
    clock_lbl.configure(bg=bg_color, fg=fg_color)
    theme_btn.configure(bg=btn_bg_color, fg=btn_fg_color)

# Initialize main window
window = tk.Tk()
window.geometry("600x250")
window.title("Video Player")

# Initialize theme state
dark_mode = True

# Theme button text variable
theme_btn_text = tk.StringVar()
theme_btn_text.set("Switch to Light Theme")

# Create widgets
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_videos_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="Update Videos", command=update_video_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

one_mode_btn = tk.Button(window, text="One Mode", command=one_mode_clicked)
one_mode_btn.grid(row=1, column=3, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Adding the real-time clock
clock_lbl = tk.Label(window, font=("Helvetica", 10))
clock_lbl.grid(row=3, column=3, padx=10, pady=10)
update_clock()

# Adding the theme toggle button
theme_btn = tk.Button(window, textvariable=theme_btn_text, command=toggle_theme)
theme_btn.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Apply the initial theme
toggle_theme()

window.mainloop()