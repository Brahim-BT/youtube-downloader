import tkinter
import customtkinter
import yt_dlp
import threading


def show_download_status(message, success=True):
    status_window = customtkinter.CTkToplevel(app)
    status_window.title("Download Status")
    if success:
        status_label = customtkinter.CTkLabel(
            master=status_window,
            text=message,
            font=("Roboto", 16, "bold"),
            text_color="green",
        )
    else:
        status_label = customtkinter.CTkLabel(
            master=status_window,
            text=message,
            font=("Roboto", 16, "bold"),
            text_color="red",
        )
    status_label.pack(pady=12, padx=10)
    status_window.after(
        10000, lambda: status_window.destroy()
    )  # Close the window after 10 seconds


def download_video():
    try:
        ytLink = url.get()
        ydl_opts = {
            "format": "bestvideo+bestaudio",
            "subtitleslangs": ["en"],
            "outtmpl": "%(title)s.%(ext)s",
        }

        def download_video_thread():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([ytLink])
            show_download_status("Video downloaded successfully!", success=True)

        thread = threading.Thread(target=download_video_thread)
        thread.start()
    except Exception as e:
        show_download_status(f"Failed to download video: {e}", success=False)


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
