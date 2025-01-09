import tkinter
import customtkinter
import yt_dlp
from pytube import YouTube


def download_video():
    try:
        ytLink = url.get()
        ydl_opts = {
            "format": "bestvideo+bestaudio",
            "subtitleslangs": ["en"],
            "outtmpl": "%(title)s.%(ext)s",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytLink])
        customtkinter.CTkLabel(
            master=app, text="Downloaded successfully", font=("Roboto", 16, "bold")
        ).pack(pady=12, padx=10)
        print("Downloaded successfully")
    except Exception as e:
        print(f"Download failed: {e}")
        customtkinter.CTkLabel(
            master=app, text="Error Downloading Video", font=("Roboto", 16, "bold")
        ).pack(pady=12, padx=10)


# creating tkinter window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


# Heading
heading = customtkinter.CTkLabel(
    master=app, text="Insert Youtube Link", font=("Roboto", 24, "bold")
)
heading.pack(pady=12, padx=10)


# Input field
url = tkinter.StringVar()
input_field = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Youtube Link",
    width=500,
    height=40,
    corner_radius=8,
    textvariable=url,
)
input_field.pack(pady=12, padx=10)


# Download button
download_button = customtkinter.CTkButton(
    master=app,
    text="Download",
    command=download_video,
    width=200,
    height=40,
    corner_radius=8,
)
download_button.pack(pady=12, padx=10)

# Running app
app.mainloop()
