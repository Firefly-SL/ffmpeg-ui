del __init__.py
pyinstaller main.py --noconsole --onefile --add-binary "ffmpeg.exe;." --name nameless_convertor
type nul > __init__.py