# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:04:00 2018

@author: Dennis Heitmann
"""
import tkinter
import qrcode
from PIL import Image
from PIL import ImageTk
import io
import time
import slugify
import win32clipboard

class qrcodeApp(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    def initialize(self):
        pass

def makeQrcode(barstring='www.dennisheitmann.de'):
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=8, border=2)
    qr.add_data(barstring)
    qr.make(fit=True)
    qrimage = qr.make_image()
    if barstring != 'www.dennisheitmann.de':
        time_now = time.strftime('%Y%m%d-%H%M%S_')
        file_name = str(time_now) + slugify.slugify(barstring) + "_qr.png"
        try:
            qrimage.save(file_name)
        except:
            pass
        try:
            send_to_clipboard(qrimage)
        except:
            pass
    qrimageBild = ImageTk.PhotoImage(qrimage)
    return qrimageBild

def evaluate(event=None):
    try:
        image = makeQrcode(str(app.entry.get()))
        qrcode_bild.configure(image=image)
        qrcode_bild.image = image
    except:
        pass

def send_to_clipboard(data):
    output = io.BytesIO()
    data.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

if __name__ == "__main__":
    app = qrcodeApp(None)
    app.title('Dennis QRcode generator')
    app.entry = tkinter.Entry(app)
    app.entry.bind("<Return>", evaluate)
    app.entry.pack()
    button = tkinter.Button(app, text=u"Absenden!", command=evaluate)
    button.pack()
    image = makeQrcode()
    qrcode_bild = tkinter.Label(app, image=image)
    qrcode_bild.pack()
    app.mainloop()
    
