# QRcodeGenWin
Simple QRcode Generator Tool for Windows

## Dependencies:
- Pillow
- qrcode
- python-slugify, unicode_slugify
- pywin32
- pyinstaller (for EXE creation)

`pip3 install qrcode Pillow unicode_slugify python-slugify pywin32 pyinstaller`

## Build as Windows-EXE (using pyinstaller):
- http://www.pyinstaller.org/

Please use a virtual environment to create the app, otherwise all libraries installed on the system will be bundled into the application.

`pyinstaller -F --noconsole qrcode-tkinter.py`
