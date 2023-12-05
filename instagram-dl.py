# Instagram Profile Downloader
# Version 0.0.1
# Created by Hedgerow512

import tkinter as tk
from tkinter import ttk, filedialog
import configparser
import os

# Initialize a configuration parser
config = configparser.ConfigParser()

# Check if the configuration file exists
if os.path.exists('config.ini'):
    config.read('config.ini')
else:
    # If the configuration file doesn't exist, create it with a default directory
    config['Settings'] = {'SaveDirectory': ''}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def save_config():
    # Save the current configuration to the file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def initiate_command():
    user = username_entry.get()
    browser = cookies_var.get()
    save_directory = save_directory_var.get()

    # Get the state of each checkbox
    stories_checked = stories_var.get()
    posts_checked = posts_var.get()
    reels_checked = reels_var.get()
    tagged_checked = tagged_var.get()
    highlights_checked = highlights_var.get()

    media_grab = ""
    if stories_checked:
        media_grab += ",stories"
    if posts_checked:
        media_grab += ",posts"
    if reels_checked:
        media_grab += ",reels"
    if tagged_checked:
        media_grab += ",tagged"
    if highlights_checked:
        media_grab += ",highlights"
    if len(media_grab) <= 1:
        print("Invalid")
    else:
        media_list = media_grab[1:]
        media_grab = media_list.split(',')

    if browser == "none":
        browser_cookie_import = " "
    else:
        browser_cookie_import = " --cookies-from-browser " + browser + " "

    o = "-o include="
    save_dir = "-D " + save_directory + "/" + user + "/"
    for media in media_grab:
        command = "gallery-dl" + browser_cookie_import + o + media + " " + save_dir + media + " " + "https://www.instagram.com/" + user
        print(f"Now downloading {media} from @{user}")
        os.system(command)

def browse_save_directory():
    directory = filedialog.askdirectory()
    save_directory_var.set(directory)
    config['Settings']['SaveDirectory'] = directory
    save_config()

# Create the main application window
app = tk.Tk()
app.title("Instagram Profile Downloader")
app.geometry("475x200")
app.resizable(False, False)

# Main frame
main_frame = tk.Frame(app)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Center alignment

# Import cookies dropdown
cookies_label = tk.Label(main_frame, text="Import Cookies:")
cookies_label.grid(row=0, column=0, pady=(0, 10))

cookies_options = ["none", "brave", "chrome", "chromium", "edge", "firefox", "safari"]
cookies_var = tk.StringVar(value=cookies_options[0])

cookies_dropdown = ttk.Combobox(main_frame, textvariable=cookies_var, values=cookies_options, state="readonly")
cookies_dropdown.grid(row=0, column=1, pady=(0, 10))

# Save directory prompt
save_directory_label = tk.Label(main_frame, text="Save Directory:")
save_directory_label.grid(row=1, column=0, pady=(0, 0))

save_directory_var = tk.StringVar()
save_directory_var.set(config['Settings']['SaveDirectory'])
save_directory_entry = tk.Entry(main_frame, textvariable=save_directory_var)
save_directory_entry.grid(row=1, column=1, pady=(0, 0))

browse_button = tk.Button(main_frame, text="...", command=browse_save_directory)
browse_button.grid(row=1, column=2, pady=(0, 0))

# Username prompt
username_label = tk.Label(main_frame, text="Username (exclude @):")
username_label.grid(row=2, column=0, pady=(0, 0))

username_entry = tk.Entry(main_frame)
username_entry.grid(row=2, column=1, pady=(0, 0))

# Media to download checkboxes
checkbox_frame = tk.Frame(main_frame)
checkbox_frame.grid(row=3, column=0, columnspan=2, pady=10)

stories_var = tk.IntVar()
stories_checkbox = tk.Checkbutton(checkbox_frame, variable=stories_var, text="Stories")
stories_checkbox.grid(row=0, column=0)

posts_var = tk.IntVar()
posts_checkbox = tk.Checkbutton(checkbox_frame, variable=posts_var, text="Posts")
posts_checkbox.grid(row=0, column=1)

reels_var = tk.IntVar()
reels_checkbox = tk.Checkbutton(checkbox_frame, variable=reels_var, text="Reels")
reels_checkbox.grid(row=0, column=2)

tagged_var = tk.IntVar()
tagged_checkbox = tk.Checkbutton(checkbox_frame, variable=tagged_var, text="Tagged Media")
tagged_checkbox.grid(row=0, column=3)

highlights_var = tk.IntVar()
highlights_checkbox = tk.Checkbutton(checkbox_frame, variable=highlights_var, text="Highlights")
highlights_checkbox.grid(row=0, column=4)

# Initiate button
initiate_button = tk.Button(main_frame, text="Download Profile", command=initiate_command)
initiate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()
