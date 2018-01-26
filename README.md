# QRcodeGenWin
Simple QRcode Generator Tool for Windows

- Dependencies:
https://pypi.python.org/pypi/qrcode
https://pypi.python.org/pypi/python-slugify
https://pypi.python.org/pypi/pywin32 (https://github.com/mhammond/pywin32)

1) pip3 install qrcode python-slugify pywin32
2) in PYTHONDIR: python Scripts/pywin32_postinstall.py -install

- Build as Windows-EXE:
pyinstaller -w -F qrcode-tkinter.py
