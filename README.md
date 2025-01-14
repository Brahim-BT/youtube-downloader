### Building the code to make it an executable file
First Install PyInstaller if not exist execute this command:
pip install pyinstaller
To build the code to make it an executable file, execute this command:
pyinstaller --onefile --windowed --icon=youtube-icon.ico --add-data "youtube-icon.ico;." --add-data "ffmpeg.exe;." --hidden-import yt_dlp main.py