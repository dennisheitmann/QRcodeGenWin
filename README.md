# QRcodeGenWin
Simple QRcode Generator Tool for Windows

## Dependencies:
- https://pypi.python.org/pypi/qrcode
- https://pypi.python.org/pypi/python-slugify
- https://pypi.python.org/pypi/pywin32 or (https://github.com/mhammond/pywin32)

1) `pip3 install qrcode python-slugify pywin32`
2) in your PYTHONDIR: `python Scripts/pywin32_postinstall.py -install`

## Build as Windows-EXE (using pyinstaller):
- http://www.pyinstaller.org/

1) `pip3 install pyinstaller`
2) `pyinstaller -w -F qrcode-tkinter.py`
