# QRcodeGenWin
Simple QRcode Generator Tool for Windows

## Dependencies:
- Pillow
- qrcode
- python-slugify, unicode_slugify
- pywin32 or (https://github.com/mhammond/pywin32)

1) `pip3 install Pillow qrcode python-slugify unicode_slugify pywin32`
2) in your PYTHONDIR: `python Scripts/pywin32_postinstall.py -install`

## Build as Windows-EXE (using pyinstaller):
- http://www.pyinstaller.org/

1) `pip3 install pyinstaller`
2) `pyinstaller -w -F qrcode-tkinter.py`
