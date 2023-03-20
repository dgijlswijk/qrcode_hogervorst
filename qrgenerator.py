import qrcode
import PIL
from PIL import ImageFont
import os
import time

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# file_path = filedialog.asksaveasfile(defaultextension=".png", filetypes=(("png file", "*.png"),("All Files", "*.*") ))

servicenummer = tk.simpledialog.askstring("Servicenummer", "Servicenummer: ",)

qr = qrcode.QRCode(
    #version=1, #integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('mailto:contact@hogervorst.nl?subject=Servicenummer: ' + str(servicenummer) + '&body=Mijn vraag is%3A' )
qr.make()

img = qr.make_image(fill_color="black", back_color="white")

img = img.resize((180, 180))

im = PIL.Image.new(mode="RGB", size=(490, 180), color=(255,255,255))
im.paste(img, (0, 0))

image_editable = PIL.ImageDraw.Draw(im)
    
font = ImageFont.truetype("files/Gidole-Regular.ttf", size=90)
image_editable.text((245,40), str(servicenummer), fill=(0, 0, 0), font=font)

# im.save(file_path.name)
im.show()